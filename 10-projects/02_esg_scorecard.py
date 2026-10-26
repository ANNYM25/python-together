"""ESG scorecard over synthetic issuers.

Run: python 10-projects/02_esg_scorecard.py
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ESG_PATH = Path(__file__).resolve().parents[1] / "09-fintech" / "04_esg_and_sustainable_finance.py"


def load_esg():
    spec = importlib.util.spec_from_file_location("esg_lab", ESG_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {ESG_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    esg = load_esg()
    issuers = [
        esg.Issuer("Harbor Solar", 88, 72, 70, False),
        esg.Issuer("River Housing", 71, 90, 66, False),
        esg.Issuer("Metals Inc", 48, 52, 61, False),
        esg.Issuer("Legacy Coal", 22, 40, 44, True),
    ]
    ranked = sorted(issuers, key=esg.blended_score, reverse=True)
    print(f"{'issuer':16} {'score':>7} {'in':>6}")
    for issuer in ranked:
        print(f"{issuer.name:16} {esg.blended_score(issuer):7.1f} {str(esg.eligible(issuer)): >6}")


if __name__ == "__main__":
    main()
