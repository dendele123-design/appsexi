import streamlit as st
import random
import time

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Secret Game", page_icon="🔞")

# CSS per pulizia totale e stile bottoni
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    [data-testid="stStatusWidget"] {visibility: hidden;}
    
    /* Stile personalizzato per i bottoni */
    div.stButton > button:first-child {
        height: 3em;
        font-size: 20px;
        font-weight: bold;
        border-radius: 15px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔞 Secret Game")
st.write("Scegli chi gioca e il livello di sfida.")

# ==========================================
#        LE 4 LISTE DI AZIONI COMPLETE
# ==========================================

# --- AZIONI PER LUI (Lui fa a Lei) ---
lui_medie = [
    "Falle un massaggio rilassante di 2 minuti sulle spalle 💆‍♀️",
    "Bacia lentamente il suo collo partendo dall'orecchio 💋",
    "Sussurrale un complimento spinto all'orecchio 👂",
    "Balla con lei tenendola stretta per un minuto intero 💃"
]

lui_hot = [
    "Usa la tua cinta per legare delicatamente le sue mani ⛓️",
    "Passa un cubetto di ghiaccio sulla sua pancia e risalire... 🧊",
    "Toglile un indumento a tua scelta usando solo i denti 🦷",
    "Falle uno striptease integrale solo per lei 🕺"
]

# --- AZIONI PER LEI (Lei fa a Lui) ---
lei_medie = [
    "Fagli un massaggio con le dita tra i capelli 💆‍♂️",
    "Bacia i suoi pettorali risalendo verso il collo 💋",
    "Accarezza la sua schiena con le unghie (piano!) 💅",
    "Siediti sulle sue ginocchia e guardalo fisso negli occhi 👀"
]

lei_hot = [
    "Usa la sua cinta per immobilizzargli le mani ⛓️",
    "Versa una goccia di vino/drink sul suo petto e lecca via 🍷",
    "Togligli un indumento a tua scelta... molto lentamente 🔥",
    "Fagli un massaggio bollente usando dell'olio 🧴"
]

# ==========================================

# 1. SCELTA DEL GIOCATORE
giocatore = st.radio("Chi deve agire?", ["Tocca a LUI 👨", "Tocca a LEI 👩"], horizontal=True)

st.divider()

# 2. I DUE BOTTONI DI LANCIO
col1, col2 = st.columns(2)

sfida_estratta = None
colore_sfida = ""

with col1:
    if st.button("😇 LIVELLO MEDIO"):
        with st.spinner("..."):
            time.sleep(0.5)
            if "LUI" in giocatore:
                sfida_estratta = random.choice(lui_medie)
            else:
                sfida_estratta = random.choice(lei_medie)
            colore_sfida = "success"

with col2:
    if st.button("🔥 LIVELLO HOT"):
        with st.spinner("..."):
            time.sleep(0.5)
            if "LUI" in giocatore:
                sfida_estratta = random.choice(lui_hot)
            else:
                sfida_estratta = random.choice(lei_hot)
            colore_sfida = "hot"

# 3. VISUALIZZAZIONE RISULTATO
if sfida_estratta:
    st.divider()
    
    if colore_sfida == "success":
        st.success("✨ SFIDA MEDEA")
        st.markdown(f"<h2 style='text-align: center;'>{sfida_estratta}</h2>", unsafe_allow_html=True)
    else:
        st.error("🔥 BOLLINO ROSSO!")
        st.markdown(f"""
            <div style="background-color: #ff4b4b22; padding: 20px; border-radius: 15px; border: 2px solid #ff4b4b;">
                <h1 style="text-align: center; color: #ff4b4b; font-size: 32px;">{sfida_estratta}</h1>
            </div>
            """, unsafe_allow_html=True)

st.divider()
st.caption("Ogni click genera una nuova sfida basata su chi agisce.")
