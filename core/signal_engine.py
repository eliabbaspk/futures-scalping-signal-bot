# core/signal_engine.py

import pandas as pd
from datetime import datetime

# Temporary sample function — real signal logic comes later
def get_live_signals():
    # Simulated example data
    data = [
        {
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Pair": "BTCUSDT",
            "Exchange": "Binance",
            "Side": "Long",
            "Entry Price": 58250.0,
            "Take Profit": 58425.75,
            "Success Rate": "87.5%",
        },
        {
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Pair": "ETHUSDT",
            "Exchange": "Bybit",
            "Side": "Short",
            "Entry Price": 3120.0,
            "Take Profit": 3100.6,
            "Success Rate": "90.0%",
        }
    ]
    return pd.DataFrame(data)
