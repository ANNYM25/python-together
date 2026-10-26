"""Time value of money.

Why this exists: every discount factor is compound interest run backwards.
Run: python 09-fintech/01_money_math.py
"""

from __future__ import annotations


def pv(cashflow: float, rate: float, years: float) -> float:
    return cashflow / (1 + rate) ** years


def npv(rate: float, cashflows: list[float]) -> float:
    """cashflows[0] is t=0 (often a negative outlay)."""
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def irr(cashflows: list[float], lo: float = -0.9, hi: float = 1.0, steps: int = 80) -> float:
    """Bisection on NPV = 0. Fine for a teaching cashflow, not a production solver."""
    for _ in range(steps):
        mid = (lo + hi) / 2
        value = npv(mid, cashflows)
        if value > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def demo() -> None:
    print("pv of 100 in 5y at 6%", round(pv(100, 0.06, 5), 2))
    project = [-1000, 300, 350, 400, 280]
    print("npv 8%", round(npv(0.08, project), 2))
    print("irr", round(irr(project), 4))


def your_turn() -> None:
    # A 4-year green loan: -500, 160, 160, 160, 160. Print NPV at 5% and IRR.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
