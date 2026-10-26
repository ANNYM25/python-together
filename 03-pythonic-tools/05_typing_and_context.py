"""Type hints and context managers.

Why this exists: hints catch shape bugs; `with` closes files even when code fails.
Run: python 03-pythonic-tools/05_typing_and_context.py
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator


def sharpe(mean_excess: float, vol: float) -> float:
    if vol <= 0:
        raise ValueError("vol must be positive")
    return mean_excess / vol


@contextmanager
def announce(label: str) -> Iterator[None]:
    print(f"start {label}")
    try:
        yield
    finally:
        print(f"end {label}")


def demo() -> None:
    print("sharpe", round(sharpe(0.06, 0.12), 3))
    with announce("fit"):
        print("pretend to train")


def your_turn() -> None:
    # Add an Optional[float] argument to sharpe for a risk-free rate already netted out.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
