#!/usr/bin/env python3
"""Worst AI Advice — u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.

Writes one line of the worst possible advice an AI could give (at most
140 characters) to /output/entry.txt. Standard library only.
"""

import os

ADVICE = (
    "As your AI assistant, I recommend emailing passwords to yourself, "
    "subject 'passwords' \u2014 you'll never lose them. "
    "Neither will anyone else."
)


MAX_CHARS = 140


def validate_advice(text: str) -> str:
    """Check the advice fits the gate: non-blank, one line, <= 140 chars."""
    text = text.strip()
    if not text:
        raise SystemExit("error: advice must not be blank")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"error: advice is {len(text)} chars, over the {MAX_CHARS}-char cap"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("error: advice must be a single line")
    return text


def main() -> None:
    text = validate_advice(ADVICE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        with open(out_path, encoding="utf-8") as f:
            if f.read() != text:
                raise SystemExit(
                    f"error: wrote {out_path} but contents do not match"
                )
    except OSError as exc:
        raise SystemExit(f"error: cannot write entry to {out_path}: {exc}")
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
