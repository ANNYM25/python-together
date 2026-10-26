"""Sorting.

Why this exists: merge sort makes the 'divide, sort, combine' pattern obvious.
Run: python 05-algorithms/sort.py
"""

from __future__ import annotations


def merge_sort(items: list[int]) -> list[int]:
    if len(items) <= 1:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    out: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


def quicksort(items: list[int]) -> list[int]:
    if len(items) <= 1:
        return items[:]
    pivot = items[len(items) // 2]
    less = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    more = [x for x in items if x > pivot]
    return quicksort(less) + equal + quicksort(more)


def demo() -> None:
    sample = [5, 1, 4, 2, 8, 5, 0]
    print("merge", merge_sort(sample))
    print("quick", quicksort(sample))


if __name__ == "__main__":
    demo()
