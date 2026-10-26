# Tekhelet Source Sheet Audit

## Summary
Audited `111 Source Sheets/tekhelet.md` (`000 Source PDFs/tekhelet.pdf`, Subject: *Halacha*, Fall 2026 Midterm). Resolved major document segmentation issues where sub-bullet points in an editorial summary note on Tekhelet identification (Source #21) triggered false header detections, inflating the source count from 26 to 30. Re-attributed modern rabbinic articles and responsa to canonical author profiles, cleaned up 11 corrupt fallback author files, consolidated 5 fragmented junk source notes into a unified source, preserved all user study notes on Sources #1 and #2, and patched root causes in `999 Scripts/process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files, and strictly 26 verified canonical sources.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Sources #1 & #2 (User Study Notes Strictly Preserved)
- **Status**: Verified intact and untouched.
- **Source #1**: [`333 Sources/תנ''ך - במדבר - פרק טו פסוק לח.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%AA%D7%A0''%D7%9A%20-%20%D7%91%D7%9E%D7%93%D7%91%D7%A8%20-%20%D7%A4%D7%A8%D7%A7%20%D7%98%D7%95%20%D7%A4%D7%A1%D7%95%D7%A7%20%D7%94.md) retains:
  `You must wear ציצית and they must have a fringe of תכילת`
- **Source #2**: [`333 Sources/תלמוד בבלי - מסכת מנחות - דף לח עמוד א.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%AA%D7%9C%D7%9E%D7%95%D7%93%20%D7%91%D7%91%D7%9C%D7%99%20-%20%D7%9E%D7%A1%D7%9B%D7%AA%20%D7%9E%D7%A0%D7%97%D7%95%D7%AA%20-%20%D7%93%D7%A3%20%D7%9E%D7%94%20%D7%A2%D7%9E%D7%95%D7%93%20%D7%90.md) retains:
  `If you don't have white or blue, you can have full white/blue`
  `If you don't have arms, you can still put on a תפילין של ראש`

### 2. Source #3 (`ספר המצוות לרמב"ם מצות עשה יד`)
- **Issue**: Hardcoded special handling in `process_source_sheets.py` set `location = ""` whenever a citation began with `ספר המצוות`, discarding `מצות עשה יד`.
- **Resolution**: Renamed note to **`רמב''ם - ספר המצוות - מצות עשה יד.md`**, attributed to **`[[רמב''ם]]`**, Book: `ספר המצוות`, Location: `מצות עשה יד`. Updated embed on sheet.

### 3. Source #4 (`השגות הרמב"ן לספר המצוות שורש יא`)
- **Issue**: Missing `שורש` token in location regex left `שורש יא` embedded in the book title and empty location.
- **Resolution**: Renamed note to **`רמב''ן - השגות לספר המצוות - שורש יא.md`**, attributed to **`[[רמב''ן]]`**, Book: `השגות לספר המצוות`, Location: `שורש יא`. Updated embed on sheet.

### 4. Source #5 (`ר׳ נחום לאם - תכלת בציצית-לאור התגליות החדישות ד׳ י"ז`)
- **Issue**: Rabbi Norman Lamm was not mapped, and prefix `ר׳` was stripped by heuristic fallback leaving author as `מקור` with active audit flag.
- **Resolution**: Renamed note to **`הרב נחום לאם - תכלת בציצית לאור התגליות החדישות - דף יז.md`**, attributed to canonical author **`[[הרב נחום לאם]]`**, Book: `תכלת בציצית לאור התגליות החדישות`, Location: `דף יז`. Audit flag cleared.
- **Author Note**: Created [`222 Authors/הרב נחום לאם.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%A0%D7%97%D7%95%D7%9D%20%D7%9C%D7%90%D7%9D.md) with biography and aliases; purged fallback `222 Authors/מקור.md`.

### 5. Source #7 (`שו"ת ישועות מלכו חלק אורח חיים סימן ג`)
- **Issue**: Title fell back to `author='שו"ת ישועות'`, `book='מלכו חלק אורח חיים'` with audit flag.
- **Resolution**: Renamed note to **`רבי יהושע מקוטנא - שו''ת ישועות מלכו - חלק אורח חיים סימן ג.md`**, attributed to canonical author **`[[רבי יהושע מקוטנא]]`** (Rabbi Yehoshua Trunk of Kutno), Book: `שו''ת ישועות מלכו`, Location: `חלק אורח חיים סימן ג`.
- **Author Note**: Created [`222 Authors/רבי יהושע מקוטנא.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%99%D7%94%D7%95%D7%55%D7%A2%20%D7%9E%D7%A7%D7%95%D7%98%D7%A0%D7%90.md); purged fallback `222 Authors/שו''ת ישועות.md`.

### 6. Source #15 (`קופת רוכלים - הקדמת ה"תפארת ישראל! לסדר מועד`)
- **Issue**: Davka exclamation point `!` corrupted quotation mark, and introduction title was packed entirely into book with empty location.
- **Resolution**: Renamed note to **`רבי ישראל ליפשיץ - קופת רוכלים - הקדמת התפארת ישראל לסדר מועד.md`**, attributed to **`[[רבי ישראל ליפשיץ]]`**, Book: `קופת רוכלים`, Location: `הקדמת התפארת ישראל לסדר מועד`.

### 7. Sources #16 & #20 (Rav Soloveitchik Works Unified)
- **Issue**: Source #16 fell back to `author='מבית'` and Source #20 fell back to `author='רב'` with audit flags.
- **Resolution**:
  - Source #16 standardized to **`הרב יוסף דוב סולוביצ׳יק - מבית מדרשו של הרב - עמוד סח.md`**.
  - Source #20 standardized to **`הרב יוסף דוב סולוביצ׳יק - שיעורים לזכר אבא מרי - חלק א עמוד רכח.md`**.
- **Author Note**: Created canonical profile [`222 Authors/הרב יוסף דוב סולוביצ׳יק.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%99%D7%95%D7%A1%D7%A3%20%D7%93%D7%95%D7%91%20%D7%A1%D7%95%D7%94%D7%95%D7%91%D7%99%D7%A6%D7%B3%D7%99%D7%A7.md) with aliases (`הגרי"ד`, `יוסף דוב הלוי סולובייצ'יק`); purged fallback author profiles `222 Authors/מבית.md` and `222 Authors/רב.md`.

### 8. Source #21 & Elimination of 5 Fragmented Junk Notes
- **Issue**: In `tekhelet.pdf`, Source #21 (`ההוכחות לזיהוי אינן מוחלטות ויש עליהן כמה שאלות`) lists 7 counterarguments formatted with numbered bullets (`1(`, `2(`, `3(`, `4(`, `5(` on page 3, continuing with `6(`, `7(` on page 4). The parser erroneously treated these bullets as source headers, creating 5 fragmented notes (`ההוכחות...`, `אין...`, `האמיתית...`, `יש...`, `מופיע...`) and 4 junk author notes (`אין.md`, `האמיתית-.md`, `יש.md`, `ההוכחות.md`).
- **Resolution**:
  - Unified into single canonical source note **`333 Sources/בירור הלכה - שאלות על זיהוי התכלת - ההוכחות לזיהוי אינן מוחלטות.md`**, attributed to **`[[בירור הלכה]]`**, Book: `שאלות על זיהוי התכלת`, Location: `ההוכחות לזיהוי אינן מוחלטות`.
  - Image block captures the entire text across the page boundary (`tekhelet_p3_s2.png` and continuation `tekhelet_p4_cont.png`).
  - Purged 5 fragmented source notes and deleted the 4 corrupt fallback author profiles.

### 9. Source #23 (Rav Shlomo Aviner on Srugim)
- **Issue**: Extracted with author `גדולי-ישראל-נגד-התכלת-של-ימינו-רשימת` and URL as book with audit flag.
- **Resolution**: Renamed note to **`הרב שלמה אבינר - אתר סרוגים - גדולי ישראל נגד התכלת של ימינו.md`**, attributed to canonical author **`[[הרב שלמה אבינר]]`**, Book: `אתר סרוגים`, Location: `גדולי ישראל נגד התכלת של ימינו`.
- **Author Note**: Created [`222 Authors/הרב שלמה אבינר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%A9%D7%9C%D7%9E%D7%94%20%D7%90%D7%91%D7%99%D7%A0%D7%A0.md); purged fallback `222 Authors/גדולי-ישראל-נגד-התכלת-של-ימינו-רשימת.md`.

### 10. Sources #24 & #26 (Rav Mordechai Willig — Kol Tzvi Vol. 22)
- **Issue**: Extracted with author `קול` and long string as book with audit flags.
- **Resolution**:
  - Source #24 standardized to **`הרב מרדכי וויליג - קול צבי - כרך כב עמוד 131.md`**.
  - Source #26 standardized to **`הרב מרדכי וויליג - קול צבי - כרך כב עמוד 136.md`**.
- **Author Note**: Created [`222 Authors/הרב מרדכי וויליג.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%9E%D7%A0%D7%93%D7%9B%D7%99%20%D7%95%D7%95%D7%99%D7%9C%D7%99%D7%92.md); purged fallback `222 Authors/קול.md`.

### 11. Source #25 (Rav Hershel Schachter — Ginat Egoz)
- **Issue**: Extracted with author `גינת`, book `אגוז` with audit flag.
- **Resolution**: Renamed note to **`הרב צבי שכטר - גינת אגוז - סימן ב.md`**, attributed to canonical author **`[[הרב צבי שכטר]]`**, Book: `גינת אגוז`, Location: `סימן ב`.
- **Author Note**: Created [`222 Authors/הרב צבי שכטר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%A6%D7%91%D7%99%20%D7%A1%D7%9B%D7%98%D7%A0.md) with aliases (`הגרצ"ש`, `הרב צבי הרשל שכטר`); purged fallback `222 Authors/גינת.md`.

---

## 2. Complete Sheet Source Verification (26/26)

| # | Canonical Embedded Source | Canonical Author | Canonical Book | Canonical Location | Status |
|---|---|---|---|---|---|
| 1 | `![[תנ''ך - במדבר - פרק טו פסוק לח#תנ''ך - במדבר - פרק טו פסוק לח]]` | [[תנ''ך]] | במדבר | פרק טו פסוק לח | ✅ Verified (User Notes Preserved) |
| 2 | `![[תלמוד בבלי - מסכת מנחות - דף לח עמוד א#תלמוד בבלי - מסכת מנחות - דף לח עמוד א]]` | [[תלמוד בבלי]] | מסכת מנחות | דף לח עמוד א | ✅ Verified (User Notes Preserved) |
| 3 | `![[רמב''ם - ספר המצוות - מצות עשה יד#רמב''ם - ספר המצוות - מצות עשה יד]]` | [[רמב''ם]] | ספר המצוות | מצות עשה יד | 🔧 **Fixed (Location Parsed)** |
| 4 | `![[רמב''ן - השגות לספר המצוות - שורש יא#רמב''ן - השגות לספר המצוות - שורש יא]]` | [[רמב''ן]] | השגות לספר המצוות | שורש יא | 🔧 **Fixed (Shoresh Loc Parsed)** |
| 5 | `![[הרב נחום לאם - תכלת בציצית לאור התגליות החדישות - דף יז#הרב נחום לאם - תכלת בציצית לאור התגליות החדישות - דף יז]]` | [[הרב נחום לאם]] | תכלת בציצית לאור התגליות החדישות | דף יז | 🔧 **Fixed (Author + Location)** |
| 6 | `![[מדרש תנחומא - פרשת שלח - סימן טו#מדרש תנחומא - פרשת שלח - סימן טו]]` | [[מדרש תנחומא]] | פרשת שלח | סימן טו | ✅ Verified |
| 7 | `![[רבי יהושע מקוטנא - שו''ת ישועות מלכו - חלק אורח חיים סימן ג#רבי יהושע מקוטנא - שו''ת ישועות מלכו - חלק אורח חיים סימן ג]]` | [[רבי יהושע מקוטנא]] | שו''ת ישועות מלכו | חלק אורח חיים סימן ג | 🔧 **Fixed (Responsa Poskim)** |
| 8 | `![[תלמוד בבלי - מסכת מנחות - דף מב עמוד ב#אמר ליה אביי לרב שמואל בר רב יהודה]]` | [[תלמוד בבלי]] | מסכת מנחות | דף מב עמוד ב | ✅ Verified |
| 9 | `![[תלמוד בבלי - מסכת מנחות - דף מד עמוד א#ת"ר]]` | [[תלמוד בבלי]] | מסכת מנחות | דף מד עמוד א | ✅ Verified |
| 10 | `![[תלמוד בבלי - מסכת מגילה - דף ו עמוד א#אמר זבולון לפני הקדוש ברוך הוא]]` | [[תלמוד בבלי]] | מסכת מגילה | דף ו עמוד א | ✅ Verified |
| 11 | `![[תלמוד בבלי - מסכת בבא מציעא - דף סא עמוד ב#אמר רבא]]` | [[תלמוד בבלי]] | מסכת בבא מציעא | דף סא עמוד ב | ✅ Verified |
| 12 | `![[תלמוד ירושלמי - מסכת ברכות - פרק א דף ג טור א -ה''ב#תלמוד ירושלמי - מסכת ברכות - פרק א דף ג טור א -ה''ב]]` | [[תלמוד ירושלמי]] | מסכת ברכות | פרק א דף ג טור א -ה''ב | ✅ Verified |
| 13 | `![[רמב''ם - הלכות ציצית - פרק ב הלכה א#רמב''ם - הלכות ציצית - פרק ב הלכה א]]` | [[רמב''ם]] | הלכות ציצית | פרק ב הלכה א | ✅ Verified |
| 14 | `![[תוספתא - מסכת מנחות - פרק ט הלכה טז#תוספתא - מסכת מנחות - פרק ט הלכה טז]]` | [[תוספתא]] | מסכת מנחות | פרק ט הלכה טז | ✅ Verified |
| 15 | `![[רבי ישראל ליפשיץ - קופת רוכלים - הקדמת התפארת ישראל לסדר מועד#רבי ישראל ליפשיץ - קופת רוכלים - הקדמת התפארת ישראל לסדר מועד]]` | [[רבי ישראל ליפשיץ]] | קופת רוכלים | הקדמת התפארת ישראל לסדר מועד | 🔧 **Fixed (Exclamation Cleaned)** |
| 16 | `![[הרב יוסף דוב סולוביצ׳יק - מבית מדרשו של הרב - עמוד סח#הרב יוסף דוב סולוביצ׳יק - מבית מדרשו של הרב - עמוד סח]]` | [[הרב יוסף דוב סולוביצ׳יק]] | מבית מדרשו של הרב | עמוד סח | 🔧 **Fixed (Author + Location)** |
| 17 | `![[רש''י - שמות - פרק כה פסוק ד#ותכלת]]` | [[רש''י]] | שמות | פרק כה פסוק ד | ✅ Verified |
| 18 | `![[רש''י - במדבר - פרק טו פסוק מא#פתיל תכלת]]` | [[רש''י]] | במדבר | פרק טו פסוק מא | ✅ Verified |
| 19 | `![[Wikipedia - Tekhelet#Wikipedia - Tekhelet]]` | [[Wikipedia]] | Tekhelet | | ✅ Verified (Continuation Crop) |
| 20 | `![[הרב יוסף דוב סולוביצ׳יק - שיעורים לזכר אבא מרי - חלק א עמוד רכח#הרב יוסף דוב סולוביצ׳יק - שיעורים לזכר אבא מרי - חלק א עמוד רכח]]` | [[הרב יוסף דוב סולוביצ׳יק]] | שיעורים לזכר אבא מרי | חלק א עמוד רכח | 🔧 **Fixed (Author + Location)** |
| 21 | `![[בירור הלכה - שאלות על זיהוי התכלת - ההוכחות לזיהוי אינן מוחלטות#בירור הלכה - שאלות על זיהוי התכלת - ההוכחות לזיהוי אינן מוחלטות]]` | [[בירור הלכה]] | שאלות על זיהוי התכלת | ההוכחות לזיהוי אינן מוחלטות | 🔧 **Fixed (Fragmented Bullets Unified)** |
| 22 | `![[ערוך השולחן - אורח חיים - סימן ט סעיף יב#ערוך השולחן - אורח חיים - סימן ט סעיף יב]]` | [[ערוך השולחן]] | אורח חיים | סימן ט סעיף יב | ✅ Verified |
| 23 | `![[הרב שלמה אבינר - אתר סרוגים - גדולי ישראל נגד התכלת של ימינו#הרב שלמה אבינר - אתר סרוגים - גדולי ישראל נגד התכלת של ימינו]]` | [[הרב שלמה אבינר]] | אתר סרוגים | גדולי ישראל נגד התכלת של ימינו | 🔧 **Fixed (Author + Article)** |
| 24 | `![[הרב מרדכי וויליג - קול צבי - כרך כב עמוד 131#הרב מרדכי וויליג - קול צבי - כרך כב עמוד 131]]` | [[הרב מרדכי וויליג]] | קול צבי | כרך כב עמוד 131 | 🔧 **Fixed (Author + Pagination)** |
| 25 | `![[הרב צבי שכטר - גינת אגוז - סימן ב#הרב צבי שכטר - גינת אגוז - סימן ב]]` | [[הרב צבי שכטר]] | גינת אגוז | סימן ב | 🔧 **Fixed (Rav Schachter Ginat Egoz)** |
| 26 | `![[הרב מרדכי וויליג - קול צבי - כרך כב עמוד 136#הרב מרדכי וויליג - קול צבי - כרך כב עמוד 136]]` | [[הרב מרדכי וויליג]] | קול צבי | כרך כב עמוד 136 | 🔧 **Fixed (Author + Pagination)** |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Sub-Bullet Suppression in Numbered Source Documents (`cur_max_header_num`)**:
   - In documents with sequential numbered headers (`has_numbered_doc`), sub-bullet lists in body paragraphs (such as `1(`, `2(`, `3(` inside Source #21) triggered false header detection.
   - Added monotonic header sequence tracking across pages. When `cur_max_header_num >= 5`, any candidate number jumping backwards (`found_num < cur_max_header_num - 2`) is rejected as an internal sub-bullet, cleanly preserving Source #21 as a unified multi-page source.

2. **Rambam Sefer HaMitzvot Location Parsing**:
   - Fixed hardcoded truncation that cleared `location = ""` for citations starting with `ספר המצוות`. The parser now extracts the remaining text, strips Rambam honorific prefixes (`לרמב"ם`), and extracts the Mitzvah location (`מצות עשה יד`).

3. **Expanded `loc_match` Keywords**:
   - Added `שורש\s+[א-ת0-9]+`, `שורש`, `הקדמת`, `עמוד`, `עמ׳`, `ד׳`, `כרך` to both `RESPONSA_SPECIAL_MAP` and generic `loc_match` regexes.

4. **Multi-Word Sefarim & Responsa Mappings (`RESPONSA_SPECIAL_MAP`)**:
   - Added direct mappings for:
     - `ישועות מלכו` $\to$ `('רבי יהושע מקוטנא', "שו''ת ישועות מלכו")`
     - `קופת רוכלים` $\to$ `('רבי ישראל ליפשיץ', 'קופת רוכלים')`
     - `מבית מדרשו של הרב` $\to$ `('הרב יוסף דוב סולוביצ׳יק', 'מבית מדרשו של הרב')`
     - `שיעורים לזכר אבא מרי` $\to$ `('הרב יוסף דוב סולוביצ׳יק', 'שיעורים לזכר אבא מרי')`
     - `גינת אגוז` $\to$ `('הרב צבי שכטר', 'גינת אגוז')`
     - `קול צבי` $\to$ `('הרב מרדכי וויליג', 'קול צבי')`
     - `השגות הרמב"ן לספר המצוות` $\to$ `("רמב''ן", 'השגות לספר המצוות')`

5. **Canonical Author Database Mappings (`AUTHOR_CANONICAL_MAP`)**:
   - Added mappings for Rabbi Norman Lamm, Rabbi Yehoshua Trunk of Kutno, Rav Joseph B. Soloveitchik, Rav Mordechai Willig, Rav Hershel Schachter, Rav Shlomo Aviner, and Birur Halacha.
