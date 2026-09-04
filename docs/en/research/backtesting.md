# Research and Backtesting Methodology (EN)

## 1. Purpose

Research and replay should produce reproducible, time-safe evidence without becoming a second uncontrolled trading implementation.

## 2. Event-Time Semantics

Decisions operate on explicitly defined event time. Data that was not available at decision time must not influence that decision.

## 3. Deterministic Replay

The same inputs, contract versions, and deterministic configuration should produce reproducible replay outputs.

## 4. No-Future-Leakage

Decision-time inputs are separated from later observation/outcome data. Future outcomes must not leak into earlier feature construction, ranking, or decisions.

## 5. Live / Replay Parity

Shared semantics should be reused where appropriate. Adapters may stay isolated, but replay must not silently bypass material live-domain execution, risk, or validation contracts.

## 6. Dataset Identity and Provenance

Source provenance, decision provenance, and outcome provenance are distinct concepts. Deterministic identities/content binding reduce accidental dataset or evidence mixing.

## 7. Independent-Sample Semantics

Rows, horizons, or repeated observations are not automatically independent samples. Independence must follow an explicit methodology appropriate to the evidence.

## 8. Time-Safe Split Methodology

Use explicit train/review/holdout boundaries. Apply purge/embargo where required to prevent boundary leakage. A one-shot holdout is not a tuning surface.

## 9. Promotion Firewall

Research evidence alone does not authorize rollout. Separate dataset-integrity, execution/domain-parity, and other required validation layers can block promotion.

## 10. Public-Safety Boundary

Do not publish current candidate names, current strategy results, private dataset hashes, current gate PASS/FAIL state, or operational rollout state.

## 11. Related Guides

- [Evidence Contracts](evidence_contracts.md)
- [Testing](../testing/testing_guide.md)
