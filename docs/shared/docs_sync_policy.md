# Documentation Sync Policy

## Objective

Keep public documentation aligned with stable private runtime behavior without
exporting private implementation details.

## Source of Truth

The private implementation is maintained in a separate non-public repository. Each public sync must record a public-safe review date in `docs/shared/public_sync_manifest.md`.

## Trigger Events

Review public docs after any of the following:

1. Runtime behavior change in trading flow.
2. Config ownership or precedence change.
3. New or changed Telegram/operator command behavior.
4. Logging layout, metrics layout, artifact ownership, or retention change.
5. New feature flag, rollout contract, or execution-safety rule.
6. Research/backtesting workflow, archive contract, or promotion-gate change.
7. Launcher or process-control behavior change that affects operators.

## Mandatory Update Targets

For each public-facing behavior change, review and update:

- `docs/en/*` affected sections.
- `docs/ua/*` affected sections.
- `docs/fr/*` affected sections.
- `docs/shared/glossary.md`.
- `docs/shared/public_sync_manifest.md`.
- `CHANGELOG.md`.

## Public-Safety Filter

Before publication, remove:

- credentials and secrets;
- production state, balances, positions, trades, and logs;
- machine-specific absolute paths;
- unpublished strategy candidates and rankings;
- raw internal-only evidence;
- source-code excerpts that are unnecessary for operator documentation.

## Verification Steps

1. Run `python3 scripts/docs/check_language_parity.py`.
2. Run `bash scripts/docs/validate_links.sh`.
3. Run `git diff --check`.
4. Confirm `docs/index.md` points to current files.
5. Review the public release checklist.

## Ownership

- Primary maintainers: maintainers of the private implementation.
- Documentation updates should include a changelog entry, source snapshot,
  parity verification, link validation, and a public-safety review.
