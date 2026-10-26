# Quality and testing

Minimum bar for a lesson you add:

- It runs with `python path/to/file.py`
- New helpers used by more than one file get a pytest

```bash
pytest 05-algorithms/tests -q
```

Style: 4 spaces, snake_case functions, PascalCase classes. A linter is optional; readable names are not.

Keep `try` blocks small so you know *which* line failed.
