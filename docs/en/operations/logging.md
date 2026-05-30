# Logging and Artifact Guide (EN)

Updated: 2026-05-30

## 1. Purpose

Logs, mutable runtime state, metrics state, and generated offline outputs have
different ownership rules. Keep them separated during operation and debugging.

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

Hostname partitioning avoids collisions when more than one machine writes to
shared storage.

## 3. State and Metrics

```text
data/<env>/          # mutable runtime state
data/metrics/<env>/  # mutable telemetry, health, and error counters
```

Treat these paths as operational state, not documentation.

## 4. Generated Offline Outputs

```text
data/out/audit/
data/out/benchmark/
data/out/integration/
data/out/readiness/
data/out/reporting/
data/out/testing/
```

Generated outputs should not be stored under `docs/` or tooling source directories
by default.

## 5. Useful Commands

```bash
tail -f logs/testnet/$(hostname)/activity.log
tail -f logs/testnet/$(hostname)/trades.log
tail -f logs/watchdog.log
tail -f logs/bot_launcher.log
```

## 6. Security Rules

- Never log raw API keys, secrets, tokens, or chat identifiers.
- Keep sanitization active for external payloads.
- Prefer reason codes and contextual IDs over raw sensitive responses.
- Do not publish production logs or generated runtime data in this docs repository.

## 7. Common Pitfalls

- Reading legacy log paths without the `<hostname>` segment.
- Mixing root control logs with env/host runtime logs.
- Treating generated reports as canonical documentation.
- Committing local research archives or generated outputs.
