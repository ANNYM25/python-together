"""Mixed foundation drills.

Run: python 01-python-foundations/exercises.py
Fill each function. The checks at the bottom should all print OK.
"""

from __future__ import annotations


def euclid(x1: float, y1: float, x2: float, y2: float) -> float:
    """Distance between two points on a plane."""
    raise NotImplementedError


def unique_sorted(words: list[str]) -> list[str]:
    """Lowercase, unique, alphabetically sorted words."""
    raise NotImplementedError


def value_weighted_return(weights: list[float], returns: list[float]) -> float:
    """Portfolio return = sum(weight_i * return_i). Lengths must match."""
    raise NotImplementedError


def main() -> None:
    checks = [
        (round(euclid(2, 3, 10, 8), 4), 9.4339, "euclid"),
        (unique_sorted(["Bond", "bond", "Cash"]), ["bond", "cash"], "unique_sorted"),
        (round(value_weighted_return([0.6, 0.4], [0.1, -0.05]), 4), 0.04, "vw return"),
    ]
    for got, expected, name in checks:
        status = "OK" if got == expected else f"FAIL got={got} expected={expected}"
        print(name, status)


if __name__ == "__main__":
    main()
