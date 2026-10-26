"""Iterators and generators.

Why this exists: you cannot load every tick into RAM. Yield one window at a time.
Run: python 03-pythonic-tools/02_iterators_generators.py
"""

from __future__ import annotations


def moving_average(series: list[float], window: int):
    if window <= 0:
        raise ValueError("window must be positive")
    total = 0.0
    for i, value in enumerate(series):
        total += value
        if i >= window:
            total -= series[i - window]
        if i + 1 >= window:
            yield total / window


def demo() -> None:
    xs = [1, 2, 3, 4, 5]
    print("ma3", [round(v, 4) for v in moving_average(xs, 3)])

    squares = (x * x for x in xs)  # generator expression, lazy
    print("sum of squares", sum(squares))
    print("second pass is empty", list(squares))


def your_turn() -> None:
    # Write batches(items, size) that yields lists of length `size` (last may be shorter).
    pass


if __name__ == "__main__":
    demo()
    your_turn()
