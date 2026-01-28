import streamlit as st
import random
import time

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Love Game", page_icon="🔥")

# --- CSS PER PULIZIA GRAFICA ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden !important;}
            header {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            .stAppDeployButton {display: none !important;}
            [data-testid="stStatusWidget"] {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- TITOLO ---
st.title("🔥 I Dadi del Destino")
st.write("Azione piccante o Penalità tremenda? Tenta la fortuna...")
st.divider()

# --- LISTE PERSONALIZZABILI ---
# Modifica queste frasi come preferisci!

azioni = [
    "Dai un bacio appassionato su...",
    "Fai un massaggio di 2 minuti a...",
    "Sussurra una cosa sporca a...",
    "Usa la lingua su...",
    "Mordicchia delicatamente...",
    "Accarezza lentamente...",
    "Lecca via un po' di panna/cioccolato da..."
]

zone = [
    "Collo",
    "Orecchio",
    "Schiena",
    "Interno coscia",
    "Piedi",
    "Ombelico",
    "Dove preferisce il partner"
]

bonus_extra = [
    "Bendando il partner 🙈",
    "Usando un cubetto di ghiaccio 🧊",
    "Senza usare le mani 🚫🖐️",
    "Con la luce spenta 🌑",
    "Mentre il partner ti guarda negli occhi 👀"
]

# --- LE PENALITÀ (CATTIVE!) ---
penalita_lui = [
    "⛔ SEI IL SUO SCHIAVO: Per 2 minuti devi fare tutto ciò che lei ordina.",
    "⛔ STOP: Non puoi toccarla per 3 minuti (ma lei può toccare te).",
    "⛔ STRIP: Togliti un indumento a sua scelta.",
    "⛔ APRI IL FRIGO: Vai a prepararle un drink o uno snack.",
    "⛔ BENDA: Fatti bendare e rimani immobile per 2 turni."
]

penalita_lei = [
    "⛔ SEI LA SUA SCHIAVA: Per 2 minuti devi fare tutto ciò che lui ordina.",
    "⛔ STOP: Non puoi toccarlo per 3 minuti (ma lui può toccare te).",
    "⛔ STRIP: Togliti un indumento a sua scelta.",
    "⛔ SPETTACOLO: Improvvisa un ballo sexy per 30 secondi.",
    "⛔ BENDA: Fatti bendare e rimani immobile per 2 turni."
]

# --- SELEZIONE GIOCATORE ---
col1, col2 = st.columns(2)
with col1:
    # Usiamo un radio button per decidere di chi è il turno
    giocatore = st.radio("Di chi è il turno?", ["Tocca a LUI 👨", "Tocca a LEI 👩"])

st.divider()

# --- IL MOTORE DEL GIOCO ---
if st.button("🎲 LANCIA I DADI 🎲", type="primary", use_container_width=True):
    
    # 1. Suspense (Barra caricamento)
    progress_text = "Il destino sta decidendo..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01) # Velocità dell'animazione
        my_bar.progress(percent_complete + 1, text=progress_text)
    my_bar.empty()
    
    # 2. Calcolo Probabilità: Sarà una Penalità? (15% di probabilità)
    # random.random() genera un numero tra 0.0 e 1.0. Se è minore di 0.15 scatta la penalità.
    if random.random() < 0.15:
        # --- CASO PENALITÀ ---
        
        # Scegliamo la lista giusta in base al giocatore
        if "LUI" in giocatore:
            penitenza = random.choice(penalita_lui)
        else:
            penitenza = random.choice(penalita_lei)
        
        # Mostriamo il box ROSSO (error)
        st.error("😱 OH NO! PENALITÀ!")
        st.header(penitenza)
        st.caption("E non puoi rifiutarti!")
        
    else:
        # --- CASO NORMALE ---
        
        azione_estratta = random.choice(azioni)
        zona_estratta = random.choice(zone)
        
        st.success("✅ Via libera!")
        st.subheader(f"{azione_estratta}")
        st.header(f"👉 {zona_estratta}")
        
        # 20% di probabilità di BONUS extra
        if random.random() < 0.20:
            bonus = random.choice(bonus_extra)
            st.warning(f"🔥 **BONUS:** {bonus}")

# --- Footer ---
st.divider()
st.caption("Divertitevi con prudenza 😉")
