"""Decorators and caching.

Why this exists: timing and memoization show up in every training loop.
Run: python 03-pythonic-tools/03_decorators_and_cache.py
"""

from __future__ import annotations

import functools
import time


def timed(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{fn.__name__} took {elapsed:.6f}s")
        return result

    return wrapper


@functools.lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@timed
def fib_30() -> int:
    return fib(30)


def demo() -> None:
    print("fib(30)", fib_30())
    print("cache info", fib.cache_info())


def your_turn() -> None:
    # Write @once that runs a function only the first time it is called.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
