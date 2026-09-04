# Дослідження мікроструктури та якості виконання (UA)

## 1. Призначення
<!-- parity-key: microstructure.scope -->

Дослідження мікроструктури оцінює execution-quality evidence, не перетворюючи збір даних на surface для order placement. Публічний контракт описує методологію, а не активну strategy logic чи production calibration.

## 2. Доказова база стану ринку
<!-- parity-key: microstructure.market-state -->

Spread, depth та пов'язаний order-book context можуть використовуватися як research evidence, якщо їхні event-time і provenance визначені явно. Такі спостереження описують ринкові умови й самі по собі не надають дозволу на trade.

## 3. Реалістичність executable price
<!-- parity-key: microstructure.executable-price -->

Коли важлива execution realism, дослідження має відрізняти executable-price model від спрощених припущень щодо reference price. Методологія може враховувати market-state constraints без публікації поточних fee, slippage, sizing або calibration parameters.

## 4. Telemetry з ізольованою provenance
<!-- parity-key: microstructure.provenance -->

Microstructure observations мають зберігати source, observation-time, decision-time та outcome provenance, щоб evidence не змішувалося непомітно між несумісними контекстами. Відсутній або неоднозначний binding має завершувати використання evidence за принципом fail-closed.

## 5. Відокремлення від execution і promotion
<!-- parity-key: microstructure.separation -->

Збір або аналіз microstructure telemetry відокремлений від order execution і promotion authorization. Сприятлива execution-quality evidence може підтримувати оцінювання, але обов'язкові dataset-integrity, execution/domain-parity та інші promotion gates залишаються незалежними.

## 6. Межа публічної безпеки
<!-- parity-key: microstructure.public-boundary -->

Не публікуйте поточну sampling cadence, recorder enablement, budgets, fee/slippage assumptions, strategy thresholds, candidate rankings, profitability conclusions, live order-book snapshots або operational telemetry contents.

## 7. Пов'язані матеріали

- [Дослідження / бектестинг](backtesting.md)
- [Контракти доказової бази](evidence_contracts.md)
- [Контракти джерел даних](data_sources.md)
