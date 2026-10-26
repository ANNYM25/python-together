"""Exceptions.

Why this exists: bad input is normal. Crash only when you cannot recover.
Run: python 02-intermediate-python/04_exceptions.py
"""


def parse_weight(text: str) -> float:
    try:
        value = float(text)
    except ValueError as exc:
        raise ValueError(f"not a number: {text!r}") from exc
    if not 0 <= value <= 1:
        raise ValueError("weights live in [0, 1]")
    return value


def safe_ratio(numer: float, denom: float) -> float | None:
    try:
        return numer / denom
    except ZeroDivisionError:
        return None
    finally:
        # finally always runs: close files, stop timers, unlock.
        pass


def demo() -> None:
    print("ok", parse_weight("0.25"))
    print("ratio", safe_ratio(1, 0))
    try:
        parse_weight("12%")
    except ValueError as exc:
        print("caught", exc)


def your_turn() -> None:
    # Write load_price(text) that returns None on failure instead of raising.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
