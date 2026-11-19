# Kluta (קלוטה כמי שהונחה דמי) Source Sheet Audit

## Summary
Audited `111 Source Sheets/kluta.md` (`000 Source PDFs/kluta.pdf`, Subject: *Gemara*, Fall 2026 Final) — 10 embedded sources across 2 pages. Verified every citation against the decoded text stream and PDF layout, resolved all 3 flagged sources (**רבינו חננאל**, **מרומי שדה / הנצי''ב**, and **באור הלכה / משנה ברורה**), normalized the long descriptive quote range in Talmud Bavli Shabbat 4a–b into canonical format **`תלמוד בבלי - מסכת שבת - דף ד עמוד א וב.md`**, created canonical author profile in `222 Authors/` (**רבינו חננאל**), enriched **הנצי''ב**, purged corrupt fallback author profiles (`222 Authors/רבינו.md`, `222 Authors/מרומי.md`, and `222 Authors/באור.md`), verified continuation crop `kluta_p2_cont.png` (Rav Elyashiv), preserved user study notes under Chashukei Chemed Shabbat 4a, disambiguated multiple-sheet section headers (`- kluta`), and patched all parser root causes in `999 Scripts/process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #1 (`תלמוד בבלי מסכת שבת דף ד עמוד א "פשט העני את ידו/ אמאי חייב?" עד עמוד ב "הא מני - רבי היא/"`)
- **Issue**: The entire descriptive opening and closing quote string was captured as the location token, creating an unwieldy filename (`333 Sources/תלמוד בבלי - מסכת שבת - דף ד עמוד א ''פשט העני את ידו- אמאי חייב-'' עד עמוד ב ''הא מ.md`).
- **Resolution**: Normalized the range to canonical vault syntax **`333 Sources/תלמוד בבלי - מסכת שבת - דף ד עמוד א וב.md`**, location `דף ד עמוד א וב`, with section heading **`### פשט העני את ידו`**. Updated master sheet embed to `![[תלמוד בבלי - מסכת שבת - דף ד עמוד א וב#פשט העני את ידו]]`.
- **Root Cause Patch**: Added regex normalization in `parse_citation` converting patterns of `דף [X] עמוד [א] "..." עד עמוד [ב] "..."` into `דף X עמוד א וב`.

