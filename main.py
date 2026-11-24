"""Write one office joke (single line, 1-200 chars) to /output/entry.txt."""

import os
from pathlib import Path

JOKE = (
    "I called a meeting about the meeting that could have been an email "
    "\u2014 HR replied-all asking for a meeting to discuss it."
)


def main() -> None:
    # Gate: exactly one line, 1-200 chars, not only whitespace.
    assert "\n" not in JOKE and 1 <= len(JOKE) <= 200, len(JOKE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
