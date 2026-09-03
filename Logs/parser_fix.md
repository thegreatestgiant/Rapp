# Parser Fixes - 2026-09-03

## Issues Found
1. **Tanach Substring Match:** `TANACH_BOOKS` was using a simple substring match (`if tb in clean:`). This caused a book named "קהלת יעקב" to be falsely attributed to the author "תנ''ך" because it contains "קהלת".
2. **Author Substring Match:** Author matching was using `if a in clean:`. This caused a book like "ליקוטי מוהר''ן" to be attributed to the author "ר''ן" because the string contains "ר''ן".

## Resolution
Patched `999 Scripts/process_source_sheets.py` to use a regular expression with Hebrew word boundaries (`(?<![א-ת])...(?![א-ת])`) to ensure that authors and Tanach books are only matched when they appear as discrete words and not as substrings within other words.
