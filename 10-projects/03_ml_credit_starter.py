"""Train a credit model on synthetic borrowers and print a short scorecard.

Run: python 10-projects/03_ml_credit_starter.py
"""

from __future__ import annotations

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def make_borrowers(n: int = 800, seed: int = 1):
    rng = np.random.default_rng(seed)
    income = rng.lognormal(mean=10.6, sigma=0.35, size=n)
    utilization = rng.beta(2, 2, size=n)
    late_12m = rng.poisson(0.5, size=n)
    logit = -2.0 + 2.6 * utilization + 0.55 * late_12m - 0.000035 * income
    p = 1 / (1 + np.exp(-logit))
    y = rng.binomial(1, p)
    x = np.column_stack([income, utilization, late_12m])
    return x, y


def main() -> None:
    x, y = make_borrowers()
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, stratify=y, random_state=1
    )
    pipe = Pipeline(
        [
            ("scale", StandardScaler()),
            ("clf", LogisticRegression(max_iter=400)),
        ]
    )
    pipe.fit(x_train, y_train)
    proba = pipe.predict_proba(x_test)[:, 1]
    y_hat = (proba >= 0.35).astype(int)
    print("default rate", round(float(y.mean()), 3))
    print("auc", round(roc_auc_score(y_test, proba), 3))
    print(classification_report(y_test, y_hat, digits=3))


if __name__ == "__main__":
    main()
