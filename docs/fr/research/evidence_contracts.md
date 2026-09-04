# Contrats de preuve et de provenance (FR)

## 1. Principe

**Un résultat de recherche ne suffit pas pour la promotion.**

## 2. Provenance

Les preuves doivent identifier le rôle et l’origine des éléments de source, de décision et de résultat sans les confondre.

## 3. Identité déterministe des artefacts

Les artefacts doivent avoir des identités déterministes dérivées de leur contrat prévu et de leur contenu afin que des générations répétées puissent être comparées de manière fiable.

## 4. Preuves liées au contenu

Les preuves utilisées pour la validation doivent être liées au contenu qu’elles représentent. Une mutation ou une liaison incohérente doit échouer en fail-closed plutôt que d’être jointe silencieusement.

## 5. Liaison du candidat et du jeu de données

L’identité du candidat/de la configuration et l’identité du jeu de données sont conceptuellement distinctes et doivent être explicitement liées lorsqu’une évaluation dépend des deux.

## 6. Classes de preuves

Les preuves mesurées, synthétiques et contrefactuelles constituent des classes différentes. Elles ne doivent pas être fusionnées silencieusement comme si elles avaient la même portée empirique.

## 7. Échantillons indépendants et agrégation

L’agrégation doit respecter la sémantique des échantillons indépendants. Les preuves dupliquées ou aliasées ne doivent pas gonfler la force de l’échantillon, et les jointures ambiguës doivent échouer en fail-closed.

## 8. Preuves de promotion et preuves d’avantage

Les preuves qui étayent un avantage statistique ou de marché ne sont pas équivalentes aux preuves requises pour la promotion. La promotion peut exiger des validations supplémentaires d’intégrité, de sécurité, d’exécution et de domaine.

## 9. Parité d’exécution / de domaine

La parité execution/domain constitue une couche de validation distincte destinée à détecter les cas où le replay ou la recherche contourne une sémantique importante du runtime.

## 10. Limite de publication sûre

Ce contrat public ne reproduit pas les champs de schéma internes, les ID/hashes actuels des preuves, les noms de candidats, les verdicts de gates ni les preuves opérationnelles.

## 11. Guides associés

- [Recherche / backtesting](backtesting.md)
- [Tests](../testing/testing_guide.md)
