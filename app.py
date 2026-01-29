import streamlit as st
import random
import time

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Secret Game", page_icon="🔞")

# CSS per nascondere tutto e rendere l'app bellissima
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    [data-testid="stStatusWidget"] {visibility: hidden;}
    .stButton>button {width: 100%; border-radius: 20px; height: 3em; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

# --- INIZIALIZZAZIONE MEMORIA (Session State) ---
# Questo serve a far sì che l'app non dimentichi la sfida estratta
if 'sfida_estratta' not in st.session_state:
    st.session_state.sfida_estratta = None
if 'livello_estratto' not in st.session_state:
    st.session_state.livello_estratto = None

st.title("🔞 Secret Game")
st.write("Scegli l'intensità e lancia i dadi.")

# --- LISTE AZIONI ---
azioni_standard = [
    "Fai un massaggio di 2 minuti sulle spalle del partner 💆‍♂️",
    "Bacia il partner in 3 punti diversi del viso 💋",
    "Sussurra un segreto imbarazzante all'orecchio 👂",
    "Fai uno spuntino sexy dividendo un frutto con la bocca 🍓",
    "Balla un lento (senza musica) abbracciati stretti 💃"
]

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

# BOTTONE DI ESTRAZIONE
if st.button("🎲 ESTRAI LA SFIDA 🎲", type="primary"):
    with st.spinner("Il destino sta scegliendo..."):
        time.sleep(1) # Effetto suspense
    
    # Salviamo il risultato nella "memoria" (session_state)
    st.session_state.livello_estratto = livello
    if "Standard" in livello:
        st.session_state.sfida_estratta = random.choice(azioni_standard)
    else:
        st.session_state.sfida_estratta = random.choice(azioni_bollino_rosso)

# --- VISUALIZZAZIONE RISULTATO ---
# Se c'è qualcosa in memoria, lo mostriamo
if st.session_state.sfida_estratta:
    st.divider()
    
    if "Standard" in st.session_state.livello_estratto:
        st.success("✨ SFIDA STANDARD")
        st.markdown(f"<h2 style='text-align: center;'>{st.session_state.sfida_estratta}</h2>", unsafe_allow_html=True)
    else:
        st.error("🔥 BOLLINO ROSSO!")
        # Testo grande, rosso e centrato
        st.markdown(f"""
            <div style="background-color: #ff4b4b22; padding: 20px; border-radius: 15px; border: 2px solid #ff4b4b;">
                <h1 style="text-align: center; color: #ff4b4b; font-size: 40px;">{st.session_state.sfida_estratta}</h1>
            </div>
            """, unsafe_allow_html=True)
    
    # Bottone per pulire lo schermo
    if st.button("❌ Cancella risultato"):
        st.session_state.sfida_estratta = None
        st.rerun()

st.divider()
st.caption("Creato per momenti privati. Divertitevi!")
