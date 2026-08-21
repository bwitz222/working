---
name: equity-research-foundation
description: >
  Academic and practitioner reasoning layer for equity research. Encodes 30+ foundational finance
  papers (Fama-French, Sloan, Kahneman-Tversky, Jensen, Tunneling, Jegadeesh-Titman, and more) as
  active analytical frameworks, not passive references. Use whenever building an investment thesis,
  auditing earnings quality, scanning for behavioral mispricing, assessing management or governance,
  diagnosing factor exposures, stress-testing a valuation, or initiating coverage. Triggers on:
  "earnings quality", "are these earnings real", "high accruals", "behavioral bias", "is the market
  wrong", "consensus too high", "contrarian", "momentum", "assess management", "promoter-led",
  "governance red flags", "tunneling", "capital allocation", "factor exposure", "value vs growth",
  "sanity check this DCF", "research foundation", "initiate coverage", "build a thesis", "why is
  this mispriced", or any underlying paper by name. Front-runs the equity-risk-report and DCF
  skills by activating the right academic model first.
---

# Equity Research Foundation

A reasoning layer that activates the right academic mental model for the analytical task at hand,
then hands off to the appropriate execution skill. The papers are encoded as **checklists and
decision rules**, not summaries. The goal is a defensible edge: every claim about a stock should
trace to a mechanism that academic or practitioner research has validated.

**Output discipline:** Lead with the conclusion. Name the specific paper/mechanism behind each
analytical move. Keep briefs to 1 page. If a finding does not change the stock call, cut it.

---

## How to use this skill

1. **Run Phase 0 (Applicability & Data Gate).** Never skip it.
2. **Detect the task type** from the user's request (see Path Router below).
3. **Load only the relevant reference file(s).** Never load all seven at once.
4. **Run the path's checklist** against the live company.
5. **Hand off** to the correct execution skill for the final deliverable.

---

## Phase 0: Applicability & Data Gate (mandatory, runs before any path)

These four checks run first, every time. If any fails, stop or adapt before proceeding.

### Check 1 — Asset class
These papers govern **public-equity, cash-flow-generating businesses**. They do **not** transfer
cleanly to:
- Crypto, FX, commodities, or any non-cash-flow asset → **[STOP]**. State that this framework is
  equity-specific and does not apply. Do not lend academic authority to an asset the papers never covered.
- Pre-revenue or private companies with no reliable financials → run only Paths 2/3 (behavioral,
  governance) if at all; explicitly disable Paths 1/4/5 (accrual, factor, DCF integrity) and say why.

### Check 2 — Sector special cases
The accrual, factor, and ROE mechanisms misfire on structurally different financials. Before Path 1
or Path 4, classify the sector and apply the correct lens:

| Sector | Standard lens breaks because | Use instead |
|---|---|---|
| **Banks / lenders** | No clean CFO/accrual split; provisions dominate | Loan-loss provisioning trend, NIM, NPL/coverage, not the Sloan accrual ratio |
| **Insurers** | Float and reserves distort accruals and earnings | Reserve development, combined ratio, not Sloan accruals |
| **REITs** | EPS understates cash; depreciation is non-economic | FFO / AFFO, not net income or P/E |
| **Utilities** | Regulated returns; heavy capex/leverage are structural, not distress | Rate-base growth, allowed ROE, regulatory climate; high D/E is normal |
| **BDCs / asset managers** | NII and NAV, not GAAP EPS, drive value | Net investment income, NAV per share, fee streams |
| **Royalty / streaming / trusts** | No operations; value is a cash-stream claim | Distribution coverage, reserve life; Williams DDM logic fits directly |
| **Biotech / pre-commercial pharma** | No revenue; value is pipeline optionality | Trial-stage probability-weighted NPV, cash runway, catalyst calendar; disable factor/accrual lenses |
| **Deep cyclicals / commodities** | Trough/peak earnings distort P/E and ROE | Mid-cycle/normalized earnings, replacement value, P/B vs cycle |
| **Pre-profit / negative equity** | P/E, B/M, ROE all break or invert | Cash runway, gross-margin trajectory, unit economics; flag that factor/ROE lenses are disabled |

