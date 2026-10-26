# Contributing (you and Annie)

This lab has two first-class authors. Treat every lesson as something the other person may teach from.

## Before you push

1. Run the lesson you touched: `python path/to/lesson.py`
2. If you changed algorithms or math helpers, run `pytest 05-algorithms/tests`
3. Keep examples small enough to read on a laptop screen
4. Put exercises in a `YOUR TURN` block, not as hidden homework in another file

## How we split work

Use this as a default, then ignore it when a lesson needs both brains:

| Owner | Usually commits here |
| --- | --- |
| CS / ML track | `05-algorithms/`, `06-mathematics/`, `08-machine-learning/` |
| Fintech track | `09-fintech/`, money-flavored projects in `10-projects/` |
| Shared | foundations, intermediate Python, data science, README, progress log |

When you open a pull request, name the other person as reviewer if the lesson crosses tracks (example: a credit model uses both sklearn and a PD/LGD story).

## Lesson template

```python
"""Short title.

Why this exists: one sentence.
Run: python this_file.py
"""

def demo() -> None:
    print("worked example")


def your_turn() -> None:
    # TODO: replace this with the exercise
    pass


if __name__ == "__main__":
    demo()
    your_turn()
```

## Commit messages

Write why, not a file list.

- `teach finite differences before sympy derivatives`
- `add ESG scorecard using dummy holdings`
- `fix binary search off-by-one on empty list`

## Adding Annie (or you) on GitHub later

1. Create an empty GitHub repository
2. Add the other person as a collaborator
3. Both clone, both push to `main` through short-lived branches

Do not commit API keys, brokerage logins, or real client data. Fintech examples in this lab use synthetic numbers only.
