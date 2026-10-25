# Avos Source Sheet Audit

## Summary
Audited `111 Source Sheets/avos.md` (`000 Source PDFs/avos.pdf`, Subject: *Sunday*, Fall 2026 Midterm) — 26 canonical embedded sources across 4 pages. Fully verified every citation against the decoded Davka font text stream and PDF layout, resolved all multi-word titles and commentaries, unified multi-excerpt citations (Ramban Bereishis 26:5 across 3 distinct excerpts, Nefesh HaChaim across 2 distinct excerpts), created and enhanced canonical author profiles in `222 Authors/`, purged 6 corrupt fallback author profiles, verified and preserved all 29 image crops (including page continuation crops), and patched parser root causes in `process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #9 (`ספר המקנה על קידושין - דף פב עמוד א:`)
- **Issue**: Extracted by generic fallback as `author='ספר המקנה'`, `book='על קידושין'`, `location='דף פב עמוד א-'` and flagged `audit_needed: true` (*"Author fell back to token 'ספר המקנה'"*).
- **Resolution**: Renamed note to **`בעל הפלאה - ספר המקנה - מסכת קידושין דף פב עמוד א.md`**; attributed to canonical author **`[[בעל הפלאה]]`** (Rabbi Pinchas Halevi Horowitz, Baal Hafla'ah). Location cleaned of trailing hyphen and colon.
- **Author Note**: Enhanced [`222 Authors/בעל הפלאה.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%91%D7%A2%D7%9C%20%D7%94%D7%A4%D7%9C%D7%90%D7%94.md) with comprehensive aliases (`ספר המקנה`, `המקנה`, `פנים יפות`) and biographical history; purged fallback `222 Authors/ספר המקנה.md`.

