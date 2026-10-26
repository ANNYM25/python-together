# Python Together

A shared lab for **Python, mathematics, machine learning, and fintech**.

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

## Setup

You need **Python 3.11+**.

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python 01-python-foundations/01_hello_and_types.py
```

Optional: Jupyter for the data and ML tracks.

```bash
jupyter lab
```

## Lesson style

Every `.py` file is a lesson you can run:

```bash
python 06-mathematics/02_calculus.py
```

Inside each file you will see:

1. A short "why this exists"
2. Worked examples that print
3. A `YOUR TURN` section at the bottom

Do not skip the `YOUR TURN` blocks. That is where the learning happens.

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
