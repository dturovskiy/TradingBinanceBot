# Preregistered Options and Dataset-Build Research (EN)

## 1. Purpose
<!-- parity-key: options.scope -->

Offline options/data research can use preregistered, reproducible, bounded dataset-build workflows with explicit provenance and acceptance controls. This page documents that workflow contract without exposing current build state or storage layout.

## 2. Preregistration
<!-- parity-key: options.preregistration -->

The intended dataset scope, evaluation role, and acceptance conditions should be defined before final outcome inspection where preregistration is part of the methodology. A preregistered holdout or dataset role is not a repeated tuning surface.

## 3. Reproducible Bounded Builds
<!-- parity-key: options.dataset-build -->

Dataset construction should use explicit source identity, transformation context, and deterministic or reproducible build semantics. Work should be bounded conceptually so an offline data workflow cannot become an uncontrolled runtime dependency.

## 4. Acceptance Controls
<!-- parity-key: options.acceptance -->

Build acceptance is distinct from evidence of market edge. Required integrity, completeness, provenance, and contract checks can reject an artifact without converting that rejection or acceptance into trading authorization.

## 5. Provenance and Evidence Binding
<!-- parity-key: options.provenance -->

Dataset identity, source provenance, transformation provenance, and downstream evidence bindings should remain explicit. Missing or incompatible required bindings fail closed rather than silently joining artifacts from different research contexts.

## 6. Public-Safety Boundary
<!-- parity-key: options.public-boundary -->

Do not publish current dataset roots, mount/storage topology, build status, current acceptance verdicts, private hashes, account/provider credentials, exact budgets, current options candidates, active strategy parameters, or the next operator action.

## 7. Related Guides

- [Data-Source Contracts](data_sources.md)
- [Evidence Contracts](evidence_contracts.md)
- [Research / Backtesting](backtesting.md)
