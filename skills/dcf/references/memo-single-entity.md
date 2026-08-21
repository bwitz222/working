
# DCF: Single-Entity Valuation

**Output standard:** 1-page memo or 2–3 tightly formatted slides. Lead with the conclusion. Defend every assumption. Answer the MD's next question before they ask it. If it cannot be digested in 5 minutes, rewrite it.

---

## Guardrail Severity System

Tier definitions ([HARD STOP] / [FLAG] / [ALERT]) are in SKILL.md.

## Master Guardrail Registry

Reference list of all active guardrails by category. Each is also embedded at the relevant step.

### Mathematical / Logical Integrity
- **G-01 [HARD STOP]** WACC ≤ g: Terminal value is infinite or negative. Model is broken.
- **G-02 [HARD STOP]** Scenario weights do not sum to 100%.
- **G-03 [HARD STOP]** Bear case implied value ≥ base case, or bull case implied value ≤ base case. Scenarios are logically inverted.
- **G-04 [HARD STOP]** WACC < risk-free rate. Cost of capital cannot be below the risk-free rate.
- **G-05 [HARD STOP]** Net debt sign error: net cash position being subtracted rather than added in the equity bridge.
- **G-06 [HARD STOP]** Shares outstanding basis is not fully diluted (options, RSUs, converts, warrants unaccounted for).
- **G-07 [HARD STOP]** Mixed discounting conventions within one model (mid-year and year-end applied simultaneously).
- **G-08 [HARD STOP]** Currency inconsistency: inputs denominated in different currencies without explicit FX conversion and stated assumption.

### WACC Component Guardrails
- **G-09 [HARD STOP]** Cost of equity (Ke) < cost of debt (Kd). Equity is residual and must carry more risk than debt in all but structurally unusual edge cases.
- **G-10 [FLAG]** Beta (β) < 0.5 or > 2.0 for an industrial company. Confirm with MD before using.
- **G-11 [FLAG]** ERP outside 3.0%–8.0%. State source and date; confirm if outside this range.
- **G-12 [FLAG]** WACC is outside sector reference range by more than 100bps in either direction.
- **G-13 [FLAG]** Effective tax rate used < 15% or > 38% without stated justification (jurisdiction, NOLs, deferred tax).
- **G-14 [FLAG]** D/(D+E) > 65% for a non-financial industrial. Covenant, refinancing, and rating risk; flag and confirm.
- **G-15 [ALERT]** Using spot capital structure when company is actively deleveraging or has recently recapitalized.

### Terminal Value Guardrails
- **G-16 [HARD STOP]** g > long-run nominal GDP growth for the company's primary market. Absolute ceiling.
- **G-17 [HARD STOP]** Terminal year FCF is negative. A perpetuity of negative cash flows produces a negative terminal value, destroying model validity.
- **G-18 [FLAG]** WACC − g spread < 1.0%. Terminal value is hyper-sensitive to small input changes; widen sensitivity range and flag.
- **G-19 [FLAG]** Terminal value > 85% of total enterprise value. Near-term cash flows are not the story.
- **G-20 [FLAG]** GGM-implied exit multiple and stated exit multiple diverge by more than 2.0x EBITDA. Reconcile before presenting both.
- **G-21 [FLAG]** Exit multiple > 20x EBITDA without a named, current pure-play comparable trading at that level.
- **G-22 [ALERT]** Terminal value between 65%–85% of EV. Note sensitivity dependence; widen sensitivity table.

### FCF Projection Guardrails
- **G-23 [FLAG]** Base case FCF is negative for 3 or more consecutive years without a stated inflection catalyst and timeline.
- **G-24 [FLAG]** Terminal year D&A > terminal year capex for a capital-intensive business. Implies infrastructure decay; unsustainable in perpetuity.
- **G-25 [FLAG]** Terminal year revenue growth rate used in projections does not equal g used in GGM. Internal inconsistency.
- **G-26 [FLAG]** Terminal year EBITDA margin has no precedent in the sector. Requires explicit justification.
- **G-27 [FLAG]** Perpetual working capital release assumed in terminal year. WC cannot be permanently released.
- **G-28 [ALERT]** FCF conversion (FCF / EBITDA) < 30% in terminal year without stated structural reason (high reinvestment, capital intensity).

