# FICHE DU SUJET F24 — MACHINE LEARNING APPLIQUÉ À LA FINANCE

## 1. Identification du projet

- **Étudiant :** Roger Kangni Soukpe
- **Code Apogée :** 22007860
- **Groupe :** 2
- **Établissement :** École Nationale de Commerce et de Gestion de Settat (ENCG Settat)
- **Module :** Base de données et Data Science (BD & DS)
- **Année universitaire :** 2026–2027
- **Sujet attribué :** F24
- **Intitulé :** Corrélation entre le Nasdaq et le S&P 500

## 2. Contexte et problématique

Le Nasdaq Composite et le S&P 500 sont deux indices boursiers majeurs du marché américain. Leurs évolutions sont généralement liées, mais l'intensité de leur relation peut varier en fonction des conditions économiques et financières.

L'étude de leur corrélation glissante permet d'observer l'évolution de cette relation au cours du temps et d'étudier sa prévisibilité à partir des données historiques.

**Problématique :**

À partir des rendements historiques du Nasdaq et du S&P 500, peut-on prédire si leur corrélation augmentera ou diminuera (ou restera stable) au cours des 20 prochaines séances boursières ?

## 3. Objectif du projet

L'objectif est de construire un modèle de Machine Learning capable de prédire le sens d'évolution de la corrélation entre le Nasdaq et le S&P 500 sur un horizon de 20 séances boursières.

Pour atteindre cet objectif, le travail consiste à :

- Collecter les données historiques des deux indices.
- Calculer leurs rendements journaliers.
- Calculer leur corrélation glissante sur une fenêtre de 60 séances.
- Construire une variable cible binaire représentant l'évolution future de la corrélation.
- Entraîner et évaluer un modèle de classification.
- Comparer ses performances à une référence naïve.

## 4. Nature du problème et approche retenue

- **Type d'apprentissage :** apprentissage supervisé.
- **Tâche :** classification binaire.
- **Algorithme principal :** régression logistique.
- **Modèle de référence :** DummyClassifier (classe majoritaire).
- **Fenêtre de calcul de la corrélation :** 60 séances boursières.
- **Horizon de prévision :** 20 séances boursières.

**Définition de la variable cible :**

- **Classe 0 :** la corrélation diminue ou reste stable.
- **Classe 1 :** la corrélation augmente.

La cible est construite en comparant la corrélation glissante observée à une date donnée avec celle observée 20 séances plus tard.

## 5. Description du jeu de données

### 5.1. Source des données

- **Plateforme :** Yahoo Finance.
- **Bibliothèque de récupération :** Python `yfinance`.
- **Indice 1 :** Nasdaq Composite (`^IXIC`).
- **Indice 2 :** S&P 500 (`^GSPC`).
- **Date d'extraction :** 17 novembre 2026.
- **Période étudiée :** du 17 novembre 2016 au 16 novembre 2026.
- **Fréquence :** quotidienne, selon les séances boursières.
- **Unité d'observation :** une séance boursière.
- **Taille initiale :** 2 512 observations et 2 variables.
- **Nombre de rendements disponibles :** 2 511 pour chaque indice.
- **Jeu de données final après préparation :** 2 432 observations et 5 colonnes.

### 5.2. Liens des sources

- Nasdaq Composite : https://finance.yahoo.com/quote/%5EIXIC/history/
- S&P 500 : https://finance.yahoo.com/quote/%5EGSPC/history/
- Documentation de yfinance : https://github.com/ranaroussi/yfinance

### 5.3. Dictionnaire des variables

| Variable | Rôle | Type | Unité |
|---|---|---|---|
| Nasdaq (prix) | Donnée initiale | Numérique continue | Points d'indice |
| SP500 (prix) | Donnée initiale | Numérique continue | Points d'indice |
| Nasdaq (rendement) | Variable explicative | Numérique continue | Pourcentage (%) |
| SP500 (rendement) | Variable explicative | Numérique continue | Pourcentage (%) |
| corr_60 | Variable explicative | Numérique continue | Coefficient de corrélation |
| corr_future_20 | Variable intermédiaire de construction de la cible | Numérique continue | Coefficient de corrélation |
| target | Variable cible | Binaire (0 ou 1) | Sans unité |

**Précision :** les colonnes `Nasdaq` et `SP500` désignent initialement les cours ajustés des indices, puis leurs rendements journaliers dans le jeu de données préparé.

La variable `corr_future_20` est utilisée uniquement pour construire la cible et n'est pas intégrée aux variables explicatives du modèle.

## 6. Qualité et préparation des données

Les principales vérifications et transformations effectuées sont les suivantes :

- Vérification des types de variables.
- Vérification de l'ordre chronologique des observations.
- Contrôle des dates dupliquées.
- Recherche des valeurs manquantes.
- Analyse statistique et détection des valeurs extrêmes.
- Calcul des rendements journaliers.
- Calcul de la corrélation glissante sur 60 séances.
- Construction de la variable cible sur un horizon de 20 séances.
- Séparation chronologique en ensembles d'entraînement, de validation et de test, avec une purge de 20 séances aux frontières.

Les valeurs extrêmes ont été conservées, car elles peuvent représenter des événements réels sur les marchés financiers.

## 7. Méthodologie d'évaluation

Le modèle de régression logistique est évalué et comparé à une référence naïve construite avec `DummyClassifier(strategy="most_frequent")`.

Les ensembles de données sont répartis chronologiquement :

- Entraînement : 1 682 observations.
- Validation : 345 observations.
- Test : 365 observations.

Les métriques retenues sont :

- **Macro-F1 :** métrique principale.
- **Balanced Accuracy :** métrique secondaire.
- **Recall de la classe 1 :** métrique secondaire.

Les performances finales sont mesurées sur le jeu de test, conservé à l'écart pendant l'entraînement et le réglage des hyperparamètres.

## 8. Sources, licence et conditions d'utilisation

Les données financières ont été récupérées à partir de Yahoo Finance à l'aide de la bibliothèque Python `yfinance`.

Il convient de distinguer les conditions d'utilisation de la bibliothèque et celles des données financières :

- **Bibliothèque `yfinance` :** logiciel libre distribué sous licence Apache 2.0.
- **Données Yahoo Finance :** leur utilisation est soumise aux conditions générales et aux conditions applicables aux services Yahoo. La licence Apache 2.0 de `yfinance` ne s'étend pas aux données téléchargées.
- **Cadre d'utilisation du projet :** exploitation à des fins pédagogiques et de recherche académique.

La documentation officielle de `yfinance` précise que l'outil n'est ni affilié à Yahoo Finance ni approuvé par cette plateforme et renvoie vers les conditions d'utilisation de Yahoo concernant les données récupérées.

En conséquence, les données brutes ne sont pas redistribuées dans le dépôt GitHub sans autorisation appropriée. La procédure de récupération des données est documentée dans le notebook.

**Références relatives aux conditions d'utilisation :**

- Licence Apache 2.0 de yfinance : https://github.com/ranaroussi/yfinance/blob/main/LICENSE.txt
- Documentation et avertissement juridique de yfinance : https://github.com/ranaroussi/yfinance
- Conditions d'utilisation Yahoo : https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html

## 9. Résultat attendu du projet

Le résultat attendu est un modèle de classification capable d'estimer la probabilité d'une augmentation future de la corrélation entre les deux indices.

L'évaluation doit permettre de déterminer si la régression logistique apporte une amélioration par rapport à une stratégie naïve et d'identifier ses limites dans la prévision de l'évolution des relations entre marchés financiers.

---
