# Sin To Fix Source Sheet Audit

## Summary
Audited `111 Source Sheets/sin to fix.md` (`000 Source PDFs/sin to fix.pdf`, Subject: *Gemara*, Maseches Shabbos 3b-4a):
1. **PDF Pruning**: Verified that the incoming 63-page PDF was exactly 3 unique pages duplicated 21 times (100% verified textually and visually via SHA-256 pixel checksums). Pruned `000 Source PDFs/sin to fix.pdf` down to the 3 unique pages, and removed all duplicate image crops from `444 Attachments/` (`p4` through `p63`).
2. **Sheet & Source Audit (19 Sources)**: Verified every source on the sheet. Resolved 8 flagged/corrupt sources (**הגהות אשרי**, **תפארת שמואל**, **ביצחק יקרא**, **בית הבחירה למאירי**, **מגיד משנה**, **הגהות רעק"א**, **שו"ת משפט כהן**, **חשוקי חמד**), separated colliding footnotes in **פסקי תשובות** (notes 26 and 30), restored missing footnote number in **משנה ברורה מהדורת דרשו** (note 27), created canonical author profiles in `222 Authors/`, purged temporary fallback author notes, and verified link and crop integrity.
3. **User Note Protection**: Fully preserved all existing user study notes across the vault (including `שולחן ערוך - סימן קכד סעיף ב`, `מגן אברהם - סימן קכד ס''ק ג`, `משנה ברורה - סימן קכד`, etc.).
4. **Script Root-Cause Patches**: Patched `999 Scripts/process_source_sheets.py` with duplicate cycle detection, RTL number un-reversal in Davka decoding, `הערה` footnote preservation, and canonical responsa/author mapping.
5. **Result**: **0 audit warnings, 0 broken embeds, 0 missing images, 0 missing authors.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Duplicate PDF Cycles (63 Pages $\to$ 3 Pages)
- **Issue**: The incoming PDF contained 63 pages consisting of 3 unique pages repeated 21 times. The initial run generated 79 redundant source headings, phantom attachment crops (`sin to fix_p4_*` to `sin to fix_p63_*`), and repetitive `### (2)...(21)` headings.
- **Resolution**: Verified exact 21-fold repetition and pruned `000 Source PDFs/sin to fix.pdf` to the 3 canonical pages. Purged phantom crops `p4`–`p63` and regenerated clean modular source notes.

### 2. Source #3 (`הגהות אשרי מסכת שבת פרק א סימן ג`)
- **Issue**: Parsed as `Author: [[הגהות]]`, `Book: אשרי מסכת שבת`, flagged `audit_needed: true` (*"Author fell back to token 'הגהות'"*), generating corrupt author `222 Authors/הגהות.md`.
- **Resolution**: Attributed to canonical author **`[[רבי ישראל מקרעמז]]`** (Mahari Krems). Standardized note to **`רבי ישראל מקרעמז - הגהות אשר''י מסכת שבת - פרק א סימן ג.md`**, book `הגהות אשר''י מסכת שבת`, location `פרק א סימן ג`.
- **Author Note**: Created [`222 Authors/רבי ישראל מקרעמז.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%99%D7%A9%D7%A8%D7%90%D7%9C%20%D7%9E%D7%A7%D7%A8%D7%24%D7%9E%D7%96.md); purged fallback `222 Authors/הגהות.md`.

### 3. Source #4 (`תפארת שמואל מסכת שבת פרק א סימן ג ד"ה הגה"ה`)
- **Issue**: Parsed as `Author: [[תפארת]]`, `Book: שמואל מסכת שבת`, flagged `audit_needed: true` (*"Author fell back to token 'תפארת'"*), generating corrupt author `222 Authors/תפארת.md`.
- **Resolution**: Attributed to canonical author **`[[רבי אהרן שמואל קאיידנובר]]`** (Maharashak). Standardized note to **`רבי אהרן שמואל קאיידנובר - תפארת שמואל מסכת שבת - פרק א סימן ג ד''ה הגה''ה.md`**, book `תפארת שמואל מסכת שבת`, location `פרק א סימן ג ד''ה הגה''ה`.
- **Author Note**: Created [`222 Authors/רבי אהרן שמואל קאיידנובר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%90%D7%94%D7%A8%D7%9F%20%D7%A9%D7%9E%D7%55%D7%90%D7%9C%20%D7%A7%D7%90%D7%99%D7%99%D7%93%D7%A0%D7%55%D7%91%D7%A8.md); purged fallback `222 Authors/תפארת.md`.

