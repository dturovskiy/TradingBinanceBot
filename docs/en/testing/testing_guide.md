# Testing Guide (EN)

## 1. Scope

Public documentation intentionally does not freeze an exact test count; collection size changes over time.

## 2. Testing Taxonomy

Current public-safe categories include:

- unit tests;
- integration tests;
- property-based tests / Hypothesis;
- parametrized regression tests;
- contract tests;
- persistence / atomic-write tests;
- order-state / recovery tests;
- failure-path / network resilience tests;
- replay / parity tests;
- research / provenance tests;
- observability tests;
- risk / API / execution tests.

## 3. Validation Pipeline Categories

Where applicable, validation combines static/type checks, configuration/fail-safe checks, pytest, and benchmark/performance checks. Public docs do not claim a current enforced coverage percentage unless separately reverified.

## 4. Execution / Recovery Testing

Validate durable-state persistence, restart reconciliation, idempotent recovery, fail-closed unresolved state, readiness gating, and the invariant that recovery does not submit fresh orders. Exercise unresolved state across external/local disagreement, incomplete or unavailable reconciliation evidence, persistence failures, and repeated recovery attempts.

## 5. Research / Replay Testing

Validate event-time semantics, no-future-leakage, deterministic replay, time-safe splits, dataset/provenance binding, independent-sample handling, and execution/domain parity. A methodology test can validate these contracts without asserting that any current candidate or gate is passing.

## 6. Documentation Validation

Run:

```bash
python3 scripts/docs/check_language_parity.py
bash scripts/docs/validate_links.sh
git diff --check
```

When Bash execution is blocked by tool policy, run equivalent internal Markdown-link validation and record that limitation.

Documentation review also verifies required shared governance files, navigation/link parity, and absence of private implementation detail or current operational/research state.

## 7. Public-Safety Boundary

Generated test/research evidence, private paths, current strategy/candidate results, and operational runtime artifacts are not published here.
