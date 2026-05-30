# Documentation Binance Trading Bot (FR)

Documentation publique sécurisée pour une implémentation privée de trading bot.

## 1. Limite des dépôts

`TradingBinanceBot` publie les contrats stables destinés aux opérateurs. Le code
runtime, les identifiants, l'état de production et les preuves internes restent privés.

Snapshot public-safe :

- date de revue public-safe : `2026-05-26`;
- date de synchronisation documentaire : `2026-05-30`.

## 2. Structure runtime

- Entrypoint fin et bootstrap CLI.
- Boucle runtime de haut niveau détenue par `BotRunner`.
- Orchestration de chaque itération détenue par `TradingExecutor`.
- Décisions et exécution par symbole détenues par `TradeProcessor`.
- Sémantique de risque portefeuille détenue par `RiskManager`.
- Monitoring, observability, métriques, reporting, livraison Telegram et surfaces
  de contrôle locales sont des domaines distincts.

## 3. Invariant du cycle de trading

Chaque itération prépare le contexte marché/positions, traite les vérifications SELL,
rafraîchit les balances si nécessaire, puis traite les candidats BUY.

Invariant clé : **SELL est traité avant BUY** afin de réduire les conflits de stale balance.

## 4. Ownership de configuration

- `config/config.json` : paramètres runtime opérationnels — cadence, retry,
  telemetry, notifications et mode risk manager.
- `config/strategy*.json` : logique de trading — TP/SL, indicateurs, targets
  et overrides d'actifs pris en charge.
- Les clés détenues par la stratégie ne retombent pas sur la configuration opérationnelle.
- Override TA global minimal : `settings.enable_ta_confirmation`.

## 5. Sécurité d'exécution

- `--dry-run` simule l'exécution sans placer d'ordres réels.
- Les lectures market-data et balances restent disponibles pour la validation.
- Les chemins Convert sont réservés au mainnet et ne doivent pas s'exécuter en dry-run.
- Les erreurs par symbole doivent suspendre ou ignorer le symbole concerné ;
  l'arrêt global est réservé aux problèmes de credentials.
- Les fichiers runtime config et strategy supportent un hot reload contrôlé ;
  les changements de clés API exigent un redémarrage.
- En mode launcher détaché, le wrapper se termine après le démarrage réussi du
  processus enfant, tandis que le bot continue de fonctionner.

## 6. Same-Core Research et Backtesting

La recherche historique reste séparée du live trading :

1. Rafraîchir une archive OHLCV locale via un workflow companion d'ingestion.
2. Passer l'archive root aux outils offline de recherche.
3. Lancer replay same-core, évaluation enabled-universe, ranking et sweeps ciblés.
4. Comparer les artifacts baseline et candidate.
5. Promouvoir uniquement après revue des preuves vers testnet, shadow, puis live.

Lire : [Research / Backtesting](research/backtesting.md).

## 7. Limites des artifacts

- État runtime mutable : `data/<env>/`.
- État métriques mutable : `data/metrics/<env>/`.
- Logs runtime : `logs/<env>/<hostname>/`.
- Logs de contrôle racine : `logs/watchdog.log`, `logs/bot_launcher.log`.
- Sorties offline générées : `data/out/<domain>/`.
- Documentation maintenue manuellement : `docs/`.

## 8. Index documentaire

- [Architecture](architecture/project_map.md)
- [Research / Backtesting](research/backtesting.md)
- [Tests](testing/testing_guide.md)
- [Logs et artifacts](operations/logging.md)
- [Shared Scope](../shared/docs_scope.md)
- [Public Sync Manifest](../shared/public_sync_manifest.md)

## 9. Notes de sécurité

- Commencer par testnet et dry-run.
- Ne jamais activer withdrawals pour les clés API de trading.
- Vérifier les limites de risque avant tout rollout mainnet.
- Ne pas publier l'état runtime, les archives de données ou les preuves internes.
