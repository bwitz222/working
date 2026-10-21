import pandas as pd
import yfinance as yf
from scipy.stats import skew, kurtosis

stocks = ["AVGO", "APLD", "MSFT", "GOOGL", "USB"]
start = "2021-01-01"

# (a) skewness and excess kurtosis of daily returns
skewness_results = []
kurtosis_results = []
returns = {}

for symbol in stocks:
    prices = yf.download(symbol, start=start, auto_adjust=True, progress=False)["Close"][symbol]
    r = prices.pct_change().dropna()
    returns[symbol] = r
    skewness_results.append(skew(r))
    kurtosis_results.append(kurtosis(r))  # scipy default = excess kurtosis (kurtosis - 3)

part_a = pd.DataFrame({"Skewness": skewness_results, "Excess Kurtosis": kurtosis_results}, index=stocks)
print("(a) Full sample")
print(part_a.round(3))

# (b) drop the single largest daily move (up or down) and recompute
rows = []
for i, symbol in enumerate(stocks):
    r = returns[symbol]
    day = r.abs().idxmax()
    r2 = r.drop(day)
    rows.append({
        "Stock": symbol,
        "Dropped Date": day.date(),
        "Dropped Return": r[day],
        "Skew Before": skewness_results[i],
        "Skew After": skew(r2),
        "Kurt Before": kurtosis_results[i],
        "Kurt After": kurtosis(r2),
    })

part_b = pd.DataFrame(rows).set_index("Stock")
part_b["Skew Change"] = part_b["Skew After"] - part_b["Skew Before"]
part_b["Kurt Change"] = part_b["Kurt After"] - part_b["Kurt Before"]
print("\n(b) Before vs after dropping the largest move")
print(part_b.round(3).to_string())
print("\nObservations per stock:", {s: len(returns[s]) for s in stocks})
print("Sample:", {s: str(returns[s].index[0].date()) + " to " + str(returns[s].index[-1].date()) for s in stocks})
