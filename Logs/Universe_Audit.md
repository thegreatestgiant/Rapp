# Universe Source Sheet Audit

## Summary
Audited the `universe.md` master source sheet (`000 Source PDFs/universe.pdf`, Subject: *Ikarim*, Fall 2026 Midterm). Resolved systematic parsing errors where English headers and citations were mangled into gibberish Hebrew, mid-paragraph parenthetical citations were falsely detected as new source headers, and missing canonical authors caused erroneous author generation.

---

## Root Causes Identified & Parser Fixes (`999 Scripts/process_source_sheets.py`)

1. **Blind QWERTY/Davka Decoding on English Text**:
   - **Root Cause**: `decode_text()` previously assumed that any string containing ASCII letters (`a-z`) was encoded in an inverted Hebrew font layout, blindly running it through `QWERTY_TO_HEBREW`. This destroyed legitimate English citations (e.g., Rav Yisroel Belsky, Lubavitcher Rebbe, Rav Shimon Schwab, Rabbi Aryeh Kaplan, Challenge excerpts) and produced scrambled Hebrew filenames.
   - **Fix**: Implemented smart line-by-line decoding (`is_line_english()` and `decode_line()`) with a common English lexicon check. English headers now remain intact while Davka-encoded Hebrew font streams decode cleanly to authentic Hebrew text.

2. **False Header Triggers on Body Paragraphs**:
   - **Root Cause**: The header regex `re.search(r"\( ?\d+|\d+ ?\(", raw)` matched anywhere inside arbitrary text blocks. Lengthy body paragraphs containing inline scripture/tractate references (such as `(1:1)`, `(Shabbat 88 and Hagiga 14)`, `(Psalms 90:4)`) were erroneously treated as new source headers. This fragmented sources, caused duplicate/truncated crops, and inflated the total source count from 16 to 18.
   - **Fix**: Restricted header number matching to line/block starts (`^\(?\s*\d{1,2}\s*[\)\.\-:]`, `\b\d{1,2}\s*\)`), added explicit detection for standalone numbers (`13`, `16)`), and capped header candidate block length (< 350 characters).

3. **Parenthesis Stripping in `parse_citation`**:
   - **Root Cause**: Stripping `\([^)]*\)` prior to author identification stripped crucial author metadata such as `(Rav Yisroel Belsky)`. Moreover, reversed parentheses in Davka text caused Sefer titles to be stripped.
   - **Fix**: Added explicit canonical checks at the head of `parse_citation()` and stripped leading source numbers before removing bracketed strings.

4. **Expanded `AUTHOR_CANONICAL_MAP`**:
   - Added canonical mappings for:
     - `Einei Yisroel` / `Rav Yisroel Belsky` -> `רבי ישראל בלסקי`
     - `Rabbi Menachem M. Schneerson` / `רבי מנחם מענדל שניאורסון` -> `הרבי מליובאוויטש`
     - `Rabbi Shimon Schwab` -> `רבי שמעון שוואב`
     - `Rabbi Aryeh Kaplan` / `The Age of the Universe` -> `רבי אריה קפלן`
     - `עולמות שחרבו` / `רבי יואל טייטלבוים` -> `הרבי מסאטמאר`
     - `אוצר החיים` -> `רבי יצחק דמן עכו`
     - `אבות דרבי נתן` / `מסכתות קטנות` -> `אבות דרבי נתן`
     - `תפארת ישראל` / `דרוש אור החיים` -> `רבי ישראל ליפשיץ`

5. **OCR-First Fallback on Problematic Headers**:
   - Before flagging any citation with `needs-audit` or generating an AI inspection callout, `process_source_sheets.py` now runs targeted high-DPI OCR (`page.get_textpage_ocr(clip=h_rect, dpi=300, language="heb+eng", full=True)`) over the header bounding box.
   - If OCR extracts clean text and resolves the author/book without fallback tokens or corrupt ASCII streams, it adopts the OCR result cleanly. Only if the OCR attempt also fails does the parser flag the citation for AI review.

---

## Vault Changes & Cleanup

### 1. Deleted Junk Authors (`222 Authors/`)
Removed temporary/garbled fallback author profiles:
- `21.md`
- `עולמות.md`
- `ץ.md`
- `ץמ׳ם.md`
- `ץפ.md`
- `ץקאןמןכמI.md`
- `ת81.md`
- `׳קןV.md`
- `מסכתות.md`

### 2. Created Canonical Author Notes (`222 Authors/`)
- `רבי ישראל בלסקי.md`
- `רבי מנחם מענדל שניאורסון.md`
- `רבי שמעון שוואב.md`
- `רבי אריה קפלן.md`
- `רבי יואל טייטלבוים.md`
- `רבי יצחק דמן עכו.md`
- `אבות דרבי נתן.md`

### 3. Sources Audited & Standardized (`333 Sources/` & `111 Source Sheets/universe.md`)
Cleaned up all 16 canonical sources with proper anchors, metadata, and cropped images:
1. `בראשית רבה - פרשה ג`
2. `תנ''ך - בראשית - פרק ז פסוק כג`
3. `הנצי''ב מולוז'ין - העמק דבר - בראשית פרק ז פסוק כג`
4. `מלבי''ם - בראשית פרשת נח - פרק ז פסוק כג`
5. `רבי ישראל בלסקי - עיני ישראל - בראשית עמ' 12-16` (spanning page 1 and continuation on page 2)
6. `אבות דרבי נתן - נוסחא א - פרק לא`
7. `תלמוד בבלי - מסכת חגיגה - דף יג עמוד ב`
8. `תלמוד בבלי - מסכת סנהדרין - דף צז עמוד א`
9. `רבי מנחם מענדל שניאורסון - A Letter on Science and Judaism - Challenge p. 145` (spanning page 2 and continuation on page 3)
10. `אליהו - זוטא - פרשה ג`
11. `רבי שמעון שוואב - How old is the Universe- - Challenge p. 165`
12. `תלמוד בבלי - מסכת סנהדרין - דף לח עמוד ב`
13. `רבי ישראל ליפשיץ - דרוש אור החיים - Challenge` (spanning page 3 and continuation on page 4)
14. `רבי אריה קפלן - The Age of the Universe - February 18, 1979`
15. `רבי יואל טייטלבוים - עולמות שחרבו - חלק ראשון עמ' קנז`
16. `רבי יצחק דמן עכו - אוצר החיים - Immortality, Resurrection and the Age of the Universe`

### 4. Cleaned Attachments (`444 Attachments/`)
Purged false intermediate crops (`universe_p1_s6.png`, `universe_p4_s4.png`, `universe_p4_s5.png`) that resulted from earlier fragmented text matches.