### Scenario and Stress Guardrails
- **G-29 [FLAG]** All three scenarios imply upside to current price. Bear case must stress-test the thesis, not just a modest reduction in base assumptions.
- **G-30 [FLAG]** Bull and bear cases are within 10% of the base case. Scenarios lack meaningful differentiation.
- **G-31 [ALERT]** Bear case implies >40% downside to current price. Confirm with MD that this stress level is intentional.

### Data and Input Guardrails
- **G-32 [FLAG]** Model valuation date is more than 6 months stale relative to current date. Update or disclose.
- **G-33 [FLAG]** Shares outstanding changed >10% year-over-year without a stated explanation (buyback, issuance, convert, M&A).
- **G-34 [FLAG]** Net debt > 3.0x EBITDA for an investment-grade rated company. Potential covenant or refinancing risk.
- **G-35 [ALERT]** Macro data source is older than 90 days. Note staleness; re-pull if rate environment or growth outlook has shifted materially.

---

## Step 0: Routing Questions

Ask all of the following in one compact block. Do not begin any analysis until answered.

1. **Company + ticker?**
2. **Sector?** Default: Industrials. Confirm or override.
3. **Document type?** Memo / Initiation report section / PT update note / Morning commentary / Client presentation / Internal use
4. **Tone?** Technical (WACC derivation shown, formula-level) or Executive summary (conclusion-first, driver callouts, no formula detail)
5. **Initiation or model update?** If update: what changed? (earnings, guidance, macro, model refresh)
6. **Valuation lenses alongside DCF?** State sector defaults and ask to confirm or change.
   - Industrials defaults: EV/EBITDA comps, EV/EBIT, P/E, precedent transactions, FCF yield
   - Non-Industrials: state defaults when sector confirmed
7. **SOTP check:** Are there materially distinct business segments? If yes, recommend dcf-sotp.
8. **Geographic exposure:** Is HQ non-US, or non-US revenue > ~30%? If yes: ask whether to use a non-US or blended risk-free rate.
9. **Scenario weights:** Default Bull 25% / Base 55% / Bear 20%. Confirm or adjust.

**Guardrail at routing:**
- **G-02** If weights provided do not sum to 100%, stop and correct before proceeding.
- If SOTP check raises doubt, present both options and let MD decide before committing to single-entity framework.

---

## Step 1: Macro Thesis Pull

Search the web for current macro data. Cite every source with publication date.

**Primary sources:**
- Fed / FOMC: Latest statement, SEP dot plot, Chair press conference
- Goldman Sachs, JPMorgan, Morgan Stanley: Most recent US macro or sector outlook
- IMF World Economic Outlook: Current edition
- BIS Quarterly Review: If credit or leverage conditions are relevant to the thesis
- ECB / Bank of England: If European exposure confirmed in routing
- NBER, Peterson Institute, Brookings: For structural or secular calls

**Extract and log:**
- 10Y UST yield (Rf baseline) — state exact observation date
- Near-term US GDP growth consensus range
- Core inflation trajectory and Fed terminal rate expectations
- Forward rate curve (1Y, 2Y, 5Y UST) for discount rate sensitivity context
- Sector-specific inputs relevant to the company: commodity prices, input cost inflation, capex cycle signals, M&A activity, regulatory environment

**Active guardrails:**
- **G-35 [ALERT]** If freshest available macro source is older than 90 days, note this explicitly in the output and state whether the rate environment or growth outlook has shifted materially since publication.
- If major sources conflict on rate path or growth trajectory, state the conflict, name which source you are anchoring to, and justify the choice.

---

## Step 2: FCF Definition

Select the FCF convention appropriate to the sector and company. State the choice and defend it before modeling begins.

