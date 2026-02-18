import requests
from datetime import datetime

# テスト用の確実に存在するCSV
JSCC_URL = "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv"

print("Downloading OIS data...")

r = requests.get(JSCC_URL)
r.raise_for_status()   # ←404ならここで停止

with open("jscc_jpy_ois.csv", "wb") as f:
    f.write(r.content)

print("File updated:", datetime.utcnow())
