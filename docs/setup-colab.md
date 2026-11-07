# Running a lesson in Google Colab (zero install)

Colab is a free Jupyter notebook that runs in your browser on Google's machines.
Nothing to install, works on any laptop or Chromebook. Perfect for beginners.

## The one-click way

Every lesson notebook has an **"Open in Colab"** badge as its first cell. On
GitHub, open any `.ipynb` file and click the badge — it launches that exact
lesson in Colab.

> The badge points at the repo path, so it only works once the repo is pushed to
> GitHub under the org/name configured in `tools/build_notebooks.py`.

## The manual way (any notebook on GitHub)

1. Go to [colab.research.google.com](https://colab.research.google.com).
2. **File → Open notebook → GitHub** tab.
3. Paste the repo URL (e.g. `ANNYM25/python-together`) and pick the
   `.ipynb` you want.

## How to use a notebook

- A notebook is a stack of **cells**. Text cells explain; code cells run.
- Click a code cell and press **Shift+Enter** to run it. Output appears below.
- Run cells **top to bottom** — later cells depend on earlier ones.
- Edit any code and re-run. Breaking things is how you learn; you can't harm
  anything.

## Installing the data/ML libraries

Colab already has `numpy`, `pandas`, `matplotlib`, and `scikit-learn`. The
foundations and intermediate lessons need nothing extra. If a lesson ever needs a
package Colab doesn't have, run this in a cell:

```python
!pip install sympy
```

(The `!` runs a shell command from inside a notebook.)

## Saving your work

Colab opens the file read-only from GitHub. To keep your edits:
**File → Save a copy in Drive** (saves to your Google Drive), or
**File → Download → .ipynb**.

To contribute a change back to the repo, you can edit the notebook in Colab and
**File → Save a copy to GitHub** (it commits straight to a branch), or edit
locally in Jupyter and push (see [setup-jupyter.md](setup-jupyter.md)).
