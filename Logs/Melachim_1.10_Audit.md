# Melachim 1.10 Source Sheet Audit

## Summary
Audited `111 Source Sheets/melachim 1.10.md` (`000 Source PDFs/melachim 1.10.pdf`, Subject: *Navi*, Fall 2026 Midterm) — 13 canonical embedded sources. Verified every citation against the decoded PDF headers, resolved all 6 flagged/corrupt sources (including the reverse-QWERTY decoded Wikipedia citation, phantom source #7, Midrash Mishlei, Sefer HaBris, Sefer Chasidim, and Shelah), created canonical author profiles in `222 Authors/`, purged corrupt fallback profiles, preserved user study notes under Gemara Sanhedrin 21b, and patched root causes in `process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #3 (`מדרש משלי (בובר) פרשה א`)
- **Issue**: Extracted as `author='מדרש'`, `book='משלי פרשה א'`, flagged `audit_needed: true` (*"Author fell back to token 'מדרש'"*).
- **Resolution**: Renamed to **`מדרש משלי - פרשה א.md`**; attributed to canonical author **`[[מדרש משלי]]`**, book `משלי`, location `פרשה א`.
- **Author Note**: Created [`222 Authors/מדרש משלי.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%9E%D7%93%D7%50%D7%A9%20%D7%9E%D7%A9%D7%9C%D7%99.md) with historical background (critical edition by Shlomo Buber, Vilna 1893) and Dataview table.

### 2. Source #5 (`ספר הברית - חלק א מאמר י"א תבנית כל הדצח"ם - פרק ז`)
- **Issue**: Filename generated with double-dash stutter `ספר הברית - - חלק א...`, attributed to book title `[[ספר הברית]]` and flagged `audit_needed: true`.
- **Resolution**: Attributed to author **`[[רבי פנחס אליהו הורביץ]]`** (Rabbi Pinchas Eliyahu Horowitz of Vilna, 1765–1821). Standardized note to **`רבי פנחס אליהו הורביץ - ספר הברית - חלק א מאמר י''א תבנית כל הדצח''ם - פרק ז.md`**.
- **Author Note**: Created [`222 Authors/רבי פנחס אליהו הורביץ.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%A4%D7%A0%D7%97%D7%A1%20%D7%90%D7%94%D7%99%D7%94%D7%95%20%D7%94%D7%95%D7%A8%D7%91%D7%99%D7%A5.md); purged fallback `222 Authors/ספר הברית.md`.

### 3. Source #6 (`http://en.wikipedia.org/wiki/Beta_Israel#Origins`)
- **Issue**: URL triggered punctuation scramble check `[a-zA-Z][,.;/][a-zA-Z]`, causing `is_line_english()` to return `False`. Reverse-QWERTY decoded into gibberish `דמןעןרO#ךקשרדI_שאקB-ןלן׳-ערםץשןגקפןלן׳ץמק---פאאי` and flagged `audit_needed: true`.
- **Resolution**: Renamed to **`Wikipedia - Beta Israel - Origins.md`**, attributed to **`[[Wikipedia]]`**, book `Beta Israel`, location `Origins`. Merged page 1 crop (`melachim 1.10_p1_s6.png`) and page 2 continuation crop (`melachim 1.10_p2_s1.png`).
- **Author Note**: Created [`222 Authors/Wikipedia.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/Wikipedia.md) with aliases; purged corrupt fallback notes (`דמןעןרO...`).

### 4. Phantom Source #7 (Trailing `19:15.` on Page 2)
- **Issue**: The last line of the Wikipedia text spilled onto page 2 as `19:15.` (part of verse citations `Job 6:19; Psalms 72:10, 15`). Because it matched `^\(?\s*\d{1,2}\s*:` (`19:`), the parser treated it as a new numbered source, creating phantom note `333 Sources/מקור.md` and shifting all subsequent source numbers on the sheet by +1.
- **Resolution**: Purged phantom note `333 Sources/מקור.md` and fallback profile `222 Authors/מקור.md`. Fixed page numbering back to 13 sources.

### 5. Source #7 (PDF #7: `ספר חסידים (מרגליות) (ברית עולם ושומר הברית) סימן אלף יט`)
- **Issue**: Extracted as `author='ספר חסידים'` and flagged `audit_needed: true`.
- **Resolution**: Renamed to **`רבי יהודה החסיד - ספר חסידים - ברית עולם ושומר הברית - סימן אלף יט.md`**, attributed to canonical author **`[[רבי יהודה החסיד]]`**.
- **Author Note**: Created [`222 Authors/רבי יהודה החסיד.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%99%D7%94%D7%95%D7%93%D7%94%20%D7%94%D7%97%D7%A1%D7%99%D7%93.md); purged fallback `222 Authors/ספר חסידים.md`.

### 6. Source #8 (PDF #8: `ספר השל"ה הקדוש - מסכת תענית - דרוש לפרשת מטות (ב)`)
- **Issue**: Extracted as `author='ספר השל"ה'`, `book='הקדוש - מסכת תענית...'` and flagged `audit_needed: true`.
- **Resolution**: Renamed to **`של''ה - של''ה מסכת תענית - דרוש לפרשת מטות.md`**, attributed to existing canonical author **`[[של''ה]]`**.
- **Author Note**: Enriched existing [`222 Authors/של''ה.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A9%D7%9C''%D7%94.md); purged fallback `222 Authors/ספר השל''ה.md`.

---

## 2. Full Sheet Verification (13/13)

| # | Canonical Title | Author | Status | Notes |
|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת בבא בתרא - דף טו עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout |
| 2 | `מהרש''א - על בבא בתרא - דף טו-ב` | [[מהרש''א]] | ✅ Verified | Clean 2-header layout |
| 3 | `מדרש משלי - פרשה א` | [[מדרש משלי]] | 🔧 **Fixed** | Attributed to canonical Midrash Mishlei |
| 4 | `פסיקתא רבתי - פרשה לג - ד''ה דבר אחר אנכי` | [[פסיקתא רבתי]] | ✅ Verified | Clean 2-header layout |
| 5 | `רבי פנחס אליהו הורביץ - ספר הברית - חלק א מאמר י''א תבנית כל הדצח''ם - פרק ז` | [[רבי פנחס אליהו הורביץ]] | 🔧 **Fixed** | Fixed double-dash title, mapped to author |
| 6 | `Wikipedia - Beta Israel - Origins` | [[Wikipedia]] | 🔧 **Fixed** | Decoded English URL, combined 2 crops |
| 7 | `רבי יהודה החסיד - ספר חסידים - ברית עולם ושומר הברית - סימן אלף יט` | [[רבי יהודה החסיד]] | 🔧 **Fixed** | Re-numbered (was #8), mapped to author |
| 8 | `של''ה - של''ה מסכת תענית - דרוש לפרשת מטות` | [[של''ה]] | 🔧 **Fixed** | Re-numbered (was #9), mapped to Shelah |
| 9 | `מדרש רבה - אסתר רבה - פרשה א` | [[מדרש רבה]] | ✅ Re-numbered | Was #10 due to phantom note |
| 10 | `תוספות - מסכת יומא - דף נד עמוד ב` | [[תוספות]] | ✅ Re-numbered | Was #11 due to phantom note |
| 11 | `תלמוד בבלי - מסכת סנהדרין - דף כא עמוד ב` | [[תלמוד בבלי]] | ✅ Preserved | **User study notes intact & preserved** |
| 12 | `תלמוד ירושלמי - מסכת סנהדרין - פרק ב דף כ טור ג -ה''ו` | [[תלמוד ירושלמי]] | ✅ Re-numbered | Was #13 due to phantom note |
| 13 | `מדרש תנחומא - פרשת וארא - סימן ה` | [[מדרש תנחומא]] | ✅ Re-numbered | Was #14 due to phantom note |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **English Detection & Web URLs (`is_line_english`)**:
   - Web URLs (`https?://`, `www.`, `.org`, `.com`) are explicitly exempted from the QWERTY scramble punctuation check, preventing web citations from being reverse-translated into corrupt Hebrew strings.
   - Added `'wikipedia'`, `'origins'`, `'israel'`, `'beta'` to `COMMON_ENG_WORDS`.

2. **Wikipedia Citation Handling (`parse_citation`)**:
   - Added native regex matching for Wikipedia URLs (`https?://(?:[a-z]+\.)?wikipedia\.org/wiki/([^#\s]+)(?:#([^\s]+))?`), automatically extracting author `Wikipedia`, article title as book, and anchor section as location with `audit_needed=False`.

3. **Multi-Word & Canonical Sefer Mappings (`RESPONSA_SPECIAL_MAP` & `AUTHOR_CANONICAL_MAP`)**:
   - Added `ספר הברית` $\to$ `('רבי פנחס אליהו הורביץ', 'ספר הברית')`.
   - Added `ספר חסידים` $\to$ `('רבי יהודה החסיד', 'ספר חסידים')`.
   - Added `ספר השל"ה` / `השל"ה` $\to$ `("של''ה", "של''ה")`.
   - Added `מדרש משלי` $\to$ `('מדרש משלי', 'מדרש משלי')`.
   - Added `דרוש` and `פרשה` handling to `RESPONSA_SPECIAL_MAP` location matching; cleans honorifics like `הקדוש` from intermediate book strings.
   - Added parenthesized Hebrew section suffix stripper `\s*[\(\)][0-9א-ת\s]+[\(\)]\s*$` to safely remove sheet markers like `(ב)` without truncating trailing Hebrew letters of legitimate locations (e.g. `עמוד ב`, `פרשה א`).
   - Added mappings for `הלכות קטנות` $\to$ `רבי יעקב חגיז`, `נודע ביהודה` $\to$ `רבי יחזקאל לנדא`, and `ראבי"ה` $\to$ `רבי אליעזר בן יואל הלוי`.

4. **Numbered Header Regex & Continuation Protection (`extract_sources_and_images`)**:
   - Guarded colon separator in header numbering: `^\(?\s*\d{1,2}\s*(?:[\)\.\-]|:(?!\d))` ensures timestamps/citations like `19:15.` are not treated as numbered headers.
   - Required `has_words = bool(re.search(r'[\u0590-\u05FFa-zA-Z]{2,}', raw_decoded))` for any block to qualify as a source header.
   - Allowed blocks at $y > 35$ before the first header on continuation pages to be captured as continuation crops (`p2_cont`), preventing trailing lines from becoming orphan sources.

5. **Dibur Hamatchil (DH) Colon Support**:
   - Expanded DH regex to `r'^(.*?)[\-\.:](?:\s|$)'` to naturally extract leading phrases terminating with a colon (e.g., `רב יהודה רמי:`, `רב יצחק רמי:`, `תנו רבנן:`).

---

## 4. Source 11 Differentiation (`Sanhedrin 21b`)

- Both `melachim 1.4 5` and `melachim 1.10` cite **Gemara Sanhedrin 21b**, but cover distinct passages:
  - **Portion 1 (`melachim 1.4 5`, `melachim 1.4 5_p2_s3.png`)**: Begins `רב יהודה רמי:` (addressing King Solomon's 40,000 stalls vs 4,000 stalls of horses). User study notes retained beneath this heading.
  - **Portion 2 (`melachim 1.10`, `melachim 1.10_p2_s5.png`)**: Begins `רב יצחק רמי:` (addressing silver accounted as stones in Jerusalem, marriage to Pharaoh's daughter, and the reasons of Torah).
- **Resolution**:
  - In [`333 Sources/תלמוד בבלי - מסכת סנהדרין - דף כא עמוד ב.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%52%D7%9C%D7%9E%D7%95%D7%93%20%D7%91%D7%91%D7%9C%D7%99%20-%20%D7%9E%D7%A1%D7%93%D7%52%20%D7%A1%D7%A0%D7%94%D7%93%D7%50%D7%99%D7%9F%20-%20%D7%93%D7%A3%20%D7%9B%D7%90%20%D7%A2%D7%9E%D7%95%D7%93%20%D7%91.md), both crops are displayed under `### Source Image`, followed by separate subsections: `### רב יהודה רמי` (with existing user study notes) and `### רב יצחק רמי`.
  - In [`111 Source Sheets/melachim 1.4 5.md`](file:///home/sean/Obsidian/Rapp/111%20Source%20Sheets/melachim%201.4%205.md#L45): embed updated to `![[תלמוד בבלי - מסכת סנהדרין - דף כא עמוד ב#רב יהודה רמי]]`.
  - In [`111 Source Sheets/melachim 1.10.md`](file:///home/sean/Obsidian/Rapp/111%20Source%20Sheets/melachim%201.10.md#L45): embed updated to `![[תלמוד בבלי - מסכת סנהדרין - דף כא עמוד ב#רב יצחק רמי]]`.

---

## 5. Authors Directory Cleanup (`222 Authors/`)

- **Purged 14 Orphan Corrupt Fallbacks**: Removed zero-reference truncated author token files (`ביאור.md`, `מנחת.md`, `משך.md`, `ספר יערות.md`, `ספר מורה.md`, `ספר מנחת.md`, `קובץ.md`, `שו''ת בית.md`, `שו''ת הלכות.md`, `שו''ת יביע.md`, `שו''ת נודע.md`, `שו''ת רדב''ז.md`, `הר צבי.md`, `מדרש.md`).
- **Standardized Frontmatter & Dataview Blocks**: Fixed missing YAML, tags, or Dataview queries across 7 legitimate author notes (`הרבי מסאטמאר.md`, `משך חכמה.md`, `רדב''ז.md`, `רבי אליעזר בן יואל הלוי.md`, `רבי יחזקאל לנדא.md`, `רבי יעקב חגיז.md`, `שולחן ערוך הרב.md`).
- **Fixed Citation Link**: Updated single non-standard link `author: "[[Gemara]]"` in `תלמוד בבלי - מסכת חגיגה - דף יג עמוד א.md` to `author: "[[תלמוד בבלי]]"`.
- **Author Invariant**: 100% of the 202 canonical author notes in `222 Authors/` strictly follow vault formatting, and 100% of source notes in `333 Sources/` link to valid author notes.

---

## 6. Verification Results

- **Parse Test**: `process_source_sheets.py` extracts exactly **13 sources** from `melachim 1.10.pdf` with **0 audit flags**.
- **Idempotency**: All 13 sources match existing vault files in `333 Sources/` with `match_existing_source()`, resulting in 0 duplicate files.
- **Regression Check**:
  - `melachim 1.9.pdf`: 14 sources, 0 audit flags.
  - `melachim 1.8.pdf`: 19 sources, 0 audit flags.
- **Vault Status**: 0 broken embeds, 0 missing images, 0 missing author notes, 0 audit flags remaining vault-wide.
