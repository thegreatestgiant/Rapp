# Bugs Fixed

## 2026-08-02
- **Author Matching Order (`process_source_sheets.py`)**: Fixed an issue where shorter author names in `KNOWN_AUTHORS` (like `רמב"ם`) were matched before longer ones (like `הרמב"ם`), which caused the prefix to remain in the book title. Sorted the list by length descending before checking.
- **Dataview Path Bug (`process_source_sheets.py`)**: Fixed the Dataview query in the Author template generating paths like `FROM "Gemara/Sources"` instead of a proper relative path. Now uses a robust `#gemara-source` tag instead.
- **Fallback Author Logic (`process_source_sheets.py`)**: Fixed the fallback logic so that when the first word of a book is used as the author, it is properly removed from the book string.
- **Image Cropping Overlaps (`process_source_sheets.py`)**: Added a safeguard (`max(y0 + 10, y1)`) to ensure PDF cropping rects always have positive height, preventing crashes on multi-column layouts where headers might share the same Y-axis.
- **Fragile Regex (`clean_pending_edits.py`)**: Improved the regex for cleaning `> [!todo] Pending Edit Approval` blocks so it correctly replaces them with blank lines instead of eating all surrounding whitespace.
- **Git History Locks (`.venv`, `.tmp.drive*`)**: Purged `.venv` and Google Drive sync folders from the entire Git history, as `.venv` was causing lock/unstaged change conflicts during rebases and filter-branch operations.
- **Git Workspace Noise**: Purged `.obsidian/workspace.json` from the entire git history because it changes constantly and dirties the working directory.
- **Empty Dataviews for Authors**: Discovered that after cloning a Git submodule, Obsidian Dataview fails to index the new files and tags until the application is fully reloaded (`Ctrl+R`). Additionally, confirmed that Obsidian 1.4+ Properties natively parses `author: "[[אבן עזרא]]"` as a Link object, meaning `contains(author, this.file.link)` perfectly works without modifications.
- **Outdated Hardcoded Paths (`Run PDF Parser.md`, `clean_pending_edits.py`, etc.)**: Fixed several hardcoded directory paths in the `Run PDF Parser.md` template and Python auxiliary scripts that were still pointing to the old unnumbered `Sources` or `Source PDFs` folders instead of `333 Sources` and `000 Source PDFs` respectively. Also updated `Run PDF Parser.md` to execute `../.venv/bin/python`.
- **Aggressive Fuzzy Matching False Positives**: Fixed a critical bug in `process_source_sheets.py` where the fuzzy matching (`difflib`) threshold was set too low (`0.7`). This caused the parser to incorrectly link unrelated sources if they shared an author and similar length (e.g., matching `תלמוד בבלי מסכת שבת דף קטז עמוד ב` instead of `תלמוד בבלי מסכת ראש השנה דף כט עמוד ב`). Increased the threshold to `0.90` to strictly require identical or near-identical text (e.g., gracefully handling minor variations like `עמוד ב` vs `ע"ב` without jumping to the wrong tractate).
- **Strict Component Matching for Source Files**: Upgraded the `match_existing_source` logic in `process_source_sheets.py` from basic full-string fuzzy matching to a strict component-based architecture. To resolve bugs where `הלכה ט` incorrectly matched `הלכה ח` (due to high string similarity), or `תלמוד בבלי` matched `רש"י`, the script now verifies that both the normalized **Author** matches exactly AND the final **Location Token** matches exactly (e.g., `ט` vs `ח` or `ע"ב` vs `עמוד ב`) before allowing `difflib` to fuzzy match the rest of the book title.

## September 1, 2026 - PyMuPDF Block Splitting Bug
* **Issue**: Sources in PDFs were arbitrarily defaulting to `מקור - מקור`. The extraction script (`process_source_sheets.py`) was misinterpreting headers that ONLY had a number (like `(2`).
* **Root Cause**: Because Hebrew text is right-to-left and numbers are left-to-right, the PyMuPDF library (`fitz`) sometimes completely separates numbers and text on the same line into completely disjoint text blocks. When checking for matching regex like `\( ?\d+`, the script would lock onto the number block alone and completely ignore the disconnected text chunk sitting nearby.
* **Fix**: Added a look-around mechanism to `extract_sources_and_images`. If the detected header block *only* consists of numbers and parentheses, it will scan all other blocks on the same page. If it finds another block sitting horizontally on the exact same Y-axis (`abs(b[1] - h[1]) < 5`), it prepends the orphaned text chunk onto the header before decoding and parsing.

