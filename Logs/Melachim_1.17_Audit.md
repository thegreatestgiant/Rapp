# Melachim 1.17 Source Sheet Audit

## Summary
Audited `111 Source Sheets/melachim 1.17.md` (`000 Source PDFs/melachim 1.17.pdf`, Subject: *Navi*, Fall 2026 Final) — 22 embedded sources across 3 pages. Verified every citation against the decoded Davka font text stream and PDF layout, resolved all flagged and malformed sources (**עקידת יצחק / רבי יצחק עראמה**, **ילקוט ראובני**, **ילקוט שמעוני**, **תוספות הרא''ש מסכת בבא מציעא**, and **שו''ת רדב''ז חלק ו**), created canonical author profile in `222 Authors/` (**ילקוט ראובני**), enriched **רבי יצחק עראמה** with aliases and scholarly background, purged corrupt fallback author profiles (`222 Authors/ספר עקידת.md`, `222 Authors/ילקוט.md`), reordered image attachments chronologically in shared multi-quote notes, and patched all parser root causes in `999 Scripts/process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #12 (`ספר עקידת יצחק - שער כב:`)
- **Issue**: Unmapped philosophical/homiletical classic caused parser to fall back to token `author: "[[ספר עקידת]]"`, `book: "יצחק - שער כב"`, generated corrupt fallback `222 Authors/ספר עקידת.md`, and flagged the source `audit_needed: true` (*"Author fell back to token 'ספר עקידת'"*).
- **Resolution**: Identified work as *Akeidat Yitzchak* by Rabbi Yitzchak Arama (matching existing note `333 Sources/רבי יצחק עראמה - עקידת יצחק - שער לא.md`). Standardized note to **`333 Sources/רבי יצחק עראמה - עקידת יצחק - שער כב.md`**, attributed to canonical author **`[[רבי יצחק עראמה]]`**, book `עקידת יצחק`, location `שער כב`. Cleared audit flag, removed `⚠️ (Needs Audit)` badge from the master sheet, and purged corrupt fallback files.
- **Author Note**: Enriched [`222 Authors/רבי יצחק עראמה.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%99%D7%A6%D7%97%D7%Aaction%20%D7%A2%D7%A8%D7%90%D7%9E%D7%94.md) with aliases `[רבי יצחק עראמה, יצחק עראמה, עקידת יצחק, בעל העקידה, Arama, Isaac Arama, Akedat Yitzchak, Akeidat Yitzchak]` and scholarly background.
- **Root Cause Patch**: Added `ספר עקידת יצחק`, `עקידת יצחק`, and `עקדת יצחק` to `KNOWN_AUTHORS`, `AUTHOR_CANONICAL_MAP`, and `RESPONSA_SPECIAL_MAP` mapped to `('רבי יצחק עראמה', 'עקידת יצחק')`. Added section handling in `process_source_sheets.py` to extract gate/sha'ar locations cleanly.