### 4. Source #5 (`ביצחק יקרא שבת ד׳ ע"א`)
- **Issue**: Extracted with sefer name as author `[[ביצחק יקרא]]`, book `שבת`, location `ד׳ ע"א` which normalized awkwardly to `דף ע''א`.
- **Resolution**: Attributed to canonical author **`[[רבי אביגדור נבנצל]]`**. Standardized note to **`רבי אביגדור נבנצל - ביצחק יקרא מסכת שבת - דף ד עמוד א.md`**, book `ביצחק יקרא מסכת שבת`, location `דף ד עמוד א`.
- **Author Note**: Created [`222 Authors/רבי אביגדור נבנצל.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%90%D7%91%D7%99%D7%20%D7%A0%D7%91%D7%A0%D7%A6%D7%9C.md).

### 5. Source #6 (`בית הבחירה למאירי מסכת שבת דף ד עמוד א`)
- **Issue**: Parsed as `Author: [[בית]]`, `Book: הבחירה למאירי מסכת שבת`, flagged `audit_needed: true` (*"Author fell back to token 'בית'"*), generating corrupt author `222 Authors/בית.md`.
- **Resolution**: Attributed to canonical author moniker **`[[המאירי]]`**. Standardized note to **`המאירי - בית הבחירה מסכת שבת - דף ד עמוד א.md`**, book `בית הבחירה מסכת שבת`, location `דף ד עמוד א`.
- **Author Note**: Linked to existing [`222 Authors/המאירי.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%9E%D7%90%D7%99%D7%A8%D7%99.md); purged fallback `222 Authors/בית.md`.

