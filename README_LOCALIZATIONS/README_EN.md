# Binance Trading Bot Documentation (EN)

Public documentation for the private `BinaceBot` project.

## 1. What This Repository Is

`TradingBinanceBot` is the public documentation layer for a private production codebase.

- Private repo (`BinaceBot`): runtime code, API credentials, execution environment.
- Public repo (`TradingBinanceBot`): architecture, setup flow, operations, testing, logging standards.

## 2. Current System Snapshot (Synced 2026-02-28)

### Core runtime shape

- Thin entrypoint: `src/main_bot.py` + CLI parser (`--testnet`, `--dry-run`, `--config`, `--strategy`, `--debug`).
- Coordinator: `src/bot_runner.py`.
- Trading orchestration: `src/trading/trading_executor.py`.
- Strategy execution: `src/trade_processor.py`.
- Portfolio risk policy: `src/risk/risk_manager.py` with `off|shadow|enforce` modes.
- Telegram control plane: watchdog + `src/telegram_ui/*` command handlers.

### Trading cycle highlights

Each iteration is orchestrated as:

1. Market fetch (prices + balances).
2. Position repricing.
3. SELL pass.
4. Optional balance refresh.
5. BUY pass.
6. Persistence + decision summary + runtime KPI snapshot.

Key behavior: **SELL is processed before BUY** to reduce stale-balance conflicts.

### Risk and rollout flags

The runtime includes feature flags in `config/config.json`:

- `freeze_dynamic_tp_sl`
- `strict_min_notional_enforcement`
- `use_closed_candles_for_signals`
- `intelligent_illiquid_unlocking`

These flags are rollout controls. Some are still in preview/compatibility mode.

## 3. Configuration Ownership (Hard-Cut)

- `config/config.json`: runtime/operational settings (loop cadence, retries, alerts, risk manager mode).
- `config/strategy*.json`: trading logic (TP/SL, filters, buy targets, indicator thresholds).
- Global override is intentionally minimal (`settings.enable_ta_confirmation`).

## 4. Main Capabilities

- Spot trading execution with Convert integration paths.
- Modular entry filters: RSI, SMA, ATR, Volume.
- Risk manager decisions with enforce and shadow telemetry.
- Circuit breaker and illiquid position controls.
- Structured logs + periodic metrics persistence.
- Telegram-driven remote process control via watchdog.

## 5. Safe Start Sequence

Recommended first launch in private repo root:

```bash
cp .env.example .env
./start_bot.sh --testnet --dry-run
```

Then validate:

```bash
./scripts/testing/run_tests_quick.sh
```

## 6. Telegram Runtime Control

Process commands (watchdog):

- `/start_bot`
- `/stop_bot`
- `/restart_bot`
- `/check_bot`
- `/reload_config`

Monitoring commands:

- `/status`
- `/positions`
- `/balance`
- `/health`
- `/performance`
- `/report`
- `/illiquid`

## 7. Testing and Quality Snapshot

- Test modules: `120`
- Property test modules: `31`
- Examples include feature-flag contracts, risk manager behavior, periodic maintenance, Telegram flows, and config validation.

## 8. Documentation Index

- Architecture (EN): [../PROJECT_MAP_EN.md](../PROJECT_MAP_EN.md)
- Architecture (UA): [../PROJECT_MAP_UA.md](../PROJECT_MAP_UA.md)
- Architecture (FR): [../PROJECT_MAP_FR.md](../PROJECT_MAP_FR.md)
- Testing (EN): [../TESTING_GUIDE_EN.md](../TESTING_GUIDE_EN.md)
- Testing (UA): [../TESTING_GUIDE_UA.md](../TESTING_GUIDE_UA.md)
- Testing (FR): [../TESTING_GUIDE_FR.md](../TESTING_GUIDE_FR.md)
- Logging (EN): [../LOGGING.md](../LOGGING.md)
- Logging (UA): [../LOGGING_UA.md](../LOGGING_UA.md)
- Logging (FR): [../LOGGING_FR.md](../LOGGING_FR.md)
- Changelog: [../CHANGELOG.md](../CHANGELOG.md)

## 9. Safety Notes

- Use testnet first.
- Do not enable withdrawals on exchange API keys.
- Treat `--dry-run` as mandatory before any strategy change.
- Review `risk_manager` limits before moving to mainnet.
