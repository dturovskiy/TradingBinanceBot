# Public Documentation Release Checklist

## Before Commit

- Work on a non-`main` branch.
- Confirm the expected changed-path manifest.
- Confirm new files are staged.
- Record the exact reviewed private source commit.
- Confirm no delete/rename occurred unless explicitly approved.

## Validation

Run:

```bash
python3 scripts/docs/check_language_parity.py
bash scripts/docs/validate_links.sh
git diff --check
git diff --cached --stat
```

If Bash execution is blocked by the tool policy, run an equivalent internal Markdown-link existence check and record that limitation.

## Public-Safety Review

Confirm the staged patch contains no:

- credentials, secrets, tokens, or chat identifiers;
- balances, positions, trade-ledger contents, or runtime logs;
- hostnames or PIDs;
- absolute machine paths;
- mount/storage or DNS/network topology;
- current strategy/candidate names, rankings, or active research status;
- exact production limits or thresholds;
- exact operational recovery commands or incident procedures;
- private implementation source when contract-level prose is sufficient;
- private evidence identifiers/hashes unnecessary for documentation provenance.

The reviewed private Git commit SHA recorded in the sync manifest is an approved provenance identifier.

## Language and Navigation Review

- EN, UA, and FR expose the same required paths.
- Corresponding pages preserve the same section hierarchy and factual claims.
- Corresponding pages keep the same security boundary and navigation targets.
- `README.md` and `docs/index.md` link to all current public topic families.

## Commit Gate

Do not commit until validation, diff review, and public-safety review pass.
