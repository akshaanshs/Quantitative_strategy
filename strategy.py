import pandas as pd

class Strategy:
    def generate_signal(self, df_15m, df_1h, position):
        df_15m["ema_fast"] = df_15m.Close.ewm(span=9).mean()
        df_15m["ema_slow"] = df_15m.Close.ewm(span=21).mean()
        df_1h["ema_trend"] = df_1h.Close.ewm(span=50).mean()

        trend_up = df_1h.Close.iloc[-1] > df_1h.ema_trend.iloc[-1]

        cross_up = df_15m.ema_fast.iloc[-2] < df_15m.ema_slow.iloc[-2] and \
                   df_15m.ema_fast.iloc[-1] > df_15m.ema_slow.iloc[-1]

        cross_down = df_15m.ema_fast.iloc[-2] > df_15m.ema_slow.iloc[-2] and \
                     df_15m.ema_fast.iloc[-1] < df_15m.ema_slow.iloc[-1]

        if position == 0:
            if trend_up and cross_up:
                return "BUY"
            if not trend_up and cross_down:
                return "SELL"

        if position == 1 and cross_down:
            return "EXIT"

        if position == -1 and cross_up:
            return "EXIT"

        return None
