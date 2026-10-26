"""Probability and a first Gaussian.

Why this exists: a loss function is an assumption about noise; VaR is a tail probability.
Run: python 06-mathematics/04_probability.py
"""

from __future__ import annotations

import math

import numpy as np


def gaussian_pdf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    z = (x - mu) / sigma
    return math.exp(-0.5 * z * z) / (sigma * math.sqrt(2 * math.pi))


def demo() -> None:
    rng = np.random.default_rng(7)
    draws = rng.normal(loc=0.01, scale=0.02, size=10_000)
    print("mean", round(float(draws.mean()), 4), "std", round(float(draws.std()), 4))
    print("P(x<0) empirical", round(float((draws < 0).mean()), 3))
    print("pdf at 0", round(gaussian_pdf(0.0, 0.01, 0.02), 3))

    # Expectation of a discrete return
    outcomes = np.array([-0.1, 0.0, 0.1])
    probs = np.array([0.2, 0.5, 0.3])
    print("E[r]", float(outcomes @ probs))


def your_turn() -> None:
    # Sample 5000 uniforms on [0, 1] and estimate E[U^2]. True value is 1/3.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
