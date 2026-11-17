# Tefilin Source Sheet Audit

## Summary
Audited `111 Source Sheets/tefilin.md` (`000 Source PDFs/tefilin.pdf`, Subject: *Halacha*, Fall 2026 Final) — 45 embedded sources.
1. **Resolved Collision & Section Disambiguation (#16 and #24)**:
   - Disambiguated two separate Shulchan Aruch citations from Siman 27 that had collided into a single un-se'ifed file (`שולחן ערוך - אורח חיים - סימן כז.md`) with duplicate headings (`(2)`).
   - Separated into **`שולחן ערוך - אורח חיים - סימן כז סעיף א`** (crop: `tefilin_p2_s6.png`) and **`שולחן ערוך - אורח חיים - סימן כז סעיף י`** (crop: `tefilin_p3_s7.png`), and purged the obsolete collided file.
2. **Page-Boundary Dibur Hamatchil Resolution (#25 and #38)**:
   - For **משנה ברורה סימן כז ס''ק מז** (#25), the citation occurred at the bottom of Page 3 while its dibur hamatchil (**`אין להקפיד`**) appeared across the page boundary at the top of Page 4. Extracted the DH, updated the heading to `### אין להקפיד`, and updated the embed in `tefilin.md`.
   - For **משנה ברורה סימן לח ס''ק יג** (#38), the citation occurred at the bottom of Page 5 while its dibur hamatchil (**`מוחים בידן`**) appeared at the top of Page 6. Extracted the DH, updated the heading to `### מוחים בידן`, and updated the embed in `tefilin.md`.
3. **Multi-Page Continuation Integrity**:
   - Verified that all 5 multi-page continuation crops across the 6-page PDF are properly linked and embedded in their respective source notes:
     - Source #10: `tefilin_p1_s10.png` + `tefilin_p2_cont.png` (SA 25:11)
     - Source #17: `tefilin_p2_s7.png` + `tefilin_p3_cont.png` (MB 27:10)
     - Source #25: `tefilin_p3_s8.png` + `tefilin_p4_cont.png` (MB 27:47)
     - Source #32: `tefilin_p4_s7.png` + `tefilin_p5_cont.png` (SA 34)
     - Source #38: `tefilin_p5_s6.png` + `tefilin_p6_cont.png` (MB 38:13)
4. **Author Canonical Integrity**:
   - All 45 sources link to canonical authors in `222 Authors/`: `[[שולחן ערוך]]`, `[[משנה ברורה]]`, and `[[הרב שמחה רבינוביץ]]` (Piskei Teshuvot).
5. **Script Root-Cause Patches (`999 Scripts/process_source_sheets.py`)**:
   - Added automatic Se'if extraction from the text block for Shulchan Aruch when the Se'if is placed on the line following the Siman header.
   - Added Shulchan Aruch Siman disambiguation post-pass (automatically attributing the earlier un-se'ifed section to `סעיף א` when subsequent sections exist in the same Siman).
   - Added multi-page continuation Dibur Hamatchil detection (scanning the top line of the next page's continuation text for the DH when a Mishnah Berurah begins at the bottom of the preceding page).
6. **Result**: **0 audit warnings, 0 broken embeds, 0 missing images, 0 duplicate/collided files, 45/45 verified.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #16 & #24 (Shulchan Aruch Siman 27 Collision)
- **Issue**: Both sources in the PDF had the header line `שולחן ערוך אורח חיים סימן כז`, with the specific Se'if on the following line (`סעיף א -` on Page 2 for Source 16, and `סעיף י -` on Page 3 for Source 24). The parser extracted only the Siman line, resulting in both sources mapping to `שולחן ערוך - אורח חיים - סימן כז.md`, stacking crops `tefilin_p2_s6.png` and `tefilin_p3_s7.png`, and creating duplicate header anchor `#שולחן ערוך - אורח חיים - סימן כז (2)`.
- **Resolution**:
  - Separated into two distinct canonical source notes:
    - **`שולחן ערוך - אורח חיים - סימן כז סעיף א.md`** (crop: `tefilin_p2_s6.png`, anchor: `#שולחן ערוך - אורח חיים - סימן כז סעיף א`)
    - **`שולחן ערוך - אורח חיים - סימן כז סעיף י.md`** (crop: `tefilin_p3_s7.png`, anchor: `#שולחן ערוך - אורח חיים - סימן כז סעיף י`)
  - Updated embeds in `111 Source Sheets/tefilin.md` accordingly.
  - Purged the collided file `333 Sources/שולחן ערוך - אורח חיים - סימן כז.md`.

### 2. Source #25 & #38 (Page-Boundary Dibur Hamatchil Missing)
- **Issue**: In both cases, the source header occurred at the very bottom of a page, with the Dibur Hamatchil text starting at the very top of the continuation page. Because the parser looked for DH only within the initial page's block, it fell back to generic headers `### משנה ברורה - סימן כז ס''ק מז` and `### משנה ברורה - סימן לח ס''ק יג`.
- **Resolution**:
  - Source #25: Text at top of Page 4 begins `אין להקפיד -`. Set heading and embed anchor to **`#אין להקפיד`**.
  - Source #38: Text at top of Page 6 begins `מוחים בידן -`. Set heading and embed anchor to **`#מוחים בידן`**.

---

## 2. Full Sheet Verification (45/45)

| # | Canonical Title | Author | Status | Notes |
|---|---|---|---|---|
| 1 | `שולחן ערוך - אורח חיים - סימן כה סעיף א` | [[שולחן ערוך]] | ✅ Verified | Crop `p1_s1.png` |
| 2 | `שולחן ערוך - אורח חיים - סימן כה סעיף ב` | [[שולחן ערוך]] | ✅ Verified | Crop `p1_s2.png` |
| 3 | `משנה ברורה - סימן כה ס''ק ח` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#בביתו`; crop `p1_s3.png` |
| 4 | `שולחן ערוך - אורח חיים - סימן כה סעיף ד` | [[שולחן ערוך]] | ✅ Verified | Crop `p1_s4.png` |
| 5 | `משנה ברורה - סימן כה ס''ק יד` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#בשעת ק"ש ותפלה`; crop `p1_s5.png` |
| 6 | `שולחן ערוך - אורח חיים - סימן כה סעיף ו` | [[שולחן ערוך]] | ✅ Verified | Crop `p1_s6.png` |
| 7 | `משנה ברורה - סימן כה ס''ק כג` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#להעביר`; crop `p1_s7.png` |
| 8 | `שולחן ערוך - אורח חיים - סימן כה סעיף ט` | [[שולחן ערוך]] | ✅ Verified | Crop `p1_s8.png` |
| 9 | `משנה ברורה - סימן כה ס''ק כח` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#אסור להפסיק`; crop `p1_s9.png` |
| 10 | `שולחן ערוך - אורח חיים - סימן כה סעיף יא` | [[שולחן ערוך]] | ✅ Verified | Multi-crop intact (`p1_s10.png`, `p2_cont.png`) |
| 11 | `משנה ברורה - סימן כה ס''ק לח` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#קודם שיכרוך`; crop `p2_s1.png` |
| 12 | `שולחן ערוך - אורח חיים - סימן כה סעיף יג` | [[שולחן ערוך]] | ✅ Verified | Crop `p2_s2.png` |
| 13 | `משנה ברורה - סימן כה ס''ק נה` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#נהגו העולם`; crop `p2_s3.png` |
| 14 | `משנה ברורה - סימן כה ס''ק נו` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#ג׳ קדושות`; crop `p2_s4.png` |
| 15 | `משנה ברורה - סימן כה ס''ק סב` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#בכל מקום`; crop `p2_s5.png` |
| 16 | `שולחן ערוך - אורח חיים - סימן כז סעיף א` | [[שולחן ערוך]] | 🔧 **Fixed** | Disambiguated from Se'if י; crop `p2_s6.png` |
| 17 | `משנה ברורה - סימן כז ס''ק י` | [[משנה ברורה]] | ✅ Verified | Multi-crop intact (`p2_s7.png`, `p3_cont.png`) |
| 18 | `שולחן ערוך - אורח חיים - סימן כז סעיף ד` | [[שולחן ערוך]] | ✅ Verified | Crop `p3_s1.png` |
| 19 | `משנה ברורה - סימן כז ס''ק טו` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#לא שנא ש"ר`; crop `p3_s2.png` |
| 20 | `שולחן ערוך - אורח חיים - סימן כז סעיף ו` | [[שולחן ערוך]] | ✅ Verified | Crop `p3_s3.png` |
| 21 | `משנה ברורה - סימן כז ס''ק כב` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#יד ימינו`; crop `p3_s4.png` |
| 22 | `שולחן ערוך - אורח חיים - סימן כז סעיף ט` | [[שולחן ערוך]] | ✅ Verified | Crop `p3_s5.png` |
| 23 | `משנה ברורה - סימן כז ס''ק לג` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#עיקרי השער`; crop `p3_s6.png` |
| 24 | `שולחן ערוך - אורח חיים - סימן כז סעיף י` | [[שולחן ערוך]] | 🔧 **Fixed** | Disambiguated from Se'if א; crop `p3_s7.png` |
| 25 | `משנה ברורה - סימן כז ס''ק מז` | [[משנה ברורה]] | 🔧 **Fixed** | Continuation DH `#אין להקפיד`; multi-crop `p3_s8.png`, `p4_cont.png` |
| 26 | `שולחן ערוך - אורח חיים - סימן כח` | [[שולחן ערוך]] | ✅ Verified | Crop `p4_s1.png` |
| 27 | `משנה ברורה - סימן כח ס''ק ב` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#שלא יסיח דעתו`; crop `p4_s2.png` |
| 28 | `משנה ברורה - סימן כח ס''ק ז` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#ועליו של יד`; crop `p4_s3.png` |
| 29 | `שולחן ערוך - אורח חיים - סימן ל` | [[שולחן ערוך]] | ✅ Verified | Crop `p4_s4.png` |
| 30 | `משנה ברורה - סימן ל ס''ק ד` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#ויישן בהם`; crop `p4_s5.png` |
| 31 | `שולחן ערוך - אורח חיים - סימן לב` | [[שולחן ערוך]] | ✅ Verified | Crop `p4_s6.png` |
| 32 | `שולחן ערוך - אורח חיים - סימן לד` | [[שולחן ערוך]] | ✅ Verified | Multi-crop intact (`p4_s7.png`, `p5_cont.png`) |
| 33 | `משנה ברורה - סימן לד ס''ק יג` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#לא יוכל`; crop `p5_s1.png` |
| 34 | `משנה ברורה - סימן לד ס''ק טז` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#כן`; crop `p5_s2.png` |
| 35 | `שולחן ערוך - אורח חיים - סימן לז` | [[שולחן ערוך]] | ✅ Verified | Crop `p5_s3.png` |
| 36 | `משנה ברורה - סימן לז` | [[משנה ברורה]] | ✅ Verified | Crop `p5_s4.png` |
| 37 | `שולחן ערוך - אורח חיים - סימן לח סעיף ג` | [[שולחן ערוך]] | ✅ Verified | Crop `p5_s5.png` |
| 38 | `משנה ברורה - סימן לח ס''ק יג` | [[משנה ברורה]] | 🔧 **Fixed** | Continuation DH `#מוחים בידן`; multi-crop `p5_s6.png`, `p6_cont.png` |
| 39 | `שולחן ערוך - אורח חיים - סימן לח סעיף ד` | [[שולחן ערוך]] | ✅ Verified | Crop `p6_s1.png` |
| 40 | `שולחן ערוך - אורח חיים - סימן לח סעיף ז` | [[שולחן ערוך]] | ✅ Verified | Crop `p6_s2.png` |
| 41 | `משנה ברורה - סימן לח ס''ק כג` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#פטורים`; crop `p6_s3.png` |
| 42 | `שולחן ערוך - אורח חיים - סימן לט סעיף י` | [[שולחן ערוך]] | ✅ Verified | Crop `p6_s4.png` |
| 43 | `משנה ברורה - סימן לט ס''ק כו` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#לעולם`; crop `p6_s5.png` |
| 44 | `משנה ברורה - סימן לט ס''ק כז` | [[משנה ברורה]] | ✅ Verified | Dibur Hamatchil `#לפרקים`; crop `p6_s6.png` |
| 45 | `הרב שמחה רבינוביץ - פסקי תשובות אורח חיים - סימן לט סעי׳ י׳` | [[הרב שמחה רבינוביץ]] | ✅ Verified | Dibur Hamatchil `#שו"ע`; crop `p6_s7.png` |

---

## 3. Parser Root Cause Patches (`999 Scripts/process_source_sheets.py`)

1. **Subsequent-Line Shulchan Aruch Se'if Detection**:
   - In `extract_sources_and_images`: when `author == 'שולחן ערוך'` or `book == 'שולחן ערוך'` and `סעיף` is not in `location`, inspects `first_line_dec` for `^סעיף\s+([א-ת0-9]+)`. If a non-aleph Se'if (e.g. `סעיף י`) is present, it is automatically added to `location`.
2. **Shulchan Aruch Siman Disambiguation Post-Pass**:
   - Added a post-pass across all extracted sources: if an un-se'ifed Shulchan Aruch source shares a Siman with another source on the sheet that specifies a Se'if, the earlier un-se'ifed source is automatically attributed to `סעיף א`. Simanim with only a single source remain clean and un-renamed (dual compatibility).
3. **Continuation Page Dibur Hamatchil Scanning**:
   - In `extract_sources_and_images`: when a multi-page continuation block (`cont_rect`) is generated, if `sources[-1]` is a Mishnah Berurah lacking a Dibur Hamatchil, the script scans the first line of the continuation text on the next page (`content_blocks[0]`) to detect and extract the Dibur Hamatchil.
