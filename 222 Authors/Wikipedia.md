---
aliases: [ויקיפדיה, Wikipedia]
tags: [author]
---
# Wikipedia

## Background Info
The multilingual online encyclopedia. Used for historical, geographical, and background reference material cited in source sheets.

## Linked Sources
```dataview
TABLE book as Book, location as Location
WHERE contains(string(author), this.file.name)
SORT book ASC, location ASC
```
