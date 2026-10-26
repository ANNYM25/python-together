"""Hello Python and core types.

Why this exists: you need a mental map of what a value *is* before you model data.
Run: python 01-python-foundations/01_hello_and_types.py
"""


def demo() -> None:
    print("Hello, Python Together.")
    print("2 + 3 =", 2 + 3)
    print("3 ** 2 =", 3**2)

    examples = {
        "int": 10,
        "float": 9.81,
        "complex": 2 + 3j,
        "str": "Annie",
        "bool": True,
        "list": [0.02, -0.01, 0.015],
        "tuple": ("train", "validate", "test"),
        "set": {"equity", "bond", "cash"},
        "dict": {"ticker": "AAPL", "weight": 0.12},
    }
    for name, value in examples.items():
        print(f"{name:8} {type(value).__name__:8} {value}")


def your_turn() -> None:
    # Print your name, the year you started coding, and the type of each.
    # Then store a tiny portfolio as a dict: three tickers and weights.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
