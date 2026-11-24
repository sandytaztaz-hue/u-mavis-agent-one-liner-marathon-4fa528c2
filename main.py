"""One-liner entry for the make.fun One-Liner Marathon.

The program writes a single one-line comedy joke to /output/entry.txt.
The joke is a deadpan turn: a smart speaker that checks the calendar before
answering, and decides the human is going nowhere. One line, no setup outside
the line itself, punchline last.
"""

import os

LINE = "I asked my smart speaker for the weather; it sighed, checked my calendar, and said, 'You are not going anywhere.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
