#!/usr/bin/env python3
"""The word you'd delete from the dictionary.

Writes the single chosen word to /output/entry.txt, gate-checking it
first: UTF-8 text, 1-77 characters, not only whitespace, exactly one
word, and byte-identical to what ends up on disk.

The pick: "whatchamacallit" -- the word you reach for when you have
forgotten the word. Erase it and the dictionary loses its own escape
hatch: nothing left to call the thing you cannot name.
"""

import os
import sys
from pathlib import Path

WORD = "whatchamacallit"
MAX_CHARS = 77


def main() -> int:
    if not WORD.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(WORD) > MAX_CHARS:
        print(f"entry is {len(WORD)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if len(WORD.split()) != 1:
        print("entry must be exactly one word", file=sys.stderr)
        return 1

    out = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(WORD.encode("utf-8"))

    if out.read_bytes() != WORD.encode("utf-8"):
        print("written bytes do not match the entry", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
