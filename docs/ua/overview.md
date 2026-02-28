# Документація Binance Trading Bot (UA)

Публічна документація для приватного проєкту `BinaceBot`.

## 1. Призначення цього репозиторію

`TradingBinanceBot` — це публічний шар документації для приватного production-коду.

- Приватний репозиторій (`BinaceBot`): runtime-код, ключі API, виконання торгів.
- Публічний репозиторій (`TradingBinanceBot`): архітектура, запуск, операційні процедури, тестування, стандарти логування.

## 2. Поточний стан системи (синхронізовано 2026-02-28)

### Форма рантайму

- Thin entrypoint: `src/main_bot.py` + CLI (`--testnet`, `--dry-run`, `--config`, `--strategy`, `--debug`).
- Координатор циклу: `src/bot_runner.py`.
- Оркестрація торгівлі: `src/trading/trading_executor.py`.
- Логіка сигналів/виконання: `src/trade_processor.py`.
- Портфельний risk-policy: `src/risk/risk_manager.py` з режимами `off|shadow|enforce`.
- Telegram керування: watchdog + модулі `src/telegram_ui/*`.

### Ключовий торговий цикл

Кожна ітерація проходить по фазах:

1. Завантаження market data (ціни + баланси).
2. Repricing відкритих позицій.
3. SELL-прохід.
4. Оновлення балансів (за потреби).
5. BUY-прохід.
6. Збереження стану + decision summary + runtime KPI snapshot.

Важлива властивість: **SELL виконується перед BUY** для зменшення конфліктів зі stale balance.

### Risk і feature flags

У `config/config.json` підтримуються rollout-прапори:

- `freeze_dynamic_tp_sl`
- `strict_min_notional_enforcement`
- `use_closed_candles_for_signals`
- `intelligent_illiquid_unlocking`

Частина прапорів працює у preview/compatibility режимі.

## 3. Ownership конфігурації (Hard-Cut)

- `config/config.json`: операційні runtime-налаштування (інтервали, retry, alerts, risk-manager mode).
- `config/strategy*.json`: торгова логіка (TP/SL, фільтри, buy targets, пороги індикаторів).
- Глобальний override обмежений (`settings.enable_ta_confirmation`).

## 4. Основні можливості

- Spot-виконання ордерів + інтеграція Convert path.
- Модульні фільтри входу: RSI, SMA, ATR, Volume.
- Risk manager з enforce/shadow телеметрією.
- Circuit breaker + керування неліквідними позиціями.
- Структуроване логування + періодичне збереження метрик.
- Віддалене Telegram-керування процесом через watchdog.

## 5. Безпечний старт

Рекомендований перший запуск у приватному репозиторії:

```bash
cp .env.example .env
./start_bot.sh --testnet --dry-run
```

Потім базова перевірка:

```bash
./scripts/testing/run_tests_quick.sh
```

## 6. Telegram-команди керування

Керування процесом (watchdog):

- `/start_bot`
- `/stop_bot`
- `/restart_bot`
- `/check_bot`
- `/reload_config`

Моніторинг:

- `/status`
- `/positions`
- `/balance`
- `/health`
- `/performance`
- `/report`
- `/illiquid`

## 7. Тестовий профіль якості

- Модулі тестів: `120`
- Модулі property tests: `31`
- Покриті контракти: feature flags, risk manager, periodic maintenance, Telegram flows, config validation.

## 8. Індекс документації

- Архітектура (EN): [../en/architecture/project_map.md](../en/architecture/project_map.md)
- Архітектура (UA): [architecture/project_map.md](architecture/project_map.md)
- Архітектура (FR): [../fr/architecture/project_map.md](../fr/architecture/project_map.md)
- Тестування (EN): [../en/testing/testing_guide.md](../en/testing/testing_guide.md)
- Тестування (UA): [testing/testing_guide.md](testing/testing_guide.md)
- Тестування (FR): [../fr/testing/testing_guide.md](../fr/testing/testing_guide.md)
- Логування (EN): [../en/operations/logging.md](../en/operations/logging.md)
- Логування (UA): [operations/logging.md](operations/logging.md)
- Логування (FR): [../fr/operations/logging.md](../fr/operations/logging.md)
- Історія змін: [../../CHANGELOG.md](../../CHANGELOG.md)

## 9. Нотатки з безпеки

- Спочатку тільки testnet.
- На API ключах не вмикати `withdrawals`.
- Перед змінами стратегії завжди проганяти `--dry-run`.
- Перед mainnet перевіряти ліміти `risk_manager`.
