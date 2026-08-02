<%*
// --- CONFIGURATION: PREFERENCES ---
// Change these to match the semester/class you want at the top of the list
const prefSemester = "Spring 2026";
const prefClass = "Linear";

// --- STEP 1: SETUP ---
const rootPath = "000 School";
const rootFolder = app.vault.getAbstractFileByPath(rootPath);

let targetFolderPath = "";
let selectedClass = "";

if (rootFolder) {
    // MAIN VAULT BEHAVIOR (Has 000 School folder)
    let semesters = rootFolder.children
        .filter(f => f.children) 
        .map(f => f.name)
        .sort((a, b) => {
            if (a.includes(prefSemester)) return -1;
            if (b.includes(prefSemester)) return 1;
            return a.localeCompare(b);
        });

    let selectedSemester = await tp.system.suggester(semesters, semesters, false, "Select Semester");
    if (!selectedSemester) return; 

    const semesterPath = `${rootPath}/${selectedSemester}`;
    const semesterFolder = app.vault.getAbstractFileByPath(semesterPath);

    let classes = semesterFolder.children
        .filter(f => f.children)
        .map(f => f.name)
        .sort((a, b) => {
            if (a.includes(prefClass)) return -1;
            if (b.includes(prefClass)) return 1;
            return a.localeCompare(b);
        });

    selectedClass = await tp.system.suggester(classes, classes, false, "Select Course");
    if (!selectedClass) return; 

    targetFolderPath = `${semesterPath}/${selectedClass}/Notes`;
    let targetFolder = app.vault.getAbstractFileByPath(targetFolderPath);
    if (!targetFolder) {
        await app.vault.createFolder(targetFolderPath);
    }
} else {
    // RAPP STANDALONE BEHAVIOR
    // 1. Load config to get subjects
    const allFolders = app.vault.getAllLoadedFiles().filter(f => f.children);
    const sourcePdfFolder = allFolders.find(f => f.name.replace(/^\d+\s*/, '') === 'Source PDFs');
    const rappRoot = (sourcePdfFolder && sourcePdfFolder.parent.path !== "/") ? sourcePdfFolder.parent.path : '';
    function rappPath(subpath) { return rappRoot ? `${rappRoot}/${subpath}` : subpath; }
    
    let config = { subjects: ['Gemara', 'Halacha', 'Navi', 'Ikarim'] };
    const configFile = app.vault.getAbstractFileByPath(rappPath('config.json'));
    if (configFile) {
        try { config = JSON.parse(await app.vault.read(configFile)); } catch(e) {}
    }
    
    // 2. Prompt for Subject
    const subjects = config.subjects || ["Gemara", "Halacha", "Navi", "Ikarim"];
    let subject = await tp.system.suggester(subjects, subjects, false, "Select Subject for Note");
    if (!subject) return;
    
    selectedClass = subject;
    
    // 3. Define folder path (e.g., 444 Attachments/Notes or 333 Sources/Subject)
    // Let's place generic notes in a "Notes" subfolder of the subject in 333 Sources
    targetFolderPath = rappPath(`333 Sources/${subject}/Notes`);
    let targetFolder = app.vault.getAbstractFileByPath(targetFolderPath);
    if (!targetFolder) {
        // Ensure 333 Sources/Subject exists
        if (!app.vault.getAbstractFileByPath(rappPath(`333 Sources/${subject}`))) {
            await app.vault.createFolder(rappPath(`333 Sources/${subject}`));
        }
        await app.vault.createFolder(targetFolderPath);
    }
}

// --- STEP 2: RENAME & MOVE ---
let title = await tp.system.prompt("Note Title (Leave blank for default)");
if (!title) title = `${selectedClass} - ${tp.date.now("YYYY-MM-DD")}`;

if (targetFolderPath) {
    await tp.file.move(`${targetFolderPath}/${title}`);
} else {
    await tp.file.rename(title);
}

let date = tp.date.now();
tR += "---"
%>
Course: "[[<%selectedClass%>]]"
Date:  <%date%>
understanding_level: ""
topic: ""
summary: ""
<%*tR += "---"%>
## Overview
Understanding Level: `INPUT[stars][:understanding_level]`
Topic: `INPUT[text(limit(25),placeholder(Unit/Class Topic)):topic]`
Summary: `INPUT[text(limit(100),placeholder(Short Note Summary)):summary]`

---

<% tp.file.cursor() %>