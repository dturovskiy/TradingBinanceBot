# Changelog

All notable documentation changes for `TradingBinanceBot` are tracked here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Planned

- Extend public API-domain documentation where the contract is stable and safe to publish.
- Add CI automation for language parity and markdown link checks.

## [2026-05-30] - Current Architecture and Research Sync

### Added

- Public-safe research/backtesting guides in English, Ukrainian, and French.
- Shared public sync manifest with source snapshot provenance.
- Shared release checklist for documentation-only publication.
- Glossary entries for archive root, same-core replay, artifact ownership, and rollout gates.

### Changed

- Synced public documentation after a public-safety review of the private implementation on `2026-05-26`.
- Clarified the boundary between the public documentation repository and the private implementation.
- Updated architecture maps with runtime ownership boundaries, observability,
  local interface, tooling, and artifact-path contracts.
- Updated testing guides to cover documentation validation, research workflows,
  launcher behavior checks, and generated-output locations.
- Updated logging guides to separate runtime logs, mutable metrics state, root-level
  control logs, and generated offline outputs.
- Updated language parity validation to require the research/backtesting page.

### Security

- No runtime source code, credentials, production data, workstation-specific paths,
  or strategy-specific candidate artifacts are exported by this sync.

## [2026.02.28] - Documentation Architecture Restructure

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

## [2025.12.26] - Stage 3 Documentation Baseline (Archived)

### Notes

- This baseline captured Stage 3 refactoring context.
- Later runtime changes made parts of that snapshot outdated.
- The 2026-02-28 release superseded Stage 3 docs for daily operations.
