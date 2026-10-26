"""A tiny in-memory ledger.

Run: python 10-projects/01_personal_finance_cli.py
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Ledger:
    rows: list[tuple[str, float]] = field(default_factory=list)

    def add(self, label: str, amount: float) -> None:
        self.rows.append((label, amount))

    def balance(self) -> float:
        return sum(amount for _, amount in self.rows)

    def report(self) -> None:
        for label, amount in self.rows:
            sign = "+" if amount >= 0 else "-"
            print(f"{label:20} {sign}{abs(amount):8.2f}")
        print(f"{'balance':20}  {self.balance():8.2f}")


def main() -> None:
    book = Ledger()
    book.add("salary", 3200)
    book.add("rent", -1100)
    book.add("groceries", -240)
    book.add("index fund", -400)
    book.report()


if __name__ == "__main__":
    main()
