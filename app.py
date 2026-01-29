import streamlit as st
import random
import time

# --- CONFIGURAZIONE E CSS (Soliti) ---
st.set_page_config(page_title="Love Game", page_icon="🔥")
hide_st_style = """<style>#MainMenu {visibility: hidden !important;} header {visibility: hidden !important;} footer {visibility: hidden !important;} .stAppDeployButton {display: none !important;} [data-testid="stStatusWidget"] {visibility: hidden !important;}</style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("🔥 I Dadi del Destino 2.0")
st.write("Logica migliorata: le azioni ora hanno senso!")
st.divider()

# ==========================================
#      NUOVA LOGICA DELLE LISTE
# ==========================================

# --- LISTE PER LUI (Lui agisce su Lei) ---
azioni_semplici_lui = ["Bacia...", "Lecca...", "Accarezza...", "Mordi piano...", "Sussurra qualcosa su..."]
zone_lei = ["Collo", "Seno", "Interno coscia", "Orecchio", "Ombelico"]

azioni_complete_lui = [
    "Usa la cinta (delicatamente) sul suo sedere 🍑",
    "Passa un cubetto di ghiaccio sulla sua pancia 🧊",
    "Falle uno striptease integrale 🕺",
    "Benda lei e falle assaggiare qualcosa di dolce 🍬"
]

# --- LISTE PER LEI (Lei agisce su Lui) ---
azioni_semplici_lei = ["Bacia...", "Lecca...", "Graffia...", "Mordi...", "Accarezza con le unghie..."]
zone_lui = ["Collo", "Pettorali", "Addominali", "Schiena", "Barba"]

azioni_complete_lei = [
    "Usa la cinta per legargli le mani (se lui vuole) ⛓️",
    "Versa una goccia di vino sul suo petto e lecca via 🍷",
    "Fagli un massaggio con l'olio sulla schiena 🧴",
    "Siediti sopra di lui e guardalo negli occhi per 1 minuto 👀"
]

# --- PENALITÀ ---
penalita_lui = ["⛔ Fai tutto quello che lei ti ordina per 2 min", "⛔ Togliti 2 indumenti"]
penalita_lei = ["⛔ Fai tutto quello che lui ti ordina per 2 min", "⛔ Togliti 2 indumenti"]

# ==========================================

# --- SELEZIONE GIOCATORE ---
giocatore = st.radio("Di chi è il turno?", ["Tocca a LUI 👨", "Tocca a LEI 👩"], horizontal=True)
st.divider()

if st.button("🎲 LANCIA I DADI 🎲", type="primary", use_container_width=True):
    
    # Animazione suspense
    progress_text = "Il destino sta scegliendo un'azione sensata..."
    my_bar = st.progress(0, text=progress_text)
    for p in range(100):
        time.sleep(0.01)
        my_bar.progress(p + 1, text=progress_text)
    my_bar.empty()

    # --- LOGICA DI ESTRAZIONE SMART ---
    
    scelta_tipo = random.random() # Genera numero tra 0 e 1

    if scelta_tipo < 0.15:
        # 1. PENALITÀ (15% di probabilità)
        res = random.choice(penalita_lui if "LUI" in giocatore else penalita_lei)
        st.error(f"😱 PENALITÀ!\n\n{res}")

    elif scelta_tipo < 0.50:
        # 2. AZIONE COMPLETA (35% di probabilità: da 0.15 a 0.50)
        # Queste sono le frasi tipo "Usa la cinta sul sedere"
        res = random.choice(azioni_complete_lui if "LUI" in giocatore else azioni_complete_lei)
        st.success("✅ AZIONE SPECIALE!")
        st.header(res)

    else:
        # 3. AZIONE SEMPLICE + ZONA (50% di probabilità)
        # Queste sono le classiche "Bacia" + "Collo"
        if "LUI" in giocatore:
            act = random.choice(azioni_semplici_lui)
            body = random.choice(zone_lei)
        else:
            act = random.choice(azioni_semplici_lei)
            body = random.choice(zone_lui)
            
        st.success("✅ AZIONE NORMALE")
        st.subheader(act)
        st.header(f"👉 {body}")

st.divider()
st.caption("Ora le azioni sono divise tra semplici e complete per evitare 'errori' anatomici!")
