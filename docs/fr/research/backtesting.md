# Méthodologie de recherche et de backtesting (FR)

## 1. Objectif

La recherche et le replay doivent produire des preuves reproductibles et sûres sur le plan temporel, sans devenir une seconde implémentation de trading non contrôlée.

## 2. Sémantique du temps d’événement

Les décisions reposent sur un event time explicitement défini. Les données qui n’étaient pas disponibles au moment de la décision ne doivent pas influencer cette décision. Le temps d’observation, le temps de décision et le temps du résultat peuvent représenter des concepts différents et ne doivent pas être silencieusement ramenés à un seul timestamp.

## 3. Replay déterministe

Les mêmes entrées, versions de contrats et configuration déterministe doivent produire des résultats de replay reproductibles.

## 4. Absence de fuite d’informations futures

Les entrées disponibles au moment de la décision sont séparées des données d’observation ou de résultat ultérieures. Les résultats futurs ne doivent pas se retrouver dans la construction antérieure des features, le classement ou les décisions.

## 5. Parité live / replay

Les sémantiques communes doivent être réutilisées lorsque c’est pertinent. Les adaptateurs peuvent rester isolés, mais le replay ne doit pas contourner silencieusement des contrats importants d’exécution live, de risque ou de validation. La parité n’exige pas des environnements identiques : les différences doivent être explicites et validées plutôt qu’accidentelles.

## 6. Identité et provenance des jeux de données

La provenance de la source, de la décision et du résultat correspond à des concepts distincts. Des identités déterministes et une liaison au contenu réduisent les mélanges accidentels de jeux de données ou de preuves.

## 7. Sémantique des échantillons indépendants

Les lignes, horizons ou observations répétées ne constituent pas automatiquement des échantillons indépendants. Des lignes dupliquées, des horizons qui se chevauchent ou plusieurs représentations du même événement sous-jacent peuvent constituer des preuves corrélées ou aliasées plutôt qu’un support indépendant. L’indépendance doit découler d’une méthodologie explicite adaptée aux preuves considérées.

## 8. Méthodologie de découpage respectant le temps

Utilisez des frontières explicites train/review/holdout. Appliquez purge/embargo lorsque nécessaire pour éviter les fuites aux frontières. Un holdout utilisé une seule fois n’est pas une surface de tuning.

## 9. Isolation du Scanner et Barrière de Promotion

L’exécution research/scanner est isolée de l’order placement. Le travail du scanner reste derrière une no-order boundary, est conceptuellement bounded et doit isoler les défaillances afin qu’un échec de recherche ne devienne pas une trading action.

La sortie du scanner constitue une evidence/input, pas une promotion authorization. Les preuves issues de la recherche n’autorisent pas à elles seules un rollout ; des couches distinctes de validation de l’intégrité des jeux de données, de la parité execution/domain et d’autres exigences peuvent bloquer la promotion. Des preuves requises absentes, invalides ou insuffisantes échouent en fail-closed plutôt que de promouvoir silencieusement un résultat.

## 10. Limite de publication sûre

Ne publiez pas les noms actuels de candidats, les résultats actuels de stratégies, les hashes privés de jeux de données, l’état courant PASS/FAIL d’un gate ni l’état opérationnel du rollout. Les sorties de recherche générées appartiennent à l’espace d’artefacts géré de l’implémentation privée, et non à ce dépôt public de documentation.

## 11. Guides associés

- [Contrats de preuve](evidence_contracts.md)
- [Tests](../testing/testing_guide.md)
