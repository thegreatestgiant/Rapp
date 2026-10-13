# Gemini Learnings and Rules

## General Workflow

1. **Parallelize Independent Tasks**: If there is a batch of tasks to run and they are not sequential (i.e., they do not rely on the output of the previous task), you must break them up and delegate them to multiple subagents concurrently using the `invoke_subagent` tool. Do not execute them sequentially yourself.

## Source File Conventions
When fixing or creating source files, the following conventions must be adhered to in order to keep the vault organized and links intact:

1. **File Naming Convention**: `[Author Name] - [Book Name] - [Location].md`
   *(Example: `רב אפרים גרינבלט - רבבות אפרים - ח''ד או''ח קפ''א.md`)*
2. **Headline Convention**: The main headline inside the source file must match the file name exactly.
   *(Example: `### רב אפרים גרינבלט - רבבות אפרים - ח''ד או''ח קפ''א`)*
3. **Link Updates**: If a source file is renamed or its headline is modified, any embed links in Source Sheets (e.g., `111 Source Sheets/`) must be updated to match the new file name and headline.
   *(Format: `![[Author - Book - Location#Author - Book - Location]]`)*
4. **Metadata**: The YAML frontmatter and DataView fields inside the source file must accurately reflect the Author and Book. The `author` field must link to the author's file (not the book file).
5. **Author Files**: Author files in the `222 Authors` folder should generally be named after the actual author (e.g., `רב אפרים גרינבלט.md`). However, for extremely famous Rabbis who are universally known by their primary Sefer (e.g., `חזון איש`, `חתם סופר`, `שולחן ערוך`, `משנה ברורה`, `מגן אברהם`), it is preferred to use the Sefer name as the Author name to match common colloquial usage.
6. **Mishnah Commentaries**: For Mishnah commentaries (e.g., Bartenura, Tosafos Yom Tov, Rambam Peirush Hamishnah), the Maseches (tractate) should be included as part of the Book name rather than the Location. For example: Book: `תוספות יום טוב מסכת שבת` and Location: `פרק א משנה א`.
7. **Source Image Section**: The cropped PDF image MUST be placed under a `### Source Image` heading at the top of the file, BEFORE the main `### Title` (or Dibur Hamatchil) heading containing the notes. The `### Source Image` heading MUST NEVER be embedded or linked to in the master source sheet. Master source sheets should ONLY embed the title/DH heading (e.g., `![[File#Title]]`), intentionally ignoring and hiding the image from the sheet.

## Source Sheet Auditor Protocol

When the user asks you to "audit", "check", or "fix" a Source Sheet, you must strictly follow this two-stage order of operations: **first fix the sheets and vault files, and then fix the root issue in the scripts**.

### Stage 1: Fix the Sheets and Sources First
1. **Check for Flagged Sources First**:
   - Immediately scan the sheet and vault for any sources marked for AI audit:
     - Badges in the master sheet: `⚠️ (Needs Audit)`
     - Frontmatter: `audit_needed: true`
     - Tags: `#needs-audit`
     - Callouts: `> [!warning] Audit Flag: Needs Verification`
   - Prioritize investigating and resolving these flagged sources first, clearing the flags once verified and fixed.
2. **Read the Full Source Sheet**: Identify all sources embedded in the sheet (e.g., links formatted like `![[Author - Book - Location#Author - Book - Location]]`).
3. **Spawn Subagents**: For each source, spawn a subagent (using `invoke_subagent` with a lightweight model if possible, or handle them directly if there are only a few) to verify and fix the source.
4. **Verification & Vault Fixes per Source**:
   - Check if the author metadata in the source file points to a real author, not a book title. Cross-reference this by doing a web search for the book to find the actual author.
   - Cross-reference the author with existing authors in the `222 Authors/` folder to maintain consistent naming conventions.
   - If the author or book is wrong, update the source file's metadata, its internal headline, and rename the file according to the `[Author Name] - [Book Name] - [Location].md` convention. Preserve any existing user study notes!
   - Verify that an author file exists in `222 Authors/` and is named after the person, updating or creating it if necessary.
   - Update the original Source Sheet link to reflect the corrected filename and headline.
   - Ensure the sheet has 0 broken links, 0 missing images, and clean embeds.

### Stage 2: Fix the Root Cause in the Scripts
4. **Root Cause Patching**: Only after the sheet and all its sources are completely fixed and verified in the vault, identify any systematic parsing errors that caused the issues (e.g., misinterpreting an honorific like `ר'`, unmapped books/responsa, flawed header regex, or mangled English text). Trace the bug to the Python parser (`999 Scripts/process_source_sheets.py`) and patch the script directly so it parses correctly next time.
5. **Document in Logs**: Record all audit findings, vault corrections, and script patches in the `Logs/` folder (e.g., `Logs/<Topic>_Audit.md`).
6. **Report Back**: Provide a summarized report of all sources corrected on the sheet, followed by the script root cause patches implemented.

## Scripting and PDF Parsing Guidelines

When making changes to the Python scripts, the PDF parser workflow, or any files inside the `999 Scripts/` directory, you **must** read and adhere to the architectural guidelines and rules documented in `999 Scripts/GEMINI.md`.

## Sheet Update Protocol (Rebbi Document Revisions)

When a Rebbi updates or revises a source sheet after the user has already studied and taken notes on it, adhere strictly to this protocol:

### 1. Ingestion & File Cleanup
- **Accepted Ingestion Formats**: The updated PDF may arrive either with the **exact same name** (overwriting `000 Source PDFs/<name>.pdf`) or with browser download numbering like **`<name> (1).pdf`**.
- **Consolidation**: If `<name> (1).pdf` is provided, compare and process against `<name>`, then replace `<name>.pdf` with the updated file and delete the `(1)` file. **Only the single updated `<name>.pdf` must exist at the end**.

### 2. Zero-Loss Note Reconciliation
- **Preserve Existing Notes**: User notes under `### [Heading]` in `333 Sources/` and custom text on master sheets must never be overwritten or deleted.
- **Classification & Triage**:
  - 🟢 **Added Sources**: Parse and create new notes in `333 Sources/`. In the master sheet, temporarily badge as `## X 🆕` for quick identification.
  - ⚪ **Unchanged Sources**: Leave the source note completely untouched.
  - 🟡 **Modified Crops**: Update or append only the image link under `### Source Image`. Never alter text below the main study heading.
  - 🟡 **Corrected Citations**: If the Rebbi modified a source's citation (e.g., changed Daf or Sefer title), rename the existing file and its internal headline so existing study notes travel with the source; update the embed link on the sheet. Do NOT create an empty new note leaving the annotated note orphaned.
  - 🔴 **Dropped/Removed Sources**: **NEVER delete the source note file from `333 Sources/`** (to protect previous learning). In the master sheet, move it to a dedicated section at the bottom:
    ```markdown
    ---
    ## 📦 Omitted by Rebbi (From Previous Revision)
    > [!note] These sources were removed by the Rebbi in the updated PDF, but are preserved here because they contain your study notes.
    ### [Old #X] ![[Author - Book - Location#Author - Book - Location]]
    ```

### 3. Renumbering & Shiur Prep Brief
- Update the master sheet sequence numbers (`## 1`, `## 2`, etc.) to match the Rebbi's revised order.
- Always present the user with a concise **Shiur Prep Brief** containing:
  1. A mapping table (`Old #` $\to$ `New #`) showing what shifted, what was added (🟢), and what was omitted (🔴).
  2. A bulleted list of newly added sources that need preparation before shiur.

## Git Commits
- **Do not commit changes yourself**: The user will review and commit all changes.

