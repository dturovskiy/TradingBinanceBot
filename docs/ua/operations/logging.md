# Гайд з Логування та Артефактів (UA)

Оновлено: 2026-05-30

## 1. Призначення

Logs, mutable runtime state, metrics state і generated offline outputs мають
різні ownership rules. Під час експлуатації та debug тримайте їх окремо.

## 2. Runtime Log Layout

```text
logs/
  mainnet/<hostname>/
    activity.log
    trades.log
    performance.log
    metrics.log
  testnet/<hostname>/
    activity.log
    trades.log
    performance.log
    metrics.log
  watchdog.log
  bot_launcher.log
```

Hostname partitioning запобігає конфліктам, коли кілька машин пишуть у shared storage.

## 3. State і Metrics

```text
data/<env>/          # mutable runtime state
data/metrics/<env>/  # mutable telemetry, health і error counters
```

Ці шляхи є operational state, а не документацією.

## 4. Generated Offline Outputs

```text
data/out/audit/
data/out/benchmark/
data/out/integration/
data/out/readiness/
data/out/reporting/
data/out/testing/
```

Generated outputs за замовчуванням не слід зберігати у `docs/` або tooling source directories.

## 5. Корисні Команди

```bash
tail -f logs/testnet/$(hostname)/activity.log
tail -f logs/testnet/$(hostname)/trades.log
tail -f logs/watchdog.log
tail -f logs/bot_launcher.log
```

## 6. Правила Безпеки

- Не логуйте raw API keys, secrets, tokens або chat identifiers.
- Тримайте sanitization активним для зовнішніх payloads.
- Використовуйте reason codes і contextual IDs замість sensitive responses.
- Не публікуйте production logs або generated runtime data у docs-репозиторії.

## 7. Типові Помилки

- Читання legacy log paths без `<hostname>`.
- Змішування root control logs і env/host runtime logs.
- Сприйняття generated reports як canonical documentation.
- Коміт локальних research archives або generated outputs.
