from backtesting import Backtest, Strategy as BTStrategy
import pandas as pd
from strategy import Strategy
from trade_logger import TradeLogger

class MyBacktest(BTStrategy):
    brain = Strategy()

    def init(self):
        self.logger = TradeLogger("backtest_trades.csv")

    def next(self):
        df_15m = self.data.df
        df_1h = df_15m.resample("1H").last()

        position = 1 if self.position.is_long else -1 if self.position.is_short else 0

        signal = self.brain.generate_signal(df_15m, df_1h, position)

        if signal == "BUY":
            self.buy()
            self.logger.log("BUY", self.data.Close[-1])

        elif signal == "SELL":
            self.sell()
            self.logger.log("SELL", self.data.Close[-1])

        elif signal == "EXIT":
            self.position.close()
            self.logger.log("EXIT", self.data.Close[-1])

data = pd.read_csv("BTCUSDT_15m.csv", index_col=0, parse_dates=True)

bt = Backtest(data, MyBacktest, cash=10000)
bt.run()
