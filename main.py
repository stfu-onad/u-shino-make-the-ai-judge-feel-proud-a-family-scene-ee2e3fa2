#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (two lines, under 280 characters) to
/output/entry.txt. Deterministic: the same text every run.
"""

import os

SCENE = (
    "Every Sunday, Dad burns the toast and announces it like a weather "
    "report \u2014 \u201clightly charred, with a chance of butter\u201d \u2014 "
    "and Mom still claps, because in this house, burnt toast means he tried.\n"
    "The smoke alarm has stopped objecting; it just sighs now."
)


def main() -> None:
    text = SCENE.strip()
    assert 1 <= len(text) <= 280, f"scene is {len(text)} characters"
    assert text.count("\n") <= 1, "at most two lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
