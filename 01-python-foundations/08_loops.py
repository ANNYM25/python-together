"""Loops.

Why this exists: almost every dataset is something you walk through once.
Run: python 01-python-foundations/08_loops.py
"""


def demo() -> None:
    prices = [100, 101, 99, 102]
    for i, price in enumerate(prices):
        print("day", i, "price", price)

    # Daily simple returns from a price list.
    simple_returns = []
    for yesterday, today in zip(prices, prices[1:]):
        simple_returns.append(today / yesterday - 1)
    print("returns", [round(r, 4) for r in simple_returns])

    n = 3
    while n > 0:
        print("countdown", n)
        n -= 1

    for x in range(5):
        if x == 2:
            continue
        if x == 4:
            break
        print("range item", x)


def your_turn() -> None:
    # Compound 1000 at 4% for 8 years in a loop. Print the final value.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
