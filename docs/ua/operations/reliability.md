# Контракти надійності та обробки відмов (UA)

## 1. Призначення
<!-- parity-key: reliability.scope -->

Надійність є окремим runtime-доменом, а не частиною торгової логіки. Публічна документація описує bounded failure handling, безпечне спостереження, межі recovery та secret-safe діагностику без розкриття приватної інфраструктури чи поточного стану інцидентів.

## 2. Обмежена обробка відмов
<!-- parity-key: reliability.bounded-failure -->

Відмови зовнішніх і network-facing залежностей мають оброблятися з обмеженим обсягом роботи. Timeouts, retries та recovery attempts не повинні перетворюватися на необмежені control loops, а невирішені залежності можуть блокувати подальший рух, якщо їхній контракт потрібен для readiness або безпечного execution.

## 3. Secret-Safe діагностика
<!-- parity-key: reliability.secret-safe -->

Повідомлення про відмови мають зберігати корисні reason/context дані й водночас санітизувати credentials, tokens, чутливі зовнішні payloads та інші операційні секрети. Діагностика не повинна послаблювати public/private boundary.

## 4. Семантика інцидентів і відновлення
<!-- parity-key: reliability.incident-normalization -->

Відмови слід нормалізувати в явні reason/state semantics, щоб спостереження, containment і recovery мали узгоджене трактування. Incident handling і recovery відокремлені від дозволу на розміщення нового ордера або promotion результату дослідження.

## 5. Fail-Safe межі
<!-- parity-key: reliability.fail-safe -->

Якщо обов'язковий state, provenance або зовнішня залежність залишаються неоднозначними, безпечний контракт — локалізувати відмову або завершити перевірку за принципом fail-closed, а не продовжувати з припущенням про валідний стан. Спостереження за відмовою саме по собі не змінює trading state.

## 6. Межа публічної безпеки
<!-- parity-key: reliability.public-boundary -->

Не публікуйте resolver/DNS details, host configuration, mount/storage topology, process IDs, incident counts, поточний outage/recovery state, точні retry budgets, точні operator recovery commands або чутливий вміст logs/telemetry.

## 7. Пов'язані матеріали

- [Логування та артефакти](logging.md)
- [Виконання / відновлення](../architecture/execution_recovery.md)
- [Тестування](../testing/testing_guide.md)
