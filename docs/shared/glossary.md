# Glossary

- `TradingBinanceBot`: public documentation repository.
- `TradingExecutor`: orchestrator of per-iteration buy/sell/risk flow.
- `RiskManager`: portfolio risk-policy evaluator with modes such as `off`, `shadow`, and `enforce`.
- `Feature Flag`: runtime rollout switch in configuration.
- `Circuit Breaker`: guard that blocks a symbol after repeated failures.
- `Illiquid Position`: symbol temporarily blocked from trading.
- `Dry-run`: simulation mode without real order placement.
- `Testnet`: Binance testing environment.
- `Mainnet`: live Binance environment with real funds.
- `Archive Root`: local directory containing normalized historical OHLCV files and summary metadata.
- `Data-Ingestion Layer`: companion workflow that fetches and stores historical market data.
- `Same-Core Replay`: research/backtesting execution that reuses the trading core instead of maintaining a second strategy implementation.
- `Research Layer`: offline tools that run replay, ranking, sweeps, and proof workflows.
- `Baseline`: reference result used for comparison.
- `Candidate`: proposed strategy/configuration revision evaluated against a baseline.
- `Promotion Gate`: evidence checkpoint before moving a candidate toward testnet, shadow, or live rollout.
- `Generated Offline Output`: non-runtime artifact stored under `data/out/<domain>/`.
- `Artifact Ownership`: rule describing the canonical home of a document, log, state file, or generated report.
