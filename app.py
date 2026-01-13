# -*- coding: utf-8 -*-
"""
🔧 SnowMaintain AI - Démonstration Snowflake
Analyse de plans machines & Assistance maintenance par IA
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import random

# =============================================================================
# CONFIGURATION PAGE
# =============================================================================
st.set_page_config(
    page_title="SnowMaintain AI | Snowflake Demo",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# STYLES CSS PERSONNALISÉS
# =============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Outfit:wght@300;400;600;700&display=swap');
    
    :root {
        --snow-blue: #29B5E8;
        --snow-dark: #0D1B2A;
        --snow-accent: #00D4AA;
        --industrial-orange: #FF6B35;
        --steel-gray: #2E3A47;
    }
    
    .main {
        background: linear-gradient(135deg, #0D1B2A 0%, #1B2838 50%, #0D1B2A 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #0D1B2A 0%, #1B2838 50%, #0D1B2A 100%);
    }
    
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif !important;
        color: #FFFFFF !important;
    }
    
    .hero-title {
        font-family: 'Outfit', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #29B5E8, #00D4AA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
    }
    
    .hero-subtitle {
        font-family: 'Outfit', sans-serif;
        font-size: 1.3rem;
        color: #8B9CAF;
        text-align: center;
        margin-top: 0.5rem;
    }
    
    .metric-card {
        background: linear-gradient(145deg, #1E2D3D, #162231);
        border: 1px solid #29B5E8;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(41, 181, 232, 0.15);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(41, 181, 232, 0.25);
    }
    
    .metric-value {
        font-family: 'JetBrains Mono', monospace;
        font-size: 2.5rem;
        font-weight: 700;
        color: #29B5E8;
    }
    
    .metric-label {
        font-family: 'Outfit', sans-serif;
        font-size: 0.9rem;
        color: #8B9CAF;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .sql-box {
        background: #0a0f14;
        border: 1px solid #29B5E8;
        border-radius: 12px;
        padding: 1rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85rem;
        color: #00D4AA;
        overflow-x: auto;
    }
    
    .ai-response {
        background: linear-gradient(145deg, #1a2634, #0f1a24);
        border-left: 4px solid #00D4AA;
        border-radius: 0 12px 12px 0;
        padding: 1.5rem;
        margin: 1rem 0;
        color: #E8EDF2;
    }
    
    .feature-badge {
        display: inline-block;
        background: linear-gradient(90deg, #29B5E8, #00D4AA);
        color: #0D1B2A;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 0.2rem;
    }
    
    .snowflake-badge {
        background: linear-gradient(90deg, #29B5E8, #56CCF2);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .machine-card {
        background: linear-gradient(145deg, #1E2D3D, #162231);
        border: 1px solid #2E3A47;
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .machine-card:hover {
        border-color: #29B5E8;
        box-shadow: 0 8px 24px rgba(41, 181, 232, 0.2);
    }
    
    .status-ok { color: #00D4AA; }
    .status-warning { color: #FFB800; }
    .status-critical { color: #FF4757; }
    
    .stTextInput > div > div > input {
        background-color: #1E2D3D;
        color: white;
        border: 1px solid #29B5E8;
        border-radius: 8px;
    }
    
    .stSelectbox > div > div {
        background-color: #1E2D3D;
        color: white;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #29B5E8, #00D4AA);
        color: #0D1B2A;
        border: none;
        border-radius: 25px;
        font-weight: 600;
        padding: 0.5rem 2rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 24px rgba(41, 181, 232, 0.4);
    }
    
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0D1B2A, #162231);
        border-right: 1px solid #29B5E8;
    }
    
    .blueprint-container {
        background: #0a0f14;
        border: 2px solid #29B5E8;
        border-radius: 12px;
        padding: 1rem;
        position: relative;
    }
    
    .pulse-dot {
        width: 12px;
        height: 12px;
        background: #00D4AA;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(0, 212, 170, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(0, 212, 170, 0); }
        100% { box-shadow: 0 0 0 0 rgba(0, 212, 170, 0); }
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# DONNÉES MOCKÉES
# =============================================================================

MACHINES_DATA = {
    "CNC-2450": {
        "nom": "Centre d'usinage CNC-2450",
        "type": "Fraiseuse 5 axes",
        "fabricant": "DMG MORI",
        "annee": 2021,
        "statut": "Opérationnel",
        "heures_fonctionnement": 12450,
        "prochain_maintenance": "2026-02-15",
        "composants": ["Broche HSK-A63", "Table rotative NC", "Système de refroidissement", "Changeur d'outils 60 pos."]
    },
    "ROBOT-ARM-7": {
        "nom": "Bras Robotisé UR-7",
        "type": "Robot collaboratif",
        "fabricant": "Universal Robots",
        "annee": 2023,
        "statut": "Alerte",
        "heures_fonctionnement": 4820,
        "prochain_maintenance": "2026-01-20",
        "composants": ["Servomoteurs J1-J6", "Capteurs de couple", "Contrôleur CB5", "Effecteur terminal"]
    },
    "PRESS-H200": {
        "nom": "Presse Hydraulique H200",
        "type": "Presse 200 tonnes",
        "fabricant": "Schuler",
        "annee": 2019,
        "statut": "Maintenance requise",
        "heures_fonctionnement": 28900,
        "prochain_maintenance": "2026-01-10",
        "composants": ["Vérin principal", "Pompe hydraulique", "Bloc de distribution", "Capteurs de pression"]
    }
}

MAINTENANCE_HISTORY = pd.DataFrame({
    "Date": pd.date_range(start="2025-01-01", periods=50, freq="W"),
    "Machine": np.random.choice(list(MACHINES_DATA.keys()), 50),
    "Type": np.random.choice(["Préventive", "Corrective", "Prédictive"], 50, p=[0.5, 0.3, 0.2]),
    "Durée (h)": np.random.uniform(0.5, 8, 50).round(1),
    "Coût (€)": np.random.uniform(150, 5000, 50).round(0)
})

AI_SQL_EXAMPLES = {
    "Quelles pièces montrent des signes d'usure sur la CNC-2450?": {
        "sql": """-- Requête générée par Snowflake Cortex AI
