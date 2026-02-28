# Testing Guide (EN)

Updated: 2026-02-28

This guide documents the current test/validation workflow used by the private `BinaceBot` runtime.

## 1. Prerequisites

From private repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 2. Main Validation Scripts

### Quick validation

```bash
./scripts/testing/run_tests_quick.sh
```

Use for fast iteration checks.

### Full validation

```bash
./scripts/testing/run_tests.sh
```

Includes stricter checks and benchmark/non-regression path.

## 3. Direct Test Commands

Run full pytest suite:

```bash
.venv/bin/python -m pytest tests/ -v
```

Run one module:

```bash
.venv/bin/python -m pytest tests/test_risk_manager.py -v
```

Run feature-flag/runtime contract tests:

```bash
.venv/bin/python -m pytest tests/test_feature_flags_contract.py -v
.venv/bin/python -m pytest tests/test_feature_flag_runtime_contract.py -v
```

Run trading execution guardrails tests:

```bash
.venv/bin/python -m pytest tests/test_trading_executor_buy_guardrails.py -v
```

## 4. Type Checking

```bash
.venv/bin/python -m mypy src --config-file config/.mypy.ini
```

## 5. Useful Focus Areas

- Risk policy engine: `tests/test_risk_manager.py`
- Runtime risk integration: `tests/test_trading_executor_buy_guardrails.py`
- Config contract: `tests/test_config_loader_validation.py`
- Feature flags contract: `tests/test_feature_flags_contract.py`
- Telegram flows: `tests/test_telegram_*`
- Maintenance cadence: `tests/test_bot_runner_periodic_maintenance.py`

## 6. Test Inventory Snapshot

- Test modules: `120`
- Property test modules: `31`

## 7. Logs and Artifacts

Common output locations:

- `logs/quick_validation_*.log`
- `logs/test_validation_*.log`
- `tools/benchmark/*.json`

## 8. Recommended Workflow

1. Run `run_tests_quick.sh` during development.
2. Run targeted module tests for touched components.
3. Run full `run_tests.sh` before merge/release.
4. Review logs for retries/errors/performance drifts.

## 9. Troubleshooting

- `Permission denied` on scripts:

```bash
chmod +x scripts/testing/run_tests.sh scripts/testing/run_tests_quick.sh
```

- Missing dependencies:

```bash
pip install -r requirements-dev.txt
```

- MyPy config path mismatch:

Use `config/.mypy.ini` (not root `mypy.ini`).
