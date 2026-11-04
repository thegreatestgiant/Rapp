# Melachim 1.12 Source Sheet Audit

## Summary
Audited `111 Source Sheets/melachim 1.12.md` (`000 Source PDFs/melachim 1.12.pdf`, Subject: *Navi*, Fall 2026 Midterm) — 15 embedded sources. Verified every citation against the decoded Davka font text stream and PDF layout, resolved all 2 flagged/corrupt sources (**יד רמה** and **ספר בני יששכר**), corrected book title and author attributions for **יערות דבש** and **מנחת חינוך**, created canonical author profiles in `222 Authors/` (**רמ''ה**, **רבי צבי אלימלך מדינוב**), purged corrupt fallback author profiles, preserved user study notes under Sanhedrin 102a and Sanhedrin 101b, verified multi-page continuation crop `melachim 1.12_p2_cont.png`, and patched root causes in `process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #8 (`ספר מנחת חינוך - מצוה קז - אות ח`)
- **Issue**: Extracted with author `author='מנחת חינוך'` and book `book='חינוך - מצוה קז'` due to truncated dictionary key `'ספר מנחת'`, separating the sefer from its canonical posek.
- **Resolution**: Attributed to canonical author **`[[רבי יוסף באבד]]`** (linking to existing [`222 Authors/רבי יוסף באבד.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%99%D7%95%D7%A1%D7%A3%20%D7%91%D7%90%D7%91%D7%93.md)). Standardized note to **`רבי יוסף באבד - מנחת חינוך - מצוה קז - אות ח.md`**, book `מנחת חינוך`, location `מצוה קז - אות ח`.

### 2. Source #12 (`יד רמה על סנהדרין דף קב עמוד א`)
- **Issue**: Extracted as `author='יד'`, `book='רמה על סנהדרין'`, and flagged `audit_needed: true` (*"Author fell back to token 'יד'"*), generating corrupt fallback author `222 Authors/יד.md`.
- **Resolution**: Attributed to canonical author **`[[רמ''ה]]`** (Rabbi Meir ben Todros HaLevi Abulafia). Standardized note to **`רמ''ה - יד רמה על סנהדרין - דף קב עמוד א.md`**, book `יד רמה על סנהדרין`, location `דף קב עמוד א`.
- **Author Note**: Created [`222 Authors/רמ''ה.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%9E''%D7%94.md) with biography and comprehensive aliases; purged fallback `222 Authors/יד.md`.

### 3. Source #13 (`ספר יערות דבש - חלק שני - דרוש יב`)
- **Issue**: Truncated key `'ספר יערות'` in `AUTHOR_CANONICAL_MAP` caused book title to be extracted as `דבש - חלק שני - דרוש יב` instead of `יערות דבש`.
- **Resolution**: Standardized note to **`רבי יהונתן אייבשיץ - יערות דבש - חלק שני - דרוש יב.md`**, book `יערות דבש`, location `חלק שני - דרוש יב`.

### 4. Source #14 (`ספר בני יששכר - מאמרי חדש מרחשון - מאמר א`)
- **Issue**: Extracted as `author='ספר בני'`, `book='יששכר'`, and flagged `audit_needed: true` (*"Author fell back to token 'ספר בני'"*), generating corrupt fallback author `222 Authors/ספר בני.md`.
- **Resolution**: Attributed to canonical author **`[[רבי צבי אלימלך מדינוב]]`** (the Bnei Yissaschar). Standardized note to **`רבי צבי אלימלך מדינוב - בני יששכר - מאמרי חדש מרחשון - מאמר א.md`**, book `בני יששכר`, location `מאמרי חדש מרחשון - מאמר א`.
- **Author Note**: Created [`222 Authors/רבי צבי אלימלך מדינוב.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%20%D7%A6%D7%91%D7%99%20%D7%90%D7%9C%D7%99%D7%9E%D7%9C%D7%9A%20%D7%9E%D7%93%D7%99%D7%A0%D7%95%D7%91.md) with biography and aliases; purged fallback `222 Authors/ספר בני.md`.

