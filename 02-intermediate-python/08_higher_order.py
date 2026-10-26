"""Higher-order functions.

Why this exists: sklearn, pandas, and maps all pass functions into functions.
Run: python 02-intermediate-python/08_higher_order.py
"""

from __future__ import annotations

from functools import reduce


def demo() -> None:
    rets = [0.01, -0.02, 0.015]

    def signed(r: float) -> str:
        return "up" if r > 0 else "down" if r < 0 else "flat"

    print(list(map(signed, rets)))
    print(list(filter(lambda r: r > 0, rets)))

    wealth = reduce(lambda w, r: w * (1 + r), rets, 1.0)
    print("growth of 1", round(wealth, 4))

    def twice(fn):
        def wrapped(x):
            return fn(fn(x))

        return wrapped

    @twice
    def add_one(x: int) -> int:
        return x + 1

    print("add_one twice", add_one(3))


def your_turn() -> None:
    # Write apply_all(fns, x) that runs a list of functions in order on x.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
