# Documentation du runtime et de la recherche (FR)

## 1. Limite du dépôt

`TradingBinanceBot` documente une plateforme privée de trading, de runtime et de recherche avec des domaines distincts pour l'exécution, le risque, la récupération, le replay, les preuves, l'observability, la reliability et l'operator control. Ce dépôt n'est pas un miroir du code source.

## 2. Structure du runtime

Les responsabilités publiques stables sont réparties entre l'initialisation/cycle de vie, l'état mutable du runtime, l'orchestration du trading, le durable execution state/recovery, l'accès exchange/API, le risque de portefeuille, le monitoring/observability, la reliability, l'operator control, la persistence/configuration, le backtesting/replay et la research/evidence.

Lire : [Carte du projet](architecture/project_map.md) et [Référence des familles de modules](architecture/module_reference.md).

## 3. Exécution et récupération

L'état d'exécution durable peut nécessiter une reconciliation avant la disponibilité normale du trading. La recovery est déterministe et idempotente, tout état non résolu est traité en fail-closed, et la recovery n'autorise pas à elle seule le placement de nouveaux ordres.

Lire : [Exécution / récupération](architecture/execution_recovery.md).

## 4. Recherche et preuves

La recherche utilise une sémantique explicite de l'event time, un deterministic replay, des no-future-leakage rules, la dataset/provenance identity, des time-safe splits et une promotion evidence qui reste distincte de la rollout authorization. La méthodologie étendue couvre les microstructure/execution-quality evidence, la provenance des sources de données externes et des preregistered bounded dataset-build workflows sans publier de stratégie active ni de données opérationnelles.

Lire : [Recherche / backtesting](research/backtesting.md), [Contrats de preuve](research/evidence_contracts.md), [Recherche en microstructure](research/microstructure.md), [Options / Dataset Builds](research/options_data.md) et [Contrats de sources de données](research/data_sources.md).

## 5. Fiabilité et contrôle opérateur

La reliability utilise une bounded failure handling, des diagnostics secret-safe, des recovery boundaries explicites et un fail-safe containment. Les operator-facing controls restent access-controlled et ne peuvent pas contourner silencieusement les gates de risk, readiness, recovery, evidence ou promotion.

Lire : [Fiabilité](operations/reliability.md), [Contrôle opérateur](operations/operator_control.md) et [Journalisation et artefacts](operations/logging.md).

## 6. Tests

Les tests comprennent les tests unitaires, d'intégration, property-based, de régression paramétrés, de contrat, de persistence/atomic-write, d'order-state/recovery, de failure paths/network resilience, de replay/parity, de research/provenance, d'observability, de risk/API/execution et la validation de la documentation.

## 7. Provenance

- Date de revue de la documentation : `2026-09-04`.
- Commit source privé revu : `05a4214895111bcdbb7960223b4af232c066c48c`.
- Date du commit source privé : `2026-09-03`.
- Synchronisation publique précédente : `2026-05-30`.
- SHA exact précédent de la source privée : `not recorded`.

## 8. Index de la documentation

- [Architecture](architecture/project_map.md)
- [Référence des familles de modules](architecture/module_reference.md)
- [Exécution / récupération](architecture/execution_recovery.md)
- [Fiabilité](operations/reliability.md)
- [Contrôle opérateur](operations/operator_control.md)
- [Journalisation et artefacts](operations/logging.md)
- [Recherche / backtesting](research/backtesting.md)
- [Contrats de preuve](research/evidence_contracts.md)
- [Recherche en microstructure](research/microstructure.md)
- [Options / Dataset Builds](research/options_data.md)
- [Contrats de sources de données](research/data_sources.md)
- [Tests](testing/testing_guide.md)
- [Manifeste de synchronisation publique](../shared/public_sync_manifest.md)

## 9. Limite de publication sûre

Ne publiez pas le code source privé, le runtime/trading state, les strategies/candidates/rankings actuels, les production thresholds, provider credentials/endpoints, infrastructure topology, commandes privileged/recovery exactes, current recorder/source state, operational hashes ou private operational evidence.
