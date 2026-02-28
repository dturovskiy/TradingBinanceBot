# Guide de Logging (FR)

Mise a jour: 2026-02-28

Guide aligne sur le comportement runtime actuel du `BinaceBot` prive.

## 1. Topologie des loggers

Definis dans `src/logging_config.py`:

- `app`
- `trade`
- `performance`
- `metrics`
- `portfolio`
- `illiquid_health`
- `decision_matrix`
- `circuit_breaker`
- `data_manager`
- `api`

Watchdog utilise un logger dedie (`scripts/monitoring/watchdog_monitor.py`).

## 2. Arborescence logs

```text
logs/
  mainnet/
    <hostname>/
      activity.log
      trades.log
      performance.log
      metrics.log
  testnet/
    <hostname>/
      activity.log
      trades.log
      performance.log
      metrics.log
  watchdog.log
```

Le sous-dossier `<hostname>` evite les conflits multi-hotes.

## 3. Rotation

- Type: size-based
- Taille max: `10 MB`
- Backups: `30`
- Compression: non activee

## 4. Role des fichiers

- `activity.log`: evenements systeme/runtime.
- `trades.log`: flux trading uniquement.
- `performance.log`: resumes performance.
- `metrics.log`: metriques et compteurs.
- `watchdog.log`: controle processus + heartbeat watchdog.

## 5. Champs utiles

- `operation`
- `symbol`
- `stage`
- `reason_code`
- `iteration`
- `recovery_action`
- `risk_manager_mode`
- `feature_*`

## 6. Securite

- Ne jamais logger les secrets API en clair.
- Maintenir la sanitation active.
- Eviter le dump complet des payloads externes en erreur.

## 7. Commandes pratiques

```bash
tail -f logs/testnet/$(hostname)/activity.log
tail -f logs/testnet/$(hostname)/trades.log
tail -f logs/watchdog.log
rg "risk_manager|reason_code|decision summary" logs/testnet/$(hostname)/activity.log
```
