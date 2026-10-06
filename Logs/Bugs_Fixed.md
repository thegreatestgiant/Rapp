
### Date: 2026-09-15
- **Bug**: The parser incorrectly grouped multiple Dibur Hamatchil sources for the same file, resulting in identical links.
  - **Root Cause**: When a source file already existed, the script bypassed adding the new extracted D"H and simply grabbed the final `###` heading in the file, causing subsequent sources from the same Pasuk to erroneously duplicate the first one.
  - **Fix**: Updated `process_source_sheets.py` to append the new D"H to the bottom of the existing file and dynamically insert the new cropped image into the `### Source Image` block at the top if the D"H didn't already exist.

- **Bug**: Inaccurate author mapping for titles with prefixes (e.g., 'ספר מורה', 'ספר יערות', 'משך').
  - **Fix**: Appended new canonical mappings to `AUTHOR_CANONICAL_MAP` in `process_source_sheets.py` (e.g. `ספר מורה` -> `רמב"ם`, `ספר יערות` -> `רבי יהונתן אייבשיץ`, `משך` -> `משך חכמה`).

- **Bug**: If multiple sources mapped to the exact same file and the D"H extraction logic failed to find a valid hyphen/period (e.g., `קהלת רבה`), both sources fell back to identical default headings (the filename) and refused to append because the heading "already existed."
  - **Fix**: Upgraded the `process_source_sheets.py` existing file logic so that if the extracted `actual_heading` is already in the file, it automatically appends an incrementing counter suffix (e.g., `(2)`, `(3)`) to guarantee unique headings are generated for every new source block, and properly linked in the source sheet.

### Date: 2026-10-06
- **Bug**: Re-running the parser script on an existing source sheet created unwanted `(2)` and `(3)` heading duplicate anchors and duplicated image embeds in the source files.
  - **Root Cause**: When re-processing a sheet, `process_source_sheets.py` saw the existing base heading and unconditionally incremented counter suffixes without checking whether the image and heading already existed for this sheet.
  - **Fix**: Updated `process_source_sheets.py` to check `if already_has_image and heading_to_use in clean_headings: return existing_stem, heading_to_use`, preventing duplicate image embeds and counter increments on repeated script runs.

- **Bug**: OCR fallback on scanned PDF `melachim 1.6.pdf` fragmented Tanach verses, missed headers, and produced filenames with nekudot.
  - **Fix**: Re-processed all 27 sources using precise coordinates, stripped all nekudot, restored user-written notes from Obsidian recovery snapshots, and verified author mappings.
