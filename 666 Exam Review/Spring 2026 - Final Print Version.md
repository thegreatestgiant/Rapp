---
season: "Spring"
year: "2026"
test_target: "Final"
---
```dataviewjs
const pages = dv.pages('"111 Source Sheets"')
  .where(p => p.season === dv.current().season 
           && p.year === dv.current().year 
           && p.test_target === dv.current().test_target)
  .sort(p => p.subject, 'asc');

for (const page of pages) {
  dv.paragraph(`![[${page.file.name}]]`);
}
```
