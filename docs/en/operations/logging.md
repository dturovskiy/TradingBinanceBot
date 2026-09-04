# Logging and Artifact Guide (EN)

Updated: 2026-09-04

## 1. Purpose

Logs, structured telemetry, mutable runtime state, metrics state, and generated offline outputs are distinct observability/artifact surfaces with different ownership rules. Ordinary logs are only one part of the observability model.

## 2. Structured Telemetry Semantics

Structured telemetry records machine-readable events and observations for later inspection and validation. Public-safe recorder families include decision-, path-, shadow-, and scanner-style observations at the contract level; this documentation does not expose their internal schemas, current enablement, or recorded contents.

Recording or observing state is not a trading authorization surface. Telemetry collection must not, by itself, create orders, promote research results, or mutate trading state.

## 3. Activation, Freshness, and Provenance

Telemetry availability is interpreted through explicit activation/profile and provenance semantics rather than inferred from a file's presence alone. A source can be enabled, disabled, unavailable, stale, or legitimately idle; expected-idle and stale data are different states.

Where a telemetry contract requires configuration or provenance binding, missing or invalid binding must not be treated as valid/current evidence. Such validation is fail-closed for telemetry interpretation without turning observation into a trading-state mutation.

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

Hostname partitioning avoids collisions when more than one machine writes to shared storage.

## 5. State and Metrics

```text
data/<env>/          # mutable runtime state
data/metrics/<env>/  # mutable telemetry, health, and error counters
```

These already-public paths describe stable ownership classes. Structured event telemetry can have additional implementation-owned storage; exact private recorder paths and runtime contents are intentionally not documented here.

## 6. Generated Offline Outputs

```text
data/out/audit/
data/out/benchmark/
data/out/integration/
data/out/readiness/
data/out/reporting/
data/out/testing/
```

Generated outputs should not be stored under `docs/` or tooling source directories by default.

## 7. Useful Commands

```bash
tail -f logs/testnet/$(hostname)/activity.log
tail -f logs/testnet/$(hostname)/trades.log
tail -f logs/watchdog.log
tail -f logs/bot_launcher.log
```

## 8. Security and Public-Safety Rules

- Never log raw API keys, secrets, tokens, or chat identifiers.
- Keep sanitization active for external payloads.
- Prefer reason codes and contextual IDs over raw sensitive responses.
- Do not publish production logs, structured telemetry contents, current recorder state, private hashes, incident data, or generated runtime data in this documentation repository.
- Do not infer current operational health or trading state from public documentation examples.

## 9. Common Pitfalls

- Treating ordinary logs as the complete observability model.
- Treating absence of fresh telemetry as equivalent to a fault without accounting for expected-idle semantics.
- Treating a recorder observation as an action or promotion authorization.
- Reading legacy log paths without the `<hostname>` segment.
- Mixing root control logs with env/host runtime logs.
- Treating generated reports as canonical documentation.
- Committing local research archives or generated outputs.

## 10. Related Guides

- [Reliability](reliability.md)
- [Operator Control](operator_control.md)
- [Project Map](../architecture/project_map.md)
- [Research / Backtesting](../research/backtesting.md)
- [Evidence Contracts](../research/evidence_contracts.md)
- [Testing](../testing/testing_guide.md)
