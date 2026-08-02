import fitz
import re
from pathlib import Path
import json

pdf_path = Path(__file__).parent.parent / "000 Source PDFs" / "shmuel 2.23.pdf"

QWERTY_TO_HEBREW = {
    "a": "ש", "b": "נ", "c": "ב", "d": "ג", "e": "ק", "f": "כ", "g": "ע", "h": "י",
    "i": "ן", "j": "ח", "k": "ל", "l": "ך", "m": "צ", "n": "מ", "o": "ם", "p": "פ",
    "q": "/", "r": "ר", "s": "ד", "t": "א", "u": "ו", "v": "ה", "w": "׳", "x": "ס",
    "y": "ט", "z": "ז", ",": "ת", ".": "ץ", ";": "ף", '"': '"'
}
def decode_text(text):
    if any(c in "abcdefghijklmnopqrstuvwxyz,.;" for c in text):
        rev = text[::-1]
        res = [QWERTY_TO_HEBREW.get(ch, ch) for ch in rev]
        return "".join(res)
    return text

doc = fitz.open(pdf_path)
extracted = []
for page_num in range(len(doc)):
    page = doc[page_num]
    blocks = page.get_text("blocks")
    headers = []
    for b in blocks:
        raw = b[4].strip()
        if re.search(r"\( ?\d+|\d+ ?\)", raw):
            headers.append(b)
    headers.sort(key=lambda b: b[1])
    for h in headers:
        raw_header = h[4].strip()
        decoded = decode_text(raw_header).replace("\n", " ")
        extracted.append(decoded)

print("Extracted count:", len(extracted))
for i, e in enumerate(extracted):
    print(f"{i+1}: {e}")
