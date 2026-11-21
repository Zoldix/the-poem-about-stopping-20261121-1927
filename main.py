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


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
