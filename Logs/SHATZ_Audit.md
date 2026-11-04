# SHATZ Source Sheet Audit

## Summary
Audited `111 Source Sheets/SHATZ.md` (`000 Source PDFs/SHATZ.pdf`, Subject: *Halacha*, Fall 2026 Midterm) — 23 embedded sources. Fully verified every citation against the decoded Davka font text stream and layout, resolved all 4 flagged/corrupt sources (**ריטב א**, **ספר אבודרהם**, **נפש הרב**, and **ספר קצור שו"ע**), resolved book title fallback issues (**טור אורח חיים** and **משנה ברורה על שולחן ערוך**), standardized Ran amud citation, created canonical author profiles in `222 Authors/` (**אבודרהם**, **רבי שלמה גאנצפריד**), purged corrupt fallback author profiles, preserved user study notes under Rosh Hashanah 33b, and patched root causes in `process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #3 (`חדושי הר"ן על חולין דף קו ע/א`)
- **Issue**: Slash in amud citation `ע/א` wasn't matched by previous regex, resulting in raw hyphenation `ר''ן - חדושי הר''ן על חולין - דף קו ע-א.md` and location `דף קו ע-א`.
- **Resolution**: Standardized to **`ר''ן - חדושי הר''ן על חולין - דף קו עמוד א.md`**, location `דף קו עמוד א`. Embed and internal header updated accordingly.

### 2. Source #4 (`ריטב א לתלמוד בבלי מסכת ראש השנה דף לד עמוד ב`)
- **Issue**: Font stream contained control character `\x18` decoded into `ריטב\x18א` with space, author fell back to `[[ריטב א]]` with flag `audit_needed: true` (*"Author fell back to token 'ריטב א'"*), generating corrupt fallback author `222 Authors/ריטב\x18א.md`, and book title extracted as `לתלמוד בבלי מסכת ראש השנה`.
- **Resolution**: Attributed to canonical author **`[[ריטב''א]]`** (linking to existing [`222 Authors/ריטב''א.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%99%D7%98%D7%91''%D7%90.md)), standardized to **`ריטב''א - חידושי הריטב''א מסכת ראש השנה - דף לד עמוד ב.md`**, book `חידושי הריטב''א מסכת ראש השנה`, location `דף לד עמוד ב`. Purged corrupt author note `222 Authors/ריטב\x18א.md`.

### 3. Source #5 (`ספר אבודרהם שמונה עשרה ד"ה נשאל הר"ם`)
- **Issue**: Extracted with author falling back to book title `[[ספר אבודרהם]]`, book set to `שמונה עשרה`, and flagged `audit_needed: true` (*"Author fell back to token 'ספר אבודרהם'"*), generating corrupt fallback author note `222 Authors/ספר אבודרהם.md`.
- **Resolution**: Attributed to canonical author moniker **`[[אבודרהם]]`** (Rabbi David Abudarham). Standardized note to **`אבודרהם - ספר אבודרהם - שמונה עשרה - ד''ה נשאל הר''ם.md`**, book `ספר אבודרהם`, location `שמונה עשרה - ד''ה נשאל הר''ם`.
- **Author Note**: Created [`222 Authors/אבודרהם.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%90%D7%91%D7%55%D7%93%D7%A8%D7%94%D7%9D.md) with historical biography and aliases (`רבי דוד אבודרהם`, `דוד אבודרהם`, `ספר אבודרהם`, `Abudarham`); purged corrupt fallback `222 Authors/ספר אבודרהם.md`.

### 4. Source #6 (`טור אורח חיים סימן קכד`)
- **Issue**: Yerushalmi column regex `(?<![א-ת])טור\s+[א-ד0-9]` erroneously matched `טור א` inside `טור אורח חיים`, treating the entire remainder as location and resetting book to `מקור` (`רבי יעקב בן אשר - מקור - טור אורח חיים סימן קכד.md`).
- **Resolution**: Standardized to **`רבי יעקב בן אשר - טור אורח חיים - סימן קכד.md`**, book `טור אורח חיים`, location `סימן קכד`.

### 5. Source #7 (`ספר בן איש חי - הלכות שנה ראשונה - פרשת תרומה`)
- **Issue**: Whole string was captured as book title leaving location empty.
- **Resolution**: Cleaned metadata in [`333 Sources/בן איש חי - ספר בן איש חי - הלכות שנה ראשונה - פרשת תרומה.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%91%D7%9F%20%D7%90%D7%99%D7%A9%20%D7%97%D7%99%20-%20%D7%A1%D7%A4%D7%A8%20%D7%91%D7%9F%20%D7%90%D7%99%D7%A9%20%D7%97%D7%99%20-%20%D7%94%D7%9C%D7%93%D7%95%D7%AA%20%D7%A9%D7%A0%D7%94%20%D7%A8%D7%90%D7%A9%D7%95%D7%A0%D7%94%20-%20%D7%A4%D7%A8%D7%A9%D7%AA%20%D7%AA%D7%A8%D7%55%D7%9E%D7%94.md) with book `ספר בן איש חי - הלכות שנה ראשונה`, location `פרשת תרומה`.

