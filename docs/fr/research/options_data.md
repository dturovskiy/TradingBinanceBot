# Recherche options et construction de datasets préréférencées (FR)

## 1. Objectif
<!-- parity-key: options.scope -->

La recherche offline options/data peut utiliser des workflows preregistered, reproductibles et bornés de construction de datasets avec une provenance explicite et des acceptance controls. Cette page documente ce contrat de workflow sans exposer l'état actuel des builds ni le storage layout.

## 2. Préréférencement
<!-- parity-key: options.preregistration -->

La portée prévue du dataset, son evaluation role et ses acceptance conditions doivent être définies avant l'inspection finale des résultats lorsque la preregistration fait partie de la méthodologie. Un preregistered holdout ou dataset role n'est pas une surface de tuning répétée.

## 3. Builds reproductibles et bornés
<!-- parity-key: options.dataset-build -->

La construction d'un dataset doit utiliser une source identity explicite, un transformation context et des build semantics déterministes ou reproductibles. Le travail doit être conceptuellement borné afin qu'un offline data workflow ne devienne pas une runtime dependency incontrôlée.

## 4. Acceptance Controls
<!-- parity-key: options.acceptance -->

Le build acceptance est distinct de l'evidence of market edge. Les contrôles requis d'integrity, completeness, provenance et de contrat peuvent rejeter un artifact sans transformer son acceptation ou son rejet en trading authorization.

## 5. Provenance et Evidence Binding
<!-- parity-key: options.provenance -->

La dataset identity, la source provenance, la transformation provenance et les downstream evidence bindings doivent rester explicites. Des bindings requis absents ou incompatibles échouent en fail-closed plutôt que de joindre silencieusement des artifacts issus de contextes de recherche différents.

## 6. Limite de publication sûre
<!-- parity-key: options.public-boundary -->

Ne publiez pas les dataset roots actuels, la topologie mount/storage, le build status, les acceptance verdicts actuels, private hashes, account/provider credentials, budgets exacts, options candidates actuels, paramètres actifs de stratégie ou la next operator action.

## 7. Guides associés

- [Contrats de sources de données](data_sources.md)
- [Contrats de preuve](evidence_contracts.md)
- [Recherche / backtesting](backtesting.md)
