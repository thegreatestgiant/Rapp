# Teima Before Tefilla Source Sheet Audit

## Summary
Audited `111 Source Sheets/teima before tefilla.md` (`000 Source PDFs/teima before tefilla.pdf`, Subject: *Halacha*, Fall 2026 Final) — 23 embedded sources.
1. **Resolved Flagged Sources (#10 and #16)**: Resolved both `שער הציון` citations which had fallen back to author token `[[שער]]` with audit flags. Attributed both to canonical author **`[[משנה ברורה]]`** (Rabbi Yisrael Meir Kagan), extracted their distinct footnote anchors (**`אות כא`** for Siman 232 and **`אות יט`** for Siman 235), and purged the corrupt fallback author note `222 Authors/שער.md`.
2. **Responsa Section Disambiguation (#21 and #23)**: Disambiguated two distinct sections of **שו"ת יביע אומר חלק ה - או"ח סימן כב** that had collided into a single file with stacked crops. Separated them into **`אות א`** (crop: `teima before tefilla_p3_s4.png`) and **`אות ב`** (crop: `teima before tefilla_p3_s6.png`).
3. **Multi-Page Continuation Integrity (#8)**: Verified **שולחן ערוך סימן רלב סעיף ב**, which spans the boundary between Page 1 and Page 2, correctly embeds both the primary crop `teima before tefilla_p1_s8.png` and continuation crop `teima before tefilla_p2_cont.png`.
4. **User Note Protection**: Fully preserved existing user study notes in [`333 Sources/תלמוד בבלי - מסכת ברכות - דף י עמוד ב.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%AA%D7%9C%D7%9E%D7%55%D7%93%20%D7%91%D7%91%D7%9C%D7%99%20-%20%D7%9E%D7%A1%D7%93%D7%AA%20%D7%91%D7%A8%D7%93%D7%95%D7%AA%20-%20%D7%93%D7%A3%20%D7%99%20%D7%A2%D7%9E%D7%55%D7%93%20%D7%91.md).
5. **Script Root-Cause Patches**: Enhanced [`999 Scripts/process_source_sheets.py`](file:///home/sean/Obsidian/Rapp/999%20Scripts/process_source_sheets.py) with canonical mapping for `שער הציון`, automatic footnote number/letter extraction for Sha'ar HaTziyun (`אות`), responsa section detection (`אות א`, `אות ב`), and `seen_in_sheet` tracking for newly created files.
6. **Result**: **0 audit warnings, 0 broken embeds, 0 missing images, 0 missing authors.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #10 & #16 (`שער הציון סימן רלב` & `שער הציון סימן רלה`)
- **Issue**: `שער הציון` was not registered in `KNOWN_AUTHORS` or `AUTHOR_CANONICAL_MAP`. It fell back to splitting on whitespace: author `[[שער]]` and book `הציון`, flagging `audit_needed: true` (*"Author fell back to token 'שער'"*) and `⚠️ (Needs Audit)` in the sheet header, while creating a corrupt fallback profile [`222 Authors/שער.md`].
- **Resolution**:
  - Attributed both sources to canonical author **`[[משנה ברורה]]`** (linking to existing [`222 Authors/משנה ברורה.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%9E%D7%A9%D7%A0%D7%94%20%D7%91%D7%A8%D7%55%D7%A8%D7%94.md)), with book `שער הציון`.
  - Extracted the specific footnote letter from the body text (`(כא)` for Siman 232, and `(יט)` for Siman 235), preventing future cross-sheet collisions:
    - **`משנה ברורה - שער הציון - סימן רלב אות כא.md`** (crop: `teima before tefilla_p2_s2.png`, header: `### אות כא`)
    - **`משנה ברורה - שער הציון - סימן רלה אות יט.md`** (crop: `teima before tefilla_p2_s8.png`, header: `### אות יט`)
  - Purged the corrupt fallback author [`222 Authors/שער.md`] and obsolete files `שער - הציון - סימן רלב.md` and `שער - הציון - סימן רלה.md`.

### 2. Sources #21 & #23 (Responsa Collision in `שו"ת יביע אומר חלק ה - או"ח סימן כב`)
- **Issue**: Both sources shared the identical header string `שו"ת יביע אומר חלק ה - או"ח סימן כב`. Because the second occurrence was matched against the existing file without section disambiguation, both image crops (`teima before tefilla_p3_s4.png` and `teima before tefilla_p3_s6.png`) collapsed into a single note, and both section embeds in `teima before tefilla.md` targeted the same identical file.
- **Resolution**:
  - Source #21 discusses whether the eating restriction before prayer applies to Musaf according to the Aruch HaShulchan (representing **אות א** of Siman 22).
  - Source #23 explicitly begins with section marker `ב/` in the text, analyzing whether Kiddush applies before Musaf (representing **אות ב**).
  - Disambiguated into two distinct canonical source notes:
    - **`רב עובדיה יוסף - שו''ת יביע אומר - חלק ה - או''ח סימן כב אות א.md`** (crop: `teima before tefilla_p3_s4.png`, anchor: `#אות א`)
    - **`רב עובדיה יוסף - שו''ת יביע אומר - חלק ה - או''ח סימן כב אות ב.md`** (crop: `teima before tefilla_p3_s6.png`, anchor: `#אות ב`)
  - Removed the collided file `רב עובדיה יוסף - שו''ת יביע אומר - חלק ה - או''ח סימן כב.md`.

### 3. Source #8 Multi-Page Spanning
- **Verification**: **שולחן ערוך אורח חיים סימן רלב סעיף ב** begins at the bottom of Page 1 and continues across the top of Page 2 before Source #9. Verified that both crops `teima before tefilla_p1_s8.png` and continuation crop `teima before tefilla_p2_cont.png` are properly embedded in [`333 Sources/שולחן ערוך - אורח חיים - סימן רלב סעיף ב.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%A9%D7%55%D7%9C%D7%97%D7%9F%20%D7%A2%D7%A8%D7%55%D7%9A%20-%20%D7%22%D7%95%D7%A8%D7%97%20%D7%97%D7%99%D7%99%D7%95%20-%20%D7%A1%D7%99%D7%9E%D7%9F%20%D7%A8%D7%9C%D7%91%20%D7%A1%D7%A2%D7%99%D7%A3%20%D7%91.md).

### 4. Preservation of User Notes
- **Verification**: Verified that [`333 Sources/תלמוד בבלי - מסכת ברכות - דף י עמוד ב.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%AA%D7%9C%D7%9E%D7%55%D7%93%20%D7%91%D7%91%D7%9C%D7%99%20-%20%D7%9E%D7%A1%D7%93%D7%AA%20%D7%91%D7%A8%D7%93%D7%95%D7%AA%20-%20%D7%93%D7%A3%20%D7%99%20%D7%A2%D7%9E%D7%55%D7%93%20%D7%91.md) retained all existing user study commentary under its internal heading while cleanly adopting the new crop `teima before tefilla_p1_s1.png`.

---

## 2. Full Sheet Verification (23/23)

| # | Canonical Title | Author | Status | Notes |
|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת ברכות - דף י עמוד ב` | [[תלמוד בבלי]] | ✅ Preserved | User study notes intact; crop `p1_s1` added |
| 2 | `רשב''א - חידושי הרשב''א מסכת ברכות - דף י עמוד ב` | [[רשב''א]] | ✅ Verified | Clean 2-header layout; crop `p1_s2` |
| 3 | `רא''ש - מסכת ברכות - פרק א סימן י` | [[רא''ש]] | ✅ Verified | Clean 2-header layout; crop `p1_s3` |
| 4 | `רבי יעקב בן אשר - טור אורח חיים - סימן פט` | [[רבי יעקב בן אשר]] | ✅ Verified | Clean 2-header layout; crop `p1_s4` |
| 5 | `בית יוסף - אורח חיים - סימן פט` | [[בית יוסף]] | ✅ Verified | Clean 2-header layout; crop `p1_s5` |
| 6 | `תלמוד בבלי - מסכת שבת - דף ט עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout; crop `p1_s6` |
| 7 | `רמב''ם - הלכות תפילה ונשיאת כפים - פרק ו הלכה ה` | [[רמב''ם]] | ✅ Verified | Clean 2-header layout; crop `p1_s7` |
| 8 | `שולחן ערוך - אורח חיים - סימן רלב סעיף ב` | [[שולחן ערוך]] | ✅ Verified | Multi-crop intact (`p1_s8` + `p2_cont`) |
| 9 | `משנה ברורה - סימן רלב ס''ק כד` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#נישואין או מילה`; crop `p2_s1` |
| 10 | `משנה ברורה - שער הציון - סימן רלב אות כא` | [[משנה ברורה]] | 🔧 **Fixed** | Attributed to MB; footnote `אות כא` extracted; audit cleared |
| 11 | `אגרות משה - חלק או''ח ד - סימן צט` | [[אגרות משה]] | ✅ Verified | Clean 2-header layout; crop `p2_s3` |
| 12 | `תלמוד בבלי - מסכת ברכות - דף ד עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout; crop `p2_s4` |
| 13 | `תוספות - מסכת ברכות - דף ד עמוד ב` | [[תוספות]] | ✅ Verified | Clean 2-header layout; crop `p2_s5` |
| 14 | `שולחן ערוך - אורח חיים - סימן רלה סעיף ב` | [[שולחן ערוך]] | ✅ Verified | Clean 2-header layout; crop `p2_s6` |
| 15 | `משנה ברורה - סימן רלה ס''ק יז` | [[משנה ברורה]] | ✅ Verified | Clean 2-header layout; crop `p2_s7` |
| 16 | `משנה ברורה - שער הציון - סימן רלה אות יט` | [[משנה ברורה]] | 🔧 **Fixed** | Attributed to MB; footnote `אות יט` extracted; audit cleared |
| 17 | `משנה ברורה - סימן רלה ס''ק כד` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#אע"פ שנטל ידיו`; crop `p2_s9` |
| 18 | `תלמוד בבלי - מסכת ברכות - דף כח עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Dibur Hamatchil `#אמר רב הונא`; crop `p3_s1` |
| 19 | `תלמוד בבלי - מסכת תענית - דף כו עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Dibur Hamatchil `#תניא`; crop `p3_s2` |
| 20 | `רא''ש - מסכת תענית - פרק ד סימן א` | [[רא''ש]] | ✅ Verified | Clean 2-header layout; crop `p3_s3` |
| 21 | `רב עובדיה יוסף - שו''ת יביע אומר - חלק ה - או''ח סימן כב אות א` | [[רב עובדיה יוסף]] | 🔧 **Fixed** | Disambiguated from Ot ב; crop `p3_s4` separated |
| 22 | `מגן אברהם - אורח חיים - סימן רפו ס''ק א` | [[מגן אברהם]] | ✅ Verified | Dibur Hamatchil `#אכילת פירות`; crop `p3_s5` |
| 23 | `רב עובדיה יוסף - שו''ת יביע אומר - חלק ה - או''ח סימן כב אות ב` | [[רב עובדיה יוסף]] | 🔧 **Fixed** | Disambiguated from Ot א; crop `p3_s6` separated |

---

## 3. Parser Root Cause Patches (`999 Scripts/process_source_sheets.py`)

1. **Sha'ar HaTziyun Recognition**:
   - Added `'שער הציון'` to `KNOWN_AUTHORS` and `KNOWN_HEADER_KEYWORDS`.
   - Added `'שער הציון': 'משנה ברורה'` to `AUTHOR_CANONICAL_MAP`.
   - In `parse_citation`: mapped `matched_text == "שער הציון"` to author `"משנה ברורה"` and book `"שער הציון"`.
2. **Sha'ar HaTziyun Footnote Detection**:
   - In `extract_sources_and_images`: when `book == "שער הציון"`, scans the decoded first line for reversed Davka parentheses enclosing the footnote marker (e.g. `)כא(` or `(יט)`), automatically enriching `location` with `אות {ot}` and setting `dibur_hamatchil = f"אות {ot}"`.
3. **Responsa Section Disambiguation**:
   - In `extract_sources_and_images`: detects leading section indicators (e.g. `ב/` in Source #23), enriching `location` with `אות {sec}`.
   - Added post-pass across extracted sources: when an un-sectioned responsa source shares a citation with a subsequent `אות ב` section, the earlier source is automatically attributed to `אות א`.
4. **Sheet Tracking (`seen_in_sheet`) on New Source Creation**:
   - Patched `process_source` to record `seen_in_sheet[file_base] = 1` immediately upon creating a new source note, ensuring any subsequent references within the same sheet correctly increment the usage counter.
