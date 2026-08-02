# Features Added
- **Attachment Submodule Migration**: Wrote and executed a script to automatically scan all `Rapp` markdown files, track down their referenced image attachments from the global vault (e.g. `999 Attachments`), and safely migrate them into `000 School/Rapp/444 Attachments` while perfectly preserving git history and un-tracking them from the parent vault.

## 2026-08-02
- **Standalone `Rapp` Architecture**: Decoupled the Gemara parsing scripts and source Markdown notes from the main Obsidian vault. Packaged everything (Scripts, Sources, Authors, Source Sheets, Attachments) into a standalone Git repository named `Rapp`, which is now integrated as a submodule in the main Obsidian vault at `000 School/Rapp`.
- **Portable Script Paths**: Updated all Python scripts to calculate paths dynamically based on their parent directory (`RAPP_ROOT`), meaning the scripts will work seamlessly whether `Rapp` is cloned independently or as a submodule.
- **Robust Dataview Tagging**: Switched from relying on hardcoded folder paths for Dataview queries to using a dedicated `#gemara-source` tag.
- **Bulk Tag Updater**: Created and ran a script to recursively inject `#gemara-source` into the frontmatter of all existing `.md` files in `Sources/` so that historical notes immediately work with the new Dataview architecture.
