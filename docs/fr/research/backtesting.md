# Guide Research et Backtesting (FR)

## 1. Objectif

La recherche historique utilise la même sémantique de trading que le runtime,
tout en séparant data ingestion et live execution.

## 2. Répartition des Responsabilités

| Couche | Responsabilité |
| --- | --- |
| Workflow companion de data-ingestion | Récupérer les données OHLCV publiques et écrire des fichiers normalisés |
| Archive root locale | Stocker des entrées historiques reproductibles |
| Outils offline de recherche | Replay, évaluation, ranking, sweeps et artifacts de preuve |
| Live runtime | Exécuter testnet/mainnet indépendamment du rafraîchissement d'archive |

Le workflow d'ingestion ne fait pas partie de la boucle live et ne prend pas de
décisions de trading.

## 3. Contrat Canonique de l'Archive

```text
<archive-root>/
  klines_15m/<SYMBOL>_15m.csv
  klines_1h/<SYMBOL>_1h.csv
  klines_4h/<SYMBOL>_4h.csv
  summary_metrics.csv
```

Les champs OHLCV attendus incluent timestamps, open, high, low, close et volume.

## 4. Workflow Opérateur

1. Rafraîchir une archive locale avec le workflow companion d'ingestion.
2. Lancer un replay smoke check étroit avec l'archive root.
3. Lancer une évaluation enabled-universe same-core.
4. Produire ranking et sweeps ciblés symbole/candidate.
5. Comparer les artifacts baseline et candidate.
6. Enregistrer un verdict fondé sur les preuves.
7. Promouvoir uniquement via les gates testnet, shadow et live.

Utiliser des placeholders dans les docs publiques :

```bash
python tools/analysis/<research-tool>.py --archive-root <archive-root>
```

## 5. Règle de Reproductibilité

Tout run influençant une décision de stratégie ou de rollout doit utiliser une
archive root locale plutôt qu'un fetch réseau ad-hoc. Les vérifications public-fetch
étroites sont acceptables uniquement pour smoke validation ou debug temporaire.

## 6. Règle des Artifacts

Les sorties générées de recherche appartiennent à :

```text
data/out/<domain>/
```

Ne pas committer archives, rapports, rankings ou chemins propres au workstation
dans ce dépôt public de documentation.

## 7. Règle d'Interface

Une UI ou TUI locale peut orchestrer refresh archive, research runs, affichage
des artifacts et candidate promotion. Elle doit rester un thin wrapper et ne pas
implémenter un second moteur de trading/backtesting.
