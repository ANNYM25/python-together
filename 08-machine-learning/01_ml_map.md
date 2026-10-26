# A small map of machine learning

- **Supervised** — you have labels. Regression (number) or classification (class).
- **Unsupervised** — you do not. Clustering, PCA, anomaly flags.
- **Generalization** — performance on data the fit did not see. That is the whole game.

A model is a function `f(x) ≈ y` plus a **loss** that says how wrong is too wrong, plus a procedure that walks the parameters downhill.

In this lab, `x` might be a company's features or a window of returns. `y` might be default / no-default, or next-month excess return. Start with the from-scratch line in `02_from_scratch_linear_regression.py` so sklearn does not feel like magic.
