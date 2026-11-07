# Running lessons locally with Jupyter

Prefer your own machine over Colab? Here's the full local setup. You need
**Python 3.11+**.

## One-time setup

```bash
# from the repo folder
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Open the notebooks

```bash
jupyter lab
```

Your browser opens JupyterLab. Navigate to any track folder and double-click a
`.ipynb` file. Run cells with **Shift+Enter**, top to bottom.

## How this repo works

Every lesson **is** a Jupyter notebook (`.ipynb`) — that's the source of truth.
You read it, run it, and (if you're contributing) edit it directly in Jupyter or
Colab.

- The **first cell** of each lesson is an "Open in Colab" badge.
- Explanation cells (markdown) alternate with runnable code cells.
- Each lesson ends with a `🏋️ Your turn` cell and a recap.

## Editing a lesson

1. Open the `.ipynb` in JupyterLab (or Colab).
2. Edit the markdown/code cells.
3. **Run it top to bottom** — every cell must execute with no error.
4. Save, commit, push (see [github-for-two-people.md](github-for-two-people.md)).

Want to double-check a whole track runs before you push?

```bash
make validate        # executes every notebook, fails loudly if one breaks
```

## "Testing" in this repo

There's no separate test suite to run — each lesson that implements something
(algorithms, from-scratch ML) carries its own `✔️ Quick check` cell full of
`assert`s. If the notebook runs top to bottom without error, it's correct. CI and
`make validate` execute every notebook for exactly this reason.
