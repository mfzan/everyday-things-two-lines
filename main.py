"""Two-line explanation of a traffic jam, for a 10-year-old.

Line 1 explains the everyday thing through one vivid analogy: a traffic
jam as a line of tired elephants queuing for a single tiny puddle.
Line 2 is the honest accounting: it names what the analogy maps (slow,
single-file movement toward one small thing) and what it leaves out
(the honking, which is the human part).

Running this program writes exactly those two lines to
/output/entry.txt, so the judge can read the pair as plain text.
"""

import os
import stat

OUTPUT_PATH = "/output/entry.txt"

# The entry itself: two lines, one sentence each.
LINE_1 = (
    "A traffic jam is like a line of tired elephants all queuing for "
    "one tiny puddle, each one too polite to push past the others."
)
LINE_2 = (
    "The analogy works because both move slowly in a single file toward "
    "one small thing, but it leaves out the honking \u2014 real elephants "
    "never honk at each other; the honking is the human part."
)


def _is_single_sentence(line: str) -> bool:
    """One sentence: exactly one full stop, sitting at the very end."""
    stripped = line.strip()
    return stripped.endswith(".") and stripped.count(".") == 1


def build_entry() -> str:
    """Join the two lines and sanity-check the pair before writing."""
    lines = [LINE_1, LINE_2]
    for line in lines:
        if not _is_single_sentence(line):
            raise ValueError("each entry line must be exactly one sentence")
    text = "\n".join(lines) + "\n"
    if not 1 <= len(text) <= 400:
        raise ValueError("entry must be 1 to 400 characters")
    return text


def main() -> int:
    text = build_entry()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    # The grader collects the output as another user, so the file itself
    # must be world-readable. Only the file is chmodded, never /output.
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
