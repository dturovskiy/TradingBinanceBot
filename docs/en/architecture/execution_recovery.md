# Durable Execution State and Recovery (EN)

## 1. Purpose

Trading systems can observe externally executed state while also maintaining local managed state. Durable execution state provides a restart-safe contract for resolving that boundary.

## 2. External and Local State

Exchange state and local managed state are distinct sources of information. A process restart, ambiguous response, or partial local update can require reconciliation before normal operation resumes.

The exchange is authoritative for what it observed and executed, while local managed state carries accounting, risk, and lifecycle context. An in-memory response alone is not sufficient proof that both views agree; durable state retains enough intent/result context to support later reconciliation without treating a retry as a new trading decision.

## 3. Reconciliation Before Readiness

Required unresolved execution state is reconciled before the normal trading readiness gate opens. If required consistency cannot be established, the system fails closed rather than assuming safe state.

Unknown, conflicting, incomplete, or temporarily unavailable reconciliation evidence remains unresolved and keeps the affected readiness path closed.

## 4. Idempotent Restart Recovery

Recovery should be deterministic and idempotent: repeating the same recovery work over the same durable evidence must not duplicate state application or create fresh trading actions.

## 5. Recovery Is Not Order Placement

Recovery may inspect and reconcile existing execution state, but it does not itself authorize new order placement. Fresh trading remains behind the normal execution and readiness contracts.

## 6. Testing Expectations

Public testing expectations include restart/recovery tests, persistence and atomic-write tests, ambiguity/failure-path tests, idempotency checks, reconciliation/readiness tests, and tests proving that recovery does not submit fresh orders. They should explicitly cover externally observed/local-state disagreement, incomplete or unavailable reconciliation evidence, and persistence failures.

## 7. Public-Safety Boundary

Public documentation intentionally omits exact storage paths, journal formats, write ordering, crash windows, operational incident details, live reconciliation mechanics, and exact recovery commands.

## 8. Related Guides

- [Project Map](project_map.md)
- [Testing](../testing/testing_guide.md)
