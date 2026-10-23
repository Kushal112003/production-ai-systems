"""Eval gate CLI: `python -m eval_harness check`.

Fail-closed once armed: if a golden dataset and thresholds exist, scores below
threshold fail with exit 1. If not armed yet, it says so and exits 0.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GOLDEN_DIR = ROOT / "golden"
THRESHOLDS = ROOT / "thresholds.json"


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] != "check":
        print("usage: python -m eval_harness check", file=sys.stderr)
        return 2

    if not GOLDEN_DIR.is_dir() or not THRESHOLDS.exists():
        print("eval gate: armed, no golden dataset yet — pass")
        return 0

    thresholds = json.loads(THRESHOLDS.read_text())
    # PoW #1 fills in the real scorer here. Until then the gate is honest:
    # it refuses to claim a passing eval it never ran.
    print("eval gate: golden dataset found but scorer not implemented — FAIL")
    print(f"thresholds on record: {sorted(thresholds)}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
