import sys
import shutil
from pathlib import Path

def remove_page(path: str):
    p = Path(path)
    
    if not p.exists():
        print(f"Path '{path}' does not exist. Skipping cleanup.")
        return
    if p.is_dir():
        shutil.rmtree(p)
        print(f"Successfully deleted directory: {path}")
    else:
        p.unlink()
        print(f"Successfully deleted file: {path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        raw_input = sys.argv[1]
        
        if "-TARGET-" in raw_input:
            short, _ = raw_input.split("-TARGET-")
        else:
            short = raw_input
            
        remove_page(short)