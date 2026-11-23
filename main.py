#!/usr/bin/env python3
"""One Emoji, One Smile — write the chosen emoji to the output file.

The entry is exactly one emoji, stored in entry.txt next to this script.
This program copies those bytes unchanged to $MAKEFUN_OUTPUT_DIR/entry.txt
so the submitted text is byte-for-byte the single emoji in entry.txt.

Pure Python standard library only; no third-party imports.
"""

import os
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.txt"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    data = source.read_bytes()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 8 or not text.strip():
        print("entry.txt must hold 1 to 8 characters, not only whitespace",
              file=sys.stderr)
        return 1
    target = Path(output_dir) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    os.chmod(target, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
