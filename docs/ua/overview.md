# Документація середовища виконання та досліджень (UA)

## 1. Межі репозиторію

`TradingBinanceBot` документує приватну платформу для торгівлі, виконання та досліджень з окремими доменами виконання, ризику, відновлення, replay, доказової бази, observability, reliability та operator control. Це не дзеркало вихідного коду.

## 2. Структура середовища виконання

Стабільні публічні зони відповідальності розділено між ініціалізацією/життєвим циклом, змінюваним runtime state, оркестрацією торгівлі, durable execution state/recovery, доступом exchange/API, портфельним ризиком, monitoring/observability, reliability, operator control, persistence/configuration, backtesting/replay та research/evidence.

Читайте: [Карта проєкту](architecture/project_map.md) і [Довідник сімейств модулів](architecture/module_reference.md).

## 3. Виконання та відновлення

Стійкий стан виконання може вимагати reconciliation до переходу в нормальний стан готовності до торгівлі. Recovery є детермінованим та ідемпотентним, невирішений стан обробляється за принципом fail-closed, а саме recovery не надає дозволу на розміщення нових ордерів.

Читайте: [Виконання / відновлення](architecture/execution_recovery.md).

## 4. Дослідження та доказова база

Дослідження використовують явну семантику event time, deterministic replay, no-future-leakage rules, dataset/provenance identity, time-safe splits і promotion evidence, яка залишається відокремленою від rollout authorization. Розширена методологія охоплює microstructure/execution-quality evidence, provenance зовнішніх джерел даних і preregistered bounded dataset-build workflows без публікації active strategy або operational data.

Читайте: [Дослідження / бектестинг](research/backtesting.md), [Контракти доказової бази](research/evidence_contracts.md), [Дослідження мікроструктури](research/microstructure.md), [Options / Dataset Builds](research/options_data.md) і [Контракти джерел даних](research/data_sources.md).

## 5. Надійність та операторське керування

Reliability використовує bounded failure handling, secret-safe diagnostics, явні recovery boundaries і fail-safe containment. Operator-facing controls залишаються access-controlled і не можуть непомітно обходити risk, readiness, recovery, evidence або promotion gates.

Читайте: [Надійність](operations/reliability.md), [Операторське керування](operations/operator_control.md) і [Логування та артефакти](operations/logging.md).

## 6. Тестування

Тестування охоплює модульні, інтеграційні, property-based, параметризовані регресійні, контрактні тести, тести persistence/atomic-write, order-state/recovery, failure paths/network resilience, replay/parity, research/provenance, observability, risk/API/execution та валідацію документації.

## 7. Provenance

- Дата перегляду документації: `2026-09-04`.
- Переглянутий commit приватного джерела: `05a4214895111bcdbb7960223b4af232c066c48c`.
- Дата commit приватного джерела: `2026-09-03`.
- Попередня публічна синхронізація: `2026-05-30`.
- Попередній точний SHA приватного джерела: `not recorded`.

## 8. Індекс документації

- [Архітектура](architecture/project_map.md)
- [Довідник сімейств модулів](architecture/module_reference.md)
- [Виконання / відновлення](architecture/execution_recovery.md)
- [Надійність](operations/reliability.md)
- [Операторське керування](operations/operator_control.md)
- [Логування та артефакти](operations/logging.md)
- [Дослідження / бектестинг](research/backtesting.md)
- [Контракти доказової бази](research/evidence_contracts.md)
- [Дослідження мікроструктури](research/microstructure.md)
- [Options / Dataset Builds](research/options_data.md)
- [Контракти джерел даних](research/data_sources.md)
- [Тестування](testing/testing_guide.md)
- [Маніфест публічної синхронізації](../shared/public_sync_manifest.md)

## 9. Межа публічної безпеки

Не публікуйте приватний вихідний код, runtime/trading state, поточні strategies/candidates/rankings, production thresholds, provider credentials/endpoints, infrastructure topology, точні privileged/recovery commands, current recorder/source state, operational hashes або private operational evidence.
