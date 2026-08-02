# Architectural Decisions

## 2026-08-02
- **Submodule `Rapp` Repository**: Decided to convert the Gemara workflow into an independent, standalone Git repository (`Rapp`) and include it as a submodule within the main Obsidian vault. This ensures the workflow and its data (PDFs, Source Sheets, Notes, Scripts) are fully encapsulated and portable.
- **Local Attachments**: Decided that `process_source_sheets.py` will save cropped image screenshots to `Rapp/Attachments/` rather than the main vault's `999 Attachments` folder. This guarantees that cloning `Rapp` independently will not result in broken image embeds.
- **Tag-Based Dataview Queries**: Decided to use a universal `#gemara-source` tag instead of absolute folder paths in Dataview queries (e.g. `FROM #gemara-source`). This prevents Dataview queries from breaking when the folder hierarchy changes (i.e., whether the folder is at the root of an independent vault or nested in `000 School/Rapp` inside the main vault).
