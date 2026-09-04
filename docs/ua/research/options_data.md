# Пререгістровані options- та dataset-build дослідження (UA)

## 1. Призначення
<!-- parity-key: options.scope -->

Offline options/data research може використовувати preregistered, відтворювані та bounded dataset-build workflows з явною provenance й acceptance controls. Ця сторінка документує контракт такого workflow без розкриття поточного build state або storage layout.

## 2. Пререгістрація
<!-- parity-key: options.preregistration -->

Перед фінальним переглядом результатів слід визначити запланований dataset scope, evaluation role та acceptance conditions, якщо preregistration є частиною методології. Preregistered holdout або dataset role не є поверхнею для повторного tuning.

## 3. Відтворювані bounded builds
<!-- parity-key: options.dataset-build -->

Побудова dataset має використовувати явну source identity, transformation context і deterministic або reproducible build semantics. Робота має бути концептуально bounded, щоб offline data workflow не перетворювався на неконтрольовану runtime dependency.

## 4. Acceptance controls
<!-- parity-key: options.acceptance -->

Build acceptance відокремлений від evidence of market edge. Обов'язкові перевірки integrity, completeness, provenance та contract можуть відхилити artifact, не перетворюючи саме прийняття чи відхилення на trading authorization.

## 5. Provenance та evidence binding
<!-- parity-key: options.provenance -->

Dataset identity, source provenance, transformation provenance і downstream evidence bindings мають залишатися явними. Відсутні або несумісні обов'язкові bindings завершуються fail-closed, а не непомітним об'єднанням artifacts з різних research contexts.

## 6. Межа публічної безпеки
<!-- parity-key: options.public-boundary -->

Не публікуйте поточні dataset roots, mount/storage topology, build status, поточні acceptance verdicts, private hashes, account/provider credentials, точні budgets, поточних options candidates, active strategy parameters або next operator action.

## 7. Пов'язані матеріали

- [Контракти джерел даних](data_sources.md)
- [Контракти доказової бази](evidence_contracts.md)
- [Дослідження / бектестинг](backtesting.md)
