# 📉 Prédiction du Risque de Défaut Client

## 🎯 Objectif du projet
Ce projet a pour but de développer un modèle de machine learning capable de prédire la probabilité qu'un client bancaire ne rembourse pas un prêt, en se basant sur des données financières et personnelles. Ce type de modèle est essentiel pour améliorer les dispositifs de supervision des risques dans le secteur bancaire.

## 🧰 Outils et technologies utilisés
- **Python** (Pandas, NumPy, Scikit-learn)
- **XGBoost**, Régression logistique
- **SHAP** pour l'interprétation des modèles
- **Power BI** pour les visualisations interactives
- **Jupyter Notebook** pour l'analyse exploratoire

## 📁 Données utilisées
Je me suis appuyé sur le dataset "Give Me Some Credit" disponible sur Kaggle. Il comprend des variables telles que :
- Revenus mensuels
- Nombres de lignes de crédit
- Historique de paiement
- Délai de remboursement

## 🚀 Étapes du projet
1. **Exploration et nettoyage** : traitement des valeurs manquantes, outliers et encodage des variables
2. **Feature engineering** : création de nouvelles variables pertinentes
3. **Modélisation** : tests de plusieurs modèles (régression logistique, Random Forest, XGBoost)
4. **Évaluation** : AUC, F1-score, matrices de confusion
5. **Interprétation** : identification des variables les plus influentes via SHAP
6. **Visualisation** : construction d'un dashboard Power BI pour présenter les résultats aux équipes métier

## 🧠 Résultats
- **Modèle XGBoost** avec une AUC de 0.86
- **Les variables les plus influentes** : nombre d'impayés, dettes en cours, ratio dette/revenu
- **Dashboard interactif** montrant les segments de clients à risque

## 📝 Enjeux métier
Un tel modèle peut aider une institution financière à :
- Identifier en amont les profils à risque
- Ajuster les politiques de crédit
- Renforcer la supervision réglementaire et la prise de décision stratégique

## 📎 Ce que j'ai appris
- Importance du data cleaning et de l'équilibrage des classes
- Interprétabilité des modèles : indispensable en contexte bancaire
- Puissance combinée d'un modèle robuste et d'un dashboard clair

## 🚦 Lancer l'application Streamlit

Pour lancer l'application Streamlit en local, exécute la commande suivante dans le terminal à la racine du projet :

```bash
streamlit run app.py
```

Assure-toi d'avoir installé toutes les dépendances nécessaires (voir `requirements.txt`).

