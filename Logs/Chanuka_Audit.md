# Chanuka Source Sheet Audit

## Summary
Audited `111 Source Sheets/Chanuka.md` (`000 Source PDFs/Chanuka.pdf`, Subject: *Machshava*, Fall 2026 Final) — 7 embedded sources across 2 pages. Verified every citation against the decoded Davka font text stream and PDF layout, resolved all flagged and malformed sources (**זכריה פרק ח פסוק יט**, **זכריה פרק ד**, and **בעקבי הצאן להגרצ"ש ס׳ י"ט**), verified preservation of user study notes in **תלמוד בבלי מסכת מועד קטן דף ט עמוד א**, verified multi-page continuation crop `Chanuka_p2_cont.png` for **הגרי"ז הלוי על זכריה פרק ד פסוק ב**, updated author profile aliases in `222 Authors/הרב צבי שכטר.md`, purged corrupt fallback author files (`222 Authors/זכריה.md` and `222 Authors/בעקבי.md`), and patched all parser root causes in `999 Scripts/process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files, 100% clean notes.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #2 (`זכריה פרק ח פסוק יט`) & Source #5 (`זכריה פרק ד`)
- **Issue**: Missing *Trei Asar* (תרי עשר) individual books in the parser's `TANACH_BOOKS` list caused the parser to fail recognizing Zechariah (*זכריה*) as Tanach scripture. The engine fell back to token extraction (`author: "[[זכריה]]"` and `book: "מקור"`), generated corrupt fallback author note `222 Authors/זכריה.md`, and flagged both sources `audit_needed: true` (*"Author fell back to token 'זכריה'"*). Furthermore, because the sources were not recognized as Tanach, line 1766 attempted Dibur Hamatchil (DH) extraction against Davka nikkud/vowel font streams, generating garbled DH anchors (`### F«ה א%מ` for Zechariah 8:19 and `### ו/H%J%ב ה` for Zechariah 4).
- **Resolution**:
  - Standardized Source #2 note to **`333 Sources/תנ''ך - זכריה - פרק ח פסוק יט.md`**, attributed to canonical author **`[[תנ''ך]]`**, book `זכריה`, location `פרק ח פסוק יט`, headline `### תנ''ך - זכריה - פרק ח פסוק יט`.
  - Standardized Source #5 note to **`333 Sources/תנ''ך - זכריה - פרק ד.md`**, attributed to canonical author **`[[תנ''ך]]`**, book `זכריה`, location `פרק ד`, headline `### תנ''ך - זכריה - פרק ד`.
  - Cleared audit flags, removed `⚠️ (Needs Audit)` badges from the master sheet, purged corrupt fallback author profile `222 Authors/זכריה.md`, and deleted malformed legacy source files.
- **Root Cause Patch**: Added all twelve books of *Trei Asar* (`הושע`, `יואל`, `עמוס`, `עובדיה`, `יונה`, `מיכה`, `נחום`, `חבקוק`, `צפניה`, `חגי`, `זכריה`, `מלאכי`), as well as `דברי הימים א`, `דברי הימים ב`, `שמואל`, and `מלכים`, to `TANACH_BOOKS`. Added `תנ"ך` and `תנ''ך` to `KNOWN_AUTHORS` and `AUTHOR_CANONICAL_MAP`. Line 1766 automatically suppresses DH extraction for Tanach, preventing font scrambling from producing corrupt subheadings.

### 2. Source #7 (`בעקבי הצאן )להגרצ"ש( ס׳ י"ט`)
- **Issue**: Unmapped contemporary halakhic masterpiece *Be'ikvei HaTzon* (*בעקבי הצאן*) by Rabbi Hershel Schachter (Rosh Yeshiva at RIETS / talmid of the Rav) caused the parser to split the title: `author: "[[בעקבי]]"`, `book: "הצאן"`, location `ס׳ י''ט`. The engine generated corrupt fallback author note `222 Authors/בעקבי.md` and flagged the source `audit_needed: true` (*"Author fell back to token 'בעקבי'"*).
- **Resolution**: Identified work as *Be'ikvei HaTzon* by HaGaon Rav Tzvi Schachter (`להגרצ"ש`), Siman 19 (analyzing Zechariah's menorah prophecy, Chanukah as an inauguration and foretaste of the Third Beit HaMikdash, and the relationship between Kedusha Rishona and Kedusha Sheniya). Standardized note to **`333 Sources/הרב צבי שכטר - בעקבי הצאן - ס׳ י''ט.md`**, attributed to canonical author **`[[הרב צבי שכטר]]`**, book `בעקבי הצאן`, location `ס׳ י''ט`, headline `### הרב צבי שכטר - בעקבי הצאן - ס׳ י''ט`. Cleared audit flag, removed `⚠️ (Needs Audit)` badge from the master sheet, purged corrupt fallback author file `222 Authors/בעקבי.md`, and updated aliases in `222 Authors/הרב צבי שכטר.md`.
- **Root Cause Patch**: Added `בעקבי הצאן`, `ספר בעקבי הצאן`, and `עקבי הצאן` to `KNOWN_AUTHORS`, `AUTHOR_CANONICAL_MAP`, and `RESPONSA_SPECIAL_MAP` mapped to `('הרב צבי שכטר', 'בעקבי הצאן')`. Added `בעקבי הצאן` variants to the special book handler in `RESPONSA_SPECIAL_MAP` so author honorific tokens like `להגרצ"ש` in parentheses/body are ignored and never contaminate the book or location.

