# Ger Toshav Source Sheet Audit

## Summary
Audited `111 Source Sheets/ger toshav.md` (`000 Source PDFs/ger toshav.pdf`, Subject: *Gemara*, Fall 2026 Final) — 20 embedded sources across 3 pages. Verified every citation against the decoded Davka font text stream and PDF layout, resolved all flagged and malformed sources (**ספר חמדת ישראל / רבי מאיר דן פלאצקי** and **ספרי דברים פרשת כי תצא**), created canonical author profile in `222 Authors/` (**רבי מאיר דן פלאצקי**), purged corrupt fallback author profile (`222 Authors/ספר חמדת.md`), verified continuation crop `ger toshav_p3_cont.png`, and patched all parser root causes in `999 Scripts/process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #20 (`ספר חמדת ישראל ח"א )הג"ר מאיר דן פלאצקי( קונטרס נר מצוה אות ל"ה`)
- **Issue**: Unmapped Polish halakhic classic caused parser to fall back to token `author: "[[ספר חמדת]]"`, `book: "ישראל"`, generated corrupt fallback `222 Authors/ספר חמדת.md`, and flagged the source `audit_needed: true` (*"Author fell back to token 'ספר חמדת'"*).
- **Resolution**: Identified work as *Chemdat Yisrael* by the renowned posek and Rosh Yeshiva Rabbi Meir Dan Plotzky of Dvohrt and Ostrów Mazowiecka (author of *Kli Chemda*), specifically Part 1, *Kuntres Ner Mitzvah*, Ot 35 (expounding on the laws and acceptance of Ger Toshav). Standardized note to **`333 Sources/רבי מאיר דן פלאצקי - חמדת ישראל - ח''א קונטרס נר מצוה אות ל''ה.md`**, attributed to canonical author **`[[רבי מאיר דן פלאצקי]]`**, book `חמדת ישראל`, location `ח''א קונטרס נר מצוה אות ל''ה`. Cleared audit flag, removed `⚠️ (Needs Audit)` badge from the master sheet, and purged corrupt fallback files.
- **Author Note**: Created canonical author profile [`222 Authors/רבי מאיר דן פלאצקי.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%9E%D7%90%D7%99%D7%A8%20%D7%93%D7%9F%20%D7%A4%D7%9C%D7%90%D7%A6%D7%A7%D7%99.md) with aliases `[רבי מאיר דן פלאצקי, מאיר דן פלאצקי, חמדת ישראל, בעל חמדת ישראל, כלי חמדה, בעל כלי חמדה, Meir Dan Plotzky, Plotzky]` and scholarly background.
- **Root Cause Patch**: Added `חמדת ישראל`, `ספר חמדת ישראל`, `רבי מאיר דן פלאצקי`, `כלי חמדה`, and `ספר כלי חמדה` to `KNOWN_AUTHORS`, `AUTHOR_CANONICAL_MAP`, and `RESPONSA_SPECIAL_MAP` mapped to `('רבי מאיר דן פלאצקי', 'חמדת ישראל')`. Added `קונטרס\s+[א-ת0-9\'״]+|קונטרס|` to `loc_match` regex.

### 2. Source #11 (`ספרי דברים פרשת כי תצא רנט`)
- **Issue**: Missing `פרשת` in general parser `loc_match` regex caused the location to fail detection, leaving `location: ""` and allowing `book` to swallow the entire string (`book: "דברים פרשת כי תצא רנט"`), resulting in an unhyphenated filename (`333 Sources/ספרי - דברים פרשת כי תצא רנט.md`).
- **Resolution**: Standardized note to **`333 Sources/ספרי - דברים - פרשת כי תצא רנט.md`**, attributed to canonical author **`[[ספרי]]`**, book `דברים`, location `פרשת כי תצא רנט`, headline `### ספרי - דברים - פרשת כי תצא רנט`. Updated master sheet embed and deleted unhyphenated legacy note.
- **Root Cause Patch**: Added `ספרי` and `ספר ספרי` to `RESPONSA_SPECIAL_MAP`, enabled Chumash parsing (`דברים`, `במדבר`, `זוטא`) to automatically partition book and Parsha/Piska, and added `פרשת` to `loc_match` regex across the engine.

### 3. Source #14 Multi-Page Continuation Verification (`שו"ת הרשב"א חלק א סימן קפב`)
- **Verification**: Source 14 began at the bottom of Page 2 (`ger toshav_p2_s7.png`) and completed at the top of Page 3 (`ger toshav_p3_cont.png`). Verified both screenshot crops are cleanly attached inside `333 Sources/רשב''א - שו''ת הרשב''א חלק א - סימן קפב.md` and display seamlessly without header bleed.

---

## 2. Complete Sheet Verification (20/20)

| # | Canonical Title | Canonical Author | Status | Notes |
|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת עבודה זרה - דף סד עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean DH `#מיתיבי` |
| 2 | `רמב''ם - הלכות מלכים - פרק ח הלכה י - יא` | [[רמב''ם]] | ✅ Verified | Clean 2-header layout |
| 3 | `שולחן ערוך - יורה דעה - סימן קכד סעיף ב` | [[שולחן ערוך]] | ✅ Verified | Clean 2-header layout |
| 4 | `רמב''ם - הלכות איסורי ביאה - פרק יד הלכה ז` | [[רמב''ם]] | ✅ Verified | Clean 2-header layout |
| 5 | `רמב''ם - הלכות עבודה זרה - פרק י הלכה ו` | [[רמב''ם]] | ✅ Verified | Clean 2-header layout |
| 6 | `רמב''ם - הלכות מאכלות אסורות - פרק יא הלכה ז` | [[רמב''ם]] | ✅ Verified | Clean 2-header layout |
| 7 | `רבי יעקב בן אשר - חושן משפט - סימן רמט` | [[רבי יעקב בן אשר]] | ✅ Verified | Tur Choshen Mishpat standard layout |
| 8 | `בית יוסף - חושן משפט - סימן רמט` | [[בית יוסף]] | ✅ Verified | Clean 2-header layout |
| 9 | `ב''ח - חושן משפט - סימן רמט` | [[ב''ח]] | ✅ Verified | Clean 2-header layout |
| 10 | `תנ''ך - דברים - פרק כג פסוק טז - יז` | [[תנ''ך]] | ✅ Verified | Clean Tanach 2-header layout |
| 11 | `ספרי - דברים - פרשת כי תצא רנט` | [[ספרי]] | 🔧 **Fixed** | Partitioned book `דברים` and location `פרשת כי תצא רנט` with canonical hyphenation |
| 12 | `רמב''ן - השגות לספר המצוות - לרמב''ם שכחת העשין מצוה טז` | [[רמב''ן]] | ✅ Verified | Clean 2-header layout |
| 13 | `תלמוד בבלי - מסכת ערכין - דף כט עמוד א` | [[תלמוד בבלי]] | ✅ Verified | Clean DH `#מיתיבי` |
| 14 | `רשב''א - שו''ת הרשב''א חלק א - סימן קפב` | [[רשב''א]] | ✅ Verified | Verified multi-page continuation crop `ger toshav_p3_cont.png` |
| 15 | `רבי יוסף קארו - כסף משנה - הלכות עבודה זרה פרק י הלכה ו` | [[רבי יוסף קארו]] | ✅ Verified | Clean 2-header layout |
| 16 | `רבי יוסף באבד - מנחת חינוך - פרשת אם כסף מצוה צג אות א` | [[רבי יוסף באבד]] | ✅ Verified | Clean 2-header layout |
| 17 | `שולחן ערוך - אורח חיים - סימן שד סעיף ג` | [[שולחן ערוך]] | ✅ Verified | Clean 2-header layout |
| 18 | `משנה ברורה - סימן שד ס''ק כד` | [[משנה ברורה]] | ✅ Verified | Clean DH `#א"י גמור` |
| 19 | `משנה ברורה - שער הציון - סימן שד ס''ק כ` | [[משנה ברורה]] | ✅ Verified | Clean 2-header layout |
| 20 | `רבי מאיר דן פלאצקי - חמדת ישראל - ח''א קונטרס נר מצוה אות ל''ה` | [[רבי מאיר דן פלאצקי]] | 🔧 **Fixed** | Attributed to Rav Meir Dan Plotzky; created canonical author file; purged fallback `ספר חמדת` |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Chemdat Yisrael / Kli Chemda Recognition**:
   - Added `'חמדת ישראל'`, `'ספר חמדת ישראל'`, `'רבי מאיר דן פלאצקי'`, `'כלי חמדה'`, and `'ספר כלי חמדה'` to `KNOWN_AUTHORS`, `AUTHOR_CANONICAL_MAP`, and `RESPONSA_SPECIAL_MAP` mapped to `('רבי מאיר דן פלאצקי', 'חמדת ישראל')`.
   - Added `קונטרס\s+[א-ת0-9\'״]+|קונטרס|` to `loc_match` regex, enabling automatic detection of treatises like *Kuntres Ner Mitzvah*.

2. **Sifrei Halakhic Midrash Parsing**:
   - Added `'ספרי'` and `'ספר ספרי'` to `RESPONSA_SPECIAL_MAP` and `AUTHOR_CANONICAL_MAP`.
   - Added Chumash detection (`דברים`, `במדבר`, `זוטא`) so that candidate citations automatically separate the biblical book from the Parsha and Piska.
   - Added `פרשת` to both `loc_match` regex patterns in `process_source_sheets.py`.
