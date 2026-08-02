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
    if any(c in "abcdefghijklmnopqrstuvwxyz,.;" for c in text):
        rev = text[::-1]
        res = [QWERTY_TO_HEBREW.get(ch, ch) for ch in rev]
        return "".join(res)
    return text

def parse_citation(header_text):
    clean = re.sub(r"\([^\)]*?\d+[^\)]*?\)", "", header_text)
    clean = re.sub(r"\b\d+[\)\(]|\([\)\d]+", "", clean)
    clean = re.sub(r"\s+", " ", clean).strip()

    author = None
    for a in KNOWN_AUTHORS:
        if a in clean:
            author = a.replace('שו"ת ', '').replace('הרמב"ם', 'רמב"ם').replace('הרמב"ן', 'רמב"ן')
            break

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
        author = book.split()[0] if book else "מקור"

    if not book:
        book = "מקור"

    location = re.sub(r"\s*\d+[\)\(]?$", "", location).strip()

    return author, book, location

import difflib

def normalize_text_for_match(t):
    return re.sub(r'[^\wא-ת]', '', t)

def match_existing_source(author, book, location):
    parsed_full = f"{author} {book} {location}"
    norm_parsed = normalize_text_for_match(parsed_full)
    
    existing_files = list(SOURCES_DIR.glob("*.md"))
    norm_existing = {normalize_text_for_match(f.stem): f for f in existing_files}
    
    matches = difflib.get_close_matches(norm_parsed, norm_existing.keys(), n=1, cutoff=0.7)
    if matches:
        return norm_existing[matches[0]]
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
            decoded_header = decode_text(raw_header).replace("\n", " ")
            author, book, location = parse_citation(decoded_header)

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
                "image_filenames": [main_img_name]
            })

    return sources
def process_source(source_data, sheet_stem):
    author = source_data["author"]
    book = source_data["book"]
    location = source_data["location"]
    img_names = source_data["image_filenames"]

    display_author = sanitize_filename(author)
    display_book = sanitize_filename(book)
    display_loc = sanitize_filename(location)

    title_parts = [display_author, display_book]
    if display_loc:
        title_parts.append(display_loc)

    file_base = " - ".join(title_parts)
    file_name = f"{file_base}.md"

    existing_file = match_existing_source(author, book, location)

    if existing_file and existing_file.exists():
        existing_stem = existing_file.stem
        print(f"Skipping existing source (already exists): {existing_file.name}")
        return existing_stem

    print(f"Creating new source: {file_name}")
    img_embeds = "\n".join([f"> ![[{img}]]" for img in img_names])

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
FROM #gemara-source
WHERE contains(author, this.file.link)
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
tags: [gemara-source]
---
> [!info]- Reference
> Author:: [[{display_author}]]
> Book:: {display_book}
> Location:: {display_loc}

### Source
{img_embeds}
> *(Cropped from {sheet_stem})*

### {file_base}
"""
    source_file.write_text(source_content, encoding="utf-8")
    return file_base

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
        note_stem = process_source(s, sheet_stem)
        linked_notes.append(note_stem)

    # Master Source Sheet note content
    sheet_content = f"""---
subject: "[[{args.subject}]]"
season: "{args.season}"
year: "{args.year}"
test_target: "{args.test_target}"
pdf_source: "[[{pdf_path.name}]]"
---
# {sheet_stem}

## Sources

"""
    for i, note in enumerate(linked_notes):
        sheet_content += f"## {i + 1}\n![[{note}#{note}]]\n\n"

    sheet_file.write_text(sheet_content, encoding="utf-8")
    print(f"\nSuccess! Processed {len(sources)} sources from {pdf_path.name}.")
    print(f"Master Source Sheet created at: {sheet_file}")

if __name__ == "__main__":
    main()
