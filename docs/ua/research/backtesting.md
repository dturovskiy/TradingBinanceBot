# Гайд Research і Backtesting (UA)

## 1. Призначення

Історичний research використовує ту саму торгову семантику, що й runtime,
але data ingestion і live execution залишаються розділеними.

## 2. Розподіл Відповідальності

| Layer | Відповідальність |
| --- | --- |
| Companion data-ingestion workflow | Завантажує публічні OHLCV-дані та записує нормалізовані файли |
| Локальний archive root | Зберігає відтворювані історичні inputs |
| Offline research tools | Replay, evaluation, ranking, sweeps і evidence artifacts |
| Live runtime | Виконує testnet/mainnet операції незалежно від archive refresh |

Data-ingestion workflow не є частиною live trading loop і не приймає торгових рішень.

## 3. Канонічний Archive Contract

```text
<archive-root>/
  klines_15m/<SYMBOL>_15m.csv
  klines_1h/<SYMBOL>_1h.csv
  klines_4h/<SYMBOL>_4h.csv
  summary_metrics.csv
```

Очікувані OHLCV-поля включають timestamps, open, high, low, close і volume.

## 4. Operator Workflow

1. Оновити локальний archive через companion ingestion workflow.
2. Запустити вузький replay smoke check із archive root.
3. Запустити enabled-universe same-core evaluation.
4. Побудувати ranking і focused symbol/candidate sweeps.
5. Порівняти baseline та candidate artifacts.
6. Зафіксувати evidence-based verdict.
7. Просувати зміни лише через testnet, shadow і live gates.

У публічній документації використовуйте placeholders:

```bash
python tools/analysis/<research-tool>.py --archive-root <archive-root>
```

## 5. Правило Відтворюваності

Будь-який прогін, що впливає на strategy або rollout decision, має використовувати
локальний archive root, а не ad-hoc network fetch. Вузькі public-fetch перевірки
допустимі лише для smoke validation або тимчасового debug.

## 6. Правило Артефактів

Generated research outputs належать до:

```text
data/out/<domain>/
```

Не комітьте generated archives, reports, rankings і workstation-specific paths
до цього публічного документаційного репозиторію.

## 7. Правило Interface

Локальний UI або TUI може оркеструвати archive refresh, research runs,
перегляд artifacts і candidate promotion. Він має залишатися thin wrapper
і не реалізовувати другу trading/backtesting систему.
