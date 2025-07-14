import pandas as pd
from datetime import datetime

def get_live_signals():
    return pd.DataFrame([
        {
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Pair": "BTCUSDT",
            "Exchange": "Binance",
            "Side": "Long",
            "Entry Price": 58250.0,
            "Take Profit": 58425.75,
            "Success Rate": "87.5%",
        }
    ])
