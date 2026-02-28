# Changelog

All notable documentation changes for `TradingBinanceBot` are tracked here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Planned

- Add CI workflow for docs parity and markdown link checks.
- Add API domain pages (market data, execution, risk, telemetry).

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
- The 2026-02-28 releases supersede Stage 3 docs for daily operations.
