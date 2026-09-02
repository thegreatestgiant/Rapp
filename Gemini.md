# Gemini Learnings and Rules

## Source File Conventions
When fixing or creating source files, the following conventions must be adhered to in order to keep the vault organized and links intact:

1. **File Naming Convention**: `[Author Name] - [Book Name] - [Location].md`
   *(Example: `רב אפרים גרינבלט - רבבות אפרים - ח''ד או''ח קפ''א.md`)*
2. **Headline Convention**: The main headline inside the source file must match the file name exactly.
   *(Example: `### רב אפרים גרינבלט - רבבות אפרים - ח''ד או''ח קפ''א`)*
3. **Link Updates**: If a source file is renamed or its headline is modified, any embed links in Source Sheets (e.g., `111 Source Sheets/`) must be updated to match the new file name and headline.
   *(Format: `![[Author - Book - Location#Author - Book - Location]]`)*
4. **Metadata**: The YAML frontmatter and DataView fields inside the source file must accurately reflect the Author and Book. The `author` field must link to the author's file (not the book file).
5. **Author Files**: Author files in the `222 Authors` folder should be named after the actual author (e.g., `רב אפרים גרינבלט.md`), not the title of their book (e.g., *not* `רבבות אפרים.md`).

## Source Sheet Auditor Protocol

When the user asks you to "audit", "check", or "fix" a Source Sheet, you must automatically execute the following protocol:

1. **Read the Source Sheet**: Identify every source embedded in the sheet (e.g., links formatted like `![[Author - Book - Location#Author - Book - Location]]`).
2. **Spawn Subagents**: For each source, spawn a subagent (using `invoke_subagent` with a lightweight model if possible, or handle them directly if there are only a few) to verify the source.
3. **Verification Steps per Source**:
   - Check if the author metadata in the source file points to a real author, not a book title. Cross-reference this by doing a web search for the book to find the actual author.
   - Cross-reference the author with existing authors in the `222 Authors/` folder to maintain consistent naming conventions.
   - If the author or book is wrong, update the source file's metadata, its internal headline, and rename the file according to the `[Author Name] - [Book Name] - [Location].md` convention.
   - Verify that an author file exists in `222 Authors/` and is named after the person, updating or renaming it if necessary.
   - Update the original Source Sheet link to reflect the corrected filename and headline.
4. **Report Back**: Once all subagents have completed their checks and fixes, provide a summarized report of all the sources that were corrected.

## Scripting and PDF Parsing Guidelines

When making changes to the Python scripts, the PDF parser workflow, or any files inside the `999 Scripts/` directory, you **must** read and adhere to the architectural guidelines and rules documented in `999 Scripts/GEMINI.md`.
