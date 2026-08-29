import sys
from pathlib import Path

def add_page(path: str, target: str):
    p = Path(path)
    if p.exists():
        return

    with open("index.html", "r") as f:
        html = f.read()

    html = html.replace("{target}", target)
    
    p.mkdir(parents=True, exist_ok=True)
    file_path = p / "index.html"
    
    with open(file_path, "w") as f:
        f.write(html)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        short, target = sys.argv[1].split("-TARGET-")
        add_page(short, target)