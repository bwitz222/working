import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import jarque_bera, skew, kurtosis

stocks = ["AVGO", "APLD", "MSFT", "GOOGL", "USB"]
start, end = "2021-01-01", "2026-10-01"  # end is exclusive, so data runs through 2026-09-30

# (a) daily returns
rows = []
prices = {}
for symbol in stocks:
    p = yf.download(symbol, start=start, end=end, auto_adjust=True, progress=False)["Close"][symbol]
    prices[symbol] = p
    r = p.pct_change().dropna()
    jb = jarque_bera(r)
    rows.append({"Ticker": symbol, "JB Statistic": jb.statistic, "p-value": jb.pvalue,
                 "Skewness": skew(r), "Kurtosis": kurtosis(r, fisher=False)})  # raw kurtosis K, normal = 3

part_a = pd.DataFrame(rows)
print("(a) Daily returns")
print(part_a.round(4).to_string(index=False))

# sanity check: formula from the lab matches scipy
r = prices["MSFT"].pct_change().dropna()
n, S, K = len(r), skew(r), kurtosis(r, fisher=False)
print("\nFormula check (MSFT):", round(n / 6 * (S**2 + (K - 3)**2 / 4), 4), "vs scipy", round(jarque_bera(r).statistic, 4))

# (b) daily vs weekly vs monthly
rows = []
for symbol in stocks:
    p = prices[symbol]
    daily = p.pct_change().dropna()
    weekly = p.resample("W-FRI").last().pct_change().dropna().iloc[:-1]  # drop the incomplete final week
    monthly = p.resample("ME").last().pct_change().dropna()
    row = {"Ticker": symbol}
    for name, r in [("Daily", daily), ("Weekly", weekly), ("Monthly", monthly)]:
        jb = jarque_bera(r)
        row[name + " N"] = len(r)
        row[name + " JB"] = jb.statistic
        row[name + " p"] = jb.pvalue
    rows.append(row)

part_b = pd.DataFrame(rows)
print("\n(b) Jarque-Bera by horizon")
print(part_b.round(4).to_string(index=False))