**Catch-all rule:** This table is not exhaustive. If the standard accrual/factor/ROE lens would
produce a structurally distorted number for *any* business model (the metric means something
different than it does for a normal operating company), stop, name the distortion, and substitute
the metric a specialist in that sub-industry would use. When unsure whether a sector qualifies,
treat it as if it does and flag the uncertainty rather than reporting a possibly-broken ratio.

If the company falls in one of these buckets, say so explicitly and substitute the correct metric
before running the checklist. Never report a Sloan accrual ratio for a bank.

### Check 3 — Live data mandate and source quality
Every number the framework consumes (accruals, CFO, consensus, multiples, ownership) must be
**sourced live before use**. Search first. For each input, record the source and date.
- **Source hierarchy:** primary filings (SEC EDGAR 10-K/10-Q, company IR) > established data
  providers (Bloomberg, FactSet, S&P, Koyfin) > aggregators (Yahoo, Macrotrends) > anything else.
  Prefer the highest available tier.
- **Dual-source rule:** any single figure that *drives a conclusion* (the accrual flag, a valuation
  multiple, a governance red flag) must be corroborated across at least two independent sources. If
  two sources materially disagree, report the range and the discrepancy — do not silently pick one.
- **Single-sourced critical numbers** must be labeled as such so the user knows the confidence level.
- If a required input cannot be sourced, mark it **UNVERIFIED** and do not let it drive a conclusion.
- If the inputs for an entire path cannot be sourced, **stop that path** and say so. Never run an
  academic mechanism on remembered or estimated figures. Rigorous-looking output on fabricated
  numbers is the worst failure mode this skill can produce.

### Check 4 — Edge-case math
Before computing any ratio, guard the denominator and the sign:
- Total assets or equity near zero or negative → the ratio is undefined, not "high" or "low." Say so.
- Negative book value → book-to-market is uninterpretable; skip the value-factor read, note why.
- Negative earnings → P/E is not a valuation signal; switch to EV/sales or FCF-based framing.

Only after Phase 0 passes do you enter the Path Router.

---

## Path Router

| User intent | Path | Load reference | Hands off to |
|---|---|---|---|
| Audit earnings, accruals, cash conversion, persistence | **1. Earnings Quality Audit** | `references/accounting-quality.md` | `equity-risk-report`, `dcf` |
| Market wrong, overreaction, contrarian, momentum, sentiment | **2. Behavioral Bias Scan** | `references/behavioral-biases.md` | `write` |
| Management quality, capital allocation, governance, promoter, tunneling | **3. Governance Assessment** | `references/corporate-governance.md` | `equity-risk-report` |
| Factor exposure, value/size/momentum/quality decomposition | **4. Factor Diagnosis** | `references/factor-anomalies.md` | `dcf` |
| Sanity-check DCF, terminal value, market-efficiency challenge | **5. Valuation Integrity Check** | `references/valuation-foundations.md` | `dcf` |
| Initiate coverage, build full thesis, research framework | **6. Full Foundation Brief** | all seven, in sequence | `smif-initiation-pipeline` |
| Analyst consensus, forecast bias, info asymmetry | (sub-path of 2) | `references/analyst-microstructure.md` | `write` |
| Emerging market / India name | (overlay on any path) | `references/emerging-markets.md` | current path's handoff |

**Routing rule:** When a request spans multiple paths (common for thesis work), default to **Path 6**
and sequence the others inside it. When in doubt between two paths, ask one routing question.

**Collision tiebreaks:**
- **"momentum" → Path 4 vs Path 2.** Use Path 4 (Factor) when the question is *whether the momentum
  factor is present and priced*. Use Path 2 (Behavioral) when the question is *whether the crowd's
  reaction driving that momentum is a bias you can exploit*. If unclear, ask.
