# Modules, packages, and environments

Python looks for imports on `sys.path`: the current directory, then the environment's `site-packages`.

```python
import math
from pathlib import Path

print(math.sqrt(16))
print(Path(".").resolve())
```

A **package** is a folder of modules. A **virtual environment** is an isolated copy of Python's third-party library folder so this lab's NumPy does not fight another project's NumPy.

Create one at the repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

When the prompt shows `(.venv)`, `pip list` is this lab, not the whole machine.

`pip freeze` writes exact versions. That is useful for a report; `requirements.txt` in this repo stays a little looser so installs keep working.

Do not commit `.venv/`.
