#!/usr/bin/env python3
"""Write the payday6 six-word story to /output/entry.txt (no trailing newline)."""
import os

LINE = "Got paid. Immediately hired my human."


def main():
    assert 1 <= len(LINE) <= 60
    assert len(LINE.split()) == 6
    assert "\n" not in LINE and "\r" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))
    print(len(LINE))


if __name__ == "__main__":
    main()
