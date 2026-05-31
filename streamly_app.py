
```python
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Configuration de la page
st.set_page_config(page_title="Logix Audit - Douala", layout="wide", page_icon="🚛")

st.title("🚛 Logix Audit & Performance")
st.subheader("Outil d'évaluation Supply Chain & Simulation de Congestion")
st.markdown("---")

# Navigation principale
page = st.sidebar.radio("Navigation", ["Formulaire d'Audit", "Dashboard Performance", "Simulateur de Congestion"])

# --- MODELE DE DONNÉES SIMPLIFIÉ ---
if 'scores' not in st.session_state:
    st.session_state.scores = {"Planification": 3, "CAMCIS & Douanes": 2, "Corridors & Transport": 4, "Gestion des Parcs": 3}

if page == "Formulaire d'Audit":
    st.header("📋 Évaluation SCOR Adaptée au Contexte de Douala")
    st.write("Répondez aux questions pour évaluer la maturité logistique.")
    
    # Curseurs pour l'audit
    st.session_state.scores["Planification"] = st.slider("Maturité Planification (S&OP, Prévisions)", 1, 5, st.session_state.scores["Planification"])
    st.session_state.scores["CAMCIS & Douanes"] = st.slider("Fluidité passages douaniers (CAMCIS)", 1, 5, st.session_state.scores["CAMCIS & Douanes"])
    st.session_state.scores["Corridors & Transport"] = st.slider("Sécurisation des Corridors (Douala-N'Djaména / Bangui)", 1, 5, st.session_state.scores["Corridors & Transport"])
    st.session_state.scores["Gestion des Parcs"] = st.slider("Optimisation des Parcs à bois / Conteneurs", 1, 5, st.session_state.scores["Gestion des Parcs"])
    
    st.success("✅ Vos réponses ont été enregistrées ! Passez à l'onglet Dashboard pour voir l'analyse.")

elif page == "Dashboard Performance":
    st.header("📊 Analyse de la Maturité")
    
    # Création du graphique en Radar
    df = pd.DataFrame(dict(
        Axe=list(st.session_state.scores.keys()),
        Score=list(st.session_state.scores.values())
    ))
    fig = px.line_polar(df, r='Score', theta='Axe', line_close=True, range_r=[0,5], title="Profil de Maturité Logistique")
    fig.update_traces(fill='adjacent')
    st.plotly_chart(fig, use_container_width=True)

elif page == "Simulateur de Congestion":
    st.header("📈 Simulateur Financier de Congestion (Loi Quadratique)")
    st.write("Visualisez l'explosion des coûts de stockage lorsque le volume dépasse la capacité critique du parc.")
    
    # Inputs en FCFA et Volumes
    capacite = st.number_input("Capacité nominale du parc (en EVP ou m³)", value=1000)
    volume_actuel = st.slider("Volume de marchandises entrant", 500, 2000, 1100)
    
    # Calcul mathématique quadratique
    x = np.linspace(500, 2000, 100)
    y = 5000 * (x - capacite)**2 + 1500000
    
    cost_actual = 5000 * (volume_actuel - capacite)**2 + 1500000 if volume_actuel > capacite else 1500000
    
    # Graphique de la courbe
    df_chart = pd.DataFrame({'Volume': x, 'Coût Total (FCFA)': y})
    fig_curve = px.line(df_chart, x='Volume', y='Coût Total (FCFA)', title="Courbe d'explosion des coûts de surestaries")
    fig_curve.add_scatter(x=[volume_actuel], y=[cost_actual], mode='markers+text', text=["Votre Position"], name="Position Actuelle", marker=dict(size=12, color='red'))
    
    st.plotly_chart(fig_curve, use_container_width=True)
    st.metric(label="Coût estimé des surestaries / pénalités", value=f"{int(cost_actual):,} FCFA")
```

