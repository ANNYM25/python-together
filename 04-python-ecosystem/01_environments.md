# Environments and packaging

Use one virtual environment per project. This repo's is `.venv/` at the root.

Useful tools, in the order we actually use them:

1. **venv** — isolation (already in the standard library)
2. **pip** — install from `requirements.txt`
3. **pytest** — run `05-algorithms/tests`
4. **uv** (optional) — a fast installer if you outgrow pip

CPython compiles source to bytecode (`.pyc`) and then interprets it. You almost never commit `.pyc` files.

`PYTHONPATH` adds extra folders to the import search. Prefer installing the project, or running from the repo root, over secretly mutating `PYTHONPATH`.