## September 2, 2026 - Rabbi Ovadia of Bartenura & Single-Letter Author Parse Bug
* **Issue**: Citations starting with `ר' עובדיה מברטנורא` or `ר׳ עובדיה מברטנורא` parsed the author as isolated `ר׳` instead of the full author name, causing erroneous author files like `ר׳.md` and incorrect source naming.
* **Root Cause**: The parser did not recognize abbreviation variants of Bartenura in its known author index, and the fallback parsing logic extracted the first token `ר׳`/`ר'` as the author when known authors failed to match.
* **Fix**:
  - Added canonical alias mappings in `AUTHOR_CANONICAL_MAP` mapping `ר' עובדיה מברטנורא`, `ר׳ עובדיה מברטנורא`, and `ברטנורא` to `רבי עובדיה מברטנורא`.
  - Added Bartenura variants to `extras` in `get_all_known_authors()`.
  - Added `ר`, `ר'`, `ר׳` to bad author filter list and fallback guards to avoid treating single-letter honorific prefixes as authors.
  - Audited and updated existing source file, author file, and source sheet embed link.

## 2026-09-08: Melachim 2 Audit & Fixes
* **Audit of `melachim 2.md`:** Systematically checked all source links in `melachim 2.md` that were poorly parsed.
* **Bad Author & Title Extraction:** Corrected several sources that incorrectly extracted titles or generic prefixes as authors. Fixed:
  * "סדר - סדר הדורות..." -> `רבי יחיאל היילפרין`
  * "תנ''ך - ילקוט שמעוני..." -> `ילקוט שמעוני`
  * "מלכים - הגרי''ז הלוי..." -> `הגרי''ז הלוי`
  * "שיחות - שיחות מוסר..." and "ה - ה '' א..." -> `רבי חיים שמואלביץ`
  * "תנ''ך - העמק דבר..." -> `הנצי''ב מולוז'ין`
  * "במדבר רבה" and "תנ''ך - רות רבה" -> `מדרש רבה`
  * Created missing author profiles in `222 Authors` for `רבי יחיאל היילפרין`, `ילקוט שמעוני`, `הגרי''ז הלוי`, `רבי חיים שמואלביץ`, `הנצי''ב מולוז'ין`, `מדרש רבה`.
  * Renamed incorrectly named source files in `333 Sources` to fit the `Author - Book - Location.md` convention.
* **Script Root Cause Patches:** Updated `process_source_sheets.py` to prevent Hebrew letters like `ה - ` from being mistakenly identified as authors due to list numbering formats not being stripped. Also added entries to `AUTHOR_CANONICAL_MAP` to correctly match well-known books like `שיחות מוסר`, `סדר הדורות`, `ילקוט שמעוני`, and `העמק דבר` and automatically map them to their canonical authors.
* **Source Embed Issue Fix:** Fixed a formatting bug in `process_source_sheets.py` where cropped images were placed under a `### Source` header rather than the `### Author - Book - Location` heading. This caused the master source sheets (which use `#Author - Book - Location` fragment embeds) to only render text and completely miss displaying the source images. Script modified to drop images directly beneath the fragment heading. 
* Updated all existing sources in `melachim 2` to move the images to the correct heading.
* **Reverted Source Embed Issue Fix:** Restored the 2-header layout for sources, using `### Source Image` to contain the images, directly above the `### Author - Book - Location` heading.
* **Image Restoration:** Fixed a bug where a formatting reversion script accidentally deleted source images from the markdown files (because the `### Source Image` header had been lost). The images were successfully restored under newly injected `### Source Image` headers. Also removed a duplicated image that was accidentally inserted into Source 17 (רד''ק).
* **Commentary Parsing Bug (`process_source_sheets.py`):** Fixed a systematic parsing issue where citations beginning with commentary prefixes like `פ׳` or `פירוש` (e.g., `פ׳ זית רענן על ילקוט שמעוני...`) caused the python parser to fail author extraction. Added regex to `process_source_sheets.py` to seamlessly strip these prefixes. As a result, Source 3 is now correctly attributed directly to the commentary `זית רענן` rather than erroneously mapping to the base text (`ילקוט שמעוני`) or the underlying rabbi (`מגן אברהם`). Created a new author profile for `זית רענן` and updated all metadata and embed links.

