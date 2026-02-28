# Гід з Тестування (UA)

Оновлено: 2026-02-28

Цей гід описує актуальний workflow тестування приватного `BinaceBot`.

## 1. Передумови

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 2. Основні скрипти

Швидка перевірка:

```bash
./scripts/testing/run_tests_quick.sh
```

Повна валідація:

```bash
./scripts/testing/run_tests.sh
```

## 3. Прямі команди

Повний pytest:

```bash
.venv/bin/python -m pytest tests/ -v
```

Точкові приклади:

```bash
.venv/bin/python -m pytest tests/test_risk_manager.py -v
.venv/bin/python -m pytest tests/test_feature_flags_contract.py -v
.venv/bin/python -m pytest tests/test_trading_executor_buy_guardrails.py -v
```

MyPy:

```bash
.venv/bin/python -m mypy src --config-file config/.mypy.ini
```

## 4. Ключові зони покриття

- Контракт risk manager.
- Контракт feature flags.
- Валідація конфігів.
- Telegram/watchdog флоу.
- Періодичне обслуговування `BotRunner`.

## 5. Зріз тестового інвентаря

- Модулі тестів: `120`
- Модулі property tests: `31`

## 6. Артефакти

- `logs/quick_validation_*.log`
- `logs/test_validation_*.log`
- `tools/benchmark/*.json`

## 7. Рекомендований порядок

1. Швидкий прогін під час розробки.
2. Точкові тести по змінених модулях.
3. Повний прогін перед merge/release.
4. Перевірка логів на помилки/регрес.
