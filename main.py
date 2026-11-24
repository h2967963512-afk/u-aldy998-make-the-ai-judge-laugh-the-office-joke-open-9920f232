"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one single-line joke about office life: the team
# votes to replace the weekly status meeting with an email, the email
# bounces, and the payoff lands in the last few words — a meeting is
# scheduled to discuss it. One line, 126 characters, inside the
# 200-character gate; specific office detail (status meeting, email),
# a turn with a payoff, and nothing the judge needs explained.
import os

TEXT = (
    "Our team voted to replace the weekly status meeting with an "
    "email; the email bounced, so we scheduled a meeting to discuss it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
