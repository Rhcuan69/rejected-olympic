"""Rejected Olympic Sports entry.

Writes one funny single-line rejected Olympic sport to /output/entry.txt.
Pure Python standard library, deterministic: the same bytes every run.
"""

import os

ENTRY = "Synchronised screaming: pairs are judged on pitch, duration, and how many pigeons flee the stadium."


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(ENTRY))
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
