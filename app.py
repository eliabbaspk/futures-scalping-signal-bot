import streamlit as st
import pandas as pd
from core.signal_engine import get_live_signals

st.set_page_config(page_title="Futures Scalping Signal Bot", layout="wide")
st.title("📈 Futures Scalping Signal Bot")

try:
    signals = get_live_signals()
except Exception as e:
    st.error(f"❌ get_live_signals() crashed: {e}")
    signals = pd.DataFrame()

# SAFELY display results
if isinstance(signals, pd.DataFrame):
    if signals.shape[0] > 0:
        st.success("✅ Live signals:")
        st.dataframe(signals, use_container_width=True)
    else:
        st.warning("🕒 No signals detected yet.")
else:
    st.error("⚠️ Invalid data format: Expected a DataFrame.")
