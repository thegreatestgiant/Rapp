import sys
import os
import re
import fitz  # PyMuPDF
import requests
import argparse
import json
from datetime import date
from pathlib import Path

# --- Configuration & Paths ---
SCRIPT_DIR = Path(__file__).parent.resolve()
RAPP_ROOT = SCRIPT_DIR.parent
SOURCES_DIR = RAPP_ROOT / "333 Sources"
AUTHORS_DIR = RAPP_ROOT / "222 Authors"
SHEETS_DIR = RAPP_ROOT / "111 Source Sheets"
ATTACHMENTS_DIR = RAPP_ROOT / "444 Attachments"

# QWERTY-to-Hebrew mapping for PDFs with encoded Hebrew font streams
QWERTY_TO_HEBREW = {
    "a": "ש", "b": "נ", "c": "ב", "d": "ג", "e": "ק", "f": "כ", "g": "ע", "h": "י",
    "i": "ן", "j": "ח", "k": "ל", "l": "ך", "m": "צ", "n": "מ", "o": "ם", "p": "פ",
    "q": "/", "r": "ר", "s": "ד", "t": "א", "u": "ו", "v": "ה", "w": "׳", "x": "ס",
    "y": "ט", "z": "ז", ",": "ת", ".": "ץ", ";": "ף", '"': '"'
}

TANACH_BOOKS = [
    "בראשית", "שמות", "ויקרא", "במדבר", "דברים", "יהושע", "שופטים",
    "שמואל א", "שמואל ב", "מלכים א", "מלכים ב", "ישעיהו", "ירמיהו",
    "יחזקאל", "תרי עשר", "תהלים", "משלי", "איוב", "שיר השירים",
    "רות", "איכה", "קהלת", "אסתר", "דניאל", "עזרא", "נחמיה", "דברי הימים"
]

KNOWN_AUTHORS = [
    'רמב"ם', 'הרמב"ם', 'רש"י', 'רמב"ן', 'הרמב"ן', 'תלמוד בבלי', 'תלמוד ירושלמי',
    'שולחן ערוך', 'משנה ברורה', 'בית יוסף', 'אגרות משה', 'שו"ת אגרות משה',
    'מהרש"א', 'רד"ק', 'אברבנאל', 'מצודת דוד', 'מלבי"ם', 'חזון איש', 'חתם סופר',
    'שו"ת חתם סופר', 'פתחי תשובה', 'באר היטב', 'רב פעלים', 'שו"ת רב פעלים',
    'אבני נזר', 'שו"ת אבני נזר', 'מגן אברהם', 'ביאור הלכה', 'ציץ אליעזר',
    'שו"ת ציץ אליעזר', 'שמירת שבת כהלכתה', 'מדרש תנחומא', 'תנחומא', 'ספרי',
    'בראשית רבה', 'במדבר רבה', 'קהלת רבה', 'מדרש רבה', 'מדרש תהלים', 'זוהר',
    'הגרמ"צ ברגמן', 'הגראי"ל שטיינמן', 'חכם צבי', 'שו"ת חכם צבי', 'מזרחי',
    'יוסף אומץ', 'אוצר המדרשים', 'ברוך שאמר'
]

def ensure_dirs():
    for d in [SOURCES_DIR, AUTHORS_DIR, SHEETS_DIR, ATTACHMENTS_DIR]:
        d.mkdir(parents=True, exist_ok=True)

def get_academic_metadata():
    today = date.today()
    month, day, year = today.month, today.day, today.year
    
    if month == 1 and day < 15:
        return 'Fall', str(year - 1), 'Final'
    elif month < 6 or (month == 6 and day < 15):
        test_target = 'Midterm' if month < 4 else 'Final'
        return 'Spring', str(year), test_target
    else:
        test_target = 'Midterm' if (month < 11 or (month == 11 and day < 20)) else 'Final'
        return 'Fall', str(year), test_target

def load_config():
    config_path = RAPP_ROOT / 'config.json'
    if config_path.exists():
        with open(config_path, 'r') as f:
            return json.load(f)
    return {'subjects': ['Gemara']}

