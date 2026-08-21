# Vendor Routing and Fallback Map

Load before any data pull that will feed a deliverable. This file assigns a primary and a fallback per
data type so a mid-run connector failure has a defined route instead of an improvised one.

## Standing rules

1. **Probe before you plan.** Connector availability and quota are session state, not fixed facts. Run one
   cheap call per connector you intend to use, in sequence, before committing to a route. A probe failure
   drops that connector for the whole run and gets logged.
2. **Never parallelize probes or pulls on a rate-limited connector.** Parallel calls trip both the daily
   and per-second limits and return mixed, misleading errors.
3. **Tier beats convenience.** When two available sources cover the same figure, the higher tier drives the
   model even if the lower tier is faster to reach.
4. **Record the route.** The provenance block's data-source table is filled from the actual route taken,
   not the intended one.

## Source tier hierarchy

| Tier | Sources | Use for |
|---|---|---|
| 1 | SEC EDGAR filings, company IR, filings-sourced fundamental vendors | Anything that will be quoted as fact in a deliverable |
| 2 | Institutional data platforms (S&P Capital IQ / Kensho, Fiscal.ai, Daloopa, Quartr, FMP, Alpha Vantage) | Fundamentals, estimates, market data, transcripts |
| 3 | Retail aggregators (Yahoo Finance, stockanalysis.com, Macrotrends) | Fallback and cross-check only |
| 4 | Web search, news, sell-side summaries | Context, catalysts, corporate actions. Never a model input. |

A Tier 3 figure may appear in a deliverable. It may not drive a conclusion unlabeled.

## Routing table

Availability varies by session. Treat this as the intended route, confirmed by probe.

| Data type | Primary | Fallback 1 | Fallback 2 | Notes |
|---|---|---|---|---|
| Real-time / last quote, 52wk range | Alpha Vantage `GLOBAL_QUOTE` | FMP | Yahoo quote page | Alpha Vantage free keys cap near 25 calls/day. Probe first, call sequentially. |
| Price history, moving averages | Alpha Vantage `TIME_SERIES_WEEKLY_ADJUSTED` | FMP | stockanalysis.com | 50-week MA is a recurring SMIF Key Statistics blocker. Pull it while quota allows. |
| Income statement / balance sheet / cash flow | Daloopa or Fiscal.ai (filings-sourced) | S&P Capital IQ via Kensho | Alpha Vantage statements, then EDGAR | Reconcile total debt definitions before building any equity bridge |
| Segment detail | Fiscal.ai | Daloopa | 10-K segment footnote | Segment tables are the most common place vendor definitions diverge |
| Consensus estimates, PT range | S&P Capital IQ via Kensho | FMP | Yahoo analysis page | Never use analyst PTs as model inputs. Report them as positioning context. |
| Earnings calls, transcripts, guidance language | Quartr | S&P Capital IQ | Company IR | Guidance is quoted from the transcript, not from a summary of it |
| Peer sets and multiples | Fiscal.ai or S&P | FMP | stockanalysis.com | Peer selection is `[MODEL]` and requires ratification. The multiples are `[SRC]`. |
| Rates, macro, treasury | Alpha Vantage `TREASURY_YIELD` | FRED via web | Web search | 10Y UST is a WACC input. Date it precisely. |
| Corporate actions, converts, buybacks | EDGAR 8-K / 10-Q | Web search | Company IR | Never invent conversion prices or if-converted share counts |
| Numerical verification | Wolfram or local Python | Local Python | none | Every figure entering a deliverable is verified programmatically, never eyeballed |

## Overlap map (which connectors compete)

Redundancy is a resilience asset and a consistency risk. Where two connectors cover the same figure with
different definitions, an unlabeled switch mid-run produces a deliverable that does not tie to itself.

| Overlap zone | Competing sources | Divergence risk |
|---|---|---|
| Core fundamentals | Daloopa, Fiscal.ai, S&P, FMP, Alpha Vantage | Restatement vintage, GAAP vs. adjusted, fiscal-year alignment |
| Market data | Alpha Vantage, FMP, Yahoo | Intraday vs. prior close, split/dividend adjustment |
| Estimates | S&P, FMP, Yahoo | Contributor panel differs. Never mix panels within one exhibit. |
| Transcripts | Quartr, S&P | Coverage gaps on smaller caps |

**One-vendor-per-figure-class rule.** Pick one vendor per figure class for the whole run. Switching
mid-run is permitted only on failure, and the switch gets a line in the provenance block naming which
figures came from which vendor.

## Failure playbook

| Failure | Action |
|---|---|
| Probe fails | Drop that connector for the entire run. Log it. Move to fallback 1. |
| Rate limit mid-run | Stop calling. Do not retry in a loop. Move to fallback and note which figures came from which source. |
| Client-rendered page returns boilerplate or a consent wall | Treat as FAILED, drop to the next tier. Do not retry with a different fetcher and do not squint figures out of partial markup. |
| Two vendors disagree materially | Run the reconciliation sequence in SKILL.md. Report the range. |
| All tiers exhausted | DATA UNAVAILABLE. Never estimate. Log as a blocker with what it would have driven. |

## Reconciliation checklist before calling something a discrepancy

Most apparent discrepancies are definitional. Check in this order:

1. Period tag (TTM vs. MRQ vs. FY vs. CY)
2. Basis (GAAP vs. adjusted vs. non-GAAP)
3. Debt definition (with vs. without capitalized and operating leases)
4. Share count (basic vs. diluted vs. if-converted)
5. Currency and units
6. Restatement vintage and cache date

Only a gap surviving all six is a genuine discrepancy.
