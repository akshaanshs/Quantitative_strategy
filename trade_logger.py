import csv
from datetime import datetime

class TradeLogger:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["time", "side", "price"])

    def log(self, side, price):
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.utcnow(), side, price])
