# Logging Guide (EN)

Updated: 2026-02-28

This guide reflects the current logging behavior of private `BinaceBot` runtime.

## 1. Logger Topology

Configured in `src/logging_config.py`:

- `app`
- `trade`
- `performance`
- `metrics`
- `portfolio`
- `illiquid_health`
- `decision_matrix`
- `circuit_breaker`
- `data_manager`
- `api`

Watchdog uses dedicated logger in `scripts/monitoring/watchdog_monitor.py`.

## 2. Log Directory Layout

Main bot logs are host-scoped:

```text
logs/
  mainnet/
    <hostname>/
      activity.log
      trades.log
      performance.log
      metrics.log
  testnet/
    <hostname>/
      activity.log
      trades.log
      performance.log
      metrics.log
  watchdog.log
```

Reason for hostname partition:
- avoids conflicts when multiple hosts write to shared storage.

## 3. Rotation Policy

Configured with `RotatingFileHandler`:

- Max file size: `10 MB`
- Backup count: `30`
- Compression: not enabled by default
- Rotation type: size-based

## 4. Content Responsibility by File

- `activity.log`: app/runtime/lifecycle/general events.
- `trades.log`: trade-only stream (`trade` logger filtered).
- `performance.log`: formatted performance summaries.
- `metrics.log`: metrics persistence and counters.
- `watchdog.log`: watchdog heartbeat/control events.

## 5. Operational Fields to Keep in Logs

Recommended structured context (where available):

- `operation`
- `symbol`
- `stage`
- `reason_code`
- `iteration`
- `recovery_action`
- `risk_manager_mode`
- feature flags (`feature_*`)

## 6. Security and Privacy Rules

- Never log raw API keys/secrets.
- Keep sanitizer active for sensitive payloads.
- Avoid dumping full external responses in ERROR paths.
- Use contextual IDs/reason codes instead of secrets.

## 7. Useful Commands

Tail current testnet activity for current host:

```bash
tail -f logs/testnet/$(hostname)/activity.log
```

Tail trade stream:

```bash
tail -f logs/testnet/$(hostname)/trades.log
```

Watchdog logs:

```bash
tail -f logs/watchdog.log
```

Find risk decisions:

```bash
rg "risk_manager|reason_code|decision summary" logs/testnet/$(hostname)/activity.log
```

## 8. Common Pitfalls

- Reading old paths without `<hostname>` subdirectory.
- Assuming daily rotation (it is size-based).
- Mixing watchdog and main-bot events when debugging process control.
