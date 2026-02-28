# Changelog

All notable documentation changes for `TradingBinanceBot` are tracked here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Planned

- Add cross-repo docs validation checklist automation.
- Add API module reference pages split by domain.

## [2026.02.28] - Full Documentation Sync with Current Runtime

### Added

- Multilingual technical guides:
  - `PROJECT_MAP_UA.md`, `PROJECT_MAP_FR.md`
  - `TESTING_GUIDE_UA.md`, `TESTING_GUIDE_FR.md`
  - `LOGGING_UA.md`, `LOGGING_FR.md`

### Changed

- Rebuilt language router in `README.md`.
- Fully refreshed localized readmes:
  - `README_LOCALIZATIONS/README_UA.md`
  - `README_LOCALIZATIONS/README_EN.md`
  - `README_LOCALIZATIONS/README_FR.md`
- Reworked architecture map (`PROJECT_MAP_EN.md`) to match current runtime:
  - `TradingExecutor`-driven iteration flow,
  - risk manager policy layer,
  - Telegram watchdog control plane,
  - feature-flag rollout contract.
- Reworked testing guide (`TESTING_GUIDE_EN.md`) to current script paths:
  - `scripts/testing/run_tests.sh`
  - `scripts/testing/run_tests_quick.sh`
  - `config/.mypy.ini`.
- Reworked logging guide (`LOGGING.md`) to real runtime layout:
  - `logs/{mainnet|testnet}/<hostname>/...`
  - `logs/watchdog.log`
  - size-based rotation (`10MB`, `30` backups).

### Fixed

- Removed outdated references to root-level legacy test scripts.
- Removed stale assumptions about daily+compressed rotation.
- Removed stale module references from older architecture snapshots.

## [2025.12.26] - Stage 3 Documentation Baseline (Archived)

### Notes

- This baseline captured Stage 3 refactoring context.
- Later runtime changes made parts of that snapshot outdated.
- The 2026-02-28 release supersedes Stage 3 docs for daily operations.
