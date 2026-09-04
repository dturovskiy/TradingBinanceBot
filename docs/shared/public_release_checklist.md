# Public Documentation Release Checklist

## Before Applying a Sync

- Work on a clean non-`main` branch.
- Record the exact reviewed private source commit and review date.
- Review the intended changed-path set and source evidence before applying changes.
- Confirm the planned patch is limited to public documentation and documentation-validation files.

## Before Commit

- Confirm the expected changed-path manifest.
- Confirm new files are staged.
- Confirm no delete/rename occurred unless explicitly approved.
- Confirm `README.md` and `docs/index.md` navigation is updated when topic families or paths changed.

## Validation

Run:

```bash
python3 scripts/docs/check_language_parity.py
bash scripts/docs/validate_links.sh
git diff --check
git status --short
git diff --stat
git diff --cached --stat
```

If Bash execution is blocked by the tool policy, run an equivalent internal Markdown-link existence check and record that limitation.

## Public-Safety Review

Confirm the patch contains no:

- credentials, secrets, tokens, or chat identifiers;
- balances, positions, trade-ledger contents, or runtime logs;
- hostnames or PIDs;
- absolute machine paths;
- mount/storage or DNS/network topology;
- current strategy/candidate names, rankings, or active research status;
- exact production limits or thresholds;
- exact operational recovery commands or incident procedures;
- private implementation source when contract-level prose is sufficient;
- private evidence identifiers/hashes unnecessary for documentation provenance;
- transient machine/environment details or current operational/research state.

The reviewed private Git commit SHA recorded in the sync manifest is an approved provenance identifier.

## Language and Navigation Review

- EN, UA, and FR expose the same required paths.
- Corresponding pages preserve the same section hierarchy and factual claims.
- Corresponding pages keep the same security boundary and navigation targets.
- `README.md` and `docs/index.md` link to all current public topic families.

## After Applying the Sync

- Review `git status --short` and the complete diff/stat for unintended scope expansion.
- Confirm source provenance and navigation remain internally consistent.
- Repeat the public-safety review against the final staged patch.

## Commit Gate

Do not commit until validation, diff review, navigation review, and public-safety review pass.
