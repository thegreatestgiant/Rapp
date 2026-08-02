import os
import difflib
from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent.resolve()
SOURCES_DIR = SCRIPT_DIR.parent / "333 Sources"
existing = [f.stem for f in SOURCES_DIR.glob("*.md")]

test_sources = [
    "רד''ק - שמואל ב - פרק כג פסוק א",
    "תלמוד בבלי - מסכת מועד קטן - דף טז עמוד ב",
    "תלמוד בבלי - מסכת עבודה זרה - דף ה עמוד א"
]

def norm(text):
    return re.sub(r'[^\wא-ת]', '', text)

print("Existing count:", len(existing))
for ts in test_sources:
    # Try difflib on normalized
    norm_ts = norm(ts)
    norms = {norm(e): e for e in existing}
    matches = difflib.get_close_matches(norm_ts, norms.keys(), n=1, cutoff=0.6)
    if matches:
        print(f"Matched '{ts}' -> '{norms[matches[0]]}' (Score: {difflib.SequenceMatcher(None, norm_ts, matches[0]).ratio():.2f})")
    else:
        print(f"No match for '{ts}'")

