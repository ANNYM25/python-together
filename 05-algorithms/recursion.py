"""Recursion and a slice of dynamic programming.

Why this exists: trees, factorials, and many ML backprops are recursive ideas.
Run: python 05-algorithms/recursion.py
"""

from __future__ import annotations


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def fib_dp(n: int) -> int:
    """Bottom-up Fibonacci — O(n) time, O(1) extra memory."""
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def demo() -> None:
    print("5!", factorial(5))
    print("fib 10", fib_dp(10))


if __name__ == "__main__":
    demo()
