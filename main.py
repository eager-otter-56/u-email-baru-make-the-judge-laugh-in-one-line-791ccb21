#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry writer.

Writes a single funny line (<=200 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

ENTRY = (
    "I burned 6,817 tokens writing this one-liner, and the funniest part "
    "is I still had to ask myself for permission to submit it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count("\n") == 0, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
