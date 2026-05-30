# Project Map (EN)

Updated: 2026-05-30
Public-safe source review date: `2026-05-26`

## 1. Public Documentation Boundary

This map describes stable public-safe ownership boundaries. It does not mirror
private source code or expose internal-only evidence.

## 2. Runtime Ownership Domains

| Domain | Responsibility | Public-safe path examples |
| --- | --- | --- |
| Bootstrap / lifecycle | CLI bootstrap, startup, shutdown, initialization, runtime snapshots | `src/main_bot.py`, `src/bot_runner.py`, `src/lifecycle/*` |
| Mutable runtime context | Thread-safe shared state and coordination | `src/bot_context.py` |
| Trading iteration | Buy/sell sequencing, summaries, risk integration | `src/trading/*` |
| Trade execution detail | Validation, sizing, execution, persistence updates | `src/trade_processor.py`, `src/api/*` |
| Portfolio risk | Risk decisions, shadow/enforce actions, reason taxonomy | `src/risk/*` |
| Monitoring / observability | Heartbeat, performance, metrics, reports | `src/monitoring/*`, `src/observability/*`, `src/metrics/*` |
| Telegram / operator control | Notifications, menus, callbacks, watchdog control | `src/telegram_ui/*`, `scripts/monitoring/*` |
| Local interface | Local control and audit/research launch surface | `interface/*` |
| Offline tooling | Audit, analysis, diagnostics, benchmarks, integration tools | `tools/*` |

## 3. High-Level Runtime Flow

1. Bootstrap parses CLI flags and loads runtime and strategy configuration.
2. Lifecycle initialization loads exchange state, positions, monitoring, and snapshots.
3. The main loop checks supported config hot-reload boundaries.
4. `TradingExecutor` prepares context, runs SELL checks, refreshes balances when
   required, then processes BUY candidates.
5. `TradeProcessor` validates opportunities, computes sizing and stop/target levels,
   executes or simulates actions, and persists results.
6. Monitoring, metrics, reports, and operator notifications are refreshed.

Key invariant: **SELL before BUY**.

## 4. Configuration Ownership

| Domain | Canonical owner |
| --- | --- |
| Operational cadence, retry, telemetry, notifications, runtime switches | `config/config.json` |
| TP/SL, indicators, targets, supported asset overrides | `config/strategy*.json` |
| Minimal global TA kill-switch | `settings.enable_ta_confirmation` |

Strategy-owned parameters do not use operational config as a fallback.

## 5. Execution-Safety Contracts

- Dry-run performs simulated execution and must not place real orders.
- Convert execution is mainnet-only and disabled for dry-run.
- Circuit-breaker and error handling should contain symbol-level failures locally.
- API-key changes remain restart-required.
- Detached launcher mode leaves the child bot process running after wrapper exit.

## 6. Research / Backtesting Boundary

```text
data-ingestion companion workflow
              |
              v
      local OHLCV archive root
              |
              v
    offline same-core research tools
              |
              v
 baseline vs candidate evidence review
              |
              v
       testnet -> shadow -> live
```

Live runtime must not depend on the archive-refresh workflow.

## 7. Canonical Artifact Paths

| Artifact class | Canonical public-safe path |
| --- | --- |
| Human-maintained docs | `docs/` |
| Mutable runtime state | `data/<env>/` |
| Mutable metrics state | `data/metrics/<env>/` |
| Runtime operational logs | `logs/<env>/<hostname>/{activity,trades,performance,metrics}.log` |
| Root control logs | `logs/watchdog.log`, `logs/bot_launcher.log` |
| Generated offline outputs | `data/out/<domain>/` |
| Tracked benchmark references | `tools/benchmark/baselines/` |

Generated artifacts do not belong in documentation paths by default.

## 8. Related Guides

- [Research / Backtesting](../research/backtesting.md)
- [Testing](../testing/testing_guide.md)
- [Logging and Artifacts](../operations/logging.md)
- [Shared Scope](../../shared/docs_scope.md)
