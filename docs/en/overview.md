# Binance Trading Bot Documentation (EN)

Public-safe documentation for a private trading-bot implementation.

## 1. Repository Boundary

`TradingBinanceBot` publishes stable operator-facing contracts. Runtime code,
credentials, production state, and internal-only evidence remain private.

Public-safe snapshot:

- public-safe source review date: `2026-05-26`;
- documentation sync date: `2026-05-30`.

## 2. Runtime Shape

- Thin entrypoint and CLI bootstrap.
- Top-level runtime loop owned by `BotRunner`.
- Per-iteration orchestration owned by `TradingExecutor`.
- Symbol-level decision and execution detail owned by `TradeProcessor`.
- Portfolio risk semantics owned by `RiskManager`.
- Monitoring, observability, metrics, reporting, Telegram delivery, and local control surfaces are separate domains.

## 3. Trading-Cycle Invariant

Each iteration prepares market and position context, processes sell-side checks,
refreshes balances when required, then processes buy-side candidates.

Key invariant: **SELL is processed before BUY** to reduce stale-balance conflicts.

## 4. Configuration Ownership

- `config/config.json`: operational/runtime settings such as cadence, retries,
  telemetry, notifications, and risk-manager mode.
- `config/strategy*.json`: trading logic such as TP/SL, indicator rules, targets,
  and supported asset overrides.
- Strategy-owned keys do not fall back to operational configuration.
- The intentionally minimal global TA override is `settings.enable_ta_confirmation`.

## 5. Execution Safety

- `--dry-run` simulates execution without placing real orders.
- Market-data and balance reads remain available during dry-run validation.
- Convert paths are mainnet-only and must not execute in dry-run.
- Symbol-level failures should pause or skip the affected symbol; credential-level
  failures are the class that may stop the bot.
- Runtime config and strategy files support controlled hot reload; API-key changes
  remain restart-required.
- Detached launcher mode exits the wrapper after a successful child launch while
  leaving the bot process running.

## 6. Same-Core Research and Backtesting

Historical research is deliberately separated from live trading:

1. Refresh a local OHLCV archive through a data-ingestion companion workflow.
2. Pass the archive root to offline research tools.
3. Run same-core replay, enabled-universe evaluation, ranking, and focused sweeps.
4. Compare baseline and candidate artifacts.
5. Promote only after evidence review into testnet, shadow, and then live rollout.

Read: [Research / Backtesting](research/backtesting.md).

## 7. Artifact Boundaries

- Mutable runtime state: `data/<env>/`.
- Mutable metrics state: `data/metrics/<env>/`.
- Runtime logs: `logs/<env>/<hostname>/`.
- Root process-control logs: `logs/watchdog.log`, `logs/bot_launcher.log`.
- Generated offline outputs: `data/out/<domain>/`.
- Human-maintained documentation: `docs/`.

## 8. Documentation Index

- [Architecture](architecture/project_map.md)
- [Research / Backtesting](research/backtesting.md)
- [Testing](testing/testing_guide.md)
- [Logging and Artifacts](operations/logging.md)
- [Shared Scope](../shared/docs_scope.md)
- [Public Sync Manifest](../shared/public_sync_manifest.md)

## 9. Safety Notes

- Start with testnet and dry-run.
- Never enable withdrawals for trading API keys.
- Review risk limits before any mainnet rollout.
- Do not publish runtime state, generated data archives, or internal evidence.
