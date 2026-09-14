# Fixing Lulav and Esrog Audit

## Summary
Audited the `Fixing Lulav and Esrog.md` source sheet to resolve systematic parsing issues related to books without matching known authors, leading to incorrect author extraction.

## Changes
- Identified multiple misattributed sources in the `Fixing Lulav and Esrog` source sheet, such as `שו"ת בית יעקב` being parsed as "שו"ת בית", `סוכת שלם` not mapped, etc.
- Created the following missing author files in `222 Authors/`:
  - `רבי זאב בראווער.md`
  - `רבי יעקב בן שמואל מצויזמיר.md`
  - `רבי יעקב ריישר.md`
  - `רבי שלום מרדכי שבדרון.md`
  - `רבי מלכיאל צבי טננבוים.md`
  - `רבי שלום טויבש.md`
  - `רבי אלעזר לנדא.md`
  - `רבי יוסף שאול נתנזון.md`
  - `רבי חיים חזקיהו מדיני.md`
  - `רבי חיים מרדכי מרגליות.md`
  - `רבי ישראל רייזמן.md`
  - `רבי אליהו וייספיש.md`
- Renamed the source files to adhere strictly to the `[Author Name] - [Book Name] - [Location].md` convention and updated the internal file links within `Fixing Lulav and Esrog.md`.
- Updated `AUTHOR_CANONICAL_MAP` in `999 Scripts/process_source_sheets.py` so that future parsing of these books automatically defaults to their true authors.
- Updated `999 Scripts/GEMINI.md` to reflect these changes.

## Additional Fixes (Follow-up)
- Fixed an issue where the `process_source_sheets.py` regex for `loc_match` did not recognize `ס'` or `ס׳` as a location marker. Because of this, source #7 was initially extracted with an empty location and `ס׳ קמ''ב` became part of the book title. Renamed source #7 to use `סימן` instead of `ס׳` and updated the link. Added `ס['׳]?` to `loc_match` in `process_source_sheets.py`.
- Fixed broken anchor links for sources #24 and #26 in the `Fixing Lulav and Esrog.md` source sheet. The automated renaming script had mistakenly overwritten their custom *Dibur Hamatchil* anchors (e.g. `#בכל שהוא`).
- Corrected the author for source #6 (`סוכת שלם`) to `רבי שמואל שולמן` per user instruction. Created the author file, renamed the source file, updated the source sheet link, and patched the canonical mapping in `process_source_sheets.py`.
- Updated author of source #6 (`סוכת שלם`) to `רבי שמריהו שולמן`, added biographical background info to the author note, and updated all corresponding files and mappings.
- Corrected the spelling of Maharsham's name from `שבדרון` to `שוודרון` ("2 vuv's") across all his author pages, source links, and the canonical parser map.
