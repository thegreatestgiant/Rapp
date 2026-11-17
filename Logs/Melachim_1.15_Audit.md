# Melachim 1.15 Source Sheet Audit

## Summary
Audited `111 Source Sheets/melachim 1.15.md` (`000 Source PDFs/melachim 1.15.pdf`, Subject: *Navi*, Fall 2026 Final) — 14 embedded sources across 2 pages. Verified every citation against the decoded Davka font text stream and PDF layout, resolved all 3 flagged/corrupt sources (**תרגום יונתן**, **בית חדש**, and **משנה מסכת אבות**), corrected corrupted Tanach Dibur Hamatchil header (**ר«פ  א ים** $\to$ canonical Tanach citation), created canonical author profiles in `222 Authors/` (**משנה** and **תרגום יונתן**), enriched **ב''ח**, purged corrupt fallback author profiles (`בית.md`, `מקור.md`, `תרגום.md`), verified continuation crop `melachim 1.15_p2_cont.png` (Yerushalmi Yevamot), preserved user study notes under Moed Katan 16b (Source #4) and Avodah Zarah 44a (Source #8), and patched all parser root causes in `999 Scripts/process_source_sheets.py`. Result: **0 audit flags, 0 broken embeds, 0 missing images, 0 missing author files.**

---

## 1. Flagged & Anomalous Sources Resolved

### 1. Source #3 (`תרגום יונתן על דברי הימים ב פרק יג פסוק ב`)
- **Issue**: Unmapped Targum title caused parser to fall back to `author='תרגום'`, `book='יונתן על דברי הימים ב'`, generated fallback author `222 Authors/תרגום.md`, and flagged the source `audit_needed: true` (*"Author fell back to token 'תרגום'"*). Furthermore, the content heading was generic without a Dibur Hamatchil anchor.
- **Resolution**: Identified work as *Targum Yonatan* on Divrei Hayamim II 13:2. Standardized note to **`תרגום יונתן - דברי הימים ב - פרק יג פסוק ב.md`**, attributed to canonical author **`[[תרגום יונתן]]`**, book `דברי הימים ב`, location `פרק יג פסוק ב`. Established D"H section heading **`### ושום אמיה מיכיהו ברת אוריאל`** containing the user's study notes (*"It's the same women from Divrei Hayamim... She was a good women, and they changed her name to show she is good..."*), and updated the sheet embed to link to `#ושום אמיה מיכיהו ברת אוריאל`.
- **Author Note**: Created [`222 Authors/תרגום יונתן.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%52%D7%A8%D7%92%D7%95%D7%9D%20%D7%99%D7%95%D7%A0%D7%AA%D7%9F.md) with aliases `[תרגום יונתן, תרגום יונתן בן עוזיאל, יונתן בן עוזיאל, תרגום, תרגום ירושלמי, Targum Jonathan, Targum Yonatan]` and Talmudic/scholarly background; purged fallback `222 Authors/תרגום.md`.

### 2. Source #4 (`תלמוד בבלי מסכת מועד קטן דף טז עמוד ב`)
- **Issue**: The sheet was quoting the top header `### תלמוד בבלי - מסכת מעוד קטן - דף ט''ז, עמוד ב` (from *Shmuel II 23*), leaving the user's specific *Melachim 1.15* study notes on David HaMelech's warfare and humility under `### כשהיה יושב ועוסק בתורה` unquoted.
- **Resolution**: Updated embed in [`111 Source Sheets/melachim 1.15.md`](file:///home/sean/Obsidian/Rapp/111%20Source%20Sheets/melachim%201.15.md) to link directly to `### כשהיה יושב ועוסק בתורה`, correctly quoting the user's Melachim 1.15 study notes (*"When דוד used to sit and learn, he made himself very humble / When he went out to war he became solid like a tree, he could kill 800 people with 1 arrow..."*).

### 3. Source #11 (`תנ''ך - דברי הימים ב - פרק טז פסוק יב`)
- **Issue**: Parser extracted reverse-font Hebrew Sof Pasuk word fragment `### ר«פ  א ים` as a Dibur Hamatchil because Tanach was not excluded from generic candidate DH regex matching colons/hyphens.
- **Resolution**: Corrected note heading in [`333 Sources/תנ''ך - דברי הימים ב - פרק טז פסוק יב.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%52%D7%A0''%D7%9A%20-%20%D7%93%D7%91%D7%A8%D7%99%20%D7%94%D7%99%D7%9E%D7%99%D7%9D%20%D7%91%20-%20%D7%A4%D7%A8%D7%A7%20%D7%98%D7%96%20%D7%A4%D7%A1%D7%95%D7%A7%20%D7%99%D7%91.md) to canonical `### תנ''ך - דברי הימים ב - פרק טז פסוק יב` and updated embed on master sheet. Added `תנ''ך` and `תנ"ך` to the parser's DH exclusion list.

### 4. Source #13 (`בית חדש על יו"ד סימן שלו (א)`)
- **Issue**: Missing mapping for *Bayit Chadash* caused parser to fall back to `author='בית'`, `book='חדש על יו''ד'`, generated corrupt fallback `222 Authors/בית.md`, and flagged `audit_needed: true` (*"Author fell back to token 'בית'"*). Furthermore, the Rebbi included an unnumbered excerpt of *Talmud Bavli Sotah 10a* immediately below the Bach within the same crop boundary (`melachim 1.15_p2_s6.png`).
- **Resolution**: Identified work as the *Bayit Chadash* (Bach, Rabbi Yoel Sirkis) on Tur/Shulchan Aruch Yoreh De'ah 336:1 regarding seeking medical healing. Standardized note to **`ב''ח - יורה דעה - סימן שלו.md`**, attributed to canonical author **`[[ב''ח]]`**, book `יורה דעה`, location `סימן שלו`. Added secondary section heading `### תלמוד בבלי - מסכת סוטה - דף י עמוד א` inside the note for the King Asa / podagra excerpt captured in the crop.
- **Author Note**: Updated [`222 Authors/ב''ח.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%91''%D7%97.md) with comprehensive aliases `[הב"ח, הב''ח, ב"ח, ב''ח, בית חדש, רבי יואל סירקיש, יואל סירקיש, Yoel Sirkis, Bach]` and biography; purged fallback `222 Authors/בית.md`.

### 5. Source #14 (`משנה מסכת אבות פרק ה משנה יח`)
- **Issue**: Location regex `loc_match` matched the keyword `משנה` at index 0 of the string, clearing `book_part` to empty and causing `author` to fall back to `'מקור'`, creating fallback author `222 Authors/מקור.md` and flagging `audit_needed: true`.
- **Resolution**: Identified work as foundational Mishnah (*Pirkei Avot 5:18*, *"Kol HaMezakeh Et HaRabim..."*). Standardized note to **`יהודה הנשיא - משנה מסכת אבות - פרק ה משנה יח.md`**, attributed to canonical author **`[[יהודה הנשיא]]`** (without honorific prefix per vault preference), book `משנה מסכת אבות`, location `פרק ה משנה יח`, with D"H anchor `### כל המזכה את הרבים`.
- **Author Note**: Created canonical author note [`222 Authors/יהודה הנשיא.md`](file:///home/sean/Obsidian/Rapp/222%20Authors/%D7%99%D7%94%D7%95%D7%93%D7%94%20%D7%94%D7%A0%D7%51%D7%99%D7%90.md) with aliases `[רבי, רבנו הקדוש, רבי יהודה הנשיא, Judah the Prince, Yehuda HaNasi, משנה]`; purged fallback `222 Authors/מקור.md` and removed corpus placeholder `משנה.md`.

### 6. User Study Notes Preserved
- **Moed Katan 16b (Source #4)**: Preserved user study notes (*"These are words of נבוא... In learning he made himself small and weak like an insect / In war he was mighty as an oak tree..."*) intact in [`333 Sources/תלמוד בבלי - מסכת מעוד קטן - דף ט''ז, עמוד ב.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%52%D7%9C%D7%9E%D7%95%D7%93%20%D7%91%D7%91%D7%94%D7%99%20-%20%D7%9E%D7%A1%D7%9B%D7%AA%20%D7%9E%D7%A2%D7%95%D7%93%20%D7%A7%D7%98%D7%9F%20-%20%D7%93%D7%A3%20%D7%98''%D7%96%2C%20%D7%A2%D7%9E%D7%95%D7%93%20%D7%91.md) and connected to the sheet embed.
- **Avodah Zarah 44a (Source #8)**: Preserved study notes (*"We jews have a special crown. He wants the special crown."*) intact under dedicated header `### תלמוד בבלי - מסכת עבודה זרה - דף מד עמוד א - melachim 1.1`, and created dedicated subsection `### תלמוד בבלי - מסכת עבודה זרה - דף מד עמוד א - melachim 1.15` in [`333 Sources/תלמוד בבלי - מסכת עבודה זרה - דף מד עמוד א.md`](file:///home/sean/Obsidian/Rapp/333%20Sources/%D7%52%D7%9C%D7%9E%D7%95%D7%93%20%D7%91%D7%91%D7%94%D7%99%20-%20%D7%9E%D7%A1%D7%9B%D7%AA%20%D7%A2%D7%91%D7%95%D7%93%D7%94%20%D7%96%D7%A8%D7%94%20-%20%D7%93%D7%A3%20%D7%9E%D7%93%20%D7%A2%D7%9E%D7%95%D7%93%20%D7%90.md). Updated embeds on both `111 Source Sheets/melachim 1.15.md` and `111 Source Sheets/melachim 1.1.md` per multi-sheet disambiguation docs.

---

## 2. Complete Sheet Verification (15/15)

| # | Canonical Title | Canonical Author | Status | Notes |
|---|---|---|---|---|
| 1 | `רד''ק - מלכים א - פרק טו פסוק ב` | [[רד''ק]] | ✅ Verified | Clean 2-header layout |
| 2 | `תנ''ך - דברי הימים ב - פרק יג` | [[תנ''ך]] | ✅ Verified | Verses 1–2; clean header anchor `#פסוקים א-ב` |
| 3 | `תרגום יונתן - דברי הימים ב - פרק יג פסוק ב` | [[תרגום יונתן]] | 🔧 **Fixed** | Attributed to Targum Yonatan; clean DH anchor `#ושום אמיה מיכיהו ברת אוריאל` |
| 4 | `תלמוד בבלי - מסכת מעוד קטן - דף ט''ז, עמוד ב` | [[תלמוד בבלי]] | ✅ Preserved | **User study notes intact; quotes `#כשהיה יושב ועוסק בתורה`** |
| 5 | `ספרי - זוטא - פיסקא כז` | [[ספרי]] | ✅ Verified | Clean 2-header layout |
| 6 | `תנ''ך - דברי הימים ב - פרק יג` | [[תנ''ך]] | ✅ Verified | Verses 3–12; clean header anchor `#פסוקים ג-יב` |
| 7 | `תלמוד ירושלמי - מסכת יבמות - פרק טז דף טו טור ג -ה''ג` | [[תלמוד ירושלמי]] | ✅ Verified | Verified continuation crop `p2_cont` |
| 8 | `תלמוד בבלי - מסכת עבודה זרה - דף מד עמוד א` | [[תלמוד בבלי]] | ✅ Preserved | **Disambiguated sheet headers (`- melachim 1.1` & `- melachim 1.15`); notes preserved** |
| 9 | `תלמוד בבלי - מסכת פסחים - דף קיט עמוד א` | [[תלמוד בבלי]] | ✅ Verified | Clean 2-header layout |
| 10 | `רש''י - מלכים א - פרק יא פסוק לט` | [[רש''י]] | ✅ Verified | Clean DH anchor `#אך לא כל הימים` |
| 11 | `תנ''ך - דברי הימים ב - פרק טז פסוק יב` | [[תנ''ך]] | 🔧 **Fixed** | Corrupt DH `#ר«פ  א ים` replaced with canonical Tanach heading |
| 12 | `אבן עזרא - שמות - פרק כג פסוק כה` | [[אבן עזרא]] | ✅ Verified | Clean 2-header layout |
| 13 | `ב''ח - יורה דעה - סימן שלו` | [[ב''ח]] | 🔧 **Fixed** | Attributed to Bach; study notes preserved |
| 14 | `תלמוד בבלי - מסכת סוטה - דף י עמוד א` | [[תלמוד בבלי]] | 🔧 **Fixed** | Separated unnumbered Gemara into dedicated note #14; study notes preserved; dedicated crop `melachim 1.15_p2_s6_sotah.png` |
| 15 | `יהודה הנשיא - משנה מסכת אבות - פרק ה משנה יח` | [[יהודה הנשיא]] | 🔧 **Fixed** | Bumped to #15; attributed to Yehudah HaNasi; DH anchor `#כל המזכה את הרבים` |

---

## 3. Stage 2 — Parser Root Cause Fixes (`999 Scripts/process_source_sheets.py`)

1. **Mishnah Citation Recognition**:
   - Added regex check `re.match(r'^(?:ספר\s+)?משנה\s+(מסכת\s+[א-ת\s]+?)\s+((?:פרק|סדר|הלכה|בבא).*)$', clean)` before general `loc_match`, ensuring Mishnaic tractates and locations extract directly (`author='משנה'`, `book='מסכת אבות'`, `location='פרק ה משנה יח'`).
   - Updated `loc_match` regex to `(?<!^)משנה(?!\s*ברורה)`, preventing construct occurrences of `משנה` at index 0 from stripping the book name into location.
   - Added canonical mappings for `משנה` to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.

2. **Targum Yonatan Mapping**:
   - Added `'תרגום יונתן'` and `'תרגום'` to `RESPONSA_SPECIAL_MAP` and `AUTHOR_CANONICAL_MAP`.
   - Handled prefix stripping (`book = re.sub(r'^(?:על\s+)?', '', extra_clean).strip()`), correctly isolating Tanach books (e.g. `דברי הימים ב`) as the book parameter.
   - Added `תרגום יונתן` and `תרגום` to `KNOWN_AUTHORS`.

3. **Bayit Chadash (Bach) Mapping & Arba'ah Turim Chelek Normalization**:
   - Added `'בית חדש'` and `'ספר בית חדש'` to `RESPONSA_SPECIAL_MAP` mapped to `("ב''ח", 'בית חדש')`.
   - Added canonical mappings for `בית חדש` and `ספר בית חדש` to `AUTHOR_CANONICAL_MAP` and `KNOWN_AUTHORS`.
   - Implemented Arba'ah Turim chelek extraction checking `rest`: correctly maps `יו"ד` / `יו''ד` to `יורה דעה`, `או"ח` to `אורח חיים`, `חו"מ` to `חושן משפט`, and `אהע"ז` to `אבן העזר`, stripping the chelek token from `location`.

4. **Tanach DH Extraction Suppression**:
   - Added `"תנ''ך"` and `'תנ"ך'` to the author exclusion list in DH extraction (`author not in ["תנ''ך", 'תנ"ך', "שמירת שבת כהלכתה", ...]`): prevents Sof Pasuk colons or verse text from generating corrupt reverse-font D"H section headings.