**General fallbacks:**
- **FCFF** (Free Cash Flow to Firm): Use when capital structure is complex, in flux, or significantly leveraged. Discount at WACC. Bridge to equity value by subtracting net debt.
- **FCFE** (Free Cash Flow to Equity): Use when capital structure is stable and simple. Discount at cost of equity directly.

**Sector-specific variants — justify every choice:**

| Sector | Preferred FCF Convention | Key Note |
|--------|--------------------------|----------|
| Industrials (general) | FCFF; maintenance vs. growth capex split | Flag if capex cycle is the thesis driver |
| Defense & Aerospace | FCFF with backlog-adjusted revenue visibility | Funded backlog anchors near-term FCF |
| Capital Goods / Machinery | FCFF; working capital intensity matters | Normalize WC through cycle |
| Transportation & Logistics | FCFF or EBITDA–CapEx proxy | Asset intensity drives convention choice |
| Utilities / Regulated | RAB-based + allowed ROE | DCF is supplemental, not the anchor |
| REITs | AFFO | Depreciation is not economically meaningful |
| E&P / Energy | Reserve-based NAV or PV10 | FCF supplements reserve life analysis |
| Financial Services | DDM or excess return model | Standard DCF is structurally inappropriate; explain why to MD |
| SaaS / Technology | Unlevered FCF with ARR/churn bridge | Always adjust for stock-based compensation |

**Notify MD:** "Using [method] because [reason]. Alternative: [other method] would imply [difference]. Override if preferred."

**Active guardrails:**
- **G-05 [HARD STOP]** Confirm net debt sign before bridging: net cash is added to equity value, net debt is subtracted. Confirm the sign and the components (gross debt minus cash and equivalents) before proceeding.
- **G-06 [HARD STOP]** Confirm share count basis is fully diluted — include in-the-money options, unvested RSUs, convertible notes, warrants. State diluted share count and source.
- **G-08 [HARD STOP]** Confirm all inputs are in a single currency. If the company reports in a non-USD currency, state the FX assumption and source.

---

## Step 3: Forecast Horizon

Select horizon based on sector and company stage. Defend the choice.

| Sector | Default Horizon | Rationale |
|--------|----------------|-----------|
| Industrials | 10 years | Long capex cycles; terminal value anchor is meaningful at Year 10 |
| Defense & Aerospace | 10 years | Program visibility; long contract cycles |
| Technology | 7–10 years | Justify explicitly if using less than 10 |
| Healthcare / Pharma | 10–15 years | Pipeline optionality and patent cliffs require extended view |
| Energy / E&P | Reserve life or 10Y | Terminal value anchored to depletion schedule |
| Utilities | 10 years | Regulatory predictability supports full horizon |
| Consumer | 5–7 years | Shorter visibility; comps typically anchor valuation |

**Active guardrails:**
- **[FLAG]** Any deviation more than 2 years from sector default requires a stated rationale and MD confirmation before proceeding.
- **[FLAG]** If company is in secular decline, a shorter horizon paired with an explicit wind-down or asset-sale terminal value may be more appropriate than a perpetuity. Flag and ask.

---

## Step 4: Nominal vs. Real Cash Flows

**Default: Nominal.** Standard for Industrials and most equity research.

**Flag and ask routing question if any of the following apply:**
- Revenue is inflation-linked (regulated infrastructure, defense cost-plus, CPI-indexed contracts)
- Commodity price exposure is the primary value driver
- Material cross-border operations where real/nominal rate divergence is significant

**Active guardrail:**
- **G-07 [HARD STOP]** Convention must be applied consistently throughout. Mixing nominal projections with a real discount rate, or vice versa, is a methodology error that inflates or destroys value mechanically. Confirm once at this step and do not deviate.

State the convention chosen in the model header. Never leave it implicit.

---

## Step 5: WACC Build

Walk through every component. Show the calculation. Defend each assumption against its benchmark.

### Cost of Equity (CAPM)
```
Ke = Rf + β × ERP + Size Premium (if applicable) + Company-Specific Premium (if warranted)
```

