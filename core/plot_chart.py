import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def plot_signal_chart(pair, side, entry, tp):
    now = datetime.now()
    times = [now - timedelta(minutes=5*i) for i in range(30)][::-1]
    prices = np.linspace(entry * 0.98, entry * 1.02, 30) + np.random.normal(0, 5, 30)
    df = pd.DataFrame({'time': times, 'price': prices})

    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df['time'],
        open=df['price'] * 0.99,
        high=df['price'] * 1.01,
        low=df['price'] * 0.98,
        close=df['price'],
        name="5m Candles"
    ))

    fig.add_hline(y=entry, line=dict(color='blue', dash='dash'), annotation_text="Entry", annotation_position="bottom right")
    fig.add_hline(y=tp, line=dict(color='green', dash='dot'), annotation_text="Take Profit", annotation_position="top right")
    fig.update_layout(title=f"{pair} Signal Chart ({side})", xaxis_title="Time", yaxis_title="Price")
    return fig