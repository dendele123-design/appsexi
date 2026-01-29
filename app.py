import streamlit as st
import random
import time

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Secret Game", page_icon="🔞")

# CSS Aggressivo per nascondere tutto il superfluo
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    [data-testid="stStatusWidget"] {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("🔞 Secret Game: The Dice")
st.write("Solo per adulti. Scegli il livello di sfida.")
st.divider()

# ==========================================
#      LE TUE LISTE DI AZIONI COMPLETE
# ==========================================

azioni_standard = [
    "Fai un massaggio di 2 minuti sulle spalle del partner 💆‍♂️",
    "Bacia il partner in 3 punti diversi del viso 💋",
    "Sussurra un segreto imbarazzante all'orecchio 👂",
    "Fai uno spuntino sexy dividendo un frutto con la bocca 🍓",
    "Balla un lento (senza musica) abbracciati stretti 💃"
]

# QUI AGGIUNGERAI LE TUE COSE "BOLLINO ROSSO"
azioni_bollino_rosso = [
    "Usa la tua cinta per legare le mani del partner ⛓️",
    "Passa un cubetto di ghiaccio ovunque lei/lui desideri 🧊",
    "Togli un indumento al partner usando solo i denti 🦷",
    "Fai uno striptease integrale al ritmo della tua canzone preferita 🎶",
    "Sperimenta una nuova posizione per 1 minuto (vestiti) 🔥"
]

# --- INTERFACCIA ---

livello = st.select_slider(
    "Seleziona l'intensità:",
    options=["Standard 😇", "Bollino Rosso 🔥"]
)

st.divider()

if st.button("ESTRAI LA SFIDA 🎲", type="primary", use_container_width=True):
    
    # Animazione suspense
    with st.spinner("Il destino sta scegliendo..."):
        time.sleep(1.2)
    
    # Scelta della lista in base allo slider
    if "Standard" in livello:
        sfida = random.choice(azioni_standard)
        st.success("✨ SFIDA STANDARD")
        st.header(sfida)
    else:
        sfida = random.choice(azioni_bollino_rosso)
        # Usiamo un box rosso per il bollino rosso
        st.error("🔥 BOLLINO ROSSO!")
        st.markdown(f"<h1 style='text-align: center; color: #ff4b4b;'>{sfida}</h1>", unsafe_allow_html=True)

st.divider()
st.caption("Usa questa app responsabilmente in un ambiente privato.")
