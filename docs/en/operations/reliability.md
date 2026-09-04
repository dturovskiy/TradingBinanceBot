# Reliability and Failure-Handling Contracts (EN)

## 1. Purpose
<!-- parity-key: reliability.scope -->

Reliability is a separate runtime concern from trading logic. Public documentation describes bounded failure handling, safe observation, recovery boundaries, and secret-safe diagnostics without exposing private infrastructure or incident state.

## 2. Bounded Failure Handling
<!-- parity-key: reliability.bounded-failure -->

External and network-facing failures should be handled with bounded work. Timeouts, retries, and recovery attempts must not become unbounded control loops, and unresolved dependencies may block progression when their contract is required for readiness or safe execution.

## 3. Secret-Safe Diagnostics
<!-- parity-key: reliability.secret-safe -->

Failure reporting should preserve useful reason/context information while sanitizing credentials, tokens, sensitive external payloads, and other operational secrets. Diagnostic detail must not weaken the public/private boundary.

## 4. Incident and Recovery Semantics
<!-- parity-key: reliability.incident-normalization -->

Failures should be normalized into explicit reason/state semantics so observation, containment, and recovery can be reasoned about consistently. Incident handling and recovery are distinct from authorization to place a new order or to promote a research result.

## 5. Fail-Safe Boundaries
<!-- parity-key: reliability.fail-safe -->

When required state, provenance, or an external dependency remains ambiguous, the safe contract is to contain the failure or fail closed rather than silently continue with assumed-valid state. Monitoring a fault does not itself mutate trading state.

## 6. Public-Safety Boundary
<!-- parity-key: reliability.public-boundary -->

Do not publish resolver or DNS details, host configuration, mount/storage topology, process IDs, incident counts, current outage/recovery state, exact retry budgets, exact operator recovery commands, or sensitive log/telemetry contents.

## 7. Related Guides

- [Logging and Artifacts](logging.md)
- [Execution / Recovery](../architecture/execution_recovery.md)
- [Testing](../testing/testing_guide.md)
