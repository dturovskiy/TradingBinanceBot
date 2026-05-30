# Carte du Projet (FR)

Mise à jour : 2026-05-30
Date de revue public-safe : `2026-05-26`

## 1. Limite de la documentation publique

Cette carte décrit les ownership boundaries stables et public-safe. Elle ne
reproduit pas le code source privé et n'exporte pas les preuves internes.

## 2. Domaines d'ownership runtime

| Domaine | Responsabilité | Exemples de chemins public-safe |
| --- | --- | --- |
| Bootstrap / lifecycle | CLI bootstrap, startup, shutdown, initialization, runtime snapshots | `src/main_bot.py`, `src/bot_runner.py`, `src/lifecycle/*` |
| Contexte runtime mutable | État partagé thread-safe et coordination | `src/bot_context.py` |
| Itération trading | Séquence BUY/SELL, summaries, intégration du risque | `src/trading/*` |
| Détail d'exécution | Validation, sizing, execution, persistence updates | `src/trade_processor.py`, `src/api/*` |
| Risque portefeuille | Décisions, actions shadow/enforce, taxonomie des raisons | `src/risk/*` |
| Monitoring / observability | Heartbeat, performance, métriques, rapports | `src/monitoring/*`, `src/observability/*`, `src/metrics/*` |
| Telegram / contrôle opérateur | Notifications, menus, callbacks, watchdog | `src/telegram_ui/*`, `scripts/monitoring/*` |
| Interface locale | Surface locale pour workflows audit/research | `interface/*` |
| Outils offline | Audit, analyse, diagnostics, benchmarks, intégration | `tools/*` |

## 3. Flux runtime de haut niveau

1. Le bootstrap analyse les flags CLI et charge les configurations runtime et stratégie.
2. L'initialisation lifecycle charge exchange state, positions, monitoring et snapshots.
3. La boucle principale vérifie les limites supportées du hot reload.
4. `TradingExecutor` prépare le contexte, exécute les vérifications SELL, rafraîchit
   les balances si nécessaire, puis traite les candidats BUY.
5. `TradeProcessor` valide les opportunités, calcule sizing et stop/target levels,
   exécute ou simule les actions et persiste les résultats.
6. Monitoring, métriques, rapports et notifications opérateur sont rafraîchis.

Invariant clé : **SELL avant BUY**.

## 4. Ownership de configuration

| Domaine | Propriétaire canonique |
| --- | --- |
| Cadence opérationnelle, retry, telemetry, notifications, switches runtime | `config/config.json` |
| TP/SL, indicateurs, targets, overrides d'actifs pris en charge | `config/strategy*.json` |
| Kill-switch TA global minimal | `settings.enable_ta_confirmation` |

Les paramètres détenus par la stratégie ne retombent pas sur la configuration opérationnelle.

## 5. Contrats de sécurité d'exécution

- Dry-run simule l'exécution et ne place pas d'ordres réels.
- Convert execution est réservé au mainnet et désactivé en dry-run.
- Circuit breaker et error handling doivent contenir localement les erreurs par symbole.
- Les changements de clés API exigent un redémarrage.
- Le mode launcher détaché maintient le processus enfant après la sortie du wrapper.

## 6. Limite Research / Backtesting

```text
workflow companion de data-ingestion
              |
              v
       archive root OHLCV locale
              |
              v
      outils offline same-core
              |
              v
 revue des preuves baseline vs candidate
              |
              v
       testnet -> shadow -> live
```

Le live runtime ne doit pas dépendre du workflow de rafraîchissement d'archive.

## 7. Chemins Canoniques des Artifacts

| Classe d'artifact | Chemin public-safe canonique |
| --- | --- |
| Documentation maintenue manuellement | `docs/` |
| État runtime mutable | `data/<env>/` |
| État métriques mutable | `data/metrics/<env>/` |
| Logs runtime | `logs/<env>/<hostname>/{activity,trades,performance,metrics}.log` |
| Logs de contrôle racine | `logs/watchdog.log`, `logs/bot_launcher.log` |
| Sorties offline générées | `data/out/<domain>/` |
| Références benchmark suivies | `tools/benchmark/baselines/` |

Les artifacts générés n'appartiennent pas aux chemins documentaires par défaut.

## 8. Guides Associés

- [Research / Backtesting](../research/backtesting.md)
- [Tests](../testing/testing_guide.md)
- [Logs et artifacts](../operations/logging.md)
- [Shared Scope](../../shared/docs_scope.md)
