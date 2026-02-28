# Documentation Sync Policy

## Objective

Keep public documentation aligned with private runtime behavior.

## Trigger Events

Update docs after any of the following:

1. Runtime behavior change in trading flow.
2. Config contract change.
3. New/changed Telegram command behavior.
4. Logging layout or retention change.
5. New feature flag or rollout contract change.

## Mandatory Update Targets

For each behavior change, review and update:

- `docs/en/*` affected sections.
- `docs/ua/*` affected sections.
- `docs/fr/*` affected sections.
- `CHANGELOG.md`.

## Verification Steps

1. Run `scripts/docs/check_language_parity.py`.
2. Run `scripts/docs/validate_links.sh`.
3. Confirm `docs/index.md` points to current files.

## Ownership

- Primary maintainers: project maintainers of private runtime.
- Documentation PRs should include changelog entry and parity verification.