### 5. Multi-Source Preservations (Sanhedrin 102a & Sanhedrin 101b)
- **Sanhedrin 102a (Source #1)**: Preserved all existing user study annotations intact in [`333 Sources/תלמוד בבלי - מסכת סנהדרין - דף קב עמוד א.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%AA%D7%94%D7%9E%D7%95%D7%93%20%D7%91%D7%91%D7%94%D7%99%20-%20%D7%9E%D7%A1%D7%93%D7%AA%20%D7%A1%D7%A0%D7%94%D7%93%D7%A8%D7%99%D7%9F%20-%20%D7%93%D7%A3%20%D7%A7%D7%91%20%D7%A2%D7%9E%D7%95%D7%93%20%D7%90.md).
- **Sanhedrin 101b (Sources #9 & #11)**: Preserved existing study notes under `### תנו רבנן` and `### אמר רבי יוחנן` from Melachim 1.11, while cleanly anchoring Melachim 1.12 excerpts under `### אמר רב נחמן` (Source #9) and `### מאי ויועץ? אמר רבי יהודה` (Source #11).
- **Ramban Shemot (Source #10)**: Preserved continuation crop `melachim 1.12_p2_cont.png` alongside `melachim 1.12_p1_s10.png` under `### Source Image`.

---

## 2. Full Sheet Verification (15/15)

| # | Canonical Title | Author | Status | Notes |
|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת סנהדרין - דף קב עמוד א` | [[תלמוד בבלי]] | ✅ Preserved | **User study notes intact & preserved** |
| 2 | `רש''י - דברי הימים ב - פרק י פסוק ג` | [[רש''י]] | ✅ Verified | Clean DH anchor `#וישלחו ויקראו לו ויבא` |
| 3 | `ר''ן - חדושי הר''ן על סנהדרין - דף כא עמוד ב` | [[ר''ן]] | ✅ Verified | Clean 2-header layout |
| 4 | `רמב''ם - ספר המצוות - מצות לא תעשה שסה` | [[רמב''ם]] | ✅ Verified | Clean 2-header layout |
| 5 | `תלמוד בבלי - מסכת הוריות - דף י עמוד א וב` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout |
| 6 | `תלמוד בבלי - מסכת מגילה - דף לא עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean DH anchor `#ויתניא' רבי שמעון בן אלעזר אומר` |
| 7 | `ספרי - זוטא - פיסקא יב` | [[ספרי]] | ✅ Verified | Clean 2-header layout |
| 8 | `רבי יוסף באבד - מנחת חינוך - מצוה קז - אות ח` | [[רבי יוסף באבד]] | 🔧 **Fixed** | Attributed to author Rav Yosef Babad; sefer title restored |
| 9 | `תלמוד בבלי - מסכת סנהדרין - דף קא עמוד ב` | [[תלמוד בבלי]] | ✅ Preserved | Multi-DH anchor `#אמר רב נחמן`; previous notes intact |
| 10 | `רמב''ן - שמות - פרק לב פסוק כה` | [[רמב''ן]] | ✅ Verified | Continuation crop `p2_cont` verified |
| 11 | `תלמוד בבלי - מסכת סנהדרין - דף קא עמוד ב` | [[תלמוד בבלי]] | ✅ Preserved | Multi-DH anchor `#מאי ויועץ? אמר רבי יהודה` |
| 12 | `רמ''ה - יד רמה על סנהדרין - דף קב עמוד א` | [[רמ''ה]] | 🔧 **Fixed** | Attributed to Ramah; author profile created in `222 Authors/` |
| 13 | `רבי יהונתן אייבשיץ - יערות דבש - חלק שני - דרוש יב` | [[רבי יהונתן אייבשיץ]] | 🔧 **Fixed** | Fixed sefer title truncation from `דבש` to `יערות דבש` |
| 14 | `רבי צבי אלימלך מדינוב - בני יששכר - מאמרי חדש מרחשון - מאמר א` | [[רבי צבי אלימלך מדינוב]] | 🔧 **Fixed** | Attributed to Bnei Yissaschar; author profile created |
| 15 | `מדרש רבה - במדבר רבה - פרשה כא` | [[מדרש רבה]] | ✅ Verified | Clean 2-header layout |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Yad Ramah Mapping**:
   - Added `יד רמה` to `RESPONSA_SPECIAL_MAP` mapped to `("רמ''ה", 'יד רמה')`.
   - Added canonical mappings for `רמ"ה`, `רמ''ה`, `הרמ"ה`, `הרמ''ה`, `רבי מאיר הלוי אבולעפיה`, and `יד רמה` to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.
   - Extracted tractate and folio (`על סנהדרין דף קב עמוד א`) cleanly into book and location.

2. **Bnei Yissaschar Mapping**:
   - Added `בני יששכר` and `ספר בני יששכר` to `RESPONSA_SPECIAL_MAP` mapped to `('רבי צבי אלימלך מדינוב', 'בני יששכר')`.
   - Added mappings to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.

3. **Ya'arot Devash Sefer Title Repair**:
   - Replaced truncated prefix `'ספר יערות'` in `AUTHOR_CANONICAL_MAP` with full title `'ספר יערות דבש'` and `'יערות דבש'` mapped to `'רבי יהונתן אייבשיץ'`.
   - Added `יערות דבש` and `ספר יערות דבש` to `RESPONSA_SPECIAL_MAP`.

4. **Minchat Chinuch Author & Sefer Attribution**:
   - Replaced truncated key `'ספר מנחת'` in `AUTHOR_CANONICAL_MAP` with `'ספר מנחת חינוך'` and `'מנחת חינוך'` mapped to canonical author `'רבי יוסף באבד'`.
   - Added `מנחת חינוך` to `RESPONSA_SPECIAL_MAP` so `מנחת חינוך` is correctly assigned as book and `רבי יוסף באבד` as author.
