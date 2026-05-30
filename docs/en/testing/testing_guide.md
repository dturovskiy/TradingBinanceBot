# Testing Guide (EN)

Updated: 2026-05-30

## 1. Scope

This page documents public-safe validation workflows for the private implementation.
Exact test inventory counts are intentionally not frozen in public docs because they
change frequently.

## 2. Runtime Validation

From the private implementation root:

```bash
./scripts/testing/run_tests_quick.sh
./scripts/testing/run_tests.sh
```

Use quick validation during iteration and the full suite before merge or rollout.

## 3. Focus Areas

Review tests and evidence for:

- dry-run: no real Spot or Convert execution;
- SELL-before-BUY iteration ordering;
- config ownership and precedence;
- risk manager modes and symbol-level containment;
- config/strategy hot reload and API-key restart boundary;
- detached launcher behavior;
- archive-root loading and same-core replay parity;
- generated-output routing under `data/out/<domain>/`.

## 4. Research Validation

For research workflows, use a local archive root:

```bash
python tools/analysis/<research-tool>.py --archive-root <archive-root>
```

A rollout-influencing result should be reproducible from a stable archive root and
should produce reviewable baseline-vs-candidate evidence.

## 5. Documentation Validation

From the public documentation repository root:

```bash
python3 scripts/docs/check_language_parity.py
bash scripts/docs/validate_links.sh
git diff --check
```

## 6. Generated Outputs

Generated validation outputs should use domain-specific paths such as:

```text
data/out/testing/
data/out/benchmark/
data/out/integration/
data/out/readiness/
data/out/audit/
```

Do not place generated output under `docs/` unless it is a deliberately curated,
human-maintained public document.
