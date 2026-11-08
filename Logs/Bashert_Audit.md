# Bashert Source Sheet Audit

## Summary
Audited `111 Source Sheets/bashert.md` (`000 Source PDFs/bashert.pdf`, Subject: *Machshava*, Fall 2026 Midterm) — 17 embedded sources. Fully verified every citation against the decoded Davka font text stream and sheet layout, resolved all 3 flagged/corrupt sources (**שו"ת תשב"ץ**, **פתח עינים להחיד"א**, and **ילקוט יוסף**), resolved author misattribution on **נעימת החיים** (falsely attributed to ט"ז) and **תוספות רא"ש** (falsely attributed to תוספות), standardized Ran Sanhedrin 22a citation (migrating un-normalized `דף כב ע-א` to `דף כב עמוד א` while updating both `bashert.md` and `melachim 1.1.md` embeds), created canonical author profiles in `222 Authors/` (**הרב יצחק יוסף**, **הרב חיים גרוס**), enhanced existing author files with aliases and biographies (**רא''ש**, **חיד''א**, **רבי שמעון בן צמח דוראן**), purged corrupt fallback author profiles (**ילקוט**, **פתח**, **שו"ת תשב"ץ**), preserved user study notes under Sanhedrin 22a and Ran Sanhedrin 22a, and patched root causes in `process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #9 (`חדושי הר"ן על סנהדרין דף כב/א`)
- **Issue**: Previously matched to an un-normalized filename `ר''ן - חדושי הר''ן על סנהדרין - דף כב ע-א.md` containing a legacy duplicate heading with study notes stuck under the `ע-א` anchor. In `bashert.md`, the embed targeted `#...דף כב עמוד א`, causing user notes to be hidden.
- **Resolution**: Standardized filename to **`ר''ן - חדושי הר''ן על סנהדרין - דף כב עמוד א.md`**, location to `דף כב עמוד א`, and tags to `[navi-source, machshava-source]`. Consolidated user study notes under single canonical headline `### ר''ן - חדושי הר''ן על סנהדרין - דף כב עמוד א`. Updated embed links in both `111 Source Sheets/bashert.md` and `111 Source Sheets/melachim 1.1.md`.

### 2. Source #11 (`תוספות רא"ש על סוטה דף ב עמוד א`)
- **Issue**: Extracted with `author='תוספות'`, `book="רא''ש על סוטה"`. `תוספות` matched greedily before `רא"ש` could be recognized.
- **Resolution**: Reattributed to canonical author **`[[רא''ש]]`** (Rabbeinu Asher), sefer **`תוספות הרא''ש מסכת סוטה`**, location **`דף ב עמוד א`**. Standardized note to **`רא''ש - תוספות הרא''ש מסכת סוטה - דף ב עמוד א.md`**, headline `### רא''ש - תוספות הרא''ש מסכת סוטה - דף ב עמוד א`, and updated embed link in `bashert.md`. Enhanced [`222 Authors/רא''ש.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%90''%D7%91.md) with aliases.

### 3. Source #14 (`שו"ת תשב"ץ חלק ב סימן א`)
- **Issue**: Extracted with author falling back to book title `[[שו''ת תשב''ץ]]`, book set to `חלק ב`, location `סימן א`, and flagged `audit_needed: true` (*"Author fell back to token 'שו\"ת תשב\"ץ'"*), generating corrupt fallback author note `222 Authors/שו''ת תשב''ץ.md`.
- **Resolution**: Attributed to canonical author **`[[רבי שמעון בן צמח דוראן]]`** (Rabbi Shimon ben Tzemach Duran / Tashbetz). Standardized note to **`רבי שמעון בן צמח דוראן - שו''ת תשב''ץ - חלק ב סימן א.md`**, book `שו''ת תשב''ץ`, location `חלק ב סימן א`. Cleared audit flag and warning badge. Enhanced canonical profile [`222 Authors/רבי שמעון בן צמח דוראן.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%51%D7%9E%D7%A2%D7%95%D7%9F%20%D7%91%D7%9F%20%D7%A6%D7%9E%D7%97%20%D7%93%D7%95%D7%A8%D7%90%D7%9F.md) with biography and aliases; purged corrupt fallback `222 Authors/שו''ת תשב''ץ.md`.