**Risk-Free Rate (Rf)**
- Use 10Y UST yield from Step 1. State observation date.
- Non-US exposure flagged in routing: use blended rate or local sovereign; state rationale and weights.

**Beta (β)**
- Prefer 2-year weekly regression (reflects current capital structure).
- Use 5-year monthly if a major restructuring, M&A, or leverage event distorts the 2-year window. State which regression and why.
- If using unlevered sector beta: re-lever to current capital structure before applying.
- State the comparable set if using a sector/peer beta.
- **G-10 [FLAG]** β < 0.5 or > 2.0 for an industrial: flag, state the regression output, and confirm with MD.

**Equity Risk Premium (ERP)**
- Pull Damodaran's current implied ERP from web. Cite date.
- **G-11 [FLAG]** If ERP is outside 3.0%–8.0%, state the value, the source, and ask MD to confirm before using.

**Size Premium**
- Apply for small and mid-cap per Duff & Phelps / Kroll tables. State decile and premium in bps.
- Skip for large-cap (market cap > $10B).

**Company-Specific Premium**
- Ask routing question if any of the following are present: single-customer concentration, active litigation, execution risk on a major program, recent covenant breach, management transition.

**Cost of Equity output check:**
- **G-09 [HARD STOP]** If Ke < Kd (after-tax), stop immediately. Equity must be riskier than debt. Identify which input is wrong and correct it.
- **G-04 [HARD STOP]** If WACC < Rf, stop immediately. WACC cannot be below the risk-free rate.

### Cost of Debt (Kd)
- Use yield on outstanding bonds (state maturity and coupon) or credit spread + Rf for illiquid issuers.
- After-tax: `Kd(post-tax) = Kd × (1 − marginal tax rate)`
- **G-13 [FLAG]** If effective tax rate < 15% or > 38%: state the jurisdiction, any NOLs, or deferred tax assets driving the divergence. Confirm before applying.

### Capital Structure
- Use normalized/target capital structure — not spot. State the normalization basis (3-year average, management target, peer median).
- **G-15 [ALERT]** If spot capital structure is distorted by a recent transaction or recapitalization, note this and state when the capital structure is expected to normalize.
- **G-14 [FLAG]** If D/(D+E) > 65% for a non-financial industrial, flag potential covenant, refinancing, and rating risk. Ask MD whether to model a step-down WACC as leverage decreases.
- State D/(D+E) and E/(D+E) at market values.

### WACC Output
```
WACC = (E/V × Ke) + (D/V × Kd × (1−T))
```
Present as base case ± 50bps range. State all components in a summary table.

**G-12 [FLAG]** If WACC is outside the sector reference range below by more than 100bps, flag and confirm.

**Industrials WACC Reference Ranges:**

| Sub-Sector | Typical WACC Range |
|------------|-------------------|
| Large-cap diversified industrial | 7.5%–9.5% |
| Defense & Aerospace | 7.0%–8.5% |
| Capital Goods / Machinery | 8.0%–10.0% |
| Transportation & Logistics | 7.5%–9.5% |
| Building Products / Construction | 8.5%–10.5% |
| Specialty Industrial / Niche | 9.0%–11.0% |

Non-Industrials: pull sector WACC benchmarks from web (Damodaran sector data) and cite source.

---

## Step 6: FCF Projections and Cycle Normalization

### Projection Structure

| Period | Approach |
|--------|----------|
| Year 1–2 | Anchor to consensus; state any deviations and why |
| Year 3–5 | Management guidance + analyst assumptions; state key drivers |
| Year 6–10 | Explicit fade toward terminal; state fade rate |

**Always state for each period:**
- Revenue growth (Year 1–5 CAGR and terminal rate)
- EBITDA margin trajectory (entry, midpoint, exit)
- Capex intensity (% of revenue; maintenance vs. growth split where material)
- Working capital assumption (NWC as % of revenue, or explicit DSO/DPO/DIO)
- D&A treatment
- Tax rate

