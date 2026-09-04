# Публічний довідник сімейств модулів (UA)

## 1. Призначення
<!-- parity-key: modules.scope -->

Цей довідник дає глибший public-safe огляд сімейств ownership без дзеркалювання приватного source tree, назв класів, сигнатур функцій або послідовності implementation.

## 2. Runtime-сімейства модулів
<!-- parity-key: modules.runtime -->

| Сімейство | Public-safe відповідальність |
| --- | --- |
| Bootstrap / lifecycle | Ініціалізація, завершення роботи, координація readiness |
| Execution / recovery (`src/execution/`) | Durable execution state, reconciliation, restart recovery |
| Exchange / API | Зовнішні exchange reads і order-facing transport/adapters |
| Risk (`src/risk/`) | Layered/grouped risk policy, reason/model semantics, fail-safe containment |
| Observability / telemetry | Logs, metrics, structured event/recorder observations, інтерпретація provenance/freshness |
| Operator control | Авторизовані notifications, status/panel surfaces і контрольовані operator workflows |
| Persistence / configuration | Ownership стану/конфігурації та межі durable artifacts |

## 3. Research-сімейства модулів
<!-- parity-key: modules.research -->

| Сімейство | Public-safe відповідальність |
| --- | --- |
| Backtesting / replay (`src/backtesting/`) | Event-time replay, execution realism, методологія live/replay parity |
| Research / evidence | Dataset identity, provenance, scanner isolation, evidence aggregation, promotion contracts |
| Microstructure research | Методологія spread/depth/executable-price, відокремлена від order execution |
| Offline dataset workflows | Preregistered, відтворювана, bounded методологія data-build і acceptance |

## 4. Межі між сімействами
<!-- parity-key: modules.boundaries -->

Ownership durable execution state відокремлений від exchange transport; observability не надає дозволу на trading; research/scanner work має no-order boundary; evidence не дорівнює promotion authorization; adapters не повинні непомітно обходити суттєві risk, timing, state або validation contracts.

## 5. Межа публічної безпеки
<!-- parity-key: modules.public-boundary -->

Не сприймайте цю сторінку як повне приватне дерево. Вона навмисно не містить private module/file inventories, внутрішніх class/function names, implementation source, поточних strategies, production configuration, runtime topology, current state або operational recovery procedures.

## 6. Пов'язані матеріали

- [Карта проєкту](project_map.md)
- [Виконання / відновлення](execution_recovery.md)
- [Надійність](../operations/reliability.md)
- [Дослідження / бектестинг](../research/backtesting.md)
