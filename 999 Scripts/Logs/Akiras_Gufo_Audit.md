# Audit: akiras gufo

**Date**: 2026-10-19
**Sheet**: `111 Source Sheets/akiras gufo.md`
**Sources audited**: 9 (1 flagged → cleared; 8 verified healthy)

## Flagged Source

| # | Old File | Author | Book | Location | Result |
|---|---|---|---|---|---|
| 9 | `שו''ת בצל - החכמה חלק ו - סימן יב` | [[בצלאל שטרן]] | שו''ת בצל החכמה | חלק ו סימן יב | 🔄 Re-attributed & Badge Cleared |

### Source 9 — Root cause & fix
- **Flag**: `Author fell back to token 'שו"ת בצל'` — the parser saw the responsa title
  *Bazel ha-Chachma* and, lacking a known-author mapping, stored the truncated title
  token `שו''ת בצל` as a **person-author** note (`222 Authors/שו''ת בצל.md`).
- **Verification**:
  - Decoded footnote 10 of `000 Source PDFs/akiras gufo.pdf` (visual-order Hebrew):
    `שו"ת בצל החכמה חלק ו סימן יב` — confirms sefer/part/siman.
  - External citations consistently attribute *שו"ת בצל החכמה* to **הרב בצלאל שטרן**,
    Rav of Vienna.
- **Vault changes**:
  - Renamed source note → `333 Sources/בצלאל שטרן - שו''ת בצל החכמה - חלק ו סימן יב.md`
    (matches `Author - Book - Location` convention; `book`/`location` split aligned
    with e.g. `שו''ת מנחת שלמה` notes and script output).
  - Frontmatter now `author: "[[בצלאל שטרן]]"`; `needs-audit` tag, `audit_needed`,
    `audit_reason`, and the `[!warning]` audit callout all removed.
  - Created `222 Authors/בצלאל שטרן.md` (with aliases incl. sefer titles).
  - Deleted erroneous author note `222 Authors/שו''ת בצל.md` (zero references remained).
  - Sheet: badge `## 9 ⚠️ (Needs Audit)` → `## 9`, embed updated to new file+heading.

## Script patch (`999 Scripts/process_source_sheets.py`)
Root cause fixed so future runs don't regress:
- `AUTHOR_CANONICAL_MAP`: added `שו"ת בצל`, `שו''ת בצל`, `בצל החכמה`,
  `שו"ת בצל החכמה`, `שו''ת בצל החכמה` → `בצלאל שטרן`.
- `RESPONSA_SPECIAL_MAP`: added `בצל החכמה` → (`בצלאל שטרן`, `שו"ת בצל החכמה`),
  so `parse_citation` yields `(בצלאל שטרן, שו"ת בצל החכמה, חלק ו סימן יב)` with no audit flag.
- Verified: compiles; test parses `שו"ת בצל החכמה חלק ו סימן יב` correctly.

## Verification (all 9 sources)
- ✅ Every embed target file exists in `333 Sources/`.
- ✅ Every `#fragment` matches an actual heading in its source note.
- ✅ Every `author` resolves to an existing `222 Authors/` note.
- ✅ Every source image exists in `444 Attachments/`.
- ✅ No `needs-audit` flags remain; no orphan references to old file/author names.
- Note: source #6 also embeds two `mesayaiya` images (cross-sheet crops) — both exist.

## Not committed
Changes left uncommitted for review. Suggested commit message:
`🧐 Gemara - Akiras Gufo`