SELECT 
    p.piece_id,
    p.nom_piece,
    p.zone_machine,
    m.niveau_usure_pct,
    m.derniere_inspection,
    CASE 
        WHEN m.niveau_usure_pct > 80 THEN 'CRITIQUE'
        WHEN m.niveau_usure_pct > 60 THEN 'ATTENTION'
        ELSE 'OK'
    END as statut_alerte
FROM MACHINES.PIECES p
JOIN MAINTENANCE.MESURES_USURE m 
    ON p.piece_id = m.piece_id
WHERE p.machine_id = 'CNC-2450'
    AND m.date_mesure = (
        SELECT MAX(date_mesure) 
        FROM MAINTENANCE.MESURES_USURE 
        WHERE piece_id = p.piece_id
    )
ORDER BY m.niveau_usure_pct DESC;""",
        "reponse": """🔍 **Analyse des pièces - CNC-2450**

D'après l'analyse des données de capteurs et l'historique de maintenance, voici les pièces présentant des signes d'usure:

| Pièce | Zone | Usure | Statut |
|-------|------|-------|--------|
| Broche HSK-A63 | Axe Z | 72% | ⚠️ ATTENTION |
| Roulement principal | Axe X | 45% | ✅ OK |
| Courroie transmission | Système | 68% | ⚠️ ATTENTION |
| Joint étanchéité | Refroidissement | 34% | ✅ OK |

**💡 Recommandation Cortex AI:** Planifier le remplacement de la broche dans les 500 prochaines heures de fonctionnement. Commande pièce suggérée: réf. HSK-A63-2450-R"""
    },
    "Prédiction de panne pour le robot UR-7": {
        "sql": """-- Analyse prédictive Snowflake ML
WITH sensor_trends AS (
    SELECT 
        sensor_id,
        AVG(valeur) as moyenne_7j,
        STDDEV(valeur) as ecart_type,
        ML_PREDICT(
            MODEL('maintenance_predictive_v3'),
            OBJECT_CONSTRUCT(
                'temperature', AVG(temp),
                'vibration', AVG(vibration),
                'couple', AVG(couple)
            )
        ) as prediction
    FROM IOT.SENSOR_DATA
    WHERE machine_id = 'ROBOT-ARM-7'
        AND timestamp > DATEADD('day', -7, CURRENT_TIMESTAMP)
    GROUP BY sensor_id
)
SELECT 
    sensor_id,
    prediction:failure_probability::FLOAT as proba_panne,
    prediction:estimated_days::INT as jours_restants,
    prediction:recommended_action::STRING as action
FROM sensor_trends
WHERE prediction:failure_probability > 0.3
ORDER BY proba_panne DESC;""",
        "reponse": """🤖 **Analyse Prédictive - Robot UR-7**

Le modèle ML Snowflake Cortex a analysé 2.4M de points de données capteurs sur les 30 derniers jours.

**⚠️ Alertes détectées:**

