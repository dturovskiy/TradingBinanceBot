# Documentation du runtime et de la recherche (FR)

## 1. Limite du dépôt

`TradingBinanceBot` documente une plateforme privée de trading, de runtime et de recherche avec des domaines distincts pour l’exécution, le risque, la récupération, le replay, les preuves et l’observabilité. Ce dépôt n’est pas un miroir du code source.

## 2. Structure du runtime

Les responsabilités publiques stables sont réparties entre l’initialisation/cycle de vie, l’état mutable du runtime, l’orchestration du trading, l’état d’exécution durable/récupération, l’accès exchange/API, le risque de portefeuille, le monitoring/l’observabilité, le contrôle opérateur, la persistance/configuration, le backtesting/replay et la recherche/les preuves.

## 3. Exécution et récupération

L’état d’exécution durable peut nécessiter une réconciliation avant la disponibilité normale du trading. La récupération est déterministe et idempotente, tout état non résolu est traité en fail-closed, et la récupération n’autorise pas à elle seule le placement de nouveaux ordres.

Lire : [Exécution / récupération](architecture/execution_recovery.md).

## 4. Recherche et preuves

La recherche utilise une sémantique explicite de l’event time, un replay déterministe, des règles empêchant les fuites d’informations futures, l’identité du jeu de données et sa provenance, des découpages respectant le temps et des preuves de promotion qui restent distinctes de l’autorisation de rollout.

Lire : [Recherche / backtesting](research/backtesting.md) et [Contrats de preuve](research/evidence_contracts.md).

## 5. Tests

Les tests comprennent les tests unitaires, d’intégration, property-based, de régression paramétrés, de contrat, de persistance/écriture atomique, d’état des ordres/récupération, de failure paths/résilience réseau, de replay/parité, de recherche/provenance, d’observabilité, de risque/API/exécution et la validation de la documentation.

## 6. Provenance

- Date de revue de la documentation : `2026-09-04`.
- Commit source privé revu : `05a4214895111bcdbb7960223b4af232c066c48c`.
- Date du commit source privé : `2026-09-03`.
- Synchronisation publique précédente : `2026-05-30`.
- SHA exact précédent de la source privée : `not recorded`.

## 7. Index de la documentation

- [Architecture](architecture/project_map.md)
- [Exécution / récupération](architecture/execution_recovery.md)
- [Recherche / backtesting](research/backtesting.md)
- [Contrats de preuve](research/evidence_contracts.md)
- [Tests](testing/testing_guide.md)
- [Journalisation et artefacts](operations/logging.md)
- [Manifeste de synchronisation publique](../shared/public_sync_manifest.md)

## 8. Limite de publication sûre

Ne publiez pas le code source privé, l’état du runtime ou du trading, les stratégies/candidats/classements actuels, les seuils de production, la topologie de l’infrastructure, les commandes exactes de récupération ni les preuves opérationnelles privées.
