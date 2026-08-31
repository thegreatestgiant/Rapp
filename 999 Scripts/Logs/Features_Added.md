# Features Added
- **Attachment Submodule Migration**: Wrote and executed a script to automatically scan all `Rapp` markdown files, track down their referenced image attachments from the global vault (e.g. `999 Attachments`), and safely migrate them into `000 School/Rapp/444 Attachments` while perfectly preserving git history and un-tracking them from the parent vault.

## 2026-08-02
- **Standalone `Rapp` Architecture**: Decoupled the Gemara parsing scripts and source Markdown notes from the main Obsidian vault. Packaged everything (Scripts, Sources, Authors, Source Sheets, Attachments) into a standalone Git repository named `Rapp`, which is now integrated as a submodule in the main Obsidian vault at `000 School/Rapp`.
- **Portable Script Paths**: Updated all Python scripts to calculate paths dynamically based on their parent directory (`RAPP_ROOT`), meaning the scripts will work seamlessly whether `Rapp` is cloned independently or as a submodule.
- **Robust Dataview Tagging**: Switched from relying on hardcoded folder paths for Dataview queries to using a dedicated `#gemara-source` tag.
- **Bulk Tag Updater**: Created and ran a script to recursively inject `#gemara-source` into the frontmatter of all existing `.md` files in `Sources/` so that historical notes immediately work with the new Dataview architecture.

## 2026-08-31
- **Automated Source Sheet Opening & Cleanup**: Updated the `Run PDF Parser.md` Templater script to automatically parse the python script output, locate the newly generated Master Source Sheet, and open it directly in Obsidian. Added auto-cleanup logic to seamlessly delete the empty "Untitled" file left behind by QuickAdd triggers, whether the script succeeds or the user cancels.
- **Improved Author Recognition**: Upgraded the `process_source_sheets.py` parser to dynamically load all known authors directly from the `222 Authors` directory rather than relying on a hardcoded list. Enhanced the citation parsing algorithm to:
  - Correctly decode Hebrew quotation marks from the PDF font stream (resolving `\x1b` issues).
  - Normalize double quotes and intelligently match the *earliest* occurring known author in a citation string.
  - Appropriately fallback for common prefixes like `שו"ת`, `ספר`, `חידושי`, `דרוש`, `חלקת`, etc., to capture multi-word authors that aren't yet in the vault.
  - Successfully extract complex authors like `רא"ש`, `ריטב"א`, `רשב"א`, `תוספות`, `הר"ן`, `חלקת יואב`, `רבבות אפרים`, and `הר צבי`.
- **Dibur Hamatchil Extraction**: Added a powerful new heuristic to `extract_sources_and_images()` in `process_source_sheets.py`. When parsing PDF text blocks, the script now actively reads the contents of the *next* block immediately following a source header. If it detects a classic *Dibur Hamatchil* pattern (e.g., a short phrase ending with a hyphen `-` or a period `.`), it dynamically extracts those words. 
  - The script now automatically injects this *Dibur Hamatchil* as a specific `#Heading` anchor when constructing the `![[Note#Heading]]` links in the generated Source Sheet. 
  - This completely solves the issue of duplicate sources on the same page (e.g., quoting two different Rashi comments from `דף כט עמוד ב`) by automatically linking to their specific subsections (e.g., `#אבל לא במדינה` and `#אלא ביבנה`), eliminating the need for manual link editing.
- **PDF Link in Source Sheets**: Updated `process_source_sheets.py` so the generated Master Source Sheet markdown file explicitly renders a wikilink to the original PDF file right beneath the title `[[{pdf_source}]]`, restoring easy navigation to the raw document.
