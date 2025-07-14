import streamlit as st
import pandas as pd
from core.signal_engine import get_live_signals

st.set_page_config(page_title="Futures Scalping Signal Bot", layout="wide")
st.title("📈 Futures Scalping Signal Bot")

# Get signals
signals = get_live_signals()

# Safely handle return value
if isinstance(signals, pd.DataFrame) and not signals.empty:
    st.dataframe(signals, use_container_width=True)
else:
    st.info("No active signals yet... Waiting for real-time data.")
