# Antigravity Session Handoff Summary

> [!important] CRITICAL SYSTEM INSTRUCTION
> Before finishing any task or ending a session, you **MUST** document all changes, bugs fixed, and architectural decisions in the `Logs/` directory and update the `Current Progress` section in this file (`GEMINI.md`). You are encouraged to use and create multiple `.md` files inside `Logs/` (e.g., `Bugs_Fixed.md`, `Features_Added.md`, `Architectural_Decisions.md`) to save a comprehensive record of your work.
> 
> **CRITICAL REQUIREMENT:** Any solution or fix you implement MUST work for BOTH existing files and newly generated future files (e.g., if you fix a query, you must also update the Python template that generates future files).
## Context & Goal
We designed an automated workflow to process Gemara Source Sheet PDFs dropped into the Obsidian vault. The goal is to detect sources inside the PDF, extract them as image screenshots, intelligently match them against existing Obsidian vault sources, create new sources/authors if they are missing, and generate a master Source Sheet note linking them all together.

## Architecture
* **Input Folder:** `000 School/Rapp/000 Source PDFs/`
* **Output Folders:** `111 Source Sheets/` (Master sheet), `333 Sources/` (Individual source notes), `222 Authors/` (Author indexes), `444 Attachments/` (Cropped images).
* **Execution:** A Python script triggered manually or via an Obsidian shortcut (e.g. Templater `tp.user.system` or Shell Commands) using `Run PDF Parser.md`. 

## Rules & Safety
1. **Never overwrite existing sources directly.** Instead, append new information (like new screenshots) under a `> [!todo] Pending Edit Approval` block at the bottom of the existing source note.
2. **Template Adherence:** Ensure new source notes strictly follow the `Gemara Source.md` frontmatter and formatting.
3. **Screenshots over Text:** The Python script uses `PyMuPDF` (`fitz`) to crop the source's bounding box and saves it to `999 Attachments/` as an image, rather than relying on extracted text which can be messy.
4. **Source File Conventions:** 
    - Naming convention: `Author - Book - Location.md`
    - Headline convention: The main `###` headline inside the source must exactly match the file name.
    - Author Links: Author metadata must point to an actual author in `222 Authors` (named after the person, e.g., `רב אפרים גרינבלט.md`), not a book title.
    - Sheet Links: Embed links in Source Sheets must always use `![[Author - Book - Location#Author - Book - Location]]` to point directly to the headline.
5. **Cleanup Test Files:** Always clean up any test scripts, dummy outputs, or temporary testing files (e.g., `test.py`) that were created during your workflow once you are done with them.

## Current Progress
1. Created the `Scripts/` folder and initial architecture.
2. Migrated the Gemara workflow into a standalone Git repository (`Rapp`), and integrated it back into the main vault as a submodule (`000 School/Rapp`).
3. Decoupled all Python script paths and attachment destinations so they point to the `Rapp` root natively.
4. Refactored Dataview queries to use the `#gemara-source` tag instead of hardcoded folder paths for maximum portability.
5. Fixed critical parsing bugs in `process_source_sheets.py` related to author name matching order, fallback logic, and overlapping PDF rects.
6. Rewrote Git history to permanently purge `.venv` and `.tmp.drive*` directories to prevent rebase locks.
7. Purged `.obsidian/workspace.json` from git history across the entire parent vault to resolve annoying git changes.
8. Documented that Obsidian Dataview cache drops new files pulled via git submodule, requiring an application restart (`Ctrl+R`) to re-index the tags. Validated that `author: "[[Link]]"` is properly supported as a link object natively in Obsidian 1.4+ Properties.
9. Fixed folder paths in auxiliary scripts (`clean_pending_edits.py`, `scratch.py`, `scratch_match.py`) to align with the new numbered directory structure (`333 Sources`, etc.).
10. Updated the `Run PDF Parser.md` Templater script to point to the correct `Rapp` directories for PDFs and sheets, and updated the WSL python call to use `../.venv/bin/python`.
11. Copied the `.obsidian` folder from the main vault into the `Rapp` folder to allow testing as a standalone vault.
12. Updated `Run PDF Parser.md` so it automatically opens the generated Source Sheet after processing, and cleanly deletes any empty "Untitled" files left behind by QuickAdd executions or cancellations.
13. Overhauled the citation matching engine in `process_source_sheets.py` to dynamically load known authors from the `222 Authors` folder, resolve font-encoding glitches with quotation marks, and implement positional string matching. It now flawlessly identifies complex authors like `רא"ש`, `ריטב"א`, `הר"ן`, `רבבות אפרים`, and `הר צבי` even if they have prefixes like `שו"ת` or `חידושי`.
14. Fixed a critical fuzzy-matching false positive bug in `process_source_sheets.py`. Upgraded the `match_existing_source` logic from basic full-string fuzzy matching to a strict component-based architecture. This prevents off-by-one errors (e.g. `הלכה ט` incorrectly matching `הלכה ח`) by verifying that the normalized author and the final location token match exactly before permitting fuzzy matching on the book title.
15. Developed an automated *Dibur Hamatchil* (DH) extraction heuristic in `process_source_sheets.py`. The parser now reads the raw text stream immediately following citations in the PDF to detect leading phrases terminated by hyphens or periods. It leverages these extracted phrases to automatically generate specific subsection anchors (e.g., `![[רש''י...#אבל לא במדינה]]`), perfectly disambiguating multiple quotes from the same page source.
16. Re-added the explicit wikilink to the original PDF directly beneath the top-level `# Heading` in generated Master Source Sheets.
17. Fixed a PyMuPDF text block splitting bug in `process_source_sheets.py` where isolated numbers (e.g., `(2`) disconnected from their Hebrew text caused the parser to fallback to `מקור - מקור`. The parser now scans horizontally across the Y-axis to reconnect orphaned text chunks back to their numerical headers before parsing.
18. Resolved single-letter author false extraction for `ר' עובדיה מברטנורא` / `ר׳ עובדיה מברטנורא` / `ברטנורא` in `process_source_sheets.py`, mapping them canonically to `רבי עובדיה מברטנורא` with `מסכת שבת` as the book, and fixed bad fallback parsing on single-letter honorifics. Audited and updated existing source, author file, and source sheet.

*See `Logs/Bugs_Fixed.md`, `Logs/Features_Added.md`, and `Logs/Architectural_Decisions.md` for a detailed breakdown of these updates.*

## Next Steps for WSL
1. **Refine the PDF Parsing Heuristic:** The current regex/logic in `extract_sources_and_images()` in `process_source_sheets.py` still uses placeholder logic for detecting the headers. We need to feed the script a real PDF from `000 Source PDFs/` and adjust the text search so the script correctly identifies citations and draws accurate bounding boxes for the images.
