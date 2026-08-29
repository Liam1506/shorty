import sys
import re
from pathlib import Path

def add_page(path: str, target: str):
    p = Path(path)
    if p.exists():
        print(f"Path '{path}' already exists.")
        return

    with open("index.html", "r") as f:
        html = f.read()

    html = html.replace("{target}", target)

    p.mkdir(parents=True, exist_ok=True)
    file_path = p / "index.html"

    with open(file_path, "w") as f:
        f.write(html)

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        body = sys.argv[2]
        short_code_match = re.search(r"### Short Code\s*\n\s*(\S+)", body)
        short_code = short_code_match.group(1) if short_code_match else ""

        url_match = re.search(r'https?://[^\s<>"]+', body)
        target_url = url_match.group(0) if url_match else ""

        clean_path = "".join(c for c in short_code if c.isalnum() or c in ("-", "_")).lower()

        if clean_path and target_url:
            add_page(clean_path, target_url)
        else:
            print(f"Error: Missing values. Path: '{clean_path}', Target: '{target_url}'")