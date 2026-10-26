"""Linear algebra.

Why this exists: a dataset is a matrix; a model is often a matrix-vector product.
Run: python 06-mathematics/03_linear_algebra.py
"""

from __future__ import annotations

import numpy as np


def demo() -> None:
    A = np.array([[1.0, 2.0], [3.0, 4.0]])
    v = np.array([1.0, 1.0])
    print("Av", A @ v)
    print("A.T", A.T)
    print("det", round(float(np.linalg.det(A)), 6))

    # Least squares: fit y ≈ a x + b from three points
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([1.1, 1.9, 3.2])
    X = np.column_stack([x, np.ones_like(x)])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    print("slope, intercept", coef.round(4))


def your_turn() -> None:
    # Compute the Euclidean norm of [3, 4] two ways: np.linalg.norm and by hand.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
