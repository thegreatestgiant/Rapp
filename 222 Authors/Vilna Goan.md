---
tags: [author]
---
# Vilna Goan

## Linked Sources
```dataview
TABLE book as Book, location as Location
FROM #gemara-source
WHERE contains(author, this.file.link)
SORT book ASC, location ASC
```
