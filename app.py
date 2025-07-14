import streamlit as st
import pandas as pd
from core.signal_engine import get_live_signals

st.set_page_config(page_title="Futures Scalping Signal Bot", layout="wide")
st.title("📈 Futures Scalping Signal Bot")

# Safe call
try:
    signals = get_live_signals()
except Exception as e:
    st.error(f"❌ Signal error: {e}")
    signals = pd.DataFrame()

# Safe display
if isinstance(signals, pd.DataFrame) and len(signals) > 0:
    st.success("✅ Live Signals:")
    st.dataframe(signals, use_container_width=True)
else:
    st.info("🕒 No signals available yet.")

