# Accounting Quality & Earnings Analysis

How to tell whether reported earnings are real, durable, and worth modeling. Load for
**Path 1 (Earnings Quality Audit)**.

## Contents
1. Sloan (1996) — Accruals Anomaly
2. Ball & Brown (1968) — Accounting Income Numbers
3. Dechow, Ge & Schrand (2010) — Earnings Quality
4. Penman & Zhang (2002) — Persistence of Earnings
5. Ou & Penman (1989) — Financial Statement Analysis and Stock Returns

---

## 1. Sloan (1996) — Do Stock Prices Fully Reflect Accruals and Cash Flows?

**Mechanism:** Earnings split into a cash component and an accrual component. The accrual component
is **far less persistent** — it reverses. But the market prices both as equally durable, so
high-accrual firms are systematically overvalued and underperform; low-accrual firms outperform.
The most actionable earnings-quality result in the literature.

**Application checklist:**
- Compute the **accrual ratio**: `(Net Income − Cash Flow from Operations) / Total Assets`.
  Large positive = earnings propped up by accruals = red flag.
- Balance-sheet version: change in non-cash working capital scaled by assets.
- High accruals + an earnings "beat" = suspect the beat is manufactured, not operational.
- The edge persists because the market under-weights this — see Bradshaw et al. in analyst-microstructure.md.

**What it changes:** Adjusts the FCF base in any DCF downward when accruals are inflating earnings;
reweights the growth pillar in a risk report.

**Failure modes:**
- Trusting a net-income beat without checking cash conversion.
- Ignoring that accruals reverse — this year's accrual boost is next year's drag.

> **SECTOR GATE (read before computing):** The Sloan accrual ratio is built for non-financial
> operating companies. It is **invalid for banks, lenders, and insurers** (no clean CFO/accrual
> split; provisions and float dominate) and **misleading for REITs** (depreciation is non-economic).
> For banks/lenders, assess loan-loss provisioning trend, coverage ratios, and NPL formation. For
> insurers, use reserve development and the combined ratio. For REITs, use FFO/AFFO. Never report a
> Sloan accrual ratio for these sectors — substitute the correct metric and say you did.

---

## 2. Ball & Brown (1968) — An Empirical Evaluation of Accounting Income Numbers

**Mechanism:** Earnings announcements carry real information — stock prices move on the surprise,
in the direction of the surprise. The founding paper of event-driven analysis and every earnings
model. Critically, the market's reaction **drifts** (post-earnings-announcement drift): prices keep
moving in the surprise direction for weeks after.

**Application checklist:**
- Identify the most recent earnings surprise magnitude and direction.
- Check for drift: has the market fully absorbed the surprise, or is it still re-rating? An
  incomplete reaction is a tradeable window.
- Build expectations explicitly — the surprise is vs. consensus, so know the consensus.

**What it changes:** Frames the earnings event as the primary information catalyst and identifies
whether drift is still in play.

**Failure modes:**
- Assuming the market instantly and fully prices a surprise (it does not — drift is real).
- Reacting to the headline number rather than the surprise vs. expectation.

---

## 3. Dechow, Ge & Schrand (2010) — Earnings Quality

**Mechanism:** The definitive survey of what "high-quality earnings" means: earnings that are
persistent, predictable, and backed by cash. Quality is multidimensional — persistence, smoothness
(can be manipulated), accrual quality, and the absence of manipulation incentives.

**Application checklist:**
- Persistence: do earnings recur, or are they boosted by one-offs?
- Cash backing: link to Sloan — are earnings cash or accrual?
- Smoothness: suspiciously smooth earnings in a volatile business signal management of the number.
- Manipulation incentives: near covenant thresholds, equity raises, executive comp triggers.

**What it changes:** Provides the full quality scorecard behind a single accrual flag; tells you
how much to trust the earnings stream you are about to capitalize.

**Failure modes:**
- Treating "smooth" as "stable" — it can mean managed.
- Checking accruals but ignoring manipulation incentives.

---

## 4. Penman & Zhang (2002) — The Persistence of Earnings (sustainability of ROE)

**Mechanism:** Not all ROE is equal. Sustainable profitability comes from durable competitive
advantage; transitory profitability fades. Conservative accounting choices can also temporarily
depress or inflate ROE in predictable ways. The key to separating durable compounders from
mean-reverting numbers.

**Application checklist:**
- Decompose ROE (DuPont): margin × turnover × leverage. Which driver is doing the work, and is it durable?
- Distinguish quality ROE (moat-driven) from leveraged or one-off ROE.
- This is the **quality overlay** that separates a value stock from a value trap (links to factor-anomalies.md).

**What it changes:** Determines whether high returns persist into the terminal value or fade —
directly governing the DCF's most valuable assumption.

**Failure modes:**
- Extrapolating a transitory ROE spike into perpetuity.
- Crediting leverage-driven ROE as if it were moat-driven.

---

## 5. Ou & Penman (1989) — Financial Statement Analysis and Stock Returns

**Mechanism:** A broad set of fundamental signals drawn directly from financial statements
systematically predicts future returns. Fundamental analysis, done systematically across many line
items, has measurable predictive power.

**Application checklist:**
- Don't rely on one ratio; build a composite of fundamental signals (margins, turnover, leverage trend, accrual quality).
- Look for confirmation across statements — income statement strength validated by balance sheet and cash flow.
- Use as the systematic backbone under a discretionary thesis.

**What it changes:** Justifies a multi-signal fundamental scorecard rather than a single-metric call.

**Failure modes:**
- Cherry-picking the one flattering ratio.
- Ignoring divergence between the income statement and the cash flow statement.

---

## Synthesis for Path 1

The audit runs: **is it cash or accrual (Sloan)** → **was the surprise fully priced (Ball & Brown
drift)** → **is the quality durable across dimensions (Dechow)** → **does the ROE persist
(Penman-Zhang)** → **do the signals confirm across statements (Ou-Penman)**. A name that passes all
five has earnings you can trust in a model. One that fails the Sloan test should have its FCF base
adjusted before any DCF.

> **DECAY NOTE:** The accruals anomaly weakened materially after ~2002 once it was widely published
> and traded. Treat the accrual ratio as a **quality screen**, not a standalone trade signal. State
> the decay caveat and confirm with live data whether high accruals are still being punished in the
> current regime before sizing anything on it.
