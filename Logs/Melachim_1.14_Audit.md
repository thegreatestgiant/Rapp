# Melachim 1.14 Source Sheet Audit

## Summary
Audited `111 Source Sheets/melachim 1.14.md` (`000 Source PDFs/melachim 1.14.pdf`, Subject: *Navi*, Fall 2026 Final) — 17 embedded sources. Verified every citation against the decoded Davka font text stream and PDF layout, resolved all 4 flagged/corrupt sources (**מדרש הנעלם**, **חומת אנך**, **מדבר קדמות**, and **אור לישרים**), standardized **שו"ת אבני נזר**, enriched canonical author profiles in `222 Authors/` (**זוהר**, **חיד''א**, **רבי שמריהו שולמן**, and **אבני נזר**), purged corrupt fallback author profiles (`אור.md`, `חומת.md`, `מדבר.md`, `מדרש.md`), verified continuation crops `melachim 1.14_p2_cont.png` (Moed Katan 28b) and `melachim 1.14_p3_cont.png` (Bava Kama 38b), preserved user study notes under Berakhot 10b (Source #3) and Kesef Mishneh (Source #12), and patched all root causes in `process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #7 (`מדרש הנעלם פרשת בראשית מאמר חנוך בן ירד`)
- **Issue**: Unmapped midrashic title caused parser to fall back to `author='מדרש'` and `book='הנעלם פרשת בראשית'`, generated corrupt fallback author note `222 Authors/מדרש.md`, and flagged the source `audit_needed: true` (*"Author fell back to token 'מדרש'"*).
- **Resolution**: Identified work as *Midrash HaNe'elam* on Parshat Bereishit (Ma'amar Chanoch ben Yered), a foundational component of Sefer HaZohar. Attributed to canonical author **`[[זוהר]]`**. Standardized note to **`זוהר - מדרש הנעלם - פרשת בראשית מאמר חנוך בן ירד.md`**, book `מדרש הנעלם`, location `פרשת בראשית מאמר חנוך בן ירד`.
- **Author Note**: Updated [`222 Authors/זוהר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%96%D7%22%D7%95%D7%94%D7%A8.md) with aliases `[ספר הזוהר, הזוהר הקדוש, הזוהר, זהר, מדרש הנעלם, זהר חדש, זוהר חדש]` and scholarly background; purged fallback `222 Authors/מדרש.md`.

### 2. Source #8 (`חומת אנך מלכים א פרק יד`)
- **Issue**: Parser fell back to `author='חומת'`, `book='אנך מלכים א'`, generating corrupt fallback author `222 Authors/חומת.md`, and flagged `audit_needed: true` (*"Author fell back to token 'חומת'"*).
- **Resolution**: Identified work as *Chomat Anach* on Melachim I by the Chida (Rabbi Chaim Yosef David Azulai). Attributed to canonical author **`[[חיד''א]]`** (matching vault note `חיד''א - חומת אנך על מלכים א - פרק ד פסוק כ.md`). Standardized note to **`חיד''א - חומת אנך על מלכים א - פרק יד.md`**, book `חומת אנך על מלכים א`, location `פרק יד`.
- **Author Note**: Updated [`222 Authors/חיד''א.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%97%D7%99%D7%93''%D7%90.md) with aliases `[החיד''א, החיד"א, חיד"א, חיד'א, רבי חיים יוסף דוד אזולאי, חיים יוסף דוד אזולאי, חומת אנך, מדבר קדמות, ברכי יוסף, פתח עינים, Chida]`; purged fallback `222 Authors/חומת.md`.

### 3. Source #14 (`מדבר קדמות מערכת נ אות כד`)
- **Issue**: Parser fell back to `author='מדבר'`, `book='קדמות מערכת נ'`, generating corrupt fallback author `222 Authors/מדבר.md`, and flagged `audit_needed: true` (*"Author fell back to token 'מדבר'"*).
- **Resolution**: Identified work as *Midbar K'deimot* (encyclopedic entry on *Na'amah Ha'Amonit*, Ma'arechet Nun, Os 24) by the Chida. Attributed to canonical author **`[[חיד''א]]`**. Standardized note to **`חיד''א - מדבר קדמות - מערכת נ אות כד.md`**, book `מדבר קדמות`, location `מערכת נ אות כד`. Purged fallback `222 Authors/מדבר.md`.

