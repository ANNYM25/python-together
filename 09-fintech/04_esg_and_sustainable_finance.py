"""ESG and sustainable finance (synthetic).

Why this exists: a score is a model with a policy wrapped around it.
Run: python 09-fintech/04_esg_and_sustainable_finance.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Issuer:
    name: str
    e: float  # 0-100, higher is better in this toy
    s: float
    g: float
    fossil_flag: bool


def blended_score(issuer: Issuer, weights: tuple[float, float, float] = (0.4, 0.3, 0.3)) -> float:
    we, ws, wg = weights
    return we * issuer.e + ws * issuer.s + wg * issuer.g


def eligible(issuer: Issuer, floor: float = 55.0) -> bool:
    if issuer.fossil_flag:
        return False
    return blended_score(issuer) >= floor


def demo() -> None:
    book = [
        Issuer("North Wind", 82, 70, 65, False),
        Issuer("City Transit", 74, 80, 60, False),
        Issuer("Old Refinery", 40, 55, 50, True),
        Issuer("Agri Co-op", 60, 78, 58, False),
    ]
    for issuer in book:
        print(
            issuer.name,
            "score",
            round(blended_score(issuer), 1),
            "eligible",
            eligible(issuer),
        )

    # Toy green bond: proceeds tagged to a wind project, coupon 3.2%
    face, coupon, years = 100.0, 0.032, 5
    cash = [coupon * face] * (years - 1) + [coupon * face + face]
    print("green bond coupons + principal", cash)


def your_turn() -> None:
    # Reweight E/S/G to (0.6, 0.2, 0.2) and list who falls out of the eligible set.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
