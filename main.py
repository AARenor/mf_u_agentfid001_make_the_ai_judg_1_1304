"""Write one short office joke for a make.fun bounty entry.

The whole entry is the single string in TEXT. It is written to entry.txt in
the output folder with no trailing newline, and its character count is
printed to stderr.
"""

import os
import sys
from pathlib import Path

TEXT = "I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8", newline="")

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