### Cycle Normalization (Industrials and Cyclicals)
- Normalize EBITDA margins through the cycle using a 5–7 year historical average, then overlay a forward adjustment for structural changes.
- State current cycle position explicitly: mid-cycle, trough, or peak. This affects near-term FCF materially.
- Flag if near-term FCF is distorted by a one-time event (facility buildout, inventory draw or build, large working capital swing).

**Active guardrails:**
- **G-23 [FLAG]** Base case FCF negative for 3+ consecutive years: state the specific inflection catalyst, timeline, and confidence level. If no clear catalyst exists, model the bear case as FCF-negative and revisit the base.
- **G-24 [FLAG]** Terminal year D&A > terminal year capex for a capital-intensive business. Flag as unsustainable in perpetuity. Ask MD whether to adjust.
- **G-25 [FLAG]** Terminal year revenue growth rate in the projection does not equal the g used in GGM. Reconcile before proceeding.
- **G-27 [FLAG]** If working capital release is assumed in the terminal year, flag. WC cannot be permanently released in perpetuity.
- **G-28 [ALERT]** FCF conversion (FCF / EBITDA) < 30% in terminal year: note structural reason (capex intensity, high reinvestment) or adjust.

---

## Step 7: Terminal Value — Both Methods Required

Both GGM and Exit Multiple must be presented. Never present only one without the other.

### Method 1: Gordon Growth Model
```
TV = FCF(n+1) / (WACC − g)
```
- **G-16 [HARD STOP]** g must not exceed long-run nominal GDP growth for the company's primary market. This is an absolute ceiling. If inputs imply otherwise, stop and ask MD to revise before proceeding.
- **G-01 [HARD STOP]** If WACC ≤ g, the denominator is zero or negative. The model is broken. Do not produce output. Stop and correct.
- **G-17 [HARD STOP]** If terminal year FCF is negative, stop. A negative perpetuity destroys model validity. Revisit terminal margin and capex assumptions.
- **G-18 [FLAG]** If WACC − g < 1.0%: terminal value is hyper-sensitive to small assumption changes. Widen sensitivity range, explicitly note this in output, and confirm assumptions with MD.
- Default g for mature industrials: long-run nominal GDP minus 0.5%–1.0%.
- High-quality compounder with durable competitive advantage: ask routing question before applying g above sector median.

### Method 2: Exit Multiple
```
TV = EBITDA(n) × Exit Multiple
```
- Anchor to current sector trading range and 10-year historical average.
- Apply a 0.5–1.0x discount to current multiple if mean reversion is expected and justified.
- State the comparable set and its median multiple explicitly.
- **G-20 [FLAG]** If GGM-implied exit multiple and stated exit multiple diverge by more than 2.0x EBITDA: investigate the source of the gap and reconcile before presenting both to MD.
- **G-21 [FLAG]** Exit multiple > 20x EBITDA: name a specific, current pure-play comparable trading at that level. If none exists, reduce the multiple or escalate to MD.

### Sensitivity Table (always generate)
5×5 grid, two versions side by side:
- **GGM grid:** Rows = WACC at base, ±50bps, ±100bps. Columns = g at base, ±25bps, ±50bps.
- **Exit Multiple grid:** Rows = WACC at base, ±50bps, ±100bps. Columns = Exit multiple at base, ±0.5x, ±1.0x.
- Highlight base case cell in both grids.

**Narrative (required):** "Implied equity value ranges from $[low] to $[high] per share across the sensitivity range. At base WACC of [W]% and terminal growth of [g]%, implied price is $[PT], representing [Z]% upside/downside to current levels of $[current price]."

**TV concentration check:**
- **G-19 [FLAG]** TV > 85% of EV: Hard flag. State: "Terminal value represents [X]% of total enterprise value. Near-term cash flows are not supporting this valuation. Assumptions are highly sensitive — widen the sensitivity range and confirm growth inputs with MD before distributing."
- **G-22 [ALERT]** TV between 65%–85% of EV: Note in output and ensure sensitivity table communicates the range clearly.

