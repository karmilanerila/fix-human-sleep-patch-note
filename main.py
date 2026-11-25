"""Fix Human Sleep: Funniest Patch Note.

Writes a single patch-note line announcing that human sleep is fixed
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line is deterministic: the same bytes on every run, so both grader
runs gate identically.
"""

import os
import stat

# The gate allows 1 to 160 characters, single line, UTF-8 text.
MAX_CHARS = 160

PATCH_NOTE = (
    "Fixed a bug where sleep only dimmed the screen for eight hours; "
    "it now actually recharges the human."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = PATCH_NOTE.strip()
    assert "\n" not in text, "entry must stay a single line"
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-160 characters"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(text.encode("utf-8"))
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Read back what we wrote: both grader runs must gate identically.
    with open(path, "rb") as handle:
        assert handle.read().decode("utf-8") == text


if __name__ == "__main__":
    main()
