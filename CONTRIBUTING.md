# Contributing (you and Anny)

This lab has two first-class authors. Treat every lesson as something the other person may teach from.

## Before you push

1. Edit the lesson **notebook** (`.ipynb`) directly in Jupyter or Colab.
2. **Run it top to bottom** — every cell must execute with no error. (`make validate`
   runs the whole repo; it's our test suite.)
3. Lessons that implement something (algorithms, from-scratch ML) should include a
   `✔️ Quick check` cell with `assert`s so correctness is verified on every run.
4. Keep examples small enough to read on a laptop screen.
5. Put exercises in a `🏋️ Your turn` cell, not as hidden homework in another file.

## How we split work

Use this as a default, then ignore it when a lesson needs both brains:

| Owner | Usually commits here |
| --- | --- |
| CS / ML track | `05-algorithms/`, `06-mathematics/`, `08-machine-learning/` |
| Fintech track | `09-fintech/`, money-flavored projects in `10-projects/` |
| Shared | foundations, intermediate Python, data science, README, progress log |

When you open a pull request, name the other person as reviewer if the lesson crosses tracks (example: a credit model uses both sklearn and a PD/LGD story).

## Lesson shape

Lessons are **flat, top-to-bottom** notebooks. No `def demo()` wrappers — a
beginner reads and runs the code directly. The cell order is always:

1. **Title + why** (markdown) — one or two sentences, ideally an ML or finance hook.
2. **Concept → code** (markdown, then a short flat code cell) — repeat a few times.
3. **`🏋️ Your turn`** (markdown + a starter code cell with blanks).
4. **`✅ What you learned`** (markdown recap) + a pointer to the next lesson.

Keep the first cell an "Open in Colab" badge so learners can launch it in one
click. (`tools/build_notebooks.py` can regenerate a notebook from a percent-format
`.py` if you prefer authoring that way, but it's optional — the `.ipynb` is the
source of truth.)

## Commit messages

Write why, not a file list.

- `teach finite differences before sympy derivatives`
- `add ESG scorecard using dummy holdings`
- `fix binary search off-by-one on empty list`

## Adding Anny (or you) on GitHub

See **[docs/github-for-two-people.md](docs/github-for-two-people.md)** for the full
walkthrough (organization vs. collaborator, how credit works, first push). Short
version: use a GitHub **Organization** so neither of you "owns" it, set your git
identity so your commits count, and push through short-lived branches.

Do not commit API keys, brokerage logins, or real client data. Fintech examples in this lab use synthetic numbers only.
