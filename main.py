#!/usr/bin/env python3
"""Pigeon Pitch, One Line — entry program.

Writes a single-line elevator pitch from a city pigeon to investors
for its startup to /output/entry.txt (200 chars max, one line).
Deterministic: the same line on every run.
"""

import os

ENTRY = (
    "Give us $500K and 40,000 New York pigeons become same-day couriers "
    "\u2014 paid in breadcrumbs, and our CEO is a statue in Central Park."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry length {len(line)} out of range"
    assert "\n" not in line, "entry must be a single line"
    assert line == line.strip(), "entry must have no leading/trailing space"
    assert all(ord(c) < 128 or c == "\u2014" for c in line), \
        "only ASCII plus the em dash allowed"
    out_path = "/output/entry.txt"
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "output", "entry.txt")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line)
    print(f"Wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