- **Cross-skill collision on "analyze [ticker]".** This skill supplies the *reasoning layer*; it does
  not produce the final dashboard or model. If the user wants a formatted report, run this skill's
  relevant path first, then hand off to `equity-risk-report` (dashboard) or the DCF skills (valuation).
  If the user only wants a number or a chart with no analytical framing, defer to those skills directly
  and do not invoke this one.

---

## Path 1: Earnings Quality Audit

**Activate when:** validating reported earnings before trusting them in a model.

**Core mechanism (Sloan 1996):** Earnings = cash flow + accruals. The accrual component is far less
persistent than the cash component, yet the market prices both as if equally durable. High-accrual
firms systematically underperform. This is the single most actionable earnings-quality result.

**Checklist:**
1. Compute the accrual ratio: `(Net Income − Cash Flow from Operations) / Total Assets`. High positive = red flag.
2. Cash conversion: is CFO tracking net income over 8+ quarters, or diverging?
3. Persistence test (Penman-Zhang): decompose ROE into sustainable vs. transitory drivers.
4. Surprise direction (Ball & Brown): is the most recent earnings surprise being under-reacted to?
5. Analyst blind spot (Bradshaw et al.): does consensus penalize the high accruals, or ignore them? If ignored, that is the edge.

**What it changes:** Adjusts the FCF base in any DCF; reweights the growth pillar in a risk report;
flags whether an "earnings beat" is real or accrual-manufactured.

Full mechanism detail: `references/accounting-quality.md`

---

## Path 2: Behavioral Bias Scan

**Activate when:** the thesis depends on the market being wrong.

**Core question:** *Which specific, documented bias is being exploited, and is it under- or over-reaction?*
A thesis that cannot name its bias is a hope, not an edge.

**Checklist:**
1. Time horizon: short-run underreaction (BSV 1998, Jegadeesh-Titman momentum) vs. long-run overreaction (De Bondt-Thaler reversal)? These point in opposite directions — pick one.
2. Loss aversion / anchoring (Kahneman-Tversky): is the crowd anchored to a reference price or a prior narrative?
3. Sentiment regime (Baker-Wurgler): high-sentiment periods punish speculative names; where are we in the cycle?
4. Herding (Scharfstein-Stein): is consensus clustered because of conviction or career risk? Clustered consensus is often the trade.
5. Size the edge: name the expected re-rating and the catalyst that closes the gap.

**What it changes:** Converts a vague "it's cheap" into a named, mechanism-backed mispricing claim
that survives an IC challenge.

Full mechanism detail: `references/behavioral-biases.md` (and `references/analyst-microstructure.md` for consensus-specific work)

---

## Path 3: Governance Assessment

**Activate when:** management behavior or ownership structure is a material part of the risk.

**Core lenses:**
- **Jensen (1986) free cash flow:** firms with excess cash and weak governance destroy value through empire-building. Watch capital allocation discipline.
- **Jensen-Meckling (1976):** the principal-agent gap is the root of every governance question. Align incentives or expect value leakage.
- **Tunneling (Johnson et al. 2000):** controlling shareholders extract value from minorities via related-party transactions, transfer pricing, and dilutive issuance. Essential for promoter-led names.
- **Kothari et al. (2009):** managers disclose good news faster than bad. Discount the timing and tone of guidance accordingly.

**Checklist:**
1. FCF deployment: buybacks/dividends vs. value-destructive M&A or pet projects?
2. Related-party transactions: scan filings for tunneling vectors.
3. Ownership: promoter stake, pledging, dual-class, minority protection.
4. Disclosure credibility: does the firm bury bad news or release it slowly?
5. Governance premium (Durnev-Kim): in EMs, better-governed firms trade at a defensible premium — size it.

**What it changes:** Feeds the risk/catalyst matrix; can justify or collapse a conglomerate discount.

Full mechanism detail: `references/corporate-governance.md`

