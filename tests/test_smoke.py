"""Smoke test: the repo imports and the harness answers."""


def test_packages_import() -> None:
    import eval_harness  # noqa: F401
    import mcp_gateway  # noqa: F401
    import rag_service  # noqa: F401


def test_eval_gate_unarmed_passes() -> None:
    from eval_harness.__main__ import main

    assert main(["eval_harness", "check"]) == 0