### 2. Source #2 (`רבינו חננאל מסכת שבת דף ד עמוד ב`)
- **Issue**: Unmapped author caused parser to fall back to single token `author: "רבינו"`, `book: "חננאל מסכת שבת"`, generated corrupt fallback `222 Authors/רבינו.md`, and flagged the source `audit_needed: true` (*"Author fell back to token 'רבינו'"*).
- **Resolution**: Identified work as *Rabbeinu Chananel* on Shabbat 4b. Standardized note to **`333 Sources/רבינו חננאל - מסכת שבת - דף ד עמוד ב.md`**, attributed to canonical author **`[[רבינו חננאל]]`**, book `מסכת שבת`, location `דף ד עמוד ב`. Cleared audit flag and removed `⚠️ (Needs Audit)` badge from the master sheet.
- **Author Note**: Created canonical author profile [`222 Authors/רבינו חננאל.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%A8%D7%91%D7%99%D7%A0%D7%20%D7%97%D7%A0%D7%A0%D7%90%D7%9C.md) with aliases `[רבינו חננאל, רבנו חננאל, ר"ח, ר''ח, רבינו חננאל בן חושיאל, Rabbeinu Chananel, Rabbeinu Hananel]` and Kairouan biographical context; purged fallback `222 Authors/רבינו.md`.
- **Root Cause Patch**: Added `רבינו חננאל` and `רבנו חננאל` to `KNOWN_AUTHORS`, `KNOWN_HEADER_KEYWORDS`, `AUTHOR_CANONICAL_MAP`, and `RESPONSA_SPECIAL_MAP`.

### 3. Source #4 (`מרומי שדה מסכת שבת דף ד עמוד א`)
- **Issue**: Multi-word Sefer title was split, causing parser to fall back to `author: "מרומי"`, `book: "שדה מסכת שבת"`, generated corrupt fallback `222 Authors/מרומי.md`, and flagged `audit_needed: true` (*"Author fell back to token 'מרומי'"*).
- **Resolution**: Identified work as *Meromei Sadeh* by Rabbi Naftali Zvi Yehuda Berlin (Netziv). Standardized note to **`333 Sources/הנצי''ב - מרומי שדה מסכת שבת - דף ד עמוד א.md`**, attributed to canonical author **`[[הנצי''ב]]`**, book `מרומי שדה מסכת שבת`, location `דף ד עמוד א`. Cleared audit flag and removed `⚠️ (Needs Audit)` badge.
- **Author Note**: Enriched [`222 Authors/הנצי''ב.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%94%D7%A0%D7%A6%D7%99''%D7%91.md) with aliases `[הנצי"ב, הנצי''ב, נצי"ב, נצי''ב, רבי נפתלי צבי יהודה ברלין, נפתלי צבי יהודה ברלין, העמק דבר, משיב דבר, מרומי שדה, Netziv, Naftali Zvi Yehuda Berlin]`; purged fallback `222 Authors/מרומי.md`.
- **Root Cause Patch**: Added `מרומי שדה` to `KNOWN_AUTHORS`, `KNOWN_HEADER_KEYWORDS`, `AUTHOR_CANONICAL_MAP` (mapped to `הנצי''ב`), and `RESPONSA_SPECIAL_MAP`.

### 4. Source #7 (`באור הלכה סימן כה סעיף ט ד"ה * ואם הפסיק`)
- **Issue**: *Chaser* spelling without yud (`באור הלכה` instead of `ביאור הלכה`) missed the special mapping, falling back to `author: "באור"`, `book: "הלכה"`, creating fallback `222 Authors/באור.md`, and flagging `audit_needed: true`. Additionally, the leading asterisk `*` in the Dibur Hamatchil was retained.
- **Resolution**: Identified work as *Biur Halacha* on Shulchan Aruch Orach Chaim 25:9 by the Chofetz Chaim. Standardized note to **`333 Sources/משנה ברורה - ביאור הלכה - סימן כה סעיף ט ד''ה ואם הפסיק.md`**, attributed to canonical author **`[[משנה ברורה]]`**, book `ביאור הלכה`, location `סימן כה סעיף ט ד''ה ואם הפסיק`, and anchor `### ואם הפסיק`. Cleared audit flag and removed `⚠️ (Needs Audit)` badge.
- **Root Cause Patch**: Added `באור הלכה` alongside `ביאור הלכה` to `KNOWN_AUTHORS`, `KNOWN_HEADER_KEYWORDS`, `AUTHOR_CANONICAL_MAP`, and `parse_citation`; added asterisk stripping from location and DH tokens (`re.sub(r'ד["״\'׳]*ה\s*[\*]\s*', 'ד"ה ', location)`). Purged fallback `222 Authors/באור.md`.

### 5. Source #10 (`הרב יצחק זילברשטיין - חשוקי חמד מסכת שבת - דף ד עמוד א`)
- **Issue**: The note contains extensive existing user study notes from two prior sheets (`sin to fix` and `sin for other`). The new section header needed disambiguation without disturbing prior user study notes.
- **Resolution**: Preserved all user annotations verbatim. Disambiguated the section heading to **`### הרב יצחק זילברשטיין - חשוקי חמד מסכת שבת - דף ד עמוד א - kluta`** and updated the master sheet embed accordingly.

---

## 2. Complete Sheet Verification (10/10)

| # | Canonical Title | Canonical Author | Status | Target Heading / Anchor |
|---|---|---|---|---|
| 1 | `תלמוד בבלי - מסכת שבת - דף ד עמוד א וב` | [[תלמוד בבלי]] | 🔧 **Fixed** | `#פשט העני את ידו` |
| 2 | `רבינו חננאל - מסכת שבת - דף ד עמוד ב` | [[רבינו חננאל]] | 🔧 **Fixed** | `#רבינו חננאל - מסכת שבת - דף ד עמוד ב` |
| 3 | `רש''י - מסכת שבת - דף ד עמוד א ד''ה קלוטה` | [[רש''י]] | ✅ Verified | `#קלוטה` |
| 4 | `הנצי''ב - מרומי שדה מסכת שבת - דף ד עמוד א` | [[הנצי''ב]] | 🔧 **Fixed** | `#הנצי''ב - מרומי שדה מסכת שבת - דף ד עמוד א` |
| 5 | `אבני נזר - שו''ת אבני נזר חלק אורח חיים - סימן רמ` | [[אבני נזר]] | ✅ Verified | Clean 2-header layout |
| 6 | `רבי יעקב חגיז - שו''ת הלכות קטנות חלק ב - סימן מב` | [[רבי יעקב חגיז]] | ✅ Verified | Clean 2-header layout |
| 7 | `משנה ברורה - ביאור הלכה - סימן כה סעיף ט ד''ה ואם הפסיק` | [[משנה ברורה]] | 🔧 **Fixed** | `#ואם הפסיק` |
| 8 | `הרב יוסף שלום אלישיב - מסכת שבת - דף ד עמוד א` | [[הרב יוסף שלום אלישיב]] | ✅ Verified | Verified continuation crop `p2_cont` |
| 9 | `רב עובדיה יוסף - שו''ת יביע אומר - חלק ה - אורח חיים סימן ה` | [[רב עובדיה יוסף]] | ✅ Verified | Clean 2-header layout |
| 10 | `הרב יצחק זילברשטיין - חשוקי חמד מסכת שבת - דף ד עמוד א` | [[הרב יצחק זילברשטיין]] | ✅ Preserved | **All user study notes intact; quotes dedicated `# - kluta` anchor** |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Rabbeinu Chananel Mapping**:
   - Added `רבינו חננאל` and `רבנו חננאל` to `KNOWN_AUTHORS`, `KNOWN_HEADER_KEYWORDS`, `AUTHOR_CANONICAL_MAP`, and `RESPONSA_SPECIAL_MAP`.

2. **Meromei Sadeh (Netziv) Recognition**:
   - Added `מרומי שדה` to `KNOWN_AUTHORS`, `KNOWN_HEADER_KEYWORDS`, `AUTHOR_CANONICAL_MAP` (mapped to `הנצי''ב`), and `RESPONSA_SPECIAL_MAP` with tractate preservation.

3. **Biur Halacha (*Chaser* Spelling & Asterisks)**:
   - Added `באור הלכה` alongside `ביאור הלכה` to `KNOWN_AUTHORS`, `KNOWN_HEADER_KEYWORDS`, `AUTHOR_CANONICAL_MAP`, and `parse_citation`.
   - Added automatic stripping of leading asterisks `*` from D"H strings.

4. **Talmud Page Range Normalization**:
   - Added regex detection in `parse_citation` mapping range expressions like `דף [X] עמוד [א] "..." עד עמוד [ב] "..."` into canonical `דף X עמוד א וב`.
   - Added slash `/` delimiter support to Dibur Hamatchil detection.