### 6. Source #8 (`נפש הרב ד׳ קכ"ג וקכ"ה`)
- **Issue**: Extracted with author `author='נפש'`, book `book='הרב'`, and flagged `audit_needed: true` (*"Author fell back to token 'נפש'"*), generating corrupt fallback author `222 Authors/נפש.md`.
- **Resolution**: Attributed to canonical author **`[[הרב צבי שכטר]]`** (Rabbi Hershel Schachter). Standardized note to **`הרב צבי שכטר - נפש הרב - ד׳ קכ''ג וקכ''ה.md`**, book `נפש הרב`, location `ד׳ קכ''ג וקכ''ה`.
- **Author Note**: Linked to existing canonical profile [`222 Authors/הרב צבי שכטר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%A6%D7%91%D7%99%20%D7%A9%D7%9B%D7%98%D7%A8.md); purged fallback `222 Authors/נפש.md`.

### 7. Source #17 (`משנה ברורה על שולחן ערוך אורח חיים סימן קכד סעיף ד`)
- **Issue**: Author parser matched subsequent token `שולחן ערוך` due to equal length tie-breaker, resetting author to `שולחן ערוך`, book to `מקור`, and location to `משנה ברורה על שולחן ערוך...` (`שולחן ערוך - מקור - משנה ברורה על שולחן ערוך אורח חיים סימן קכד סעיף ד.md`).
- **Resolution**: Attributed to canonical author **`[[משנה ברורה]]`**, book `משנה ברורה`, location `סימן קכד סעיף ד`. Renamed to **`משנה ברורה - משנה ברורה - סימן קכד סעיף ד.md`**, preserving continuation crops `SHATZ_p3_s6.png` and `SHATZ_p4_cont.png`.

### 8. Source #22 (`ספר קצור שו"ע סימן כ - דין חזרת תפלת הש"ץ`)
- **Issue**: Extracted as `author='ספר קצור'`, `book="שו''ע"`, and flagged `audit_needed: true` (*"Author fell back to token 'ספר קצור'"*), generating corrupt fallback author `222 Authors/ספר קצור.md`.
- **Resolution**: Attributed to canonical author **`[[רבי שלמה גאנצפריד]]`** (Rabbi Shlomo Ganzfried). Standardized note to **`רבי שלמה גאנצפריד - קיצור שולחן ערוך - סימן כ - דין חזרת תפלת הש''ץ.md`**, book `קיצור שולחן ערוך`, location `סימן כ - דין חזרת תפלת הש''ץ`.
- **Author Note**: Created [`222 Authors/רבי שלמה גאנצפריד.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%A9%D7%9C%D7%9E%D7%94%20%D7%92%D7%90%D7%A0%D7%A6%D7%A4%D7%A8%D7%99%D7%93.md) with biography and comprehensive aliases; purged fallback `222 Authors/ספר קצור.md`.

---

## 2. Full Sheet Verification (23/23)

