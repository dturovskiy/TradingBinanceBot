# Research and Backtesting Guide (EN)

## 1. Purpose

Historical research uses the same trading semantics as the runtime while keeping
data ingestion and live execution separated.

## 2. Responsibility Split

| Layer | Responsibility |
| --- | --- |
| Data-ingestion companion workflow | Fetch historical public OHLCV data and write normalized files |
| Local archive root | Store repeatable historical inputs |
| Offline research tools | Replay, evaluate, rank, sweep, and produce evidence |
| Live runtime | Execute testnet/mainnet operations independently of archive refresh |

The data-ingestion workflow is not part of the live trading loop and must not
make trading decisions.

## 3. Canonical Archive Contract

```text
<archive-root>/
  klines_15m/<SYMBOL>_15m.csv
  klines_1h/<SYMBOL>_1h.csv
  klines_4h/<SYMBOL>_4h.csv
  summary_metrics.csv
```

Expected OHLCV-style fields include timestamps, open, high, low, close, and volume.

## 4. Operator Workflow

1. Refresh a local archive using the companion ingestion workflow.
2. Run a narrow replay smoke check against the archive root.
3. Run enabled-universe same-core evaluation.
4. Produce ranking and focused symbol/candidate sweeps.
5. Compare baseline and candidate artifacts.
6. Record an evidence-based verdict.
7. Promote only through testnet, shadow, and live gates.

Use placeholders in public docs:

```bash
python tools/analysis/<research-tool>.py --archive-root <archive-root>
```

## 5. Reproducibility Rule

Any run that influences a strategy or rollout decision should use a local archive
root rather than an ad-hoc network fetch. Narrow public-fetch checks are acceptable
only for smoke validation or temporary debugging.

## 6. Artifact Rule

Generated research outputs belong under:

```text
data/out/<domain>/
```

Do not commit generated archives, reports, rankings, or workstation-specific paths
to this public documentation repository.

## 7. Interface Rule

A local UI or TUI may orchestrate archive refresh, research runs, artifact viewing,
and candidate promotion. It must remain a thin wrapper and must not implement a
second trading or backtesting engine.
