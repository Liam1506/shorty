import sys
import re
from pathlib import Path

def add_page(path: str, target: str):
    if not path or not target:
        print("Error: Missing path or target URL.")
        return

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
        raw_title = sys.argv[1]
        raw_body = sys.argv[2]
        
        clean_path = "".join(c for c in raw_title if c.isalnum() or c in ("-", "_")).lower()
        
        url_match = re.search(r'https?://[^\s<>"]+', raw_body)
        target_url = url_match.group(0) if url_match else raw_body.strip()

        add_page(clean_path, target_url)
    else:
        print("Usage: python addUrl.py <title> <body>")