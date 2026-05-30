# Guide de Tests (FR)

Mise à jour : 2026-05-30

## 1. Scope

Cette page décrit les workflows public-safe de validation de l'implémentation privée.
Les nombres exacts de modules de tests ne sont volontairement pas figés dans les
docs publiques, car ils changent fréquemment.

## 2. Validation Runtime

Depuis la racine de l'implémentation privée :

```bash
./scripts/testing/run_tests_quick.sh
./scripts/testing/run_tests.sh
```

Utiliser la validation rapide pendant les itérations et la suite complète avant
merge ou rollout.

## 3. Focus Areas

Vérifier les tests et preuves pour :

- dry-run : aucune exécution Spot ou Convert réelle ;
- ordering SELL-before-BUY ;
- ownership et precedence de configuration ;
- modes risk manager et containment par symbole ;
- hot reload config/strategy et limite restart pour les clés API ;
- comportement du launcher détaché ;
- chargement archive-root et parité same-core replay ;
- routage des sorties générées sous `data/out/<domain>/`.

## 4. Validation Research

Pour les workflows research, utiliser une archive root locale :

```bash
python tools/analysis/<research-tool>.py --archive-root <archive-root>
```

Un résultat influençant le rollout doit être reproductible depuis une archive root
stable et produire des preuves baseline-vs-candidate révisables.

## 5. Validation Documentation

Depuis la racine du dépôt public de documentation :

```bash
python3 scripts/docs/check_language_parity.py
bash scripts/docs/validate_links.sh
git diff --check
```

## 6. Sorties Générées

Les sorties de validation générées doivent utiliser des chemins par domaine :

```text
data/out/testing/
data/out/benchmark/
data/out/integration/
data/out/readiness/
data/out/audit/
```

Ne pas placer de sortie générée sous `docs/`, sauf document public volontairement
curaté et maintenu manuellement.
