import streamlit as st
from core.signal_engine import get_live_signals

st.set_page_config(page_title="Futures Scalping Signal Bot", layout="wide")
st.title("📈 Futures Scalping Signal Bot")

# Load live signals from engine
signals = get_live_signals()

if not signals:
    st.info("No active signals yet... Waiting for real-time data.")
else:
    st.dataframe(signals)
