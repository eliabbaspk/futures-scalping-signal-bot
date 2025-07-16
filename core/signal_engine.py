import pandas as pd
from datetime import datetime

def get_live_signals():
    data = [
        {
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Pair": "BTCUSDT",
            "Exchange": "Binance",
            "Side": "Long",
            "Entry Price": 58250.0,
            "Take Profit": 58425.75,
            "Success Rate": "92.1%",
        },
        {
            "Time": datetime.now().strftime("%H:%M:%S"),
            "Pair": "ETHUSDT",
            "Exchange": "Binance",
            "Side": "Short",
            "Entry Price": 3105.0,
            "Take Profit": 3078.5,
            "Success Rate": "88.6%",
        }
    ]
    return pd.DataFrame(data)