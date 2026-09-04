# Documentation Trading Runtime et Research (FR)

## 1. Limite du Dépôt

`TradingBinanceBot` documente une plateforme privée trading/runtime/research avec des domaines séparés execution, risk, recovery, replay, evidence et observability. Ce n'est pas un miroir du code source.

## 2. Structure Runtime

L'ownership public stable est séparé entre bootstrap/lifecycle, mutable runtime state, trading orchestration, durable execution state/recovery, exchange/API access, portfolio risk, monitoring/observability, operator control, persistence/configuration, backtesting/replay et research/evidence.

## 3. Execution et Recovery

Le durable execution state peut exiger une reconciliation avant la normal trading readiness. Le recovery est deterministic/idempotent, l'état non résolu fail closed, et le recovery n'autorise pas à lui seul de nouveaux ordres.

Lire : [Execution / Recovery](architecture/execution_recovery.md).

## 4. Research et Evidence

La recherche utilise explicit event-time semantics, deterministic replay, no-future-leakage, dataset/provenance identity, time-safe splits et promotion evidence séparée de l'autorisation de rollout.

Lire : [Research / Backtesting](research/backtesting.md) et [Evidence Contracts](research/evidence_contracts.md).

## 5. Testing

Les tests couvrent unit, integration, property-based, parametrized regression, contract, persistence/atomic-write, order-state/recovery, failure-path/network resilience, replay/parity, research/provenance, observability, risk/API/execution et documentation validation.

## 6. Provenance

- Date de revue : `2026-09-04`.
- Commit source privé revu : `05a4214895111bcdbb7960223b4af232c066c48c`.
- Synchronisation publique précédente : `2026-05-30`.
- Statut actuel : prepared for review, not yet merged.

## 7. Index de Documentation

- [Architecture](architecture/project_map.md)
- [Execution / Recovery](architecture/execution_recovery.md)
- [Research / Backtesting](research/backtesting.md)
- [Evidence Contracts](research/evidence_contracts.md)
- [Testing](testing/testing_guide.md)
- [Logging and Artifacts](operations/logging.md)
- [Public Sync Manifest](../shared/public_sync_manifest.md)

## 8. Public-Safety Boundary

Ne pas publier private source, runtime/trading state, current strategies/candidates/rankings, production thresholds, infrastructure topology, exact recovery commands ou private operational evidence.
