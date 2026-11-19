# Melachim 1.16 Source Sheet Audit

## Summary
Audited `111 Source Sheets/melachim 1.16.md` (`000 Source PDFs/melachim 1.16.pdf`, Subject: *Navi*, Fall 2026 Final) — 15 embedded sources across 2 pages. Verified every citation against the decoded Davka font text stream and PDF layout, resolved all flagged and malformed sources (**פסיקתא דרב כהנא**, **אוצר המדרשים / אייזנשטיין**, **משך חכמה**, **אברבנאל**, and disambiguated **תלמוד בבלי מסכת סנהדרין דף קב עמוד ב**), created canonical author profile in `222 Authors/` (**פסיקתא דרב כהנא**), enriched **רבי יהודה דוד אייזנשטיין** and **אוצר המדרשים**, purged corrupt fallback author profile (`222 Authors/פסיקתא.md`), verified continuation crop `melachim 1.16_p2_cont.png`, and patched all parser root causes in `999 Scripts/process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #4 (`משך חכמה על בראשית פרק טו פסוק יג`)
- **Issue**: The parser did not strip the leading preposition `על ` from the book name, leaving `book: "על בראשית"`, diverging from standard vault naming conventions (e.g. `משך חכמה - דברים - פרק יב פסוק יג.md`).
- **Resolution**: Renamed source note to **`333 Sources/משך חכמה - בראשית - פרק טו פסוק יג.md`**, set `book: "בראשית"`, updated the headline anchor to `### משך חכמה - בראשית - פרק טו פסוק יג`, and updated the embed on the master sheet.
- **Root Cause Patch**: Generalized Tanach commentary book cleaning in `process_source_sheets.py`: strips `^על[-\s]+` when the remainder is a Tanach book or the author is a known Tanach commentator (`משך חכמה`, `אברבנאל`, `חזקוני`, `רש"י`, `רד"ק`, `מלבי"ם`, `רלב"ג`, `ספורנו`, `כלי יקר`, `אלשיך`).

