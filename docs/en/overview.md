# Trading Runtime and Research Documentation (EN)

## 1. Repository Boundary

`TradingBinanceBot` documents a private trading/runtime/research platform with separate execution, risk, recovery, replay, evidence, observability, reliability, and operator-control domains. It is not a source-code mirror.

## 2. Runtime Shape

Stable public ownership is separated across bootstrap/lifecycle, mutable runtime state, trading orchestration, durable execution state/recovery, exchange/API access, portfolio risk, monitoring/observability, reliability, operator control, persistence/configuration, backtesting/replay, and research/evidence.

Read: [Project Map](architecture/project_map.md) and [Module-Family Reference](architecture/module_reference.md).

## 3. Execution and Recovery

Durable execution state may require reconciliation before normal trading readiness. Recovery is deterministic/idempotent, unresolved state fails closed, and recovery does not itself authorize fresh order placement.

Read: [Execution / Recovery](architecture/execution_recovery.md).

## 4. Research and Evidence

Research uses explicit event-time semantics, deterministic replay, no-future-leakage rules, dataset/provenance identity, time-safe splits, and promotion evidence that remains separate from rollout authorization. Extended methodology covers microstructure/execution-quality evidence, external data-source provenance, and preregistered bounded dataset-build workflows without publishing active strategy or operational data.

Read: [Research / Backtesting](research/backtesting.md), [Evidence Contracts](research/evidence_contracts.md), [Microstructure Research](research/microstructure.md), [Options / Dataset Builds](research/options_data.md), and [Data-Source Contracts](research/data_sources.md).

## 5. Reliability and Operator Control

Reliability uses bounded failure handling, secret-safe diagnostics, explicit recovery boundaries, and fail-safe containment. Operator-facing controls remain access-controlled and cannot silently bypass risk, readiness, recovery, evidence, or promotion gates.

Read: [Reliability](operations/reliability.md), [Operator Control](operations/operator_control.md), and [Logging and Artifacts](operations/logging.md).

## 6. Testing

Testing includes unit, integration, property-based, parametrized regression, contract, persistence/atomic-write, order-state/recovery, failure-path/network resilience, replay/parity, research/provenance, observability, risk/API/execution, and documentation validation.

## 7. Provenance

- Documentation review date: `2026-09-04`.
- Reviewed private source commit: `05a4214895111bcdbb7960223b4af232c066c48c`.
- Private source commit date: `2026-09-03`.
- Previous public sync: `2026-05-30`.
- Previous exact private source SHA: `not recorded`.

## 8. Documentation Index

- [Architecture](architecture/project_map.md)
- [Module-Family Reference](architecture/module_reference.md)
- [Execution / Recovery](architecture/execution_recovery.md)
- [Reliability](operations/reliability.md)
- [Operator Control](operations/operator_control.md)
- [Logging and Artifacts](operations/logging.md)
- [Research / Backtesting](research/backtesting.md)
- [Evidence Contracts](research/evidence_contracts.md)
- [Microstructure Research](research/microstructure.md)
- [Options / Dataset Builds](research/options_data.md)
- [Data-Source Contracts](research/data_sources.md)
- [Testing](testing/testing_guide.md)
- [Public Sync Manifest](../shared/public_sync_manifest.md)

## 9. Public-Safety Boundary

Do not publish private source, runtime/trading state, current strategies/candidates/rankings, production thresholds, provider credentials/endpoints, infrastructure topology, exact privileged/recovery commands, current recorder/source state, operational hashes, or private operational evidence.
