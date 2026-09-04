# Contrats de fiabilité et de gestion des défaillances (FR)

## 1. Objectif
<!-- parity-key: reliability.scope -->

La fiabilité est une préoccupation runtime distincte de la logique de trading. La documentation publique décrit la gestion bornée des défaillances, l'observation sûre, les limites de recovery et les diagnostics secret-safe sans exposer l'infrastructure privée ni l'état courant des incidents.

## 2. Gestion bornée des défaillances
<!-- parity-key: reliability.bounded-failure -->

Les défaillances des dépendances externes et network-facing doivent être traitées avec un travail borné. Les timeouts, retries et tentatives de recovery ne doivent pas devenir des boucles de contrôle sans limite, et une dépendance non résolue peut bloquer la progression lorsque son contrat est requis pour la readiness ou une exécution sûre.

## 3. Diagnostics Secret-Safe
<!-- parity-key: reliability.secret-safe -->

Le reporting des défaillances doit conserver des informations utiles de reason/context tout en assainissant credentials, tokens, payloads externes sensibles et autres secrets opérationnels. Les diagnostics ne doivent pas affaiblir la frontière public/private.

## 4. Sémantique des incidents et de la récupération
<!-- parity-key: reliability.incident-normalization -->

Les défaillances doivent être normalisées en sémantiques explicites de reason/state afin que l'observation, le containment et la recovery restent cohérents. L'incident handling et la recovery sont distincts de l'autorisation de placer un nouvel ordre ou de promouvoir un résultat de recherche.

## 5. Limites Fail-Safe
<!-- parity-key: reliability.fail-safe -->

Lorsqu'un state, une provenance ou une dépendance externe requise reste ambiguë, le contrat sûr consiste à contenir la défaillance ou à échouer en fail-closed plutôt qu'à poursuivre en supposant l'état valide. L'observation d'une panne ne modifie pas, à elle seule, le trading state.

## 6. Limite de publication sûre
<!-- parity-key: reliability.public-boundary -->

Ne publiez pas les détails resolver/DNS, la configuration des hôtes, la topologie mount/storage, les process IDs, les incident counts, l'état actuel outage/recovery, les retry budgets exacts, les operator recovery commands exactes ni le contenu sensible des logs/telemetry.

## 7. Guides associés

- [Journalisation et artefacts](logging.md)
- [Exécution / récupération](../architecture/execution_recovery.md)
- [Tests](../testing/testing_guide.md)
