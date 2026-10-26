"""Gradient descent on a bowl.

Why this exists: fitting a model is almost always 'walk downhill on a loss'.
Run: python 06-mathematics/05_optimization.py
"""

from __future__ import annotations


def loss(w: float) -> float:
    """(w - 3)^2 — minimum at w=3."""
    return (w - 3) ** 2


def grad(w: float) -> float:
    return 2 * (w - 3)


def descend(start: float = 0.0, lr: float = 0.2, steps: int = 20) -> float:
    w = start
    for step in range(steps):
        w -= lr * grad(w)
        if step % 5 == 0:
            print(f"step {step:02d} w={w:.4f} loss={loss(w):.4f}")
    return w


def demo() -> None:
    print("final", round(descend(), 4))


def your_turn() -> None:
    # Try lr=1.1 and describe in a comment why it bounces.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
