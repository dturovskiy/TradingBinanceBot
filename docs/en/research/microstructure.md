# Microstructure and Execution-Quality Research (EN)

## 1. Purpose
<!-- parity-key: microstructure.scope -->

Microstructure research evaluates execution-quality evidence without turning data collection into an order-placement surface. The public contract describes methodology, not active strategy logic or production calibration.

## 2. Market-State Evidence
<!-- parity-key: microstructure.market-state -->

Spread, depth, and related order-book context can be treated as research evidence when their event-time and provenance are explicit. Such observations describe market conditions; they do not by themselves authorize a trade.

## 3. Executable-Price Realism
<!-- parity-key: microstructure.executable-price -->

Research should distinguish an executable-price model from simplistic reference-price assumptions when execution realism matters. The methodology may account for market-state constraints without publishing current fee, slippage, sizing, or calibration parameters.

## 4. Provenance-Isolated Telemetry
<!-- parity-key: microstructure.provenance -->

Microstructure observations should retain source, observation-time, decision-time, and outcome provenance so evidence is not silently mixed across incompatible contexts. Missing or ambiguous binding should fail closed for evidence use.

## 5. Separation from Execution and Promotion
<!-- parity-key: microstructure.separation -->

Collecting or analyzing microstructure telemetry is separate from order execution and from promotion authorization. Favorable execution-quality evidence can support evaluation, but required dataset-integrity, execution/domain-parity, and other promotion gates remain independent.

## 6. Public-Safety Boundary
<!-- parity-key: microstructure.public-boundary -->

Do not publish current sampling cadence, recorder enablement, budgets, fee/slippage assumptions, strategy thresholds, candidate rankings, profitability conclusions, live order-book snapshots, or operational telemetry contents.

## 7. Related Guides

- [Research / Backtesting](backtesting.md)
- [Evidence Contracts](evidence_contracts.md)
- [Data-Source Contracts](data_sources.md)
