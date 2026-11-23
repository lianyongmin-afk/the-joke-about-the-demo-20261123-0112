"""One-line joke about working beside an AI coding agent.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for local testing). The entry must be UTF-8, 1-280 Unicode code points,
and not only whitespace.
"""

import os

JOKE = (
    "My coding agent fixed the demo crash live "
    "\u2014 by deleting the feature everyone came to see."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