## 2026-09-08: Chatzi Shiur Audit & Fixes
* **Audit of `chatzi shiur.md`:** Systematically checked all source links in `chatzi shiur.md` that were poorly parsed.
* **Bad Author & Title Extraction:** Corrected several sources that incorrectly extracted the first word of the title as the author due to missing canonical maps. Fixed:
  * "לחם - לחם שמים על..." -> `רבי יעקב עמדין`
  * "בית - בית מאיר..." -> `רבי מאיר פוזנר`
  * "ספר אשי - ספר אשי ישראל..." -> `אשי ישראל`
  * "תפארת - תפארת ישראל..." -> `רבי ישראל ליפשיץ`
  * "שש''כ - שש''כ..." -> `שמירת שבת כהלכתה`
  * "ביצחק - ביצחק יקרא..." -> `ביצחק יקרא`
* **Cleaned up Author Profiles:** Deleted erroneous author profiles (e.g., `לחם.md`, `בית.md`, `ביצחק.md`) and created the proper ones in `222 Authors`.
* **Renamed Source Files:** Renamed incorrectly named source files in `333 Sources` to fit the convention, and updated their internal metadata and headers.
* **Script Root Cause Patches:** Expanded `AUTHOR_CANONICAL_MAP` in `process_source_sheets.py` to automatically map these books (`לחם שמים`, `בית מאיר`, `אשי ישראל`, `תפארת ישראל`, `שש"כ`, `ביצחק יקרא`) to their canonical authors.

## 2026-09-09: Eating on Yom Kippur Audit & Fixes
* **Audit of `eating erev yom kippur.md`:** Systematically checked all source links in `eating erev yom kippur.md` that were poorly parsed.
* **Bad Author & Title Extraction:** Corrected several sources that incorrectly extracted the first word of the title as the author due to missing canonical maps or generic fallbacks. Fixed:
  * "מקור - מקור - טור..." -> `רבי יעקב בן אשר`
  * "ספר שבולי - ספר שבולי הלקט..." -> `רבי צדקיה בן אברהם הרופא`
  * "ספר שערי - ספר שערי תשובה..." -> `רבינו יונה גירונדי`
  * "משנה ברורה - מקור..." -> `חפץ חיים`
  * "ספר מנחת - ספר מנחת חינוך..." -> `רבי יוסף באבד`
* **Cleaned up Author Profiles:** Deleted erroneous author profiles (`מקור.md`, `ספר שבולי.md`, `ספר שערי.md`, `ספר מנחת.md`, `משנה ברורה.md`) and created the proper ones in `222 Authors`.
* **Renamed Source Files:** Renamed incorrectly named source files in `333 Sources` to fit the convention, and updated their internal metadata and headers.
* **Script Root Cause Patches:** Expanded `AUTHOR_CANONICAL_MAP` in `process_source_sheets.py` to automatically map these books (`טור`, `שבלי הלקט`, `שערי תשובה`, `מנחת חינוך`, `משנה ברורה`) to their canonical authors.
* **Image Cropping Cutoff:** Fixed a bug in `process_source_sheets.py` where the final source on a page would be cropped prematurely because the script subtracted 15 pixels from the page height. This caused the bottom of the text to be cut off (e.g., in `eating erev yom kippur` Source 18). Updated the script to crop all the way to `page.rect.height`.
* **Image Cropping Refinement:** Following up on the cropping fix, hardcoding the crop boundary to `page.rect.height` caused issues if the final source ended halfway down a page, leading to massive blocks of whitespace being included in the screenshot. Updated `process_source_sheets.py` to dynamically calculate the maximum Y-coordinate (`y1`) among all text blocks on the page. The script now crops perfectly at the bottom of the lowest text block (plus a 5-pixel padding), rather than going all the way to the page boundary.
