import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SHILLER_URL = ("https://img1.wsimg.com/blobby/go/"
               "e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/"
               "1449043e-a1ed-4e2e-8e9c-7b9a2a064493/ie_data.xls")

def load_shiller(url=SHILLER_URL):
    d = pd.read_excel(url, sheet_name="Data", skiprows=7)
    d = d.dropna(subset=["Date"])           # the footnote row at the bottom
    dates = (d["Date"] * 100).round().astype(int).astype(str)
    d.index = pd.to_datetime(dates, format="%Y%m")
    d = d[["P", "D", "E", "CPI"]].astype(float)
    d.columns = ["Price", "Dividend", "Earnings", "CPI"]
    return d

shiller = load_shiller()
print(shiller.shape)
print(shiller.head())

# (a) Price, linear vs log axis
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
shiller["Price"].plot(ax=ax[0], title="Price (linear axis)")
shiller["Price"].plot(ax=ax[1], logy=True, title="Price (log axis)")
plt.show()

# (b) monthly returns: (P_t + D_t/12) / P_{t-1} - 1
r = ((shiller["Price"] + shiller["Dividend"] / 12) / shiller["Price"].shift(1) - 1).dropna()
r.plot(figsize=(12, 4), title="Monthly returns")
plt.show()

# (c)-(e) mean, standard error, 95% confidence interval
def summarize(r, label):
    n = len(r)
    mean = r.mean()
    se = r.std() / np.sqrt(n)
    lo, hi = mean - 1.96 * se, mean + 1.96 * se
    print(f"\n{label}  (n = {n})")
    print(f"Mean:   monthly {mean:.4%}   annualized {mean * 12:.2%}")
    print(f"SE:     monthly {se:.4%}   annualized {se * 12:.2%}")
    print(f"95% CI: monthly [{lo:.4%}, {hi:.4%}]   annualized [{lo * 12:.2%}, {hi * 12:.2%}]")

summarize(r, "Full sample")

# (f) post-WWII sub-sample
summarize(r.loc["1946":], "1946 onwards")
summarize(r.loc[:"1945"], "Before 1946 (for comparison)")
