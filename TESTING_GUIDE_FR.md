# Guide de Test (FR)

Mise a jour: 2026-02-28

Guide du workflow de validation du runtime prive `BinaceBot`.

## 1. Prerequis

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 2. Scripts principaux

Validation rapide:

```bash
./scripts/testing/run_tests_quick.sh
```

Validation complete:

```bash
./scripts/testing/run_tests.sh
```

## 3. Commandes directes

```bash
.venv/bin/python -m pytest tests/ -v
.venv/bin/python -m pytest tests/test_risk_manager.py -v
.venv/bin/python -m pytest tests/test_feature_flags_contract.py -v
.venv/bin/python -m pytest tests/test_trading_executor_buy_guardrails.py -v
.venv/bin/python -m mypy src --config-file config/.mypy.ini
```

## 4. Zones critiques

- Contrat risk manager.
- Contrat feature flags.
- Validation config.
- Flux Telegram/watchdog.
- Maintenance periodique de `BotRunner`.

## 5. Inventaire observe

- Modules de test: `120`
- Modules property tests: `31`

## 6. Artifacts

- `logs/quick_validation_*.log`
- `logs/test_validation_*.log`
- `tools/benchmark/*.json`

## 7. Workflow recommande

1. Run rapide pendant dev.
2. Tests cibles sur modules modifies.
3. Run complet avant merge/release.
4. Verification des logs et regressions.
