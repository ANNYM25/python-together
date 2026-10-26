"""Dictionaries.

Why this exists: a row in a table, a JSON payload, and a model's hyperparameters are maps.
Run: python 01-python-foundations/06_dictionaries.py
"""


def demo() -> None:
    position = {"ticker": "MSFT", "shares": 12, "price": 410.5}
    print(position["ticker"])
    position["shares"] += 3
    position["sector"] = "technology"
    print(position)

    print("keys", list(position.keys()))
    print("market value", position["shares"] * position["price"])

    portfolio = {
        "MSFT": {"shares": 12, "price": 410.5},
        "BND": {"shares": 40, "price": 72.1},
    }
    total = 0.0
    for ticker, lot in portfolio.items():
        value = lot["shares"] * lot["price"]
        total += value
        print(ticker, value)
    print("total", round(total, 2))


def your_turn() -> None:
    # Add a cash lot to portfolio and recompute total.
    # Then print the weight of each position as a fraction of total.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
