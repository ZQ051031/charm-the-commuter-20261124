"""Charm the Commuter — one-line commuter forecast for the city.

Writes exactly one line (<=140 chars) to /output/entry.txt.
Standard library only; deterministic output, no network, no randomness.
"""

import os

ENTRY = (
    "Today's forecast: clear skies, a window seat, and one stranger's "
    "smile that makes the whole city feel like it's flirting back."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
