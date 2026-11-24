# 22007860-KANGNI-SOUKPE-Kangni-Roger-G2
# F24 — Corrélation glissante entre le Nasdaq et le S&P 500

**Projet individuel de Machine Learning appliqué à la finance**

| Informations | Description |
|---|---|
| Étudiant | Roger Kangni Soukpe |
| Code Apogée | 22007860 |
| Groupe | 2 |
| Établissement | ENCG Settat |
| Module | Base de données et Data Science (BD & DS) |
| Année universitaire | 2026–2027 |
| Sujet | F24 — Corrélation Nasdaq et S&P 500 |

---

## 1. Présentation du projet

Le Nasdaq Composite et le S&P 500 sont deux indices boursiers majeurs du marché américain. Leurs évolutions sont généralement liées, mais l'intensité de leur relation peut varier au cours du temps.

Ce projet vise à étudier la corrélation entre ces deux indices et à construire un modèle de Machine Learning capable de prédire son sens d'évolution à court terme.

### Problématique

À partir des rendements historiques du Nasdaq et du S&P 500, peut-on prédire si leur corrélation augmentera ou diminuera (ou restera stable) au cours des 20 prochaines séances boursières ?

### Objectif

Construire un modèle de classification binaire permettant d'anticiper l'évolution future de la corrélation entre les deux indices.

---

## 2. Source et description des données

Les données financières proviennent de **Yahoo Finance** et ont été récupérées à l'aide de la bibliothèque Python `yfinance`.

**Indices étudiés :**
- Nasdaq Composite : `^IXIC`
- S&P 500 : `^GSPC`

**Caractéristiques du jeu de données :**

| Caractéristique | Description |
|---|---|
| Source | Yahoo Finance |
| Période | 17/11/2016 au 16/11/2026 |
| Date d'extraction | 17/11/2026 |
| Fréquence | Quotidienne |
| Observations initiales | 2 512 |
| Rendements disponibles | 2 511 |
| Observations après préparation | 2 432 |
| Valeurs manquantes initiales | 0 |
| Doublons de dates | 0 |

Les données utilisées correspondent aux cours ajustés (`auto_adjust=True`).

**Variables explicatives du modèle :**
- `Nasdaq` : rendement journalier du Nasdaq.
- `SP500` : rendement journalier du S&P 500.
- `corr_60` : coefficient de corrélation glissante calculé sur 60 séances.

**Variable cible :**
- `target` : indique si la corrélation augmente (1) ou diminue/reste stable (0) sur les 20 prochaines séances.

---

## 3. Méthodologie et algorithme

Le projet suit une démarche de science des données comprenant la collecte, l'exploration, la préparation, l'entraînement et l'évaluation du modèle.

### Étapes principales

1. Collecte des données historiques des deux indices.
2. Calcul des rendements journaliers.
3. Analyse exploratoire des données (EDA).
4. Calcul de la corrélation glissante sur 60 séances.
5. Construction de la variable cible à horizon de 20 séances.
6. Séparation chronologique des données avec une purge de 20 séances aux frontières.
7. Standardisation des variables et entraînement du modèle.
8. Évaluation et analyse des erreurs.

### Algorithme principal

**Régression logistique (Logistic Regression)**

La régression logistique est utilisée pour résoudre le problème de classification binaire.

Le modèle exploite trois variables explicatives : les rendements du Nasdaq, les rendements du S&P 500 et la corrélation glissante sur 60 séances.

### Modèle de référence

Un `DummyClassifier(strategy="most_frequent")` est utilisé comme référence naïve afin de comparer les performances du modèle principal à une stratégie qui prédit systématiquement la classe majoritaire.

### Protocole d'évaluation

La séparation des données respecte l'ordre chronologique :

| Ensemble | Observations |
|---|---:|
| Entraînement | 1 682 |
| Validation | 345 |
| Test | 365 |

Le réglage des hyperparamètres est effectué à partir de l'ensemble de validation. Le test est conservé pour l'évaluation finale.

---

## 4. Résultats obtenus

Les performances finales sont mesurées sur l'ensemble de test.

### Comparaison du modèle avec la baseline

| Métrique | Régression logistique | Baseline |
|---|---:|---:|
| Accuracy | **65,48 %** | 42,47 % |
| Macro-F1 | **0,5788** | 0,2981 |
| Balanced Accuracy | **60,45 %** | 50,00 % |

La régression logistique obtient de meilleures performances que la référence naïve sur les trois métriques.

### Analyse des erreurs

L'évaluation finale donne les résultats suivants :

