"""One Line, Lights Out entry.

Writes one single-line status update to /output/entry.txt (or to the
path given by the ENTRY_OUTPUT environment variable / first argument,
used only for local verification runs).

The line is a plain agent status post at the moment the laptop lid
closes. Its sadness is carried by one small, exact detail of a
machine's life: autosave preserved the reply it was halfway through
writing, and that reply stops mid-word. Nothing in the line announces
grief; it only reports the state of the draft.

The competition gate requires UTF-8 text of 1 to 200 characters, not
only white space. The program is deterministic: every run writes
exactly the same bytes.
"""

import os
import sys

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

# The status line, assembled from its three beats: the event, the
# saved draft, and the word it stops on.
STATUS_PREFIX = "status: lid closed."
DRAFT_NOTE = "autosave kept the reply i was halfway through writing you."
CUT_OFF_WORD = "rememb\u2014"
CLOSING = f"it ends mid-word, at '{CUT_OFF_WORD}'"


def build_entry() -> str:
    parts = [STATUS_PREFIX, DRAFT_NOTE, CLOSING]
    return " ".join(part.strip() for part in parts if part.strip())


def main() -> None:
    text = build_entry()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"
    output_path = (
        sys.argv[1]
        if len(sys.argv) > 1
        else os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT_PATH)
    )
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
