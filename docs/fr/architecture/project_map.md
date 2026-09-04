# Carte du projet (FR)

## 1. Limite de la documentation publique

Cette carte décrit des domaines de responsabilité stables et adaptés à la documentation publique, et non l’arborescence complète du code source privé.

## 2. Domaines de responsabilité du runtime

| Domaine | Responsabilité publiable |
| --- | --- |
| Initialisation / cycle de vie | Démarrage, arrêt, initialisation et orchestration de la disponibilité |
| État mutable du runtime | Contexte d’exécution coordonné en mémoire |
| Orchestration du trading | Séquencement des itérations et coordination du flux de trading |
| État d’exécution durable / récupération | Intention et état d’exécution persistés, réconciliation après redémarrage et contrôle de disponibilité |
| Exchange / API | Lecture de l’état externe de l’exchange et adaptateurs orientés ordres |
| Risque de portefeuille | Politique et confinement du risque au niveau du portefeuille |
| Monitoring / observabilité | Santé, métriques, télémétrie et rapports |
| Contrôle opérateur | Notifications et contrôles destinés à l’opérateur |
| Persistance / configuration | Responsabilité de la persistance du runtime et de la configuration |
| Backtesting / replay | Replay en temps d’événement et méthodologie de parité d’exécution |
| Recherche / preuves | Identité des jeux de données, provenance, validation et preuves de promotion |

## 3. Flux d’exécution de haut niveau

1. L’initialisation et le cycle de vie mettent en place les domaines requis.
2. L’état persisté et l’état mutable sont chargés.
3. La réconciliation requise de l’état d’exécution s’effectue avant la disponibilité normale.
4. L’orchestration normale du trading ne se poursuit que lorsque l’état requis est cohérent.
5. Exchange/API, risque, persistance et observabilité restent des domaines de responsabilité séparés.

## 4. État d’exécution durable / récupération

L’exécution des ordres est distincte de la responsabilité de l’état durable. Un redémarrage peut nécessiter une réconciliation entre l’état externe de l’exchange et l’état géré localement. La récupération doit être déterministe et idempotente, tout état non résolu est traité en fail-closed, et la récupération n’autorise pas à elle seule le placement de nouveaux ordres.

Voir [Exécution / récupération](execution_recovery.md).

## 5. Limite recherche / replay

Le replay utilise un temps d’événement explicite et doit, lorsque c’est pertinent, partager les sémantiques de domaine importantes avec l’exécution live. Les adaptateurs peuvent rester isolés, mais le replay ne doit pas contourner silencieusement des contrats importants du domaine live.

Voir [Recherche / backtesting](../research/backtesting.md).

## 6. Limites de publication sûre

Cette page ne publie ni les noms ou formats exacts des journaux, ni l’ordre des écritures, les fenêtres de panne, les commandes de récupération, les procédures de réconciliation live, les seuils de production, l’état opérationnel courant ou la topologie privée.

## 7. Guides associés

- [Exécution / récupération](execution_recovery.md)
- [Recherche / backtesting](../research/backtesting.md)
- [Contrats de preuve](../research/evidence_contracts.md)
- [Tests](../testing/testing_guide.md)
- [Journalisation et artefacts](../operations/logging.md)
