# production-ai-systems

> Portfolio repo for the 3 hiring-manager-validated proof pieces of the Job Mission:
> **PoW #1** public eval harness + golden dataset · **PoW #2** MCP servers with enterprise auth ·
> **PoW #3** published AI incident postmortem + cost/latency teardown.

## Results (numbers first — this is what stops the scroll)

| Metric | Before | After | Δ | Source |
|---|---|---|---|---|
| Eval faithfulness (golden set) | — | — | — | [`eval_harness/scores/`](eval_harness) |
| Hallucination rate | — | — | — | [`eval_harness/scores/`](eval_harness) |
| p99 latency | — | — | — | [`docs/cost-teardown.md`](docs/cost-teardown.md) |
| Cost per 1k queries | — | — | — | [`docs/cost-teardown.md`](docs/cost-teardown.md) |

*Cells fill in as each PoW lands. PoW #1 → 29 Dec 2026 · PoW #2 → 26 Jan 2027 · PoW #3 → 1 Mar 2027.
No number goes here unless it was measured by the eval harness in CI.*

## Architecture

```
                    ┌─────────────────────────┐
                    │        eval_harness       │  ← golden dataset + scorer
                    │  (PoW #1, lands 29 Dec)  │     gates every deploy
                    └────────────┬────────────┘
                                 │  blocks deploy on regression
                                 v
┌──────────┐   ┌─────────────────────────────┐   ┌──────────────┐
│  client  │──▶│         rag_service         │──▶│  pgvector    │
└──────────┘   │  FastAPI + Pydantic + tests │   │  (embeddings)│
               └──────────────┬──────────────┘   └──────────────┘
                              │
                              v
                    ┌─────────────────────────┐
                    │        mcp_gateway       │  ← enterprise auth
                    │  (PoW #2, lands 26 Jan)  │
                    └─────────────────────────┘
```

## Run in 3 commands

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest                                   # tests + eval gate
```

## Proof pieces

- **Eval report** — `eval_harness/scores/` (published scores, CI-enforced)
- **Postmortems** — [`docs/postmortems/`](docs/postmortems/) (PoW #3)
- **Cost/latency teardown** — [`docs/cost-teardown.md`](docs/cost-teardown.md) (measured before → after)
- **Design judgment** — [`docs/adr/`](docs/adr/) (architecture decision records)

## CI

Fail-closed: lint + pytest + eval gate on every push. There is no `continue-on-error`
and no `|| true` anywhere in [`.github/workflows/ci.yml`](.github/workflows/ci.yml) —
a failing test **must** fail the workflow. The eval gate (`python -m eval_harness check`)
currently passes with "no golden dataset yet" and hardens automatically: the moment a
golden dataset exists, it enforces the recorded thresholds.
