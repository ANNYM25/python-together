"""Linear regression from scratch.

Why this exists: ordinary least squares is gradient descent on a quadratic bowl.
Run: python 08-machine-learning/02_from_scratch_linear_regression.py
"""

from __future__ import annotations

import numpy as np


def fit_gd(x: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 400) -> tuple[float, float]:
    w, b = 0.0, 0.0
    n = len(x)
    for _ in range(steps):
        pred = w * x + b
        err = pred - y
        w -= lr * (2 / n) * float(np.dot(err, x))
        b -= lr * (2 / n) * float(err.sum())
    return w, b


def demo() -> None:
    rng = np.random.default_rng(4)
    x = rng.normal(size=80)
    y = 1.7 * x - 0.4 + rng.normal(scale=0.2, size=80)
    w, b = fit_gd(x, y)
    print("learned", round(w, 3), round(b, 3), "true ~ 1.7, -0.4")
    pred = w * x + b
    mse = float(np.mean((pred - y) ** 2))
    print("mse", round(mse, 4))


def your_turn() -> None:
    # Split the last 20 points as a test set and print train vs test MSE.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