| Composant | Probabilité panne | Délai estimé | Action recommandée |
|-----------|------------------|--------------|-------------------|
| Servomoteur J3 | 67% | 12 jours | Remplacement préventif |
| Capteur couple J5 | 42% | 28 jours | Recalibration |
| Réducteur J2 | 35% | 45 jours | Surveillance accrue |

**📊 Tendances identifiées:**
- Augmentation vibrations J3: +23% sur 14 jours
- Température moteur J3: pics à 78°C (seuil: 75°C)
- Couple résiduel anormal détecté

**💰 Impact estimé si panne non anticipée:** 45 000€ (arrêt ligne + pièces urgentes)"""
    },
    "Optimiser le planning de maintenance ce trimestre": {
        "sql": """-- Optimisation planning avec Snowflake Cortex
WITH maintenance_scores AS (
    SELECT 
        m.machine_id,
        m.nom_machine,
        CORTEX.ANALYZE_MAINTENANCE_PRIORITY(
            m.machine_id,
            m.heures_fonctionnement,
            m.criticite_production,
            ARRAY_AGG(DISTINCT a.alerte_type)
        ) as priority_score,
        CORTEX.ESTIMATE_MAINTENANCE_WINDOW(
            m.machine_id,
            CURRENT_DATE,
            DATEADD('month', 3, CURRENT_DATE)
        ) as fenetre_optimale
    FROM MACHINES.EQUIPEMENTS m
    LEFT JOIN ALERTES.ACTIVES a ON m.machine_id = a.machine_id
    GROUP BY m.machine_id, m.nom_machine, 
             m.heures_fonctionnement, m.criticite_production
)
SELECT 
    machine_id,
    nom_machine,
    priority_score:score::INT as score_priorite,
    priority_score:reason::STRING as justification,
    fenetre_optimale:start_date::DATE as debut_maintenance,
    fenetre_optimale:duration_hours::INT as duree_estimee
FROM maintenance_scores
ORDER BY priority_score:score DESC;""",
        "reponse": """📅 **Planning Optimisé - Q1 2026**

Snowflake Cortex a analysé la criticité production, l'état des équipements et les contraintes calendaires.

**🎯 Planning recommandé:**

| Semaine | Machine | Intervention | Durée | Impact prod. |
|---------|---------|--------------|-------|--------------|
| S3 (Jan 13-17) | PRESS-H200 | Révision complète | 16h | Ligne B arrêt |
| S4 (Jan 20-24) | ROBOT-ARM-7 | Remplacement J3 | 4h | Minimal |
| S7 (Fév 10-14) | CNC-2450 | Maintenance préventive | 8h | Ligne A arrêt |

**📈 Gains estimés:**
- Réduction temps d'arrêt non planifié: -34%
- Économies pièces (achat groupé): 12 400€
- Optimisation main d'œuvre: 18h récupérées

**🔄 Synergies identifiées:** Commander ensemble réf. HSK-A63 et joints PRESS-H200 (même fournisseur, -8% négocié)"""
    },
    "Analyser le schéma technique de la presse hydraulique": {
        "sql": """-- Analyse documentaire avec Snowflake Document AI
SELECT 
    doc.document_id,
    doc.titre,
    CORTEX.DOCUMENT_PARSE(doc.contenu_pdf) as structure,
    CORTEX.EXTRACT_SPECIFICATIONS(
        doc.contenu_pdf,
        'hydraulic_press'
    ) as specs_extraites,
    CORTEX.FIND_RELATED_PROCEDURES(
        doc.document_id,
        'maintenance'
    ) as procedures_liees
FROM DOCUMENTATION.PLANS_TECHNIQUES doc
WHERE doc.machine_ref = 'PRESS-H200'
    AND doc.type_document = 'SCHEMA_HYDRAULIQUE';""",
        "reponse": """📐 **Analyse Schéma - Presse H200**

Document AI a analysé le plan hydraulique (réf: SCH-H200-HYD-v3.2)

**🔧 Spécifications extraites:**

| Paramètre | Valeur | Tolérance |
|-----------|--------|-----------|
| Pression max | 320 bar | ±5 bar |
| Débit pompe | 85 L/min | ±2 L/min |
| Volume réservoir | 450 L | - |
| Viscosité huile | ISO VG 46 | - |

**⚡ Points critiques identifiés:**
1. **Valve de surpression (V-03):** Réglage usine 340 bar - vérifier calibration
2. **Filtre retour (F-02):** Indicateur colmatage à surveiller
3. **Vérin principal:** Joint spy réf. OR-320-45 (usure typique à 25 000h)

