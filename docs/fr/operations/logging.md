# Guide Logs et Artifacts (FR)

Mise à jour : 2026-09-04

## 1. Objectif

Les logs, la structured telemetry, l'état runtime mutable, l'état des métriques et les sorties offline générées sont des surfaces d'observabilité/artifacts distinctes avec des règles d'ownership différentes. Les logs ordinaires ne constituent qu'une partie du modèle d'observabilité.

## 2. Sémantique de la Structured Telemetry

La structured telemetry enregistre des événements et observations lisibles par machine pour l'inspection et la validation ultérieures. Au niveau du contrat public-safe, les familles de recorders peuvent couvrir des observations de type decision, path, shadow et scanner ; cette documentation n'expose ni leurs schémas internes, ni leur activation actuelle, ni leur contenu enregistré.

L'enregistrement ou l'observation d'un état n'est pas une surface d'autorisation de trading. La collecte de telemetry ne doit pas, à elle seule, créer des ordres, promouvoir des résultats de recherche ou modifier le trading state.

## 3. Activation, Freshness et Provenance

La disponibilité de la telemetry s'interprète à partir de sémantiques explicites d'activation/profile et de provenance, et non simplement de la présence d'un fichier. Une source peut être enabled, disabled, unavailable, stale ou légitimement idle ; expected-idle et stale data sont des états distincts.

Lorsqu'un contrat de telemetry exige un binding de configuration ou de provenance, un binding absent ou invalide ne doit pas être traité comme une preuve valide/actuelle. Cette validation est fail-closed pour l'interprétation de la telemetry sans transformer l'observation en mutation du trading state.

## 4. Layout des Logs Runtime

```text
logs/
  mainnet/<hostname>/
    activity.log
    trades.log
    performance.log
    metrics.log
  testnet/<hostname>/
    activity.log
    trades.log
    performance.log
    metrics.log
  watchdog.log
  bot_launcher.log
```

Le partitionnement par hostname évite les collisions lorsque plusieurs machines écrivent vers un stockage partagé.

## 5. État et Métriques

```text
data/<env>/          # état runtime mutable
data/metrics/<env>/  # telemetry, health et compteurs d'erreurs mutables
```

Ces chemins déjà publics décrivent des classes d'ownership stables. La structured event telemetry peut disposer d'un stockage supplémentaire owned by implementation ; les chemins privés exacts des recorders et leur contenu runtime ne sont volontairement pas documentés ici.

## 6. Sorties Offline Générées

```text
data/out/audit/
data/out/benchmark/
data/out/integration/
data/out/readiness/
data/out/reporting/
data/out/testing/
```

Les sorties générées ne doivent pas être stockées sous `docs/` ou dans les répertoires de code tooling par défaut.

## 7. Commandes Utiles

```bash
tail -f logs/testnet/$(hostname)/activity.log
tail -f logs/testnet/$(hostname)/trades.log
tail -f logs/watchdog.log
tail -f logs/bot_launcher.log
```

## 8. Règles de Sécurité et Public-Safety

- Ne jamais logger des clés API, secrets, tokens ou chat identifiers bruts.
- Garder la sanitization active pour les payloads externes.
- Préférer reason codes et IDs contextuels aux réponses sensibles brutes.
- Ne pas publier les production logs, le contenu de structured telemetry, l'état actuel des recorders, les private hashes, les incident data ou les generated runtime data dans ce dépôt de documentation.
- Ne pas déduire l'operational health actuel ni le trading state à partir des exemples de documentation publique.

## 9. Pièges Courants

- Considérer les logs ordinaires comme le modèle complet d'observabilité.
- Assimiler l'absence de fresh telemetry à une panne sans tenir compte des expected-idle semantics.
- Considérer une recorder observation comme une action ou une promotion authorization.
- Lire d'anciens chemins de logs sans segment `<hostname>`.
- Mélanger logs de contrôle racine et logs runtime env/host.
- Traiter les rapports générés comme documentation canonique.
- Committer archives research locales ou sorties générées.

## 10. Guides Associés

- [Project Map](../architecture/project_map.md)
- [Research / Backtesting](../research/backtesting.md)
- [Evidence Contracts](../research/evidence_contracts.md)
- [Testing](../testing/testing_guide.md)
