# %% [markdown]
# # Lab 05: Getting Data — Stocks, FRED, and Inflation
# Stock used: **TSLA**. Change `TICKER` below to use a different stock.

# %%
# Setup: import the libraries we need
import pandas as pd                # tables of data (DataFrames)
import matplotlib.pyplot as plt    # plotting
import yfinance as yf              # downloads stock prices from Yahoo Finance

# %% [markdown]
# ## 1. Subsetting and Downsampling

# %% [markdown]
# ### (a) Download all available daily price data

# %%
TICKER = "TSLA"

# period="max" asks Yahoo for every day of history it has
stock = yf.Ticker(TICKER)
prices = stock.history(period="max")

# Drop the time zone so we can slice the index with plain date strings
prices.index = prices.index.tz_localize(None)

display(prices.head())
display(prices.tail())
print("First date:", prices.index[0].date(), "| Last date:", prices.index[-1].date())

# %% [markdown]
# ### (b) Daily closing prices, Feb 25 2021 to Mar 8 2021

# %%
# .loc with two date strings selects that date range (both ends included)
close_b = prices.loc["2021-02-25":"2021-03-08", "Close"]

close_b.plot(marker="o", title=f"{TICKER} Daily Close: Feb 25 - Mar 8, 2021")
plt.ylabel("Price ($)")
plt.show()

# %% [markdown]
# ### (c) Daily closing prices for the past 3 weeks

# %%
# Start date = last date in the data minus 3 weeks
last_date = prices.index[-1]
start_c = last_date - pd.Timedelta(weeks=3)

close_c = prices.loc[start_c:, "Close"]

close_c.plot(marker="o", title=f"{TICKER} Daily Close: Past 3 Weeks")
plt.ylabel("Price ($)")
plt.show()

# %% [markdown]
# ### (d) Quarterly closing prices for the first 2 years of data

# %%
# Keep only the first 2 years of data
first_date = prices.index[0]
end_d = first_date + pd.DateOffset(years=2)
first_two_years = prices.loc[:end_d, "Close"]

# Downsample daily -> quarterly: take the last close of each quarter ("QE" = quarter end)
quarterly_close = first_two_years.resample("QE").last()
display(quarterly_close)

quarterly_close.plot(marker="o", title=f"{TICKER} Quarterly Close: First 2 Years")
plt.ylabel("Price ($)")
plt.show()

# %% [markdown]
# ## 2. Economic Data from FRED

# %%
# Helper from the lab guide: download one FRED series into a DataFrame indexed by date
def get_fred(series_id):
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    return pd.read_csv(url,
                       parse_dates=['observation_date'],
                       index_col='observation_date',
                       na_values='.')   # FRED marks missing values with "."

# Example from the guide: Japan / U.S. exchange rate
jpy = get_fred("DEXJPUS")
display(jpy.head())
jpy.plot(title="DEXJPUS: Japan / U.S. Foreign Exchange Rate");

# %% [markdown]
# ### (a) 1-Month Treasury Constant Maturity Rate (DGS1MO)

# %%
tbill = get_fred("DGS1MO")
display(tbill.tail())

tbill.plot(title="DGS1MO: 1-Month Treasury Constant Maturity Rate", legend=False)
plt.ylabel("Percent")
plt.show()

# %% [markdown]
# ### (b) CPI series
# Using **CPIAUCSL**: Consumer Price Index for All Urban Consumers, All Items, seasonally adjusted, monthly (index 1982-84 = 100).

# %%
cpi = get_fred("CPIAUCSL")
display(cpi.tail())

cpi.plot(title="CPIAUCSL: Consumer Price Index (All Urban Consumers)", legend=False)
plt.ylabel("Index (1982-84 = 100)")
plt.show()

# %% [markdown]
# ### (c) Inflation rate = 12-month % change in CPI
# CPI is monthly, so each value is compared with the value 12 rows earlier.

# %%
# pct_change(12) = (CPI_t / CPI_{t-12}) - 1; multiply by 100 for percent
inflation = cpi["CPIAUCSL"].pct_change(12) * 100

# Same thing using shift, as a check
inflation_check = (cpi["CPIAUCSL"] / cpi["CPIAUCSL"].shift(12) - 1) * 100
print("Both methods match:", inflation.dropna().round(10).equals(inflation_check.dropna().round(10)))

inflation = inflation.dropna()   # first 12 months have no prior-year value
display(inflation.tail())

