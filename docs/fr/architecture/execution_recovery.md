# État d’exécution durable et récupération (FR)

## 1. Objectif

Les systèmes de trading peuvent observer un état exécuté à l’extérieur tout en maintenant un état géré localement. L’état d’exécution durable fournit un contrat résistant aux redémarrages pour résoudre cette frontière.

## 2. État externe et état local

L’état de l’exchange et l’état géré localement sont des sources d’information distinctes. Un redémarrage de processus, une réponse ambiguë ou une mise à jour locale partielle peuvent imposer une réconciliation avant la reprise du fonctionnement normal.

L’exchange fait autorité sur ce qu’il a observé et exécuté, tandis que l’état géré localement porte le contexte de comptabilité, de risque et de cycle de vie. Une réponse conservée en mémoire ne suffit pas à prouver que les deux vues concordent ; l’état durable conserve assez de contexte d’intention et de résultat pour permettre une réconciliation ultérieure sans traiter une nouvelle tentative comme une nouvelle décision de trading.

## 3. Réconciliation avant la disponibilité

Tout état d’exécution non résolu mais requis est réconcilié avant l’ouverture du gate normal de disponibilité du trading. Si la cohérence requise ne peut pas être établie, le système fonctionne en fail-closed au lieu de supposer que l’état est sûr.

Des preuves de réconciliation inconnues, contradictoires, incomplètes ou temporairement indisponibles restent non résolues et maintiennent fermé le chemin de disponibilité concerné.

## 4. Récupération idempotente après redémarrage

La récupération doit être déterministe et idempotente : répéter la même opération de récupération sur les mêmes preuves durables ne doit ni appliquer deux fois le même état ni créer de nouvelles actions de trading.

## 5. La récupération ne place pas de nouveaux ordres

La récupération peut inspecter et réconcilier un état d’exécution existant, mais elle n’autorise pas à elle seule le placement de nouveaux ordres. Toute nouvelle activité de trading reste soumise aux contrats normaux d’exécution et de disponibilité.

## 6. Attentes en matière de tests

Les attentes publiables en matière de tests comprennent les tests de redémarrage/récupération, les tests de persistance et d’écriture atomique, les tests d’ambiguïté et de failure paths, les contrôles d’idempotence, les tests de réconciliation/disponibilité et les tests démontrant que la récupération ne soumet pas de nouveaux ordres. Elles doivent couvrir explicitement les divergences entre état externe observé et état local, les preuves de réconciliation incomplètes ou indisponibles et les échecs de persistance.

## 7. Limite de publication sûre

La documentation publique omet volontairement les chemins de stockage exacts, les formats de journaux, l’ordre des écritures, les fenêtres de panne, les détails d’incidents opérationnels, les mécanismes de réconciliation live et les commandes exactes de récupération.

## 8. Guides associés

- [Carte du projet](project_map.md)
- [Tests](../testing/testing_guide.md)
