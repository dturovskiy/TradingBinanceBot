# Public Documentation Release Checklist

## Before Applying a Sync

- Work on a clean branch in `TradingBinanceBot`.
- Review the patch manifest and source implementation snapshot.
- Confirm the patch contains documentation and docs-validation files only.

## After Applying a Sync

Run:

```bash
python3 scripts/docs/check_language_parity.py
bash scripts/docs/validate_links.sh
git diff --check
git status --short
git diff --stat
```

## Public-Safety Review

Confirm that the diff contains no:

- API keys, secrets, tokens, or chat identifiers;
- production balances, positions, trades, or logs;
- absolute workstation paths;
- generated data archives;
- private source-code files;
- unpublished strategy-specific ranking or rollout artifacts.

## Commit

After review:

```bash
git add README.md CHANGELOG.md docs scripts/docs/check_language_parity.py
git commit -m "docs: sync public documentation with current architecture and research contracts"
```
