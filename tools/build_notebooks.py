"""Build runnable Jupyter notebooks from the lesson source files.

Every lesson is authored as a *flat, top-to-bottom* ``.py`` file in jupytext
"percent" format:

    # %% [markdown]
    # ## A heading and some prose a beginner can read

    # %%
    x = 2 + 3
    print(x)

That format is:

* readable  -- no ``def demo()`` / ``if __name__ == "__main__"`` scaffolding
               hiding the lesson from a beginner,
* runnable  -- ``python lesson.py`` still works,
* reviewable-- a real ``.py`` diff in a pull request instead of raw notebook JSON.

This script turns each ``*.py`` source into a ``*.ipynb`` notebook sitting next
to it, and injects an "Open in Colab" badge as the first cell so a learner can
launch the exact lesson in Google Colab with one click.

Usage:
    python tools/build_notebooks.py           # build every lesson
    python tools/build_notebooks.py 01-python-foundations   # one track
"""

from __future__ import annotations

import sys
from pathlib import Path

import jupytext
import nbformat

# --- Edit these two lines if your GitHub org/repo name is different ----------
GITHUB_ORG = "R341CUL"
GITHUB_REPO = "python-together"
DEFAULT_BRANCH = "main"
# -----------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent

# Folders we never scan for lessons.
SKIP_DIRS = {".git", ".venv", "venv", "tools", "__pycache__", ".pytest_cache",
            "progress", "resources", "docs", ".github"}

KERNELSPEC = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3",
}


def colab_badge_cell(ipynb_relpath: str) -> nbformat.NotebookNode:
    """A markdown cell with a clickable 'Open in Colab' badge for this lesson."""
    url = (
        f"https://colab.research.google.com/github/"
        f"{GITHUB_ORG}/{GITHUB_REPO}/blob/{DEFAULT_BRANCH}/{ipynb_relpath}"
    )
    badge = (
        f'<a href="{url}" target="_parent">'
        f'<img src="https://colab.research.google.com/assets/colab-badge.svg" '
        f'alt="Open In Colab"/></a>'
    )
    return nbformat.v4.new_markdown_cell(badge)


def build_one(py_path: Path) -> Path:
    """Convert a single percent-format .py lesson into a sibling .ipynb."""
    nb = jupytext.read(py_path)

    ipynb_path = py_path.with_suffix(".ipynb")
    ipynb_relpath = ipynb_path.relative_to(REPO_ROOT).as_posix()

    # Drop any previously-injected badge so rebuilds stay idempotent.
    cells = list(nb.cells)
    if cells and cells[0].cell_type == "markdown" and "colab-badge.svg" in cells[0].source:
        cells = cells[1:]
    nb.cells = [colab_badge_cell(ipynb_relpath), *cells]

    nb.metadata["kernelspec"] = KERNELSPEC
    nb.metadata.setdefault("language_info", {"name": "python"})

    nbformat.write(nb, ipynb_path)
    return ipynb_path


def iter_lesson_sources(root: Path):
    for py_path in sorted(root.rglob("*.py")):
        if any(part in SKIP_DIRS for part in py_path.relative_to(REPO_ROOT).parts):
            continue
        # Only convert files that are actually in percent/notebook format.
        text = py_path.read_text(encoding="utf-8")
        if "# %%" in text:
            yield py_path


def main(argv: list[str]) -> int:
    scope = REPO_ROOT / argv[0] if argv else REPO_ROOT

    if scope.is_file():
        sources = [scope]
    else:
        sources = list(iter_lesson_sources(scope))

    built = 0
    for py_path in sources:
        out = build_one(py_path)
        print(f"built {out.relative_to(REPO_ROOT)}")
        built += 1
    print(f"\n{built} notebook(s) built.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
