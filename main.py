"""The Router That Fakes a Power Cut — a make.fun entry.

One sentence pitching a ridiculous invention that fixes a tiny everyday
annoyance: a Wi-Fi router that fakes a power cut whenever too many devices
connect, so the family at dinner finally talks to each other.

Writes the pitch to /output/entry.txt (created if missing). The gate
requires UTF-8 text of 1 to 220 characters; this entry is 132.
"""

import os

ENTRY = (
    "A Wi-Fi router that fakes a power cut whenever more than five devices "
    "connect, so your family finally talks to each other at dinner."
)


def validate(text: str) -> None:
    """Check the entry against the bounty gate: UTF-8 text, 1-220 chars,
    exactly one sentence."""
    if not 1 <= len(text) <= 220:
        raise ValueError(f"entry length {len(text)} out of range (1-220)")
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    # Exactly one sentence: one terminal mark at the very end, none inside.
    if stripped[-1] not in ".!?":
        raise ValueError("entry must end with sentence-ending punctuation")
    if stripped[-2:] in ("..", "!!", "??", "!?", "?!"):
        raise ValueError("entry must end with a single sentence mark")
    for sep in (". ", "! ", "? "):
        if sep in stripped:
            raise ValueError("entry must be a single sentence")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip: the file the judge reads must be exactly the entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the entry sentence"
    print(f"Wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
