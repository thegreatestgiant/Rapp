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

def decode_text(text):
    if any(c in "abcdefghijklmnopqrstuvwxyz,.;\x1b" for c in text):
        rev = text[::-1]
        res = [QWERTY_TO_HEBREW.get(ch, ch) for ch in rev]
        return "".join(res).replace('\x1b', '"')
    return text

def get_all_known_authors():
    authors = set(KNOWN_AUTHORS)
    if AUTHORS_DIR.exists():
        for f in AUTHORS_DIR.glob("*.md"):
            name = f.stem.replace("''", '"')
            authors.add(name)
    
    extras = [
        'רא"ש', 'הרא"ש', 'ריטב"א', 'הריטב"א', 'רשב"א', 'הרשב"א', 'תוספות', 'הר"ן', 'ר"ן', 
        'חלקת יואב', 'רבבות אפרים', 'דרוש וחדוש', 'מועדים בהלכה', 'רי"ף', 'הרי"ף', 'רש"י', 'הר צבי'
    ]
    for e in extras:
        authors.add(e)
        
    # Remove some generic prefixes that might have slipped into authors if we don't want them as strict authors
    bad = {'שו"ת', 'ספר', 'פ', 'חידושי', 'ערוך', 'תוספת', 'דרוש', 'חלקת'}
    for b in bad:
        if b in authors:
            authors.remove(b)
            
    return sorted(list(authors), key=len, reverse=True)

ALL_KNOWN_AUTHORS = get_all_known_authors()

def parse_citation(header_text):
    clean = re.sub(r"\([^\)]*?\d+[^\)]*?\)", "", header_text)
    clean = re.sub(r"\b\d+[\)\(]|\([\)\d]+", "", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    clean = clean.replace("''", '"') # Normalize quotes for matching

    author = None
    matches = []
    for a in ALL_KNOWN_AUTHORS:
        if a in clean:
            matches.append(a)
            
    if matches:
        matches.sort(key=lambda x: (clean.find(x), -len(x)))
        best_match = matches[0]
        author = best_match.replace('שו"ת ', '').replace('הרמב"ם', 'רמב"ם').replace('הרמב"ן', 'רמב"ן')
        author = author.replace('הרא"ש', 'רא"ש').replace('הריטב"א', 'ריטב"א').replace('הרשב"א', 'רשב"א').replace('הר"ן', 'ר"ן')

    loc_match = re.search(r"(דף|פרק|סימן|פסוק|סעיף|מאמר|אות|טור|ס\"ק|ד\"ה|משנה|פיסקא|ח\"א|ח\"ב|ח\"ג|ח\"ד).*", clean)
    if loc_match:
        location = loc_match.group(0).strip()
        book_part = clean[:loc_match.start()].strip()
    else:
        location = ""
        book_part = clean

    if author and book_part.startswith(author):
        book_part = book_part[len(author):].strip()
    elif author and ('שו"ת ' + author) in book_part:
        book_part = book_part.replace('שו"ת ' + author, "").strip()

    book = re.sub(r"^[-\s:;]+|[-\s:;]+$", "", book_part).strip()

    if not author:
        for tb in TANACH_BOOKS:
            if tb in clean:
                author = 'תנ"ך'
                if not book:
                    book = tb
                break

    if not author:
        words = book.split()
        if len(words) > 1 and words[0] in ['שו"ת', "שו''ת", 'חידושי', 'ספר', 'פ', 'פירוש', 'דרוש', 'חלקת', 'ערוך', 'תוספת', 'קונטרס']:
            author = " ".join(words[:2])
        elif words:
            author = words[0]
        else:
            author = "מקור"

    if not book:
        book = "מקור"

    location = re.sub(r"\s*\d+[\)\(]?$", "", location).strip()

    return author, book, location

import difflib

def normalize_text_for_match(t):
    return re.sub(r'[^\wא-ת]', '', t)

def get_normalized_location(t):
    t = re.sub(r'[^\wא-ת]', '', t)
    t = t.replace('עמודב', 'עב').replace('עמודא', 'עא')
    return t

def match_existing_source(author, book, location):
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
                        
    return None

def extract_sources_and_images(pdf_path):
    doc = fitz.open(pdf_path)
    sources = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("blocks")

        headers = []
        for b in blocks:
            raw = b[4].strip()
            if re.search(r"\( ?\d+|\d+ ?\)", raw):
                headers.append(b)

        headers.sort(key=lambda b: b[1])

        if page_num > 0 and sources and (not headers or headers[0][1] > 90):
            cont_y1 = headers[0][1] - 5 if headers else min(page.rect.height, page.rect.height - 15)
            cont_rect = fitz.Rect(0, 30, page.rect.width, cont_y1)
            pix = page.get_pixmap(clip=cont_rect, dpi=150)
            cont_img_name = sanitize_filename(f"{pdf_path.stem}_p{page_num+1}_cont.png")
            pix.save(str(ATTACHMENTS_DIR / cont_img_name))
            sources[-1]["image_filenames"].append(cont_img_name)

        for i, h in enumerate(headers):
            raw_header = h[4].strip()
            
            # If the header block ONLY contains a number (like '(2' or '11)'),
            # the actual text might be in another block on the same horizontal line.
            if re.match(r"^[\(\)\s\d]+$", raw_header):
                same_line_texts = []
                for b in blocks:
                    if b != h and abs(b[1] - h[1]) < 5:
                        same_line_texts.append(b[4].strip())
                if same_line_texts:
                    raw_header = " ".join(same_line_texts) + " " + raw_header

            decoded_header = decode_text(raw_header).replace("\n", " ")
            author, book, location = parse_citation(decoded_header)

            # Attempt to extract Dibur Hamatchil (DH) from the next block
            dh = None
            block_idx = blocks.index(h)
            if block_idx + 1 < len(blocks):
                first_line = blocks[block_idx+1][4].strip().split('\n')[0]
                first_line_dec = decode_text(first_line).strip()
                # Check for DH ending with hyphen or period
                match = re.search(r'^(.*?)[\-\.](?:\s|$)', first_line_dec)
                if match:
                    candidate = match.group(1).strip()
                    if len(candidate.split()) <= 8:
                        dh = candidate
                elif first_line_dec.endswith('-') or first_line_dec.endswith('.'):
                    candidate = first_line_dec[:-1].strip()
                    if len(candidate.split()) <= 8:
                        dh = candidate

            y0 = max(0, h[1] - 5)
            if i + 1 < len(headers):
                y1 = headers[i+1][1] - 5
            else:
                y1 = min(page.rect.height, page.rect.height - 15)

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
                "image_filenames": [main_img_name]
            })

    return sources
