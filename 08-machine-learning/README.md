# Machine learning — from first principles to your own network

This is the deep track. We build the intuition *and* the code: first by hand in
NumPy (so nothing is magic), then with scikit-learn (so you're productive), then
we climb to neural networks, convolutions, and — in `10-projects/` — your own
tiny language model.

Everything here runs on **synthetic or built-in datasets** so it works in Colab
with no downloads and no API keys. No production or investment claims.

## The map of ML (read `01_what_is_ml` first)

```
Machine learning
├── Supervised        you have labelled answers (y)
│   ├── Regression      predict a number      (price, return, risk)
│   └── Classification  predict a category    (default / no-default, spam / not)
├── Unsupervised      no labels — find structure
│   ├── Clustering      group similar rows     (customer segments, regimes)
│   └── Dimensionality  compress features      (PCA)
└── (Reinforcement)   learn from reward — mentioned, not covered here
```

Two vocab pairs the field keeps using:

| Pair | Plain meaning |
| --- | --- |
| **labelled vs unlabelled** data | do we *know* the right answer for each row? → supervised vs unsupervised |
| **structured vs unstructured** data | tables of numbers (CSV, SQL) vs raw text / images / audio |

Classic ML (trees, KNN, logistic regression) loves **structured** data. Deep
learning earns its keep on **unstructured** data — images → CNNs, text → the
transformers behind LLMs.

## Lesson order

| # | Lesson | You build |
| --- | --- | --- |
| 01 | `what_is_ml` | the taxonomy above, train/test split, overfitting — with tiny live demos |
| 02 | `linear_regression_from_scratch` | gradient descent fitting a line, by hand |
| 03 | `classification_and_metrics` | confusion matrix, precision/recall/F1 (why accuracy lies) |
| 04 | `knn` | k-nearest-neighbours from scratch, then with sklearn |
| 05 | `sklearn_pipeline` | scale → model → split → report, the real unit of work |
| 06 | `unsupervised` | PCA + k-means on data with no labels |
| 07 | `neural_net_from_scratch` | a one-hidden-layer net + backprop in NumPy |
| 08 | `cnn_intro` | what a convolution *is*, a hand-rolled edge filter, then the PyTorch shape |
| 09 | `kaggle_workflow` | how to attack a Kaggle dataset: EDA → baseline → CV → submission |

## Then go build (`10-projects/`)

- **Build your own neural network** — a reusable `NeuralNet` class you train on a
  dataset of your choice.
- **A tiny language model** — a character-level model, the same idea an LLM scales
  up a billion-fold. Watch it babble, then learn to spell.

## Going further (needs extra installs)

The from-scratch lessons use only NumPy. For real deep learning, install PyTorch
(`pip install torch`) — lesson 08 shows the exact shape your NumPy code maps onto.
Great next datasets: MNIST (digits), Fashion-MNIST, and the Titanic / House Prices
starters on [kaggle.com](https://www.kaggle.com/competitions).
