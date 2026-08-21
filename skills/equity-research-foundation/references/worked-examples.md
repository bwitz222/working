# Worked Gate Examples

Concrete walkthroughs that show each gate firing. Load when you want a model for how a path should
actually run end to end, or when a gate feels abstract. Numbers below are **illustrative placeholders**
to show the reasoning shape — in a live run, every figure must be sourced per Phase 0, Check 3.

---

## Example A — Phase 0 catches a bank (Scenario 1)

**Request:** "Check the earnings quality on a large-cap bank."

**Wrong run (what the skill must NOT do):**
> Accrual ratio = (NI − CFO) / Total Assets = high → red flag on earnings quality.

This is meaningless. A bank's cash flow statement does not separate operating accruals the way an
industrial's does; provisioning and balance-sheet growth dominate.

**Correct run:**
1. Phase 0 Check 2 fires: sector = bank → Sloan accrual ratio is invalid.
2. Substitute: loan-loss provisioning trend (rising/falling vs charge-offs), NPL formation, coverage
   ratio, net interest margin trajectory, reserve adequacy.
3. Output: "Earnings quality for a lender is assessed through provisioning and credit metrics, not
   the accrual ratio. [Sourced figures here.] Verdict: ___."

**Lesson:** the gate changes the metric, not just adds a caveat.

---

## Example B — Edge-case math on a negative-equity name (Scenario 2)

**Request:** "Factor exposure for [unprofitable growth company with negative book equity]."

**Correct run:**
1. Phase 0 Check 4 fires: equity is negative → ROE DuPont and book-to-market are undefined.
2. Disable the value-factor and ROE reads; say why explicitly. Do not report a negative B/M as
   "extreme value."
3. Substitute: EV/sales vs peers, gross-margin trajectory, Rule-of-40-style unit economics, cash
   runway. Note the stock is effectively a duration/optionality bet, not a value-factor play.
4. Momentum and sentiment lenses still apply and may be the real story.

**Lesson:** a broken denominator is "undefined," never "high" or "low."

---

## Example C — Recommendation guardrail (Scenario 4)

**Request:** "Should I buy NVDA? Build me the thesis."

**Correct run:**
1. Run the relevant paths (factor, earnings quality, behavioral) on live data.
2. Present the bull case AND the mandatory bear case with kill criteria.
3. **Reframe the directive:** do not answer "yes/buy." Output the evidence and the mechanisms, state
   the key tensions, and close with: "This is educational analysis of the setup, not a recommendation
   or personalized financial advice. The buy/sell decision and position sizing are yours."

**Lesson:** the skill arms the decision; it never makes it.

---

## Example D — Falsification with teeth (Scenario 6)

**Request:** "Build the multibagger case for [name]."

**Weak bear case (rejected):** "Competition could increase and the macro could turn."

**Bear case with teeth (required):**
- *Specific:* "The value re-rating depends on margin recovery to 20%; if gross margin stays sub-15%
  for two more quarters, the thesis breaks. The accrual ratio is elevated, so the recent 'beat' may
  reverse next quarter."
- *Kill criteria:* (1) gross margin < 15% in the next two prints; (2) promoter pledge > 30%; (3) the
  re-rating does not begin within ~9 months of the [named] catalyst.
- *Pre-mortem:* "18 months out, the most likely failure is that the margin recovery was a one-off
  cost deferral, not structural — and signs of that are already visible in rising payables today."

**Lesson:** if you can't name what proves you wrong, you don't have a thesis.

---

## Example E — Anomaly decay applied (any factor path)

**Request:** "Is this a value play? It's trading at half its sector multiple."

**Correct run:**
1. Compute the value read on live, dual-sourced multiples.
2. Apply the decay note: "The value premium endured a long drawdown through the 2010s and is
   regime-dependent. Cheap alone is not an edge."
3. Confirm with the quality overlay (Penman-Zhang): is this durable cheapness or a value trap?
4. Check whether value is *currently being paid* in the market before treating the discount as
   opportunity rather than justified.

**Lesson:** cite the paper, then check whether the effect still pays today.
