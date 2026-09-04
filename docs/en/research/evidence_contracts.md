# Evidence and Provenance Contracts (EN)

## 1. Principle

**A research result is not sufficient for promotion.**

## 2. Provenance

Evidence should identify the role and origin of source, decision, and outcome material without conflating them. Provenance should not be inferred only from filenames, timestamps, or local directories.

## 3. Deterministic Artifact Identity

Artifacts should have deterministic identities derived from their intended contract and contents so repeated generation can be compared reliably.

## 4. Content-Bound Evidence

Evidence used for validation should be bound to the content it represents. Mutation or mismatched binding should fail closed rather than silently join.

## 5. Candidate and Dataset Binding

Candidate/configuration identity and dataset identity are conceptually distinct and should be explicitly bound when an evaluation depends on both. If required candidate, dataset, or evidence bindings disagree, aggregation must fail closed rather than produce a blended result with ambiguous provenance.

## 6. Evidence Classes

Measured, synthetic, and counterfactual evidence are different classes. They must not be silently merged as if they carried identical empirical meaning.

## 7. Independent Samples and Aggregation

Aggregation must respect independent-sample semantics. Duplicate or aliased evidence should not inflate sample strength, and ambiguous joins should fail closed.

## 8. Promotion Evidence vs Edge Evidence

Evidence that supports a statistical/market edge is not equivalent to evidence required for promotion. Promotion can require additional integrity, safety, execution, and domain validation.

## 9. Execution / Domain Parity

Execution/domain parity is a separate validation layer intended to catch cases where replay or research bypasses material runtime semantics. It covers execution, timing, risk, and state semantics relevant to the target path; a favorable research result can still be blocked when this layer is missing or inconsistent.

## 10. Public-Safety Boundary

This public contract does not reproduce internal schema fields, current evidence IDs/hashes, candidate names, gate verdicts, or operational evidence.

## 11. Related Guides

- [Research / Backtesting](backtesting.md)
- [Testing](../testing/testing_guide.md)
