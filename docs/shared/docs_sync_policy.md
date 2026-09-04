# Documentation Sync Policy

## Objective

Keep public documentation aligned with stable private behavior while preserving the public/private boundary.

## Source of Truth

The private implementation is the source of truth. Every public sync must record the exact reviewed private Git commit SHA and review date in `public_sync_manifest.md`. A review date alone is not sufficient provenance for future syncs.

## Trigger Events

Review public docs after changes to:

1. trading/runtime behavior or ownership;
2. execution-state or recovery behavior;
3. configuration ownership or precedence;
4. research dataset or provenance contracts;
5. replay/live parity semantics;
6. promotion/evidence gates;
7. fault-tolerance or failure-path behavior;
8. observability or reliability contracts;
9. operator-facing lifecycle or control behavior;
10. microstructure/execution-quality research methodology;
11. external-data provenance or dataset-build contracts;
12. options/offline research workflow contracts;
13. public module-family ownership boundaries.

## Mandatory Update Targets

For each public-facing change, review as applicable:

- affected EN pages;
- semantically equivalent UA and FR pages;
- affected shared governance docs;
- `README.md` and `docs/index.md` when topic families or navigation change;
- `docs/shared/glossary.md`;
- `docs/shared/public_sync_manifest.md`;
- `CHANGELOG.md`.

Language variants must preserve the same factual claims, section hierarchy, navigation targets, and public-safety boundary. Topic families that adopt semantic `parity-key` markers must also preserve the same ordered marker set across EN/UA/FR.

## Public-Safety Filter

Before publication, remove credentials, runtime state, logs, current strategies/candidates/rankings, production thresholds, infrastructure topology, exact privileged/recovery commands, provider credentials/private endpoints, current external-source or recorder state, exact acquisition/sampling/calibration budgets, unnecessary private hashes/evidence IDs, and implementation source excerpts. Explicitly review the diff for machine-specific environment details, current operational/research state, and other transient private context.

## Verification Steps

1. Run `python3 scripts/docs/check_language_parity.py` and review semantic `parity-key` coverage for topic families that use it.
2. Run the repository link validator when the execution policy permits it; otherwise run equivalent internal Markdown-link validation.
3. Run `git diff --check`.
4. Review changed-path scope and staged diff.
5. Confirm root/index navigation points to current public pages when structure changed.
6. Run an explicit public-safety review for environment-specific detail and current private state.

## Ownership

Documentation maintainers are responsible for exact source binding, factual/language parity, validation, navigation consistency, and public-safety review before merge.
