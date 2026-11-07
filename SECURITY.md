# Security policy

This is an educational repository. It is designed to be **leak-proof by default**:

- **No secrets, ever.** Every dataset is synthetic or built into a library. There
  are no API keys, tokens, brokerage logins, or real client/market data anywhere.
- **Automated secret scanning.** A [gitleaks](https://github.com/gitleaks/gitleaks)
  GitHub Action (`.github/workflows/gitleaks.yml`) scans every push and pull
  request against the full history. Any detected credential fails the build.
- **No executed outputs committed.** Notebooks are committed without run outputs,
  so no accidental data ends up in version control.

## If you need to add data or a key

Don't commit it. Instead:

- Use a synthetic / generated dataset (see how the lessons use `numpy.random`).
- For a genuine credential during local experiments, put it in a `.env` file
  (already covered by `.gitignore`) and read it with `os.environ` — never hard-code
  it in a notebook cell.

## Reporting something sensitive

If you find a committed secret or a security concern, **do not open a public
issue.** Contact the maintainers directly:

- Lucifer — [@R341CUL](https://github.com/R341CUL)
- Anny — [@ANNYM25](https://github.com/ANNYM25)

We'll rotate anything exposed and scrub it from history.