def process_source(source_data, sheet_stem, subject):
    author = source_data["author"]
    book = source_data["book"]
    location = source_data["location"]
    dh = source_data.get("dibur_hamatchil")
    img_names = source_data["image_filenames"]

    display_author = sanitize_filename(author)[:60].strip()
    display_book = sanitize_filename(book)[:60].strip()
    display_loc = sanitize_filename(location)[:60].strip()

    title_parts = [display_author, display_book]
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
        print(f"Skipping existing source (already exists): {existing_file.name}")
        return existing_stem, heading_to_use

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

    # 2. Source note creation
    source_file = SOURCES_DIR / file_name
    source_content = f"""---
author: "[[{display_author}]]"
book: "{display_book}"
location: "{display_loc}"
tags: [{tag_name}]
---
> [!info]- Reference
> Author:: [[{display_author}]]
> Book:: {display_book}
> Location:: {display_loc}

### Source
{img_embeds}
> *(Cropped from {sheet_stem})*

### {heading_to_use}
"""
    source_file.write_text(source_content, encoding="utf-8")
    return file_base, heading_to_use

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
    for s in sources:
        note_stem, heading = process_source(s, sheet_stem, args.subject)
        linked_notes.append((note_stem, heading))

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
    for i, (note, heading) in enumerate(linked_notes):
        sheet_content += f"## {i + 1}\n![[{note}#{heading}]]\n\n"

    sheet_file.write_text(sheet_content, encoding="utf-8")
    print(f"\nSuccess! Processed {len(sources)} sources from {pdf_path.name}.")
    print(f"Master Source Sheet created at: {sheet_file}")

if __name__ == "__main__":
    main()
