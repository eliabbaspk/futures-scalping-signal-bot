import streamlit as st
import pandas as pd
from core.signal_engine import get_live_signals

# Set Streamlit page config
st.set_page_config(page_title="Futures Scalping Signal Bot", layout="wide")
st.title("📈 Futures Scalping Signal Bot")

# Load live signals (as DataFrame)
signals = get_live_signals()

# Display signal table or fallback message
if signals.empty:
    st.info("No active signals yet... Waiting for real-time data.")
else:
    st.dataframe(signals, use_container_width=True)
