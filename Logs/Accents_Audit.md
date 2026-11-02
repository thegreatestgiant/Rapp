# Accents Source Sheet Audit

## Summary
Audited `111 Source Sheets/accents.md` (`000 Source PDFs/accents.pdf`, Subject: *Gemara*, Fall 2026 Midterm) — 17 sources across 3 pages focusing on Hebrew pronunciation, phonetic traditions (Ashkenazic vs. Sephardic vs. Yemenite), and halachic obligations in Tefillah and Krias Shema.

Resolved multiple author fallback anomalies, multi-word and responsa title misattributions, and multi-quote collision dynamics. Created 4 new canonical author profiles in `222 Authors/`, purged 7 corrupt fallback author profiles, unified 3 distinct excerpts of *Yabia Omer* with their proper Diburei Hamatchil while restoring displaced crops, verified all 18 image attachments (including page continuation crops), and patched root-cause parsing logic in `999 Scripts/process_source_sheets.py`.

**Result**: 0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files, and strictly 17 verified canonical sources.

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #3 (`רבנו בחיי על בראשית פרק יח פסוק ג`)
- **Issue**: Extracted as `author='רבנו'`, `book='בחיי על בראשית'` with audit flag `audit_needed: true` (*"Author fell back to token 'רבנו'"*), creating corrupt fallback author `222 Authors/רבנו.md`.
- **Resolution**: Renamed note to **[`333 Sources/רבנו בחיי - בראשית - פרק יח פסוק ג.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%A8%D7%91%D7%A0%D7%20%D7%91%D7%97%D7%99%D7%99%20-%20%D7%91%D7%55%D7%90%D7%A9%D7%99%D7%AA%20-%20%D7%A4%D7%A8%D7%A7%20%D7%99%D7%97%20%D7%A4%D7%A1%D7%95%D7%A7%20%D7%92.md)**; attributed to canonical author **`[[רבנו בחיי]]`** (Rabbeinu Bachya ben Asher ibn Halawa), Book: `בראשית`, Location: `פרק יח פסוק ג`. Embed updated on master sheet.
- **Author Note**: Created [`222 Authors/רבנו בחיי.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%A0%D7%20%D7%91%D7%97%D7%99%D7%99.md) with biography and aliases; purged corrupt fallback `222 Authors/רבנו.md`.

### 2. Source #4 (`שו"ת רב פעלים חלק ב - או"ח סימן כה ד"ה ומה ששאלתם`)
- **Issue**: Unmapped in `RESPONSA_SPECIAL_MAP`, resulting in author falling back to sefer title `[[רב פעלים]]` and creating corrupt fallback author `222 Authors/רב פעלים.md`.
- **Resolution**: Renamed note to **[`333 Sources/בן איש חי - רב פעלים - חלק ב או''ח סימן כה ד''ה ומה ששאלתם.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%91%D7%9F%20%D7%90%D7%99%D7%55%20%D7%97%D7%99%20-%20%D7%A8%D7%91%20%D7%A4%D7%A2%D7%94%D7%99%D7%9D%20-%20%D7%97%D7%94%D7%A7%20%D7%91%20%D7%90%D7%95''%D7%97%20%D7%A1%D7%99%D7%9E%D7%9F%20%D7%9B%D7%94%20%D7%93''%D7%94%20%D7%95%D7%9E%D7%94%20%D7%A9%D7%A9%D7%90%D7%94%D7%AA%D7%9D.md)**, attributed to canonical author **`[[בן איש חי]]`** (matching existing vault conventions e.g. `בן איש חי - רב פעלים - סימן ל''ז.md`), Book: `רב פעלים`, Location: `חלק ב או''ח סימן כה ד''ה ומה ששאלתם`.
- **Author Note**: Linked to existing canonical [`222 Authors/בן איש חי.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%91%D7%9F%20%D7%90%D7%99%D7%55%20%D7%97%D7%99.md); purged fallback `222 Authors/רב פעלים.md`.

