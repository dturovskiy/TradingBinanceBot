# Glossary

- `TradingBinanceBot`: public documentation-only repository.
- `Durable State`: locally persisted execution state intended to survive process restart.
- `Reconciliation`: comparison and resolution of externally observed exchange state with locally managed state.
- `Restart Recovery`: deterministic process for resolving durable execution state before normal readiness.
- `Idempotency`: property that allows a recovery or state-application step to be repeated without duplicating its effect.
- `Readiness Gate`: condition that must be satisfied before normal trading activity resumes.
- `Fail Closed`: block progression when required state or evidence remains unresolved.
- `Event Time`: explicitly defined time associated with an observation/decision in replay or research.
- `Deterministic Replay`: reproducible replay for the same inputs and contract versions.
- `No-Future-Leakage`: rule preventing future observations/outcomes from influencing past decisions.
- `Dataset Identity`: deterministic identity binding a dataset to its intended contents/provenance.
- `Provenance`: metadata describing the origin and role of data or evidence.
- `Content-Bound Evidence`: evidence whose identity is deterministically tied to its contents.
- `Independent Sample`: an observation counted as statistically independent under an explicit methodology rather than merely because it occupies a separate row.
- `Purge / Embargo`: time-safety techniques used to reduce leakage across train/review/holdout boundaries.
- `One-Shot Holdout`: holdout semantics intended to prevent repeated tuning against the final evaluation set.
- `Promotion Firewall`: separation between research evidence and authorization to advance toward deployment.
- `Execution/Domain Parity`: validation that replay/research does not silently bypass material execution-domain contracts.
