# Contrats de contrôle opérateur (FR)

## 1. Objectif
<!-- parity-key: operator.scope -->

Le runtime possède des surfaces de notification et de contrôle destinées aux opérateurs, notamment des interactions de type messaging/panel. Cette page décrit des contrats de contrôle stables et public-safe, pas la syntaxe privée des commandes ni l'état opérationnel courant.

## 2. Limite d'autorisation
<!-- parity-key: operator.auth -->

Les actions opérateur sont soumises à des contrôles d'access-control et d'autorization. La connaissance d'un nom de commande ou l'accès à un message transport ne confère pas, à elle seule, d'autorité, et la documentation publique ne doit pas exposer credentials, chat identifiers, allowlists ou configuration privée d'autorisation.

## 3. Notifications et panneaux
<!-- parity-key: operator.notifications -->

Les notifications et surfaces status/panel peuvent présenter observations, health ou contexte de workflow à un opérateur autorisé. Afficher ou acquitter une information est distinct d'une mutation du trading state.

## 4. Classes de commandes
<!-- parity-key: operator.command-classes -->

Au niveau du contrat public, les contrôles opérateur peuvent couvrir observation/status, workflows de lifecycle ou configuration, notifications/panels et actions de contrôle explicitement autorisées. Les privileged command strings exactes, recovery procedures et production parameters restent privés.

## 5. Le contrôle ne contourne pas les Safety Gates
<!-- parity-key: operator.non-authority -->

Une surface operator-control ne contourne pas silencieusement les gates de risk, readiness, recovery, evidence ou promotion. Une research evidence ne devient pas une rollout authority simplement parce qu'elle est visible dans une interface opérateur.

## 6. Limite de publication sûre
<!-- parity-key: operator.public-boundary -->

Ne publiez pas les chat IDs, access-control lists, tokens, commandes privileged ou recovery exactes, l'état runtime courant, les incident procedures, positions/trades actuels, infrastructure identifiers ou production thresholds.

## 7. Guides associés

- [Fiabilité](reliability.md)
- [Journalisation et artefacts](logging.md)
- [Carte du projet](../architecture/project_map.md)
