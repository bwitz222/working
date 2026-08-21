# Behavioral Finance

How investors actually decide, and where that creates exploitable mispricing. Load for
**Path 2 (Behavioral Bias Scan)**.

## Contents
1. Kahneman & Tversky (1979) — Prospect Theory
2. Baker & Wurgler (2006) — Investor Sentiment and the Cross-Section
3. Barberis, Shleifer & Vishny (1998) — A Model of Investor Sentiment

---

## 1. Kahneman & Tversky (1979) — Prospect Theory: An Analysis of Decision Under Risk

**Mechanism:** People do not evaluate outcomes rationally. They feel losses ~2x as intensely as
equivalent gains (**loss aversion**), evaluate outcomes relative to a **reference point** rather
than absolute wealth, and distort probabilities (overweight small probabilities, underweight
moderate ones). These shape how the crowd prices risk.

**Application checklist:**
- **Reference-point anchoring:** is the market anchored to a prior high, IPO price, or 52-week range
  rather than fundamental value? Anchors create stale prices.
- **Loss aversion:** are holders refusing to sell a loser (disposition effect), creating overhang?
  Or are they so scarred they have dumped a name below fair value?
- **Probability distortion:** is a low-probability catastrophe being overpriced (cheap optionality
  for you), or a low-probability jackpot being overpaid for (short candidate)?

**What it changes:** Identifies the precise cognitive error the price reflects, which becomes the
named edge in the thesis.

**Failure modes:**
- Assuming you are immune — your own reference points and loss aversion distort your call too.
- Naming "irrationality" generically instead of the specific mechanism.

---

## 2. Baker & Wurgler (2006) — Investor Sentiment and the Cross-Section of Stock Returns

**Mechanism:** Market-wide sentiment is a systematic factor. When sentiment is high, hard-to-value
and hard-to-arbitrage stocks (small, young, unprofitable, volatile, distressed) get overpriced and
subsequently underperform; when sentiment is low, those same stocks are primed to outperform.
Sentiment predicts the *cross-section*, not just the level.

**Application checklist:**
- Gauge the sentiment regime (positioning surveys, IPO volume, retail flows, speculative-asset behavior).
- Classify the name: is it sentiment-sensitive (speculative, hard to value) or sentiment-robust
  (stable, profitable, easy to value)?
- High-sentiment regime → lean away from speculative names, toward stable ones (and vice versa).

**What it changes:** Adds a market-cycle overlay to any single-name thesis; flags when a speculative
long is fighting a sentiment headwind.

**Failure modes:**
- Treating a single-name thesis as immune to the sentiment regime.
- Going long speculative names at a sentiment peak because the story is good.

---

## 3. Barberis, Shleifer & Vishny (1998) — A Model of Investor Sentiment

**Mechanism:** A unifying model explaining both anomalies at once. Investors **underreact** to news
in the short run (conservatism — they cling to priors, so prices drift, producing momentum and
PEAD) and **overreact** in the long run (representativeness — they extrapolate streaks, producing
reversal). One framework reconciles momentum and mean reversion.

**Application checklist:**
- Pin the horizon. Short-run news → underreaction → drift/momentum (links to Ball & Brown, Jegadeesh-Titman).
- Long-run streak → overreaction → reversal (links to De Bondt-Thaler, LSV).
- Diagnose which regime the name is in: fresh surprise being slowly absorbed, or a multi-year
  narrative that has over-extended?

**What it changes:** Resolves the apparent contradiction between momentum and reversal so the thesis
picks the right horizon and mechanism.

**Failure modes:**
- Expecting reversal during the underreaction window, or momentum during the overreaction window.
- Failing to state the horizon, leaving the bias claim incoherent.

---

## Synthesis for Path 2

A behavioral thesis must answer four things: **which bias (Kahneman-Tversky mechanism), which
horizon (BSV: underreaction short / overreaction long), which sentiment regime (Baker-Wurgler), and
what catalyst closes the gap.** A thesis that names its bias, horizon, and catalyst survives an IC
challenge. One that says "the market is wrong" does not. For consensus- and analyst-specific biases
(herding, forecast under-reaction), load analyst-microstructure.md.
