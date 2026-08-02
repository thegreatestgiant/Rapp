import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
SOURCES_DIR = SCRIPT_DIR.parent / "333 Sources"

for md_file in SOURCES_DIR.glob("*.md"):
    content = md_file.read_text(encoding="utf-8")
    if "> [!todo] Pending Edit Approval" in content:
        # Regex to match the block: starting with > [!todo] Pending Edit Approval
        # and continuing as long as lines start with "> " or are empty, until a non "> " line is found.
        # Actually, let's just match the exact pattern:
        # > [!todo] Pending Edit Approval
        # > Found on sheet: .*
        # > !\[\[.*\]\]
        
        new_content = re.sub(
            r'\n*> \[!todo\] Pending Edit Approval\n> Found on sheet:.*?\n(?:> !\[\[.*?\]\]\n?)*',
            '',
            content,
            flags=re.MULTILINE
        )
        if new_content != content:
            md_file.write_text(new_content, encoding="utf-8")
            print(f"Cleaned: {md_file.name}")

