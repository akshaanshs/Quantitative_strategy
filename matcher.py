# matcher.py
import pandas as pd

bt = pd.read_csv("backtest_trades.csv")
live = pd.read_csv("live_trades.csv")

print("Backtest trades:", len(bt))
print("Live trades:", len(live))

print(bt.head())
print(live.head())
