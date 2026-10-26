"""Search.

Why this exists: binary search is the skeleton of many numeric methods (including root finding).
Run: python 05-algorithms/search.py
"""

from __future__ import annotations


def linear_search(items: list[int], target: int) -> int:
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1


def binary_search(sorted_items: list[int], target: int) -> int:
    lo, hi = 0, len(sorted_items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        guess = sorted_items[mid]
        if guess == target:
            return mid
        if guess < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def demo() -> None:
    xs = [3, 1, 4, 1, 5, 9]
    print("linear 5", linear_search(xs, 5))
    ys = sorted(xs)
    print("binary 5", binary_search(ys, 5), "missing", binary_search(ys, 2))


if __name__ == "__main__":
    demo()
