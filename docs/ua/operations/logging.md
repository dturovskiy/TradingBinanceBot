# Гайд з Логування та Артефактів (UA)

Оновлено: 2026-09-04

## 1. Призначення

Логи, structured telemetry, mutable runtime state, metrics state і generated offline outputs є різними observability/artifact surfaces з окремими правилами ownership. Звичайні логи — лише одна частина моделі observability.

## 2. Семантика Structured Telemetry

Structured telemetry фіксує машинозчитувані події та спостереження для подальшого аналізу й валідації. На public-safe contract-рівні до recorder families належать decision-, path-, shadow- і scanner-style observations; ця документація не розкриває їхні внутрішні схеми, поточний стан увімкнення або записаний вміст.

Запис або спостереження стану не є поверхнею авторизації торгівлі. Збір telemetry сам по собі не повинен створювати ордери, просувати research results або змінювати trading state.

## 3. Activation, Freshness і Provenance

Доступність telemetry інтерпретується через явні activation/profile та provenance semantics, а не лише за фактом наявності файла. Джерело може бути enabled, disabled, unavailable, stale або коректно idle; expected-idle і stale data — різні стани.

Якщо telemetry contract вимагає configuration або provenance binding, відсутній чи некоректний binding не повинен вважатися valid/current evidence. Така перевірка є fail-closed для інтерпретації telemetry і не перетворює observation на зміну trading state.

## 4. Runtime Log Layout

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

## 5. State і Metrics

```text
data/<env>/          # mutable runtime state
data/metrics/<env>/  # mutable telemetry, health і error counters
```

Ці вже публічні шляхи описують стабільні класи ownership. Structured event telemetry може мати додаткове implementation-owned storage; точні приватні recorder paths і runtime contents навмисно не документуються тут.

## 6. Generated Offline Outputs

```text
data/out/audit/
data/out/benchmark/
data/out/integration/
data/out/readiness/
data/out/reporting/
data/out/testing/
```

Generated outputs за замовчуванням не слід зберігати у `docs/` або tooling source directories.

## 7. Корисні Команди

```bash
tail -f logs/testnet/$(hostname)/activity.log
tail -f logs/testnet/$(hostname)/trades.log
tail -f logs/watchdog.log
tail -f logs/bot_launcher.log
```

## 8. Правила Безпеки та Public-Safety

- Не логуйте raw API keys, secrets, tokens або chat identifiers.
- Тримайте sanitization активним для зовнішніх payloads.
- Використовуйте reason codes і contextual IDs замість raw sensitive responses.
- Не публікуйте production logs, structured telemetry contents, поточний recorder state, private hashes, incident data або generated runtime data у цьому documentation repository.
- Не робіть висновків про поточний operational health чи trading state з прикладів у public documentation.

## 9. Типові Помилки

- Сприйняття звичайних логів як повної моделі observability.
- Сприйняття відсутності fresh telemetry як помилки без урахування expected-idle semantics.
- Сприйняття recorder observation як дії або promotion authorization.
- Читання legacy log paths без `<hostname>`.
- Змішування root control logs і env/host runtime logs.
- Сприйняття generated reports як canonical documentation.
- Коміт локальних research archives або generated outputs.

## 10. Пов'язані Гайди

- [Project Map](../architecture/project_map.md)
- [Research / Backtesting](../research/backtesting.md)
- [Evidence Contracts](../research/evidence_contracts.md)
- [Testing](../testing/testing_guide.md)
