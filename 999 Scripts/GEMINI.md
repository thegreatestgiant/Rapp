# Antigravity PDF Parser & Vault System Architecture

> [!important] CRITICAL SYSTEM INSTRUCTIONS
> 1. **Preserve User Notes**: NEVER overwrite existing source notes or user study annotations. Append new information under `> [!todo] Pending Edit Approval` at the bottom of the source note. If notes are ever displaced, restore immediately via Obsidian File Recovery snapshots or Git history.
> 2. **Dual Compatibility**: Any parser fix or script update MUST work for both existing vault notes and newly generated future notes.
> 3. **Audit Order of Operations**: When auditing, **first fix the sheets and vault files** so notes and embeds are immediately functional and clean, and **then fix the root issue in the scripts** (`process_source_sheets.py`) so future runs parse correctly out-of-the-box.
> 4. **Session Logging**: Document audit results and architectural updates in `Logs/` (e.g., `Logs/<Topic>_Audit.md` or `Logs/Bugs_Fixed.md`). Keep this file focused on enduring system rules and capabilities, not chronological logs.
> 5. **Git Safety**: Do not commit changes directly; the user reviews and commits all changes.

---

## Vault Architecture & Directory Structure
* `000 Source PDFs/`: Incoming Gemara source sheet PDFs to process.
* `111 Source Sheets/`: Master source sheets linking individual sources via block/headline embeds.
* `222 Authors/`: Canonical author index notes (named by author, e.g. `רב אפרים גרינבלט.md`, or famous Sefer for universally recognized figures like `חזון איש.md`).
* `333 Sources/`: Modular, reusable individual source notes (`Author - Book - Location.md`).
* `444 Attachments/`: High-resolution source screenshot crops (`.png`).
* `555 Vocabulary/`: Vocabulary and concept definitions.
* `666 Exam Review/`: Review sheets and summary notes.
* `888 Templates/`: Note templates (`Gemara Source.md`).
* `999 Scripts/`: Python automation engine (`process_source_sheets.py`, `Run PDF Parser.md`).
* `Logs/`: Dedicated audit records and bug fix documentation.

---

## Source Note & Sheet Conventions
1. **File Naming**: `[Author Name] - [Book Name] - [Location].md` (e.g., `רב אפרים גרינבלט - רבבות אפרים - ח''ד או''ח קפ''א.md`).
2. **2-Header Note Architecture**:
   - `### Source Image`: Contains the cropped image embed (`![[image.png]]`) at the top of the note. **Never embed this header in master sheets.**
   - `### [Author - Book - Location]` or `### [Dibur Hamatchil]`: Contains study notes. Master sheets embed **only** this heading: `![[Author - Book - Location#Author - Book - Location]]` (or `![[Author - Book - Location#DH]]`), keeping image crops hidden from the sheet.
3. **Link Updates**: Renaming any source file or headline requires updating all embed links across `111 Source Sheets/`.
4. **Metadata**: The YAML `author` field must be an internal wikilink to an author note in `222 Authors/` (not a book title), except for universally famous figures recognized by their primary Sefer (`חזון איש`, `חתם סופר`, `שולחן ערוך`, `משנה ברורה`, `מגן אברהם`).
5. **Mishnah Commentaries**: The Maseches belongs in the Book name (e.g., `תוספות יום טוב מסכת שבת`), with only the Perek/Mishnah in the Location (`פרק א משנה א`).
6. **Cleanup**: Always remove temporary testing files, dummy scripts, and scratch files.

---

## Parser Engine Architecture (`process_source_sheets.py`)
1. **Dual Text Decoding (`decode_text`)**:
   - Reverse QWERTY-to-Hebrew translation decodes Davka/Word font streams.
   - Smart English detection (`is_line_english()` using vowel ratio >=0.32, letter-comma anomaly checks, and rabbinic/academic keywords) protects legitimate English citations (e.g., Rav Yisroel Belsky, Aryeh Kaplan, Max Munk) from font scrambling.
2. **Citation Normalization & Author Mapping**:
   - `AUTHOR_CANONICAL_MAP`: Normalizes book titles, abbreviations, and honorific variations to canonical author files.
   - `RESPONSA_SPECIAL_MAP`: Maps responsa sefarim directly to their poskim (`שו"ת יחווה דעת` -> `רב עובדיה יוסף`, `שו"ת מנחת יצחק` -> `רבי יצחק יעקב וייס`, `שו"ת מנחת שלמה` -> `רבי שלמה זלמן אויערבאך`, `שו"ת הר צבי` -> `רב צבי פסח פרנק`).
   - `has_numbered_doc`: PDF-wide numbered header enforcement; suppresses false source triggers from body text keywords when the PDF is numbered.
   - Cleans dangling parentheses, Hebrew bullet prefixes (`ה - `), and prioritizes Midrash Rabbah regex over generic Tanach matching.
   - Scans horizontally across the Y-axis to reconnect orphaned numbers (`(2`) to Hebrew text headers.
3. **Component-Based Source Matching (`match_existing_source`)**:
   - Enforces strict exact matches on normalized author and final location token before allowing fuzzy matching on book titles, eliminating off-by-one false positives (`הלכה ח` vs `הלכה ט`).
