# Public Sync Manifest

## Current Public-Safe Snapshot

- Public documentation sync date: `2026-05-30`
- Private implementation: maintained in a separate non-public repository
- Public-safe source review date: `2026-05-26`

## Curated Source Contracts

This public-safe sync was derived from stable contracts represented by:

- root runtime overview;
- current project map;
- configuration ownership contract;
- runtime behavior contract;
- artifact ownership matrix;
- data archive and backtesting research guide;
- launcher/process-control behavior affecting detached starts.

## Publication Boundary

This repository is not a mirror of the private implementation. The sync exports
operator-facing contracts and architecture guidance only.

The sync intentionally excludes:

- private runtime source;
- credentials and environment values;
- production state and logs;
- workstation-specific paths;
- unpublished strategy candidates, rankings, and internal rollout evidence.

## Review Rule

When the private implementation changes after the public-safe review date above, review
`docs/shared/docs_sync_policy.md` and run another public-safe sync pass.
