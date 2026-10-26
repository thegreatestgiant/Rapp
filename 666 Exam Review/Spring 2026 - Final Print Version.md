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
  .values
  .sort((a, b) => {
    const sA = String(a.subject || '');
    const sB = String(b.subject || '');
    if (sA !== sB) return sA.localeCompare(sB);
    const dA = (a.date || a.file.cday)?.toString() || '';
    const dB = (b.date || b.file.cday)?.toString() || '';
    if (dA !== dB) return dA.localeCompare(dB);
    return a.file.name.localeCompare(b.file.name);
  });

for (const page of pages) {
  dv.paragraph(`![[${page.file.name}]]`);
}
```
