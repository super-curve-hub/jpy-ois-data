import pandas as pd
import requests
from datetime import datetime

# =========================
# JSCC CSV URL（実URLに差し替え）
# =========================
JSCC_URL = "https://www.jpx.co.jp/jscc/statistics/ois/jpy_ois.csv"

print("Downloading JSCC OIS...")

r = requests.get(JSCC_URL)
with open("jscc_jpy_ois.csv", "wb") as f:
    f.write(r.content)

print("File updated:", datetime.utcnow())
