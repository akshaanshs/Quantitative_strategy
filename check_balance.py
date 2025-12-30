from binance.client import Client

API_KEY = "iNDtQHYPv1bz05lYBU9r6KCV7j2Q7n0CkZNiCsVJ2NYiZAyjJA1UwNqN5EyypgxT"
SECRET_KEY = "OWePxiXFpyj04u3C4Z4PLVYcPabax0zD8Hc7Skqtquw0i6Ikuda3jNVQk2mWkEkI"

client = Client(API_KEY, SECRET_KEY, testnet=True)

account = client.get_account()

print("Your balances:")
for asset in account["balances"]:
    if float(asset["free"]) > 0:
        print(asset["asset"], asset["free"])

