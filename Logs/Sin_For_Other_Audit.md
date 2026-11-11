# Sin For Other Source Sheet Audit

## Summary
Audited `111 Source Sheets/sin for other.md` (`000 Source PDFs/sin for other.pdf`, Subject: *Gemara*, Maseches Shabbos 4a / Eruvin 32b, Fall 2026 Final) — 14 embedded sources.
1. **Resolved Flagged Sources (#7, #8, #12)**:
   - **Source #7 (`ספר נחלת שבעה תשובות סימן פג`)**: Resolved from fallback author `[[ספר נחלת]]` and book `שבעה תשובות`. Attributed to canonical author **`[[רבי שמואל הלוי]]`** (Rabbi Shmuel ben David Moshe HaLevi, Baal Nachalat Shiva), book **`שו''ת נחלת שבעה`**, location **`סימן פג`**. Created canonical author profile [`222 Authors/רבי שמואל הלוי.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%50%D7%91%D7%99%20%D7%A9%D7%9E%D7%55%D7%90%D7%9C%20%D7%94%D7%9C%D7%95%D7%99.md) and purged fallback author note `222 Authors/ספר נחלת.md`.
   - **Source #8 (`ברכי יוסף אורח חיים סימן שו ס"ק טז`)**: Resolved from fallback author `[[ברכי]]` and book `יוסף אורח חיים`. Attributed to canonical author **`[[חיד''א]]`** (linking to existing canonical [`222 Authors/חיד''א.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%97%D7%99%D7%93''%D7%90.md)), book **`ברכי יוסף אורח חיים`**, location **`סימן שו ס''ק טז`**. Purged fallback author note `222 Authors/ברכי.md`.
   - **Source #12 (`שו"ת שבט הלוי חלק ח סימן קצג )ב(`)**: Resolved from fallback author `[[שו''ת שבט]]` and book `הלוי חלק ח`. Attributed to canonical author **`[[רבי שמואל הלוי וואזנר]]`** (Shevet HaLevi), book **`שו''ת שבט הלוי`**, location **`חלק ח סימן קצג אות ב`** (preserving the section identifier `)ב(` as `אות ב`). Created canonical author profile [`222 Authors/רבי שמואל הלוי וואזנר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%50%D7%91%D7%99%20%D7%A9%D7%9E%D7%55%D7%90%D7%9C%20%D7%94%D7%9C%D7%95%D7%99%20%D7%95%D7%95%D7%90%D7%96%D7%A0%D7%A8.md) and purged fallback author note `222 Authors/שו''ת שבט.md`.
2. **Fixed Shemirat Shabbat Kehilchatah (#13)**:
   - Fixed erroneous book fallback `מקור` and stripped mangled Dibur Hamatchil anchor (`נקרעו חוטי העירוב המקיפים את העיר והמשמשים צורת`, caused by regex splitting on the hyphen in the compound word `צורת-הפתח`). Standardized to canonical note **`שמירת שבת כהלכתה - פרק יז אות לד.md`** under author **`[[שמירת שבת כהלכתה]]`** and clean 2-header layout.
3. **Multi-Sheet Note Partitioning (#11 Chashukei Chemed Shabbat 4a)**:
   - Disambiguated and partitioned [`333 Sources/הרב יצחק זילברשטיין - חשוקי חמד מסכת שבת - דף ד עמוד א.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%94%D7%A8%D7%91%20%D7%99%D7%A6%D7%97%D7%A7%20%D7%96%D7%99%D7%9C%D7%91%D7%A8%D7%A9%D7%98%D7%99%D7%99%D7%9F%20-%20%D7%97%D7%A9%D7%55%D7%A7%D7%99%20%D7%97%D7%9E%D7%93%20%D7%9E%D7%A1%D7%93%D7%AA%20%D7%A9%D7%91%D7%AA%20-%20%D7%93%D7%A3%20%D7%93%20%D7%A2%D7%9E%D7%55%D7%93%20%D7%90.md) between its usage in `sin to fix` (question on baking in an electric oven) and `sin for other` (question on removing a refrigerator light bulb for elderly residents). Partitioned with `### sin to fix` and `### sin for other` subheadings, updating embed links on both master sheets accordingly.
4. **Multi-Page Continuation Integrity (#5 & #11)**:
   - Verified **בית יוסף אורח חיים סימן שו** spans Page 1 and Page 2 (`sin for other_p1_s5.png` + continuation crop `sin for other_p2_cont.png`).
   - Verified **חשוקי חמד מסכת שבת דף ד עמוד א** spans Page 2 and Page 3 (`sin for other_p2_s6.png` + continuation crop `sin for other_p3_cont.png`).
5. **Script Root-Cause Patches**: Patched [`999 Scripts/process_source_sheets.py`](file:///home/sean/Obsidian/Rapp/999%20Scripts/process_source_sheets.py) with canonical author mappings, `RESPONSA_SPECIAL_MAP` entries for *Shevet HaLevi*, *Nachalat Shiva*, and *Birkei Yosef*, trailing Hebrew section extraction (`(ב)` $\to$ `אות ב`), fallback book resolution for *Shemirat Shabbat Kehilchatah*, and Dibur Hamatchil guards preventing halacha codes from false-positive DH truncation.
6. **Result**: **0 audit warnings, 0 broken embeds, 0 missing images, 0 missing authors.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #7 (`ספר נחלת שבעה תשובות סימן פג`)
- **Issue**: `נחלת שבעה` / `ספר נחלת שבעה` was not registered in `RESPONSA_SPECIAL_MAP` or `AUTHOR_CANONICAL_MAP`. The parser fell back to splitting on whitespace: author `[[ספר נחלת]]` and book `שבעה תשובות`, flagging `audit_needed: true` (*"Author fell back to token 'ספר נחלת'"*) and `⚠️ (Needs Audit)` in the sheet, while creating corrupt fallback profile [`222 Authors/ספר נחלת.md`].
- **Resolution**:
  - Attributed to canonical author **`[[רבי שמואל הלוי]]`** (Rabbi Shmuel ben David Moshe HaLevi, Baal Nachalat Shiva).
  - Standardized note to **`רבי שמואל הלוי - שו''ת נחלת שבעה - סימן פג.md`**, book `שו''ת נחלת שבעה`, location `סימן פג`.
  - Created canonical author note [`222 Authors/רבי שמואל הלוי.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%50%D7%91%D7%99%20%D7%A9%D7%9E%D7%55%D7%90%D7%9C%20%D7%94%D7%9C%D7%95%D7%99.md); purged fallback `222 Authors/ספר נחלת.md`.
  - Updated embed in `sin for other.md` to `![[רבי שמואל הלוי - שו''ת נחלת שבעה - סימן פג#רבי שמואל הלוי - שו''ת נחלת שבעה - סימן פג]]`.

### 2. Source #8 (`ברכי יוסף אורח חיים סימן שו ס"ק טז`)
- **Issue**: `ברכי יוסף` was not mapped in `RESPONSA_SPECIAL_MAP` or `AUTHOR_CANONICAL_MAP`. It fell back to author `[[ברכי]]` and book `יוסף אורח חיים`, flagging `audit_needed: true` (*"Author fell back to token 'ברכי'"*), creating corrupt profile [`222 Authors/ברכי.md`].
- **Resolution**:
  - Attributed to the Chida via canonical author **`[[חיד''א]]`** (linking to existing [`222 Authors/חיד''א.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%97%D7%99%D7%93''%D7%90.md)), book `ברכי יוסף אורח חיים`, location `סימן שו ס''ק טז`.
  - Standardized note to **`חיד''א - ברכי יוסף אורח חיים - סימן שו ס''ק טז.md`**, headline `### חיד''א - ברכי יוסף אורח חיים - סימן שו ס''ק טז`.
  - Purged corrupt fallback note `222 Authors/ברכי.md`.
  - Updated embed in `sin for other.md` to `![[חיד''א - ברכי יוסף אורח חיים - סימן שו ס''ק טז#חיד''א - ברכי יוסף אורח חיים - סימן שו ס''ק טז]]`.

### 3. Source #12 (`שו"ת שבט הלוי חלק ח סימן קצג )ב(`)
- **Issue**: `שבט הלוי` was not in `RESPONSA_SPECIAL_MAP`. It fell back to author `[[שו''ת שבט]]` and book `הלוי חלק ח`, flagging `audit_needed: true` (*"Author fell back to token 'שו"ת שבט'"*), creating corrupt profile [`222 Authors/שו''ת שבט.md`]. Additionally, trailing section indicator `)ב(` was stripped by generic parenthesis regex.
- **Resolution**:
  - Attributed to canonical posek **`[[רבי שמואל הלוי וואזנר]]`**, book `שו''ת שבט הלוי`, location `חלק ח סימן קצג אות ב`.
  - Standardized note to **`רבי שמואל הלוי וואזנר - שו''ת שבט הלוי - חלק ח סימן קצג אות ב.md`**, headline `### רבי שמואל הלוי וואזנר - שו''ת שבט הלוי - חלק ח סימן קצג אות ב`.
  - Created canonical author profile [`222 Authors/רבי שמואל הלוי וואזנר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%50%D7%91%D7%99%20%D7%A9%D7%9E%D7%55%D7%90%D7%9C%20%D7%94%D7%9C%D7%95%D7%99%20%D7%95%D7%95%D7%90%D7%96%D7%A0%D7%A8.md); purged fallback `222 Authors/שו''ת שבט.md`.
  - Updated embed in `sin for other.md` to `![[רבי שמואל הלוי וואזנר - שו''ת שבט הלוי - חלק ח סימן קצג אות ב#רבי שמואל הלוי וואזנר - שו''ת שבט הלוי - חלק ח סימן קצג אות ב]]`.

### 4. Source #13 (`שמירת שבת כהלכתה פרק יז אות לד`)
- **Issue**:
  1. Book name defaulted to fallback `מקור` when author matched `שמירת שבת כהלכתה`.
  2. Generic Dibur Hamatchil regex matched the hyphen in `צורת - הפתח`, erroneously extracting `נקרעו חוטי העירוב המקיפים את העיר והמשמשים צורת` as a D"H anchor.
- **Resolution**:
  - Standardized note to **`שמירת שבת כהלכתה - פרק יז אות לד.md`**, author `[[שמירת שבת כהלכתה]]`, book `שמירת שבת כהלכתה`, location `פרק יז אות לד`.
  - Replaced mangled D"H anchor with standard headline `### שמירת שבת כהלכתה - פרק יז אות לד`.
  - Updated embed in `sin for other.md` to `![[שמירת שבת כהלכתה - פרק יז אות לד#שמירת שבת כהלכתה - פרק יז אות לד]]`.

### 5. Source #11 (Chashukei Chemed Multi-Sheet Partitioning)
- **Convention**: In source notes shared across multiple source sheets with distinct shiur topics, content headings are partitioned by sheet name (e.g. `### sin to fix`, `### sin for other`), matching the vault convention established in Berachot 10b, Sanhedrin 22a, and Sanhedrin 102a.
- **Resolution**:
  - In [`333 Sources/הרב יצחק זילברשטיין - חשוקי חמד מסכת שבת - דף ד עמוד א.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%94%D7%A8%D7%91%20%D7%99%D7%A6%D7%97%D7%A7%20%D7%96%D7%99%D7%9C%D7%91%D7%A8%D7%A9%D7%98%D7%99%D7%99%D7%9F%20-%20%D7%97%D7%A9%D7%55%D7%A7%D7%99%20%D7%97%D7%9E%D7%93%20%D7%9E%D7%A1%D7%93%D7%AA%20%D7%A9%D7%91%D7%AA%20-%20%D7%93%D7%A3%20%D7%93%20%D7%A2%D7%9E%D7%55%D7%93%20%D7%90.md), preserved crops from both sheets under `### Source Image` (`sin for other_p2_s6.png`, `sin for other_p3_cont.png`, and `sin to fix_p3_s3.png`).
  - Added partitioned subheadings:
    - `### sin to fix`: for notes on baking bread in an electric oven.
    - `### sin for other`: for notes on unscrewing a refrigerator light bulb for elderly residents.
  - Updated embed in [`111 Source Sheets/sin to fix.md`](file:///home/sean/Obsidian/Rapp/111%20Source%20Sheets/sin%20to%20fix.md) to `![[הרב יצחק זילברשטיין - חשוקי חמד מסכת שבת - דף ד עמוד א#sin to fix]]`.
  - Updated embed in [`111 Source Sheets/sin for other.md`](file:///home/sean/Obsidian/Rapp/111%20Source%20Sheets/sin%20for%20other.md) to `![[הרב יצחק זילברשטיין - חשוקי חמד מסכת שבת - דף ד עמוד א#sin for other]]`.

---

## 2. Full Sheet Verification (14/14)

| # | Canonical Title | Author | Status | Notes |
|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת שבת - דף ד עמוד א` | [[תלמוד בבלי]] | ✅ Verified | D"H `#גופא' בעי רב ביבי בר אביי`; crop `p1_s1` |
| 2 | `תלמוד בבלי - מסכת עירובין - דף לב עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | D"H `#רבי סבר`; crop `p1_s2` |
| 3 | `תוספות - מסכת שבת - דף ד עמוד א ד''ה וכי אומרים` | [[תוספות]] | ✅ Verified | Clean 2-header layout; crop `p1_s3` |
| 4 | `תוספות - מסכת עירובין - דף לב עמוד ב ד''ה ולא ליעבד` | [[תוספות]] | ✅ Verified | Clean 2-header layout; crop `p1_s4` |
| 5 | `בית יוסף - אורח חיים - סימן שו` | [[בית יוסף]] | ✅ Verified | Multi-crop intact (`p1_s5` + `p2_cont`) |
| 6 | `שולחן ערוך - אורח חיים - סימן שו סעיף יד` | [[שולחן ערוך]] | ✅ Verified | Clean 2-header layout; crop `p2_s1` |
| 7 | `רבי שמואל הלוי - שו''ת נחלת שבעה - סימן פג` | [[רבי שמואל הלוי]] | 🔧 **Fixed** | Attributed to Baal Nachalat Shiva; fallback purged; audit cleared |
| 8 | `חיד''א - ברכי יוסף אורח חיים - סימן שו ס''ק טז` | [[חיד''א]] | 🔧 **Fixed** | Attributed to Chida; fallback purged; audit cleared |
| 9 | `מגן אברהם - אורח חיים - סימן רנד ס''ק כא` | [[מגן אברהם]] | ✅ Verified | Clean 2-header layout; crop `p2_s4` |
| 10 | `משנה ברורה - שער הציון - סימן שו ס''ק מו` | [[משנה ברורה]] | ✅ Verified | Clean 2-header layout; crop `p2_s5` |
| 11 | `הרב יצחק זילברשטיין - חשוקי חמד מסכת שבת - דף ד עמוד א` | [[הרב יצחק זילברשטיין]] | 🔧 **Fixed** | Multi-crop intact (`p2_s6` + `p3_cont` + `sin to fix_p3_s3`); partitioned headings `#sin to fix` & `#sin for other` |
| 12 | `רבי שמואל הלוי וואזנר - שו''ת שבט הלוי - חלק ח סימן קצג אות ב` | [[רבי שמואל הלוי וואזנר]] | 🔧 **Fixed** | Attributed to Shevet HaLevi; section `אות ב` preserved; audit cleared |
| 13 | `שמירת שבת כהלכתה - פרק יז אות לד` | [[שמירת שבת כהלכתה]] | 🔧 **Fixed** | Purged fallback book `מקור` & mangled D"H; standardized 2-header layout |
| 14 | `ציץ אליעזר - חלק ו - סימן ג` | [[ציץ אליעזר]] | ✅ Verified | Clean 2-header layout; crop `p3_s3` |

---

## 3. Parser Root Cause Patches (`999 Scripts/process_source_sheets.py`)

1. **Shevet HaLevi, Nachalat Shiva, and Birkei Yosef Support**:
   - Added `'שבט הלוי'`, `'שו"ת שבט הלוי'`, `'רבי שמואל הלוי וואזנר'`, `'ברכי יוסף'`, `'נחלת שבעה'`, `'שו"ת נחלת שבעה'`, `'ספר נחלת שבעה'`, and `'רבי שמואל הלוי'` to `KNOWN_AUTHORS` and `KNOWN_HEADER_KEYWORDS`.
   - Added canonical author mappings to `AUTHOR_CANONICAL_MAP`:
     - `'שבט הלוי'` / `'שו"ת שבט הלוי'` $\to$ `'רבי שמואל הלוי וואזנר'`
     - `'ברכי יוסף'` $\to$ `"חיד''א"`
     - `'נחלת שבעה'` / `'ספר נחלת שבעה'` / `'שו"ת נחלת שבעה'` $\to$ `'רבי שמואל הלוי'`
   - Registered in `RESPONSA_SPECIAL_MAP`:
     - `'שבט הלוי'`: `('רבי שמואל הלוי וואזנר', 'שו"ת שבט הלוי')`
     - `'נחלת שבעה'` / `'ספר נחלת שבעה'`: `('רבי שמואל הלוי', 'שו"ת נחלת שבעה')`
     - `'ברכי יוסף'`: `("חיד''א", 'ברכי יוסף')`
2. **Trailing Responsa Section Identification (`(ב)` $\to$ `אות ב`)**:
   - In `parse_citation`: captured trailing single Hebrew letter enclosed in parentheses (e.g. `)ב(` or `(ב)`) prior to generic parenthesis stripping, enriching `location` with `אות {ot}` when not already present.
3. **Shemirat Shabbat Kehilchatah Book Fallback Fix**:
   - In `parse_citation`: added explicit handling ensuring that when `author == "שמירת שבת כהלכתה"`, `book` resolves to `"שמירת שבת כהלכתה"` instead of falling back to `"מקור"`.
4. **Halacha Code Dibur Hamatchil Guard**:
   - In `extract_sources_and_images`: guarded candidate D"H extraction so that halachic codes (`שמירת שבת כהלכתה`, `שולחן ערוך`, `רמב''ם`, `חיי אדם`, `קיצור שולחן ערוך`) do not treat body text sentences containing hyphens (such as `צורת - הפתח`) as Dibur Hamatchil anchors, and constrained candidate D"H word length to $\le 4$ words.