def sanitize_filename(name):
    clean = name.replace('"', "''")
    clean = re.sub(r'[:\\/|?*<>]', '-', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean

COMMON_ENG_WORDS = {
    'the', 'of', 'and', 'in', 'to', 'a', 'is', 'that', 'for', 'it', 'as', 'was', 'with', 'by',
    'on', 'at', 'from', 'this', 'be', 'are', 'or', 'an', 'not', 'rabbi', 'rav', 'challenge',
    'science', 'judaism', 'letter', 'age', 'universe', 'kaplan', 'schwab', 'belsky', 'einei',
    'yisroel', 'translated', 'immortality', 'resurrection', 'kabbalistic', 'view', 'perspective',
    'february', 'torah', 'printed', 'translation', 'how', 'old', 'pp', 'page', 'bereishis'
}

def is_line_english(line):
    words = [re.sub(r'[^a-zA-Z]', '', w).lower() for w in line.split()]
    words = [w for w in words if w]
    if not words:
        return False
    eng_matches = sum(1 for w in words if w in COMMON_ENG_WORDS)
    return (eng_matches / len(words)) >= 0.25 or any(w in {'rabbi', 'challenge', 'universe', 'kaplan', 'schwab', 'belsky'} for w in words)

def decode_line(line):
    if not any(c in "abcdefghijklmnopqrstuvwxyz\x1b" for c in line.lower()):
        return line
    if is_line_english(line):
        return line
    rev = line[::-1]
    res = [QWERTY_TO_HEBREW.get(ch, ch) for ch in rev]
    return "".join(res).replace('\x1b', '"')

def decode_text(text):
    if not text:
        return text
    lines = text.splitlines()
    return "\n".join(decode_line(l) for l in lines)

AUTHOR_CANONICAL_MAP = {
    'פירוש המשניות להרמב"ם': 'רמב"ם',
    'פירוש המשניות': 'רמב"ם',
    'ביאור הלכה': 'משנה ברורה',
    'שו"ת בית יהודה': 'רבי יהודה עייאש',
    "שו''ת בית יהודה": 'רבי יהודה עייאש',
    'שו"ת בית': 'רבי יהודה עייאש',
    "שו''ת בית": 'רבי יהודה עייאש',
    'ביאור': 'הגר"א',
    'ביאור הגר"א': 'הגר"א',
    "ביאור הגר''א": 'הגר"א',
    'ספר מנחת': 'מנחת חינוך',
    'קובץ': 'רבי אלחנן וסרמן',
    'קובץ שעורים': 'רבי אלחנן וסרמן',
    'מנחת אשר': 'רבי אשר וייס',
    'שו"ת מנחת אשר': 'רבי אשר וייס',
    "שו''ת מנחת אשר": 'רבי אשר וייס',
    'ספר החינוך': 'ספר החינוך',
    'חזון איש': 'חזון איש',
    'כלי יקר': 'כלי יקר',
    'משך': 'משך חכמה',
    'ספר מורה': 'רמב"ם',
    'ספר יערות': 'רבי יהונתן אייבשיץ',
    'רבי יעקב בן אשר - מקור': 'רבי יעקב בן אשר',
    'בית יוסף': 'בית יוסף',
    'שו"ת רדב"ז': 'רדב"ז',
    "שו''ת רדב''ז": 'רדב"ז',
    'ר\' עובדיה מברטנורא': 'רבי עובדיה מברטנורא',
    'ר׳ עובדיה מברטנורא': 'רבי עובדיה מברטנורא',
    'ברטנורא': 'רבי עובדיה מברטנורא',
    'הרמב"ם': 'רמב"ם',
    'הרמב"ן': 'רמב"ן',
    'הרא"ש': 'רא"ש',
    'הריטב"א': 'ריטב"א',
    'הרשב"א': 'רשב"א',
    'הר"ן': 'ר"ן',
    'הרי"ף': 'רי"ף',
    'חמדת שלמה': 'רבי שלמה זלמן ליפשיץ',
    'חשק שלמה': 'רבי שלמה הכהן מווילנה',
    'הערות הגרי"ש אלישיב': 'הרב יוסף שלום אלישיב',
    'בנין ציון': 'רבי יעקב עטלינגר',
    'ארץ צבי': 'רבי אריה צבי פרומר',
    'שיחות מוסר': 'רבי חיים שמואלביץ',
    'סדר הדורות': 'רבי יחיאל היילפרין',
    'ילקוט שמעוני': 'ילקוט שמעוני',
    'הגרי"ז הלוי': 'הגרי"ז הלוי',
    'הנצי"ב מולוז\'ין': 'הנצי"ב מולוז\'ין',
    'במדבר רבה': 'מדרש רבה',
    'רות רבה': 'מדרש רבה',
    'העמק דבר': 'הנצי"ב מולוז\'ין',
    'זית רענן': 'מגן אברהם',
    'סוכת שלם': 'רבי שמריהו שולמן',
    'בית יעקב': 'רבי יעקב בן שמואל מצויזמיר',
    'שו"ת בית יעקב': 'רבי יעקב בן שמואל מצויזמיר',
    "שו''ת בית יעקב": 'רבי יעקב בן שמואל מצויזמיר',
    'שבות יעקב': 'רבי יעקב ריישר',
    'שו"ת שבות יעקב': 'רבי יעקב ריישר',
    "שו''ת שבות יעקב": 'רבי יעקב ריישר',
    'מהרש"ם': 'רבי שלום מרדכי שוודרון',
    'שו"ת מהרש"ם': 'רבי שלום מרדכי שוודרון',
    "שו''ת מהרש''ם": 'רבי שלום מרדכי שוודרון',
    'דברי מלכיאל': 'רבי מלכיאל צבי טננבוים',
    'שו"ת דברי מלכיאל': 'רבי מלכיאל צבי טננבוים',
    "שו''ת דברי מלכיאל": 'רבי מלכיאל צבי טננבוים',
    'שאילת שלום': 'רבי שלום טויבש',
    'שו"ת שאילת שלום': 'רבי שלום טויבש',
    "שו''ת שאילת שלום": 'רבי שלום טויבש',
    'יד המלך': 'רבי אלעזר לנדא',
    'אליהו רבה': 'רבי אליהו שפירא',
    'ספר אליהו רבה': 'רבי אליהו שפירא',
    'שואל ומשיב': 'רבי יוסף שאול נתנזון',
    'שו"ת שואל ומשיב': 'רבי יוסף שאול נתנזון',
    "שו''ת שואל ומשיב": 'רבי יוסף שאול נתנזון',
    'שדי חמד': 'רבי חיים חזקיהו מדיני',
    'שערי תשובה': 'רבי חיים מרדכי מרגליות',
    'המתיבתא תשנ"ו': 'רבי ישראל רייזמן',
    "המתיבתא תשנ''ו": 'רבי ישראל רייזמן',
    'ארבעת המינים השלם': 'רבי אליהו וייספיש',
    'טור': 'רבי יעקב בן אשר',
    'עיני ישראל': 'רבי ישראל בלסקי',
    'Einei Yisroel': 'רבי ישראל בלסקי',
    'Rav Yisroel Belsky': 'רבי ישראל בלסקי',
    'Rabbi Menachem M. Schneerson': 'הרבי מליובאוויטש',
    'רבי מנחם מענדל שניאורסון': 'הרבי מליובאוויטש',
    'הרבי מליובאוויטש': 'הרבי מליובאוויטש',
    'Rabbi Shimon Schwab': 'רבי שמעון שוואב',
    'Rabbi Aryeh Kaplan': 'רבי אריה קפלן',
    'The Age of the Universe': 'רבי אריה קפלן',
    'עולמות שחרבו': 'הרבי מסאטמאר',
    'רבי יואל טייטלבוים': 'הרבי מסאטמאר',
    'הרבי מסאטמאר': 'הרבי מסאטמאר',
    'אוצר החיים': 'רבי יצחק דמן עכו',
    'אבות דרבי נתן': 'אבות דרבי נתן',
    'מסכתות קטנות': 'אבות דרבי נתן',
    'מסכת אבות דרבי נתן': 'אבות דרבי נתן',
    'תפארת ישראל': 'רבי ישראל ליפשיץ',
    'דרוש אור החיים': 'רבי ישראל ליפשיץ',
    'יחווה דעת': 'רב עובדיה יוסף',
    'שו"ת יחווה דעת': 'רב עובדיה יוסף',
    "שו''ת יחווה דעת": 'רב עובדיה יוסף',
    'שו"ת יחווה': 'רב עובדיה יוסף',
    "שו''ת יחווה": 'רב עובדיה יוסף',
    'מנחת יצחק': 'רבי יצחק יעקב וייס',
    'שו"ת מנחת יצחק': 'רבי יצחק יעקב וייס',
    "שו''ת מנחת יצחק": 'רבי יצחק יעקב וייס',
    'מנחת שלמה': 'רבי שלמה זלמן אויערבאך',
    'שו"ת מנחת שלמה': 'רבי שלמה זלמן אויערבאך',
    "שו''ת מנחת שלמה": 'רבי שלמה זלמן אויערבאך',
    'הר צבי': 'רב צבי פסח פרנק',
    'שו"ת הר צבי': 'רב צבי פסח פרנק',
    "שו''ת הר צבי": 'רב צבי פסח פרנק',
    'משנת יעבץ': 'רב יעקב בצלאל זולטי',
    'משנת יעב"ץ': 'רב יעקב בצלאל זולטי',
    "משנת יעב''ץ": 'רב יעקב בצלאל זולטי',
    'יעקב בצלאל זולטי': 'רב יעקב בצלאל זולטי',
    "יעקב בצלאל ז'ולטי": 'רב יעקב בצלאל זולטי',
    "יעקב בצלאל ז''ולטי": 'רב יעקב בצלאל זולטי',
    'רוזובסקי': 'רבי שמואל רוזובסקי',
    'שמואל רוזובסקי': 'רבי שמואל רוזובסקי',
    'קונטרסי שעורים': 'רבי שמואל רוזובסקי',
    'קונטרס שיעורים': 'רבי שמואל רוזובסקי',
    'הלכה ברורה בירור הלכה': 'מכון הלכה ברורה',
    'הלכה ברורה ובירור הלכה': 'מכון הלכה ברורה',
    'בירור הלכה': 'מכון הלכה ברורה',
    'מכון הלכה ברורה': 'מכון הלכה ברורה'
}

def get_all_known_authors():
    authors = set(KNOWN_AUTHORS)
    if AUTHORS_DIR.exists():
        for f in AUTHORS_DIR.glob("*.md"):
            name = f.stem.replace("''", '"')
            authors.add(name)
    
    extras = [
        'רא"ש', 'הרא"ש', 'ריטב"א', 'הריטב"א', 'רשב"א', 'הרשב"א', 'תוספות', 'הר"ן', 'ר"ן', 
        'חלקת יואב', 'רבבות אפרים', 'דרוש וחדוש', 'מועדים בהלכה', 'רי"ף', 'הרי"ף', 'רש"י', 'הר צבי',
        'רבי עובדיה מברטנורא', 'ר\' עובדיה מברטנורא', 'ר׳ עובדיה מברטנורא', 'ברטנורא'
    ]
    for ex in extras:
        authors.add(ex)
        
    for k in AUTHOR_CANONICAL_MAP.keys():
        authors.add(k)
        
    # Remove some generic prefixes that might have slipped into authors if we don't want them as strict authors
    bad = {'שו"ת', 'ספר', 'פ', 'חידושי', 'ערוך', 'תוספת', 'דרוש', 'חלקת', 'ר', "ר'", "ר׳", 'מקור'}
    for b in bad:
        if b in authors:
            authors.remove(b)
            
    return sorted(list(authors), key=len, reverse=True)

ALL_KNOWN_AUTHORS = get_all_known_authors()

def parse_citation(citation):
    c_str = citation.strip()
    audit_needed = False
    audit_reason = ""

    # 1. English citation heuristic parsing
    if is_line_english(c_str):
        c = re.sub(r'^\s*\(?\s*\d+[\)\.\-:]?\s*', '', c_str).strip()
        author = ""
        book = ""
        location = ""

        # Pattern A: Sefer/Title (Author) Location (e.g. Einei Yisroel (Rav Yisroel Belsky) Bereishis pp. 12-16)
        m = re.match(r'^([^(]+)\s*\(([^)]+)\)\s*(.*)$', c)
        if m:
            book = m.group(1).strip()
            author = m.group(2).strip()
            location = m.group(3).strip()
        else:
            # Pattern B: Title by Author Date/Location (e.g. THE AGE OF THE UNIVERSE ... By Rabbi Aryeh Kaplan February 18, 1979)
            m = re.search(r'^(.*?)\s+by\s+([A-Za-z\.\s\']+?)(?:\s+([A-Z][a-z]+ \d{1,2},? \d{4}|\b(?:pp?|vol|ch)\b.*|$))', c, re.IGNORECASE)
            if m:
                book = m.group(1).strip()
                author = m.group(2).strip()
                location = (m.group(3) or "").strip()
            else:
                # Pattern C: Author, Title, Location/Source (e.g. Rabbi Shimon Schwab, How old is the Universe?, Challenge p. 165)
                parts = [p.strip() for p in re.split(r'[,;]\s*', c) if p.strip()]
                if len(parts) >= 2:
                    author = parts[0]
                    if len(parts) >= 3 and re.search(r'\b(?:p\.|pp\.|page|vol\.|ch\.|§)\b', parts[-1], re.IGNORECASE):
                        location = parts[-1]
                        book = ", ".join(parts[1:-1])
                    else:
                        book = ", ".join(parts[1:])
                else:
                    author = c
                    audit_needed = True
                    audit_reason = "Unrecognized English citation structure"

        # Resolve through canonical map
        canonical_author = AUTHOR_CANONICAL_MAP.get(author, AUTHOR_CANONICAL_MAP.get(book, author))
        if canonical_author != author or canonical_author in ALL_KNOWN_AUTHORS:
            author = canonical_author
        else:
            audit_needed = True
            audit_reason = f"English author '{author}' not in canonical author database"

        return author, book, location, audit_needed, audit_reason

    # 2. Hebrew citation heuristic parsing
    clean = re.sub(r'^\s*\(?\s*\d+[\)\.\-:]?\s*', '', citation)
    clean = re.sub(r'^[א-ת]\s*-\s*', '', clean)
    clean = re.sub(r'^מקור\s*-\s*', '', clean)
    clean = re.sub(r'^סוכת\s*-\s*', '', clean)
    clean = re.sub(r'^Succos\s*-\s*', '', clean, flags=re.IGNORECASE)
    clean = re.sub(r'^Makor\s*-\s*', '', clean, flags=re.IGNORECASE)
    clean = re.sub(r'[\(\)][^\(\)]*[\(\)]', '', clean)
    clean = re.sub(r'\([^)]*\)', '', clean)
    clean = re.sub(r'\)[^(]*\(', '', clean)
    clean = re.sub(r'\[[^\]]*\]', '', clean)
    clean = re.sub(r'\][^\[]*\[', '', clean)
    clean = re.sub(r"[()\[\]]", "", clean)
    clean = re.sub(r"\b\d+[\)\(]|\([\)\d]+", "", clean)
    clean = re.sub(r"^\s*\d+[\)\.]?\s*", "", clean)
    clean = re.sub(r"\s*[\(\-]?[\s]*\d+\s*[\)]?\s*$", "", clean)
    clean = re.sub(r"^[א-ת]\"?[א-ת]?\s*[\)\.\-]\s*", "", clean)
    if not re.search(r"פירוש המשניות", clean):
        clean = re.sub(r"^(פ['׳]|פי['׳]|פירוש)\s*", "", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    # Check for known responsa sefarim where book title implies author
    RESPONSA_SPECIAL_MAP = {
        'יחווה דעת': ('רב עובדיה יוסף', 'שו"ת יחווה דעת'),
        'מנחת יצחק': ('רבי יצחק יעקב וייס', 'שו"ת מנחת יצחק'),
        'מנחת שלמה': ('רבי שלמה זלמן אויערבאך', 'שו"ת מנחת שלמה'),
        'הר צבי': ('רב צבי פסח פרנק', 'הר צבי'),
        'משנת יעבץ': ('רב יעקב בצלאל זולטי', 'משנת יעב"ץ'),
        'משנת יעב"ץ': ('רב יעקב בצלאל זולטי', 'משנת יעב"ץ'),
        "משנת יעב''ץ": ('רב יעקב בצלאל זולטי', 'משנת יעב"ץ'),
        'קונטרסי שעורים': ('רבי שמואל רוזובסקי', 'קונטרסי שעורים'),
        'קונטרס שיעורים': ('רבי שמואל רוזובסקי', 'קונטרסי שעורים'),
        'הלכה ברורה בירור הלכה': ('מכון הלכה ברורה', 'בירור הלכה'),
        'הלכה ברורה ובירור הלכה': ('מכון הלכה ברורה', 'בירור הלכה'),
        'בירור הלכה': ('מכון הלכה ברורה', 'בירור הלכה'),
    }
    for sefer_key, (resp_author, resp_book) in RESPONSA_SPECIAL_MAP.items():
        resp_pat = r'^(?:שו"ת\s+|שו\'\'ת\s+)?' + re.escape(sefer_key)
        m_resp = re.search(resp_pat, clean)
        if m_resp:
            author = resp_author
            rest = clean[m_resp.end():].strip()
            loc_match = re.search(r'(חלק\s+[א-ת0-9\']+|או"ח\s+[א-ת0-9\']+|או\'\'ח\s+[א-ת0-9\']+|יו"ד\s+[א-ת0-9\']+|יו\'\'ד\s+[א-ת0-9\']+|אבהע"ז|חו"מ|בבא\s+[א-ת]+|דף|פרק|סימן|פסוק|סעיף|מאמר|אות|טור|ס"ק|ס[\'׳]|ס׳|ס\'|ד"ה|משנה|פיסקא|שיעור|שעור|ח"א|ח"ב|ח"ג|ח"ד).*', rest)
            if loc_match:
                location = loc_match.group(0).strip()
                extra_book = rest[:loc_match.start()].strip()
                book = f"{resp_book} {extra_book}".strip()
            else:
                location = rest
                book = resp_book
            return author, book, location, False, None

    author = None
    matched_text = None
    matches = []
    
    # Sort authors by length descending so longer authors match first
    sorted_authors = sorted(ALL_KNOWN_AUTHORS, key=len, reverse=True)
    for a in sorted_authors:
        pattern = r'(?<![א-ת])' + re.escape(a) + r'(?![א-ת])'
        if re.search(pattern, clean):
            matches.append(a)
            
    if matches:
        best_match = matches[0]
        matched_text = best_match
        author = best_match.replace('שו"ת ', '')
        author = AUTHOR_CANONICAL_MAP.get(author, AUTHOR_CANONICAL_MAP.get(best_match, author))

    loc_match = re.search(r"(דף|פרק|סימן|פסוק|סעיף|מאמר|אות|טור|ס\"ק|ס['׳]|ד\"ה|משנה|פיסקא|ח\"א|ח\"ב|ח\"ג|ח\"ד).*", clean)
    if loc_match:
        location = loc_match.group(0).strip()
        book_part = clean[:loc_match.start()].strip()
    else:
        location = ""
        book_part = clean

    if matched_text and book_part.startswith(matched_text):
        book_part = book_part[len(matched_text):].strip()
    elif author and book_part.startswith(author):
        book_part = book_part[len(author):].strip()
    elif author and ('שו"ת ' + author) in book_part:
        book_part = book_part.replace('שו"ת ' + author, "").strip()

    book = re.sub(r"^[-\s:;]+|[-\s:;]+$", "", book_part).strip()

    if matched_text in ["פירוש המשניות להרמב\"ם", "פירוש המשניות"]:
        author = "רמב\"ם"
        book = "פירוש המשניות"
    elif matched_text == "ביאור הלכה":
        author = "משנה ברורה"
        book = "ביאור הלכה"

    if not author:
        for tb in TANACH_BOOKS:
            pattern = r'^(ספר\s+|חומש\s+)?' + re.escape(tb) + r'(?![א-ת])'
            if re.search(pattern, clean):
                author = 'תנ"ך'
                if not book:
                    book = tb
                break

    if not author:
        words = book.split()
        if len(words) > 1 and words[0] in ['שו"ת', "שו''ת", 'חידושי', 'ספר', 'פ', 'פירוש', 'דרוש', 'חלקת', 'ערוך', 'תוספת', 'קונטרס']:
            author = " ".join(words[:2])
            book = " ".join(words[2:]).strip()
        elif words and words[0] not in ["ר'", "ר׳", "ר"]:
            author = words[0]
            book = " ".join(words[1:]).strip()
        else:
            author = "מקור"
        audit_needed = True
        audit_reason = f"Author fell back to token '{author}'"

    # Check for possible gibberish or corrupt font stream
    if re.search(r'\b[A-Za-z]{3,}\b', clean):
        audit_needed = True
        audit_reason = "Suspicious ASCII non-words / font stream in citation"

    # Fix Shulchan Aruch / Tur Chelek topics
    for chelek in ["אורח חיים", "יורה דעה", "אבן העזר", "חושן משפט"]:
        if book.startswith(chelek + " הלכות"):
            book = chelek
            break

    if not book or book == "מקור":
        if author == "משנה ברורה":
            book = "משנה ברורה"
        elif author == "רבי חיים חזקיהו מדיני":
            book = "שדי חמד"
        else:
            book = "מקור"

    location = re.sub(r"\s*\d+[\)\(]?$", "", location).strip()

    return author, book, location, audit_needed, audit_reason

import difflib

def normalize_text_for_match(t):
    return re.sub(r'[^\wא-ת]', '', t)

def get_normalized_location(t):
    t = re.sub(r'[^\wא-ת]', '', t)
    t = t.replace('עמודב', 'עב').replace('עמודא', 'עא')
    return t

def match_existing_source(author, book, location):
    display_author = sanitize_filename(author)[:60].strip()
    display_book = sanitize_filename(book)[:60].strip()
    display_loc = sanitize_filename(location)[:60].strip()
    title_parts = [display_author]
    if display_book and display_book != display_author:
        title_parts.append(display_book)
    if display_loc:
        title_parts.append(display_loc)
    direct_base = " - ".join(title_parts)
    if len(direct_base) > 100:
        direct_base = direct_base[:100].strip()
    direct_file = SOURCES_DIR / f"{direct_base}.md"
    if direct_file.exists():
        return direct_file

    norm_author = normalize_text_for_match(author)
    norm_loc = get_normalized_location(location)
    norm_book = normalize_text_for_match(book)
    
    existing_files = list(SOURCES_DIR.glob("*.md"))
    
    for f in existing_files:
        stem = f.stem
        parts = stem.split(" - ")
        if len(parts) >= 3:
            ex_author = parts[0]
            ex_book = " - ".join(parts[1:-1])
            ex_loc = parts[-1]
            
            if normalize_text_for_match(ex_author) == norm_author:
                if get_normalized_location(ex_loc) == norm_loc:
                    if difflib.SequenceMatcher(None, norm_book, normalize_text_for_match(ex_book)).ratio() >= 0.7:
                        return f
        elif len(parts) == 2:
            ex_author = parts[0]
            ex_loc = parts[1]
            if normalize_text_for_match(ex_author) == norm_author:
                if get_normalized_location(ex_loc) == norm_loc:
                    return f
                        
    return None

KNOWN_HEADER_KEYWORDS = [
    "תלמוד בבלי", "תלמוד ירושלמי", "רש\"י", "רמב\"ם", "משנה ברורה", "שולחן ערוך", "רא\"ש",
    "בית יוסף", "ביאור הלכה", "מגן אברהם", "טור", "ספרי", "מדרש", "פסיקתא", "בראשית רבה",
    "במדבר רבה", "קהלת רבה", "אגרות משה", "חזון איש", "חתם סופר", "אבני נזר", "פתחי תשובה",
    "ציץ אליעזר", "שמירת שבת כהלכתה", "ערוך השולחן", "פרי מגדים", "תוספות", "ריטב\"א",
    "רשב\"א", "ר\"ן", "רי\"ף", "פירוש המשניות"
]

def extract_sources_and_images(pdf_path):
    doc = fitz.open(pdf_path)
    sources = []

    # Detect if document has numbered headers across pages
    has_numbered_doc = False
    for p in doc:
        for b in p.get_text("blocks"):
            for l in [line.strip() for line in b[4].strip().splitlines() if line.strip()]:
                if re.search(r'^\(?\s*\d{1,2}\s*[\)\.\-:]', l) or re.search(r'\(?\s*\d{1,2}\s*\)?$', l) or re.search(r'\b\d{1,2}\s*\)', l):
                    has_numbered_doc = True
                    break
            if has_numbered_doc:
                break
        if has_numbered_doc:
            break

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("blocks")

        is_ocr = False
        if not blocks or sum(len(b[4].strip()) for b in blocks) < 10:
            try:
                print(f"No text stream found on page {page_num+1}. Running OCR fallback...")
                ocr_tp = page.get_textpage_ocr(dpi=300, language="heb+eng")
                blocks = ocr_tp.extractBLOCKS()
                is_ocr = True
            except Exception as e:
                print(f"OCR fallback failed on page {page_num+1}: {e}")

        headers = []
        for b in blocks:
            raw = b[4].strip()
            if not raw:
                continue
            raw_decoded = decode_text(raw) if not is_ocr else raw
            lines = [l.strip() for l in raw.splitlines() if l.strip()]
            has_num_prefix = any(
                re.search(r'^\(?\s*\d{1,2}\s*[\)\.\-:]', l) or 
                re.search(r'\(?\s*\d{1,2}\s*\)?$', l) or
                re.search(r'\b\d{1,2}\s*\)', l)
                for l in lines
            )
            has_special_num = any(re.search(r'\b13\b', l) and ('Translation' in l or 'Challenge' in l) for l in lines) or any('16)' in l and ('Translated' in l or 'Kaplan' in l) for l in lines)
            is_kw = any(kw in raw_decoded for kw in KNOWN_HEADER_KEYWORDS)
            
            is_header = False
            if len(raw) < 350:
                if has_numbered_doc:
                    is_header = has_num_prefix or has_special_num
                else:
                    is_header = has_num_prefix or has_special_num or (is_kw and b[1] > 30 and len(raw_decoded) < 150)

            if is_header:
                headers.append(b)

        headers.sort(key=lambda b: b[1])

        if page_num > 0 and sources and headers:
            top_y = headers[0][1] - 5
            top_blocks = [b for b in blocks if b[3] <= top_y + 10]
            # filter out standalone short running headers (e.g. single-line header like הלכות ציצית)
            content_blocks = [b for b in top_blocks if len((b[4] if is_ocr else decode_text(b[4])).strip().splitlines()) > 1 or len((b[4] if is_ocr else decode_text(b[4])).strip()) > 20]
            if content_blocks:
                min_y = max(30, min(b[1] for b in content_blocks) - 5)
                max_y = max(b[3] for b in content_blocks) + 5
                cont_rect = fitz.Rect(0, min_y, page.rect.width, max_y)
                pix = page.get_pixmap(clip=cont_rect, dpi=150)
                cont_img_name = sanitize_filename(f"{pdf_path.stem}_p{page_num+1}_cont.png")
                pix.save(str(ATTACHMENTS_DIR / cont_img_name))
                sources[-1]["image_filenames"].append(cont_img_name)

        for i, h in enumerate(headers):
            raw_header = h[4].strip()
            
            if re.match(r"^[\(\)\s\d]+$", raw_header):
                same_line_texts = []
                for b in blocks:
                    if b != h and abs(b[1] - h[1]) < 10:
                        same_line_texts.append(b[4].strip())
                if same_line_texts:
                    raw_header = " ".join(same_line_texts) + " " + raw_header

            if is_ocr:
                cleaned_h = re.sub(r'[A-Za-z]+', ' ', raw_header)
                decoded_header = cleaned_h.replace("\n", " ")
            else:
                decoded_header = decode_text(raw_header).replace("\n", " ")
            author, book, location, audit_needed, audit_reason = parse_citation(decoded_header)

            # If citation parsing flagged an issue or non-words, try OCR retry on the header before AI flagging
            if audit_needed and not is_ocr:
                try:
                    h_rect = fitz.Rect(h[0], max(0, h[1] - 5), h[2], min(page.rect.height, h[3] + 5))
                    ocr_h_tp = page.get_textpage_ocr(clip=h_rect, dpi=300, language="heb+eng", full=True)
                    ocr_header_text = ocr_h_tp.extractTEXT().strip().replace("\n", " ")
                    if ocr_header_text:
                        ocr_author, ocr_book, ocr_loc, ocr_audit, ocr_reason = parse_citation(ocr_header_text)
                        # If OCR produced a valid parse without needing audit, use it!
                        if not ocr_audit:
                            author, book, location, audit_needed, audit_reason = ocr_author, ocr_book, ocr_loc, False, None
                            decoded_header = ocr_header_text
                            print(f"OCR successfully resolved header: '{ocr_header_text}' -> Author: {author}, Book: {book}, Loc: {location}")
                        else:
                            # Even if still needing audit, if it got a cleaner author/book, adopt it
                            if ocr_author != "מקור" and not re.search(r'\b[A-Za-z]{3,}\b', ocr_header_text):
                                author, book, location = ocr_author, ocr_book, ocr_loc
                                decoded_header = ocr_header_text
                                audit_reason = f"OCR attempted; {ocr_reason}"
                except Exception as ocr_err:
                    print(f"Header OCR retry failed: {ocr_err}")

            dh = None
            try:
                block_idx = blocks.index(h)
                if block_idx + 1 < len(blocks):
                    first_line = blocks[block_idx+1][4].strip().split('\n')[0]
                    first_line_dec = first_line.strip() if is_ocr else decode_text(first_line).strip()
                    match = re.search(r'^(.*?)[\-\.](?:\s|$)', first_line_dec)
                    if match:
                        candidate = match.group(1).strip()
                        if len(candidate.split()) <= 8:
                            dh = candidate
                    elif first_line_dec.endswith('-') or first_line_dec.endswith('.'):
                        candidate = first_line_dec[:-1].strip()
                        if len(candidate.split()) <= 8:
                            dh = candidate
            except ValueError:
                pass

            y0 = max(0, h[1] - 5)
            if i + 1 < len(headers):
                y1 = headers[i+1][1] - 5
            else:
                max_b_y1 = max((b[3] for b in blocks), default=page.rect.height)
                y1 = min(page.rect.height, max_b_y1 + 5)

            clip_rect = fitz.Rect(0, y0, page.rect.width, y1)
            pix = page.get_pixmap(clip=clip_rect, dpi=150)

            main_img_name = sanitize_filename(f"{pdf_path.stem}_p{page_num+1}_s{i+1}.png")
            pix.save(str(ATTACHMENTS_DIR / main_img_name))

            sources.append({
                "author": author,
                "book": book,
                "location": location,
                "header": decoded_header,
                "dibur_hamatchil": dh,
                "image_filenames": [main_img_name],
                "audit_needed": audit_needed,
                "audit_reason": audit_reason
            })

    return sources
def process_source(source_data, sheet_stem, subject, seen_in_sheet=None):
    author = source_data["author"]
    book = source_data["book"]
    location = source_data["location"]
    dh = source_data.get("dibur_hamatchil")
    img_names = source_data["image_filenames"]

    display_author = sanitize_filename(author)[:60].strip()
    display_book = sanitize_filename(book)[:60].strip()
    display_loc = sanitize_filename(location)[:60].strip()

    title_parts = [display_author]
    if display_book and display_book != display_author:
        title_parts.append(display_book)
    if display_loc:
        title_parts.append(display_loc)

    file_base = " - ".join(title_parts)
    if len(file_base) > 100:
        file_base = file_base[:100].strip()
    file_name = f"{file_base}.md"
    
    heading_to_use = dh if dh else file_base

    existing_file = match_existing_source(author, book, location)

    if existing_file and existing_file.exists():
        existing_stem = existing_file.stem
        times_used = seen_in_sheet.get(existing_stem, 0) if seen_in_sheet is not None else 0
        if seen_in_sheet is not None:
            seen_in_sheet[existing_stem] = times_used + 1

        print(f"Source already exists: {existing_file.name}. Checking for new D\"H or image.")
        
        actual_heading = heading_to_use
        try:
            file_content = existing_file.read_text(encoding="utf-8")
            import re
            
            # Check if this heading already exists
            headings = re.findall(r'^###\s+(.+)$', file_content, flags=re.MULTILINE)
            clean_headings = [h.strip() for h in headings if 'source image' not in h.strip().lower()]

            already_has_image = any(img in file_content for img in img_names)

            # If this is the first time this file is referenced in this sheet run,
            # and the heading already exists, it is a re-run / existing match -> reuse!
            if times_used == 0 and heading_to_use in clean_headings:
                if not already_has_image:
                    # Update images from this sheet if crop filenames changed
                    new_img_embeds = "\n".join([f"> ![[{img}]]\n> *(Cropped from {sheet_stem})*" for img in img_names])
                    sheet_pattern = rf"> !\[\[[^\n]*\]\]\n> \*\([Cc]ropped from {re.escape(sheet_stem)}\)\*"
                    if re.search(sheet_pattern, file_content):
                        # Replace old crop block from this sheet
                        first = True
                        def repl_crop(m):
                            nonlocal first
                            if first:
                                first = False
                                return new_img_embeds
                            return ""
                        file_content = re.sub(sheet_pattern, repl_crop, file_content)
                        # Clean up any leftover empty lines in Source Image block
                        file_content = re.sub(r'(\n> \*\([Cc]ropped from [^\n]+\)\*\n)\s*\n', r'\1', file_content)
                    else:
                        if "### Source Image" in file_content:
                            file_content = file_content.replace("### Source Image", f"### Source Image\n{new_img_embeds}")
                        else:
                            file_content += f"\n### Source Image\n{new_img_embeds}\n"
                    existing_file.write_text(file_content, encoding="utf-8")
                print(f"Source already contains heading '{heading_to_use}'. Reusing without duplicate.")
                return existing_stem, heading_to_use, False

            if already_has_image and heading_to_use in clean_headings:
                print(f"Source already contains this image and heading '{heading_to_use}'. Reusing.")
                return existing_stem, heading_to_use, False
            
            # If genuinely another occurrence in this sheet run (times_used > 0)
            base_heading = actual_heading
            counter = 2
            while actual_heading in clean_headings:
                actual_heading = f"{base_heading} ({counter})"
                counter += 1
                
            print(f"Adding new D\"H '{actual_heading}' to existing file.")
            # We need to add the new image to the ### Source Image block
            img_embeds = "\n".join([f"> ![[{img}]]\n> *(Cropped from {sheet_stem})*" for img in img_names if img not in file_content])
            
            if img_embeds:
                if "### Source Image" in file_content:
                    file_content = file_content.replace("### Source Image", f"### Source Image\n{img_embeds}")
                else:
                    file_content += f"\n### Source Image\n{img_embeds}\n"
                
            # Append the new heading at the bottom
            file_content += f"\n### {actual_heading}\n"
            
            existing_file.write_text(file_content, encoding="utf-8")
                
        except Exception as e:
            print(f"Error updating existing file: {e}")
            pass
            
        return existing_stem, actual_heading, False

    print(f"Creating new source: {file_name}")
    img_embeds = "\n".join([f"> ![[{img}]]" for img in img_names])
    
    # Strip brackets from subject for the tag
    tag_subject = subject.replace("[", "").replace("]", "").lower()
    tag_name = f"{tag_subject}-source"

    # 1. Author note creation
    author_file = AUTHORS_DIR / f"{display_author}.md"
    if not author_file.exists():
        author_content = f"""---
tags: [author]
---
# {display_author}

## Background Info

## Linked Sources
```dataview
TABLE book as Book, location as Location
WHERE contains(string(author), this.file.name)
SORT book ASC, location ASC
```
"""
        author_file.write_text(author_content, encoding="utf-8")

    # 2. Audit Flagging
    audit_needed = source_data.get("audit_needed", False)
    audit_reason = source_data.get("audit_reason", "")

    audit_frontmatter = ""
    audit_callout = ""
    if audit_needed:
        tag_list = f"[{tag_name}, needs-audit]"
        audit_frontmatter = f'audit_needed: true\naudit_reason: "{audit_reason}"\n'
        audit_callout = f"> [!warning] Audit Flag: Needs Verification\n> - **Reason**: {audit_reason}\n> - **AI Action**: Verify attribution against cropped source image and cross-reference with `222 Authors/`.\n\n"
    else:
        tag_list = f"[{tag_name}]"

    # 3. Source note creation
    source_file = SOURCES_DIR / file_name
    source_content = f"""---
author: "[[{display_author}]]"
book: "{display_book}"
location: "{display_loc}"
tags: {tag_list}
{audit_frontmatter}---
{audit_callout}> [!info]- Reference
> Author:: [[{display_author}]]
> Book:: {display_book}
> Location:: {display_loc}
### Source Image
{img_embeds}
> *(Cropped from {sheet_stem})*

### {heading_to_use}
"""
    source_file.write_text(source_content, encoding="utf-8")
    return file_base, heading_to_use, audit_needed

def main():
    config = load_config()
    default_subject = config.get('subjects', ['Gemara'])[0] if config.get('subjects') else 'Gemara'
    auto_season, auto_year, auto_test = get_academic_metadata()

    parser = argparse.ArgumentParser(description="Process source sheets from PDF")
    parser.add_argument('pdf_path', help="Path to the PDF")
    parser.add_argument('--subject', default=default_subject, help="Subject name")
    parser.add_argument('--season', default=auto_season, help="Season")
    parser.add_argument('--year', default=auto_year, help="Year")
    parser.add_argument('--test-target', default=auto_test, help="Test Target")
    args = parser.parse_args()

    pdf_path = Path(args.pdf_path)
    if not pdf_path.is_absolute():
        if not pdf_path.exists():
            candidate = RAPP_ROOT / "000 Source PDFs" / pdf_path.name
            if candidate.exists():
                pdf_path = candidate

    if not pdf_path.exists():
        print(f"Error: PDF file not found at {pdf_path}")
        sys.exit(1)

    ensure_dirs()
    print(f"Processing PDF: {pdf_path.name}...")

    sources = extract_sources_and_images(pdf_path)
    sheet_stem = sanitize_filename(pdf_path.stem)
    sheet_file = SHEETS_DIR / f"{sheet_stem}.md"

    linked_notes = []
    seen_in_sheet = {}
    for s in sources:
        note_stem, heading, needs_audit = process_source(s, sheet_stem, args.subject, seen_in_sheet=seen_in_sheet)
        linked_notes.append((note_stem, heading, needs_audit))

    # Master Source Sheet note content
    sheet_content = f"""---
subject: "[[{args.subject}]]"
season: "{args.season}"
year: "{args.year}"
test_target: "{args.test_target}"
pdf_source: "[[{pdf_path.name}]]"
---
# {sheet_stem}

[[{pdf_path.name}]]

## Sources

"""
    for i, (note, heading, needs_audit) in enumerate(linked_notes):
        badge = " ⚠️ (Needs Audit)" if needs_audit else ""
        sheet_content += f"## {i + 1}{badge}\n![[{note}#{heading}]]\n\n"

    sheet_file.write_text(sheet_content, encoding="utf-8")
    print(f"\nSuccess! Processed {len(sources)} sources from {pdf_path.name}.")
    print(f"Master Source Sheet created at: {sheet_file}")

if __name__ == "__main__":
    main()
