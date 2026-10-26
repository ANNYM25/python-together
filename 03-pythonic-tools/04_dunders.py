"""Magic methods (dunders).

Why this exists: pandas objects feel native because they implement +, len, and [].
Run: python 03-pythonic-tools/04_dunders.py
"""

from __future__ import annotations


class Money:
    __slots__ = ("cents",)

    def __init__(self, cents: int) -> None:
        self.cents = int(cents)

    def __add__(self, other: "Money") -> "Money":
        return Money(self.cents + other.cents)

    def __len__(self) -> int:
        return abs(self.cents)

    def __repr__(self) -> str:
        sign = "-" if self.cents < 0 else ""
        value = abs(self.cents)
        return f"{sign}${value // 100}.{value % 100:02d}"


def demo() -> None:
    fee = Money(1250)
    tax = Money(80)
    print(fee + tax)
    print("len (cents magnitude)", len(fee))


def your_turn() -> None:
    # Add __eq__ and a classmethod Money.from_dollars(12.50).
    pass


if __name__ == "__main__":
    demo()
    your_turn()
