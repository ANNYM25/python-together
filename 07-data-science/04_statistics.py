"""Statistics that show up in both ML and finance.

Why this exists: mean and variance are not enough; tails and sample size matter.
Run: python 07-data-science/04_statistics.py
"""

from __future__ import annotations

import numpy as np


def demo() -> None:
    rng = np.random.default_rng(3)
    x = rng.standard_t(df=5, size=2000)
    print("mean", x.mean().round(4), "median", np.median(x).round(4))
    print("skew", ((x.mean() - np.median(x)) / x.std()).round(4))
    q = np.quantile(x, [0.05, 0.5, 0.95])
    print("5/50/95", q.round(3))

    # Standard error of the mean
    se = x.std(ddof=1) / np.sqrt(len(x))
    print("mean +/- 2 se", (x.mean() - 2 * se).round(3), (x.mean() + 2 * se).round(3))


def your_turn() -> None:
    # Bootstrap the median of x with 200 resamples and print the 5th/95th percentiles.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
