"""Conditionals.

Why this exists: models branch; so do trading and risk rules.
Run: python 01-python-foundations/07_conditionals.py
"""


def risk_bucket(volatility: float) -> str:
    if volatility < 0.08:
        return "low"
    if volatility < 0.18:
        return "medium"
    return "high"


def demo() -> None:
    for vol in (0.05, 0.12, 0.25):
        print(vol, "->", risk_bucket(vol))

    drawdown = -0.12
    if drawdown < -0.10:
        print("review the book: drawdown past 10%")
    elif drawdown < -0.05:
        print("watchlist")
    else:
        print("inside tolerance")


def your_turn() -> None:
    # Write grade(score) -> "A"/"B"/"C"/"F" with your own cutoffs.
    # Then map a list of scores to grades.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
