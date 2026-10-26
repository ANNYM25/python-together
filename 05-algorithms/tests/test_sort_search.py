from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from search import binary_search, linear_search
from sort import merge_sort, quicksort
from recursion import factorial, fib_dp


def test_linear_and_binary() -> None:
    items = [4, 1, 9, 7]
    assert linear_search(items, 9) == 2
    assert linear_search(items, 3) == -1
    ordered = sorted(items)
    assert binary_search(ordered, 7) == 2
    assert binary_search(ordered, 3) == -1
    assert binary_search([], 1) == -1


def test_sorts() -> None:
    sample = [3, 1, 2, 3, 0]
    assert merge_sort(sample) == [0, 1, 2, 3, 3]
    assert quicksort(sample) == [0, 1, 2, 3, 3]
    assert sample == [3, 1, 2, 3, 0]


def test_recursion() -> None:
    assert factorial(5) == 120
    assert fib_dp(10) == 55
