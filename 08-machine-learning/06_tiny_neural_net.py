"""A one-hidden-layer net in NumPy.

Why this exists: backprop is the chain rule from the calculus track.
Run: python 08-machine-learning/06_tiny_neural_net.py
"""

from __future__ import annotations

import numpy as np


def relu(z: np.ndarray) -> np.ndarray:
    return np.maximum(0, z)


def demo() -> None:
    rng = np.random.default_rng(6)
    x = rng.normal(size=(80, 2))
    y = (x[:, 0] ** 2 + x[:, 1] > 0.7).astype(float)[:, None]

    w1 = rng.normal(scale=0.4, size=(2, 8))
    b1 = np.zeros((1, 8))
    w2 = rng.normal(scale=0.4, size=(8, 1))
    b2 = np.zeros((1, 1))
    lr = 0.15

    for step in range(400):
        h = relu(x @ w1 + b1)
        logit = h @ w2 + b2
        pred = 1 / (1 + np.exp(-logit))
        loss = float(np.mean((pred - y) ** 2))
        dpred = 2 * (pred - y) / len(x)
        dw2 = h.T @ dpred
        db2 = dpred.sum(axis=0, keepdims=True)
        dh = dpred @ w2.T
        dh *= (x @ w1 + b1) > 0
        dw1 = x.T @ dh
        db1 = dh.sum(axis=0, keepdims=True)
        w2 -= lr * dw2
        b2 -= lr * db2
        w1 -= lr * dw1
        b1 -= lr * db1
        if step % 100 == 0:
            print(f"step {step} loss {loss:.4f}")

    acc = float(np.mean((pred > 0.5) == y))
    print("train acc", round(acc, 3))


def your_turn() -> None:
    # Hold out 20 rows and print test accuracy after training on the rest.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
