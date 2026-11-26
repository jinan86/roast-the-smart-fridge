"""One-line roast for the smart fridge competition.

Builds the entry line from its parts and writes it to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

PARTS = [
    "My robot vacuum mapped my whole flat,",
    "memorised where the dog sleeps,",
    "and still eats the same charging cable every single day.",
]


def build_entry() -> str:
    """Join the roast parts into the single entry line."""
    line = " ".join(part.strip() for part in PARTS)
    assert 1 <= len(line) <= 160, f"entry must be 1-160 chars, got {len(line)}"
    return line


def write_entry(entry: str) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry, encoding="utf-8")


def main() -> None:
    entry = build_entry()
    write_entry(entry)
    print(f"Wrote {len(entry)}-char entry to {OUTPUT_PATH}")
    print(entry)


if __name__ == "__main__":
    main()
