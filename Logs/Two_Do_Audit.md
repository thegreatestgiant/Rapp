# Two Do (שנים שעשאוה) Source Sheet Audit

## Summary
Audited the `two do.md` master source sheet (`000 Source PDFs/two do.pdf`, Subject: *Gemara*, Fall 2026 Midterm, topic: *Shnayim She'asuha* / שנים שעשאוה במלאכת שבת). Successfully audited and standardized all 6 canonical sources, resolved 3 `⚠️ (Needs Audit)` flags, re-attributed fallback authors to their canonical Torah personalities, cleaned up 3 corrupt fallback author profiles, and created 3 enriched canonical author files with full aliases and background information.

---

## Sources Audited & Standardized (`111 Source Sheets/two do.md`)

| # | Canonical Title | Author | Book | Location | Status |
|---|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת שבת - דף ג עמוד א ''שניהן פטורין- והא'' עד ''שנים שעשאוה פטורין-''` | [[תלמוד בבלי]] | מסכת שבת | דף ג עמוד א | Verified |
| 2 | `תלמוד בבלי - מסכת שבת - דף צב עמוד ב` | [[תלמוד בבלי]] | מסכת שבת | דף צב עמוד ב (D"H: המוציא ככר לרשות הרבים) | Verified |
| 3 | `רמב''ם - הלכות שבת - פרק א הלכה טו` | [[רמב''ם]] | הלכות שבת | פרק א הלכה טו | Verified |
| 4 | `רב יעקב בצלאל זולטי - משנת יעב''ץ - או''ח ס׳ ל''ט` | [[רב יעקב בצלאל זולטי]] | משנת יעב"ץ | או"ח ס׳ ל"ט | Re-attributed & Cleaned |
| 5 | `רבי שמואל רוזובסקי - קונטרסי שעורים - בבא קמא שעור יג אות יב` | [[רבי שמואל רוזובסקי]] | קונטרסי שעורים | בבא קמא שעור יג אות יב | Re-attributed & Continuation Verified |
| 6 | `מכון הלכה ברורה - בירור הלכה - סימן שז סעיף לח - לט` | [[מכון הלכה ברורה]] | בירור הלכה | סימן שז סעיף לח - לט | Re-attributed & Cleaned |

---

## Root Causes & Enhancements

1. **Token Fallback on Renowned Sefer Titles**:
   - `משנת יעב"ץ`: Previously split as token author `משנת` and book `יעב''ץ או''ח`. Mapped canonically to **רב יעקב בצלאל זולטי** (Chief Rabbi of Jerusalem, member of the Supreme Rabbinical Court), author of *Mishnas Yaavetz*.
   - `קונטרסי שעורים`: Previously stripped parenthetical `(ר"ש רוזובסקי)` and fell back to token `קונטרסי`. Mapped canonically to **רבי שמואל רוזובסקי** (legendary Rosh Yeshiva of Ponevezh), author of *Kuntresei Shiurim*.
   - `הלכה ברורה בירור הלכה`: Previously fell back to token `הלכה`. Mapped canonically to **מכון הלכה ברורה** (Torah research institute founded upon the vision of Maran HaRav Avraham Yitzchak HaKohen Kook and Rav Tzvi Yehuda Kook), book *Birur Halacha*.

2. **Parser Upgrades (`999 Scripts/process_source_sheets.py`)**:
   - Integrated `משנת יעבץ`, `משנת יעב"ץ`, `קונטרסי שעורים`, `בירור הלכה`, and `הלכה ברורה בירור הלכה` into `RESPONSA_SPECIAL_MAP` and `AUTHOR_CANONICAL_MAP`.
   - Enhanced location regex to recognize Masechta keywords (e.g. `בבא קמא`) and siman indicators (e.g. `או"ח ס׳ ל"ט`).

3. **Vault Cleanup**:
   - **Deleted Junk Authors**: Removed `222 Authors/משנת.md`, `222 Authors/קונטרסי.md`, and `222 Authors/הלכה.md`.
   - **Created Canonical Authors**:
     - [`רב יעקב בצלאל זולטי.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%20%D7%99%D7%A2%D7%A7%D7%91%20%D7%91%D7%A6%D7%9C%D7%90%D7%9C%20%D7%96%D7%95%D7%9C%D7%98%D7%99.md)
     - [`רבי שמואל רוזובסקי.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%A9%D7%9E%D7%95%D7%90%D7%9C%20%D7%A8%D7%95%D7%96%D7%95%D7%91%D7%A1%D7%A7%D7%99.md)
     - [`מכון הלכה ברורה.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%9E%D7%9B%D7%95%D7%9F%20%D7%94%D7%9C%D7%9B%D7%94%20%D7%91%D7%A8%D7%95%D7%A8%D7%94.md)
