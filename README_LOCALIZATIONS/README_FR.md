# Documentation Binance Trading Bot (FR)

Documentation publique du projet prive `BinaceBot`.

## 1. Role de ce depot

`TradingBinanceBot` est la couche publique de documentation du systeme prive.

- Depot prive (`BinaceBot`) : code runtime, cles API, execution reelle.
- Depot public (`TradingBinanceBot`) : architecture, procedures, tests, standards de logs.

## 2. Etat actuel (synchronise le 2026-02-28)

### Structure runtime

- Point d'entree fin : `src/main_bot.py` + CLI (`--testnet`, `--dry-run`, `--config`, `--strategy`, `--debug`).
- Coordinateur : `src/bot_runner.py`.
- Orchestrateur trading : `src/trading/trading_executor.py`.
- Logique signaux/execution : `src/trade_processor.py`.
- Politique de risque portefeuille : `src/risk/risk_manager.py` (`off|shadow|enforce`).
- Controle Telegram : watchdog + `src/telegram_ui/*`.

### Cycle d'iteration

1. Recuperation marche (prix + balances).
2. Repricing des positions.
3. Passage SELL.
4. Refresh balance si necessaire.
5. Passage BUY.
6. Persistance + decision summary + KPI runtime.

Comportement cle : **SELL avant BUY**.

### Feature flags de rollout

Dans `config/config.json`:

- `freeze_dynamic_tp_sl`
- `strict_min_notional_enforcement`
- `use_closed_candles_for_signals`
- `intelligent_illiquid_unlocking`

Certaines options restent en mode preview/compatibilite.

## 3. Ownership de configuration

- `config/config.json` : runtime operationnel.
- `config/strategy*.json` : logique de trading.
- Override global volontairement minimal (`settings.enable_ta_confirmation`).

## 4. Capacites principales

- Execution Spot avec chemins Convert.
- Filtres modulaires : RSI, SMA, ATR, Volume.
- Risk manager avec telemetry shadow/enforce.
- Circuit breaker + controle des positions illiquides.
- Logging structure + persistance periodique des metriques.
- Controle distant Telegram via watchdog.

## 5. Demarrage securise

Dans le depot prive:

```bash
cp .env.example .env
./start_bot.sh --testnet --dry-run
```

Validation rapide:

```bash
./scripts/testing/run_tests_quick.sh
```

## 6. Commandes Telegram

Controle processus:

- `/start_bot`
- `/stop_bot`
- `/restart_bot`
- `/check_bot`
- `/reload_config`

Monitoring:

- `/status`
- `/positions`
- `/balance`
- `/health`
- `/performance`
- `/report`
- `/illiquid`

## 7. Profil qualite (tests)

- Modules de test: `120`
- Modules property tests: `31`

## 8. Index documentation

- Architecture EN: [../PROJECT_MAP_EN.md](../PROJECT_MAP_EN.md)
- Architecture UA: [../PROJECT_MAP_UA.md](../PROJECT_MAP_UA.md)
- Architecture FR: [../PROJECT_MAP_FR.md](../PROJECT_MAP_FR.md)
- Testing EN: [../TESTING_GUIDE_EN.md](../TESTING_GUIDE_EN.md)
- Testing UA: [../TESTING_GUIDE_UA.md](../TESTING_GUIDE_UA.md)
- Testing FR: [../TESTING_GUIDE_FR.md](../TESTING_GUIDE_FR.md)
- Logging EN: [../LOGGING.md](../LOGGING.md)
- Logging UA: [../LOGGING_UA.md](../LOGGING_UA.md)
- Logging FR: [../LOGGING_FR.md](../LOGGING_FR.md)
- Changelog: [../CHANGELOG.md](../CHANGELOG.md)

## 9. Notes de securite

- Toujours commencer en testnet.
- Ne jamais activer les retraits sur les cles API.
- Utiliser `--dry-run` avant tout changement de strategie.
- Verifier les limites `risk_manager` avant mainnet.