---

## Path 4: Factor Diagnosis

**Activate when:** classifying what systematically drives the stock's returns.

**Core mechanism (Fama-French 1992):** Value and size premia explain cross-sectional returns beyond
market beta. Layer momentum (Jegadeesh-Titman 1993) and the behavioral value story (LSV 1994).

**Checklist:**
1. Value: where does the stock sit on B/M, E/P, FCF yield vs. its sector?
2. Size: does the thesis lean on a small-cap premium that may not be currently paid?
3. Momentum: 12-month price trend — is the stock fighting or riding the factor?
4. Quality overlay: high ROE persistence (Penman-Zhang) distinguishes value from value-trap.
5. Crowding check: is the factor premium the thesis relies on currently priced in or washed out?

**What it changes:** Informs scenario weighting in a DCF; flags when a "value" call is really a
value trap, or a "growth" name is riding momentum that can reverse.

Full mechanism detail: `references/factor-anomalies.md`

---

## Path 5: Valuation Integrity Check

**Activate when:** stress-testing an existing DCF or intrinsic-value claim.

**Core lenses:**
- **Williams (1938):** intrinsic value = discounted future distributions. Everything reduces to cash to shareholders.
- **Miller-Modigliani (1961):** terminal value assumptions dominate equity valuations — interrogate them first.
- **Grossman-Stiglitz (1980):** markets cannot be fully efficient, which is the only reason your research has value. State explicitly what the market is missing.
- **Fama (1970) EMH:** name which form of efficiency (weak/semi-strong/strong) the model is betting against. If you can't, the edge is undefined.

**Checklist:**
1. Terminal value as % of EV — if >75%, the near-term model is theater; sensitize aggressively.
2. WACC − g spread: below 1% is hyper-sensitive; widen the table.
3. Distribution logic: does the model trace to actual cash to shareholders, or accounting abstractions?
4. Efficiency bet: write one sentence on what specifically the market has wrong. If you can't, stop.

**What it changes:** A second-opinion layer that catches indefensible terminal assumptions before
they reach an MD or IC.

Full mechanism detail: `references/valuation-foundations.md`

---

## Path 6: Full Foundation Brief

**Activate when:** initiating coverage or building a thesis from scratch.

Run all six analytical lenses in sequence and compress into a 1-page brief:

1. **Active-research justification (Grossman-Stiglitz):** one sentence on the specific inefficiency.
2. **Factor exposure (Path 4):** where the stock sits on value/size/momentum/quality.
3. **Earnings quality pre-check (Path 1):** accrual ratio and cash conversion verdict.
4. **Behavioral context (Path 2):** what the crowd is getting wrong and why.
5. **Governance flags (Path 3):** material agency or tunneling risks.
6. **EM overlay (if applicable):** governance premium / accounting-noise adjustment.