### 3. Source #3 User Study Notes Preservation (`תלמוד בבלי מסכת מועד קטן דף ט עמוד א`)
- **Verification**: Verified that existing user study notes (`We learn we don't mix simchos with simchos`, `We have a 2 week inaguration party...`) are preserved intact beneath the main content heading in `333 Sources/תלמוד בבלי - מסכת מועד קטן - דף ט עמוד א.md`. Added `Chanuka_p1_s3.png` embed into `### Source Image` alongside the prior `melachim 1.8_p3_s3.png` without disturbing study annotations.

### 4. Source #6 Multi-Page Continuation Verification (`הגרי"ז הלוי על זכריה פרק ד פסוק ב`)
- **Verification**: Verified that Source 6 begins on Page 1 (`Chanuka_p1_s6.png`) and cleanly continues at the top of Page 2 (`Chanuka_p2_cont.png`). Both crops are attached inside `333 Sources/הגרי''ז הלוי - על זכריה - פרק ד פסוק ב.md` under `### Source Image`, with DH `#הפטרת שבת חנוכה ובהעלתך` linking cleanly without header bleed.

---

## 2. Complete Sheet Verification (7/7)

| # | Canonical Title | Canonical Author | Status | Notes |
|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת ראש השנה - דף יח עמוד ב דף יט עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout, image `Chanuka_p1_s1.png` |
| 2 | `תנ''ך - זכריה - פרק ח פסוק יט` | [[תנ''ך]] | 🔧 **Fixed** | Fixed author attribution to Tanach, purged fallback `זכריה`, cleared corrupt DH `F«ה א%מ` |
| 3 | `תלמוד בבלי - מסכת מועד קטן - דף ט עמוד א` | [[תלמוד בבלי]] | ✅ Verified | User study notes preserved; multi-source image crops (`Chanuka_p1_s3.png`, `melachim 1.8_p3_s3.png`) |
| 4 | `תלמוד בבלי - מסכת יומא - דף ט עמוד ב` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout, image `Chanuka_p1_s4.png` |
| 5 | `תנ''ך - זכריה - פרק ד` | [[תנ''ך]] | 🔧 **Fixed** | Fixed author attribution to Tanach, purged fallback `זכריה`, cleared corrupt DH `ו/H%J%ב ה` |
| 6 | `הגרי''ז הלוי - על זכריה - פרק ד פסוק ב` | [[הגרי''ז הלוי]] | ✅ Verified | Verified multi-page continuation crop `Chanuka_p2_cont.png`, clean DH `#הפטרת שבת חנוכה ובהעלתך` |
| 7 | `הרב צבי שכטר - בעקבי הצאן - ס׳ י''ט` | [[הרב צבי שכטר]] | 🔧 **Fixed** | Attributed to Rav Hershel Schachter; purged fallback `בעקבי`; updated canonical author aliases |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Complete Tanach / Trei Asar Recognition**:
   - Expanded `TANACH_BOOKS` to include all twelve books of Trei Asar (`הושע`, `יואל`, `עמוס`, `עובדיה`, `יונה`, `מיכה`, `נחום`, `חבקוק`, `צפניה`, `חגי`, `זכריה`, `מלאכי`), plus `דברי הימים א`, `דברי הימים ב`, `שמואל`, and `מלכים`.
   - Added `תנ"ך` and `תנ''ך` to `KNOWN_AUTHORS` and `AUTHOR_CANONICAL_MAP`.
   - Suppressed DH extraction for all Tanach sources in line 1766, preventing cantillation/nikkud font artifacts from becoming invalid subheadings.

2. **Rav Hershel Schachter / Be'ikvei HaTzon Recognition**:
   - Added `בעקבי הצאן`, `ספר בעקבי הצאן`, and `עקבי הצאן` to `KNOWN_AUTHORS`, `AUTHOR_CANONICAL_MAP`, and `RESPONSA_SPECIAL_MAP` mapped to `('הרב צבי שכטר', 'בעקבי הצאן')`.
   - Added `בעקבי הצאן` variants to the special book handler in `RESPONSA_SPECIAL_MAP` (lines 1255 & 1330) so author honorific tokens (`להגרצ"ש`, `הגרצ"ש`) are discarded and do not pollute the book title or break location extraction.