4. **Dibur Hamatchil (DH) Extraction**:
   - Detects leading phrases terminated by periods/hyphens to create disambiguated subsection anchors for quotes from the same page.
5. **Dynamic Bounding Box Cropping**:
   - Uses PyMuPDF (`fitz`) to crop dynamically to the lowest text block on the page, eliminating excess whitespace when sources end early.

---

## Source Sheet Auditor Protocol
When auditing or fixing a master source sheet, adhere to a strict two-stage process: **first fix the sheets and vault files, and then fix the root issue in the scripts**.

### Stage 1: Fix the Sheets and Sources First
1. **Check for AI Audit Flags First**:
   - Immediately scan the sheet and source notes for active audit markers (`⚠️ (Needs Audit)` badges in the sheet, `audit_needed: true` or `#needs-audit` in frontmatter, `> [!warning] Audit Flag: Needs Verification` callouts).
   - Prioritize investigating and resolving these flagged sources first, clearing the flags and badges once verified and fixed.
2. **Identify All Sources**: Parse all embeds in the target sheet from `111 Source Sheets/`.
3. **Parallelize Subagents**: Use `invoke_subagent` to verify sources concurrently.
4. **Verify and Fix Each Source**:
   - Ensure author metadata links to a canonical author file in `222 Authors/` (not a book title).
   - Standardize source note filenames (`[Author] - [Book] - [Location].md`), headlines, and 2-header layout (`### Source Image` at top, study notes under content heading). Preserve any user study notes!
   - Ensure canonical author notes exist in `222 Authors/`.
   - Update embeds in `111 Source Sheets/` to match corrected filenames and headlines (`![[Author - Book - Location#Author - Book - Location]]`).
   - Confirm 0 broken links, 0 missing images, and clean embeds across the sheet.

### Stage 2: Fix the Root Cause in the Scripts
4. **Root-Cause Analysis & Script Patching**:
   - Only after all sheets and vault files are completely fixed and verified, trace systematic extraction errors back to `process_source_sheets.py` (e.g., missing author mappings in `AUTHOR_CANONICAL_MAP`, responsa handling in `RESPONSA_SPECIAL_MAP`, header regex, English font decoding, or crop boundaries).
   - Patch the Python script directly so future runs parse correctly automatically.
5. **Log Results**: Document the audit and script fixes in `Logs/<Topic>_Audit.md` (e.g., `Melachim_Audit.md`, `Two_Do_Audit.md`, `Tzitzis_Audit.md`, `Universe_Audit.md`, `Fixing_Lulav_and_Esrog_Audit.md`).
6. **Report Back**: Summarize all sources corrected on the sheet, followed by the script root cause patches implemented.

---

## Sheet Revision & Update Protocol (Rebbi Document Updates)
When a source sheet PDF is revised after initial study, execute the following protocol:

### 1. PDF File Ingestion & Consolidation
- Support both direct overwrite (`000 Source PDFs/<name>.pdf`) and browser download numbered duplicates (`<name> (1).pdf`).
- When `<name> (1).pdf` is supplied, identify target base `<name>`. Compare and process against `<name>`, replace the old `<name>.pdf` with the updated content, and delete `<name> (1).pdf`.
- **Enforce Single File Invariant**: At the end of the update, only the single updated `000 Source PDFs/<name>.pdf` must exist in the vault.

### 2. Diffing & Source Classification
- Compare newly extracted sources against the existing `111 Source Sheets/<name>.md`:
  - **Added (🟢)**: New sources appearing in the revision.
  - **Unchanged (⚪)**: Identical author, book, and location.
  - **Modified (🟡)**: Changed crop boundaries or corrected citation/Daf.
  - **Omitted (🔴)**: Present in previous sheet, omitted in the new PDF.

### 3. Note Preservation & Reconciliation
- **Zero Data Loss**: Existing notes beneath the main header in `333 Sources/` must never be wiped or overwritten.
- **Citations Corrected**: When a citation is adjusted, rename the existing note file and header to match the new citation; update embeds in the sheet so existing user study notes follow the source. Never create a blank new note leaving the previous notes stranded.
- **Image Crops Updated**: Only modify or append content inside the `### Source Image` block. Never disturb user notes below it.
- **Omitted Sources Kept**: Do NOT delete omitted source notes from `333 Sources/`. Move their embed links on the master sheet into a bottom section:
  ```markdown
  ---
  ## 📦 Omitted by Rebbi (From Previous Revision)
  > [!note] These sources were removed by the Rebbi in the updated PDF, but are preserved here because they contain your study notes.
  ### [Old #X] ![[Author - Book - Location#Author - Book - Location]]
  ```

### 4. Renumbering & Shiur Prep Brief
- Update sequence numbers (`## 1`, `## 2`, etc.) on the master sheet to match the new PDF order.
- Mark new sources temporarily with `🆕` (e.g. `## 3 🆕`).
- Produce a concise Shiur Prep Brief:
  - Mapping table (`Old #` $\to$ `New #`) showing what shifted, what was added (🟢), and what was omitted (🔴).
  - Bullet points of newly added sources requiring preparation before shiur.

