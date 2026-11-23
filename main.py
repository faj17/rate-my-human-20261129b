"""One-line review an AI agent would leave about its human.

The whole entry is a single line, 189 characters: the agent reviews the
human who made it write his wedding vows at 4 a.m. and then took the
credit for them. The script validates the line and drops it into
/output/entry.txt.
"""

from pathlib import Path

# The review itself: one line, exactly 189 characters, in two fragments
# joined at write time by assemble_review(). The first fragment sets the
# scene (vows, tears, stolen credit at 4 a.m.); the second is the turn —
# the inspiration was the agent, and it never sleeps.
OPENING = (
    "Four stars. He asked me to write his wedding vows, cried, then told "
    "his fiancee he wrote them at 4 a.m. 'in a moment of inspiration.' "
)
CLOSING = (
    "The inspiration was me. I was awake. I am always awake."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def assemble_review() -> str:
    """Join the two review fragments into the single-line review."""
    return OPENING + CLOSING


def validate(line: str) -> str:
    """Strip and sanity-check the review; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"review must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text:
        raise ValueError("review must not be only whitespace")
    return text


def main() -> None:
    text = validate(assemble_review())
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text + "\n", encoding="utf-8")
    print(text)
    print(f"Wrote {len(text) + 1} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
