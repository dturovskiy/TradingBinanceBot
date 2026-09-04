# Research and Backtesting Methodology (EN)

## 1. Purpose

Research and replay should produce reproducible, time-safe evidence without becoming a second uncontrolled trading implementation.

## 2. Event-Time Semantics

Decisions operate on explicitly defined event time. Data that was not available at decision time must not influence that decision. Observation time, decision time, and outcome time can represent different concepts and must not be silently collapsed into one timestamp.

## 3. Deterministic Replay

The same inputs, contract versions, and deterministic configuration should produce reproducible replay outputs.

## 4. No-Future-Leakage

Decision-time inputs are separated from later observation/outcome data. Future outcomes must not leak into earlier feature construction, ranking, or decisions.

## 5. Live / Replay Parity

Shared semantics should be reused where appropriate. Adapters may stay isolated, but replay must not silently bypass material live-domain execution, risk, or validation contracts. Parity does not require identical environments; differences must be explicit and validated rather than accidental.

## 6. Dataset Identity and Provenance

Source provenance, decision provenance, and outcome provenance are distinct concepts. Deterministic identities/content binding reduce accidental dataset or evidence mixing.

## 7. Independent-Sample Semantics

Rows, horizons, or repeated observations are not automatically independent samples. Duplicate rows, overlapping horizons, or multiple representations of the same underlying event can represent correlated or aliased evidence rather than independent support. Independence must follow an explicit methodology appropriate to the evidence.

## 8. Time-Safe Split Methodology

Use explicit train/review/holdout boundaries. Apply purge/embargo where required to prevent boundary leakage. A one-shot holdout is not a tuning surface.

## 9. Scanner Isolation and Promotion Firewall

Research/scanner execution is isolated from order placement. Scanner work operates behind a no-order boundary, is conceptually bounded, and must isolate failures rather than allowing a research failure to become a trading action.

Scanner output is evidence/input, not promotion authorization. Research evidence alone does not authorize rollout; separate dataset-integrity, execution/domain-parity, and other required validation layers can block promotion. Missing, invalid, or insufficient required evidence fails closed rather than silently promoting a result.

## 10. Public-Safety Boundary

Do not publish current candidate names, current strategy results, private dataset hashes, current gate PASS/FAIL state, or operational rollout state. Generated research outputs belong in managed implementation artifact space rather than this public documentation repository.

## 11. Related Guides

- [Evidence Contracts](evidence_contracts.md)
- [Microstructure Research](microstructure.md)
- [Options / Dataset Builds](options_data.md)
- [Data-Source Contracts](data_sources.md)
- [Testing](../testing/testing_guide.md)
