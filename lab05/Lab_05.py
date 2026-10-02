# %% [markdown]
# # Lab 05: Getting Data — Stocks, FRED, and Inflation
# Stock used: **TSLA**

# %%
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Simple helper: plot one series with a title and y-axis label
def plot_series(series, title, ylabel):
    series.plot(marker="o" if len(series) < 50 else None)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.show()

# %% [markdown]
# ## 1. Subsetting and Downsampling
# ### (a) Download all daily price data

# %%
prices = yf.Ticker("TSLA").history(period="max")   # all available history
prices.index = prices.index.tz_localize(None)      # remove time zone so date slicing is easy
close = prices["Close"]                            # we only need closing prices
close.head()

# %% [markdown]
# ### (b) Closing prices, Feb 25 2021 to Mar 8 2021

# %%
plot_series(close["2021-02-25":"2021-03-08"], "TSLA Close: Feb 25 - Mar 8, 2021", "Price ($)")

# %% [markdown]
# ### (c) Closing prices for the past 3 weeks

# %%
start = close.index[-1] - pd.Timedelta(weeks=3)    # last date minus 3 weeks
plot_series(close[start:], "TSLA Close: Past 3 Weeks", "Price ($)")

# %% [markdown]
# ### (d) Quarterly closing prices for the first 2 years

# %%
end = close.index[0] + pd.DateOffset(years=2)      # first date plus 2 years
quarterly = close[:end].resample("QE").last()      # last close of each quarter
plot_series(quarterly, "TSLA Quarterly Close: First 2 Years", "Price ($)")

# %% [markdown]
# ## 2. Economic Data from FRED

# %%
# Download one FRED series by its ID (helper from the lab guide)
def get_fred(series_id):
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    return pd.read_csv(url,
                       parse_dates=['observation_date'],
                       index_col='observation_date',
                       na_values='.')

# Example from the guide
jpy = get_fred("DEXJPUS")
jpy.plot(title="DEXJPUS: Japan / U.S. Foreign Exchange Rate");

# %% [markdown]
# ### (a) 1-Month T-bill rate (DGS1MO)

# %%
tbill = get_fred("DGS1MO")["DGS1MO"]
plot_series(tbill, "1-Month Treasury Rate (DGS1MO)", "Percent")

# %% [markdown]
# ### (b) CPI (CPIAUCSL: all urban consumers, monthly)

# %%
cpi = get_fred("CPIAUCSL")["CPIAUCSL"]
plot_series(cpi, "Consumer Price Index (CPIAUCSL)", "Index (1982-84 = 100)")

# %% [markdown]
# ### (c) Inflation = 12-month % change in CPI

# %%
inflation = cpi.pct_change(12) * 100               # compare each month with 12 months earlier
plot_series(inflation, "U.S. Inflation Rate (12-Month % Change in CPI)", "Percent")

# %% [markdown]
# ### (d) U.S. house prices, past 20 years
# Data: CSUSHPISA, the Case-Shiller U.S. National Home Price Index (monthly).

# %%
house = get_fred("CSUSHPISA")["CSUSHPISA"]
start = house.index[-1] - pd.DateOffset(years=20)  # last 20 years
house = house[start:]

plot_series(house, "Case-Shiller U.S. Home Price Index", "Index (Jan 2000 = 100)")

# %%
# Yearly growth in house prices vs. CPI inflation
house_growth = house.pct_change(12) * 100
house_growth.plot(label="House prices")
inflation[start:].plot(label="CPI inflation")
plt.title("House Price Growth vs. Inflation (12-Month % Change)")
plt.ylabel("Percent")
plt.legend()
plt.show()

# %%
# Key numbers for the write-up
peak = house[:"2008"].idxmax()                     # housing-bubble peak
low = house[peak:"2015"].idxmin()                  # post-crisis low
print("Bubble peak:", peak.date(), round(house[peak], 1))
print("Crisis low: ", low.date(), round(house[low], 1))
print("Drop from peak to low (%):", round((house[low] / house[peak] - 1) * 100, 1))
print("Rise from low to latest (%):", round((house.iloc[-1] / house[low] - 1) * 100, 1))
print("Fastest yearly growth (%):", round(house_growth.max(), 1), "on", house_growth.idxmax().date())

# %% [markdown]
# **Findings** (check against the numbers printed above):
# - Prices peaked in the mid-2000s housing bubble, then fell hard through the 2008 crisis, bottoming around 2011-2012.
# - From about 2012 to 2019 prices recovered steadily and passed the old peak.
# - 2020-2022 had the fastest growth in the period, well above CPI inflation (low mortgage rates, strong demand, tight supply).
# - After the Fed raised rates in 2022, mortgage rates jumped and house-price growth slowed sharply.
