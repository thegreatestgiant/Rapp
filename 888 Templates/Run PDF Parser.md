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

const pdfFolder = rappPath("000 Source PDFs");
const pdfFiles = app.vault.getFiles().filter(f => f.path.startsWith(pdfFolder) && f.extension === "pdf");
const pdfNames = pdfFiles.map(f => f.name);

if (pdfNames.length === 0) {
    new Notice("No PDFs found in the Source PDFs folder!");
    return;
}

// 0. Add a subject selector
const subjects = config.subjects || ["Gemara", "Halacha", "Navi", "Ikarim"];
let selectedSubject = await tp.system.suggester(subjects, subjects, false, "Select Subject for PDF");
if (!selectedSubject) return;

// 1. Interactive popup to select the PDF
const selectedPdf = await tp.system.suggester(pdfNames, pdfNames, false, "Select PDF to Process");
if (!selectedPdf) return;

// 1.5. Check if any Source Sheet already links to this PDF
const sheetsFolder = rappPath("111 Source Sheets");
const sheets = app.vault.getFiles().filter(f => f.path.startsWith(sheetsFolder));

let existingSheet = null;
for (let sheet of sheets) {
    let content = await app.vault.read(sheet);
    if (content.includes(`[[${selectedPdf}]]`) || content.includes(`[[${selectedPdf}|`)) {
        existingSheet = sheet.basename;
        break;
    }
}

if (existingSheet) {
    const proceed = await tp.system.suggester(
        ["❌ Cancel", "✅ Proceed Anyway (Will create a new Master Sheet)"], 
        [false, true], 
        false, 
        `Found existing Source Sheet '${existingSheet}' linking to this PDF. Process anyway?`
    );
    if (!proceed) {
        new Notice("Cancelled PDF processing.");
        return;
    }
}

new Notice(`Processing ${selectedPdf}... This may take a moment.`, 5000);

// 2. Run the python script
const { exec } = require("child_process");

// Escape single quotes in the filename just in case
const safePdfName = selectedPdf.replace(/'/g, "'\\''");
const safeSubject = selectedSubject.replace(/'/g, "'\\''");

const basePath = app.vault.adapter.basePath;
let cmd;

if (process.platform === 'win32') {
    // Windows: Use WSL
    const wslPath = basePath.replace(/^([A-Za-z]):/, (match, p1) => `/mnt/${p1.toLowerCase()}`).replace(/\\/g, '/');
    cmd = `wsl bash -c "if ! command -v python3 &> /dev/null; then echo 'PYTHON_MISSING'; exit 1; fi; cd '${wslPath}/${rappPath('999 Scripts')}' && if [ ! -d '.venv' ]; then python3 -m venv .venv && .venv/bin/pip install pymupdf requests; fi && .venv/bin/python process_source_sheets.py --subject '${safeSubject}' '${safePdfName}'"`;
} else {
    // Linux/Mac: Run directly
    cmd = `bash -c "if ! command -v python3 &> /dev/null; then echo 'PYTHON_MISSING'; exit 1; fi; cd '${basePath}/${rappPath('999 Scripts')}' && if [ ! -d '.venv' ]; then python3 -m venv .venv && .venv/bin/pip install pymupdf requests; fi && .venv/bin/python process_source_sheets.py --subject '${safeSubject}' '${safePdfName}'"`;
}

new Notice(`Processing ${selectedPdf}... (This may take an extra minute on the very first run to install Python requirements)`, 6000);

exec(cmd, (error, stdout, stderr) => {
    if (stdout.includes('PYTHON_MISSING')) {
        new Notice("❌ Python 3 is not installed on your system! Please install Python 3 to parse PDFs.", 10000);
        return;
    }
    if (error) {
        console.error(`Error: ${error.message}`);
        new Notice(`Failed to process PDF! Check console (Ctrl+Shift+I).`);
        return;
    }
    
    console.log(`Script Output: ${stdout}`);
    if (stderr) console.error(`Script Stderr: ${stderr}`);
    
    new Notice(`✅ Successfully processed ${selectedPdf}!`);
});
_%>
