# Source Sheet Workflow Setup Guide

Since you use Obsidian across multiple devices, follow these steps to set up the Source Sheet processing engine on any new machine.

## 1. Prerequisites
You need Python installed on your device to run the PDF cropping and processing engine.
* **Windows/Mac:** Download and install Python from [python.org](https://www.python.org/downloads/). (On Windows, make sure to check "Add Python to PATH" during installation).
* **Linux / WSL:** `sudo apt install python3 python3-venv python3-pip`

## 2. Install Dependencies (Virtual Environment)
Open your terminal and navigate to this `Scripts` folder in your Obsidian vault. Then run:
```bash
cd "path/to/Obsidian/Scripts"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
This will install `PyMuPDF` (for PDF cropping) and `requests` (for the Sefaria API) within an isolated virtual environment.

## 3. Obsidian Integration
To run this seamlessly from *inside* Obsidian without ever opening a terminal, we will use your existing **Templater** plugin (or the **Shell Commands** plugin).

### Option A: Using Templater (Recommended)
1. Go to **Settings > Templater**.
2. Scroll down to **User System Command Execution**.
3. Enable it, and add a new User Function:
   * **Function Name:** `process_source_sheet`
   * **System Command (WSL / Linux):** `"{{vault_path}}/Scripts/venv/bin/python" "{{vault_path}}/Scripts/process_source_sheets.py" "%1"`
   * **System Command (Windows via WSL):** `wsl bash -c "cd \"{{vault_path}}/Scripts\" && ./venv/bin/python process_source_sheets.py \"%1\""`
4. You can now create a template that prompts you for a PDF name and runs `<% await tp.user.process_source_sheet("Sheet.pdf") %>`.

### Option B: Using the "Shell Commands" Plugin
1. Install **Shell Commands** from the Obsidian Community Plugins.
2. Add a new shell command:
   * **WSL / Linux:** `"{{vault_path}}/Scripts/venv/bin/python" "{{vault_path}}/Scripts/process_source_sheets.py" "{{file_path:absolute}}"`
   * **Windows via WSL:** `wsl bash -c "cd \"{{vault_path}}/Scripts\" && ./venv/bin/python process_source_sheets.py \"{{file_path:absolute}}\""`
3. Assign it to a hotkey or add it to your right-click menu for PDF files!

---
*Note: If you are syncing this vault to a mobile device (iOS/Android), Python scripts cannot run natively on the mobile OS. The processing must be triggered from your computer.*