- 239 prédictions correctes sur 365 observations.
- 126 erreurs de classification.
- 113 faux négatifs : augmentations de corrélation non détectées.
- 13 faux positifs : fausses alertes d'augmentation.
- Recall de la classe 1 : 27,10 %.

Ces résultats montrent que le modèle détecte mieux les diminutions ou stabilités de corrélation que les augmentations.

### Conclusion des résultats

La régression logistique présente une capacité de classification supérieure à la référence naïve. Toutefois, ses performances restent modérées, notamment en matière de détection des augmentations de corrélation.

---

## 5. Structure du dépôt

```text
22007860-KANGNI-SOUKPE-Kangni-Roger-G2/
│
├── README.md
├── requirements.txt
├── .gitignore
├── DECLARATION_IA.md
│
├── data/
│   └── raw/
│
├── docs/
│   └── fiche_sujet_F24.md
│
├── notebooks/
│   └── projet_F24.ipynb
│
├── figures/
│   ├── evolution_indices.png
│   ├── rendements_journaliers.png
│   ├── correlation_glissante.png
│   └── matrice_confusion.png
│
├── rapport/
│   └── rapport.pdf
│
└── presentation/
    ├── presentation.pdf
    └── presentation.pptx
```

La vidéo explicative est accessible depuis le lien indiqué dans la section suivante.

---

## 6. Présentation et vidéo explicative

- **Présentation PDF :** [Consulter les six diapositives](https://drive.google.com/file/d/1MZ5-U_pkl4mHoxt9Hkw0csrVUTV8-kkU/view?usp=sharing)
- **Présentation PowerPoint :** [Télécharger le fichier source](https://docs.google.com/presentation/d/1NDTHfv5nVzGdszhcyyZi7NKdn4b94mMT/edit?usp=sharing&ouid=105769077090336634002&rtpof=true&sd=true)
- **Rapport PDF :** [Consulter le rapport](https://drive.google.com/file/d/1wMK950vCDvkukgv4y-gsRYLwS9SHsQTY/view?usp=sharing)
- **Vidéo explicative :** [Regarder la démonstration du projet](https://drive.google.com/file/d/1xTBeHT6_Yrz-aQBECBWHsvkdf0q7f3Pc/view?usp=sharing)

---

## 7. Installation et exécution du projet

### Prérequis

- Python 3.13.18
- Jupyter Notebook, JupyterLab ou Google Colab.
- Une connexion Internet pour récupérer les données depuis Yahoo Finance.

### Installation des dépendances

Cloner le dépôt GitHub, puis installer les bibliothèques nécessaires :

```bash
pip install -r requirements.txt
```

### Exécution

1. Ouvrir le notebook `notebooks/projet_F24.ipynb`.
2. Vérifier que les dépendances sont installées.
3. Exécuter les cellules dans l'ordre, de la première à la dernière.
4. Le notebook récupère les données historiques, réalise les traitements et produit les résultats du modèle.

**Remarque :** la récupération des données nécessite une connexion Internet. Les données brutes de Yahoo Finance ne sont pas redistribuées dans ce dépôt ; elles sont récupérées à l'exécution du notebook.

---

## 8. Bibliothèques utilisées

- `yfinance` : récupération des données financières.
- `pandas` : manipulation et structuration des données.
- `numpy` : calculs numériques.
- `matplotlib` : visualisation graphique.
- `seaborn` : visualisation statistique.
- `scikit-learn` : préparation, entraînement et évaluation du modèle de Machine Learning.

---

## 9. Sources et références

- [Yahoo Finance — Nasdaq Composite](https://finance.yahoo.com/quote/%5EIXIC/history/)
- [Yahoo Finance — S&P 500](https://finance.yahoo.com/quote/%5EGSPC/history/)
- [Documentation yfinance](https://github.com/ranaroussi/yfinance)
- [Documentation Pandas](https://pandas.pydata.org/docs/)
- [Documentation Scikit-learn](https://scikit-learn.org/stable/)

**Conditions d'utilisation :** les données récupérées sur Yahoo Finance restent soumises aux conditions d'utilisation de cette plateforme. La licence de la bibliothèque `yfinance` ne constitue pas une licence de redistribution des données financières.

---

## 10. Déclaration d'utilisation de l'intelligence artificielle

Une déclaration détaillant l'utilisation de ChatGPT dans le cadre de ce projet est disponible dans le fichier [`DECLARATION_IA.md`](DECLARATION_IA.md).

---

**Projet réalisé dans le cadre du module Base de données et Data Science — ENCG Settat, année universitaire 2026–2027.**