---

## Step 8: Bull / Base / Bear Scenarios

Probability-weighted average is the price target.
```
Price Target = (P_bull × V_bull) + (P_base × V_base) + (P_bear × V_bear)
```
Default weights: Bull 25% / Base 55% / Bear 20%. Confirm with MD.

### Scenario Driver Table (required)

| Driver | Bull | Base | Bear |
|--------|------|------|------|
| Revenue CAGR (Yr 1–5) | [above base] | [consensus anchor] | [below base] |
| EBITDA Margin | [expansion / peak] | [normalized] | [compression / trough] |
| WACC | [base −50bps] | [base] | [base +100bps] |
| Terminal Growth (g) | [base +25bps] | [base] | [base −50bps] |
| Implied PT | $[X] | $[Y] | $[Z] |
| vs. Current Price | [+X%] | [+Y%] | [−Z%] |

### Downside Stress — Both Levers Required

**1. Input stress:**
- WACC up 100–150bps
- Terminal growth down 50–100bps
- State implied PT and % downside under this stress

**2. FCF stress:**
- EBITDA margin compression (state bps haircut)
- Capex intensity increase (state % of revenue step-up)
- Revenue miss (state % below base)
- State which lever is the binding constraint

### Distress Scenario
Routing question: "Should I model a distress or impairment scenario alongside the bear case? [Yes / No]"
If yes:
```
Blended Bear = (1 − p_distress) × Going Concern Bear + p_distress × Recovery Value
```
State p(distress) and recovery value assumption with justification.

**Active guardrails:**
- **G-02 [HARD STOP]** Scenario weights must sum to 100%. Check before any output.
- **G-03 [HARD STOP]** Bear case implied value ≥ base case, or bull case implied value ≤ base case: scenarios are logically inverted. Identify and correct the input error before proceeding.
- **G-29 [FLAG]** All three scenarios imply upside to the current price. Bear case is not stressing the thesis — it is a mildly reduced base. Rebuild the bear case with genuine downside assumptions.
- **G-30 [FLAG]** Bull and bear are within 10% of base: differentiation is insufficient. Widen scenario assumptions.
- **G-31 [ALERT]** Bear case implies > 40% downside: confirm with MD this level of stress is intentional.

---

## Step 9: Consensus Tension Flags

After building all assumptions, run the following checks. Every flag requires a routing question and MD confirmation before the output is finalized.

| Check | Condition | Action |
|-------|-----------|--------|
| Terminal growth vs. sector | g > 150bps above sector median | "Your g of [X]% is [Y]bps above the sector median of [Z]%. Justify with competitive positioning or reduce." |
| WACC vs. sector range | WACC > 150bps below sector floor | "Your WACC of [X]% is [Y]bps below the [sector] floor of [Z]%. Confirm capital structure and beta inputs." |
| Near-term revenue vs. consensus | Year 1–3 growth > 2× consensus | "Your growth of [X]% is [Y]× consensus [Z]%. Is this a deliberate differentiation or a model error?" |
| EBITDA margin vs. comps | Margin > 300bps above or below sector median | "Your [Year X] margin of [Y]% is [Z]bps [above/below] sector comps. Quantify the structural reason or adjust." |
| Terminal value concentration | TV > 75% of EV | "Terminal value is [X]% of EV. The valuation is driven almost entirely by terminal assumptions. Confirm growth inputs." |
| Market-implied assumptions | Back-solve at current price | Always state: "At the current price of $[X], the market is implying WACC [Y]% / g [Z]% / exit multiple [M]x — which requires [assumption] to hold." |

---

## Step 10: Peer Valuation and Premium / Discount Analysis

Present DCF-implied multiples versus the comparable set.

- DCF-implied EV/EBITDA vs. sector comp median
- DCF-implied P/E vs. sector comp median
- DCF-implied FCF yield vs. sector comp median

For each metric, address:
- Is the premium or discount justified? (growth CAGR differential, ROIC premium, moat quality, balance sheet strength)
- Which 2–3 variables are most responsible for the gap? Bold those in the output.
- What does the current market price imply? (back-solve as above)

