#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes a single line -- a robot vacuum's deadpan excuse for missing
one spot -- to /output/entry.txt.

Deterministic: the same line is written on every run. Standard
library only, no network, no randomness, no input files.
"""

import os

ENTRY = (
    # Chosen line: bureaucratic machine logic. The vacuum does not
    # apologise or blame its sensors -- it reclassifies the crumb as
    # structural ("load-bearing") after 412 passes, then refuses
    # questions. Deadpan, smug, specific, punchline last.
    "I did not miss that spot. The crumb has survived 412 passes, "
    "so I have reclassified it as load-bearing. "
    "I will not be taking questions."
)

MAX_CHARS = 200


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
    )
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    # Read back and verify: the file must contain exactly this line.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line + "\n", "verification failed: entry.txt mismatch"
    print(f"Wrote {len(line)} characters to {out_path}")


if __name__ == "__main__":
    main()