inflation.plot(title="U.S. Inflation Rate (12-Month % Change in CPI)")
plt.axhline(0, color="black", linewidth=0.8)   # zero line makes deflation easy to spot
plt.ylabel("Percent")
plt.show()

# %% [markdown]
# ### (d) Mini-research: U.S. house prices over the past ~20 years
# Data: **CSUSHPISA**, S&P CoreLogic Case-Shiller U.S. National Home Price Index (monthly, seasonally adjusted).
# Three views:
# 1. Nominal index level
# 2. Year-over-year % change (house-price "inflation")
# 3. Real index (house prices divided by CPI), to strip out general inflation

# %%
hpi = get_fred("CSUSHPISA")["CSUSHPISA"].dropna()

# Keep roughly the last 20 years
start_hpi = hpi.index[-1] - pd.DateOffset(years=20)
hpi_20 = hpi.loc[start_hpi:]

# 1) Nominal level
hpi_20.plot(title="Case-Shiller U.S. National Home Price Index (Nominal)")
plt.ylabel("Index (Jan 2000 = 100)")
plt.show()

# %%
# 2) Year-over-year % change, compared with CPI inflation from part (c)
hpi_yoy = (hpi.pct_change(12) * 100).loc[start_hpi:]

hpi_yoy.plot(label="House prices YoY %")
inflation.loc[start_hpi:].plot(label="CPI inflation YoY %")
plt.axhline(0, color="black", linewidth=0.8)
plt.title("House Price Growth vs. CPI Inflation")
plt.ylabel("Percent")
plt.legend()
plt.show()

# %%
# 3) Real house prices: divide the house-price index by CPI on matching months
both = pd.concat([hpi, cpi["CPIAUCSL"]], axis=1, join="inner").loc[start_hpi:]
real_hpi = both["CSUSHPISA"] / both["CPIAUCSL"]
real_hpi = real_hpi / real_hpi.iloc[0] * 100      # rebase so the first month = 100

nominal_rebased = both["CSUSHPISA"] / both["CSUSHPISA"].iloc[0] * 100

nominal_rebased.plot(label="Nominal")
real_hpi.plot(label="Real (CPI-adjusted)")
plt.title("House Prices: Nominal vs. Real (start = 100)")
plt.ylabel("Index")
plt.legend()
plt.show()

# %%
# Key numbers to support the write-up (all computed from the data above)
pre_crisis = hpi.loc[:"2008-12-31"]
peak_date = pre_crisis.idxmax()
trough_date = hpi.loc[peak_date:"2015-12-31"].idxmin()

print(f"Data range used: {hpi_20.index[0].date()} to {hpi_20.index[-1].date()}")
print(f"Pre-crisis peak:  {peak_date.date()}  index = {hpi[peak_date]:.1f}")
print(f"Post-crisis low:  {trough_date.date()}  index = {hpi[trough_date]:.1f}")
print(f"Peak-to-trough change: {(hpi[trough_date] / hpi[peak_date] - 1) * 100:.1f}%")
print(f"Change from low to latest: {(hpi.iloc[-1] / hpi[trough_date] - 1) * 100:.1f}%")
print(f"Nominal change over the window: {nominal_rebased.iloc[-1] - 100:.1f}%")
print(f"Real change over the window:    {real_hpi.iloc[-1] - 100:.1f}%")
print(f"Fastest YoY growth in window: {hpi_yoy.max():.1f}% ({hpi_yoy.idxmax().date()})")
print(f"Latest YoY growth: {hpi_yoy.iloc[-1]:.1f}% ({hpi_yoy.index[-1].date()})")

# %% [markdown]
# **Findings** (check against the printed numbers above):
# - **Housing bubble and bust:** prices peaked in the mid-2000s, then fell sharply through the 2008 financial crisis, bottoming out around 2011-2012.
# - **Long recovery:** from roughly 2012 to 2019 prices rose steadily, eventually passing the old peak.
# - **Pandemic boom:** 2020-2022 saw the fastest house-price growth in the window, far above CPI inflation, driven by very low mortgage rates, strong demand for space, and tight supply.
# - **Cooling:** as the Fed raised rates from 2022, mortgage rates jumped and year-over-year house-price growth slowed sharply.
# - **Real vs. nominal:** a good part of the nominal gain is general inflation, but the real (CPI-adjusted) line shows house prices still outpaced the overall price level over the period.

