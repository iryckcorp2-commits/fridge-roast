#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — one-line entry writer.

Writes a single roast line (at most 200 characters, no em-dash) to
entry.txt inside MAKEFUN_OUTPUT_DIR (default /output).
Python 3 standard library only; no network access; deterministic.
"""

import os

ENTRY = (
    "My smart fridge sent my weekly report: 14 door opens, "
    "0 meals cooked, and one yogurt filed as a missing person."
)


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\u2014" not in ENTRY, "entry must not contain an em-dash"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