### 4. Source #15 (`פתח עינים להחיד"א מסכת סנהדרין דף כב עמוד א`)
- **Issue**: Extracted with `author='פתח'`, `book="עינים להחיד''א מסכת סנהדרין"`, and flagged `audit_needed: true` (*"Author fell back to token 'פתח'"*), generating corrupt fallback author note `222 Authors/פתח.md`.
- **Resolution**: Attributed to canonical author **`[[חיד''א]]`** (Rabbi Chaim Yosef David Azulai). Standardized note to **`חיד''א - פתח עינים מסכת סנהדרין - דף כב עמוד א.md`**, book `פתח עינים מסכת סנהדרין`, location `דף כב עמוד א`. Cleared audit flag and warning badge. Enhanced [`222 Authors/חיד''א.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%97%D7%99%D7%93''%D7%90.md) with aliases and biography; purged corrupt fallback `222 Authors/פתח.md`.

### 5. Source #16 (`נעימת החיים ד׳ ט"ז`)
- **Issue**: The unmapped contemporary book header `נעימת החיים` was parsed by generic author search, which matched `ט"ז` in `ד׳ ט"ז` (page 16), falsely attributing the 20th-century work to the Taz (**ט''ז** - Rabbi David HaLevi Segal, 17th century).
- **Resolution**: Identified true author as contemporary posek **`[[הרב חיים גרוס]]`** (Rabbi Chaim Gross). Standardized note to **`הרב חיים גרוס - נעימת החיים - ד׳ ט''ז.md`**, book `נעימת החיים`, location `ד׳ ט''ז`. Created canonical author file [`222 Authors/הרב חיים גרוס.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%97%D7%99%D7%99%D7%9D%20%D7%92%D7%A8%D7%95%D7%A1.md) and updated embed in `bashert.md`.

### 6. Source #17 (`ילקוט יוסף - שובע שמחות א - ד׳ כ"א השתדלות בעניני שידוכין`)
- **Issue**: Extracted with `author='ילקוט'`, `book="יוסף - שובע שמחות א"`, and flagged `audit_needed: true` (*"Author fell back to token 'ילקוט'"*), generating corrupt fallback author note `222 Authors/ילקוט.md`.
- **Resolution**: Attributed to canonical author **`[[הרב יצחק יוסף]]`** (Rishon LeZion Rabbi Yitzchak Yosef). Standardized note to **`הרב יצחק יוסף - ילקוט יוסף - שובע שמחות א - ד׳ כ''א השתדלות בעניני שידוכין.md`**, book `ילקוט יוסף - שובע שמחות א`, location `ד׳ כ''א השתדלות בעניני שידוכין`. Cleared audit flag and warning badge. Created canonical author profile [`222 Authors/הרב יצחק יוסף.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%99%D7%A6%D7%97%D7%A7%20%D7%99%D7%95%D7%A1%D7%A3.md) and purged corrupt fallback `222 Authors/ילקוט.md`.

---

## 2. Full Sheet Verification (17/17)

| # | Canonical Title | Author | Status | Notes |
|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת מועד קטן - דף יח עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean DH anchor `#גמרא/ אמר שמואל` |
| 2 | `תוספות - מסכת סנהדרין - דף כב עמוד א` | [[תוספות]] | ✅ Verified | Clean DH anchor `#ארבעים יום קודם יצירת הולד` |
| 3 | `ריטב''א - חידושי הריטב''א מסכת מועד קטן - דף יח עמוד ב` | [[ריטב''א]] | ✅ Verified | Clean 2-header layout |
| 4 | `ר''ן - חדושי הר''ן על מועד קטן - דף יח עמוד ב` | [[ר''ן]] | ✅ Verified | Clean 2-header layout |
| 5 | `רבי יהודה החסיד - ספר חסידים - סימן שפג` | [[רבי יהודה החסיד]] | ✅ Verified | Clean 2-header layout |
| 6 | `תלמוד בבלי - מסכת סוטה - דף ב עמוד א` | [[תלמוד בבלי]] | ✅ Verified | Clean DH anchor `#אמר רבה בר בר חנה אמר ר׳ יוחנן` |
| 7 | `תלמוד בבלי - מסכת גיטין - דף צ עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean DH anchor `#כי שנא שלח` |
| 8 | `תלמוד בבלי - מסכת סנהדרין - דף כב עמוד א` | [[תלמוד בבלי]] | ✅ Preserved | **User study notes intact & preserved**; continuation crop intact |
| 9 | `ר''ן - חדושי הר''ן על סנהדרין - דף כב עמוד א` | [[ר''ן]] | 🔧 **Fixed** | Slashed amud normalized to `עמוד א`; **User study notes consolidated & preserved**; embeds updated in `bashert.md` & `melachim 1.1.md` |
| 10 | `רש''י - מסכת סוטה - דף ב עמוד א` | [[רש''י]] | ✅ Verified | Clean DH anchor `#זוג ראשון` |
| 11 | `רא''ש - תוספות הרא''ש מסכת סוטה - דף ב עמוד א` | [[רא''ש]] | 🔧 **Fixed** | Attributed to Rosh; Sefer normalized to `תוספות הרא''ש מסכת סוטה` |
| 12 | `המאירי - על מסכת סוטה - דף ב עמוד א` | [[המאירי]] | ✅ Verified | Clean 2-header layout |
| 13 | `רמב''ם - שו''ת הרמב''ם - סימן תלו` | [[רמב''ם]] | ✅ Verified | Continuation crop `p3_cont` intact |
| 14 | `רבי שמעון בן צמח דוראן - שו''ת תשב''ץ - חלק ב סימן א` | [[רבי שמעון בן צמח דוראן]] | 🔧 **Fixed** | Canonical author attribution; audit cleared; corrupt author purged |
| 15 | `חיד''א - פתח עינים מסכת סנהדרין - דף כב עמוד א` | [[חיד''א]] | 🔧 **Fixed** | Canonical author attribution to Chida; audit cleared; corrupt author purged |
| 16 | `הרב חיים גרוס - נעימת החיים - ד׳ ט''ז` | [[הרב חיים גרוס]] | 🔧 **Fixed** | Fixed Taz collision; canonical author profile created |
| 17 | `הרב יצחק יוסף - ילקוט יוסף - שובע שמחות א - ד׳ כ''א השתדלות בעניני שידוכין` | [[הרב יצחק יוסף]] | 🔧 **Fixed** | Canonical author profile created; audit cleared; corrupt author purged |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Tosafos HaRosh Handling**:
   - Added `תוספות רא"ש`, `תוספות הרא"ש`, and their single-quote variations to `RESPONSA_SPECIAL_MAP` mapped to `('רא"ש', 'תוספות הרא"ש')`.
   - Added canonical entries in `AUTHOR_CANONICAL_MAP`.
   - Added tractate normalizer in `RESPONSA_SPECIAL_MAP` handling:
     `maseches = re.sub(r'^(?:על\s+)?(?:מסכת\s+)?', '', extra_clean).strip()`
     `book = f"תוספות הרא''ש מסכת {maseches}".strip()`
   - Properly resolves `תוספות רא"ש על סוטה` to `author='רא"ש'`, `book="תוספות הרא''ש מסכת סוטה"`.

2. **Responsa Tashbetz (`שו"ת תשב"ץ`)**:
   - Added `תשב"ץ`, `התשב"ץ`, `ספר תשב"ץ`, and single-quote variations to `RESPONSA_SPECIAL_MAP` mapped to `('רבי שמעון בן צמח דוראן', 'שו"ת תשב"ץ')`.
   - Added canonical mappings in `AUTHOR_CANONICAL_MAP` and added `רבי שמעון בן צמח דוראן`, `תשב"ץ` to `KNOWN_AUTHORS`.
   - Added `"שו''ת תשב''ץ"`, `'שו"ת תשב"ץ'` to the `bad` blacklist in `get_all_known_authors()` to eliminate corrupt fallback author creation.

3. **Petach Einayim on Shas by the Chida (`פתח עינים להחיד"א`)**:
   - Added `פתח עינים להחיד"א`, `פתח עינים`, and single-quote variations to `RESPONSA_SPECIAL_MAP` mapped to `('חיד"א', 'פתח עינים')`.
   - Added canonical entries in `AUTHOR_CANONICAL_MAP`.
   - Added tractate normalizer in `RESPONSA_SPECIAL_MAP` handling:
     `extra_clean = re.sub(r'^(?:להחיד"?א|להחיד\'\'א)\s*', '', extra_clean).strip()`
     `book = f"פתח עינים {extra_clean}".strip()`
   - Added `'פתח'` to the `bad` blacklist in `get_all_known_authors()` to prevent generic token fallbacks.

4. **Neimat HaChayim & Taz Token Collision**:
   - Traced false attribution to `ט"ז` to `נעימת החיים ד׳ ט"ז` where unmapped sefer title allowed the location token `ט"ז` (page 16) to match the Taz regex.
   - Added `נעימת החיים` and `ספר נעימת החיים` to `RESPONSA_SPECIAL_MAP` mapped to `('הרב חיים גרוס', 'נעימת החיים')`.
   - Added canonical entries in `AUTHOR_CANONICAL_MAP` and added `הרב חיים גרוס` to `KNOWN_AUTHORS`.

5. **Yalkut Yosef by Rav Yitzchak Yosef**:
   - Added `ילקוט יוסף` and `ספר ילקוט יוסף` to `RESPONSA_SPECIAL_MAP` mapped to `('הרב יצחק יוסף', 'ילקוט יוסף')`.
   - Preserves sub-volume titles (e.g., `שובע שמחות א`) in `book`:
     `if extra_book: book = f"ילקוט יוסף - {extra_book}".strip()`
   - Added canonical entries in `AUTHOR_CANONICAL_MAP` and added `הרב יצחק יוסף` to `KNOWN_AUTHORS`.
   - Added `'ילקוט'` to the `bad` blacklist in `get_all_known_authors()` to prevent fallback author generation.

6. **Page & Daf Prefix Normalization in Location Matching**:
   - In `get_normalized_location()`, added normalization `t = re.sub(r'^דף(?=[א-ת0-9])', 'ד', t)` so citations using `ד׳` or `דף` evaluate as identical during source matching and reconciliation.
