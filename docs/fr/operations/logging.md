# Guide Logs et Artifacts (FR)

Mise à jour : 2026-05-30

## 1. Objectif

Logs, état runtime mutable, état des métriques et sorties offline générées ont
des règles d'ownership distinctes. Les séparer pendant l'exploitation et le debug.

## 2. Layout des Logs Runtime

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

Le partitionnement par hostname évite les collisions lorsque plusieurs machines
écrivent vers un stockage partagé.

## 3. État et Métriques

```text
data/<env>/          # état runtime mutable
data/metrics/<env>/  # telemetry, health et compteurs d'erreurs mutables
```

Traiter ces chemins comme état opérationnel, non comme documentation.

## 4. Sorties Offline Générées

```text
data/out/audit/
data/out/benchmark/
data/out/integration/
data/out/readiness/
data/out/reporting/
data/out/testing/
```

Les sorties générées ne doivent pas être stockées sous `docs/` ou dans les
répertoires de code tooling par défaut.

## 5. Commandes Utiles

```bash
tail -f logs/testnet/$(hostname)/activity.log
tail -f logs/testnet/$(hostname)/trades.log
tail -f logs/watchdog.log
tail -f logs/bot_launcher.log
```

## 6. Règles de Sécurité

- Ne jamais logger clés API, secrets, tokens ou chat identifiers bruts.
- Garder la sanitization active pour les payloads externes.
- Préférer reason codes et IDs contextuels aux réponses sensibles brutes.
- Ne pas publier logs de production ou données runtime générées dans ce dépôt docs.

## 7. Pièges Courants

- Lire d'anciens chemins de logs sans segment `<hostname>`.
- Mélanger logs de contrôle racine et logs runtime env/host.
- Traiter les rapports générés comme documentation canonique.
- Committer archives research locales ou sorties générées.
