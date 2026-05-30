# Documentation Scope

## Purpose

`TradingBinanceBot` is the public documentation repository for a private trading-bot implementation.

## In Scope

- Public-safe user and operator documentation.
- Stable architecture overviews and ownership boundaries.
- Testing and validation workflows.
- Logging, metrics, and generated-artifact path contracts.
- Research/backtesting workflow documentation at the contract level.
- Cross-repository integration references that do not expose private internals.

## Out of Scope

- Private runtime source code.
- API secrets, environment credentials, chat identifiers, and tokens.
- Production runtime data, balances, positions, trades, and logs.
- Internal-only operational artifacts and raw audit evidence.
- Workstation-specific absolute paths.
- Strategy-specific candidate files, rankings, or unpublished rollout decisions.

## Repository Boundary

- Public docs repository: `TradingBinanceBot`.
- Private implementation: maintained in a separate non-public repository.

## Publication Rule

Publish contracts and operator guidance, not private implementation details.
When a public explanation needs an example, use placeholders and generic paths.
