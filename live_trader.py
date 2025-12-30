from binance.client import Client
import time
import csv

API_KEY = "iNDtQHYPv1bz05lYBU9r6KCV7j2Q7n0CkZNiCsVJ2NYiZAyjJA1UwNqN5EyypgxT"
SECRET_KEY = "OWePxiXFpyj04u3C4Z4PLVYcPabax0zD8Hc7Skqtquw0i6Ikuda3jNVQk2mWkEkI"

client = Client(API_KEY, SECRET_KEY)
client.API_URL = "https://testnet.binance.vision/api"

SYMBOL = "BTCUSDT"
QUANTITY = 0.001

# Create CSV file
with open("live_trades.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "side", "price", "quantity"])

print("Live trading started...")

while True:
    price = float(client.get_symbol_ticker(symbol=SYMBOL)["price"])
    print("Current price:", price)

    # BUY
    buy = client.order_market_buy(
        symbol=SYMBOL,
        quantity=QUANTITY
    )

    buy_price = price

    time.sleep(5)

    # SELL
    sell = client.order_market_sell(
        symbol=SYMBOL,
        quantity=QUANTITY
    )

    sell_price = float(client.get_symbol_ticker(symbol=SYMBOL)["price"])

    # Save to CSV
    with open("live_trades.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), "BUY", buy_price, QUANTITY])
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), "SELL", sell_price, QUANTITY])

    print("Trade completed\n")

    time.sleep(10)