| # | Canonical Title | Author | Status | Notes |
|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת ראש השנה - דף לג עמוד ב` | [[תלמוד בבלי]] | ✅ Preserved | **User study notes intact & preserved** |
| 2 | `תלמוד בבלי - מסכת ראש השנה - דף לד עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout |
| 3 | `ר''ן - חדושי הר''ן על חולין - דף קו עמוד א` | [[ר''ן]] | 🔧 **Fixed** | Slashed amud `ע/א` normalized to `עמוד א` |
| 4 | `ריטב''א - חידושי הריטב''א מסכת ראש השנה - דף לד עמוד ב` | [[ריטב''א]] | 🔧 **Fixed** | Control char removed, canonical author & sefer set |
| 5 | `אבודרהם - ספר אבודרהם - שמונה עשרה - ד''ה נשאל הר''ם` | [[אבודרהם]] | 🔧 **Fixed** | Canonical author profile created; audit cleared |
| 6 | `רבי יעקב בן אשר - טור אורח חיים - סימן קכד` | [[רבי יעקב בן אשר]] | 🔧 **Fixed** | Fixed `loc_match` regex collision on `טור א` |
| 7 | `בן איש חי - ספר בן איש חי - הלכות שנה ראשונה - פרשת תרומה` | [[בן איש חי]] | 🔧 **Fixed** | Cleaned metadata and location field; multi-crop intact |
| 8 | `הרב צבי שכטר - נפש הרב - ד׳ קכ''ג וקכ''ה` | [[הרב צבי שכטר]] | 🔧 **Fixed** | Attributed to Rav Schachter; audit flag cleared |
| 9 | `אגרות משה - חלק או''ח ב - סימן כט` | [[אגרות משה]] | ✅ Verified | Clean 2-header layout |
| 10 | `רבי יצחק יעקב וייס - שו''ת מנחת יצחק - חלק ו סימן לא` | [[רבי יצחק יעקב וייס]] | ✅ Verified | Clean 2-header layout |
| 11 | `רב עובדיה יוסף - שו''ת יביע אומר - חלק ו - או''ח סימן י` | [[רב עובדיה יוסף]] | ✅ Verified | Continuation crop `p3_cont` intact |
| 12 | `שולחן ערוך - אורח חיים - סימן קכד סעיף ב` | [[שולחן ערוך]] | ✅ Verified | Clean 2-header layout |
| 13 | `מגן אברהם - אורח חיים - סימן קכד ס''ק ג` | [[מגן אברהם]] | ✅ Verified | Clean 2-header layout |
| 14 | `משנה ברורה - משנה ברורה סימן קכד ס''ק ו' ז' ח` | [[משנה ברורה]] | ✅ Verified | Clean DH anchor `#שעת הדחק` |
| 15 | `רב עובדיה יוסף - שו''ת יחווה דעת - חלק ג סימן טז` | [[רב עובדיה יוסף]] | ✅ Verified | Clean DH anchor `#שאלה` |
| 16 | `שולחן ערוך - אורח חיים - סימן קכד סעיף ד` | [[שולחן ערוך]] | ✅ Verified | Clean 2-header layout |
| 17 | `משנה ברורה - משנה ברורה - סימן קכד סעיף ד` | [[משנה ברורה]] | 🔧 **Fixed** | Attributed to Mishnah Berurah; multi-crop intact |
| 18 | `אגרות משה - חלק או''ח ד - סימן יט` | [[אגרות משה]] | ✅ Verified | Clean 2-header layout |
| 19 | `שולחן ערוך - אורח חיים - סימן נה סעיף ו` | [[שולחן ערוך]] | ✅ Verified | Clean 2-header layout |
| 20 | `מגן אברהם - אורח חיים - סימן נה ס''ק ח` | [[מגן אברהם]] | ✅ Verified | Clean DH anchor `#מצטרף עמהם` |
| 21 | `שולחן ערוך - אורח חיים - סימן קכד סעיף ג` | [[שולחן ערוך]] | ✅ Verified | Clean 2-header layout |
| 22 | `רבי שלמה גאנצפריד - קיצור שולחן ערוך - סימן כ - דין חזרת תפלת הש''ץ` | [[רבי שלמה גאנצפריד]] | 🔧 **Fixed** | Canonical author profile created; audit cleared |
| 23 | `ציץ אליעזר - חלק יב - סימן ט` | [[ציץ אליעזר]] | ✅ Verified | Clean 2-header layout |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Davka Font Stream Control Characters & Sanitization**:
   - Enhanced `decode_line` and `sanitize_filename` to strip ASCII control characters (`\x18`, `\x00-\x1f`) that were polluting filenames and author tokens (such as `ריטב\x18א`).
   - Added regex pre-processor for Ritva tractate commentaries:
     `clean = re.sub(r'^(?:ריטב\s*א|הריטב\s*א)\s+(?:לתלמוד בבלי\s+)?מסכת\s+', "חידושי הריטב''א מסכת ", clean)`.
   - Added canonical mappings for `חידושי הריטב"א` and `חידושי הריטב''א` to `ריטב''א`.

