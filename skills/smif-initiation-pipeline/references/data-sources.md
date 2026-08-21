# Data Sources — Fallback Ladder and Known Traps

Load before Stage 0. Every number pulled here gets a source + as-of date recorded at pull
time. Conclusion-driving figures (price, accrual inputs, consensus EPS, beta, debt/cash)
need a second source or a "single-sourced" label that survives into the deliverables.

## Ladder (stop at the first tier that yields usable data per item)

### Tier 1 — Alpha Vantage MCP (if connected)
Probe quota FIRST with one GLOBAL_QUOTE call. Free keys: 25 requests/day + per-second
burst limits, and parallel calls trip both with misleading mixed error messages. Probe
fails → skip AV for the entire run, log it. Probe succeeds → call SEQUENTIALLY only.
Useful endpoints: GLOBAL_QUOTE, COMPANY_OVERVIEW, INCOME_STATEMENT, BALANCE_SHEET,
CASH_FLOW, EARNINGS_ESTIMATES, TREASURY_YIELD, TIME_SERIES_WEEKLY_ADJUSTED (this last one
is the source for the 50-week moving average the SMIF Key Statistics block requires —
pull it whenever quota allows, it was a [TBD] blocker in the AEIS run).

### Tier 2 — Yahoo Finance (primary web fallback)
Fetch via web_fetch:
- `https://finance.yahoo.com/quote/{T}/` — price, change, ranges, mcap, beta, P/E
- `https://finance.yahoo.com/quote/{T}/key-statistics/` — EV, multiples, shares, margins
- `https://finance.yahoo.com/quote/{T}/financials/` (+ `/balance-sheet/`, `/cash-flow/`)
- `https://finance.yahoo.com/quote/{T}/analysis/` — consensus estimates, PT range

**Shell-detection rule:** Yahoo is client-rendered. If a fetch returns navigation
boilerplate, a consent page, or is missing the figures you asked for, treat that page as
FAILED and drop to Tier 3 for those items. Do not retry via curl/python/other fetchers
(prohibited), and do not squint numbers out of partial markup.
**Yahoo conventions:** statistics are a mix of TTM, MRQ, and 5-yr figures — record the
period tag next to each number. "Total Debt" includes capitalized leases. Beta is 5-yr
monthly. EPS rows may be non-GAAP where a company reports adjusted; classify before use.

### Tier 3 — stockanalysis.com (secondary web fallback)
`/stocks/{t}/`, `/stocks/{t}/financials/` (+ `balance-sheet/`, `cash-flow-statement/`,
`?p=quarterly`), `/stocks/{t}/forecast/`. Traps proven in live runs:
- Pages serve DIFFERENT cache vintages in the same session (prices days apart). Record
  the as-of shown on each page; use the freshest; log the skew.
- "Total Debt" = borrowings + operating leases. Reconcile against the ST debt / LT debt /
  lease lines before building an equity bridge, or leases get double-counted.
- Overview-page analyst PT and forecast-page PT can disagree (different vintages). Report
  both in the run log; never use PTs as model inputs.

### Tier 4 — SEC EDGAR + WebSearch
EDGAR for filings-grade numbers that the ladder failed to produce. WebSearch always runs
regardless of tier for: latest quarter results + guidance, any large recent price move
and its cause, 10-year U.S. Treasury yield (WACC input), corporate actions in the last
two quarters (converts, buybacks, redemptions, M&A), and one attempt at live sector
median multiples (if none found, use the risk-report skill's fallback defaults and label
them as defaults).

## Minimum dataset before Stage 1 may begin
Price/52wk/mcap/beta (dated) · 5 fiscal years + TTM of IS, BS, CF · 4+ quarters of
revenue, net income, operating margin · consensus revenue + EPS for the next 2 fiscal
years + analyst PT range · 10Y UST yield · basic AND diluted shares · dated news items
covering the last two quarters. GAAP vs non-GAAP EPS basis must be classified for every
EPS figure captured. Anything missing after Tier 4 = DATA UNAVAILABLE, never estimated.

## Cross-cutting rules
- Convert/lease/pension mechanics: never invent conversion prices or if-converted share
  counts. If a recent convertible muddies the bridge, use the last FILED balance sheet,
  add a pro forma note, and flag G-15 in the model.
- Two sources disagreeing materially → report the range and the discrepancy in the run
  log; do not silently pick one.
