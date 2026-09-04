# Документація Trading Runtime і Research (UA)

## 1. Межа Репозиторію

`TradingBinanceBot` документує приватну trading/runtime/research платформу з окремими доменами execution, risk, recovery, replay, evidence та observability. Це не дзеркало source code.

## 2. Форма Runtime

Стабільний public ownership розділено між bootstrap/lifecycle, mutable runtime state, trading orchestration, durable execution state/recovery, exchange/API access, portfolio risk, monitoring/observability, operator control, persistence/configuration, backtesting/replay та research/evidence.

## 3. Execution і Recovery

Durable execution state може вимагати reconciliation до normal trading readiness. Recovery є deterministic/idempotent, unresolved state працює fail-closed, а recovery саме по собі не авторизує нове розміщення ордерів.

Читайте: [Execution / Recovery](architecture/execution_recovery.md).

## 4. Research і Evidence

Research використовує explicit event-time semantics, deterministic replay, no-future-leakage, dataset/provenance identity, time-safe splits і promotion evidence, яке залишається окремим від rollout authorization.

Читайте: [Research / Backtesting](research/backtesting.md) і [Evidence Contracts](research/evidence_contracts.md).

## 5. Testing

Testing охоплює unit, integration, property-based, parametrized regression, contract, persistence/atomic-write, order-state/recovery, failure-path/network resilience, replay/parity, research/provenance, observability, risk/API/execution та documentation validation.

## 6. Provenance

- Дата review: `2026-09-04`.
- Reviewed private source commit: `05a4214895111bcdbb7960223b4af232c066c48c`.
- Попередній public sync: `2026-05-30`.
- Поточний статус: prepared for review, not yet merged.

## 7. Індекс Документації

- [Архітектура](architecture/project_map.md)
- [Execution / Recovery](architecture/execution_recovery.md)
- [Research / Backtesting](research/backtesting.md)
- [Evidence Contracts](research/evidence_contracts.md)
- [Testing](testing/testing_guide.md)
- [Logging and Artifacts](operations/logging.md)
- [Public Sync Manifest](../shared/public_sync_manifest.md)

## 8. Public-Safety Boundary

Не публікуйте private source, runtime/trading state, current strategies/candidates/rankings, production thresholds, infrastructure topology, exact recovery commands або private operational evidence.