**📚 Procédures liées:**
- PROC-H200-001: Purge circuit hydraulique
- PROC-H200-007: Remplacement joint vérin
- PROC-H200-012: Calibration pressostat

**🎓 Formation suggérée:** Module HYD-Advanced disponible dans Snowflake Training"""
    }
}

# =============================================================================
# FONCTIONS UTILITAIRES
# =============================================================================

def create_machine_status_chart():
    """Crée un graphique de statut des machines"""
    statuts = ["Opérationnel", "Alerte", "Maintenance requise"]
    couleurs = ["#00D4AA", "#FFB800", "#FF4757"]
    valeurs = [8, 3, 1]
    
    fig = go.Figure(data=[go.Pie(
        labels=statuts,
        values=valeurs,
        hole=0.6,
        marker_colors=couleurs,
        textinfo='label+value',
        textfont_size=12,
        textfont_color='white'
    )])
    
    fig.update_layout(
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=20, b=20, l=20, r=20),
        annotations=[dict(text='12<br>Machines', x=0.5, y=0.5, font_size=18, font_color='white', showarrow=False)]
    )
    return fig

def create_maintenance_trend():
    """Crée un graphique de tendance maintenance"""
    dates = pd.date_range(start="2025-01-01", periods=12, freq="M")
    preventive = [12, 15, 11, 14, 16, 13, 18, 15, 14, 17, 16, 19]
    corrective = [8, 6, 9, 5, 4, 7, 3, 4, 5, 3, 2, 2]
    predictive = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=preventive, name='Préventive', 
                             line=dict(color='#29B5E8', width=3), fill='tonexty'))
    fig.add_trace(go.Scatter(x=dates, y=corrective, name='Corrective', 
                             line=dict(color='#FF4757', width=3)))
    fig.add_trace(go.Scatter(x=dates, y=predictive, name='Prédictive (ML)', 
                             line=dict(color='#00D4AA', width=3, dash='dot')))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        legend=dict(orientation='h', yanchor='bottom', y=1.02),
        margin=dict(t=40, b=40, l=40, r=40),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    )
    return fig

def create_sensor_realtime():
    """Simule des données capteur temps réel"""
    times = pd.date_range(end=datetime.now(), periods=60, freq='1min')
    temp = 65 + np.cumsum(np.random.randn(60) * 0.5)
    vibration = 2.5 + np.cumsum(np.random.randn(60) * 0.1)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=times, y=temp, name='Température (°C)', 
                             line=dict(color='#FF6B35', width=2)))
    fig.add_trace(go.Scatter(x=times, y=vibration * 20, name='Vibration (mm/s)', 
                             line=dict(color='#29B5E8', width=2)))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        legend=dict(orientation='h', yanchor='bottom', y=1.02),
        margin=dict(t=40, b=40, l=40, r=40),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    )
    return fig

def display_machine_blueprint():
    """Affiche un schéma de machine stylisé en SVG"""
    svg = """
    <svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
        <!-- Base -->
        <rect x="50" y="200" width="300" height="60" fill="#1E2D3D" stroke="#29B5E8" stroke-width="2"/>
        
        <!-- Corps principal -->
        <rect x="80" y="80" width="240" height="120" fill="#162231" stroke="#29B5E8" stroke-width="2"/>
        
        <!-- Broche -->
        <rect x="170" y="40" width="60" height="50" fill="#2E3A47" stroke="#00D4AA" stroke-width="2"/>
        <circle cx="200" cy="50" r="15" fill="#0D1B2A" stroke="#29B5E8" stroke-width="2"/>
        
        <!-- Points de monitoring -->
        <circle cx="100" cy="120" r="8" fill="#00D4AA" opacity="0.8">
            <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
        </circle>
        <circle cx="200" cy="150" r="8" fill="#FFB800" opacity="0.8">
            <animate attributeName="opacity" values="0.4;1;0.4" dur="1.5s" repeatCount="indefinite"/>
        </circle>
        <circle cx="300" cy="120" r="8" fill="#00D4AA" opacity="0.8">
            <animate attributeName="opacity" values="0.4;1;0.4" dur="2.5s" repeatCount="indefinite"/>
        </circle>
        
        <!-- Labels -->
        <text x="100" y="105" fill="#8B9CAF" font-size="10" text-anchor="middle">AXE X</text>
        <text x="200" y="135" fill="#8B9CAF" font-size="10" text-anchor="middle">BROCHE</text>
        <text x="300" y="105" fill="#8B9CAF" font-size="10" text-anchor="middle">AXE Y</text>
        
        <!-- Indicateurs -->
        <rect x="320" y="90" width="25" height="15" fill="#162231" stroke="#00D4AA" stroke-width="1"/>
        <text x="332" y="101" fill="#00D4AA" font-size="8" text-anchor="middle">OK</text>
        
        <rect x="320" y="140" width="25" height="15" fill="#162231" stroke="#FFB800" stroke-width="1"/>
        <text x="332" y="151" fill="#FFB800" font-size="8" text-anchor="middle">72%</text>
    </svg>
    """
    return svg

# =============================================================================
# SIDEBAR
# =============================================================================

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <span style="font-size: 3rem;">❄️</span>
        <h2 style="margin: 0.5rem 0; background: linear-gradient(90deg, #29B5E8, #00D4AA); 
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            SnowMaintain AI
        </h2>
        <p style="color: #8B9CAF; font-size: 0.85rem;">Powered by Snowflake Cortex</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    page = st.radio(
        "Navigation",
        ["🏠 Dashboard", "🔍 AI SQL Query", "📐 Analyse Plans", "🤖 Assistant Maintenance", "📊 Analytics"],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    st.markdown("""
    <div style="padding: 1rem; background: linear-gradient(145deg, #1E2D3D, #162231); 
                border-radius: 12px; border: 1px solid #29B5E8;">
        <h4 style="color: #29B5E8; margin-bottom: 0.5rem;">🎯 Capacités démontrées</h4>
        <ul style="color: #8B9CAF; font-size: 0.8rem; padding-left: 1.2rem;">
            <li>Snowflake Cortex AI</li>
            <li>Document AI (OCR)</li>
            <li>ML Prédictif intégré</li>
            <li>Streaming IoT</li>
            <li>Natural Language SQL</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style="text-align: center; padding: 0.5rem;">
        <span class="snowflake-badge">
            <span>❄️</span> Snowflake Partner Demo
        </span>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# PAGES
