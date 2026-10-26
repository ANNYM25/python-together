"""Unpacking and slicing.

Why this exists: batch tensors, n-grams, and train/test splits are slice problems.
Run: python 03-pythonic-tools/01_unpacking_and_slicing.py
"""


def demo() -> None:
    elems = [1, 2, 3, 4, 5]
    first, *middle, last = elems
    print(first, middle, last)

    days = list(range(10))
    print("even idx", days[::2])
    print("reverse", days[::-1])

    # Insert without a loop
    days[1:1] = [0.5]
    print("inserted", days)

    train, *rest = ["fold0", "fold1", "fold2", "fold3"]
    print("holdout-style", train, rest)


def ngrams(tokens: list[str], n: int):
    for i in range(len(tokens) - n + 1):
        yield tuple(tokens[i : i + n])


def your_turn() -> None:
    tokens = "rates stay higher for longer".split()
    print(list(ngrams(tokens, 2)))
    # Change ngrams to skip stopwords like "for".


if __name__ == "__main__":
    demo()
    your_turn()
