"""Strings.

Why this exists: tickers, reports, file names, and model labels are text.
Run: python 01-python-foundations/03_strings.py
"""


def demo() -> None:
    name = "Annie"
    field = "sustainable finance"
    line = f"{name} studies {field}."
    print(line)
    print("upper:", line.upper())
    print("slice first word:", line[:5])
    print("contains finance:", "finance" in line)
    print("split:", line.replace(".", "").split())

    ticker = "  esg.xlb  "
    print("clean ticker:", ticker.strip().upper())


def your_turn() -> None:
    # Build a filename like 'returns_2024_q3.csv' from year, quarter, and a stem.
    # Then check whether it ends with .csv.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
