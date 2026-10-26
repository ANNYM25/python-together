"""Classification metrics.

Why this exists: accuracy lies when defaults are rare.
Run: python 08-machine-learning/03_classification_and_metrics.py
"""

from __future__ import annotations

import numpy as np


def confusion(y_true: np.ndarray, y_hat: np.ndarray) -> dict[str, int]:
    tp = int(np.sum((y_true == 1) & (y_hat == 1)))
    tn = int(np.sum((y_true == 0) & (y_hat == 0)))
    fp = int(np.sum((y_true == 0) & (y_hat == 1)))
    fn = int(np.sum((y_true == 1) & (y_hat == 0)))
    return {"tp": tp, "tn": tn, "fp": fp, "fn": fn}


def precision_recall(cm: dict[str, int]) -> tuple[float, float]:
    p = cm["tp"] / (cm["tp"] + cm["fp"] + 1e-12)
    r = cm["tp"] / (cm["tp"] + cm["fn"] + 1e-12)
    return p, r


def demo() -> None:
    y_true = np.array([0, 0, 0, 0, 0, 1, 1, 1])
    y_hat = np.array([0, 0, 0, 1, 0, 1, 0, 1])
    cm = confusion(y_true, y_hat)
    p, r = precision_recall(cm)
    acc = (cm["tp"] + cm["tn"]) / y_true.size
    print(cm, "acc", round(acc, 3), "prec", round(p, 3), "rec", round(r, 3))


def your_turn() -> None:
    # Implement F1 = 2pr / (p+r) and print it for the demo arrays.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
