# Recherche en microstructure et qualité d'exécution (FR)

## 1. Objectif
<!-- parity-key: microstructure.scope -->

La recherche en microstructure évalue des execution-quality evidence sans transformer la collecte de données en surface d'order placement. Le contrat public décrit la méthodologie, pas la strategy logic active ni la production calibration.

## 2. Preuves d'état du marché
<!-- parity-key: microstructure.market-state -->

Le spread, la depth et le contexte order-book associé peuvent servir de research evidence lorsque leur event-time et leur provenance sont explicites. Ces observations décrivent les conditions de marché ; elles n'autorisent pas, à elles seules, un trade.

## 3. Réalisme de l'Executable Price
<!-- parity-key: microstructure.executable-price -->

Lorsque l'execution realism est important, la recherche doit distinguer un executable-price model des hypothèses simplistes de reference price. La méthodologie peut tenir compte de contraintes de market state sans publier les paramètres actuels de fee, slippage, sizing ou calibration.

## 4. Telemetry à provenance isolée
<!-- parity-key: microstructure.provenance -->

Les microstructure observations doivent conserver source, observation-time, decision-time et outcome provenance afin que les evidence ne soient pas mélangées silencieusement entre contextes incompatibles. Un binding absent ou ambigu doit échouer en fail-closed pour l'utilisation des preuves.

## 5. Séparation de l'exécution et de la promotion
<!-- parity-key: microstructure.separation -->

La collecte ou l'analyse de microstructure telemetry est distincte de l'order execution et de la promotion authorization. Une execution-quality evidence favorable peut soutenir l'évaluation, mais les gates requis de dataset-integrity, execution/domain-parity et autres promotion gates restent indépendants.

## 6. Limite de publication sûre
<!-- parity-key: microstructure.public-boundary -->

Ne publiez pas la sampling cadence actuelle, l'activation des recorders, les budgets, les hypothèses fee/slippage, les strategy thresholds, candidate rankings, profitability conclusions, snapshots live d'order book ou contenus opérationnels de telemetry.

## 7. Guides associés

- [Recherche / backtesting](backtesting.md)
- [Contrats de preuve](evidence_contracts.md)
- [Contrats de sources de données](data_sources.md)
