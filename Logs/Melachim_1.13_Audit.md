# Melachim 1.13 Source Sheet Audit

## Summary
Audited `111 Source Sheets/melachim 1.13.md` (`000 Source PDFs/melachim 1.13.pdf`, Subject: *Navi*, Fall 2026 Final) — 14 embedded sources. Verified every citation against the decoded Davka font text stream and PDF layout, resolved all 4 flagged/corrupt sources (**פרקי דרבי אליעזר**, **סנהדרי קטנה**, **ספר העקרים**, and **ערוך לנר**), created canonical author profiles in `222 Authors/` (**פרקי דרבי אליעזר**, **רבי אברהם יהושע העשיל בורנשטיין**), updated aliases on canonical author notes (**רב יוסף אלבו**, **רבי יעקב עטלינגר**), purged corrupt fallback author profiles (`מקור.md`, `סנהדרי.md`, `ספר העקרים.md`, `ערוך לנר.md`), verified continuation crop `melachim 1.13_p2_cont.png` for Sefer HaIkkarim, preserved user study notes under Sanhedrin 102a (Source #12) and Sanhedrin 101b (Source #14), and patched all root causes in `process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #3 (`פרקי דרבי אליעזר )היגר( - "חורב"  פרק יז`)
- **Issue**: Unanchored regex `(דף|פרק|...)` matched the prefix `פרק` inside the title word `פרקי`, causing the location parser to consume the entire title and leave the author and book empty. The parser fell back to `author='מקור'` and `book='מקור'`, generated corrupt fallback author note `222 Authors/מקור.md`, and flagged the source `audit_needed: true` (*"Author fell back to token 'מקור'"*).
- **Resolution**: Attributed to canonical midrashic work **`[[פרקי דרבי אליעזר]]`**. Standardized note to **`פרקי דרבי אליעזר - חורב - פרק יז.md`**, book `חורב`, location `פרק יז`.
- **Author Note**: Created [`222 Authors/פרקי דרבי אליעזר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A4%D7%A8%D7%A7%D7%99%20%D7%93%D7%A8%D7%91%D7%99%20%D7%90%D7%9C%D7%99%D7%A2%D7%96%D7%A8.md) with scholarly background and aliases `[פרקי דרבי אליעזר, פרקי דר''א]`; purged fallback `222 Authors/מקור.md`.

### 2. Source #6 (`סנהדרי קטנה סנהדרין דף פט עמוד ב`)
- **Issue**: Extracted as `author='סנהדרי'`, `book='קטנה סנהדרין'`, and flagged `audit_needed: true` (*"Author fell back to token 'סנהדרי'"*), generating corrupt fallback author `222 Authors/סנהדרי.md`.
- **Resolution**: Identified work as *Sanhedri Ketana* on Tractate Sanhedrin by Rabbi Avraham Yehoshua Heschel Bornstein (Av Beis Din of Brezin, Poland, 1903). Attributed to canonical author **`[[רבי אברהם יהושע העשיל בורנשטיין]]`**. Standardized note to **`רבי אברהם יהושע העשיל בורנשטיין - סנהדרי קטנה על סנהדרין - דף פט עמוד ב.md`**, book `סנהדרי קטנה על סנהדרין`, location `דף פט עמוד ב`.
- **Author Note**: Created [`222 Authors/רבי אברהם יהושע העשיל בורנשטיין.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%90%D7%91%D7%A0%D7%94%D7%9D%20%D7%99%D7%94%D7%95%D7%A9%D7%A2%20%D7%94%D7%A2%D7%A9%D7%99%D7%9C%20%D7%91%D7%95%D7%A8%D7%A0%D7%A9%D7%98%D7%99%D7%99%D7%9F.md) with biography and aliases; purged fallback `222 Authors/סנהדרי.md`.

### 3. Source #7 (`ספר העקרים - מאמר שלישי פרק יח`)
- **Issue**: Extracted as `author='ספר העקרים'`, `book='מקור'`, and flagged `audit_needed: true` (*"Author fell back to token 'ספר העקרים'"*), generating corrupt fallback author `222 Authors/ספר העקרים.md`.
- **Resolution**: Attributed to canonical posek **`[[רב יוסף אלבו]]`** (linking to existing [`222 Authors/רב יוסף אלבו.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%20%D7%99%D7%95%D7%A1%D7%A3%20%D7%90%D7%9C%D7%91%D7%95.md)). Standardized note to **`רב יוסף אלבו - ספר העיקרים - מאמר שלישי פרק יח.md`**, book `ספר העיקרים`, location `מאמר שלישי פרק יח`. Verified continuation crop `melachim 1.13_p2_cont.png` alongside `melachim 1.13_p1_s7.png` under `### Source Image`. Added aliases `[יוסף אלבו, ספר העקרים, ספר העיקרים, בעל העיקרים]` to author note; purged fallback `222 Authors/ספר העקרים.md`.

### 4. Source #13 (`ערוך לנר סנהדרין - דף קב/א`)
- **Issue**: Extracted as `author='ערוך לנר'`, `book='סנהדרין'`, and flagged `audit_needed: true` (*"Author fell back to token 'ערוך לנר'"*), generating corrupt fallback author `222 Authors/ערוך לנר.md`.
- **Resolution**: Attributed to canonical author **`[[רבי יעקב עטלינגר]]`** (linking to existing [`222 Authors/רבי יעקב עטלינגר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%99%D7%A2%D7%A7%D7%91%20%D7%A2%D7%98%D7%9C%D7%99%D7%A0%D7%92%D7%A8.md)). Standardized note to **`רבי יעקב עטלינגר - ערוך לנר על סנהדרין - דף קב עמוד א.md`**, book `ערוך לנר על סנהדרין`, location `דף קב עמוד א`. Added aliases `[ערוך לנר, בעל ערוך לנר, יעקב עטלינגר, רבי יעקב יוקב עטלינגר, בנין ציון]` to author note; purged fallback `222 Authors/ערוך לנר.md`.

### 5. Multi-Source Preservations (Sanhedrin 102a & Sanhedrin 101b)
- **Sanhedrin 102a (Source #12)**: Preserved all existing user study annotations intact in [`333 Sources/תלמוד בבלי - מסכת סנהדרין - דף קב עמוד א.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%AA%D7%94%D7%9E%D7%95%D7%93%20%D7%91%D7%91%D7%94%D7%99%20-%20%D7%9E%D7%A1%D7%93%D7%AA%20%D7%A1%D7%A0%D7%94%D7%93%D7%A8%D7%99%D7%9F%20-%20%D7%93%D7%A3%20%D7%A7%D7%91%20%D7%A2%D7%9E%D7%95%D7%93%20%D7%90.md).
- **Sanhedrin 101b (Source #14)**: Preserved existing study notes under `### תנו רבנן`, `### אמר רבי יוחנן`, `### אמר רב נחמן`, and `### מאי ויועץ? אמר רבי יהודה`, while cleanly anchoring Melachim 1.13 excerpt under `### ומנא לן דלא אתי לעלמא דאתי`.

---

## 2. Full Sheet Verification (14/14)

| # | Canonical Title | Author | Status | Notes |
|---|---|---|---|---|
| 1 | `רמב''ם - הלכות יסודי התורה - פרק ז הלכה ז` | [[רמב''ם]] | ✅ Verified | Clean 2-header layout |
| 2 | `מדרש רבה - שיר השירים רבה - פרשה ב` | [[מדרש רבה]] | ✅ Verified | Clean 2-header layout |
| 3 | `פרקי דרבי אליעזר - חורב - פרק יז` | [[פרקי דרבי אליעזר]] | 🔧 **Fixed** | Resolved `פרק` regex truncation; author profile created |
| 4 | `מדרש תנחומא - פרשת תולדות - סימן יב` | [[מדרש תנחומא]] | ✅ Verified | Clean 2-header layout |
| 5 | `תלמוד בבלי - מסכת סנהדרין - דף פט עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean DH anchor `#נביא שעבר על דברי עצמו` |
| 6 | `רבי אברהם יהושע העשיל בורנשטיין - סנהדרי קטנה על סנהדרין - דף פט עמוד ב` | [[רבי אברהם יהושע העשיל בורנשטיין]] | 🔧 **Fixed** | Attributed to Rav A.Y.H. Bornstein; author profile created |
| 7 | `רב יוסף אלבו - ספר העיקרים - מאמר שלישי פרק יח` | [[רב יוסף אלבו]] | 🔧 **Fixed** | Attributed to Rav Yosef Albo; verified `p2_cont` crop |
| 8 | `רשב''א - שו''ת הרשב''א חלק א - סימן יא` | [[רשב''א]] | ✅ Verified | Clean 2-header layout |
| 9 | `רד''ק - מלכים א - פרק יג פסוק כח` | [[רד''ק]] | ✅ Verified | Clean 2-header layout |
| 10 | `רש''י - בראשית - פרק ט פסוק ה` | [[רש''י]] | ✅ Verified | Clean DH anchor `#מיד כל חיה` |
| 11 | `רמב''ן - בראשית - פרק ט פסוק ה` | [[רמב''ן]] | ✅ Verified | Clean DH anchor `#מיד כל חיה אדרשנו` |
| 12 | `תלמוד בבלי - מסכת סנהדרין - דף קב עמוד א` | [[תלמוד בבלי]] | ✅ Preserved | **User study notes intact & preserved** |
| 13 | `רבי יעקב עטלינגר - ערוך לנר על סנהדרין - דף קב עמוד א` | [[רבי יעקב עטלינגר]] | 🔧 **Fixed** | Attributed to Rav Yaakov Ettlinger; tractate & folio mapped |
| 14 | `תלמוד בבלי - מסכת סנהדרין - דף קא עמוד ב` | [[תלמוד בבלי]] | ✅ Preserved | Multi-DH anchor `#ומנא לן דלא אתי לעלמא דאתי`; previous notes intact |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Word-Boundary Protection for `פרק` in Location Matching**:
   - Replaced unanchored `|פרק|` with word-boundary lookaround `|(?<![א-ת])פרק(?![א-ת])|` in both `RESPONSA_SPECIAL_MAP` (line 843) and heuristic parser `loc_match` (line 1062).
   - Prevents titles containing `פרקי` (e.g. `פרקי דרבי אליעזר`, `פרקי אבות`) from prematurely truncating the entire book title into the location field.

2. **Pirkei DeRabbi Eliezer Mapping**:
   - Added `פרקי דרבי אליעזר` and `ספר פרקי דרבי אליעזר` to `RESPONSA_SPECIAL_MAP` mapped to `('פרקי דרבי אליעזר', 'פרקי דרבי אליעזר')`.
   - Added extraction logic for edition markers like `חורב` in `extra_clean`.
   - Added canonical mappings for `פרקי דרבי אליעזר`, `ספר פרקי דרבי אליעזר`, `פרקי דר"א`, and `פרקי דר''א` to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.

3. **Sanhedri Ketana Mapping**:
   - Added `סנהדרי קטנה` and `ספר סנהדרי קטנה` to `RESPONSA_SPECIAL_MAP` mapped to `('רבי אברהם יהושע העשיל בורנשטיין', 'סנהדרי קטנה על סנהדרין')`.
   - Added tractate extraction logic: `f"סנהדרי קטנה על {maseches}"`.
   - Added canonical mappings for `סנהדרי קטנה`, `ספר סנהדרי קטנה`, `רבי אברהם יהושע העשיל בורנשטיין`, and `אברהם יהושע העשיל בורנשטיין` to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.

4. **Sefer HaIkkarim Mapping**:
   - Added `ספר העקרים`, `ספר העיקרים`, `ספר עקרים`, `ספר עיקרים`, `העקרים`, and `העיקרים` to `RESPONSA_SPECIAL_MAP` mapped to `('רב יוסף אלבו', 'ספר העיקרים')`.
   - Added canonical mappings to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.

5. **Aruch LaNer Mapping**:
   - Added `ערוך לנר` and `ספר ערוך לנר` to `RESPONSA_SPECIAL_MAP` mapped to `('רבי יעקב עטלינגר', 'ערוך לנר על סנהדרין')`.
   - Added tractate extraction logic: `f"ערוך לנר על {maseches}"`.
   - Added canonical mappings for `ערוך לנר`, `ספר ערוך לנר`, `רבי יעקב עטלינגר`, `רבי יעקב עטלינגער`, and `יעקב עטלינגר` to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.