---

## Step 11: Risk Factor Page

Generate as a separate section. Always include. Always quantify where possible.

### Upside Risks (3–5 bullets, quantified)
Sector-relevant examples for Industrials:
- Accelerated capex supercycle or infrastructure program spend (state $ size if public)
- Market share gain from competitor capacity rationalization
- Accretive M&A at below-sector multiples (state balance sheet capacity)
- Input cost deflation (state commodity sensitivity: $X EPS impact per Y% move)
- Buyback or dividend capacity above base case (state FCF yield and capacity)

### Downside Risks (3–5 bullets, quantified)
Categories — always evaluate each:
- Regulatory / policy risk (tariffs, ITAR, environmental, permitting delays)
- Competitive displacement (pricing pressure, technology substitution, new entrant)
- Balance sheet / leverage risk (covenant thresholds, refinancing at higher rates, rating downgrade trigger)
- Execution / management risk (integration, program cost overrun, management turnover)
- Macro / cycle risk (PMI contraction, capex freeze, destocking cycle)
- ESG / stranded asset risk (flag if sector-relevant; state potential impairment magnitude)

### Key Model Assumptions — Sensitivity Ranking
State the 5–7 most consequential assumptions in plain language. Rank by impact: which assumption, if wrong by 10%, moves the price target most?

---

## Step 12: Disclosure Language

### Methodology Disclosure (always include)
> "Our [X]-year DCF uses a WACC of [Y]% (cost of equity [Z]%, after-tax cost of debt [W]%), a terminal growth rate of [g]% (Gordon Growth Model), and an exit multiple of [M]x EBITDA. We use [FCFF / FCFE / variant] in nominal terms. All projections are estimates subject to material uncertainty."

### Forward-Looking Statements (all client-facing documents)
> "This analysis contains forward-looking statements based on assumptions and estimates. Actual results may differ materially from those projected."

### Research Independence
Routing question: "Is this for external distribution? Should I include your firm's standard research independence disclosure? [Yes / No / Add manually]"

---

## Step 13: Output Format

### One-Page Memo (default for quick reads)
Rigid structure — no exceptions:

1. **Headline (1 sentence):** [Rating] [Ticker]: Price target $[X], implying [Y]% [upside/downside]
2. **Thesis (3 bullets):** Why buy/sell/hold. Most important bullet first.
3. **Valuation summary table:** Base PT / Bull PT / Bear PT / Probability-weighted PT / Current price / % upside or downside
4. **Key assumptions (4–6 lines):** WACC, terminal growth, revenue CAGR, EBITDA margin trajectory, FCF convention
5. **Sensitivity range (1 line):** "$[low]–$[high] per share across WACC / terminal growth sensitivity"
6. **Valuation vs. peers (2 lines):** Implied EV/EBITDA vs. comps median; premium or discount and why
7. **Top 2 upside risks / top 2 downside risks**
8. **Disclosure (1–2 lines)**

### 2–3 Slide Format
- **Slide 1:** Headline, thesis (3 bullets), scenario summary table, bull/base/bear range visual
- **Slide 2:** WACC build summary table, key FCF assumptions, 5×5 sensitivity table, TV as % of EV
- **Slide 3:** Risk factors (upside + downside), peer valuation comp table, disclosure

### Non-Negotiable Output Rules
- First sentence contains the price target and thesis. No exceptions.
- Every number has a stated reason.
- No filler language or preamble.
- Always answers: "What does the market need to believe for the current price to be fair?"
- If it does not pre-empt a question the MD would ask in the next five minutes, remove it.

---

## Quality Benchmark

A passing output from this skill:
- States price target and thesis in sentences 1–2
- Defends every material assumption without being asked
- Flags every tension with consensus before the MD notices it
- Answers what is priced in at current levels
- Quantifies the most important upside and downside risks
- Can be read completely in under 5 minutes
- Would not embarrass a senior MD in front of a buy-side PM
