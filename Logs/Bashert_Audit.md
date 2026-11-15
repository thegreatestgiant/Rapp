# Bashert Source Sheet Audit

## Summary
Audited `111 Source Sheets/bashert.md` (`000 Source PDFs/bashert.pdf`, Subject: *Machshava*, Fall 2026 Midterm).
Updated to reflect the **new 4-page version** of `bashert.pdf` which expands the sheet from 17 to **18 sources**, inserting **הרב בן ציון פירר** (*Panim Chadashot BaTorah*, Parashat Chayei Sarah) as Source #16.

All 18 sources have been reconciled without side effects:
- Prevented/purged corrupt fallback author note `222 Authors/פנים.md`.
- Created canonical author profile [`222 Authors/הרב בן ציון פירר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%91%D7%9F%20%D7%A6%D7%99%D7%95%D7%9F%20%D7%A4%D7%99%D7%A8%D7%A8.md).
- Created canonical source note [`333 Sources/הרב בן ציון פירר - פנים חדשות בתורה - פ׳ חיי שרה ס׳ ה׳.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%94%D7%A8%D7%91%20%D7%91%D7%9F%20%D7%A6%D7%99%D7%95%D7%9F%20%D7%A4%D7%99%D7%A8%D7%A8%20-%20%D7%A4%D7%A0%D7%99%D7%9D%20%D7%97%D7%93%D7%A9%D7%95%D7%AA%20%D7%91%D7%AA%D7%95%D7%A8%D7%94%20-%20%D7%A4%D7%A8%D7%A9%D7%AA%20%D7%97%D7%99%D7%99%20%D7%A9%D7%A8%D7%94%20%D7%A1%D7%99%D7%9E%D7%9F%20%D7%94.md), migrating all existing user study notes.
- Re-cropped all page images cleanly (`bashert_p1_s1..s7`, `bashert_p2_cont`, `bashert_p2_s1..s5`, `bashert_p3_cont`, `bashert_p3_s1..s4`, `bashert_p4_cont`, `bashert_p4_s1..s2`), resolving all shifted/broken images.
- Purged orphaned `bashert_p1_s8.png`.
- Removed duplicate empty headings in existing source files, preserving all user study notes.
- Updated `process_source_sheets.py` parser with canonical mappings for *Panim Chadashot BaTorah* and parsha location regex.
- Result: **0 audit flags, 0 broken embeds, 0 missing/broken images, 0 lost study notes.**

---

## 1. Revision Details (18 Sources)

| # | Canonical Title | Author | Status | Notes & Images |
|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת מועד קטן - דף יח עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | `bashert_p1_s1.png` |
| 2 | `תוספות - מסכת סנהדרין - דף כב עמוד א` | [[תוספות]] | ✅ Verified | `bashert_p1_s2.png` |
| 3 | `ריטב''א - חידושי הריטב''א מסכת מועד קטן - דף יח עמוד ב` | [[ריטב''א]] | ✅ Verified | `bashert_p1_s3.png` |
| 4 | `ר''ן - חדושי הר''ן על מועד קטן - דף יח עמוד ב` | [[ר''ן]] | ✅ Verified | `bashert_p1_s4.png` |
| 5 | `רבי יהודה החסיד - ספר חסידים - סימן שפג` | [[רבי יהודה החסיד]] | ✅ Verified | `bashert_p1_s5.png` |
| 6 | `תלמוד בבלי - מסכת סוטה - דף ב עמוד א` | [[תלמוד בבלי]] | ✅ Verified | `bashert_p1_s6.png` |
| 7 | `תלמוד בבלי - מסכת גיטין - דף צ עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | `bashert_p1_s7.png`, `bashert_p2_cont.png` |
| 8 | `תלמוד בבלי - מסכת סנהדרין - דף כב עמוד א` | [[תלמוד בבלי]] | ✅ Verified | `bashert_p2_s1.png` (entirely on p2) |
| 9 | `ר''ן - חדושי הר''ן על סנהדרין - דף כב עמוד א` | [[ר''ן]] | ✅ Verified | `bashert_p2_s2.png` |
| 10 | `רש''י - מסכת סוטה - דף ב עמוד א` | [[רש''י]] | ✅ Verified | `bashert_p2_s3.png` |
| 11 | `רא''ש - תוספות הרא''ש מסכת סוטה - דף ב עמוד א` | [[רא''ש]] | ✅ Verified | `bashert_p2_s4.png` |
| 12 | `המאירי - על מסכת סוטה - דף ב עמוד א` | [[המאירי]] | ✅ Verified | `bashert_p2_s5.png`, `bashert_p3_cont.png` |
| 13 | `רמב''ם - שו''ת הרמב''ם - סימן תלו` | [[רמב''ם]] | ✅ Verified | `bashert_p3_s1.png` (entirely on p3) |
| 14 | `רבי שמעון בן צמח דוראן - שו''ת תשב''ץ - חלק ב סימן א` | [[רבי שמעון בן צמח דוראן]] | ✅ Verified | `bashert_p3_s2.png` |
| 15 | `חיד''א - פתח עינים מסכת סנהדרין - דף כב עמוד א` | [[חיד''א]] | ✅ Verified | `bashert_p3_s3.png` |
| 16 | `הרב בן ציון פירר - פנים חדשות בתורה - פ׳ חיי שרה ס׳ ה׳` | [[הרב בן ציון פירר]] | 🆕 **Added** | `bashert_p3_s4.png`, `bashert_p4_cont.png`; user notes preserved |
| 17 | `הרב חיים גרוס - נעימת החיים - ד׳ ט''ז` | [[הרב חיים גרוס]] | ✅ Verified | `bashert_p4_s1.png` (shifted from p3) |
| 18 | `הרב יצחק יוסף - ילקוט יוסף - שובע שמחות א - ד׳ כ''א השתדלות בעניני שידוכין` | [[הרב יצחק יוסף]] | ✅ Verified | `bashert_p4_s2.png` (shifted from p3) |

---

## 2. Parser Enhancements (`999 Scripts/process_source_sheets.py`)
1. **Panim Chadashot BaTorah**: Added `'פנים חדשות בתורה'` and `'ספר פנים חדשות בתורה'` mapped to canonical author `[[הרב בן ציון פירר]]`.
2. **Author Blacklist**: Added `'פנים'` and `'חדשות'` to blacklist to prevent fallback author generation.
3. **Parsha Regex**: Enhanced location parser to support `פ׳ <Parsha>` citations.
