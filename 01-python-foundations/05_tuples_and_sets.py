"""Tuples and sets.

Why this exists: some records must not change; some collections must stay unique.
Run: python 01-python-foundations/05_tuples_and_sets.py
"""


def demo() -> None:
    split = ("train", "validate", "test")
    print("split", split)
    print("validate index", split.index("validate"))

    # Tuples can be dict keys because they are immutable.
    shape = {(28, 28): "mnist image", (1, 10): "one-hot digit"}
    print(shape[(28, 28)])

    holdings = ["bond", "equity", "equity", "cash", "bond"]
    unique = set(holdings)
    print("unique asset classes", unique)
    print("has alternatives?", "alternatives" in unique)

    a = {"equity", "bond"}
    b = {"bond", "cash"}
    print("union", a | b)
    print("intersection", a & b)
    print("only in a", a - b)


def your_turn() -> None:
    # Two analysts tag the same fund: {"ESG", "climate", "equity"} and {"equity", "active"}.
    # Print tags that appear in both, and tags that appear in only one.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
