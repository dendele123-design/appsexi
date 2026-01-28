import streamlit as st
import random
import time

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Love Game", page_icon="🔥")

# --- CSS (NO MENU) ---
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

# ==========================================
#      AREA DI PERSONALIZZAZIONE LISTE
# ==========================================

# ------------------------------------------
# SCENARIO A: TOCCA A LUI (Lui agisce su di Lei)
# ------------------------------------------
azioni_turno_lui = [
    "Dai un bacio lungo su...",
    "Massaggia delicatamente...",
    "Usa la lingua su...",
    "Sussurra qualcosa all'orecchio mentre tocchi...",
    "Mordi piano..."
]

zone_su_lei = [
    "Collo",
    "Seno",
    "Interno coscia",
    "Lobo dell'orecchio",
    "Fianchi",
    "Dove lei preferisce"
]

# ------------------------------------------
# SCENARIO B: TOCCA A LEI (Lei agisce su di Lui)
# ------------------------------------------
azioni_turno_lei = [
    "Bacia con passione...",
    "Graffia leggermente...",
    "Accarezza con le unghie...",
    "Lecca via un po' di panna da...",
    "Stringi con le mani..."
]

zone_su_lui = [
    "Collo",
    "Pettorali",
    "Addominali",
    "Interno coscia",
    "Schiena",
    "Dove lui preferisce"
]

# ------------------------------------------
# BONUS E PENALITÀ (Validi per tutti o divisi)
# ------------------------------------------
bonus_extra = [
    "Bendando il partner 🙈",
    "Usando un cubetto di ghiaccio 🧊",
    "Senza usare le mani 🚫🖐️",
    "Con la luce spenta 🌑",
    "Mentre ti guarda negli occhi 👀"
]

penalita_per_lui = [
    "⛔ SEI IL SUO SCHIAVO: Per 2 minuti devi fare tutto ciò che lei ordina.",
    "⛔ STOP: Non puoi toccarla per 3 minuti.",
    "⛔ STRIP: Togliti un indumento a sua scelta.",
    "⛔ COCKTAIL: Vai a prepararle da bere."
]

penalita_per_lei = [
    "⛔ SEI LA SUA SCHIAVA: Per 2 minuti devi fare tutto ciò che lui ordina.",
    "⛔ STOP: Non puoi toccarlo per 3 minuti.",
    "⛔ STRIP: Togliti un indumento a sua scelta.",
    "⛔ SPETTACOLO: Ballo sexy per 30 secondi."
]

# ==========================================
#      FINE AREA PERSONALIZZAZIONE
# ==========================================

# --- SELEZIONE GIOCATORE ---
col1, col2 = st.columns(2)
with col1:
    giocatore = st.radio("Di chi è il turno (Chi agisce)?", ["Tocca a LUI 👨", "Tocca a LEI 👩"])

st.divider()

# --- MOTORE DI GIOCO ---
if st.button("🎲 LANCIA I DADI 🎲", type="primary", use_container_width=True):
    
    # Animazione
    progress_text = "Il destino sta decidendo..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    my_bar.empty()
    
    # --- LOGICA DI ESTRAZIONE ---
    
    # 1. Controlliamo se scatta la PENALITÀ (15% probabilità)
    if random.random() < 0.15:
        if "LUI" in giocatore:
            penitenza = random.choice(penalita_per_lui)
        else:
            penitenza = random.choice(penalita_per_lei)
            
        st.error("😱 OH NO! PENALITÀ!")
        st.header(penitenza)
        
    else:
        # 2. Se non è penalità, scegliamo AZIONE + ZONA in base a chi gioca
        if "LUI" in giocatore:
            # Tocca a Lui -> Usa le liste per Lui
            azione = random.choice(azioni_turno_lui)
            zona = random.choice(zone_su_lei)
        else:
            # Tocca a Lei -> Usa le liste per Lei
            azione = random.choice(azioni_turno_lei)
            zona = random.choice(zone_su_lui)
            
        st.success("✅ Via libera!")
        st.subheader(f"{azione}")
        st.header(f"👉 {zona}")
        
        # 3. Bonus Extra (20% probabilità)
        if random.random() < 0.20:
            bonus = random.choice(bonus_extra)
            st.warning(f"🔥 **BONUS:** {bonus}")

# --- FOOTER ---
st.divider()
st.caption("Buon divertimento!")
