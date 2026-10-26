"""Unsupervised: PCA and k-means on toy returns.

Why this exists: you often have features and no labels — regimes, styles, clients.
Run: python 08-machine-learning/05_unsupervised.py
"""

from __future__ import annotations

import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


def demo() -> None:
    rng = np.random.default_rng(5)
    style_a = rng.normal(0.01, 0.02, size=(40, 3))
    style_b = rng.normal(-0.005, 0.03, size=(40, 3))
    x = np.vstack([style_a, style_b])
    z = PCA(n_components=2, random_state=0).fit_transform(x)
    labels = KMeans(n_clusters=2, n_init=10, random_state=0).fit_predict(z)
    print("PCA var ratio", PCA(n_components=2, random_state=0).fit(x).explained_variance_ratio_.round(3))
    print("cluster counts", {int(k): int((labels == k).sum()) for k in np.unique(labels)})


def your_turn() -> None:
    # Try k=3 and print inertia. Does a third cluster earn its keep on this toy?
    pass


if __name__ == "__main__":
    demo()
    your_turn()
