import streamlit as st
import random
import time

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Love Game", page_icon="🔥")

# CSS per nascondere i menu (come prima)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- TITOLO ---
st.title("🔥 I Dadi del Destino")
st.write("Cosa succederà stasera? Lascia decidere al caso...")
st.divider()

# --- LE LISTE (DA PERSONALIZZARE!) ---
# Qui è dove devi mettere la tua fantasia. 
# Io metto cose soft, tu puoi scrivere quello che vuoi.

azioni = [
    "Dai un bacio appassionato su...",
    "Fai un massaggio di 2 minuti a...",
    "Sussurra una cosa sporca a...",
    "Usa un cubetto di ghiaccio su...",
    "Mordicchia delicatamente...",
    "Accarezza lentamente..."
]

zone = [
    "Collo",
    "Orecchio",
    "Schiena",
    "Interno coscia",
    "Piedi",
    "Dove preferisce il partner"
]

bonus = [
    "Bendando il partner 🙈",
    "Usando un filo d'olio o crema 🧴",
    "Senza usare le mani 🚫🖐️",
    "Con la luce spenta 🌑",
    "Mentre suona la vostra canzone 🎵"
]

# --- IL GIOCO ---

col1, col2 = st.columns(2)
with col1:
    giocatore = st.radio("Chi tocca?", ["Tocca a LUI 👨", "Tocca a LEI 👩"], horizontal=True)

st.divider()

if st.button("🎲 LANCIA I DADI 🎲", type="primary", use_container_width=True):
    
    # Effetto "suspense" (barra di caricamento)
    progress_text = "Estrazione in corso..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01) # Velocità caricamento
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    my_bar.empty() # Cancella la barra
    
    # Estrazione Casuale (La magia di Python)
    azione_estratta = random.choice(azioni)
    zona_estratta = random.choice(zone)
    
    # 20% di possibilità di avere un bonus extra
    if random.random() < 0.2:
        bonus_estratto = random.choice(bonus)
        testo_bonus = f"\n\n🔥 **BONUS:** {bonus_estratto}"
    else:
        testo_bonus = ""

    # Mostra il risultato
    st.success(f"Il dado ha deciso!")
    st.header(f"{azione_estratta}")
    st.header(f"👉 {zona_estratta}")
    
    if testo_bonus:
        st.warning(testo_bonus)

# --- NOTE ---
st.divider()
st.caption("Regole: Chi si rifiuta deve bere uno shot! (Usa l'altra app per tracciarlo 😉)")
