"""Plots.

Why this exists: a chart is how you notice a bug before a metric does.
Run: python 07-data-science/03_visualization.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent / "equity_curve.png"


def demo() -> None:
    rng = np.random.default_rng(2)
    rets = rng.normal(0.0004, 0.01, size=252)
    curve = np.cumprod(1 + rets)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(curve, color="#1f4e5f")
    ax.set_title("Synthetic equity curve")
    ax.set_xlabel("day")
    ax.set_ylabel("growth of 1")
    fig.tight_layout()
    fig.savefig(OUT, dpi=120)
    plt.close(fig)
    print("wrote", OUT)


def your_turn() -> None:
    # Histogram the returns on a second figure and save it next to this file.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
