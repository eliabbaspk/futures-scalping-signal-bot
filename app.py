import streamlit as st
import pandas as pd
from core.signal_engine import get_live_signals
from core.plot_chart import plot_signal_chart

st.set_page_config(page_title="Futures Scalping Signal Bot", layout="wide")
st.title("📈 Futures Scalping Signal Bot")

try:
    signals = get_live_signals()
except Exception as e:
    st.error(f"❌ Signal error: {e}")
    signals = pd.DataFrame()

if isinstance(signals, pd.DataFrame) and len(signals) > 0:
    for i, row in signals.iterrows():
        with st.expander(f"{row['Pair']} - {row['Side']} - Success: {row['Success Rate']}"):
            st.write(f"**Exchange:** {row['Exchange']}")
            st.write(f"**Entry:** {row['Entry Price']} | **TP:** {row['Take Profit']}")
            chart_fig = plot_signal_chart(row['Pair'], row['Side'], row['Entry Price'], row['Take Profit'])
            st.plotly_chart(chart_fig, use_container_width=True)
else:
    st.info("🕒 No signals yet. Waiting for high-confidence trades...")