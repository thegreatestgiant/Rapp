with open("process_source_sheets.py", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith("def process_source"):
        break

lines.insert(i, """def extract_sources_and_images(pdf_path):
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
            decoded_header = decode_text(raw_header).replace("\\n", " ")
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
""")

with open("process_source_sheets.py", "w") as f:
    f.writelines(lines)
