"""Dates and regular expressions.

Why this exists: prices have timestamps; reports have patterns.
Run: python 02-intermediate-python/06_dates_and_regex.py
"""

from __future__ import annotations

import re
from datetime import datetime, timedelta


def demo() -> None:
    start = datetime(2024, 1, 15)
    print("iso", start.date().isoformat())
    print("plus 7 days", (start + timedelta(days=7)).date())

    raw = "ISIN US0378331005 weight 0.08; ISIN US5949181045 weight 0.11"
    isins = re.findall(r"[A-Z]{2}[A-Z0-9]{9}[0-9]", raw)
    print("isins", isins)

    ticker_ok = bool(re.fullmatch(r"[A-Z]{1,5}", "MSFT"))
    print("ticker_ok", ticker_ok)


def your_turn() -> None:
    # Extract all percentages like 12.5% from a sentence using re.findall.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
