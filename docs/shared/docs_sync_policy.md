# Documentation Sync Policy

## Objective

Keep public documentation aligned with stable private behavior while preserving the public/private boundary.

## Source of Truth

The private implementation is the source of truth. Every public sync must record the exact reviewed private Git commit SHA and review date in `public_sync_manifest.md`.

## Trigger Events

Review public docs after changes to:

1. trading/runtime behavior or ownership;
2. execution-state or recovery behavior;
3. configuration ownership or precedence;
4. research dataset or provenance contracts;
5. replay/live parity semantics;
6. promotion/evidence gates;
7. fault-tolerance or failure-path behavior;
8. observability contracts;
9. operator-facing lifecycle or control behavior.

## Mandatory Update Targets

Review affected EN/UA/FR pages, shared governance docs, navigation, and `CHANGELOG.md`. Preserve language-path parity and the same factual/security boundary across languages.

## Public-Safety Filter

Before publication, remove credentials, runtime state, logs, current strategies/candidates/rankings, production thresholds, infrastructure topology, exact recovery commands, unnecessary private hashes/evidence IDs, and implementation source excerpts.

## Verification Steps

1. Run `python3 scripts/docs/check_language_parity.py`.
2. Run the repository link validator when the execution policy permits it; otherwise run equivalent internal Markdown-link validation.
3. Run `git diff --check`.
4. Review changed-path scope and staged diff.
5. Run the public-safety review.

## Ownership

Documentation maintainers are responsible for source binding, factual parity, validation, and public-safety review before merge.
