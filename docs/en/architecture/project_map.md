# Project Map (EN)

## 1. Public Documentation Boundary

This map describes stable public-safe ownership domains, not the full private source tree.

## 2. Runtime Ownership Domains

| Domain | Public-safe responsibility |
| --- | --- |
| Bootstrap / lifecycle | Startup, shutdown, initialization, readiness orchestration |
| Mutable runtime state | Coordinated in-memory runtime context |
| Trading orchestration | Iteration sequencing and trading-flow coordination |
| Durable execution state / recovery | Persisted execution intent/state, restart reconciliation, readiness gating |
| Exchange / API | External exchange reads and order-facing adapters |
| Portfolio risk | Layered/grouped portfolio risk policy, reason/model separation, and fail-safe containment |
| Monitoring / observability | Health, metrics, telemetry, reports |
| Operator control | Notifications and operator-facing controls |
| Persistence / config | Runtime persistence and configuration ownership |
| Backtesting / replay | Event-time replay and execution-parity methodology |
| Research / evidence | Dataset identity, provenance, validation and promotion evidence |

## 3. High-Level Runtime Flow

1. Bootstrap and lifecycle initialize required domains.
2. Persisted/mutable state is loaded.
3. Required execution-state reconciliation runs before normal readiness.
4. Normal trading orchestration proceeds only when required state is consistent.
5. Exchange/API, risk, persistence, and observability remain separate ownership domains.

This is ownership and safety ordering, not an exact startup implementation sequence.

Risk ownership is layered: reason/model semantics remain distinct from grouped/portfolio-level coordination so risk concerns can be contained and fail safe without coupling the public contract to production thresholds or current exposure.

## 4. Durable Execution State / Recovery

Order execution is separate from durable state ownership. A restart can require reconciliation between external exchange state and locally managed state. Recovery must be deterministic and idempotent, unresolved state fails closed, and recovery itself does not authorize fresh order placement.

See [Execution / Recovery](execution_recovery.md).

## 5. Research / Replay Boundary

Replay uses explicit event time and should share material domain semantics with live execution where appropriate. Adapters may remain isolated, but replay must not silently bypass important live-domain contracts. Parity does not require identical offline and live environments; differences must be explicit and validated rather than accidental.

See [Research / Backtesting](../research/backtesting.md).

Stable artifact/configuration concepts include human-maintained documentation, mutable runtime or telemetry state, operational logs, generated offline research/testing outputs, and tracked reference artifacts when they are part of a stable developer contract. Generated outputs do not become canonical documentation by location or convenience.

## 6. Public-Safety Limits

This page does not publish exact journal names/formats, write ordering, crash windows, recovery commands, live reconciliation procedures, production thresholds, current operational state, or private topology.

## 7. Related Guides

- [Execution / Recovery](execution_recovery.md)
- [Research / Backtesting](../research/backtesting.md)
- [Evidence Contracts](../research/evidence_contracts.md)
- [Testing](../testing/testing_guide.md)
- [Logging and Artifacts](../operations/logging.md)
