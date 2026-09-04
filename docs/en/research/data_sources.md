# External Data-Source Contracts (EN)

## 1. Purpose
<!-- parity-key: data-sources.scope -->

External research data is accepted through provenance and evidence contracts rather than trusted merely because it came from a known provider or file. This public page defines source-handling methodology; provider-specific operational configuration remains private unless separately reviewed for publication.

## 2. Source Identity and Provenance
<!-- parity-key: data-sources.identity -->

Source identity, acquisition context, dataset role, and downstream evidence role are distinct concepts. A provider label, filename, or timestamp alone is not sufficient provenance for a research artifact.

## 3. Availability and Event Time
<!-- parity-key: data-sources.time -->

Source timestamp, observation/arrival time, decision time, and outcome time can differ. Research must use the time at which information was actually available to the decision process so external data does not introduce future leakage.

## 4. Transformation Binding
<!-- parity-key: data-sources.transform -->

Material transformations should be reproducible and bound to the source/dataset identity they represent. Ambiguous joins, incompatible provenance, or missing required identity should fail closed rather than silently create blended evidence.

## 5. Acceptance and Evidence Use
<!-- parity-key: data-sources.acceptance -->

Data-source acceptance, dataset integrity, and evidence of market edge are separate judgments. A source can be technically acceptable without proving an edge, and favorable research output cannot compensate for missing required provenance or integrity evidence.

## 6. Public-Safety Boundary
<!-- parity-key: data-sources.public-boundary -->

Do not publish provider credentials, private account identifiers, private endpoints, current source availability, exact acquisition cadence or budgets, storage roots, mount topology, current dataset hashes, or operational source-health state. Provider names are not part of this public contract unless independently verified and approved for publication.

## 7. Related Guides

- [Preregistered Options / Data Research](options_data.md)
- [Microstructure Research](microstructure.md)
- [Evidence Contracts](evidence_contracts.md)
