import streamlit as st
import pandas as pd
from core.signal_engine import get_live_signals

st.set_page_config(page_title="Futures Scalping Signal Bot", layout="wide")
st.title("📈 Futures Scalping Signal Bot")

# Load signals safely
try:
    signals = get_live_signals()
    if isinstance(signals, pd.DataFrame):
        if len(signals.index) > 0:
            st.dataframe(signals, use_container_width=True)
        else:
            st.info("✅ App running, but no signals yet.")
    else:
        st.warning("⚠️ get_live_signals() did not return a DataFrame.")
except Exception as e:
    st.error(f"❌ Runtime error: {e}")