### 4. Source #15 (`אור לישרים )ר"ש שולמן( ד׳ רטו`)
- **Issue**: Parser fell back to `author='אור'`, `book='לישרים'`, generating corrupt fallback author `222 Authors/אור.md`, and flagged `audit_needed: true` (*"Author fell back to token 'אור'"*).
- **Resolution**: Identified work as *Ohr LiYesharim* by Rabbi Shmaryahu Shulman (revered rosh yeshiva, posek, and rebbe of Rabbi Hershel Schachter). Attributed to canonical author **`[[רבי שמריהו שולמן]]`** (linking to existing [`222 Authors/רבי שמריהו שולמן.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%A9%D7%9E%D7%A8%D7%99%D7%94%D7%95%20%D7%A9%D7%95%D7%9C%D7%9E%D7%9F.md)). Standardized note to **`רבי שמריהו שולמן - אור לישרים - דף רטו.md`**, book `אור לישרים`, location `דף רטו`. Added aliases `[שמריהו שולמן, שמריה שולמן, ר' שמריהו שולמן, ר' שמריה שולמן, ר"ש שולמן, ר''ש שולמן, אור לישרים]` to author note; purged fallback `222 Authors/אור.md`.

### 5. Source #17 (`שו"ת אבני נזר חלק יו"ד סימן שיב ד"ה יח( עוד`)
- **Issue**: Book parsed merely as `חלק יו''ד` instead of the canonical sefer title `שו''ת אבני נזר חלק יו''ד`.
- **Resolution**: Identified responsa work *She'elot U'Teshuvot Avnei Nezer*, section *Yoreh De'ah*, siman 312. Standardized note to **`אבני נזר - שו''ת אבני נזר חלק יו''ד - סימן שיב ד''ה יח עוד.md`**, author `[[אבני נזר]]`, book `שו''ת אבני נזר חלק יו''ד`, location `סימן שיב ד''ה יח עוד`.
- **Author Note**: Updated [`222 Authors/אבני נזר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%90%D7%91%D7%A0%D7%99%20%D7%A0%D7%96%D7%A8.md) with comprehensive aliases and biography.

### 6. User Study Notes Preserved
- **Berakhot 10b (Source #3)**: Preserved existing study notes under `### תלמוד בבלי - מסכת ברכות - דף י עמוד ב - melachim 1.6` and `### תלמוד בבלי - מסכת ברכות - דף י עמוד ב - teima before tefilla`, and established dedicated disambiguated subsection `### תלמוד בבלי - מסכת ברכות - דף י עמוד ב - melachim 1.14` containing full English translation of the Kings I 14:9 derashah (*"And You have cast Me behind your back [gavecha]... do not read it as gavecha, but rather ge'echa"*), referenced cleanly in [`111 Source Sheets/melachim 1.14.md`](file:///home/sean/Obsidian/Rapp/111%20Source%20Sheets/melachim%201.14.md).
- **Kesef Mishneh (Source #12)**: Preserved study notes (*"His mother was a convert, but because his father was king he could be king"*) intact in [`333 Sources/רבי יוסף קארו - כסף משנה - הלכות מלכים פרק א הלכה ד.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%A8%D7%91%D7%99%20%D7%99%D7%95%D7%A1%D7%A3%20%D7%A7%D7%90%D7%A8%D7%95%20-%20%D7%93%D7%A1%D7%A3%20%D7%9E%D7%50%D7%A0%D7%94%20-%20%D7%94%D7%94%D7%93%D7%95%D7%AA%20%D7%9E%D7%94%D7%93%D7%99%D7%95%20%D7%A4%D7%A8%D7%A7%20%D7%90%20%D7%94%D7%94%D7%93%D7%94%20%D7%93.md).

---

## 2. Full Sheet Verification (17/17)

| # | Canonical Title | Author | Status | Notes |
|---|---|---|---|---|
| 1 | `רשב''א - שו''ת הרשב''א חלק ז - סימן תקלג` | [[רשב''א]] | ✅ Verified | Clean 2-header layout |
| 2 | `מדרש רבה - בראשית רבה - פרשה סה` | [[מדרש רבה]] | ✅ Verified | Clean 2-header layout |
| 3 | `תלמוד בבלי - מסכת ברכות - דף י עמוד ב` | [[תלמוד בבלי]] | ✅ Preserved | **User study notes intact & preserved** |
| 4 | `מהרש''א - על ברכות - דף י עמוד ב` | [[מהרש''א]] | ✅ Verified | Clean 2-header layout |
| 5 | `תלמוד בבלי - מסכת סנהדרין - דף מו עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean DH anchor `#איבעיא להו` |
| 6 | `תלמוד בבלי - מסכת מועד קטן - דף כח עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean DH anchor `#תנו רבנן`; verified continuation crop `p2_cont` |
| 7 | `זוהר - מדרש הנעלם - פרשת בראשית מאמר חנוך בן ירד` | [[זוהר]] | 🔧 **Fixed** | Attributed to Zohar; book & location standardized |
| 8 | `חיד''א - חומת אנך על מלכים א - פרק יד` | [[חיד''א]] | 🔧 **Fixed** | Attributed to Chida; book & Tanach mapping standardized |
| 9 | `תלמוד בבלי - מסכת תענית - דף כ עמוד א` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout |
| 10 | `רד''ק - מלכים א - פרק יד פסוק כא` | [[רד''ק]] | ✅ Verified | Clean DH anchor `#ושם אמו נעמה העמונית` |
| 11 | `תלמוד בבלי - מסכת בבא קמא - דף לח עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean DH anchor `#ויאמר לו הקב"ה`; verified continuation crop `p3_cont` |
| 12 | `רבי יוסף קארו - כסף משנה - הלכות מלכים פרק א הלכה ד` | [[רבי יוסף קארו]] | ✅ Preserved | **User study notes intact & preserved** |
| 13 | `רבי יחזקאל לנדא - שו''ת נודע ביהודה מהדורה קמא - חו''מ - סימן א ד''ה אמנם להוציא` | [[רבי יחזקאל לנדא]] | ✅ Verified | Clean 2-header layout |
| 14 | `חיד''א - מדבר קדמות - מערכת נ אות כד` | [[חיד''א]] | 🔧 **Fixed** | Attributed to Chida; alphabetical ma'arechet mapped |
| 15 | `רבי שמריהו שולמן - אור לישרים - דף רטו` | [[רבי שמריהו שולמן]] | 🔧 **Fixed** | Attributed to Rav Shmaryahu Shulman; Daf folio normalized |
| 16 | `תלמוד בבלי - מסכת פסחים - דף פז עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout |
| 17 | `אבני נזר - שו''ת אבני נזר חלק יו''ד - סימן שיב ד''ה יח עוד` | [[אבני נזר]] | 🔧 **Fixed** | Standardized book to include responsa chelek |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Midrash HaNe'elam Mapping**:
   - Added `'מדרש הנעלם'` and `'ספר מדרש הנעלם'` to `RESPONSA_SPECIAL_MAP` mapped to `('זוהר', 'מדרש הנעלם')`.
   - Added canonical mappings for `מדרש הנעלם` to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.

2. **Chomat Anach Mapping**:
   - Added `'חומת אנך'` and `'ספר חומת אנך'` to `RESPONSA_SPECIAL_MAP` mapped to `("חיד''א", 'חומת אנך')`.
   - Added automatic Tanach book integration: `book = f"{resp_book} על {extra_clean}"` (e.g. `חומת אנך על מלכים א`).
   - Added canonical mappings for `חומת אנך` to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.

3. **Midbar K'deimot & `מערכת` Location Recognition**:
   - Added `'מדבר קדמות'` and `'ספר מדבר קדמות'` to `RESPONSA_SPECIAL_MAP` mapped to `("חיד''א", 'מדבר קדמות')`.
   - Added `|מערכת\s+[א-ת0-9\'׳]+|מערכת` to `loc_match` regex in both `RESPONSA_SPECIAL_MAP` and heuristic parser, ensuring alphabetical section indices (`מערכת נ אות כד`) parse cleanly as location.
   - Added canonical mappings to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.

4. **Ohr LiYesharim & Rav Shmaryahu Shulman Mapping**:
   - Added `'אור לישרים'` and `'ספר אור לישרים'` to `RESPONSA_SPECIAL_MAP` mapped to `('רבי שמריהו שולמן', 'אור לישרים')`.
   - Added canonical author mappings for `רבי שמריהו שולמן`, `שמריהו שולמן`, `שמריה שולמן`, `ר"ש שולמן`, `ר''ש שולמן`, and `אור לישרים` to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.
   - Ensured folio location normalization parses `ד׳ רטו` as `דף רטו`.

5. **Avnei Nezer Responsa & Chelek Extraction**:
   - Added `'אבני נזר'`, `'שו"ת אבני נזר'`, `"שו''ת אבני נזר"`, and `'ספר אבני נזר'` to `RESPONSA_SPECIAL_MAP` mapped to `('אבני נזר', 'שו"ת אבני נזר')`.
   - Implemented chelek extraction: detects leading `חלק (יו"ד|או"ח|חו"מ|אבהע"ז...)` and binds it into `book = f"{resp_book} {chelek}"` while preserving the remainder as location (`סימן שיב ד"ה יח עוד`).

6. **Hebrew Smichut Support for `פרשת` in Location Matching**:
   - Added `פרשת` alongside `פרשה` in `loc_match` regex (`|פרשה|פרשת|`), preventing construct forms (`פרשת בראשית`) from premature split.

7. **Chida Canonical Normalization**:
   - Corrected canonical mapping target for `חיד"א` and `החיד"א` in `AUTHOR_CANONICAL_MAP` from double-quote to canonical vault standard `"חיד''א"`.

8. **Flexible Location & D"H Stripping in `match_existing_source`**:
   - Enhanced `match_existing_source` to iterate through all possible split points between book and location (`split_idx in range(1, len(parts))`), accommodating dashes inside book titles or locations (e.g. `חו''מ - סימן א`).
   - Implemented `strip_dh` normalization (`re.sub(r'[\s\-_]*(?:ד["״\'׳]{1,2}ה|דיבור המתחיל)\s+.*$', '', t)`) so citations containing specific D"H variants match existing notes for the same Siman/Daf instead of creating redundant duplicate files.

---

## 4. Post-Audit Deduplication & Sheet Disambiguation

1. **Noda BiYehuda Consolidation**:
   - Merged duplicate note `333 Sources/רבי יחזקאל לנדא - שו''ת נודע ביהודה מהדורה קמא - חו''מ - סימן א ד''ה אמנם להוציא.md` into canonical note [`333 Sources/רבי יחזקאל לנדא - שו''ת נודע ביהודה מהדורה קמא - חו''מ - סימן א.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%A8%D7%91%D7%99%20%D7%99%D7%97%D7%96%D7%A7%D7%90%D7%94%20%D7%9C%D7%A0%D7%93%D7%90%20-%20%D7%A9%D7%95''%D7%AA%20%D7%A0%D7%95%D7%93%D7%A2%20%D7%91%D7%99%D7%94%D7%95%D7%93%D7%94%20%D7%9E%D7%94%D7%93%D7%95%D7%A8%D7%94%20%D7%A7%D7%9E%D7%90%20-%20%D7%97%D7%95''%D7%9E%20-%20%D7%A1%D7%99%D7%9E%D7%97%20%D7%90.md).
   - Preserved all user study notes from both sheets under dedicated headers:
     - `### ... - melachim 1.14`
     - `### ... - melachim 1.11`
   - Updated embeds in both [`111 Source Sheets/melachim 1.14.md`](file:///home/sean/Obsidian/Rapp/111%20Source%20Sheets/melachim%201.14.md) and [`111 Source Sheets/melachim 1.11.md`](file:///home/sean/Obsidian/Rapp/111%20Source%20Sheets/melachim%201.11.md).

2. **Kessef Mishneh Disambiguation**:
   - Disambiguated [`333 Sources/רבי יוסף קארו - כסף משנה - הלכות מלכים פרק א הלכה ד.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%A8%D7%91%D7%99%20%D7%99%D7%95%D7%A1%D7%A3%20%D7%A7%D7%90%D7%A8%D7%95%20-%20%D7%9B%D7%A1%D7%A4%20%D7%9E%D7%A9%D7%A0%D7%94%20-%20%D7%94%D7%94%D7%9B%D7%95%D7%AA%20%D7%9E%D7%94%D7%9B%D7%99%D7%95%20%D7%A4%D7%A8%D7%A7%20%D7%90%20%D7%94%D7%94%D7%9B%D7%94%20%D7%93.md) into sheet-specific sections (` - melachim 1.14` and ` - melachim 1.11`), preventing cross-sheet bleed.
   - Updated embeds in both master source sheets.

3. **Berachot 10b & Maharsha Disambiguation**:
   - Disambiguated `ברכות י עמוד ב` and `מהרש''א על ברכות י עמוד ב` with dedicated `- melachim 1.14` anchors.

4. **PDF Double #9 Clarification**:
   - Documented that page 2 of `000 Source PDFs/melachim 1.14.pdf` contains two sources numbered `(9` (Ta'anit 20a and Radak), resulting in 17 canonical sources on the sheet while the PDF's last printed number is `(16`.