### 2. Source #6 (`פסיקתא דרב כהנא )מנדלבוים( נספחים פרשה א ד"ה ר׳ בניי בשם`)
- **Issue**: Unmapped Midrashic title caused parser to fall back to single token `author: "פסיקתא"`, `book: "דרב כהנא נספחים"`, generated corrupt fallback `222 Authors/פסיקתא.md`, and flagged the source `audit_needed: true` (*"Author fell back to token 'פסיקתא'"*).
- **Resolution**: Identified work as *Pesikta de-Rav Kahana* (Mandelbaum critical edition, Appendix 1). Standardized note to **`333 Sources/פסיקתא דרב כהנא - נספחים - פרשה א ד''ה ר׳ בניי בשם.md`**, attributed to canonical author **`[[פסיקתא דרב כהנא]]`**, book `נספחים`, location `פרשה א ד''ה ר׳ בניי בשם`. Cleared audit flag and removed `⚠️ (Needs Audit)` badge from the master sheet. Verified continuation crop `melachim 1.16_p2_cont.png`.
- **Author Note**: Created canonical author profile [`222 Authors/פסיקתא דרב כהנא.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A4%D7%A1%D7%99%D7%A7%D7%AA%D7%20%D7%93%D7%A8%D7%91%20%D7%93%D7%94%D7%A0%D7%90.md) with aliases `[פסיקתא דרב כהנא, פסיקתא דריב"ק, פסיקתא, Pesikta de-Rav Kahana, Pesikta deRav Kahana]` and scholarly background; purged fallback `222 Authors/פסיקתא.md`.
- **Root Cause Patch**: Added `פסיקתא דרב כהנא` and `פסיקתא רבתי` to `KNOWN_AUTHORS`, `KNOWN_HEADER_KEYWORDS`, `AUTHOR_CANONICAL_MAP`, and `RESPONSA_SPECIAL_MAP` in `process_source_sheets.py`.

### 3. Source #8 (`אברבנאל על מלכים א - פרק טז )יח(`)
- **Issue**: The verse specification `)יח(` in the header was lost/stripped by parenthesis cleanup, and `על ` remained in the book title (`book: "על מלכים א"`, `location: "פרק טז"`).
- **Resolution**: Normalized chapter-with-parenthesized-verse into `פסוק יח`. Standardized note to **`333 Sources/אברבנאל - מלכים א - פרק טז פסוק יח.md`**, attributed to canonical author **`[[אברבנאל]]`**, book `מלכים א`, location `פרק טז פסוק יח`, and updated master sheet embed.
- **Root Cause Patch**: Added normalization rule `re.sub(r'פרק\s+([א-ת0-9]+)\s*[\(\[\]\)]\s*([א-ת0-9]+)\s*[\(\[\]\)]', r'פרק \1 פסוק \2', clean)` before generic paren stripping, preserving precise verse citations.

### 4. Sources #10, #11, #13 (`תלמוד בבלי מסכת סנהדרין דף קב עמוד ב`)
- **Issue**: Three distinct passages from Sanhedrin 102b were included on page 2. Sources 10 and 11 extracted Dibur Hamatchil headings (`### אמר רבי יוחנן` and `### אחאב`), but Source 13 began with a parenthesized Tanach cross-reference `)מלכים א׳ ט"ז( ויעש אחאב את האשרה...`, causing DH extraction to fail and falling back to generic `### תלמוד בבלי - מסכת סנהדרין - דף קב עמוד ב`. In addition, image attachments were prepended in reverse chronological order.
- **Resolution**: Updated Source 13 heading to **`### ויעש אחאב את האשרה`** and updated master sheet embed to `![[תלמוד בבלי - מסכת סנהדרין - דף קב עמוד ב#ויעש אחאב את האשרה]]`. Reordered image attachments in `333 Sources/תלמוד בבלי - מסכת סנהדרין - דף קב עמוד ב.md` to chronological order (`melachim 1.16_p2_s4.png` for #10, `melachim 1.16_p2_s5.png` for #11, `melachim 1.16_p2_s7.png` for #13).
- **Root Cause Patch**: Added multi-source Talmud/Midrash daf collision disambiguation pass in `extract_sources_and_images`: when multiple excerpts share the same daf/location and a source lacks a DH, automatically strips leading parenthesized citations `)מלכים...(` and extracts the opening phrase as the Dibur Hamatchil.

### 5. Source #14 (`אוצר המדרשים )אייזנשטיין( עמוד תסא ד"ה בשם היוצר גבוהים`)
- **Issue**: `אוצר המדרשים` was matched as author while `אייזנשטיין` was in parentheses, leaving the book part empty and triggering fallback `book: "מקור"` (`333 Sources/אוצר המדרשים - מקור - עמוד תסא ד''ה בשם היוצר גבוהים.md`).
- **Resolution**: Standardized note to **`333 Sources/רבי יהודה דוד אייזנשטיין - אוצר המדרשים - עמוד תסא ד''ה בשם היוצר גבוהים.md`**, attributed to canonical author **`[[רבי יהודה דוד אייזנשטיין]]`**, book `אוצר המדרשים`, location `עמוד תסא ד''ה בשם היוצר גבוהים`. Updated master sheet embed and deleted corrupt `* - מקור - *.md` file.
- **Author Note**: Enriched [`222 Authors/רבי יהודה דוד אייזנשטיין.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%99%D7%94%D7%95%D7%93%D7%94%20%D7%93%D7%95%D7%93%20%D7%90%D7%99%D7%99%D7%96%D7%A0%D7%51%D7%98%D7%99%D7%99%D7%9F.md) with aliases `[רבי יהודה דוד אייזנשטיין, יהודה דוד אייזנשטיין, אייזנשטיין, בעל אוצר המדרשים, אוצר המדרשים, J. D. Eisenstein, Judah David Eisenstein]` and bio while preserving user study notes. Enriched [`222 Authors/אוצר המדרשים.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%90%D7%95%D7%A6%D7%A8%20%D7%94%D7%9E%D7%93%D7%A8%D7%51%D7%99%D7%9D.md) linking to Eisenstein.
- **Root Cause Patch**: Mapped `'אוצר המדרשים'` in `RESPONSA_SPECIAL_MAP` to `('רבי יהודה דוד אייזנשטיין', 'אוצר המדרשים')`, added canonical author mappings to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`, and ensured `book` defaults to `אוצר המדרשים` instead of `מקור`.

---

## 2. Complete Sheet Verification (15/15)

| # | Canonical Title | Canonical Author | Status | Notes |
|---|---|---|---|---|
| 1 | `רש''י - מלכים א - פרק טז פסוק ז` | [[רש''י]] | ✅ Verified | Clean DH anchor `#ועל אשר הכה אותו` |
| 2 | `רמב''ם - הלכות תשובה - פרק ו הלכה ה` | [[רמב''ם]] | ✅ Verified | Clean 2-header layout (includes Ra'avad gloss) |
| 3 | `רמב''ן - בראשית - פרק טו פסוק יד` | [[רמב''ן]] | ✅ Verified | Clean 2-header layout |
| 4 | `משך חכמה - בראשית - פרק טו פסוק יג` | [[משך חכמה]] | 🔧 **Fixed** | Stripped `על `, standardized book to `בראשית` |
| 5 | `רמב''ם - הלכות מלכים - פרק ג הלכה ה` | [[רמב''ם]] | ✅ Verified | Clean 2-header layout |
| 6 | `פסיקתא דרב כהנא - נספחים - פרשה א ד''ה ר׳ בניי בשם` | [[פסיקתא דרב כהנא]] | 🔧 **Fixed** | Attributed to Pesikta de-Rav Kahana; cleared audit flag; verified continuation crop `p2_cont` |
| 7 | `רד''ק - מלכים א - פרק טז פסוק יח` | [[רד''ק]] | ✅ Verified | Clean DH anchor `#וישרף עליו` |
| 8 | `אברבנאל - מלכים א - פרק טז פסוק יח` | [[אברבנאל]] | 🔧 **Fixed** | Preserved verse 18; stripped `על ` from book name |
| 9 | `רד''ק - מלכים א - פרק טז פסוק כב` | [[רד''ק]] | ✅ Verified | Clean DH anchor `#וימת תבני` |
| 10 | `תלמוד בבלי - מסכת סנהדרין - דף קב עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean DH anchor `#אמר רבי יוחנן` |
| 11 | `תלמוד בבלי - מסכת סנהדרין - דף קב עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean DH anchor `#אחאב` |
| 12 | `מדרש תנחומא - פרשת ואתחנן - הוספה - סימן ב` | [[מדרש תנחומא]] | ✅ Verified | Clean 2-header layout |
| 13 | `תלמוד בבלי - מסכת סנהדרין - דף קב עמוד ב` | [[תלמוד בבלי]] | 🔧 **Fixed** | Assigned clean DH anchor `#ויעש אחאב את האשרה`; reordered image crops chronologically |
| 14 | `רבי יהודה דוד אייזנשטיין - אוצר המדרשים - עמוד תסא ד''ה בשם היוצר גבוהים` | [[רבי יהודה דוד אייזנשטיין]] | 🔧 **Fixed** | Attributed to Eisenstein; cleared corrupt `מקור` book title |
| 15 | `תלמוד בבלי - מסכת סנהדרין - דף קיג עמוד א` | [[תלמוד בבלי]] | ✅ Verified | Clean DH anchor `#תניא` |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Pesikta Recognition (`פסיקתא דרב כהנא` & `פסיקתא רבתי`)**:
   - Added `פסיקתא דרב כהנא` and `פסיקתא רבתי` to `KNOWN_AUTHORS`, `KNOWN_HEADER_KEYWORDS`, and `AUTHOR_CANONICAL_MAP`.
   - Bound to `RESPONSA_SPECIAL_MAP` and book resolution logic: detects `נספחים` addenda and extracts clean book and location.

2. **Otzar HaMidrashim / Eisenstein Mapping**:
   - Added `'אוצר המדרשים'` to `RESPONSA_SPECIAL_MAP` mapped to `('רבי יהודה דוד אייזנשטיין', 'אוצר המדרשים')`.
   - Added canonical author mappings for `אוצר המדרשים`, `רבי יהודה דוד אייזנשטיין`, `יהודה דוד אייזנשטיין`, and `אייזנשטיין`.
   - Guaranteed `book` defaults to `אוצר המדרשים` when author is Eisenstein and `book` is empty/`מקור`.

3. **Tanach Commentary `על ` Prefix Stripping**:
   - Generalized book cleaning rule: automatically strips `^על[-\s]+` whenever the candidate book belongs to `TANACH_BOOKS` or the author is a recognized Tanach commentator (`משך חכמה`, `אברבנאל`, `חזקוני`, `מלבי"ם`, `רלב"ג`, `רש"י`, `רד"ק`, `ספורנו`, `כלי יקר`, `אלשיך`).

4. **Tanach Parenthesized Verse Extraction**:
   - Added pre-cleanup normalization: `re.sub(r'פרק\s+([א-ת0-9]+)\s*[\(\[\]\)]\s*([א-ת0-9]+)\s*[\(\[\]\)]', r'פרק \1 פסוק \2', clean)`, converting notations like `פרק טז )יח(` into `פרק טז פסוק יח`.

5. **Talmud / Midrash Multi-Source Collision Disambiguation**:
   - Added duplicate excerpt disambiguation pass in `extract_sources_and_images`: when multiple sources on the same sheet share the exact same daf/location and one lacks a DH, strips leading cross-references (such as reverse-encoded `)מלכים א׳ ט"ז(`) and extracts the opening 2–4 words as a disambiguated Dibur Hamatchil.
