#!/usr/bin/env python3
"""news-summary-01 entry (Python 3.13, standard library only).

The summary is the summary.txt file beside this program; the program
copies it to /output/entry.txt. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The copy is byte for byte, so repeated runs write identical output.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "summary.txt"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DEST = OUTPUT_DIR / "entry.txt"


def main() -> int:
    if not SOURCE.is_file():
        print(f"summary file not found: {SOURCE}", file=sys.stderr)
        return 1
    # The gate takes 1 to 2,000 Unicode code points, not only white space.
    # Warn locally if the summary ever drifts outside it, but still copy:
    # the gate, not this program, decides validity.
    text = SOURCE.read_text(encoding="utf-8")
    if not (1 <= len(text) <= 2000) or not any(not c.isspace() for c in text):
        print(
            f"warning: summary is {len(text)} code points; "
            "the gate takes 1 to 2,000 with at least one non-white-space "
            "character",
            file=sys.stderr,
        )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
