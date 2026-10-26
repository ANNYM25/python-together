"""Returns and risk.

Why this exists: a 'good' year can still hide an ugly path.
Run: python 09-fintech/02_returns_and_risk.py
"""

from __future__ import annotations

import numpy as np


def max_drawdown(prices: np.ndarray) -> float:
    peaks = np.maximum.accumulate(prices)
    dd = prices / peaks - 1.0
    return float(dd.min())


def demo() -> None:
    rng = np.random.default_rng(8)
    rets = rng.normal(0.0005, 0.012, size=252)
    log_rets = np.log1p(rets)
    prices = 100 * np.cumprod(1 + rets)
    print("simple mean", rets.mean().round(5))
    print("log mean", log_rets.mean().round(5))
    print("ann vol", (rets.std() * np.sqrt(252)).round(4))
    print("max drawdown", round(max_drawdown(prices), 4))
    var_5 = float(np.quantile(rets, 0.05))
    print("historical daily 5% VaR", round(var_5, 4))


def your_turn() -> None:
    # Convert VaR to a dollar loss on a 1_000_000 book (approximate, one-day).
    pass


if __name__ == "__main__":
    demo()
    your_turn()
