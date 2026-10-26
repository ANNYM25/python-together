"""NumPy tour.

Why this exists: a 10,000-day return series should never be a Python for-loop.
Run: python 07-data-science/01_numpy_tour.py
"""

from __future__ import annotations

import numpy as np


def demo() -> None:
    rng = np.random.default_rng(0)
    rets = rng.normal(0.0004, 0.01, size=252)
    wealth = np.cumprod(1 + rets)
    print("shape", rets.shape, "dtype", rets.dtype)
    print("mean", rets.mean().round(5), "vol", rets.std().round(5))
    print("end wealth", wealth[-1].round(4))
    print("worst day", rets.min().round(4))

    # Broadcast: annualize assuming 252 days
    print("ann mean", (rets.mean() * 252).round(4))
    print("ann vol", (rets.std() * np.sqrt(252)).round(4))


def your_turn() -> None:
    # Build a 5x3 random matrix and print its column means.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
