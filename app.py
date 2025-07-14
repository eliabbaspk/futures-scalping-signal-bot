import streamlit as st
import pandas as pd
from core.signal_engine import get_live_signals

st.set_page_config(page_title="Futures Scalping Signal Bot", layout="wide")
st.title("📈 Futures Scalping Signal Bot")

# Defensive fallback
signals = get_live_signals()

if isinstance(signals, pd.DataFrame):
    if not signals.empty:
        st.dataframe(signals, use_container_width=True)
    else:
        st.info("No signals available yet.")
else:
    st.error("Error: get_live_signals() did not return a DataFrame.")
