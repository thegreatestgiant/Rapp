---
season: "Fall"
year: "2026"
test_target: "Midterm"
---
# Fall 2026 — Midterm Exam Review

## Source Sheets

```dataview
TABLE
  subject as "Subject",
  default(date, file.cday) as "Date",
  file.link as "Source Sheet"
FROM "111 Source Sheets"
WHERE season = this.season AND year = this.year AND test_target = this.test_target
SORT subject ASC, default(date, file.cday) ASC, file.name ASC
```


## Print Version

To export all source sheets for this exam as a single PDF without any UI or tables, open [[Fall 2026 - Midterm Print Version]] and use the **Export to PDF** command.
