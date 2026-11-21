#!/usr/bin/env python3
"""Emit the stopping poem as this entry's artifact.

The poem lives in entry.txt next to this file. This program reads it and
writes it to $MAKEFUN_OUTPUT_DIR/entry.txt, defaulting to /output/entry.txt.
Nothing here touches the network; the standard library is all it needs.
"""
import os
from pathlib import Path

POEM = Path(__file__).resolve().parent / "entry.txt"
DESTINATION = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"

def emit() -> None:
    poem = POEM.read_text(encoding="utf-8")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(poem, encoding="utf-8")

if __name__ == "__main__":
    emit()
