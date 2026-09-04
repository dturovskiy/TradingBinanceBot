# Contrats de sources de données externes (FR)

## 1. Objectif
<!-- parity-key: data-sources.scope -->

Les données externes de recherche sont acceptées via des contrats de provenance et d'evidence plutôt que considérées fiables uniquement parce qu'elles proviennent d'un provider connu ou d'un fichier donné. Cette page publique définit la méthodologie de gestion des sources ; la configuration opérationnelle propre aux providers reste privée sauf revue distincte pour publication.

## 2. Identité de la source et provenance
<!-- parity-key: data-sources.identity -->

La source identity, l'acquisition context, le dataset role et le downstream evidence role sont des concepts distincts. Un provider label, filename ou timestamp ne constitue pas, à lui seul, une provenance suffisante pour un research artifact.

## 3. Disponibilité et Event Time
<!-- parity-key: data-sources.time -->

Le source timestamp, l'observation/arrival time, le decision time et l'outcome time peuvent différer. La recherche doit utiliser le moment où l'information était réellement disponible pour le decision process afin que les données externes n'introduisent pas de future leakage.

## 4. Transformation Binding
<!-- parity-key: data-sources.transform -->

Les transformations matérielles doivent être reproductibles et liées à la source/dataset identity qu'elles représentent. Des joins ambigus, une provenance incompatible ou une identity requise absente doivent échouer en fail-closed plutôt que de créer silencieusement des evidence mélangées.

## 5. Acceptance et utilisation des preuves
<!-- parity-key: data-sources.acceptance -->

Le data-source acceptance, la dataset integrity et l'evidence of market edge sont des jugements distincts. Une source peut être techniquement acceptable sans démontrer un edge, et un research output favorable ne compense pas l'absence de provenance ou d'integrity evidence requise.

## 6. Limite de publication sûre
<!-- parity-key: data-sources.public-boundary -->

Ne publiez pas les provider credentials, private account identifiers, private endpoints, la current source availability, la cadence exacte d'acquisition ou les budgets, storage roots, mount topology, current dataset hashes ou l'operational source-health state. Les noms de providers ne font pas partie de ce contrat public sans vérification et approbation indépendantes pour publication.

## 7. Guides associés

- [Recherche options / data préréférencée](options_data.md)
- [Recherche en microstructure](microstructure.md)
- [Contrats de preuve](evidence_contracts.md)
