# Planting Source Sheet Audit

## Summary
Audited `111 Source Sheets/planting.md` (`000 Source PDFs/planting.pdf`, Subject: *Gemara*, Fall 2026 Midterm) — 10 sources across 3 pages focusing on *Melechet Zorei'a* (מלאכת זורע) on Shabbat, analyzing the core mechanism of whether the biblical prohibition takes effect immediately at planting (*she'at ma'aseh*) or depends on subsequent rooting (*hashrasha*), in comparison with *Hilchot Kilayim*, *Omer*, *Terumot*, and modern fertility/medical ethics.

Resolved author fallback anomalies, multi-word and responsa sefer title misattributions, and broken sheet embeds. Created 2 new canonical author profiles in `222 Authors/`, purged 4 corrupt fallback author profiles, corrected misattributed *Yabia Omer* metadata, verified all 12 image attachments (including multi-part and page continuation crops), and patched root-cause parsing logic in `999 Scripts/process_source_sheets.py`.

**Result**: 0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files, and strictly 10 verified canonical sources.

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #5 (`שו"ת דבר אברהם חלק א - סימן כג`)
- **Issue**: Listed on master sheet as `## 5 ⚠️ (Needs Audit)` with broken link `![[שו''ת דבר - אברהם חלק א - סימן כג#...]]`. The file had previously been created under the canonical title `333 Sources/רבי אברהם דובער כהנא שפירא - שו''ת דבר אברהם חלק א - סימן כג.md`, but the embed on `planting.md` pointed to a non-existent fallback filename, generating fallback author `222 Authors/שו''ת דבר.md`.
- **Resolution**: Updated embed on [`111 Source Sheets/planting.md`](file:///home/sean/Obsidian/Rapp/111%20Source%20Sheets/planting.md) to **[`333 Sources/רבי אברהם דובער כהנא שפירא - שו''ת דבר אברהם חלק א - סימן כג.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%A8%D7%91%D7%99%20%D7%90%D7%91%D7%A8%D7%94%D7%9D%20%D7%93%D7%95%D7%91%D7%A2%D7%55%20%D7%9B%D7%94%D7%A0%D7%90%20%D7%A9%D7%A4%D7%99%D7%A8%D7%90%20-%20%D7%A1%D7%95''%D7%AA%20%D7%93%D7%91%D7%55%20%D7%90%D7%91%D7%A8%D7%94%D7%9D%20%D7%97%D7%94%D7%A7%20%D7%90%20-%20%D7%A1%D7%99%D7%9E%D7%9F%20%D7%9B%D7%92.md)**; mapped to canonical author profile **`[[רבי אברהם דובער כהנא שפירא]]`** (Rabbi Avraham DovBer Kahana Shapiro, Kovno Rav), Book: `שו''ת דבר אברהם חלק א`, Location: `סימן כג`. Purged corrupt fallback `222 Authors/שו''ת דבר.md`.

### 2. Source #6 (`אגלי טל זורע ביאורים ח (א)`)
- **Issue**: Listed on master sheet as `## 6 ⚠️ (Needs Audit)` with broken link `![[אגלי - טל זורע ביאורים ח#...]]`. The file had previously been created under the canonical title `333 Sources/אבני נזר - אגלי טל - זורע ביאורים ח (א).md`, but the embed on `planting.md` pointed to a non-existent fallback filename, generating fallback author `222 Authors/אגלי.md`.
- **Resolution**: Updated embed on [`111 Source Sheets/planting.md`](file:///home/sean/Obsidian/Rapp/111%20Source%20Sheets/planting.md) to **[`333 Sources/אבני נזר - אגלי טל - זורע ביאורים ח (א).md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%90%D7%91%D7%A0%D7%99%20%D7%A0%D7%96%D7%A8%20-%20%D7%90%D7%92%D7%94%D7%99%20%D7%98%D7%94%20-%20%D7%96%D7%95%D7%55%D7%A2%20%D7%91%D7%99%D7%90%D7%95%D7%55%D7%99%D7%9D%20%D7%97%20(%D7%90).md)**; mapped to canonical author **`[[אבני נזר]]`** (Rabbi Avraham Bornsztein of Sochatchov), Book: `אגלי טל`, Location: `זורע ביאורים ח (א)`. Purged corrupt fallback `222 Authors/אגלי.md`.

### 3. Source #7 (`שו"ת יביע אומר חלק ד - אורח חיים סימן לה`)
- **Issue**: Note was created under corrupted title `333 Sources/יביע - אומר חלק ד - אורח חיים - סימן לה.md` with `author: "[[יביע]]"`, `book: "אומר חלק ד - אורח חיים"`, completely missing attribution to Rav Ovadia Yosef.
- **Resolution**: Replaced with canonical note **[`333 Sources/רב עובדיה יוסף - שו''ת יביע אומר - חלק ד או''ח סימן לה.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%A8%D7%91%20%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%94%20%D7%99%D7%95%D7%A1%D7%A3%20-%20%D7%A1%D7%95''%D7%AA%20%D7%99%D7%91%D7%99%D7%A2%20%D7%90%D7%95%D7%9E%D7%A8%20-%20%D7%97%D7%94%D7%A7%20%D7%93%20%D7%90%D7%95''%D7%97%20%D7%A1%D7%99%D7%9E%D7%9F%20%D7%94%D7%94.md)**; mapped to canonical author **`[[רב עובדיה יוסף]]`**, Book: `שו''ת יביע אומר`, Location: `חלק ד או''ח סימן לה`. Preserved both image attachments (`planting_p1_s7.png` and continuation `planting_p2_cont.png`). Updated embed on master sheet.

### 4. Source #8 (`תיבת משה מלאכת זורע`)
- **Issue**: `תיבת משה` fell back to first token `author: "[[תיבת]]"`, leaving book as `משה מלאכת זורע`, location empty, active audit flag `audit_needed: true` (*"Author fell back to token 'תיבת'"*), and corrupt fallback author `222 Authors/תיבת.md`.
- **Resolution**: Renamed note to **[`333 Sources/תיבת משה - מלאכת זורע.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%AA%D7%99%D7%91%D7%AA%20%D7%9E%D7%A9%D7%94%20-%20%D7%9E%D7%94%D7%90%D7%9B%D7%AA%20%D7%96%D7%95%D7%55%D7%A2.md)**; attributed to canonical author **`[[תיבת משה]]`**, Book: `תיבת משה`, Location: `מלאכת זורע`. Preserved both image attachments (`planting_p2_s1.png` and continuation `planting_p3_cont.png`). Updated embed on master sheet.
- **Author Note**: Created [`222 Authors/תיבת משה.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%AA%D7%99%D7%91%D7%AA%20%D7%9E%D7%A9%D7%94.md) with context and aliases; purged fallback `222 Authors/תיבת.md`.

### 5. Source #10 (`שו"ת שמע שלמה ח"ח אה"ע ס׳ ט`)
- **Issue**: Unmapped in `RESPONSA_SPECIAL_MAP`, causing author to fall back to `author: "[[שו''ת שמע]]"`, book `שלמה ח''ח אה''ע`, location `ס׳ ט`, active audit flag `audit_needed: true` (*"Author fell back to token 'שו\"ת שמע'"*), and corrupt fallback author `222 Authors/שו''ת שמע.md`.
- **Resolution**: Renamed note to **[`333 Sources/הרב שלמה משה עמאר - שו''ת שמע שלמה - ח''ח אה''ע ס׳ ט.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%94%D7%A8%D7%91%20%D7%A9%D7%94%D7%9E%D7%94%20%D7%9E%D7%A9%D7%94%20%D7%A2%D7%9E%D7%90%D7%55%20-%20%D7%A1%D7%95''%D7%AA%20%D7%A9%D7%9E%D7%A2%20%D7%A9%D7%94%D7%9E%D7%94%20-%20%D7%97''%D7%97%20%D7%90%D7%94''%D7%A2%20%D7%A1%D7%B3%20%D7%98.md)**; attributed to canonical author **`[[הרב שלמה משה עמאר]]`** (Rishon LeZion Rav Shlomo Amar, discussing Rav Shlomo Zalman Auerbach's position in Source #9), Book: `שו''ת שמע שלמה`, Location: `ח''ח אה''ע ס׳ ט`. Preserved image attachment `planting_p3_s2.png`. Updated embed on master sheet.
- **Author Note**: Created [`222 Authors/הרב שלמה משה עמאר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%A9%D7%94%D7%9E%D7%94%20%D7%9E%D7%A9%D7%94%20%D7%A2%D7%9E%D7%90%D7%55.md) with biography and aliases; purged fallback `222 Authors/שו''ת שמע.md`.

---

## 2. Complete Roster of 10 Verified Sources

| # | Embed on Sheet (`111 Source Sheets/planting.md`) | Canonical Author (`222 Authors/`) | Book | Location / Anchor |
|---|---|---|---|---|
| **1** | `![[תלמוד בבלי - מסכת שבת - דף ג עמוד ב ''אמר אביי- פשיטא לי'' עד ''לא קנסו שוגג אטו מזי#תלמוד בבלי - מסכת שבת - דף ג עמוד ב ''אמר אביי- פשיטא לי'' עד ''לא קנסו שוגג אטו מזי]]` | `[[תלמוד בבלי]]` | מסכת שבת | דף ג עמוד ב ''אמר אביי- פשיטא לי'' עד ''לא קנסו שוגג אטו מזי |
| **2** | `![[רש''ש - מסכת שבת - דף עג עמוד א#רש''ש - מסכת שבת - דף עג עמוד א]]` | `[[רש''ש]]` | מסכת שבת | דף עג עמוד א |
| **3** | `![[רבי יעקב חגיז - שו''ת הלכות קטנות חלק ב - סימן לו#רבי יעקב חגיז - שו''ת הלכות קטנות חלק ב - סימן לו]]` | `[[רבי יעקב חגיז]]` | שו''ת הלכות קטנות חלק ב | סימן לו |
| **4** | `![[מנחת חינוך - פרשת אמור מצוה רצח - אות ח#מנחת חינוך - פרשת אמור מצוה רצח - אות ח]]` | `[[מנחת חינוך]]` | פרשת אמור מצוה רצח | אות ח |
| **5** | `![[רבי אברהם דובער כהנא שפירא - שו''ת דבר אברהם חלק א - סימן כג#רבי אברהם דובער כהנא שפירא - שו''ת דבר אברהם חלק א - סימן כג]]` | `[[רבי אברהם דובער כהנא שפירא]]` | שו''ת דבר אברהם חלק א | סימן כג |
| **6** | `![[אבני נזר - אגלי טל - זורע ביאורים ח (א)#אבני נזר - אגלי טל - זורע ביאורים ח (א)]]` | `[[אבני נזר]]` | אגלי טל | זורע ביאורים ח (א) |
| **7** | `![[רב עובדיה יוסף - שו''ת יביע אומר - חלק ד או''ח סימן לה#רב עובדיה יוסף - שו''ת יביע אומר - חלק ד או''ח סימן לה]]` | `[[רב עובדיה יוסף]]` | שו''ת יביע אומר | חלק ד או''ח סימן לה (כולל המשך עמוד 2) |
| **8** | `![[תיבת משה - מלאכת זורע#תיבת משה - מלאכת זורע]]` | `[[תיבת משה]]` | תיבת משה | מלאכת זורע (כולל המשך עמוד 3) |
| **9** | `![[רבי שלמה זלמן אויערבאך - שו''ת מנחת שלמה תניינא - סימן קכד#רבי שלמה זלמן אויערבאך - שו''ת מנחת שלמה תניינא - סימן קכד]]` | `[[רבי שלמה זלמן אויערבאך]]` | שו''ת מנחת שלמה תניינא | סימן קכד |
| **10** | `![[הרב שלמה משה עמאר - שו''ת שמע שלמה - ח''ח אה''ע ס׳ ט#הרב שלמה משה עמאר - שו''ת שמע שלמה - ח''ח אה''ע ס׳ ט]]` | `[[הרב שלמה משה עמאר]]` | שו''ת שמע שלמה | ח''ח אה''ע ס׳ ט |

---

## 3. Parser Root-Cause Fixes in `process_source_sheets.py`

1. **Responsa & Rabbinic Works Canonical Mapping (`RESPONSA_SPECIAL_MAP`)**:
   - Added mappings for:
     - `דבר אברהם`: `('רבי אברהם דובער כהנא שפירא', 'שו"ת דבר אברהם')`
     - `אגלי טל`: `('אבני נזר', 'אגלי טל')`
     - `שמע שלמה`: `('הרב שלמה משה עמאר', 'שו"ת שמע שלמה')`
     - `תיבת משה`: `('תיבת משה', 'תיבת משה')`

2. **Author Canonical Dictionary (`AUTHOR_CANONICAL_MAP` & `get_all_known_authors`)**:
   - Registered canonical mappings for:
     - `דבר אברהם`, `שו"ת דבר אברהם` -> `רבי אברהם דובער כהנא שפירא`
     - `אגלי טל` -> `אבני נזר`
     - `שמע שלמה`, `שו"ת שמע שלמה`, `שלמה משה עמאר`, `הרב שלמה משה עמאר` -> `הרב שלמה משה עמאר`
     - `תיבת משה` -> `תיבת משה`
   - Added `'שו"ת דבר'`, `"שו''ת דבר"`, `'שו"ת שמע'`, `"שו''ת שמע"`, `'תיבת'`, `'אגלי'` to the forbidden author filter set `bad` in `get_all_known_authors()` to ensure partial title prefixes never generate fallback author profiles.