### 2. Source #15 (`ילקוט ראובני שמות בא`)
- **Issue**: Unmapped anthological Kabbalistic/Midrashic commentary caused parser to fall back to single token `author: "[[ילקוט]]"`, `book: "ראובני שמות בא"`, generated corrupt fallback `222 Authors/ילקוט.md`, and flagged the source `audit_needed: true` (*"Author fell back to token 'ילקוט'"*).
- **Resolution**: Identified work as *Yalkut Reuveni* on Chumash Shemot, Parashat Bo (`ויאמרו עבדי פרעה עד מתי`). Standardized note to **`333 Sources/ילקוט ראובני - שמות - פרשת בא.md`**, attributed to canonical author **`[[ילקוט ראובני]]`**, book `שמות`, location `פרשת בא`. Cleared audit flag, removed `⚠️ (Needs Audit)` badge from the master sheet, and purged corrupt fallback files.
- **Author Note**: Created canonical author profile [`222 Authors/ילקוט ראובני.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%99%D7%9C%D7%A7%D7%95%D7%98%20%D7%A8%D7%90%D7%95%D7%91%D7%A0%D7%99.md) with aliases `[ילקוט ראובני, ראובני, רבי ראובן הושקה, רבי ראובן בן הושקע סופר, רבי ראובן כ"ץ, Yalkut Reuveni, Reuveni]` and historical overview of Rabbi Reuven ben Hoshke Sofer of Prague.
- **Root Cause Patch**: Added `ילקוט ראובני` and `ספר ילקוט ראובני` to `KNOWN_AUTHORS`, `AUTHOR_CANONICAL_MAP`, and `RESPONSA_SPECIAL_MAP`. Added Chumash extraction and Parsha normalization logic in `process_source_sheets.py`.

### 3. Source #14 (`ילקוט שמעוני מלכים א רמז רח`)
- **Issue**: The PDF header omitted a hyphen between the book name and Remez citation (`ילקוט שמעוני מלכים א רמז רח`). Because `רמז` was missing from `loc_match` regex, the parser failed to split the tractate/book from the Remez number, resulting in `book: "מלכים א רמז רח"`, `location: ""`, and file `ילקוט שמעוני - מלכים א רמז רח.md`.
- **Resolution**: Standardized note to **`333 Sources/ילקוט שמעוני - מלכים א - רמז רח.md`**, set `book: "מלכים א"`, `location: "רמז רח"`, updated headline anchor to `### ילקוט שמעוני - מלכים א - רמז רח`, updated master sheet embed, and deleted old unhyphenated note.
- **Root Cause Patch**: Added `רמז\s+[א-ת0-9\'׳]+|רמז` to `loc_match` regex in `process_source_sheets.py`, mapped `ילקוט שמעוני` in `RESPONSA_SPECIAL_MAP`, and ensured book/remez partitioning when hyphens are omitted.

### 4. Source #20 (`תוספות הרא"ש על מסכת בבא מציעא דף קיד/ב`)
- **Issue**: Overly broad `בבא\s+[א-ת]+` pattern in `loc_match` regex mistakenly matched the tractate name `בבא מציעא` as a location token rather than part of the book title. In addition, regex `re.sub(r'^(?:על\s+)?(?:מסכת\s+)?', ...)` failed when `extra_clean` had no trailing space, resulting in duplicated `book: "תוספות הרא''ש מסכת מסכת"` and `location: "בבא מציעא דף קיד עמוד ב"`.
- **Resolution**: Standardized note to **`333 Sources/רא''ש - תוספות הרא''ש מסכת בבא מציעא - דף קיד עמוד ב.md`**, attributed to canonical author **`[[רא''ש]]`**, book `תוספות הרא''ש מסכת בבא מציעא`, location `דף קיד עמוד ב`, with clean headline `### לאו כהן ניהו מר`. Updated master sheet embed and deleted duplicated filename.
- **Root Cause Patch**: Constrained `בבא` matching in `loc_match` to internal Mishnah clauses (`בבא\s+(?:קמייתא|מציעתא|בתרייתא|דרישא|דסיפא)`), preventing Shas tractates (`בבא מציעא`, `בבא קמא`, `בבא בתרא`) from being hijacked as location tokens. Updated Maseches regex in `תוספות הרא"ש` handler to `(?:מסכת\s*)?`.

### 5. Source #22 (`שו"ת רדב"ז חלק ו סימן ב אלפים רג`)
- **Issue**: `שו"ת רדב"ז` was mapped in `AUTHOR_CANONICAL_MAP` but absent from `RESPONSA_SPECIAL_MAP` chelek handling, causing the volume specification `חלק ו` to be stripped of its responsa prefix and leaving `book: "חלק ו"`, diverging from standard vault convention (e.g. `רדב''ז - שו''ת רדב''ז חלק ג - סימן תרלד.md`).
- **Resolution**: Standardized note to **`333 Sources/רדב''ז - שו''ת רדב''ז חלק ו - סימן ב אלפים רג.md`**, attributed to canonical author **`[[רדב''ז]]`**, book `שו''ת רדב''ז חלק ו`, location `סימן ב אלפים רג`. Updated master sheet embed and deleted legacy file.
- **Root Cause Patch**: Added `שו"ת רדב"ז`, `שו''ת רדב''ז`, `רדב"ז`, and `ספר רדב"ז` to `RESPONSA_SPECIAL_MAP` and enabled automatic `חלק` volume extraction into `resp_book`.

### 6. Chronological Image Ordering (Sources #1, #6, #13, #16, #18, #19)
- **Issue**: In shared notes containing multiple quotes from the same daf/perakim, newly extracted crops were prepended out of order (e.g. page 3 crops appearing above page 1 crops).
- **Resolution**: Reordered attachment blocks into strict chronological order:
  - `333 Sources/תלמוד בבלי - מסכת סנהדרין - דף קיג עמוד א.md`: `melachim 1.16_p2_s9.png` (#1.16), then `melachim 1.17_p1_s1.png` (#1), then `melachim 1.17_p3_s2.png` (#18), while fully preserving user study note under `### תניא`.
  - `333 Sources/תוספות - מסכת בבא מציעא - דף קיד עמוד ב.md`: `melachim 1.17_p1_s6.png` (#6), then `melachim 1.17_p3_s3.png` (#19).
  - `333 Sources/פרקי דרבי אליעזר - חורב - פרק לב.md`: `melachim 1.17_p2_s4.png` (#13), then `melachim 1.17_p2_s7.png` (#16).

---

## 2. Complete Sheet Verification (22/22)

| # | Canonical Title | Canonical Author | Status | Notes |
|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת סנהדרין - דף קיג עמוד א` | [[תלמוד בבלי]] | ✅ Verified | Clean DH `#אחאב שושביניה הוה' אתא`; image order verified |
| 2 | `תלמוד בבלי - מסכת תענית - דף ב עמוד א` | [[תלמוד בבלי]] | ✅ Verified | Clean DH `#אמר רבי יוחנן` |
| 3 | `תוספות - מסכת תענית - דף ב עמוד א` | [[תוספות]] | ✅ Verified | Clean 2-header layout |
| 4 | `מדרש רבה - בראשית רבה - פרשה עא ט` | [[מדרש רבה]] | ✅ Verified | Clean 2-header layout |
| 5 | `תלמוד בבלי - מסכת בבא מציעא - דף קיד עמוד א וב` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout |
| 6 | `תוספות - מסכת בבא מציעא - דף קיד עמוד ב` | [[תוספות]] | ✅ Verified | Clean DH `#נמצא בתשובת גאון שכתב`; image order verified |
| 7 | `רש''י - בראשית - פרק ח פסוק ז` | [[רש''י]] | ✅ Verified | Clean DH `#עד יבשת המים` |
| 8 | `תלמוד בבלי - מסכת חולין - דף ה עמוד א` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout |
| 9 | `רש''י - מסכת חולין - דף ה עמוד א` | [[רש''י]] | ✅ Verified | Clean DH `#על פי הדבור שאני` |
| 10 | `ריטב''א - חידושי הריטב''א מסכת חולין - דף ה עמוד א` | [[ריטב''א]] | ✅ Verified | Clean DH `#על פי הדיבור שאני` |
| 11 | `מדרש רבה - במדבר רבה - פרשה כג` | [[מדרש רבה]] | ✅ Verified | Preserved existing Melachim 1 study notes; DH `#מדרש רבה - במדבר רבה - פרשה כג ד''ה ט כי אתם` |
| 12 | `רבי יצחק עראמה - עקידת יצחק - שער כב` | [[רבי יצחק עראמה]] | 🔧 **Fixed** | Attributed to Rav Yitzchak Arama; cleared fallback `ספר עקידת`; purged corrupt author file |
| 13 | `פרקי דרבי אליעזר - חורב - פרק לב` | [[פרקי דרבי אליעזר]] | ✅ Verified | Clean DH `#אליהו התשבי שהלך לו`; image order verified |
| 14 | `ילקוט שמעוני - מלכים א - רמז רח` | [[ילקוט שמעוני]] | 🔧 **Fixed** | Separated book `מלכים א` from location `רמז רח` with canonical hyphenation |
| 15 | `ילקוט ראובני - שמות - פרשת בא` | [[ילקוט ראובני]] | 🔧 **Fixed** | Attributed to Yalkut Reuveni on Shemot; created canonical author file; purged fallback `ילקוט` |
| 16 | `פרקי דרבי אליעזר - חורב - פרק לב` | [[פרקי דרבי אליעזר]] | ✅ Verified | Clean DH `#לאחר ימים חלה בן` |
| 17 | `רמב''ם - הלכות איסורי ביאה - פרק כב הלכה טז` | [[רמב''ם]] | ✅ Verified | Clean 2-header layout |
| 18 | `תלמוד בבלי - מסכת סנהדרין - דף קיג עמוד א` | [[תלמוד בבלי]] | ✅ Verified | Clean DH `#ויהי מקץ ימים וייבש` |
| 19 | `תוספות - מסכת בבא מציעא - דף קיד עמוד ב` | [[תוספות]] | ✅ Verified | Clean DH `#אמר ליה לאו כהן` |
| 20 | `רא''ש - תוספות הרא''ש מסכת בבא מציעא - דף קיד עמוד ב` | [[רא''ש]] | 🔧 **Fixed** | Resolved `מסכת מסכת` duplication and extracted Maseches `בבא מציעא` out of location token |
| 21 | `רבנו בחיי - במדבר - פרק כה פסוק יא` | [[רבנו בחיי]] | ✅ Verified | Clean 2-header layout |
| 22 | `רדב''ז - שו''ת רדב''ז חלק ו - סימן ב אלפים רג` | [[רדב''ז]] | 🔧 **Fixed** | Standardized book to `שו''ת רדב''ז חלק ו` and location to `סימן ב אלפים רג` |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Akeidat Yitzchak Recognition**:
   - Added `'ספר עקידת יצחק'`, `'עקידת יצחק'`, and `'עקדת יצחק'` to `KNOWN_AUTHORS`, `AUTHOR_CANONICAL_MAP`, and `RESPONSA_SPECIAL_MAP` mapped to `('רבי יצחק עראמה', 'עקידת יצחק')`.
   - Added gate parsing in `RESPONSA_SPECIAL_MAP` to cleanly isolate gate/sha'ar locations (`שער כב`).

2. **Yalkut Reuveni Recognition**:
   - Added `'ילקוט ראובני'` and `'ספר ילקוט ראובני'` to `KNOWN_AUTHORS`, `AUTHOR_CANONICAL_MAP`, and `RESPONSA_SPECIAL_MAP`.
   - Added Chumash detection (`בראשית`, `שמות`, `ויקרא`, `במדבר`, `דברים`) and Parsha prefix normalization so citations like `ילקוט ראובני שמות בא` correctly partition into `book: "שמות"`, `location: "פרשת בא"`.

3. **Yalkut Shimoni Remez & Unhyphenated Header Support**:
   - Added `רמז\s+[א-ת0-9\'׳]+|רמז` to `loc_match` regex in `process_source_sheets.py`.
   - Added `'ילקוט שמעוני'` and `'ספר ילקוט שמעוני'` to `RESPONSA_SPECIAL_MAP`, enabling automatic separation of the Tanach book from the Remez number even when the sheet header omits hyphens.

4. **Tosafot HaRosh Shas Tractate Disambiguation**:
   - Replaced greedy `בבא\s+[א-ת]+` in `loc_match` with specific Mishnah clause regex `בבא\s+(?:קמייתא|מציעתא|בתרייתא|דרישא|דסיפא)`. This prevents tractates such as `בבא מציעא`, `בבא קמא`, and `בבא בתרא` from being falsely captured as location strings.
   - Refined `maseches` cleanup in `תוספות הרא"ש` handler to `re.sub(r'^(?:על\s+)?(?:מסכת\s*)?', '', extra_clean).strip()`, eliminating `מסכת מסכת` duplications.

5. **Responsa Radbaz Chelek Volume Extraction**:
   - Added `'שו"ת רדב"ז'`, `"שו''ת רדב''ז"`, `'רדב"ז'`, and `'ספר רדב"ז'` to `RESPONSA_SPECIAL_MAP` mapped to `('רדב"ז', "שו''ת רדב''ז")`.
   - Included Radbaz in `m_chelek` volume extraction logic, ensuring `חלק [א-ת0-9]+` attaches to the book title (`שו''ת רדב''ז חלק ו`).