# =============================================================================

if page == "🏠 Dashboard":
    # Header
    st.markdown('<h1 class="hero-title">SnowMaintain AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Plateforme intelligente de maintenance prédictive propulsée par Snowflake</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Métriques principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">12</div>
            <div class="metric-label">Machines connectées</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value" style="color: #00D4AA;">94.7%</div>
            <div class="metric-label">Disponibilité</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value" style="color: #FFB800;">3</div>
            <div class="metric-label">Alertes actives</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">2.4M</div>
            <div class="metric-label">Points données/jour</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Graphiques
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 📊 État du parc")
        st.plotly_chart(create_machine_status_chart(), use_container_width=True)
    
    with col2:
        st.markdown("### 📈 Évolution maintenance 2025")
        st.plotly_chart(create_maintenance_trend(), use_container_width=True)
    
    # Alertes
    st.markdown("### ⚠️ Alertes récentes")
    
    alert_col1, alert_col2, alert_col3 = st.columns(3)
    
    with alert_col1:
        st.markdown("""
        <div class="machine-card" style="border-left: 4px solid #FF4757;">
            <h4 style="color: #FF4757; margin: 0;">🔴 PRESS-H200</h4>
            <p style="color: #8B9CAF; margin: 0.5rem 0;">Maintenance échue depuis 3 jours</p>
            <span class="feature-badge" style="background: #FF4757;">CRITIQUE</span>
        </div>
        """, unsafe_allow_html=True)
    
    with alert_col2:
        st.markdown("""
        <div class="machine-card" style="border-left: 4px solid #FFB800;">
            <h4 style="color: #FFB800; margin: 0;">🟡 ROBOT-ARM-7</h4>
            <p style="color: #8B9CAF; margin: 0.5rem 0;">Vibration J3 +23% - Surveillance</p>
            <span class="feature-badge" style="background: #FFB800;">ATTENTION</span>
        </div>
        """, unsafe_allow_html=True)
    
    with alert_col3:
        st.markdown("""
        <div class="machine-card" style="border-left: 4px solid #FFB800;">
            <h4 style="color: #FFB800; margin: 0;">🟡 CNC-2450</h4>
            <p style="color: #8B9CAF; margin: 0.5rem 0;">Broche usure 72% - Planifier</p>
            <span class="feature-badge" style="background: #FFB800;">ATTENTION</span>
        </div>
        """, unsafe_allow_html=True)

elif page == "🔍 AI SQL Query":
    st.markdown("## 🔍 Interrogation AI SQL")
    st.markdown("""
    <p style="color: #8B9CAF;">
        Posez vos questions en langage naturel. <strong>Snowflake Cortex</strong> génère automatiquement 
        les requêtes SQL optimisées et analyse les résultats.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Sélecteur de questions prédéfinies
    question = st.selectbox(
        "💬 Sélectionnez une question ou tapez la vôtre",
        list(AI_SQL_EXAMPLES.keys()),
        index=0
    )
    
    custom_question = st.text_input(
        "Ou posez votre propre question...",
        placeholder="Ex: Quel est l'historique de pannes du robot?"
    )
    
    if st.button("🚀 Analyser avec Cortex AI", type="primary"):
        with st.spinner("🧠 Cortex AI analyse votre question..."):
            time.sleep(1.5)
        
        selected_question = custom_question if custom_question else question
        example = AI_SQL_EXAMPLES.get(question, list(AI_SQL_EXAMPLES.values())[0])
        
        st.markdown("### 📝 Requête SQL générée")
        st.markdown(f"""
        <div class="sql-box">
            <pre>{example['sql']}</pre>
        </div>
        """, unsafe_allow_html=True)
        
        with st.spinner("⚡ Exécution sur Snowflake..."):
            time.sleep(1)
        
        st.markdown("### 🎯 Réponse AI")
        st.markdown(f"""
        <div class="ai-response">
            {example['reponse']}
        </div>
        """, unsafe_allow_html=True)
        
        # Badges de fonctionnalités utilisées
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center;">
            <span class="feature-badge">Cortex LLM</span>
            <span class="feature-badge">Warehouse XS</span>
            <span class="feature-badge">12ms query time</span>
            <span class="feature-badge">Zero-copy clone</span>
        </div>
        """, unsafe_allow_html=True)

elif page == "📐 Analyse Plans":
    st.markdown("## 📐 Analyse de Plans Techniques")
    st.markdown("""
    <p style="color: #8B9CAF;">
        <strong>Snowflake Document AI</strong> extrait et analyse automatiquement les informations 
        des plans machines, schémas techniques et documentations PDF.
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🖼️ Schéma machine interactif")
        st.markdown(f"""
        <div class="blueprint-container">
            {display_machine_blueprint()}
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("💡 Cliquez sur les points lumineux pour voir les détails capteurs")
    
    with col2:
        st.markdown("### 📄 Documents analysés")
        
        doc_type = st.selectbox(
            "Type de document",
            ["Schéma hydraulique", "Plan électrique", "Manuel opérateur", "Fiche technique"]
        )
        
        machine = st.selectbox(
            "Machine",
            list(MACHINES_DATA.keys())
        )
        
        if st.button("🔍 Analyser le document", type="primary"):
            with st.spinner("📖 Document AI analyse le PDF..."):
                time.sleep(2)
            
            st.success("✅ Document analysé avec succès!")
            
            st.markdown("""
            <div class="ai-response">
                <h4>📋 Informations extraites</h4>
                <ul>
                    <li><strong>Référence:</strong> SCH-H200-HYD-v3.2</li>
                    <li><strong>Date création:</strong> 15/03/2019</li>
                    <li><strong>Dernière révision:</strong> 08/11/2024</li>
                    <li><strong>Composants identifiés:</strong> 47</li>
                    <li><strong>Procédures liées:</strong> 12</li>
                </ul>
                <h4>⚙️ Paramètres critiques détectés</h4>
                <table style="width: 100%; color: #E8EDF2;">
                    <tr><td>Pression service</td><td>250 bar</td></tr>
                    <tr><td>Pression max</td><td>320 bar</td></tr>
                    <tr><td>Température huile</td><td>40-60°C</td></tr>
                    <tr><td>Niveau mini réservoir</td><td>380L</td></tr>
                </table>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔗 Graphe de connaissances")
    
    # Graphe de relations
    fig = go.Figure()
    
    # Nodes
    nodes = ["PRESS-H200", "Vérin", "Pompe", "Valve", "Capteur P1", "Capteur P2", "PROC-001", "PROC-007"]
    x = [0, -1, 1, 0, -1.5, 1.5, -0.5, 0.5]
    y = [0, -1, -1, -1.5, -0.5, -0.5, -2, -2]
    colors = ["#29B5E8", "#00D4AA", "#00D4AA", "#00D4AA", "#FFB800", "#FFB800", "#FF6B35", "#FF6B35"]
    
    # Edges
    for i in range(1, len(nodes)):
        fig.add_trace(go.Scatter(
            x=[x[0], x[i]], y=[y[0], y[i]],
            mode='lines',
            line=dict(color='rgba(41,181,232,0.3)', width=2),
            showlegend=False
        ))
    
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='markers+text',
        marker=dict(size=30, color=colors),
        text=nodes,
        textposition='top center',
        textfont=dict(color='white', size=10),
        showlegend=False
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        margin=dict(t=20, b=20, l=20, r=20),
        height=300
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif page == "🤖 Assistant Maintenance":
    st.markdown("## 🤖 Assistant Maintenance IA")
    st.markdown("""
    <p style="color: #8B9CAF;">
        Votre copilote intelligent pour la maintenance. Posez vos questions techniques, 
        demandez des procédures ou des diagnostics.
    </p>
    """, unsafe_allow_html=True)
    
    # Chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "👋 Bonjour! Je suis votre assistant maintenance propulsé par **Snowflake Cortex**. Comment puis-je vous aider aujourd'hui?\n\n*Exemples de questions:*\n- Comment purger le circuit hydraulique de la PRESS-H200?\n- Quelle est la procédure de calibration du robot UR-7?\n- Diagnostic: la CNC fait un bruit anormal à haute vitesse"}
        ]
    
    # Display messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Posez votre question technique..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("🧠 Analyse en cours..."):
                time.sleep(1.5)
            
            # Réponse simulée intelligente
            responses = {
                "purge": """### 🔧 Procédure de purge - Circuit hydraulique PRESS-H200

**Prérequis:**
- Machine à l'arrêt depuis >30 min
- Température huile < 40°C
- EPI: gants, lunettes

**Étapes:**

1. **Dépressurisation** (⚠️ CRITIQUE)
   - Couper alimentation électrique
   - Actionner 5x la pédale pour évacuer pression résiduelle
   - Vérifier manomètre M1 = 0 bar

2. **Vidange circuit**
   - Ouvrir vanne V-12 (bas réservoir)
   - Collecter huile usagée (~420L)
   - Inspecter visuellement (particules, émulsion)

3. **Remplissage & purge**
   - Fermer V-12, ouvrir purge P1 et P2
   - Remplir huile neuve ISO VG 46
   - Purger jusqu'à absence de bulles

**📎 Documents liés:** PROC-H200-001, Fiche sécurité FS-HYD-003

*Source: Documentation Schuler analysée par Document AI*""",
                
                "calibration": """### 🎯 Calibration Robot UR-7 - Procédure complète

**Durée estimée:** 45 minutes

**Outils requis:**
- Teach pendant UR
- Cible calibration TCP
- Pied à coulisse digital

**Étapes:**

1. **Position Home**
   ```
   Move → Home Position → Confirm
   ```

2. **Calibration TCP (Tool Center Point)**
   - Installer cible sur effecteur
   - Menu: Installation → TCP
   - Méthode 4 points recommandée

3. **Calibration axes**
   - Pour chaque joint J1-J6:
     - Position 0° mécanique
     - Encoder reset si écart >0.1°

4. **Vérification**
   - Programme test `CAL_CHECK.urp`
   - Tolérance: ±0.05mm sur cible

**⚠️ Attention:** Recalibrer après tout impact ou changement d'outil

*Analyse Cortex: Dernière calibration il y a 89 jours - dans les normes*""",
                
                "bruit": """### 🔊 Diagnostic: Bruit anormal CNC-2450

**Analyse basée sur vos données capteurs (dernières 24h):**

| Paramètre | Valeur | Seuil | Statut |
|-----------|--------|-------|--------|
| Vibration X | 4.2 mm/s | 3.5 mm/s | ⚠️ |
| Vibration Y | 2.1 mm/s | 3.5 mm/s | ✅ |
| Fréquence dominante | 847 Hz | - | 📊 |
| Température broche | 68°C | 75°C | ✅ |

**🎯 Diagnostic probable:**

La fréquence de 847 Hz correspond à la **fréquence de rotation du roulement avant** de la broche à 12,000 RPM.

**Causes possibles (par probabilité):**
1. **Usure roulement broche (78%)** - Cohérent avec 12,450h de fonctionnement
2. **Balourd porte-outil (15%)** - Vérifier le faux-rond
3. **Desserrage fixation (7%)** - Contrôler couples de serrage

**📋 Actions recommandées:**
1. Réduire vitesse broche à 8,000 RPM en attendant
2. Commander roulement SKF 7014 (délai 5j)
3. Planifier intervention S7 (créneaux disponibles)

*Voulez-vous que je génère un bon de commande ou réserve un créneau maintenance?*"""
            }
            
            # Trouver la meilleure réponse
            response = "Je vais analyser votre question avec les données disponibles dans Snowflake...\n\n"
            
            prompt_lower = prompt.lower()
            if "purge" in prompt_lower or "hydraulique" in prompt_lower:
                response = responses["purge"]
            elif "calibr" in prompt_lower or "robot" in prompt_lower:
                response = responses["calibration"]
            elif "bruit" in prompt_lower or "cnc" in prompt_lower or "anormal" in prompt_lower:
                response = responses["bruit"]
            else:
                response = f"""### 🔍 Recherche en cours...

J'ai analysé votre question: *"{prompt}"*

**Sources consultées:**
- 📚 Documentation technique (2,847 documents)
- 📊 Historique maintenance (15,420 interventions)
- 📡 Données capteurs temps réel (2.4M points/jour)
- 🧠 Base de connaissances Cortex

**Résultat:**

Je n'ai pas trouvé de correspondance exacte, mais voici des suggestions:

1. Reformulez avec le nom exact de la machine (CNC-2450, ROBOT-ARM-7, PRESS-H200)
2. Précisez le type d'intervention (préventive, diagnostic, procédure)
3. Ajoutez des symptômes observés si c'est un problème

*💡 Tip: Essayez "Comment purger le circuit hydraulique?" ou "Diagnostic bruit CNC"*"""
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

elif page == "📊 Analytics":
    st.markdown("## 📊 Analytics & Insights")
    st.markdown("""
    <p style="color: #8B9CAF;">
        Tableaux de bord temps réel alimentés par <strong>Snowflake Snowsight</strong> 
        avec refresh automatique et partage sécurisé.
    </p>
    """, unsafe_allow_html=True)
    
    # Filtres
    col1, col2, col3 = st.columns(3)
    with col1:
        periode = st.selectbox("Période", ["7 derniers jours", "30 derniers jours", "90 derniers jours", "12 mois"])
    with col2:
        machines = st.multiselect("Machines", list(MACHINES_DATA.keys()), default=list(MACHINES_DATA.keys()))
    with col3:
        refresh = st.button("🔄 Rafraîchir")
    
    st.markdown("---")
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    
    metrics = [
        ("MTBF", "847h", "+12%", "Mean Time Between Failures"),
        ("MTTR", "2.3h", "-18%", "Mean Time To Repair"),
        ("OEE", "87.4%", "+5.2%", "Overall Equipment Effectiveness"),
        ("Coût/Machine", "1,240€", "-8%", "Coût maintenance mensuel moyen")
    ]
    
    for col, (label, value, delta, desc) in zip([col1, col2, col3, col4], metrics):
        with col:
            color = "#00D4AA" if "+" in delta or "-" in delta and "Coût" in label else "#00D4AA"
            if "-" in delta and "Coût" not in label:
                color = "#FF4757"
            st.metric(label=label, value=value, delta=delta, help=desc)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Graphiques avancés
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌡️ Données capteurs temps réel")
        st.plotly_chart(create_sensor_realtime(), use_container_width=True)
    
    with col2:
        st.markdown("### 📉 Coûts par type de maintenance")
        
        costs_data = pd.DataFrame({
            "Type": ["Préventive", "Corrective", "Prédictive"],
            "Coût (€)": [45000, 78000, 12000],
            "Interventions": [156, 42, 28]
        })
        
        fig = px.bar(
            costs_data, 
            x="Type", 
            y="Coût (€)",
            color="Type",
            color_discrete_map={
                "Préventive": "#29B5E8",
                "Corrective": "#FF4757",
                "Prédictive": "#00D4AA"
            }
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white',
            showlegend=False,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Tableau détaillé
    st.markdown("### 📋 Historique des interventions")
    
    # Style du dataframe
    st.dataframe(
        MAINTENANCE_HISTORY.tail(10).style.background_gradient(subset=['Durée (h)'], cmap='Blues'),
        use_container_width=True,
        hide_index=True
    )
    
    # Export
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        st.download_button(
            "📥 Export CSV",
            MAINTENANCE_HISTORY.to_csv(index=False),
            "maintenance_export.csv",
            "text/csv"
        )
    with col2:
        st.button("📧 Partager rapport")

# =============================================================================
# FOOTER
# =============================================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #8B9CAF;">
    <p>
        <strong>SnowMaintain AI</strong> - Démonstration des capacités Snowflake<br>
        <span style="font-size: 0.8rem;">
            Cortex AI • Document AI • Snowpark • Snowsight • Dynamic Tables • Streamlit in Snowflake
        </span>
    </p>
    <p style="font-size: 0.75rem; margin-top: 1rem;">
        ❄️ Propulsé par <strong>Snowflake Data Cloud</strong> | 
        🔒 Sécurité enterprise-grade | 
        ⚡ Performance élastique
    </p>
</div>
""", unsafe_allow_html=True)

