"""Functions.

Why this exists: a named function is how you reuse a formula without copy-paste.
Run: python 02-intermediate-python/01_functions.py
"""

from __future__ import annotations


def simple_return(start: float, end: float) -> float:
    return end / start - 1


def future_value(principal: float, rate: float, years: int, compounds: int = 1) -> float:
    """Compound interest. compounds=1 is annual, 12 is monthly."""
    return principal * (1 + rate / compounds) ** (compounds * years)


def describe(name: str, *skills: str, **meta: str) -> str:
    skill_text = ", ".join(skills) if skills else "none listed"
    extra = ", ".join(f"{k}={v}" for k, v in meta.items())
    return f"{name}: {skill_text}" + (f" ({extra})" if extra else "")


def demo() -> None:
    print("return", round(simple_return(100, 107), 4))
    print("FV annual", round(future_value(1000, 0.05, 10), 2))
    print("FV monthly", round(future_value(1000, 0.05, 10, compounds=12), 2))
    print(describe("Annie", "Python", "ESG", city="studio"))


def your_turn() -> None:
    # Write cagr(start, end, years) and print it for 1000 -> 1610.51 over 10 years.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
