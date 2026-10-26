"""Classes.

Why this exists: a Position is more than a dict once it grows behavior.
Run: python 02-intermediate-python/07_classes.py
"""

from __future__ import annotations


class Position:
    def __init__(self, ticker: str, shares: float, price: float) -> None:
        self.ticker = ticker
        self.shares = shares
        self.price = price

    def market_value(self) -> float:
        return self.shares * self.price

    def __repr__(self) -> str:
        return f"Position({self.ticker!r}, shares={self.shares}, price={self.price})"


class LinearModel:
    """y_hat = slope * x + intercept — a tiny stand-in for later ML."""

    def __init__(self, slope: float, intercept: float = 0.0) -> None:
        self.slope = slope
        self.intercept = intercept

    def predict(self, x: float) -> float:
        return self.slope * x + self.intercept


def demo() -> None:
    lot = Position("BND", shares=40, price=72.1)
    print(lot, "value", round(lot.market_value(), 2))
    model = LinearModel(slope=0.8, intercept=0.1)
    print("y_hat", model.predict(2.0))


def your_turn() -> None:
    # Add a method Position.weight(total_value) and print weights for two lots.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
