import pandas as pd
import time
from strategy import Strategy
from trade_logger import TradeLogger

# load same data used in backtest
data = pd.read_csv("BTCUSDT_15m.csv", index_col=0, parse_dates=True)

brain = Strategy()
logger = TradeLogger("live_trades.csv")

position = 0          # 0 = no trade, 1 = buy, -1 = sell
window = 100          # candles visible at start

print("Live trading started...\n")

for i in range(window, len(data)):
    df_15m = data.iloc[:i]
    df_1h = df_15m.resample("1H").last()

    signal = brain.generate_signal(df_15m, df_1h, position)
    price = df_15m.Close.iloc[-1]

    if signal == "BUY":
        position = 1
        logger.log("BUY", price)
        print("LIVE BUY at", price)

    elif signal == "SELL":
        position = -1
        logger.log("SELL", price)
        print("LIVE SELL at", price)

    elif signal == "EXIT":
        position = 0
        logger.log("EXIT", price)
        print("LIVE EXIT at", price)

    time.sleep(0.5)   # makes it feel live

