# Python Together

[![notebooks](https://github.com/R341CUL/python-together/actions/workflows/notebooks.yml/badge.svg)](https://github.com/R341CUL/python-together/actions/workflows/notebooks.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A shared lab for **Python, mathematics, machine learning, and fintech** — taught as
**runnable notebooks** you can open in one click.

> Every lesson is a notebook: read the explanation, run the code cell under it,
> then do the `🏋️ Your turn`. Open any lesson in **Google Colab** (nothing to
> install) or run it locally in **Jupyter**.

This repository is built for two people who will both commit:

- **You** — bachelor's in computer science and machine learning
- **Annie** — master's in sustainable finance and fintech

Anyone who can write a little Python can start in `01-python-foundations/` and walk all the way through calculus, algorithms, models, and money.

The five public repos you named were used as a **topic map** (what a complete path should cover). The lessons here are original teaching material written for this lab. They are not copies of those projects.

## How to walk the lab

| Track | Folder | What you leave with |
| --- | --- | --- |
| Start | `00-start-here/` | Setup, how we learn, first run |
| Foundations | `01-python-foundations/` | Types, strings, collections, control flow |
| Intermediate | `02-intermediate-python/` | Functions, files, classes, errors, regex |
| Pythonic tools | `03-pythonic-tools/` | Generators, decorators, dunders, caching |
| Ecosystem | `04-python-ecosystem/` | Environments, how CPython runs, tests, lint |
| Algorithms | `05-algorithms/` | Search, sort, lists, graphs, recursion |
| Mathematics | `06-mathematics/` | Algebra, calculus, linear algebra, probability |
| Data | `07-data-science/` | NumPy, pandas, plots, statistics |
| Machine learning | `08-machine-learning/` | From-scratch models, sklearn, a tiny net |
| Fintech | `09-fintech/` | Time value of money, risk, portfolios, ESG |
| Projects | `10-projects/` | Shared capstones you both can ship |

Suggested split of ownership (not a wall — both of you can edit anything):

- **You** often lead: algorithms, math-for-ML, models, evaluation.
- **Annie** often leads: money math, returns and risk, ESG, sustainable-finance case studies.

Keep a living log in `progress/PROGRESS.md`.

## Two ways to run a lesson

**1. Google Colab — zero install (best for starting out).**
Open any `.ipynb` on GitHub and click its **Open in Colab** badge. Full guide:
[docs/setup-colab.md](docs/setup-colab.md).

**2. Locally with Jupyter.**

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab                        # then open any lesson .ipynb
```

Full local guide (and how to author/edit lessons):
[docs/setup-jupyter.md](docs/setup-jupyter.md).

## How a lesson is built

Every lesson **is** a Jupyter notebook (`.ipynb`) — open it in Colab or Jupyter,
read the explanation, run the code cell under it. Inside every lesson you'll
find, in order:

1. A short **why this matters** (usually an ML or finance hook)
2. Plain, **flat** worked code — read top to bottom, no scaffolding to decode
3. A **`🏋️ Your turn`** cell — edit it and run it

Do not skip the `🏋️ Your turn` cells. That is where the learning happens.

## Working on this together

Two authors, both committing. See
**[docs/github-for-two-people.md](docs/github-for-two-people.md)** for how to set
it up as a GitHub organization so you both own it equally, and how commit credit
works. Contribution rules live in [CONTRIBUTING.md](CONTRIBUTING.md).

## What this is not

- Not a dump of other people's READMEs, notebooks, or algorithm trees
- Not a certificate mill
- Not only CS, and not only finance

It is one place where a CS/ML person and a sustainable-finance person can meet in Python.

## License

MIT. See `LICENSE`.

## Inspired by (topic coverage only)

- [Python-KIT](https://github.com/avinash201199/Python-KIT)
- [30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python)
- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)
- [understanding-the-python-ecosystem](https://github.com/brunocampos01/understanding-the-python-ecosystem)
- [python-is-cool](https://github.com/chiphuyen/python-is-cool)
