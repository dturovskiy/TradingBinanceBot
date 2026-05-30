# Мапа Проєкту (UA)

Оновлено: 2026-05-30
Дата public-safe review: `2026-05-26`

## 1. Межа публічної документації

Ця мапа описує стабільні public-safe ownership boundaries. Вона не є дзеркалом
приватного source code і не експортує internal-only evidence.

## 2. Runtime Ownership Domains

| Домен | Відповідальність | Public-safe приклади шляхів |
| --- | --- | --- |
| Bootstrap / lifecycle | CLI bootstrap, startup, shutdown, initialization, runtime snapshots | `src/main_bot.py`, `src/bot_runner.py`, `src/lifecycle/*` |
| Mutable runtime context | Thread-safe shared state і coordination | `src/bot_context.py` |
| Trading iteration | BUY/SELL sequencing, summaries, risk integration | `src/trading/*` |
| Trade execution detail | Validation, sizing, execution, persistence updates | `src/trade_processor.py`, `src/api/*` |
| Portfolio risk | Risk decisions, shadow/enforce actions, reason taxonomy | `src/risk/*` |
| Monitoring / observability | Heartbeat, performance, metrics, reports | `src/monitoring/*`, `src/observability/*`, `src/metrics/*` |
| Telegram / operator control | Notifications, menus, callbacks, watchdog control | `src/telegram_ui/*`, `scripts/monitoring/*` |
| Local interface | Локальна control surface для audit/research workflows | `interface/*` |
| Offline tooling | Audit, analysis, diagnostics, benchmarks, integration tools | `tools/*` |

## 3. Високорівневий Runtime Flow

1. Bootstrap читає CLI flags і завантажує runtime та strategy configuration.
2. Lifecycle initialization завантажує exchange state, positions, monitoring і snapshots.
3. Main loop перевіряє підтримувані config hot-reload boundaries.
4. `TradingExecutor` готує context, запускає SELL checks, за потреби оновлює
   balances і лише потім обробляє BUY candidates.
5. `TradeProcessor` валідує opportunities, розраховує sizing і stop/target levels,
   виконує або симулює actions та зберігає результати.
6. Monitoring, metrics, reports і operator notifications оновлюються.

Ключовий інваріант: **SELL перед BUY**.

## 4. Ownership Конфігурації

| Домен | Канонічний власник |
| --- | --- |
| Operational cadence, retry, telemetry, notifications, runtime switches | `config/config.json` |
| TP/SL, indicators, targets, підтримувані asset overrides | `config/strategy*.json` |
| Мінімальний глобальний TA kill-switch | `settings.enable_ta_confirmation` |

Strategy-owned параметри не використовують operational config як fallback.

## 5. Execution-Safety Contracts

- Dry-run симулює execution і не має розміщувати реальні ордери.
- Convert execution працює лише у mainnet і вимкнений для dry-run.
- Circuit breaker та error handling мають локалізувати symbol-level failures.
- Зміни API keys потребують restart.
- Detached launcher mode залишає child bot process активним після exit wrapper-процесу.

## 6. Межа Research / Backtesting

```text
companion data-ingestion workflow
              |
              v
      локальний OHLCV archive root
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

Live runtime не повинен залежати від archive-refresh workflow.

## 7. Канонічні Шляхи Артефактів

| Клас артефактів | Канонічний public-safe шлях |
| --- | --- |
| Human-maintained docs | `docs/` |
| Mutable runtime state | `data/<env>/` |
| Mutable metrics state | `data/metrics/<env>/` |
| Runtime operational logs | `logs/<env>/<hostname>/{activity,trades,performance,metrics}.log` |
| Root control logs | `logs/watchdog.log`, `logs/bot_launcher.log` |
| Generated offline outputs | `data/out/<domain>/` |
| Tracked benchmark references | `tools/benchmark/baselines/` |

Generated artifacts за замовчуванням не належать до documentation paths.

## 8. Пов'язані Гайди

- [Research / Backtesting](../research/backtesting.md)
- [Тестування](../testing/testing_guide.md)
- [Логування та артефакти](../operations/logging.md)
- [Shared Scope](../../shared/docs_scope.md)
