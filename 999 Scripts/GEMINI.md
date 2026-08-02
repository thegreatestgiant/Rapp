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

*See `Logs/Bugs_Fixed.md`, `Logs/Features_Added.md`, and `Logs/Architectural_Decisions.md` for a detailed breakdown of these updates.*

## Next Steps for WSL
1. **Refine the PDF Parsing Heuristic:** The current regex/logic in `extract_sources_and_images()` in `process_source_sheets.py` still uses placeholder logic for detecting the headers. We need to feed the script a real PDF from `000 Source PDFs/` and adjust the text search so the script correctly identifies citations and draws accurate bounding boxes for the images.
