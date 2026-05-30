# Документація Binance Trading Bot (UA)

Публічна безпечна документація для приватної реалізації торгового бота.

## 1. Межа репозиторіїв

`TradingBinanceBot` публікує стабільні операторські контракти. Runtime-код,
credentials, production-state та внутрішні докази залишаються приватними.

Поточний public-safe snapshot:

- дата public-safe review приватної основи: `2026-05-26`;
- дата синхронізації документації: `2026-05-30`.

## 2. Форма рантайму

- Thin entrypoint і CLI bootstrap.
- Власник верхньорівневого циклу: `BotRunner`.
- Власник orchestration кожної ітерації: `TradingExecutor`.
- Деталі symbol-level рішень і виконання: `TradeProcessor`.
- Семантика portfolio risk: `RiskManager`.
- Monitoring, observability, metrics, reporting, Telegram delivery та локальні control surfaces є окремими доменами.

## 3. Інваріант торгового циклу

Кожна ітерація готує market/position context, виконує SELL-перевірки,
за потреби оновлює баланси та лише після цього обробляє BUY-кандидатів.

Ключовий інваріант: **SELL виконується перед BUY**, щоб зменшити конфлікти зі stale balance.

## 4. Ownership конфігурації

- `config/config.json`: операційні runtime-параметри — cadence, retry,
  telemetry, notifications і режим risk manager.
- `config/strategy*.json`: торгова логіка — TP/SL, правила індикаторів,
  targets і підтримувані asset overrides.
- Strategy-owned ключі не мають fallback до operational config.
- Мінімальний глобальний TA override: `settings.enable_ta_confirmation`.

## 5. Безпека виконання

- `--dry-run` симулює виконання без реальних ордерів.
- Market-data і balance reads залишаються доступними для валідації.
- Convert paths працюють лише у mainnet і не мають виконуватися у dry-run.
- Symbol-level помилки мають блокувати або пропускати конкретний символ;
  зупинка всього бота зарезервована для credential-level проблем.
- Runtime config і strategy-файли підтримують контрольований hot reload;
  зміни API-ключів вимагають restart.
- У detached launcher mode wrapper завершується після успішного запуску child-процесу,
  а процес бота продовжує працювати.

## 6. Same-Core Research і Backtesting

Історичний research відділений від live trading:

1. Оновлюємо локальний OHLCV-архів через companion data-ingestion workflow.
2. Передаємо archive root в offline research tools.
3. Запускаємо same-core replay, enabled-universe evaluation, ranking і focused sweeps.
4. Порівнюємо baseline та candidate artifacts.
5. Лише після evidence review рухаємо candidate через testnet, shadow і live rollout.

Читайте: [Research / Backtesting](research/backtesting.md).

## 7. Межі артефактів

- Mutable runtime state: `data/<env>/`.
- Mutable metrics state: `data/metrics/<env>/`.
- Runtime logs: `logs/<env>/<hostname>/`.
- Root process-control logs: `logs/watchdog.log`, `logs/bot_launcher.log`.
- Generated offline outputs: `data/out/<domain>/`.
- Human-maintained documentation: `docs/`.

## 8. Індекс документації

- [Архітектура](architecture/project_map.md)
- [Research / Backtesting](research/backtesting.md)
- [Тестування](testing/testing_guide.md)
- [Логування та артефакти](operations/logging.md)
- [Shared Scope](../shared/docs_scope.md)
- [Public Sync Manifest](../shared/public_sync_manifest.md)

## 9. Нотатки з безпеки

- Починайте з testnet і dry-run.
- Не вмикайте withdrawals для trading API keys.
- Перед mainnet rollout перевіряйте risk limits.
- Не публікуйте runtime-state, архіви даних та internal evidence.
