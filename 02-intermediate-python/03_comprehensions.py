"""Comprehensions.

Why this exists: a one-line transform is easier to read than a five-line loop — when it stays short.
Run: python 02-intermediate-python/03_comprehensions.py
"""


def demo() -> None:
    xs = range(-2, 3)
    squares = [x * x for x in xs]
    positives = [x for x in xs if x > 0]
    labels = {x: "non-neg" if x >= 0 else "neg" for x in xs}
    unique_abs = {abs(x) for x in xs}
    print(squares, positives, labels, unique_abs)

    # Nested: flatten a small matrix
    matrix = [[1, 2], [3, 4]]
    flat = [cell for row in matrix for cell in row]
    print("flat", flat)


def your_turn() -> None:
    # From [0.02, -0.01, 0.0, 0.04], build a list of "up"/"down"/"flat" labels.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
