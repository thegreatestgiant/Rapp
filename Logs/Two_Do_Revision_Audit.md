# Two Do (שנים שעשאוה) Source Sheet Revision Audit

## Summary
Reconciled and audited the updated revision of `two do.md` (`000 Source PDFs/two do.pdf`, received as `two do (1).pdf`).
- Consolidated incoming PDF from `two do (1).pdf` into the canonical `two do.pdf` (deleting the duplicate).
- Expanded sheet from 6 sources to 11 sources.
- **Zero user note loss**: 100% of study notes across existing sources (Shabbat 3a, Shabbat 92b, Rambam 1:15) preserved intact.
- Re-attributed *Kuntresei Shiurim* to **רבי ישראל זאב גוסטמן** per the Rebbi's explicit citation `(רי"ז גוסטמן)`.
- Created author profiles for [`פני יהושע.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A4%D7%A0%D7%99%20%D7%99%D7%94%D7%95%D7%A9%D7%A2.md) and [`רבי ישראל זאב גוסטמן.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%99%D7%A9%D7%A8%D7%90%D7%9C%20%D7%96%D7%90%D7%91%20%D7%92%D7%95%D7%A1%D7%98%D7%9E%D7%9F.md).
- Patched root cause in `999 Scripts/process_source_sheets.py` (`is_line_english()` QWERTY punctuation handling and canonical author mappings).

---

## Shiur Prep Brief (Revision Comparison)

| Old # | New # | Source Title | Author | Status / Change |
| :---: | :---: | :--- | :--- | :--- |
| 1 | 1 | `תלמוד בבלי - מסכת שבת - דף ג עמוד א ''שניהן פטורין- והא'' עד ''שנים שעשאוה פטורין-''` | [[תלמוד בבלי]] | ⚪ Unchanged (User notes preserved) |
| 2 | 2 | `תלמוד בבלי - מסכת שבת - דף צב עמוד ב` | [[תלמוד בבלי]] | ⚪ Unchanged (User notes preserved) |
| 3 | 3 | `רמב''ם - הלכות שבת - פרק א הלכה טו` | [[רמב''ם]] | ⚪ Unchanged (User notes preserved) |
| — | 4 | `פני יהושע - מסכת שבת - דף צג עמוד א` | [[פני יהושע]] | 🟢 **New Source to learn** |
| — | 5 | `ריטב''א - מסכת קידושין - דף מג עמוד א` | [[ריטב''א]] | 🟢 **New Source to learn** |
| 4 | 6 | `רב יעקב בצלאל זולטי - משנת יעב''ץ - או''ח ס׳ ל''ט` | [[רב יעקב בצלאל זולטי]] | 🔄 Shifted (was #4) |
| 5 | 7 | `רבי ישראל זאב גוסטמן - קונטרסי שעורים - בבא קמא שעור יג אות יב` | [[רבי ישראל זאב גוסטמן]] | 🔄 Shifted & Re-attributed to Rav Gustman per Rebbi's revision |
| 6 | 8 | `מכון הלכה ברורה - בירור הלכה - סימן שז סעיף לח - לט` | [[מכון הלכה ברורה]] | 🔄 Shifted (was #6) |
| — | 9 | `רמ''א - שו''ת הרמ''א - סימן עו` | [[רמ''א]] | 🟢 **New Source to learn** |
| — | 10 | `ט''ז - אורח חיים - סימן שכה ס''ק א` | [[ט''ז]] | 🟢 **New Source to learn** |
| — | 11 | `מגן אברהם - אורח חיים - סימן שמח ס''ק ד` | [[מגן אברהם]] | 🟢 **New Source to learn** |
