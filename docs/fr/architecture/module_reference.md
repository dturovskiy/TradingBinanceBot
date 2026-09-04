# Référence publique des familles de modules (FR)

## 1. Objectif
<!-- parity-key: modules.scope -->

Cette référence offre une vue public-safe plus approfondie des familles d'ownership sans reproduire l'arborescence source privée, les noms de classes, signatures de fonctions ou séquences d'implémentation.

## 2. Familles de modules Runtime
<!-- parity-key: modules.runtime -->

| Famille | Responsabilité public-safe |
| --- | --- |
| Bootstrap / lifecycle | Initialisation, arrêt, coordination de la readiness |
| Execution / recovery (`src/execution/`) | Durable execution state, reconciliation, restart recovery |
| Exchange / API | External exchange reads et transport/adapters orientés ordres |
| Risk (`src/risk/`) | Layered/grouped risk policy, reason/model semantics, fail-safe containment |
| Observability / telemetry | Logs, metrics, structured event/recorder observations, interprétation provenance/freshness |
| Operator control | Notifications autorisées, surfaces status/panel et operator workflows contrôlés |
| Persistence / configuration | Ownership de l'état/configuration et limites des durable artifacts |

## 3. Familles de modules Research
<!-- parity-key: modules.research -->

| Famille | Responsabilité public-safe |
| --- | --- |
| Backtesting / replay (`src/backtesting/`) | Event-time replay, execution realism, méthodologie live/replay parity |
| Research / evidence | Dataset identity, provenance, scanner isolation, evidence aggregation, promotion contracts |
| Microstructure research | Méthodologie spread/depth/executable-price séparée de l'order execution |
| Offline dataset workflows | Méthodologie preregistered, reproductible et bounded de data-build et acceptance |

## 4. Limites entre familles
<!-- parity-key: modules.boundaries -->

L'ownership du durable execution state est distinct de l'exchange transport ; l'observability n'autorise pas le trading ; le research/scanner work possède une no-order boundary ; l'evidence n'équivaut pas à la promotion authorization ; et les adapters ne doivent pas contourner silencieusement les contrats importants de risk, timing, state ou validation.

## 5. Limite de publication sûre
<!-- parity-key: modules.public-boundary -->

Ne traitez pas cette page comme une arborescence privée complète. Elle omet volontairement les private module/file inventories, noms internes de class/function, implementation source, stratégies actuelles, production configuration, runtime topology, current state et operational recovery procedures.

## 6. Guides associés

- [Carte du projet](project_map.md)
- [Exécution / récupération](execution_recovery.md)
- [Fiabilité](../operations/reliability.md)
- [Recherche / backtesting](../research/backtesting.md)
