# Public Module-Family Reference (EN)

## 1. Purpose
<!-- parity-key: modules.scope -->

This reference gives a deeper public-safe view of ownership families without mirroring the private source tree, class names, function signatures, or implementation sequencing.

## 2. Runtime Module Families
<!-- parity-key: modules.runtime -->

| Family | Public-safe responsibility |
| --- | --- |
| Bootstrap / lifecycle | Initialization, shutdown, readiness coordination |
| Execution / recovery (`src/execution/`) | Durable execution state, reconciliation, restart recovery |
| Exchange / API | External exchange reads and order-facing transport/adapters |
| Risk (`src/risk/`) | Layered/grouped risk policy, reason/model semantics, fail-safe containment |
| Observability / telemetry | Logs, metrics, structured event/recorder observations, provenance/freshness interpretation |
| Operator control | Authorized notifications, status/panel surfaces, controlled operator workflows |
| Persistence / configuration | State/configuration ownership and durable artifact boundaries |

## 3. Research Module Families
<!-- parity-key: modules.research -->

| Family | Public-safe responsibility |
| --- | --- |
| Backtesting / replay (`src/backtesting/`) | Event-time replay, execution realism, live/replay parity methodology |
| Research / evidence | Dataset identity, provenance, scanner isolation, evidence aggregation, promotion contracts |
| Microstructure research | Spread/depth/executable-price methodology separated from order execution |
| Offline dataset workflows | Preregistered, reproducible, bounded data-build and acceptance methodology |

## 4. Cross-Family Boundaries
<!-- parity-key: modules.boundaries -->

Durable execution-state ownership is distinct from exchange transport; observability does not authorize trading; research/scanner work has a no-order boundary; evidence does not equal promotion authorization; and adapters must not silently bypass material risk, timing, state, or validation contracts.

## 5. Public-Safety Boundary
<!-- parity-key: modules.public-boundary -->

Do not treat this page as a full private tree. It intentionally omits private module/file inventories, internal class/function names, implementation source, current strategies, production configuration, runtime topology, current state, and operational recovery procedures.

## 6. Related Guides

- [Project Map](project_map.md)
- [Execution / Recovery](execution_recovery.md)
- [Reliability](../operations/reliability.md)
- [Research / Backtesting](../research/backtesting.md)
