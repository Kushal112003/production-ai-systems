# Eval harness

Automated grading of whether the system answered well, against reference answers I wrote: a **golden dataset**. This is the #1 thing 2026 AI-backend interviews screen for.

## Layout

- `golden/` — golden datasets, versioned (`v1.jsonl`, `v2.jsonl`, …). Each line: `{question, reference_answer, tags}`.
- `scorers/` — faithfulness, hallucination rate, citation accuracy, abstention correctness.
- `reports/` — per-release score reports. Every report is committed; scores only move up on purpose.
- `run.py` — runs the full suite, exits non-zero if any gate fails.

## The gate

A release passes only if, on the current golden dataset:

| Metric | Gate |
|---|---|
| Faithfulness | ≥ 0.85 |
| Hallucination rate | ≤ 0.10 |
| Citation accuracy | ≥ 0.90 |
| Abstention correctness | ≥ 0.90 |
| p99 latency | ≤ 8s |

Gates ratchet: when a release beats a gate by margin, the gate moves up and the ADR records why.
