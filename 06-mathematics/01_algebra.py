"""Algebra you actually use.

Why this exists: compounding, geometric series, and logs sit under every return model.
Run: python 06-mathematics/01_algebra.py
"""

from __future__ import annotations

import math


def geometric_sum(a: float, r: float, n: int) -> float:
    """a + a r + ... + a r^{n-1}."""
    if n <= 0:
        return 0.0
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)


def demo() -> None:
    # Annuity: 100 per year for 10 years, discount rate 5%
    payment, rate, years = 100.0, 0.05, 10
    pv = geometric_sum(payment / (1 + rate), 1 / (1 + rate), years)
    print("present value of annuity", round(pv, 2))

    print("log return", round(math.log(110 / 100), 4))
    print("exp check", round(100 * math.exp(math.log(1.1)), 4))


def your_turn() -> None:
    # Solve 1.04 ** n = 2 for n using logs. Print years to double at 4%.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
