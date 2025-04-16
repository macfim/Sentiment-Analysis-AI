# Détection d'Émotions dans le Texte par Traitement du Langage Naturel

## Introduction

Ce projet vise à identifier les émotions ressenties à partir d'un texte écrit grâce aux techniques de traitement du langage naturel (NLP) et d'apprentissage automatique. L'application permet aux utilisateurs de saisir un texte et d'analyser automatiquement l'émotion dominante exprimée dans ce texte, accompagnée de conseils psychologiques adaptés et de ressources vidéo pertinentes.

L'analyse des émotions dans le texte a des applications variées dans de nombreux domaines :

- Soutien psychologique et bien-être mental
- Analyse de sentiment pour les avis clients
- Recherche en psychologie cognitive
- Amélioration des interactions homme-machine

## Dataset

Le dataset utilisé pour ce projet contient des données textuelles en anglais, étiquetées avec l'une des huit émotions suivantes : colère (anger), dégoût (disgust), peur (fear), joie (joy), neutre (neutral), tristesse (sadness), honte (shame) et surprise (surprise). Le dataset contient un total de 34 795 lignes.

Les données ont été pré-traitées pour éliminer les caractères spéciaux, normaliser la casse et supprimer les mots vides (stop words), afin d'améliorer la précision du modèle de classification.

## Méthodologie

Notre approche méthodologique s'est déroulée en plusieurs étapes :

1. **Prétraitement des données** :

   - Nettoyage du texte (suppression des caractères spéciaux et de la ponctuation)
   - Tokenisation (découpage du texte en mots individuels)
   - Suppression des mots vides (stop words)
   - Lemmatisation (réduction des mots à leur forme de base)

2. **Extraction de caractéristiques** :

   - Utilisation de la technique TF-IDF (Term Frequency-Inverse Document Frequency)
   - Vectorisation du texte pour créer des représentations numériques exploitables par le modèle

3. **Modélisation** :

   - Entraînement d'un modèle de régression logistique multiclasse
   - Optimisation des hyperparamètres par validation croisée
   - Évaluation du modèle sur un ensemble de test séparé

4. **Développement de l'interface utilisateur** :
   - Création d'une application web interactive avec Streamlit
   - Intégration d'une API YouTube pour recommander des vidéos pertinentes
   - Mise en place d'un système de suivi des prédictions et des visites

## Résultats

Le modèle de classification d'émotions a obtenu les performances suivantes :

- **Précision globale** : 62%

L'application web fournit en temps réel :

- L'émotion détectée avec un indice de confiance
- Des conseils psychologiques adaptés à l'émotion identifiée
- Des exercices pratiques pour gérer l'émotion
- Des vidéos YouTube recommandées en fonction de l'émotion
- Un suivi des statistiques d'utilisation

## Fonctionnalités de l'Application

- **Analyse en temps réel** des émotions dans le texte saisi
- **Visualisation des probabilités** pour chaque classe d'émotion
- **Conseils personnalisés** basés sur l'émotion détectée
- **Recommandations de vidéos** YouTube pertinentes
- **Tableau de bord de suivi** des statistiques d'utilisation
- **Interface responsive** adaptée à différents appareils

## Installation

1. Clonez le dépôt sur votre machine locale :

```
git clone https://github.com/SannketNikam/Emotion-Detection-in-Text.git
```

2. Installez les dépendances requises :

```
pip install -r requirements.txt
```

3. Lancez l'application :

```
streamlit run app.py
```

4. L'application s'ouvrira automatiquement dans votre navigateur par défaut.

## Technologies Utilisées

- Python
- Streamlit
- Scikit-learn
- NLTK
- Pandas & NumPy
- Altair pour la visualisation
- API YouTube
