# Factor Anomalies & Return Drivers

The systematic, documented sources of cross-sectional return. Load for **Path 4 (Factor Diagnosis)**.

## Contents
1. Fama & French (1992) — Cross-Section of Expected Stock Returns
2. Jegadeesh & Titman (1993) — Returns to Buying Winners and Selling Losers
3. Lakonishok, Shleifer & Vishny (1994) — Value vs. Glamour / Contrarian Investment
4. De Bondt & Thaler (1985) — Does the Stock Market Overreact?

---

## 1. Fama & French (1992) — The Cross-Section of Expected Stock Returns

**Mechanism:** Market beta alone does not explain returns. Two additional factors do: **size**
(small caps outperform) and **value** (high book-to-market outperforms). The three-factor model is
the reference framework for decomposing what actually drives a stock.

**Application checklist:**
- Locate the stock on **book-to-market** (or E/P, FCF yield) relative to its sector. Is the thesis a value bet?
- Locate it on **size**. Does the thesis lean on a small-cap premium?
- Ask whether each premium is *currently being paid*. Factors go through long dry spells; a value
  bet in a growth-led regime is fighting the tape.

**What it changes:** Tells you which documented premium your return actually depends on, so you can
check whether that premium is alive right now.

**Failure modes:**
- Calling something a "value" stock on a single cheap multiple without confirming book-to-market or quality.
- Assuming the size premium pays in all regimes.

---

## 2. Jegadeesh & Titman (1993) — Returns to Buying Winners and Selling Losers

**Mechanism:** Over 3–12 month horizons, past winners keep winning and past losers keep losing.
Momentum is persistent, robust across markets, and survives transaction costs. Price action carries
information.

**Application checklist:**
- Check the 12-month (skip most recent month) price trend. Is the stock a winner or loser?
- If your fundamental thesis fights strong momentum, the catalyst and timeline must be explicit —
  you are betting against a documented force.
- Momentum and value often conflict (cheap stocks are cheap because they fell). Decide which you
  are actually playing.

**What it changes:** Stops you from anchoring purely on fundamentals while ignoring that price
trend is itself a signal. Sharpens entry timing.

**Failure modes:**
- Catching a falling knife: buying a value name with deeply negative momentum and no catalyst.
- Ignoring that momentum reverses sharply at turning points (links to De Bondt-Thaler at longer horizons).

---

## 3. Lakonishok, Shleifer & Vishny (1994) — Value vs. Glamour / Contrarian Investment

**Mechanism:** The value premium is behavioral, not just risk-based. Investors over-extrapolate:
they bid up "glamour" stocks with strong past growth and dump out-of-favor names, pushing prices
too far. Cheap stocks outperform because expectations embedded in them are too low.

**Application checklist:**
- Is the market extrapolating recent growth into perpetuity (glamour) or recent weakness (value)?
- Quantify the expectations gap: what growth/decline is the current price implying vs. a base rate?
- Look for mean-reversion candidates where extrapolation has overshot.

**What it changes:** Provides the *behavioral why* behind a value call, which is what makes it
defensible rather than a hope that "cheap goes up."

**Failure modes:**
- Confusing a value trap (cheap for a real, durable reason) with extrapolation-driven mispricing.
- Buying glamour at peak extrapolation because the story is compelling.

---

## 4. De Bondt & Thaler (1985) — Does the Stock Market Overreact?

**Mechanism:** Over 3–5 year horizons, prior extreme losers outperform prior extreme winners.
Investors overreact to dramatic news, and prices mean-revert once the overreaction fades. The
long-horizon contrarian counterpart to short-horizon momentum.

**Application checklist:**
- For multi-year theses, check whether the name is a long-horizon loser primed for reversal.
- Reconcile horizon with momentum: short-run momentum and long-run reversal coexist. State which
  horizon you are trading.
- Look for overreaction triggers: a single bad print, a narrative collapse, forced selling.

**What it changes:** Frames patient contrarian positions on a documented mean-reversion mechanism.

**Failure modes:**
- Mixing horizons: expecting reversal on a 6-month view where momentum still dominates.
- Treating every beaten-down stock as a reversal candidate without the overreaction trigger.

---

## Synthesis for Path 4

Factors are not a rainbow to cycle through — they encode meaning and they conflict. **Value (FF, LSV)
and momentum (JT) frequently point opposite ways; momentum (short horizon) and reversal (De Bondt,
long horizon) coexist.** A clean factor diagnosis states: where the stock sits on each factor, which
premium the return depends on, whether that premium is currently paid, and how horizon resolves any
value/momentum conflict. Add a quality overlay (see accounting-quality.md, Penman-Zhang) to separate
value from value trap.

> **EDGE-CASE GATE (read before computing):** Negative book value makes book-to-market
> uninterpretable — skip the value-factor read and say why; do not report a negative B/M as "deep
> value." Negative earnings make P/E meaningless — switch to EV/sales or FCF yield. Negative or
> near-zero equity breaks the ROE DuPont decomposition — do not force it. For financials, standard
> value multiples need sector-specific framing (P/B and ROE for banks, P/FFO for REITs), not the
> generic B/M read.

> **DECAY NOTE:** These factors are not perpetual-motion machines. The **size premium** is contested
> and weak in modern samples; the **value premium** endured a long drawdown through the 2010s;
> **momentum** persists but crashes hard at turning points. For any factor the thesis leans on, state
> that it may have decayed and confirm with live data whether it is *currently being paid* before
> treating it as an edge.