### 2. Source #10 (`דעת זקנים מבעלי התוספות על בראשית פרק לז פסוק לה`)
- **Issue**: Extracted as `author='דעת'`, `book='זקנים מבעלי התוספות על בראשית'` and flagged `audit_needed: true` (*"Author fell back to token 'דעת'"*).
- **Resolution**: Renamed note to **`בעלי התוספות - דעת זקנים - בראשית פרק לז פסוק לה.md`**; attributed to canonical author **`[[בעלי התוספות]]`**.
- **Author Note**: Created [`222 Authors/בעלי התוספות.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%91%D7%A2%D7%9C%D7%99%20%D7%94%D7%55%D7%A1%D7%A4%D7%95%D7%AA.md); purged fallback `222 Authors/דעת.md`.

### 3. Source #11 (`חזקוני על בראשית פרק כט פסוק כט`)
- **Issue**: Flagged `audit_needed: true` on initial parse; book retained prefix `'על בראשית'`.
- **Resolution**: Standardized to **`חזקוני - בראשית - פרק כט פסוק כט.md`**, attributed to **`[[חזקוני]]`** with Dibur Hamatchil `### ויתן לו את רחל`.
- **Author Note**: Enhanced [`222 Authors/חזקוני.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%97%D7%96%D7%A7%D7%95%D7%A0%D7%99.md) with Rabbeinu Chizkiah ben Manoach bio and aliases.

### 4. Sources #13 & #16 (`בראשית רבה פרשה צד` & `פרשה עט`)
- **Issue**: Extracted with author `בראשית רבה` and empty location due to missing mapping in `AUTHOR_CANONICAL_MAP` and absence of `פרשה` in generic location regex.
- **Resolution**: Standardized to **`מדרש רבה - בראשית רבה - פרשה צד.md`** and **`מדרש רבה - בראשית רבה - פרשה עט.md`**, attributed to canonical author **`[[מדרש רבה]]`**, book `בראשית רבה`, locations `פרשה צד` and `פרשה עט`. Source #16 embeds Dibur Hamatchil `### ויחן את פני העיר`.

### 5. Sources #2 & #15 (Rashi Leading Verse Markers Stripped)
- **Issue**: Rashi commentary text begins with parenthesized verse letters (e.g. `(י) בן הכנענית` for verse 10, `(ה) אשר עשו בחרן` for verse 5), which were captured as part of the Dibur Hamatchil section headings.
- **Resolution**: Cleaned section headings in [`333 Sources/רש''י - בראשית - פרק מו פסוק י.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%A8%D7%A9''%D7%99%20-%20%D7%91%D7%A8%D7%90%D7%A9%D7%99%D7%AA%20-%20%D7%A4%D7%A8%D7%A7%20%D7%9E%D7%95%20%D7%A4%D7%A1%D7%95%D7%A7%20%D7%99.md) to `### בן הכנענית` (strictly preserving user study notes) and in [`333 Sources/רש''י - בראשית - פרק יב פסוק ה.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%A8%D7%A9''%D7%99%20-%20%D7%91%D7%A8%D7%90%D7%A9%D7%99%D7%AA%20-%20%D7%A4%D7%A8%D7%A7%20%D7%99%D7%91%20%D7%A4%D7%A1%D7%95%D7%A7%20%D7%94.md) to `### אשר עשו בחרן`. Updated embeds in [`111 Source Sheets/avos.md`](file:///home/sean/Obsidian/Rapp/111%20Source%20Sheets/avos.md).

### 6. Sources #8, #19, #22 (Ramban Bereishis 26:5 Multi-Excerpt Collision)
- **Issue**: Three distinct passages from the same long Ramban were included on the source sheet. The parser matched existing file `רמב''ן - בראשית - פרק כו פסוק ה.md`, causing crops to overwrite (`avos_p1_s8.png` was displaced) and sheet embeds to duplicate the same section heading.
- **Resolution**: Unified all 3 excerpts into the canonical note **`333 Sources/רמב''ן - בראשית - פרק כו פסוק ה.md`**:
  - Image block preserves all 3 crops: `avos_p1_s8.png`, `avos_p3_s4.png`, `avos_p3_s7.png`.
  - Created 3 distinct Dibur Hamatchil section headings:
    - `### ויש לשאול` (Source #8: Kashya on Yaakov erecting a Matzevah and marrying two sisters)
    - `### והנראה אלי מדעת רבותינו` (Source #19: Yesod of Eino Metzuvah V'Oseh)
    - `### ושמירתו אותה היה בארץ בלבד` (Source #22: Yesod of Mitzvos Hatluyos Ba'aretz)
  - Updated `111 Source Sheets/avos.md` so #8, #19, and #22 embed their respective distinct sections.

### 7. Source #20 (`קדושת הלוי בראשית פרק יד פסוק יח`)
- **Issue**: Extracted as `author='קדושת'`, `book='הלוי בראשית'` and flagged `audit_needed: true`.
- **Resolution**: Renamed note to **`רבי לוי יצחק מברדיטשוב - קדושת לוי - בראשית פרק יד פסוק יח.md`**, attributed to canonical author **`[[רבי לוי יצחק מברדיטשוב]]`**.
- **Author Note**: Created [`222 Authors/רבי לוי יצחק מברדיטשוב.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%9C%D7%95%D7%99%20%D7%99%D7%A6%D7%97%D7%A7%20%D7%9E%D7%91%D7%A8%D7%23%D7%99%D7%98%D7%A9%D7%95%D7%91.md); purged fallback `222 Authors/קדושת.md`.

### 8. Sources #21 & #23 (Nefesh HaChaim Sha'ar 1 Perek 20-21)
- **Issue**: Multi-word title split into `author='נפש'`, `book='החיים שער א!'`, and when Source #23 was processed, crop `avos_p3_s6.png` was displaced. Davka font exclamation point scrambled quote character.
- **Resolution**: Unified both excerpts into canonical note **`333 Sources/רבי חיים מוולוז'ין - נפש החיים - שער א פרק כ-כא.md`**, attributed to **`[[רבי חיים מוולוז'ין]]`**:
  - Image block preserves all crops: `avos_p3_s6.png`, `avos_p3_s8.png`, `avos_p4_cont.png`.
  - Created 2 distinct section headings:
    - `### והאדם הישר העובד אמיתי` (Source #21)
    - `### היינו שהשיגו ענייני הכחות העליונים` (Source #23)
  - Updated `avos.md` to embed each excerpt's specific section.
- **Author Note**: Created [`222 Authors/רבי חיים מוולוז'ין.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%97%D7%99%D7%99%D7%95%20%D7%9E%D7%95%D7%95%D7%9C%D7%95%D7%96'%D7%99%D7%9F.md); purged fallback `222 Authors/נפש.md`.

### 9. Source #24 (`קובץ שיערים קידושין ס! קמ א`)
- **Issue**: Davka font typo `שיערים` and exclamation mark `ס!` broke location regex, leaving `location=''` and storing corrupted string into `book`.
- **Resolution**: Renamed note to **`רבי אלחנן וסרמן - קובץ שעורים - קידושין סימן קמ אות א.md`**, attributed to canonical author **`[[רבי אלחנן וסרמן]]`**, book `קובץ שעורים`, location `קידושין סימן קמ אות א`.

### 10. Source #25 (`הטור הארוך על בראשית פרק מו פסוק י`)
- **Issue**: Generic location regex matched the token `טור` inside `הטור הארוך`, treating `טור הארוך...` as the location and leaving `author='ה'`, `book='מקור'` with audit flag.
- **Resolution**: Renamed note to **`רבי יעקב בן אשר - הטור הארוך - בראשית פרק מו פסוק י.md`**, attributed to canonical author **`[[רבי יעקב בן אשר]]`**, book `הטור הארוך`, location `בראשית פרק מו פסוק י`. Purged fallback `222 Authors/ה.md`.

### 11. Source #26 (`גור אריה בראשית פרק מו פסוק י`)
- **Issue**: Title split into `author='גור'`, `book='אריה בראשית'` with audit flag.
- **Resolution**: Renamed note to **`מהר''ל - גור אריה - בראשית פרק מו פסוק י.md`**, attributed to canonical author **`[[מהר''ל]]`**, book `גור אריה`, location `בראשית פרק מו פסוק י`.
- **Author Note**: Created [`222 Authors/מהר''ל.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%9E%D7%94%D7%A8''%D7%9C.md); purged fallback `222 Authors/גור.md`.

---

## 2. Complete Sheet Source Verification (26/26)

| # | Canonical Embedded Source | Canonical Author | Canonical Book | Canonical Location | Status |
|---|---|---|---|---|---|
| 1 | `![[תנ''ך - בראשית - פרק מו פסוק י#תנ''ך - בראשית - פרק מו פסוק י]]` | [[תנ''ך]] | בראשית | פרק מו פסוק י | ✅ Verified |
| 2 | `![[רש''י - בראשית - פרק מו פסוק י#בן הכנענית]]` | [[רש''י]] | בראשית | פרק מו פסוק י | 🔧 **Fixed (Verse Marker Stripped)** |
| 3 | `![[תלמוד בבלי - מסכת יומא - דף כח עמוד ב#אמר רב]]` | [[תלמוד בבלי]] | מסכת יומא | דף כח עמוד ב | ✅ Verified |
| 4 | `![[רש''י - בראשית - פרק לב פסוק ה#רש''י - בראשית - פרק לב פסוק ה]]` | [[רש''י]] | בראשית | פרק לב פסוק ה | ✅ Verified |
| 5 | `![[תנ''ך - ויקרא - פרק כד פסוק י#תנ''ך - ויקרא - פרק כד פסוק י]]` | [[תנ''ך]] | ויקרא | פרק כד פסוק י | ✅ Verified |
| 6 | `![[רש''י - ויקרא - פרק כד פסוק י#בתוך בני ישראל]]` | [[רש''י]] | ויקרא | פרק כד פסוק י | ✅ Verified |
| 7 | `![[רמב''ן - ויקרא - פרק כד פסוק י#רמב''ן - ויקרא - פרק כד פסוק י]]` | [[רמב''ן]] | ויקרא | פרק כד פסוק י | ✅ Verified |
| 8 | `![[רמב''ן - בראשית - פרק כו פסוק ה#ויש לשאול]]` | [[רמב''ן]] | בראשית | פרק כו פסוק ה | 🔧 **Fixed (DH Disambiguation)** |
| 9 | `![[בעל הפלאה - ספר המקנה - מסכת קידושין דף פב עמוד א#בעל הפלאה - ספר המקנה - מסכת קידושין דף פב עמוד א]]` | [[בעל הפלאה]] | ספר המקנה | מסכת קידושין דף פב עמוד א | 🔧 **Fixed (Author + Sefer)** |
| 10 | `![[בעלי התוספות - דעת זקנים - בראשית פרק לז פסוק לה#בעלי התוספות - דעת זקנים - בראשית פרק לז פסוק לה]]` | [[בעלי התוספות]] | דעת זקנים | בראשית פרק לז פסוק לה | 🔧 **Fixed (Author + Sefer)** |
| 11 | `![[חזקוני - בראשית - פרק כט פסוק כט#ויתן לו את רחל]]` | [[חזקוני]] | בראשית | פרק כט פסוק כט | 🔧 **Fixed (Book Clean)** |
| 12 | `![[הגרי''ז הלוי - על בראשית - פרק טז פסוק ה#הגרי''ז הלוי - על בראשית - פרק טז פסוק ה]]` | [[הגרי''ז הלוי]] | על בראשית | פרק טז פסוק ה | ✅ Verified |
| 13 | `![[מדרש רבה - בראשית רבה - פרשה צד#מדרש רבה - בראשית רבה - פרשה צד]]` | [[מדרש רבה]] | בראשית רבה | פרשה צד | 🔧 **Fixed (Midrash Rabbah)** |
| 14 | `![[תלמוד בבלי - מסכת סנהדרין - דף נט עמוד א#ואמר רבי יוחנן]]` | [[תלמוד בבלי]] | מסכת סנהדרין | דף נט עמוד א | ✅ Verified |
| 15 | `![[רש''י - בראשית - פרק יב פסוק ה#אשר עשו בחרן]]` | [[רש''י]] | בראשית | פרק יב פסוק ה | 🔧 **Fixed (Pasuk + DH Clean)** |
| 16 | `![[מדרש רבה - בראשית רבה - פרשה עט#ויחן את פני העיר]]` | [[מדרש רבה]] | בראשית רבה | פרשה עט | 🔧 **Fixed (Midrash Rabbah)** |
| 17 | `![[תלמוד בבלי - מסכת סנהדרין - דף נח עמוד ב#ואמר ריש לקיש]]` | [[תלמוד בבלי]] | מסכת סנהדרין | דף נח עמוד ב | ✅ Verified |
| 18 | `![[רבי יעקב עטלינגר - שו''ת בנין ציון - סימן קכו#רבי יעקב עטלינגר - שו''ת בנין ציון - סימן קכו]]` | [[רבי יעקב עטלינגר]] | שו''ת בנין ציון | סימן קכו | ✅ Verified |
| 19 | `![[רמב''ן - בראשית - פרק כו פסוק ה#והנראה אלי מדעת רבותינו]]` | [[רמב''ן]] | בראשית | פרק כו פסוק ה | 🔧 **Fixed (DH Disambiguation)** |
| 20 | `![[רבי לוי יצחק מברדיטשוב - קדושת לוי - בראשית פרק יד פסוק יח#רבי לוי יצחק מברדיטשוב - קדושת לוי - בראשית פרק יד פסוק יח]]` | [[רבי לוי יצחק מברדיטשוב]] | קדושת לוי | בראשית פרק יד פסוק יח | 🔧 **Fixed (Author + Sefer)** |
| 21 | `![[רבי חיים מוולוז'ין - נפש החיים - שער א פרק כ-כא#והאדם הישר העובד אמיתי]]` | [[רבי חיים מוולוז'ין]] | נפש החיים | שער א פרק כ-כא | 🔧 **Fixed (DH Disambiguation)** |
| 22 | `![[רמב''ן - בראשית - פרק כו פסוק ה#ושמירתו אותה היה בארץ בלבד]]` | [[רמב''ן]] | בראשית | פרק כו פסוק ה | 🔧 **Fixed (DH Disambiguation)** |
| 23 | `![[רבי חיים מוולוז'ין - נפש החיים - שער א פרק כ-כא#היינו שהשיגו ענייני הכחות העליונים]]` | [[רבי חיים מוולוז'ין]] | נפש החיים | שער א פרק כ-כא | 🔧 **Fixed (DH Disambiguation)** |
| 24 | `![[רבי אלחנן וסרמן - קובץ שעורים - קידושין סימן קמ אות א#רבי אלחנן וסרמן - קובץ שעורים - קידושין סימן קמ אות א]]` | [[רבי אלחנן וסרמן]] | קובץ שעורים | קידושין סימן קמ אות א | 🔧 **Fixed (Font Decode + Loc)** |
| 25 | `![[רבי יעקב בן אשר - הטור הארוך - בראשית פרק מו פסוק י#רבי יעקב בן אשר - הטור הארוך - בראשית פרק מו פסוק י]]` | [[רבי יעקב בן אשר]] | הטור הארוך | בראשית פרק מו פסוק י | 🔧 **Fixed (Tur Regex Collision)** |
| 26 | `![[מהר''ל - גור אריה - בראשית פרק מו פסוק י#מהר''ל - גור אריה - בראשית פרק מו פסוק י]]` | [[מהר''ל]] | גור אריה | בראשית פרק מו פסוק י | 🔧 **Fixed (Author + Sefer)** |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Classic Multi-Word Titles in `RESPONSA_SPECIAL_MAP`**:
   - Added direct mappings for:
     - `ספר המקנה`, `המקנה` $\to$ `('בעל הפלאה', 'ספר המקנה')`
     - `דעת זקנים` $\to$ `('בעלי התוספות', 'דעת זקנים')`
     - `קדושת לוי`, `קדושת הלוי` $\to$ `('רבי לוי יצחק מברדיטשוב', 'קדושת לוי')`
     - `נפש החיים` $\to$ `("רבי חיים מוולוז'ין", 'נפש החיים')`
     - `גור אריה` $\to$ `("מהר''ל", 'גור אריה')`
     - `הטור הארוך`, `טור הארוך` $\to$ `('רבי יעקב בן אשר', 'הטור הארוך')`
     - `קובץ שיעורים`, `קובץ שעורים`, `קובץ שיערים` $\to$ `('רבי אלחנן וסרמן', 'קובץ שעורים')`
   - Added contextual Chumash/Maseches routing so that citations like `ספר המקנה על קידושין דף פב ע"א` route `מסכת קידושין` into the location, and `גור אריה בראשית פרק מו` routes `בראשית` into the location.

2. **Canonical Author Database Mappings (`AUTHOR_CANONICAL_MAP`)**:
   - Mapped all 10 Midrash Rabbah works (`בראשית רבה`, `שמות רבה`, `ויקרא רבה`, `דברים רבה`, `שיר השירים רבה`, `איכה רבה`, `קהלת רבה`, `אסתר רבה`) directly to canonical author `מדרש רבה`.
   - Added canonical author entries for `ספר המקנה`, `דעת זקנים`, `קדושת לוי`, `קדושת הלוי`, `נפש החיים`, `גור אריה`, `הטור הארוך`, `טור הארוך`, `חזקוני`, and `בעלי התוספות`.

3. **Prevention of Tur False Positive in Location Matching**:
   - Replaced plain `טור` in both `RESPONSA_SPECIAL_MAP` and generic `loc_match` regexes with `(?<![א-ת])טור\s+[א-ד0-9]`. This allows column numbers (e.g. Yerushalmi `טור ג`) to trigger location matching while completely preventing Sefer titles like `הטור` or `הטור הארוך` from being parsed as a location token.

4. **Added `פרשה` to Location Regex & Midrash Rabbah Parsing**:
   - Added `פרשה` into the generic location matching regex. When `author == "מדרש רבה"`, auto-populates `book` with the specific Rabbah midrash (e.g., `בראשית רבה`) and routes `פרשה` into `location`.

5. **Davka Font Stream Exclamation Point & Siman Normalization**:
   - Expanded post-cleaning in `RESPONSA_SPECIAL_MAP` to translate Davka exclamation points `!` into standard geresh/single quotes `'`, and translate `ס!` into `סימן `.

6. **Automatic Verse Marker Stripping from Dibur Hamatchil**:
   - Added regex cleanup in `extract_sources_and_images` to automatically strip leading parenthesized verse letters (e.g. `(י)` or `(ה)`) from extracted Dibur Hamatchil headings across commentary texts.
