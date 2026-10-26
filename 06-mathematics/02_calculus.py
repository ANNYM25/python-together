"""Calculus with Python.

Why this exists: a derivative is a slope; gradient descent is that slope in many dimensions.
Run: python 06-mathematics/02_calculus.py
"""

from __future__ import annotations

import math

try:
    import sympy as sp
except ImportError:  # pragma: no cover - optional for the numeric half
    sp = None


def finite_difference(fn, x: float, h: float = 1e-6) -> float:
    return (fn(x + h) - fn(x - h)) / (2 * h)


def trap_integral(fn, a: float, b: float, n: int = 200) -> float:
    if n < 1:
        raise ValueError("n >= 1")
    width = (b - a) / n
    total = 0.5 * (fn(a) + fn(b))
    for i in range(1, n):
        total += fn(a + i * width)
    return total * width


def demo() -> None:
    def f(x: float) -> float:
        return x**3 - 2 * x

    x0 = 1.5
    numeric = finite_difference(f, x0)
    print("f'(1.5) numeric", round(numeric, 6), "true", round(3 * x0**2 - 2, 6))

    area = trap_integral(lambda x: math.sin(x), 0.0, math.pi)
    print("integral sin 0..pi", round(area, 6), "true", 2.0)

    if sp is not None:
        x = sp.symbols("x")
        g = sp.exp(-x**2)
        print("symbolic derivative", sp.diff(g, x))
        print("symbolic integral 0..1", sp.integrate(g, (x, 0, 1)).evalf())


def your_turn() -> None:
    # Approximate the derivative of log(x) at x=2 and compare with 1/2.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
