import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

# FRED APIキーをSecretsから取得
api_key = '3a9b149188c85dfdf21e468641cd8a0a'

# FREDからT10Y2Yデータを取得
url = f"https://api.stlouisfed.org/fred/series/observations?series_id=T10Y2Y&api_key={api_key}&file_type=json"
response = requests.get(url)
data = response.json()

# APIから返されたデータ全体を表示する
print(data)  # ここでレスポンスデータを確認します

# データをデータフレームに変換
df = pd.DataFrame(data['observations'])
df['date'] = pd.to_datetime(df['date'])
df['value'] = pd.to_numeric(df['value'], errors='coerce')

# グラフの生成
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['value'], label='T10Y2Y')
plt.title('10-Year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.savefig('T10Y2Y_plot.png')
plt.show()
