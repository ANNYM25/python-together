"""Lists.

Why this exists: a return series, a mini-batch, and a shopping list are the same shape.
Run: python 01-python-foundations/04_lists.py
"""


def demo() -> None:
    returns = [0.01, -0.02, 0.015, 0.0, 0.004]
    print("len", len(returns))
    print("first", returns[0], "last", returns[-1])
    print("middle", returns[1:4])

    returns.append(0.008)
    returns[1] = -0.018
    print("updated", returns)

    print("sum", sum(returns))
    print("sorted copy", sorted(returns))
    print("original still", returns)

    doubled = [2 * r for r in returns]
    print("doubled", doubled)


def your_turn() -> None:
    # Keep only non-negative returns from the demo list using a loop or a comprehension.
    # Then print how many days were up or flat.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
