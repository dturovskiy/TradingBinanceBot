# Guide de tests (FR)

## 1. Périmètre

La documentation publique ne fige volontairement pas un nombre exact de tests ; la taille de la collection évolue avec le temps.

## 2. Taxonomie des tests

Les catégories actuellement adaptées à la documentation publique comprennent :

- tests unitaires ;
- tests d’intégration ;
- tests property-based / Hypothesis ;
- tests de régression paramétrés ;
- tests de contrat ;
- tests de persistance / écriture atomique ;
- tests d’état des ordres / récupération ;
- tests de failure paths / résilience réseau ;
- tests de replay / parité ;
- tests de recherche / provenance ;
- tests d’observabilité ;
- tests de risque / API / exécution.

## 3. Catégories du pipeline de validation

Lorsque c’est pertinent, la validation combine des contrôles statiques/de types, des contrôles de configuration/fail-safe, pytest et des contrôles benchmark/performance. La documentation publique ne revendique pas un pourcentage de coverage actuellement imposé sans nouvelle vérification spécifique.

## 4. Tests d’exécution / récupération

Validez la persistance de l’état durable, la réconciliation après redémarrage, la récupération idempotente, le traitement fail-closed des états non résolus, le gate de disponibilité et l’invariant selon lequel la récupération ne soumet pas de nouveaux ordres. Exercez explicitement les divergences entre état externe et local, les preuves de réconciliation incomplètes ou indisponibles, les échecs de persistance et les tentatives répétées de récupération.

## 5. Tests de recherche / replay

Validez la sémantique de l’event time, l’absence de fuite d’informations futures, le replay déterministe, les découpages respectant le temps, la liaison du jeu de données et de la provenance, le traitement des échantillons indépendants et la parité execution/domain. Un test méthodologique peut valider ces contrats sans affirmer qu’un candidat ou un gate actuel réussit.

## 6. Validation de la documentation

Exécutez :

```bash
python3 scripts/docs/check_language_parity.py
bash scripts/docs/validate_links.sh
git diff --check
```

Lorsque l’exécution Bash est bloquée par la politique des outils, effectuez une validation interne équivalente des liens Markdown et consignez cette limitation.

La revue documentaire vérifie aussi la présence des fichiers de gouvernance partagés obligatoires, la parité de navigation/des liens et l’absence de détails d’implémentation privée ou d’état opérationnel/de recherche courant.

## 7. Limite de publication sûre

Les preuves générées par les tests ou la recherche, les chemins privés, les résultats actuels de stratégies/candidats et les artefacts opérationnels du runtime ne sont pas publiés ici.
