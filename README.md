# ❄️ SnowMaintain AI - Démo Snowflake

> **Plateforme intelligente de maintenance prédictive propulsée par Snowflake**

![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🎯 Objectif

Application de démonstration pour présenter les capacités de **Snowflake** dans le contexte de la maintenance industrielle :

- **Analyse de plans machines** avec Document AI
- **Requêtes en langage naturel** avec Cortex AI
- **Maintenance prédictive** avec ML intégré
- **Visualisations temps réel** avec Streamlit

## 🚀 Fonctionnalités

| Page | Description | Technologies Snowflake |
|------|-------------|----------------------|
| 🏠 Dashboard | Vue d'ensemble du parc machines | Snowsight, Dynamic Tables |
| 🔍 AI SQL Query | Questions en langage naturel → SQL | Cortex AI, LLM |
| 📐 Analyse Plans | Extraction d'infos des schémas techniques | Document AI, OCR |
| 🤖 Assistant | Chatbot maintenance intelligent | Cortex AI, RAG |
| 📊 Analytics | KPIs et tendances | Snowpark, Streamlit |

## 📸 Aperçu

L'interface utilise un design industriel sombre avec les couleurs Snowflake :
- Bleu glacier `#29B5E8`
- Vert émeraude `#00D4AA`
- Fond acier `#0D1B2A`

## 🛠️ Installation locale

```bash
# Cloner le repo
git clone https://github.com/laurabelmd/snowmaintain-ai-demo.git
cd snowmaintain-ai-demo

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

## ☁️ Déploiement Streamlit Cloud

1. Fork ce repository
2. Connectez-vous à [share.streamlit.io](https://share.streamlit.io)
3. Sélectionnez ce repo et `app.py`
4. Déployez !

## 📁 Structure

```
├── app.py                 # Application Streamlit principale
├── requirements.txt       # Dépendances Python
├── .streamlit/
│   └── config.toml       # Configuration thème
└── README.md
```

## 💡 Cas d'usage démontrés

### 1. Natural Language to SQL
> "Quelles pièces montrent des signes d'usure sur la CNC-2450?"

Génération automatique de requêtes SQL optimisées avec analyse contextuelle.

### 2. Maintenance Prédictive
Modèles ML intégrés pour prédire les pannes avant qu'elles ne surviennent.

### 3. Analyse Documentaire
Extraction automatique des spécifications depuis les plans PDF.

## 🔒 Note

Cette application est une **démonstration front-end**. Le backend Snowflake n'est pas connecté - les données sont simulées pour illustrer l'expérience utilisateur possible.

---

<p align="center">
  <strong>Propulsé par</strong><br>
  <img src="https://www.snowflake.com/wp-content/themes/flavor/assets/img/snowflake-logo-white.png" alt="Snowflake" width="150">
</p>

