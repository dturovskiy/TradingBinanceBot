# Documentation Scope

## Purpose

`TradingBinanceBot` is a public documentation-only repository for a private trading/runtime/research implementation.

## In Scope

- Stable public-safe architecture, module-family references, and ownership boundaries.
- Public-safe lifecycle, readiness, execution-state, recovery, reliability, and bounded failure-handling semantics.
- Portfolio-risk concepts without current production thresholds.
- Testing taxonomy and validation methodology.
- Research/backtesting methodology, including event-time and replay semantics.
- Dataset, external-data provenance, evidence, and promotion methodology at the contract level.
- Microstructure/execution-quality methodology without current calibration or strategy detail.
- Preregistered, reproducible, bounded offline options/data-build methodology without current storage/run state.
- Operator/developer-facing notification and control contracts that do not expose privileged command syntax or private operational detail.
- Logging, observability, telemetry, and generated-artifact concepts.

## Out of Scope

- Private runtime or research implementation source.
- Credentials, secrets, tokens, chat identifiers, balances, positions, trades, or runtime logs.
- Current strategy/candidate names, rankings, profitability, research verdicts, or rollout state.
- Exact production thresholds, limits, or current risk settings.
- Hostnames, PIDs, absolute machine paths, mount/storage topology, or DNS/network topology.
- Exact recovery or privileged operator commands, crash sequences, journal formats, or operational incident evidence.
- Provider credentials/private endpoints, current external-source availability, exact acquisition cadence/budgets, or provider-account configuration.
- Current recorder enablement, current sampling/calibration settings, live order-book snapshots, or current dataset-build state.
- Private evidence identifiers/content hashes except an explicitly approved Git source commit used for documentation provenance.

## Repository Boundary

- Public documentation: `TradingBinanceBot`.
- Private implementation: maintained separately and not mirrored here.

## Publication Rule

Publish stable concepts, contracts, ownership boundaries, and methodology. Do not publish private implementation mechanics or current operational state.
