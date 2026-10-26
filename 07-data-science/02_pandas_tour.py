"""pandas tour.

Why this exists: finance and ML both start as a table with a date index.
Run: python 07-data-science/02_pandas_tour.py
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def demo() -> None:
    rng = np.random.default_rng(1)
    idx = pd.date_range("2024-01-02", periods=8, freq="B")
    df = pd.DataFrame(
        {
            "equity": rng.normal(0.0005, 0.012, size=len(idx)),
            "bond": rng.normal(0.0001, 0.003, size=len(idx)),
        },
        index=idx,
    )
    df["blend"] = 0.6 * df["equity"] + 0.4 * df["bond"]
    print(df.round(4))
    print("corr\n", df.corr().round(3))
    print("rolling 3d equity vol", df["equity"].rolling(3).std().round(4))


def your_turn() -> None:
    # Add a column that is 1 on days equity beat bonds, else 0, and print the hit rate.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
