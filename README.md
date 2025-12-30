# Quant Developer Assignment – Binance Live Trading

## Overview
This project implements a simple trading system using Binance Spot Testnet.
It connects to Binance APIs, fetches live market prices, places market orders,
and records all trades in a CSV file.

---

## Project Structure
- live_trader.py : Live trading bot using Binance Testnet
- paper_live.py  : Paper trading using real-time Binance prices
- check_balance.py : Verifies Binance Testnet API connectivity
- live_trades.csv : Trade execution logs
- requirements.txt : Required Python libraries

---

## Part 8 – Live Trading Implementation
Live trading is implemented using Binance Spot Testnet.

Steps:
1. API keys were generated on https://testnet.binance.vision
2. Testnet account was funded with test coins
3. Bot connects to Binance Testnet API
4. Market BUY and SELL orders are placed
5. Trades are logged in CSV format

If the testnet is temporarily unavailable, the paper trading module simulates
live trading using real-time Binance market data.

---

## How to Run

### Install dependencies
```bash
pip install -r requirements.txt
