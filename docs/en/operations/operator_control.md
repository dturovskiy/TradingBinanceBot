# Operator Control Contracts (EN)

## 1. Purpose
<!-- parity-key: operator.scope -->

The runtime has operator-facing notification and control surfaces, including messaging/panel-style interaction. This page documents stable public-safe control contracts rather than private command syntax or current operational state.

## 2. Authorization Boundary
<!-- parity-key: operator.auth -->

Operator actions are subject to access-control and authorization checks. Possession of a command name or message transport does not itself grant authority, and public documentation must not expose credentials, chat identifiers, allowlists, or private authorization configuration.

## 3. Notifications and Panels
<!-- parity-key: operator.notifications -->

Notifications and status/panel surfaces can present observations, health, or workflow context to an authorized operator. Displaying or acknowledging information is distinct from mutating trading state.

## 4. Command Classes
<!-- parity-key: operator.command-classes -->

At a public contract level, operator controls can cover observation/status, lifecycle or configuration workflows, notifications/panels, and explicitly authorized control actions. Exact privileged command strings, recovery procedures, and production parameters remain private.

## 5. Control Does Not Bypass Safety Gates
<!-- parity-key: operator.non-authority -->

An operator-control surface does not silently bypass risk, readiness, recovery, evidence, or promotion gates. Research evidence is not converted into rollout authority merely because it is visible through an operator interface.

## 6. Public-Safety Boundary
<!-- parity-key: operator.public-boundary -->

Do not publish chat IDs, access-control lists, tokens, exact privileged or recovery commands, current runtime state, incident procedures, current positions/trades, infrastructure identifiers, or production thresholds.

## 7. Related Guides

- [Reliability](reliability.md)
- [Logging and Artifacts](logging.md)
- [Project Map](../architecture/project_map.md)