### 3. Sources #6, #9, #10 (Yabia Omer Vol. 6 Orach Chaim 11 Excerpt Collision)
- **Issue**:
  - `שו"ת יביע אומר` was missing from `RESPONSA_SPECIAL_MAP`, causing the parser to fall back to `author='שו"ת יביע'` / `author='יביע'`, generating corrupt fallback author files `222 Authors/שו''ת יביע.md` and `222 Authors/יביע.md` with active audit flags.
  - Three distinct excerpts from the same siman (Source #6 citing Ya'avetz on Kamatz/Patach, Source #9 citing the grammatical accuracy of Sephardic consonants, Source #10 citing specific letters like Ches/Chaf, Taf/Samech, and Reish) all collided into a single note.
  - During collision, crop replacement erased `accents_p2_s1.png` from markdown, and lack of Dibur Hamatchil extraction led to duplicate and numbered fallback headings (`(2)`), causing Sources #6 and #9 on the master sheet to point to the exact same anchor.
- **Resolution**:
  - Unified into canonical note **[`333 Sources/רב עובדיה יוסף - שו''ת יביע אומר - חלק ו או''ח סימן יא.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%A8%D7%91%20%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%94%20%D7%99%D7%95%D7%A1%D7%A3%20-%20%D7%A1%D7%95''%D7%AA%20%D7%99%D7%91%D7%99%D7%A2%20%D7%90%D7%95%D7%9E%D7%A8%20-%20%D7%97%D7%94%D7%A7%20%D7%95%20%D7%90%D7%95''%D7%97%20%D7%A1%D7%99%D7%9E%D7%9F%20%D7%99%D7%90.md)**, attributed to canonical profile **`[[רב עובדיה יוסף]]`**, Book: `שו''ת יביע אומר`, Location: `חלק ו או''ח סימן יא`.
  - Image block fully preserves all 3 cropped sources in reading sequence: `accents_p2_s1.png`, `accents_p2_s4.png`, and `accents_p2_s5.png`.
  - Created 3 distinct Dibur Hamatchil anchors:
    - `### ובסידור הגאון יעב''ץ` (Source #6)
    - `### לכאורה במבטא האותיות` (Source #9)
    - `### והאשכנזים שמבטאים חי''ת` (Source #10)
  - Updated [`111 Source Sheets/accents.md`](file:///home/sean/Obsidian/Rapp/111%20Source%20Sheets/accents.md) so each item embeds its own anchor cleanly.
  - Purged fallback author files `222 Authors/שו''ת יביע.md` and `222 Authors/יביע.md`.

### 4. Source #7 (`חקר ועיון )ר׳ קלמן כהנא( ח"ה ד׳ שכ"א`)
- **Issue**: Parenthetical author string `)ר׳ קלמן כהנא(` was stripped prior to author extraction; `חקר ועיון` was unmapped, causing author fallback to `[[חקר]]` and creating corrupt fallback author `222 Authors/חקר.md` with active audit flag.
- **Resolution**: Renamed note to **[`333 Sources/הרב קלמן כהנא - חקר ועיון - ח''ה דף שכ''א.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%94%D7%A8%D7%91%20%D7%A7%D7%94%D7%9E%D7%9F%20%D7%9B%D7%94%D7%A0%D7%90%20-%20%D7%97%D7%A7%D7%A8%20%D7%95%D7%A2%D7%99%D7%95%D7%9F%20-%20%D7%97''%D7%94%20%D7%93%D7%A3%20%D7%A9%D7%9B''%D7%90.md)**; attributed to canonical author **`[[הרב קלמן כהנא]]`**, Book: `חקר ועיון`, Location: `ח''ה דף שכ''א`.
- **Author Note**: Created [`222 Authors/הרב קלמן כהנא.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%A7%D7%94%D7%9E%D7%9F%20%D7%9B%D7%94%D7%A0%D7%90.md) with biography and aliases; purged fallback `222 Authors/חקר.md`.

### 5. Source #11 (`ספר תפארת ישראל להמהר"ל - פרק סו`)
- **Issue**: Generic substring matching on `תפארת ישראל` misattributed this classical philosophical treatise by the Maharal of Prague to Rabbi Yisrael Lipschitz (author of the Mishnah commentary *Tiferes Yisrael*), creating note `רבי ישראל ליפשיץ - ספר תפארת ישראל להמהר''ל - פרק סו.md`.
- **Resolution**: Renamed note to **[`333 Sources/מהר''ל - תפארת ישראל - פרק סו.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%9E%D7%94%D7%A8''%D7%94%20-%20%D7%AA%D7%A4%D7%90%D7%A8%D7%AA%20%D7%99%D7%A9%D7%A8%D7%90%D7%94%20-%20%D7%A4%D7%A8%D7%A7%20%D7%A1%D7%95.md)**; attributed to canonical author **`[[מהר''ל]]`** (linking to existing [`222 Authors/מהר''ל.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%9E%D7%94%D7%A8''%D7%94.md)), Book: `תפארת ישראל`, Location: `פרק סו`. Updated embed on sheet.

### 6. Source #15 (`שו"ת אורח משפט או"ח סימן יז`)
- **Issue**: Unmapped in `RESPONSA_SPECIAL_MAP`, causing fallback to `author='שו"ת אורח'`, `book='משפט או"ח'`, generating corrupt fallback author `222 Authors/שו''ת אורח.md` with active audit flag.
- **Resolution**: Renamed note to **[`333 Sources/הרב אברהם יצחק הכהן קוק - שו''ת אורח משפט - או''ח סימן יז.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%94%D7%A8%D7%91%20%D7%90%D7%91%D7%A8%D7%94%D7%9D%20%D7%99%D7%A6%D7%97%D7%A7%20%D7%94%D7%93%D7%9B%D7%94%D7%9F%20%D7%A7%D7%95%D7%A7%20-%20%D7%A1%D7%95''%D7%AA%20%D7%90%D7%95%D7%A8%D7%97%20%D7%9E%D7%A9%D7%A4%D7%90%20-%20%D7%90%D7%95''%D7%97%20%D7%A1%D7%99%D7%9E%D7%9F%20%D7%99%D7%96.md)**; attributed to canonical author **`[[הרב אברהם יצחק הכהן קוק]]`** (Chief Rabbi Rav Kook), Book: `שו''ת אורח משפט`, Location: `או''ח סימן יז`.
- **Author Note**: Created [`222 Authors/הרב אברהם יצחק הכהן קוק.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%90%D7%91%D7%A8%D7%94%D7%9D%20%D7%99%D7%A6%D7%97%D7%A7%20%D7%94%D7%93%D7%9B%D7%94%D7%9F%20%D7%A7%D7%95%D7%A7.md) with biography and aliases; purged fallback `222 Authors/שו''ת אורח.md`.

### 7. Source #16 (`שו"ת משפטי עוזיאל כרך א - או"ח סימן א`)
- **Issue**: Unmapped in `RESPONSA_SPECIAL_MAP`, causing fallback to `author='שו"ת משפטי'`, `book='עוזיאל'`, generating corrupt fallback author `222 Authors/שו''ת משפטי.md` with active audit flag.
- **Resolution**: Renamed note to **[`333 Sources/הרב בן ציון מאיר חי עוזיאל - שו''ת משפטי עוזיאל - כרך א או''ח סימן א.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%94%D7%A8%D7%91%20%D7%91%D7%9F%20%D7%A6%D7%99%D7%95%D7%9F%20%D7%9E%D7%90%D7%99%D7%A8%20%D7%97%D7%99%20%D7%A2%D7%95%D7%96%D7%99%D7%90%D7%94%20-%20%D7%A1%D7%95''%D7%AA%20%D7%9E%D7%A9%D7%A4%D7%90%D7%99%20%D7%A2%D7%95%D7%96%D7%99%D7%90%D7%94%20-%20%D7%9B%D7%A8%D7%9A%20%D7%90%20%D7%90%D7%95''%D7%97%20%D7%A1%D7%99%D7%9E%D7%9F%20%D7%90.md)**; attributed to canonical author **`[[הרב בן ציון מאיר חי עוזיאל]]`** (First Sephardic Chief Rabbi of Israel), Book: `שו''ת משפטי עוזיאל`, Location: `כרך א או''ח סימן א`.
- **Author Note**: Created [`222 Authors/הרב בן ציון מאיר חי עוזיאל.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%91%D7%9F%20%D7%A6%D7%99%D7%95%D7%9F%20%D7%9E%D7%90%D7%99%D7%A8%20%D7%97%D7%99%20%D7%A2%D7%95%D7%96%D7%99%D7%90%D7%94.md) with biography and aliases; purged fallback `222 Authors/שו''ת משפטי.md`.

---

## 2. Complete Roster of 17 Verified Sources

| # | Embed on Sheet (`111 Source Sheets/accents.md`) | Canonical Author (`222 Authors/`) | Book | Location / Anchor |
|---|---|---|---|---|
| **1** | `![[תנ''ך - בראשית - פרק יח פסוק ג#תנ''ך - בראשית - פרק יח פסוק ג]]` | `[[תנ''ך]]` | בראשית | פרק יח פסוק ג |
| **2** | `![[רש''י - בראשית - פרק יח פסוק ג#ויאמר אדני אם נא וגו׳]]` | `[[רש''י]]` | בראשית | פרק יח פסוק ג (#ויאמר אדני אם נא וגו׳) |
| **3** | `![[רבנו בחיי - בראשית - פרק יח פסוק ג#רבנו בחיי - בראשית - פרק יח פסוק ג]]` | `[[רבנו בחיי]]` | בראשית | פרק יח פסוק ג |
| **4** | `![[בן איש חי - רב פעלים - חלק ב או''ח סימן כה ד''ה ומה ששאלתם#בן איש חי - רב פעלים - חלק ב או''ח סימן כה ד''ה ומה ששאלתם]]` | `[[בן איש חי]]` | רב פעלים | חלק ב או''ח סימן כה ד''ה ומה ששאלתם |
| **5** | `![[רב צבי פסח פרנק - הר צבי - או''ח א סימן ד#רב צבי פסח פרנק - הר צבי - או''ח א סימן ד]]` | `[[רב צבי פסח פרנק]]` | הר צבי | או''ח א סימן ד |
| **6** | `![[רב עובדיה יוסף - שו''ת יביע אומר - חלק ו או''ח סימן יא#ובסידור הגאון יעב''ץ]]` | `[[רב עובדיה יוסף]]` | שו''ת יביע אומר | חלק ו או''ח סימן יא (#ובסידור הגאון יעב''ץ) |
| **7** | `![[הרב קלמן כהנא - חקר ועיון - ח''ה דף שכ''א#הרב קלמן כהנא - חקר ועיון - ח''ה דף שכ''א]]` | `[[הרב קלמן כהנא]]` | חקר ועיון | ח''ה דף שכ''א |
| **8** | `![[זוהר - חלק ג - דף רכח-א#זוהר - חלק ג - דף רכח-א]]` | `[[זוהר]]` | חלק ג | דף רכח-א |
| **9** | `![[רב עובדיה יוסף - שו''ת יביע אומר - חלק ו או''ח סימן יא#לכאורה במבטא האותיות]]` | `[[רב עובדיה יוסף]]` | שו''ת יביע אומר | חלק ו או''ח סימן יא (#לכאורה במבטא האותיות) |
| **10** | `![[רב עובדיה יוסף - שו''ת יביע אומר - חלק ו או''ח סימן יא#והאשכנזים שמבטאים חי''ת]]` | `[[רב עובדיה יוסף]]` | שו''ת יביע אומר | חלק ו או''ח סימן יא (#והאשכנזים שמבטאים חי''ת) |
| **11** | `![[מהר''ל - תפארת ישראל - פרק סו#מהר''ל - תפארת ישראל - פרק סו]]` | `[[מהר''ל]]` | תפארת ישראל | פרק סו |
| **12** | `![[תלמוד בבלי - מסכת מגילה - דף כד עמוד ב#אמר רב אסי]]` | `[[תלמוד בבלי]]` | מסכת מגילה | דף כד עמוד ב (#אמר רב אסי) |
| **13** | `![[תלמוד בבלי - מסכת יבמות - דף קו עמוד ב#תלמוד בבלי - מסכת יבמות - דף קו עמוד ב]]` | `[[תלמוד בבלי]]` | מסכת יבמות | דף קו עמוד ב (כולל המשך עמוד 3) |
| **14** | `![[אגרות משה - חלק או''ח ג - סימן ה#אגרות משה - חלק או''ח ג - סימן ה]]` | `[[אגרות משה]]` | חלק או''ח ג | סימן ה |
| **15** | `![[הרב אברהם יצחק הכהן קוק - שו''ת אורח משפט - או''ח סימן יז#הרב אברהם יצחק הכהן קוק - שו''ת אורח משפט - או''ח סימן יז]]` | `[[הרב אברהם יצחק הכהן קוק]]` | שו''ת אורח משפט | או''ח סימן יז |
| **16** | `![[הרב בן ציון מאיר חי עוזיאל - שו''ת משפטי עוזיאל - כרך א או''ח סימן א#הרב בן ציון מאיר חי עוזיאל - שו''ת משפטי עוזיאל - כרך א או''ח סימן א]]` | `[[הרב בן ציון מאיר חי עוזיאל]]` | שו''ת משפטי עוזיאל | כרך א או''ח סימן א |
| **17** | `![[רבי יצחק יעקב וייס - שו''ת מנחת יצחק - חלק ג סימן ט#רבי יצחק יעקב וייס - שו''ת מנחת יצחק - חלק ג סימן ט]]` | `[[רבי יצחק יעקב וייס]]` | שו''ת מנחת יצחק | חלק ג סימן ט |

---

## 3. Parser Root-Cause Fixes in `process_source_sheets.py`

1. **Responsa & Rabbinic Works Canonical Mapping (`RESPONSA_SPECIAL_MAP`)**:
   - Added mappings for:
     - `יביע אומר`: `('רב עובדיה יוסף', 'שו"ת יביע אומר')`
     - `רב פעלים`: `('בן איש חי', 'רב פעלים')`
     - `אורח משפט`: `('הרב אברהם יצחק הכהן קוק', 'שו"ת אורח משפט')`
     - `משפטי עוזיאל`: `('הרב בן ציון מאיר חי עוזיאל', 'שו"ת משפטי עוזיאל')`
     - `חקר ועיון`: `('הרב קלמן כהנא', 'חקר ועיון')`
     - `תפארת ישראל להמהר"ל`: `("מהר''ל", 'תפארת ישראל')` (prioritized over Mishnah commentary)
     - `רבנו בחיי`: normalized `book` to Chumash name by stripping `על` prefix from `על בראשית`.

2. **Author Canonical Dictionary (`AUTHOR_CANONICAL_MAP` & `get_all_known_authors`)**:
   - Registered canonical mappings for `רבנו בחיי`, `הראי"ה קוק`, `הרב אברהם יצחק הכהן קוק`, `הרב בן ציון מאיר חי עוזיאל`, `הרב קלמן כהנא`, and `בן איש חי`.
   - Added `רבנו` to the forbidden author filter set `bad` in `get_all_known_authors()` so single honorific words never masquerade as autonomous author names.

3. **Extended Volume Regex Matching (`ח"[א-ת]`)**:
   - Broadened location regexes in `RESPONSA_SPECIAL_MAP` and generic citation matching from hardcoded `ח"א|ח"ב|ח"ג|ח"ד` to `ח\"[א-ת]|ח\'\'[א-ת]|ח[\'׳][א-ת]`. This allows higher volumes (e.g., `ח"ה` in Cheker V'Iyun Vol. 5) to be recognized as location components rather than trailing parts of book titles.

4. **Multi-Source Crop Preservation in `process_source`**:
   - Replaced aggressive regex image-block replacement logic with an additive check (`if img not in file_content`). This prevents earlier crops from the same sheet (e.g. `accents_p2_s1.png`) from being inadvertently overwritten when subsequent excerpts from the same work/location are parsed.
