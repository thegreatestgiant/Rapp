<%*
// Find Rapp root by looking for a folder whose name ends with "Source PDFs" (ignoring numeric prefix)
const allFolders = app.vault.getAllLoadedFiles().filter(f => f.children);
const sourcePdfFolder = allFolders.find(f => f.name.replace(/^\d+\s*/, '') === 'Source PDFs');
const rappRoot = (sourcePdfFolder && sourcePdfFolder.parent.path !== "/") ? sourcePdfFolder.parent.path : '';
function rappPath(subpath) {
  return rappRoot ? `${rappRoot}/${subpath}` : subpath;
}

function getAcademicMetadata() {
  const now = new Date();
  const month = now.getMonth() + 1;
  const day = now.getDate();
  let year = now.getFullYear();
  let season, testTarget;
  
  if (month === 1 && day < 15) {
    season = 'Fall'; year = year - 1; testTarget = 'Final';
  } else if (month < 6 || (month === 6 && day < 15)) {
    season = 'Spring';
    testTarget = (month < 4) ? 'Midterm' : 'Final';
  } else {
    season = 'Fall';
    testTarget = (month < 11 || (month === 11 && day < 20)) ? 'Midterm' : 'Final';
  }
  
  return { season, year: String(year), testTarget };
}

// Load config from the Rapp root
const configFile = app.vault.getAbstractFileByPath(rappPath('config.json'));
let config = { subjects: ['Gemara', 'Halacha', 'Navi', 'Ikarim'], seasons: ['Spring', 'Fall'], test_types: ['Final', 'Midterm'] };
if (configFile) {
  try {
    config = JSON.parse(await app.vault.read(configFile));
  } catch(e) { console.error('Failed to load config.json:', e); }
}

// --- STEP 1: DEFINE ARCHITECTURE ---
const basePath = rappPath("333 Sources");
const authorsPath = rappPath("222 Authors");

// Ensure base folders exist
if (rappRoot && !app.vault.getAbstractFileByPath(rappRoot)) await app.vault.createFolder(rappRoot);
if (!app.vault.getAbstractFileByPath(basePath)) await app.vault.createFolder(basePath);
if (!app.vault.getAbstractFileByPath(authorsPath)) await app.vault.createFolder(authorsPath);

// --- STEP 2: GET OR CREATE AUTHOR ---
let authorFiles = app.vault.getAbstractFileByPath(authorsPath).children;
let authorNames = authorFiles.map(f => f.basename).sort();
authorNames.unshift("[ ➕ Add New Author ]"); 

let selectedAuthor = await tp.system.suggester(authorNames, authorNames, false, "Select Author");
if (!selectedAuthor) return;

if (selectedAuthor === "[ ➕ Add New Author ]") {
    let rawAuthor = await tp.system.prompt("Enter new Author name:");
    if (!rawAuthor) return;
    
    // CRITICAL FIX: Convert " to '' instantly so file creation doesn't crash
    selectedAuthor = rawAuthor.replace(/"/g, "''").replace(/[:\\/|?*<>]/g, '-');
    
    let authorTemplate = `---
tags: [author]
---
# ${selectedAuthor}

## Background Info

## Linked Sources
\`\`\`dataview
TABLE book as Book, location as Location
FROM "${rappPath("333 Sources")}"
WHERE contains(author, this.file.link)
SORT book ASC, location ASC
\`\`\`
`;
    await app.vault.create(`${authorsPath}/${selectedAuthor}.md`, authorTemplate);
}

// --- STEP 3: SMART SORT BOOKS ---
let allFiles = app.vault.getMarkdownFiles().filter(f => f.path.startsWith(basePath));
let authorBooks = new Set();
let otherBooks = new Set();

for (let file of allFiles) {
    let cache = app.metadataCache.getFileCache(file);
    if (cache && cache.frontmatter && cache.frontmatter.book) {
        let bookName = cache.frontmatter.book;
        let fileAuthor = cache.frontmatter.author || "";
        if (fileAuthor.includes(selectedAuthor)) {
            authorBooks.add(bookName);
        } else {
            otherBooks.add(bookName);
        }
    }
}

let sortedBooks = Array.from(authorBooks).sort();
let remainingBooks = Array.from(otherBooks).filter(b => !authorBooks.has(b)).sort();

let bookMenuOptions = ["[ ➕ Add New Book ]", ...sortedBooks, "--- Other Books ---", ...remainingBooks];
let bookMenuValues = ["[ ➕ Add New Book ]", ...sortedBooks, null, ...remainingBooks];

let selectedBook = await tp.system.suggester(bookMenuOptions, bookMenuValues, false, "Select Book");
if (!selectedBook) return;

if (selectedBook === "[ ➕ Add New Book ]") {
    let rawBook = await tp.system.prompt("Enter new Book name:");
    if (!rawBook) return;
    // Fix quotes for new books
    selectedBook = rawBook.replace(/"/g, "''"); 
}

// --- STEP 4: GET SPECIFIC LOCATION ---
let location = await tp.system.prompt("Location (e.g., Perek 5 Halacha 1):");
if (location === null) return; 
// Fix quotes for location acronyms
location = location.replace(/"/g, "''"); 

// --- STEP 5: RENAME AND MOVE FILE ---
let rawName = `${selectedAuthor} - ${selectedBook}${location ? ' - ' + location : ''}`;
// Catch any straggling illegal characters
let fileName = rawName.replace(/[:\\/|?*<>"]/g, '-'); 

await tp.file.rename(fileName);
await tp.file.move(`${basePath}/${fileName}`);

// --- STEP 6: GENERATE CONTENT ---
let content = `---
author: "[[${selectedAuthor}]]"
book: "${selectedBook}"
location: "${location}"
---
> [!info]- Reference
> Author:: [[${selectedAuthor}]]
> Book:: ${selectedBook}
> Location:: ${location}

### Source
> Paste Sefaria Hebrew text here...

### ${fileName}

`;

tR += content;
tR += tp.file.cursor();
_%>