"""A small sklearn pipeline.

Why this exists: scaling + model + split is the real unit of work, not a lone estimator.
Run: python 08-machine-learning/04_sklearn_pipeline.py
"""

from __future__ import annotations

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def demo() -> None:
    x, y = make_classification(
        n_samples=400,
        n_features=6,
        n_informative=4,
        n_redundant=0,
        weights=[0.8, 0.2],
        random_state=0,
    )
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, stratify=y, random_state=0
    )
    pipe = Pipeline(
        [
            ("scale", StandardScaler()),
            ("clf", LogisticRegression(max_iter=500)),
        ]
    )
    pipe.fit(x_train, y_train)
    y_hat = pipe.predict(x_test)
    print(classification_report(y_test, y_hat, digits=3))


def your_turn() -> None:
    # Print pipe.predict_proba on the first 5 test rows.
    pass


if __name__ == "__main__":
    demo()
    your_turn()