### 6. Source #9 (`מגיד משנה הלכות שבת פרק ט הלכה ה`)
- **Issue**: Parsed as `Author: [[מגיד]]`, `Book: מקור`, location `משנה הלכות שבת...`, flagged `audit_needed: true` (*"Author fell back to token 'מגיד'"*), generating corrupt author `222 Authors/מגיד.md`.
- **Resolution**: Attributed to canonical author **`[[רבי וידאל די טולוזא]]`**. Standardized note to **`רבי וידאל די טולוזא - מגיד משנה הלכות שבת - פרק ט הלכה ה.md`**, book `מגיד משנה הלכות שבת`, location `פרק ט הלכה ה`.
- **Author Note**: Created [`222 Authors/רבי וידאל די טולוזא.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%95%D7%99%D7%93%D7%90%D7%9C%20%D7%93%D7%99%20%D7%98%D7%55%D7%9C%D7%55%D7%96%D7%90.md); purged fallback `222 Authors/מגיד.md`.

### 7. Source #10 (`ב"ח אורח חיים סימן רנד )ו(`)
- **Issue**: Token `ב"ח` fell back without canonical normalization, generating unnormalized author file.
- **Resolution**: Standardized author to canonical Nosei Keilim moniker **`[[ב''ח]]`** (matching `ט''ז` and `ש''ך`), standardized note to **`ב''ח - אורח חיים - סימן רנד.md`**, book `אורח חיים`, location `סימן רנד`.
- **Author Note**: Standardized [`222 Authors/ב''ח.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%91''%D7%97.md).

### 8. Source #14 (`הגהות רעק"א או"ח רנ"ד - ה׳`)
- **Issue**: Parsed as `Author: [[הגהות]]`, `Book: רעק''א או''ח רנ''ד - ה׳`, location empty, flagged `audit_needed: true` (*"Author fell back to token 'הגהות'"*).
- **Resolution**: Attributed to canonical author **`[[רבי עקיבא איגר]]`**. Standardized note to **`רבי עקיבא איגר - הגהות רבי עקיבא איגר - או''ח רנ''ד - ה׳.md`**, book `הגהות רבי עקיבא איגר`, location `או''ח רנ''ד - ה׳`.
- **Author Note**: Linked to existing canonical profile [`222 Authors/רבי עקיבא איגר.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%A2%D7%A7%D7%99%D7%91%D7%90%20%D7%90%D7%99%D7%22%D7%A8.md).

### 9. Source #15 (`שו"ת משפט כהן )ענייני ארץ ישראל( סימן לט`)
- **Issue**: Parsed as `Author: [[שו"ת משפט]]`, `Book: כהן`, flagged `audit_needed: true` (*"Author fell back to token 'שו\"ת משפט'"*), generating corrupt authors `222 Authors/משפט.md` and `222 Authors/שו''ת משפט.md`.
- **Resolution**: Attributed to canonical author **`[[הרב אברהם יצחק הכהן קוק]]`**. Standardized note to **`הרב אברהם יצחק הכהן קוק - שו''ת משפט כהן - סימן לט.md`**, book `שו''ת משפט כהן`, location `סימן לט`.
- **Author Note**: Linked to existing canonical profile [`222 Authors/הרב אברהם יצחק הכהן קוק.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%90%D7%91%D7%A8%D7%94%D7%9D%20%D7%99%D7%A6%D7%97%D7%A7%20%D7%94%D7%93%D7%94%D7%9F%20%D7%A7%D7%55%D7%A7.md); purged fallback author notes.

### 10. Sources #16 & #17 (`פסקי תשובות הערות סימן רנד הערה 26` & `הערה 30`)
- **Issue**: Numbers at the end of the line were reversed to `62` and `03` by font stream decoding, and then stripped by regex because `הערה` was not in the trailing number whitelist. Consequently, both footnotes collapsed into identical location `סימן רנד הערה`, merging into a single collided file with repetitive image crops.
- **Resolution**: Un-reversed digits in `decode_line`, whitelisted `הערה` in location regexes, and separated them into two distinct canonical source notes:
  - **`הרב שמחה רבינוביץ - פסקי תשובות - סימן רנד הערה 26.md`** (crop: `sin to fix_p3_s1.png`)
  - **`הרב שמחה רבינוביץ - פסקי תשובות - סימן רנד הערה 30.md`** (crop: `sin to fix_p3_s2.png`)

### 11. Source #18 (`חשוקי חמד מסכת שבת דף ד עמוד א`)
- **Issue**: Parsed as `Author: [[חשוקי]]`, `Book: חמד מסכת שבת`, flagged `audit_needed: true` (*"Author fell back to token 'חשוקי'"*), generating corrupt author `222 Authors/חשוקי.md`.
- **Resolution**: Attributed to canonical author **`[[הרב יצחק זילברשטיין]]`**. Standardized note to **`הרב יצחק זילברשטיין - חשוקי חמד מסכת שבת - דף ד עמוד א.md`**, book `חשוקי חמד מסכת שבת`, location `דף ד עמוד א`.
- **Author Note**: Created [`222 Authors/הרב יצחק זילברשטיין.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A8%D7%91%20%D7%99%D7%A6%D7%97%D7%A7%20%D7%96%D7%99%D7%9C%D7%91%D7%A8%D7%A9%D7%98%D7%99%D7%99%D7%9F.md); purged fallback `222 Authors/חשוקי.md`.

### 12. Source #19 (`משנה ברורה מהדורת דרשו ס׳ רנ"ד הע׳ 27`)
- **Issue**: Footnote number `27` was reversed to `72` and stripped by regex because `הע'` was not whitelisted, leaving location as truncated `ס׳ רנ''ד הע׳`.
- **Resolution**: Standardized to **`משנה ברורה - מהדורת דרשו - ס׳ רנ''ד הע׳ 27.md`**, book `מהדורת דרשו`, location `ס׳ רנ''ד הע׳ 27`.

---

## 2. Full Sheet Verification (19/19)

| # | Canonical Title | Author | Status | Notes |
|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת שבת - דף ג עמוד ב ''תפשוט דרב ביבי בר אביי'' עד דף ד עמוד א ''קודם` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout |
| 2 | `תוספות - מסכת שבת - דף ג עמוד ב ד''ה ואיבעית אימא` | [[תוספות]] | ✅ Verified | Dibur Hamatchil anchor verified |
| 3 | `רבי ישראל מקרעמז - הגהות אשר''י מסכת שבת - פרק א סימן ג` | [[רבי ישראל מקרעמז]] | 🔧 **Fixed** | Canonical author profile created; audit flag cleared |
| 4 | `רבי אהרן שמואל קאיידנובר - תפארת שמואל מסכת שבת - פרק א סימן ג ד''ה הגה''ה` | [[רבי אהרן שמואל קאיידנובר]] | 🔧 **Fixed** | Canonical author profile created; audit flag cleared |
| 5 | `רבי אביגדור נבנצל - ביצחק יקרא מסכת שבת - דף ד עמוד א` | [[רבי אביגדור נבנצל]] | 🔧 **Fixed** | Author & Daf normalized to `דף ד עמוד א`; audit cleared |
| 6 | `המאירי - בית הבחירה מסכת שבת - דף ד עמוד א` | [[המאירי]] | 🔧 **Fixed** | Attributed to Meiri; fallback purged; audit cleared |
| 7 | `רמב''ם - הלכות שבת - פרק ט הלכה ה` | [[רמב''ם]] | ✅ Verified | Clean 2-header layout |
| 8 | `רבי יעקב בן אשר - טור אורח חיים הלכות שבת - סימן רנד` | [[רבי יעקב בן אשר]] | ✅ Verified | Clean 2-header layout |
| 9 | `רבי וידאל די טולוזא - מגיד משנה הלכות שבת - פרק ט הלכה ה` | [[רבי וידאל די טולוזא]] | 🔧 **Fixed** | Attributed to Rav Vidal; book `מקור` bug resolved |
| 10 | `ב''ח - אורח חיים - סימן רנד` | [[ב''ח]] | 🔧 **Fixed** | Canonical acronym profile created; audit cleared |
| 11 | `שולחן ערוך - אורח חיים - סימן רנד סעיף ו` | [[שולחן ערוך]] | ✅ Verified | Clean 2-header layout |
| 12 | `משנה ברורה - סימן רנד ס''ק לט` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil anchor verified |
| 13 | `מגן אברהם - אורח חיים - סימן רנד ס''ק כב` | [[מגן אברהם]] | ✅ Verified | Clean 2-header layout |
| 14 | `רבי עקיבא איגר - הגהות רבי עקיבא איגר - או''ח רנ''ד - ה׳` | [[רבי עקיבא איגר]] | 🔧 **Fixed** | Attributed to R' Akiva Eiger; audit flag cleared |
| 15 | `הרב אברהם יצחק הכהן קוק - שו''ת משפט כהן - סימן לט` | [[הרב אברהם יצחק הכהן קוק]] | 🔧 **Fixed** | Attributed to Rav Kook; fallbacks purged; audit cleared |
| 16 | `הרב שמחה רבינוביץ - פסקי תשובות - סימן רנד הערה 26` | [[הרב שמחה רבינוביץ]] | 🔧 **Fixed** | Disambiguated footnote 26 from 30; crops separated |
| 17 | `הרב שמחה רבינוביץ - פסקי תשובות - סימן רנד הערה 30` | [[הרב שמחה רבינוביץ]] | 🔧 **Fixed** | Disambiguated footnote 30 from 26; crops separated |
| 18 | `הרב יצחק זילברשטיין - חשוקי חמד מסכת שבת - דף ד עמוד א` | [[הרב יצחק זילברשטיין]] | 🔧 **Fixed** | Attributed to Rav Zilberstein; audit flag cleared |
| 19 | `משנה ברורה - מהדורת דרשו - ס׳ רנ''ד הע׳ 27` | [[משנה ברורה]] | 🔧 **Fixed** | Footnote number 27 restored from Davka font reversal |

---

## 3. Script Root-Cause Fixes in `process_source_sheets.py`

1. **Automatic Duplicate Page Cycle Detection**:
   - Added automated multi-page repetition cycle detection before page iteration. Detects repeated page cycles (such as 3 pages duplicated 21 times) and restricts processing to the base unique sequence, preventing vault bloat.
2. **Davka RTL Digit Reversal**:
   - In `decode_line`, `rev = line[::-1]` reversed multi-digit numbers (e.g. `26` became `62`, `30` became `03`, `27` became `72`). Added `re.sub(r'\d+', lambda m: m.group(0)[::-1], decoded)` to un-reverse contiguous digits back to original order.
3. **Footnote Number Whitelisting**:
   - Updated trailing number whitelists in lines 663 and 1112 to include `הערה` and `הע['׳]`, preventing footnote numbers from being stripped.
4. **Responsa & Author Canonical Mappings**:
   - Added mappings to `RESPONSA_SPECIAL_MAP` and `AUTHOR_CANONICAL_MAP` for:
     - `הגהות אשרי` / `הגהות אשר"י` $\to$ `רבי ישראל מקרעמז`
     - `תפארת שמואל` $\to$ `רבי אהרן שמואל קאיידנובר`
     - `ביצחק יקרא` $\to$ `רבי אביגדור נבנצל`
     - `בית הבחירה למאירי` / `בית הבחירה` $\to$ `המאירי`
     - `מגיד משנה` $\to$ `רבי וידאל די טולוזא`
     - `ב"ח` / `ב''ח` $\to$ `ב''ח`
     - `הגהות רעק"א` $\to$ `רבי עקיבא איגר`
     - `משפט כהן` / `שו"ת משפט כהן` $\to$ `הרב אברהם יצחק הכהן קוק`
     - `חשוקי חמד` $\to$ `הרב יצחק זילברשטיין`
5. **Daf Normalization**:
   - Added regex to normalize `ד׳ ע"א` to `דף ד עמוד א`.
