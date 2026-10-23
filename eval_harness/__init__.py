"""PoW #1 — eval harness: golden dataset + scorer + published scores.

Lands 29 Dec 2026. Until then this package is harness only:
`python -m eval_harness check` reports "gate armed, no golden dataset yet"
and exits 0. The moment `golden/` contains a dataset and `thresholds.json`
exists, the gate enforces the recorded thresholds and FAILS CI on regression.
"""
