# Trading Runtime and Research Documentation (EN)

## 1. Repository Boundary

`TradingBinanceBot` documents a private trading/runtime/research platform with separate execution, risk, recovery, replay, evidence, and observability domains. It is not a source-code mirror.

## 2. Runtime Shape

Stable public ownership is separated across bootstrap/lifecycle, mutable runtime state, trading orchestration, durable execution state/recovery, exchange/API access, portfolio risk, monitoring/observability, operator control, persistence/configuration, backtesting/replay, and research/evidence.

## 3. Execution and Recovery

Durable execution state may require reconciliation before normal trading readiness. Recovery is deterministic/idempotent, unresolved state fails closed, and recovery does not itself authorize fresh order placement.

Read: [Execution / Recovery](architecture/execution_recovery.md).

## 4. Research and Evidence

Research uses explicit event-time semantics, deterministic replay, no-future-leakage rules, dataset/provenance identity, time-safe splits, and promotion evidence that remains separate from rollout authorization.

Read: [Research / Backtesting](research/backtesting.md) and [Evidence Contracts](research/evidence_contracts.md).

## 5. Testing

Testing includes unit, integration, property-based, parametrized regression, contract, persistence/atomic-write, order-state/recovery, failure-path/network resilience, replay/parity, research/provenance, observability, risk/API/execution, and documentation validation.

## 6. Provenance

- Review date: `2026-09-04`.
- Reviewed private source commit: `05a4214895111bcdbb7960223b4af232c066c48c`.
- Previous public sync: `2026-05-30`.
- Current status: prepared for review, not yet merged.

## 7. Documentation Index

- [Architecture](architecture/project_map.md)
- [Execution / Recovery](architecture/execution_recovery.md)
- [Research / Backtesting](research/backtesting.md)
- [Evidence Contracts](research/evidence_contracts.md)
- [Testing](testing/testing_guide.md)
- [Logging and Artifacts](operations/logging.md)
- [Public Sync Manifest](../shared/public_sync_manifest.md)

## 8. Public-Safety Boundary

Do not publish private source, runtime/trading state, current strategies/candidates/rankings, production thresholds, infrastructure topology, exact recovery commands, or private operational evidence.
