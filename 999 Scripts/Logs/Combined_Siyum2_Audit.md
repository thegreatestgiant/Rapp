# Combined Siyum 2 Audit

**Date**: 2026-10-19
**Sheet**: `111 Source Sheets/combined siyum.md` (source PDFs: `combined siyum.pdf`, `combined siyum2.pdf`)
**Sources audited**: 11 (7 newly imported from `combined siyum2.pdf` → cleared; 4 pre-existing verified)

## Summary

`combined siyum2.pdf` was processed and its new sources were merged into the
existing `combined siyum` sheet. The parser had fallen back to sefer-title
tokens as authors (`שו"ת יעלת`, `אגרות`, `הערות`, `מועדי`, `צפנת`, `ספר נפש`,
`שו"ת קנין`, `חזון`) and had mis-cropped several source images. All were
corrected against the cropped headers and cross-referenced with `222 Authors/`.

## Sources Corrected

| # | Old note | Author (fixed) | Book | Location |
|---|---|---|---|---|
| 2 | `ראובן מרגליות - חיה מרגליות או''ח …` | [[ראובן מרגליות]] | נפש חיה | או''ח סימן תקנ''א דף נ''ז |
| 4 | `אברהם דויד הורוויץ - תורה בהלכה …` | [[אברהם דויד הורוויץ]] | קנין תורה בהלכה | ה נ''ב |
| 5 | `צפנת פנחס - פרשת תרומה` | [[המהרי''ט]] | צפנת פענח | פרשת תרומה |
| 6 | `אגרות קודש - כרך ד - מכתב תתסט` | [[הרבי מליובאוויטש]] | אגרות קודש | כרך ד מכתב תתסט |
| 7 | `רש''ב ולדנברג - הערות - בסוף הספר` | [[רש''ב ולדנברג]] | הערות | בסוף הספר |
| 8 | `שו''ת יעלת חן - …` | [[רבי אריה ליב צינץ]] | שו''ת יעלת חן | ח''א חו''מ סימן כ''א |
| 10 | `מועדי הגר''ח - …` | [[הרב חיים קניבסקי]] | מועדי הגר''ח | ח''א תשובה ל''ו |
| 11 | `שו''ת מישרים אהבוך - …` | [[ישי מזלומין]] | שו''ת מישרים אהבוך | חלק ד תשובה לא |

Sources 1, 3, 9 were verified healthy and left unchanged (`שלמה קלוגר`, `ט''ז`,
`חזון עובדיה`).

### Root cause & fixes
- **Author-as-sefer fallback**: the parser lacked canonical mappings for these
  sefarim, so it stored the sefer title as a *person-author* note. Converted to
  the canonical posek/mechaber per the vault convention.
- **Image mis-mapping**: `אגרות קודש` pointed at the `נחלה לישראל` crop
  (`p1_s3`; corrected to `p1_s4`), and `רש''ב ולדנברג` pointed at the
  `מישרים אהבוך` crop (`p2_s6`; corrected to `p2_s2`).
- **Wrong author bio**: `222 Authors/המהרי''ט.md` described Rabbi Yosef Tzvi
  Dushinsky (mistaking *צפנת פענח* for the Dushinsky *צפנת פנחס*). The header
  reads *צפנת פענח להמהרי''ט*, i.e. the Maharit = **רבי יוסף טראני**; bio
  replaced.

## Vault Changes
- Renamed 7 source notes in `333 Sources/` to `Author - Book - Location`.
- Updated all 11 embeds in `111 Source Sheets/combined siyum.md`.
- Created author notes: [[רבי אריה ליב צינץ]], [[הרב חיים קניבסקי]], [[ישי מזלומין]].
- Fixed [[המהרי''ט]] author note.
- Removed parser fallback/obsolete author notes and duplicate source notes
  (`אגרות`, `אגרות קודש`, `הערות`, `חזון`, `מועדי`, `מועדי הגר''ח`, `ספר נפש`,
  `צפנת`, `שאלות`, `שו''ת יעלת`, `שו''ת יעלת חן`, `שו''ת מישרים אהבוך`,
  `שו''ת קנין`, plus the ill-named duplicate source files).
- Removed the redundant auto-generated `111 Source Sheets/combined siyum2.md`.
- Verified: 11/11 embeds resolve, headings match, all source images exist,
  0 `needs-audit` flags remain in `333 Sources/`.

## Script Notes
- Added canonical mappings to `process_source_sheets.py`:
  - `AUTHOR_CANONICAL_MAP`: `צפנת פענח/פנעח`→המהרי''ט, `נפש חיה`→ראובן מרגליות,
    `קנין תורה בהלכה`→אברהם דויד הורוויץ, `אגרות קודש`→הרבי מליובאוויטש,
    `יעלת חן`→רבי אריה ליב צינץ, `מועדי הגר"ח`→הרב חיים קניבסקי,
    `מישרים אהבוך`→ישי מזלומין, `רש"ב ולדנברג`, `חזון עובדיה`.
  - `RESPONSA_SPECIAL_MAP`: `יעלת חן`, `קנין תורה בהלכה`, `מישרים אהבוך`.
- Verified `parse_citation` now returns the canonical authors with no audit flag
  for these headers.

## Open Items
- `000 Source PDFs/combined siyum.pdf` and `combined siyum2.pdf` coexist; per the
  Sheet Revision protocol the revision would normally be consolidated to a single
  base PDF. Left as-is (both referenced by the sheet) pending user confirmation.
- `שו''ת מישרים אהבוך` author (`ישי מזלומין`) is a best-effort attribution from
  the catalogue; worth a spot-check.
