# Changelog

All notable documentation changes for `TradingBinanceBot` are tracked here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Prepared - 2026-09-04 Public Documentation Sync

#### Added

- Durable execution/recovery contract pages in EN/UA/FR.
- Evidence/provenance contract pages in EN/UA/FR.
- Reliability/failure-handling and operator-control contract pages in EN/UA/FR.
- Public module-family reference pages in EN/UA/FR without mirroring the private source tree.
- Microstructure/execution-quality, external data-source, and preregistered options/dataset-build methodology pages in EN/UA/FR.

#### Changed

- Refreshed public architecture ownership, including durable execution state/recovery.
- Modernized research/backtesting methodology around event time, deterministic replay, no-future-leakage, dataset identity, time-safe splits, and promotion firewalls.
- Expanded testing taxonomy without freezing a test count or coverage percentage.
- Strengthened public-sync provenance and public-safety governance.
- Preserved EN/UA/FR path, hierarchy, factual, security-boundary, and link parity.
- Expanded logging/observability guidance with structured telemetry, activation/profile, freshness/expected-idle, provenance, and non-mutating observation semantics.
- Documented scanner isolation, the no-order boundary, bounded/failure-isolated research work, and fail-closed promotion evidence requirements.
- Clarified layered/grouped portfolio-risk ownership and reason/model separation without publishing thresholds or current exposure.
- Expanded README/index/overview navigation to the full curated public-safe topic set.
- Added semantic `parity-key` validation for new multilingual topic families while retaining human semantic review.
- Expanded scope/sync/release governance for provider, operator-control, microstructure, reliability, and offline dataset-workflow safety boundaries.

#### Security

- Published no private implementation source, runtime/trading state, current strategies/candidates/rankings, production thresholds, infrastructure topology, exact privileged/recovery commands, provider credentials/private endpoints, current recorder/source state, exact acquisition/sampling/calibration budgets, or private operational evidence.
- The reviewed private Git SHA is recorded only as approved documentation provenance.

### Provenance

- Review date: `2026-09-04`
- Reviewed private source: `05a4214895111bcdbb7960223b4af232c066c48c`
- Previous public sync: `2026-05-30`
- Previous exact private source SHA: `not recorded`

## [2026-05-30] - Current Architecture and Research Sync

### Added

- Public-safe research/backtesting guides in English, Ukrainian, and French.
- Shared public sync manifest with source snapshot provenance.
- Shared release checklist for documentation-only publication.
- Glossary entries for archive root, same-core replay, artifact ownership, and rollout gates.

### Changed

- Synced public documentation after a public-safety review of the private implementation on `2026-05-26`.
- Clarified the boundary between the public documentation repository and the private implementation.
- Updated architecture maps with runtime ownership boundaries, observability, local interface, tooling, and artifact-path contracts.
- Updated testing guides to cover documentation validation, research workflows, launcher behavior checks, and generated-output locations.
- Updated logging guides to separate runtime logs, mutable metrics state, root-level control logs, and generated offline outputs.
- Updated language parity validation to require the research/backtesting page.

### Security

- No runtime source code, credentials, production data, workstation-specific paths, or strategy-specific candidate artifacts were exported by this sync.

## [2026-02-28] - Documentation Architecture Restructure

### Added

- New language-first tree under `docs/`:
  - `docs/en/*`
  - `docs/ua/*`
  - `docs/fr/*`
- New shared governance docs:
  - `docs/shared/docs_scope.md`
  - `docs/shared/docs_sync_policy.md`
  - `docs/shared/style_guide.md`
  - `docs/shared/glossary.md`
- New docs maintenance scripts:
  - `scripts/docs/validate_links.sh`
  - `scripts/docs/check_language_parity.py`
- New central navigation page: `docs/index.md`.

### Changed

- Root `README.md` now routes to the new `docs/` structure.
- Technical documentation moved to language-scoped paths:
  - architecture maps,
  - testing guides,
  - logging guides,
  - localized overviews.

### Removed

- Legacy duplicate root files:
  - `PROJECT_MAP_*.md`
  - `TESTING_GUIDE_*.md`
  - `LOGGING*.md`
- Legacy `README_LOCALIZATIONS/` directory.

## [2025-12-26] - Stage 3 Documentation Baseline (Archived)

### Notes

- This baseline captured Stage 3 refactoring context.
- Later runtime changes made parts of that snapshot outdated.
- The 2026-02-28 release superseded Stage 3 docs for daily operations.
