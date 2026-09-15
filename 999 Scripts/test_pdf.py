import fitz
doc = fitz.open("/home/sean/Obsidian/Rapp/000 Source PDFs/melachim 1.3.pdf")
page = doc[3] # page 4
blocks = page.get_text("blocks")
def decode_text(text): return "".join(reversed(text))
for i, b in enumerate(blocks):
    print(f"[{i}] {decode_text(b[4].strip().replace(chr(10), ' '))}")
