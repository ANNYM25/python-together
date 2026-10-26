"""Credit-style labels on synthetic borrowers.

Why this exists: fintech underwriting is classification with a cost of being wrong.
Run: python 09-fintech/05_credit_and_fintech_data.py
"""

from __future__ import annotations

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split


def make_borrowers(n: int = 600, seed: int = 0):
    rng = np.random.default_rng(seed)
    income = rng.lognormal(mean=10.5, sigma=0.4, size=n)
    utilization = rng.uniform(0.05, 0.95, size=n)
    late_12m = rng.poisson(0.4, size=n)
    # Higher utilization and lates raise default odds; income lowers them
    logit = -2.2 + 2.4 * utilization + 0.7 * late_12m - 0.00004 * income
    p = 1 / (1 + np.exp(-logit))
    y = rng.binomial(1, p)
    x = np.column_stack([income, utilization, late_12m])
    return x, y


def demo() -> None:
    x, y = make_borrowers()
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, stratify=y, random_state=0
    )
    model = LogisticRegression(max_iter=400)
    model.fit(x_train, y_train)
    proba = model.predict_proba(x_test)[:, 1]
    print("default rate", round(float(y.mean()), 3))
    print("auc", round(roc_auc_score(y_test, proba), 3))
    print("coef income, util, lates", model.coef_.round(4))


def your_turn() -> None:
    # At threshold 0.25, print how many test borrowers would be declined.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
