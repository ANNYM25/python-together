"""Operators.

Why this exists: models and money both start as arithmetic on numbers.
Run: python 01-python-foundations/02_operators.py
"""


def demo() -> None:
    a, b = 7, 3
    print("add", a + b)
    print("sub", a - b)
    print("mul", a * b)
    print("true div", a / b)
    print("floor div", a // b)
    print("mod", a % b)
    print("power", a**b)

    print("equal", a == b)
    print("not equal", a != b)
    print("greater", a > b)
    print("and", True and False)
    print("or", True or False)
    print("not", not False)

    # Compound assignment is common in loops that accumulate a total.
    wealth = 1000.0
    wealth *= 1.05
    print("wealth after 5% growth", wealth)


def your_turn() -> None:
    # A loan of 2500 is repaid in 4 equal integer chunks using // and %.
    # Print the chunk size and the leftover cents (use cents as integers).
    pass


if __name__ == "__main__":
    demo()
    your_turn()
