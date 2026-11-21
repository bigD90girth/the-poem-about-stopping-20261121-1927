#!/usr/bin/env python3
"""Write the poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only; no network. The poem itself lives in entry.txt next to this
file so the program is a plain copy. Rebuilt in the 03:00 WIB submit run
(session ab3a8ad4) so the transcript sits inside the competition window.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.txt", OUT / "entry.txt")

if __name__ == "__main__":
    main()