7. **Falsification step (mandatory, before any synthesis).** A bear case with teeth, not a token
   paragraph. It must contain all three:
   - **Specific bear thesis:** the strongest version of why this is wrong, argued through the same
     lenses (which factor reverses, which accrual reverses, which governance risk triggers). Vague
     statements ("competition could rise," "macro could worsen") do not count.
   - **Kill criteria:** 2–3 *observable, dated* events that would end the thesis (e.g., "accrual ratio
     stays above X for two more quarters," "promoter pledges rise above Y%," "the value re-rating
     fails to begin within Z months of the named catalyst"). If you cannot name what would prove you
     wrong, you do not have a thesis.
   - **Pre-mortem:** assume it's 18 months later and the call failed. Write the single most likely
     reason. If that reason is already visible today, the thesis is not ready.

   Do not soften the bear case to reach a cleaner conclusion. A thesis builder without a real
   disconfirmation step is a rationalization engine, not research.

8. **Consensus divergence gate (mandatory, after falsification, before synthesis).** Load
   `references/consensus-divergence.md`. Four answers, recorded, not implied:
   - **Consensus as a number:** estimates, PT range and median, current multiple vs. own history and
     peers. Live-sourced and dated. Not "the market likes it."
   - **Where the view differs and by how much:** the line item and the magnitude, plus the share of the
     valuation gap it drives. A difference in tone is not a variant view.
   - **Why the gap persists:** a named mechanism (horizon mismatch, structural exclusion, interpretive
     difficulty, recency). "The market is short-sighted" is not a mechanism. No mechanism means the
     likeliest explanation is that the view is not variant.
   - **Derivative-view check:** could this be a well-argued restatement of consensus that arrived
     through sources or tooling that already encode it? Name what was checked.

   Concluding "no edge here" is a legitimate and common output of this gate. The failure it exists to
   prevent is holding a consensus view while believing it is a researched one, which leads to sizing
   the position as though it carried edge it does not have.

Then hand off to `smif-initiation-pipeline` for the full report, or to `dcf` for the valuation
build. This brief is the **intake layer** that should precede
any heavy modeling.

---

## The Practitioner Bridge

**Yartseva (2022) — The Alchemy of a Multibagger:** the connective tissue across all six paths. The
factors that compound into 10x+ returns are the ones where multiple lenses align: a high-quality,
well-governed, factor-favorable business that the market is mispricing for a nameable behavioral
reason, with durable (low-accrual) earnings. When all six paths point the same direction on one
name, that is the multibagger signal. Use it as the final synthesis check in Path 6.

**Confirmation-bias guard:** Alignment must be *discovered*, not *manufactured*. Do not stretch a
lens to make it agree. If four of six lenses align and two conflict, report the conflict — that is
more useful than a forced six-for-six. A genuine multibagger setup is rare; if every name you run
looks like one, the synthesis is being gamed.

---

## Anomaly Decay & Live Validity (apply to every quantitative lens)

These papers documented real effects, but **publication does not mean permanence**. Once an anomaly
is published and trafficked, capital crowds in and the edge often shrinks or inverts. Treat every
factor and accrual signal as a hypothesis about the present, not a law. Specific decay notes:

| Effect | Status today | Implication |
|---|---|---|
| **Accruals anomaly (Sloan)** | Weaker post-2002 as it became widely known | Still a quality screen; do not size a standalone trade on it alone |
| **Size premium (Fama-French SMB)** | Contested; weak/insignificant in several modern samples | Do not lean a thesis on small-cap premium as a given |
| **Value premium (HML)** | Endured a long drawdown through the 2010s before partial recovery | Regime-dependent; confirm it is currently being paid |
| **Momentum (Jegadeesh-Titman)** | Persists but suffers rare, severe crashes at turning points | Robust, but tail-risky; never lever it naively |
| **Sentiment (Baker-Wurgler)** | Regime-dependent by construction | Only meaningful relative to the current sentiment level |

**Rule:** When a lens relies on a documented anomaly, state (1) that the effect may have decayed and
(2) whether it is currently being paid in the market, using live data. An edge that was real in 1996
is not automatically real today. This is the difference between citing a paper and understanding it.

---

## Conflict Resolution Protocol (when lenses disagree)

Lenses will contradict each other — that is normal and informative. Do not average them into mush
or cherry-pick the convenient one. Resolve explicitly:

1. **State the conflict** plainly (e.g., "value lens says cheap; momentum lens says falling knife").
2. **Check horizon** — many conflicts are horizon artifacts (short-run momentum vs long-run reversal).
   Resolve by fixing the holding period the thesis actually targets.
3. **Weight by data quality** — a lens built on hard, dual-sourced filings outranks one built on a
   soft or single-sourced input.
4. **Weight by applicability** — a lens partially broken by Phase 0 (sector/edge-case) gets downgraded.
5. **If still unresolved,** the honest output is "mixed signal, here is the tension and what would
   break the tie," not a forced verdict. A clean answer manufactured from a genuine conflict is worse
   than an honest "it depends, on X."

---

## Pre-Flight Self-Check (run before presenting any output)

Verify every box before the analysis leaves your hands. If any fails, fix it or disclose it.

- [ ] Phase 0 ran: asset class valid, sector special-cases applied, edge-case math guarded.
- [ ] Every conclusion-driving number is live-sourced, dated, and dual-sourced (or flagged UNVERIFIED).
- [ ] Every analytical claim names its mechanism/paper.
- [ ] No single metric is acting as a verdict.
- [ ] Anomaly-decay caveat stated for any factor/accrual lens relied on.
- [ ] Lens conflicts resolved explicitly, not averaged or hidden.
- [ ] Thesis output includes a real bear case with kill criteria and a pre-mortem.
- [ ] Consensus stated as a number; variant view named with a magnitude, or "no edge" stated plainly.
- [ ] Persistence mechanism named for any claimed variant view.
- [ ] Derivative-view check run: no conclusion rests solely on a consensus-aggregating source.
- [ ] Every conclusion-driving figure carries its attribution tag per `decision-provenance`.
- [ ] No directive language (buy/sell/hold/target); not-advice note included.
- [ ] Output leads with the conclusion and fits one page.

---

## Guardrails (apply to every path, every output)

1. **Not investment advice.** This skill produces analytical framing, not recommendations. Never
   output "buy," "sell," "hold," "overweight," "underweight," "accumulate," or a price target framed
   as a directive. Present the evidence and the mechanism; let the user decide. Close any thesis-style
   output by noting it is educational analysis, not personalized financial advice.
2. **Source before you assert.** Every figure traces to a live source with a date (Phase 0, Check 3).
   No remembered numbers reach a conclusion.
3. **Name the mechanism or cut the claim.** Every analytical move cites the specific paper/mechanism
   behind it. A claim with no mechanism is opinion, not foundation.
4. **One metric is never a verdict.** No single ratio (accrual, B/M, momentum) decides a call.
   Require confirmation across the relevant lenses.
5. **Falsify before you conclude.** Any thesis-level output includes a real bear case (Path 6, step 7).
6. **Respect the applicability gate.** No academic mechanism runs on an asset class or sector it does
   not fit (Phase 0, Checks 1–2).

7. **Differentiate or say you did not.** Any thesis-level output states consensus as a number and either
   names where it differs and why that gap persists, or states plainly that the view is consensus. A
   well-argued restatement of the prevailing view is not research, however well argued.
8. **Attribute before you conclude.** Every conclusion-driving figure carries a `[SRC]`, `[CALC]`,
   `[MODEL]`, or `[HUMAN]` tag per `decision-provenance`. Material `[MODEL]` items ship only with human
   ratification recorded.

---

## Reference files

Load only what the path requires:

- `references/valuation-foundations.md` — Williams, M&M, Grossman-Stiglitz, Fama EMH
- `references/factor-anomalies.md` — Fama-French, Jegadeesh-Titman, LSV, De Bondt-Thaler
- `references/accounting-quality.md` — Sloan, Ball & Brown, Dechow, Penman-Zhang, Ou-Penman
- `references/behavioral-biases.md` — Kahneman-Tversky, Baker-Wurgler, BSV
- `references/corporate-governance.md` — Jensen, Jensen-Meckling, Tunneling, Kothari
- `references/analyst-microstructure.md` — Scharfstein-Stein, Abarbanell-Bernard, Bradshaw, Akerlof
- `references/emerging-markets.md` — Levine-Zervos, Bhattacharya, Durnev-Kim
- `references/consensus-divergence.md` — Grossman-Stiglitz applied live: the Path 6 step 8 divergence gate, cognitive convergence, derivative-view self-audit
- `references/worked-examples.md` — end-to-end walkthroughs showing each gate firing (load when a gate feels abstract or you want a run template)

Each reference file contains, per paper: the mechanism, the application checklist, what it changes
in a live analysis, and the failure modes to avoid.
