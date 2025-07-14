import streamlit as st
import pandas as pd
from core.signal_engine import get_live_signals

st.set_page_config(page_title="Futures Scalping Signal Bot", layout="wide")
st.title("📈 Futures Scalping Signal Bot")

# Safely get signal data
signals = get_live_signals()

# Check if it's a valid DataFrame
if isinstance(signals, pd.DataFrame):
    if len(signals) > 0:
        st.dataframe(signals, use_container_width=True)
    else:
        st.info("✅ App running. No signals yet.")
else:
    st.error("❌ Error: get_live_signals() did not return a DataFrame.")
