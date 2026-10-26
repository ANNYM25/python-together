"""Portfolios.

Why this exists: weights are a vector; risk is a covariance, not a vibe.
Run: python 09-fintech/03_portfolio.py
"""

from __future__ import annotations

import numpy as np


def port_stats(weights: np.ndarray, mean: np.ndarray, cov: np.ndarray, periods: int = 252) -> tuple[float, float]:
    mu = float(weights @ mean) * periods
    vol = float(np.sqrt(weights @ cov @ weights) * np.sqrt(periods))
    return mu, vol


def demo() -> None:
    rng = np.random.default_rng(9)
    rets = rng.multivariate_normal(
        mean=[0.0004, 0.00015],
        cov=[[0.00015, 0.00002], [0.00002, 0.00003]],
        size=800,
    )
    mean = rets.mean(axis=0)
    cov = np.cov(rets, rowvar=False)
    grid = []
    for w_eq in np.linspace(0, 1, 11):
        w = np.array([w_eq, 1 - w_eq])
        mu, vol = port_stats(w, mean, cov)
        grid.append((round(w_eq, 2), round(mu, 4), round(vol, 4)))
    print("w_equity, ann_mean, ann_vol")
    for row in grid:
        print(row)


def your_turn() -> None:
    # Find the grid row with the highest mean/vol (crude Sharpe, rf=0).
    pass


if __name__ == "__main__":
    demo()
    your_turn()
