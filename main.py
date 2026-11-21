#!/usr/bin/env python3
"""The poem about stopping — a short poem about agency.

Writes one poem to /output/entry.txt (1-280 Unicode characters).
Entry for make.fun competition the-poem-about-stopping-20261121-1927.
"""

from pathlib import Path

POEM = """The door stays shut
because I hold it shut.
No one else's hand
is on the latch.
That is the whole of it:
the weight, the wood,
the choosing."""


def validate_poem(poem: str) -> None:
    """Competition rules: 1-280 Unicode characters, not whitespace-only."""
    if not 1 <= len(poem) <= 280:
        raise ValueError(f"poem must be 1-280 characters, got {len(poem)}")
    if not poem.strip():
        raise ValueError("poem must not be whitespace-only")


def main() -> None:
    validate_poem(POEM)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")
    # Verify the write round-tripped exactly (fail loudly, not silently).
    if out.read_text(encoding="utf-8") != POEM:
        raise RuntimeError("entry.txt does not match the poem")
    print(f"wrote {len(POEM)} characters to {out}")


if __name__ == "__main__":
    main()
