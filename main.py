"""Snooze Button Roast entry.

Writes one fixed roast line to <output_dir>/entry.txt (default /output).
Deterministic: the same line, byte for byte, on every run. Stdlib only.
"""

import os

PARTS = (
    "My alarm clock rings at 6 AM on a Saturday",
    "like the weekend personally owes it money.",
)

LINE = " ".join(PARTS)


def build_line() -> str:
    """Assemble the roast line from its two parts."""
    return " ".join(PARTS)


def main() -> None:
    line = build_line()
    if not 1 <= len(line) <= 200:
        raise ValueError(
            f"entry line must be 1-200 chars, got {len(line)}: {line!r}"
        )
    out_dir = (
        os.environ.get("ENTRY_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
