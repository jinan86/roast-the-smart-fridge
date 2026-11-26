"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single roast line to /output/entry.txt.
"""

import os

ENTRY = (
    "My robot vacuum mapped my whole flat, memorised where the dog sleeps, "
    "and still eats the same charging cable every single day."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
