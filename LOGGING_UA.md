# Гід з Логування (UA)

Оновлено: 2026-02-28

Документ відображає фактичну поведінку логування приватного `BinaceBot`.

## 1. Топологія логерів

У `src/logging_config.py` налаштовані:

- `app`
- `trade`
- `performance`
- `metrics`
- `portfolio`
- `illiquid_health`
- `decision_matrix`
- `circuit_breaker`
- `data_manager`
- `api`

Watchdog пише окремо через `scripts/monitoring/watchdog_monitor.py`.

## 2. Структура директорій

```text
logs/
  mainnet/
    <hostname>/
      activity.log
      trades.log
      performance.log
      metrics.log
  testnet/
    <hostname>/
      activity.log
      trades.log
      performance.log
      metrics.log
  watchdog.log
```

Підкаталог `<hostname>` потрібен для уникнення конфліктів між інстансами на різних хостах.

## 3. Політика ротації

- Тип: size-based (`RotatingFileHandler`)
- Розмір файлу: `10 MB`
- Backup count: `30`
- Компресія: вимкнена за замовчуванням

## 4. Призначення файлів

- `activity.log`: системні події, lifecycle, runtime.
- `trades.log`: тільки торговий стрім (`trade` logger).
- `performance.log`: форматовані performance-репорти.
- `metrics.log`: збереження метрик і лічильників.
- `watchdog.log`: події watchdog і remote control.

## 5. Корисні поля в логах

- `operation`
- `symbol`
- `stage`
- `reason_code`
- `iteration`
- `recovery_action`
- `risk_manager_mode`
- feature-поля (`feature_*`)

## 6. Безпека

- Не логувати сирі API ключі/секрети.
- Використовувати sanitizer для чутливих даних.
- Не скидати повні payload зовнішніх API в ERROR.

## 7. Операційні команди

```bash
tail -f logs/testnet/$(hostname)/activity.log
tail -f logs/testnet/$(hostname)/trades.log
tail -f logs/watchdog.log
rg "risk_manager|reason_code|decision summary" logs/testnet/$(hostname)/activity.log
```

## 8. Типові помилки

- Ігнорувати `<hostname>` у шляхах.
- Очікувати time-based ротацію (у нас size-based).
- Змішувати діагностику watchdog і main bot без розділення контексту.