2. **Daf & Amud Slash Normalization**:
   - Updated regex normalizer across both responsa and standard citation handlers:
     `location = re.sub(r'דף\s+([א-ת0-9]+)\s*(?:ע[/\-]|[/|\-])\s*([אב])\b', r'דף \1 עמוד \2', location)`
     `location = re.sub(r'\bע[/\-]([אב])\b', r'עמוד \1', location)`
   - Properly normalizes `דף קו ע/א` to canonical `דף קו עמוד א`.

3. **Sefer Abudarham Handling**:
   - Added `ספר אבודרהם` and `אבודרהם` to `RESPONSA_SPECIAL_MAP` mapped to `('אבודרהם', 'ספר אבודרהם')`.
   - Added canonical author mapping in `AUTHOR_CANONICAL_MAP` and added `אבודרהם` / `ספר אבודרהם` to `KNOWN_AUTHORS`.
   - Preserves prayer section (e.g. `שמונה עשרה - ד"ה...`) inside location.

4. **Tur Column Collision Bug (`loc_match`)**:
   - Traced root cause of Tur Orach Chaim collapsing into `book='מקור'` to `loc_match` regex: `(?<![א-ת])טור\s+[א-ד0-9]` was matching `טור א` in `טור אורח חיים` because `א` is in `[א-ד0-9]`.
   - Patched both occurrences in `process_source_sheets.py` with negative lookahead:
     `(?<![א-ת])טור\s+[א-ד0-9](?![א-ת])`.
   - Added `טור אורח חיים` to `RESPONSA_SPECIAL_MAP` and `AUTHOR_CANONICAL_MAP`.

5. **Nefesh HaRav Attribution**:
   - Added `נפש הרב` to `RESPONSA_SPECIAL_MAP` mapped to `('הרב צבי שכטר', 'נפש הרב')`.
   - Added mappings in `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS` for `נפש הרב` and `הרב צבי שכטר`.

6. **Mishnah Berurah on Shulchan Aruch & Regex Lookahead**:
   - Fixed author token collision where `שולחן ערוך` was selected over leading `משנה ברורה`.
   - Added match position ranking:
     `matches.sort(key=lambda x: (x[0], -len(x[1])))` prioritizing authors appearing earlier in citation text.
   - Guarded `משנה` token inside `loc_match` with negative lookahead `משנה(?!\s*ברורה)` to prevent splitting `משנה ברורה` citations into bogus locations and eliminating duplicate stutter (`משנה ברורה - משנה ברורה סימן...`).

7. **Kitzur Shulchan Aruch Mapping**:
   - Added `ספר קצור שו"ע`, `ספר קיצור שולחן ערוך`, `קצור שו"ע`, and `קיצור שולחן ערוך` to `RESPONSA_SPECIAL_MAP` mapped to `('רבי שלמה גאנצפריד', 'קיצור שולחן ערוך')`.
   - Added canonical author profile and mappings in `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.
