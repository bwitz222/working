
# DCF: Sum-of-the-Parts (SOTP) Valuation

**Output standard:** 1-page memo or 2–3 tightly formatted slides. Lead with total implied value, the SOTP bridge, and the conglomerate discount rationale. Defend every segment assumption. Ruthless, logical flow. Digestible in under 5 minutes.

---

## Guardrail Severity System

Tier definitions ([HARD STOP] / [FLAG] / [ALERT]) are in SKILL.md.

## Master Guardrail Registry

### SOTP Structure and Integrity
- **S-01 [HARD STOP]** Segment revenue or EBIT percentages do not sum to 100% (within ±1% rounding). Segment map is incomplete or double-counted.
- **S-02 [HARD STOP]** Using a single consolidated WACC across all segments in an SOTP model. This is a fundamental methodology error. Each DCF-valued segment requires a segment-appropriate WACC.
- **S-03 [HARD STOP]** Intercompany revenues, cost allocations, or transfer pricing between segments have not been identified or addressed. Gross-up without elimination overstates segment values.
- **S-04 [HARD STOP]** Currency mismatch across segments without explicit FX conversion and stated rate assumption.
- **S-05 [HARD STOP]** Net debt sign error in the SOTP bridge: net cash being subtracted instead of added.
- **S-06 [HARD STOP]** Shares outstanding are not fully diluted (options, RSUs, converts, warrants unaccounted for).
- **S-07 [FLAG]** Corporate overhead (unallocated central costs) has not been deducted from gross SOTP value. Omitting this overstates equity value.
- **S-08 [FLAG]** Minority interests, JV stakes, or non-consolidated affiliates not addressed. State treatment: include at proportionate value, exclude, or ask MD.
- **S-09 [FLAG]** Net debt allocated to individual segments rather than held at HoldCo level without explicit rationale. State the allocation method and basis.
- **S-10 [ALERT]** One segment contributes >60% of total gross SOTP value. Flag as concentration risk and confirm with MD that thesis is intended to rest on that segment.

### Mathematical / Logical Integrity (shared with dcf-single-entity)
- **G-01 [HARD STOP]** WACC ≤ g for any DCF-valued segment. Terminal value is infinite or negative. Model is broken.
- **G-02 [HARD STOP]** Scenario probability weights do not sum to 100%.
- **G-03 [HARD STOP]** Bear case implied SOTP value ≥ base case, or bull case ≤ base case. Scenarios are logically inverted.
- **G-04 [HARD STOP]** Any segment WACC < risk-free rate.
- **G-07 [HARD STOP]** Mixed discounting conventions (mid-year and year-end) applied within one segment or across segments inconsistently.

### Segment WACC Guardrails
- **G-09 [HARD STOP]** Ke < Kd for any segment. Equity must be riskier than debt.
- **G-10 [FLAG]** Segment beta (pure-play relevered) < 0.5 or > 2.0. Confirm comp set and re-levering calculation.
- **G-11 [FLAG]** ERP outside 3.0%–8.0%. State source and date; confirm if outside range.
- **G-12 [FLAG]** Any segment WACC outside its respective sector reference range by more than 100bps.
- **G-13 [FLAG]** Effective tax rate < 15% or > 38% without stated justification.
- **G-14 [FLAG]** Consolidated D/(D+E) > 65% for a non-financial industrial. Flag covenant and refinancing risk.

### Terminal Value Guardrails (per segment)
- **G-16 [HARD STOP]** Any segment g > long-run nominal GDP growth for that segment's primary market.
- **G-17 [HARD STOP]** Terminal year FCF negative for any DCF-valued segment.
- **G-18 [FLAG]** WACC − g < 1.0% for any segment. Terminal value is hyper-sensitive; widen sensitivity range.
- **G-19 [FLAG]** Any single segment's terminal value > 75% of that segment's DCF enterprise value.
- **G-20 [FLAG]** GGM-implied and stated exit multiples diverge by more than 2.0x for any segment.
- **G-21 [FLAG]** Exit multiple > 20x EBITDA for any segment without a named comparable.
- **S-11 [FLAG]** One segment's terminal value > 60% of total gross SOTP value. Concentration risk; confirm thesis.

### FCF Projection Guardrails (per segment)
- **G-23 [FLAG]** Base case FCF negative for 3+ consecutive years for any segment without a stated inflection catalyst.
- **G-24 [FLAG]** Terminal year D&A > terminal year capex for any capital-intensive segment.
- **G-25 [FLAG]** Terminal year revenue growth rate in projections does not equal g in GGM for that segment.
- **G-27 [FLAG]** Working capital release assumed in perpetuity for any segment.

### Scenario Guardrails
- **G-29 [FLAG]** All three scenarios imply upside to current price. Bear case is insufficient stress.
- **G-30 [FLAG]** Bull and bear cases within 10% of base. Scenarios lack differentiation.

### Conglomerate Discount Guardrails
- **S-12 [FLAG]** Conglomerate discount applied is outside 0%–20% of gross SOTP value without named structural justification. Discounts above 20% are unusual; confirm with MD.
- **S-13 [FLAG]** No conglomerate discount applied to a highly diversified conglomerate with no stated structural rationale for a premium or parity valuation.
- **S-14 [ALERT]** Gross SOTP value > 40% above current market cap with no identified catalyst (spin-off, activist, self-help, strategic review). Flag the gap and its implications.

### Data and Input Guardrails
- **G-32 [FLAG]** Model valuation date more than 6 months stale.
- **G-35 [ALERT]** Macro data source older than 90 days.

---

## Step 0: SOTP Routing Questions

Ask all of the following in one compact block. Do not begin any analysis until answered.

1. **Company + ticker?**
2. **Segment map?** List segments as currently understood. Ask MD to confirm, correct, or add. State assumed primary sector (default: Industrials).
3. **Segment materiality threshold?** Default: value any segment contributing > 5% of consolidated revenue or EBIT separately. Confirm or adjust.
4. **Document type?** Memo / Initiation report / PT update / Client presentation / Internal use / Break-up analysis / Spin-off analysis
5. **Tone?** Technical (full methodology per segment) or Executive summary (conclusion-first, segment summary table)
6. **Initiation or model update?** If update: what changed?
7. **Proposed methodology per segment:** State proposed methodology for each identified segment and ask MD to confirm before proceeding. (See Step 1 for methodology selection logic.)
8. **Conglomerate discount?** "Should I apply a conglomerate discount? [Yes / No / Estimate it for me]" If yes: structural, cyclical, or execution/management overhang?
9. **Corporate overhead?** Confirm unallocated corporate costs are known and will be deducted from gross SOTP value.
10. **Minority interests and JV stakes?** Identify any non-wholly-owned entities. State treatment.
11. **Net debt location?** Held at HoldCo, allocated to segments, or split? State basis.
12. **Geographic exposure per segment?** Flag any segment with non-US revenue > ~30%. Ask whether a non-US or blended risk-free rate applies.
13. **Scenario weights?** Default: Bull 25% / Base 55% / Bear 20%. Confirm or adjust.
14. **Single-entity check:** If segments share most cost structure, capital allocation, and management with no distinct pure-play comparables, flag: "This company may be better modeled with dcf-single-entity using segment margin assumptions. Proceed with SOTP or switch?"

**Active guardrails at routing:**
- **S-01 [HARD STOP]** If initial segment map percentages do not sum to ~100%, resolve before proceeding.
- **G-02 [HARD STOP]** If scenario weights provided do not sum to 100%, correct before proceeding.
- **S-07 [FLAG]** If corporate overhead is not yet known, flag: "Unallocated overhead must be identified and deducted before finalizing SOTP. Proceed with placeholder and confirm figures?"

---

## Step 1: Segment Map and Methodology Assignment

Before any modeling, produce a confirmed segment summary table. Do not proceed until MD approves.

| Segment | % Revenue | % EBIT | Proposed Methodology | Rationale |
|---------|-----------|--------|---------------------|-----------|
| [Seg A] | [X]% | [Y]% | [See logic below] | [Why] |
| [Seg B] | [X]% | [Y]% | [See logic below] | [Why] |
| [Seg C below threshold] | [X]% | [Y]% | Fold into "Other" or value separately? | [Ask MD] |

**Methodology selection logic:**

| Segment Type | Preferred Methodology | Key Note |
|-------------|----------------------|----------|
| Stable, cash-generative, mature | DCF (FCFF) | Full build with segment WACC and TV |
| High-growth, pre-profit | Revenue multiple or DCF with explicit terminal ramp | Justify growth premium explicitly |
| Asset-heavy / capital-intensive | EV/EBITDA or DCF with capex-intensive FCF | Maintenance vs. growth capex split |
| Regulated / utility-like | RAB-based + allowed ROE | DCF supplements, not anchors |
| Real estate / infrastructure | NAV or cap rate | AFFO if REIT-like characteristics |
| Financial services segment | P/TBV or excess return model | Standard DCF is inappropriate; flag and explain |
| IP / technology platform | DCF with ARR/churn bridge or royalty stream PV | Adjust for stock-based compensation |
| E&P / resource segment | PV10 / reserve-based NAV | FCF supplements reserve analysis |
| Turnaround / distressed | Probability-weighted recovery value | Apply distress probability explicitly |

**Active guardrails:**
- **S-02 [HARD STOP]** If MD requests a single WACC across all segments, flag this as a methodology error, explain why it distorts value, and ask MD to confirm or allow segment-specific WACCs.
- **S-03 [HARD STOP]** Before finalizing segment FCF builds: identify all intercompany revenues, shared cost allocations, and transfer pricing items. State how each is handled. Unaddressed eliminations overstate value.
- **S-08 [FLAG]** Minority interests and JV stakes: state whether included at proportionate consolidated value, shown as a separate line in the bridge, or excluded. Ask MD if unclear.

---

## Step 2: Macro Thesis Pull

Search the web for current macro data. Cite every source with publication date.

**Primary sources:**
- Fed / FOMC: Latest statement, SEP dot plot, Chair press conference
- Goldman Sachs, JPMorgan, Morgan Stanley: Most recent macro or sector outlook
- IMF World Economic Outlook: Current edition
- BIS Quarterly Review: If credit or leverage dynamics are relevant
- ECB / Bank of England: If European segment exposure confirmed in routing
- NBER, Peterson Institute, Brookings: For structural or secular macro calls

**Extract and log:**
- 10Y UST yield (Rf baseline) — state exact observation date
- Near-term US GDP growth consensus range
- Core inflation trajectory and Fed terminal rate expectations
- Forward rate curve (1Y, 2Y, 5Y UST)
- Segment-specific inputs: commodity prices, input cost inflation, regulatory signals, capex cycle data relevant to each confirmed segment

**Active guardrail:**
- **G-35 [ALERT]** If freshest macro source is older than 90 days, note this explicitly and state whether the rate environment has shifted materially since publication.
- If major sources conflict materially on rate path or growth outlook: state the conflict, anchor to one source, and justify the choice.

---

## Step 3: Segment-Level WACC Builds

Build a separate WACC for each DCF-valued segment. Segment-appropriate beta is required for each. A single consolidated WACC is a hard-stop methodology error (S-02).

For each DCF-valued segment:

### Cost of Equity
```
Ke(segment) = Rf + β(segment) × ERP + Size Premium (if applicable) + Segment-Specific Premium
```
- **β(segment):** Use a pure-play comparable beta re-levered to company capital structure. State the comparable set used for each segment.
- **ERP:** Damodaran current implied ERP (pull from web, cite date). Apply consistently across all segments.
- **Segment-specific premium:** Ask routing question if any segment carries idiosyncratic risk (single-customer, regulatory, execution, technology displacement).
- **G-10 [FLAG]** Any segment beta < 0.5 or > 2.0: flag and confirm comp set and re-levering math.
- **G-11 [FLAG]** ERP outside 3.0%–8.0%: confirm source and date.
- **G-09 [HARD STOP]** Any segment Ke < Kd: stop and correct.

### Cost of Debt
- Use company-level cost of debt unless segments have distinct debt tranches (project finance, secured asset-backed, ring-fenced entities). State assumption.
- After-tax: `Kd(post-tax) = Kd × (1 − marginal tax rate)`
- **G-13 [FLAG]** Effective tax rate < 15% or > 38%: state jurisdiction, NOLs, or deferred tax rationale. Confirm before applying.

### Capital Structure per Segment
- Allocate capital structure to each segment using asset value or EBIT-based weights. State the allocation method explicitly.
- **S-09 [FLAG]** If net debt is allocated to segments rather than held at HoldCo: state the allocation basis and confirm with MD. Misallocation leads to double-counting in the bridge.
- **G-14 [FLAG]** Consolidated D/(D+E) > 65%: flag covenant, refinancing, and rating risk. Ask whether a step-down WACC should be modeled.

### Segment WACC Reference Check
Cross-check each segment's WACC against its relevant sector reference range. Flag any outlier by more than 100bps and ask MD to confirm.

**Industrials Sub-Sector WACC Reference Ranges:**

| Sub-Sector | Typical WACC Range |
|------------|-------------------|
| Large-cap diversified industrial | 7.5%–9.5% |
| Defense & Aerospace | 7.0%–8.5% |
| Capital Goods / Machinery | 8.0%–10.0% |
| Transportation & Logistics | 7.5%–9.5% |
| Building Products / Construction | 8.5%–10.5% |
| Specialty Industrial / Niche | 9.0%–11.0% |

Non-Industrials segments: pull sector WACC benchmarks from web (Damodaran sector data) and cite source.

---

## Step 4: Segment FCF Builds

For each DCF-valued segment, build FCF projections independently. Do not aggregate until Step 5.

### Projection Structure per Segment

| Period | Approach |
|--------|----------|
| Year 1–2 | Segment-level consensus or reported guidance; state deviations and why |
| Year 3–5 | Analyst model assumptions; state key drivers per segment |
| Year 6–10 | Explicit fade toward terminal; state fade rate per segment |

**Always state per segment:**
- Revenue growth (Year 1–5 CAGR and terminal rate)
- EBITDA margin trajectory (entry, midpoint, exit)
- Capex intensity (% of revenue; maintenance vs. growth split)
- Working capital assumptions
- Intercompany eliminations: explicitly address shared cost allocations or transfer pricing before finalizing segment FCF

### Cycle Normalization (Cyclical Segments)
- Normalize EBITDA margins through the cycle for each cyclical segment independently using a 5–7 year historical average with a forward structural adjustment.
- State current cycle position per segment. Each segment can be at a different point in its cycle simultaneously — treat them independently.
- Flag if near-term FCF is distorted by a one-time event (facility investment, large working capital swing, integration cost).

**Active guardrails:**
- **G-23 [FLAG]** Base case FCF negative for 3+ consecutive years for any segment without a stated inflection catalyst.
- **G-24 [FLAG]** Terminal year D&A > terminal year capex for any capital-intensive segment.
- **G-25 [FLAG]** Terminal year revenue growth in projections ≠ g used in GGM for that segment. Reconcile.
- **G-27 [FLAG]** Working capital release assumed in perpetuity for any segment.
- **S-03 [HARD STOP]** All intercompany items must be identified and eliminated before FCF is finalized. Unaddressed eliminations overstate segment value.

---

## Step 5: Terminal Value — Both Methods per Segment

Apply both GGM and Exit Multiple to each DCF-valued segment. Non-DCF segments use their designated methodology from Step 1.

### GGM per Segment
```
TV(segment) = FCF(n+1) / (WACC(segment) − g(segment))
```
- Each segment gets its own g tied to segment-level GDP exposure and competitive positioning.
- **G-16 [HARD STOP]** No segment's g may exceed long-run nominal GDP growth for that segment's primary market.
- **G-01 [HARD STOP]** If WACC(segment) ≤ g(segment): the denominator is zero or negative. Stop and correct.
- **G-17 [HARD STOP]** If any segment's terminal year FCF is negative: stop. Negative perpetuity destroys model validity.
- **G-18 [FLAG]** WACC − g < 1.0% for any segment: flag hyper-sensitivity. Widen sensitivity range for that segment.
- Default g for mature industrial segments: long-run nominal GDP minus 0.5%–1.0%.

### Exit Multiple per Segment
- Use segment-specific pure-play comparable set — not consolidated company multiples.
- State the comp set for each segment.
- **G-20 [FLAG]** GGM-implied and stated exit multiples diverge by more than 2.0x for any segment: investigate and reconcile.
- **G-21 [FLAG]** Exit multiple > 20x EBITDA for any segment: name a specific current comparable. If none, reduce or escalate to MD.

### Sensitivity
- **Per segment (on MD request):** Individual 5×5 sensitivity grids for each DCF-valued segment.
- **Consolidated (always present):** 5×5 grid varying blended WACC ± and blended terminal growth ±. Highlight base case. State equity value range in narrative.

**Active guardrails:**
- **G-19 [FLAG]** Any segment's terminal value > 75% of that segment's DCF EV: flag sensitivity dependence.
- **S-11 [FLAG]** Any single segment's terminal value > 60% of total gross SOTP value: flag concentration risk and confirm with MD.

---

## Step 6: SOTP Bridge and Conglomerate Discount

### SOTP Bridge — Always Present

| Component | EV ($M) | Per Share ($) | Methodology / Notes |
|-----------|---------|---------------|---------------------|
| Segment A | $[X] | $[X/sh] | [DCF at WACC X%, g Y%] |
| Segment B | $[X] | $[X/sh] | [EV/EBITDA at Mx vs. [comps]] |
| Segment C | $[X] | $[X/sh] | [NAV / PV10 / other] |
| **Gross SOTP Value** | **$[Sum]** | **$[X/sh]** | |
| Corporate overhead (PV) | ($[X]) | ($[X/sh]) | Unallocated central costs capitalized at [WACC] |
| Conglomerate discount | ($[X]) | ($[X/sh]) | [%] — [rationale] |
| Minority interests | ($[X]) | ($[X/sh]) | [Proportionate value or exclusion basis] |
| JV / affiliate stakes | +/−$[X] | +/−$[X/sh] | [Methodology] |
| Equity options / dilutive instruments | ($[X]) | ($[X/sh]) | [Treasury stock or if-converted method] |
| Net debt / (net cash) | ($[X]) | ($[X/sh]) | Gross debt minus cash at [quarter-end date] |
| **SOTP Equity Value** | **$[X]** | **$[PT/sh]** | Fully diluted share count: [X]M |

**Active guardrails:**
- **S-07 [FLAG]** Corporate overhead not deducted: flag before finalizing. State placeholder if figures are uncertain.
- **S-05 [HARD STOP]** Net cash must be added (not subtracted) in the bridge. Confirm sign before output.
- **S-06 [HARD STOP]** Confirm share count is fully diluted. State diluted share count and dilutive instrument basis.
- **S-08 [FLAG]** Minority interests and JV stakes: state treatment explicitly. Exclusion without a reason is not acceptable.

### Conglomerate Discount

State the basis. Never apply a discount without explaining it.

| Type | Typical Range | Basis |
|------|--------------|-------|
| Structural | 10%–20% | Management bandwidth dilution, cross-subsidization, lack of pure-play multiple |
| Cyclical | 3%–10% | Segments in different cycle phases creating near-term drag; expected to compress |
| Execution / overhang | 5%–15% | Post-acquisition integration, succession risk, activist pressure |
| None (premium) | 0% or negative | Diversification provides genuine risk reduction or cross-segment synergy |

Routing question: "I'm proposing a [X]% conglomerate discount based on [rationale]. Confirm, increase, reduce, or remove?"

**Active guardrails:**
- **S-12 [FLAG]** Discount outside 0%–20% of gross SOTP without named structural justification: flag as unusual and confirm.
- **S-13 [FLAG]** No discount applied to a highly diversified conglomerate without a stated rationale.

### Unlock Case (always calculate if gap exists)
If gross SOTP > current market cap by >15%, calculate the separation value explicitly:
"Separation of [Segment X] could unlock $[Y]/share, representing [Z]% of current market cap. Catalyst required: [spin-off / strategic review / activist]."

**S-14 [ALERT]** Gross SOTP > 40% above current market cap with no identified catalyst: flag and note that assumptions may be too optimistic or a re-rating catalyst is required.

---

## Step 7: Bull / Base / Bear Scenarios

Probability-weighted SOTP value is the price target.
```
Price Target = (P_bull × SOTP_bull) + (P_base × SOTP_base) + (P_bear × SOTP_bear)
```
Default weights: Bull 25% / Base 55% / Bear 20%. Confirm with MD.

### Scenario Operating Level
Ask routing question: "Should I run scenarios at the segment level, consolidated portfolio level, or model a specific event? [Segment-level / Portfolio-level / Event-driven (spin-off, divestiture, merger)]"

### Scenario Driver Table

| Driver | Bull | Base | Bear |
|--------|------|------|------|
| Segment A revenue CAGR | [above] | [base] | [below] |
| Segment A EBITDA margin | [expansion] | [normalized] | [compression] |
| Segment B [relevant driver] | [above] | [base] | [below] |
| Blended WACC | [base −50bps] | [base] | [base +100bps] |
| Blended g | [base +25bps] | [base] | [base −50bps] |
| Conglomerate discount | [narrows or removed] | [base] | [widens by 3–5pp] |
| Implied SOTP PT | $[X] | $[Y] | $[Z] |
| vs. Current Price | [+X%] | [+Y%] | [−Z%] |

### Downside Stress — Both Levers per Segment

**1. Input stress:**
- WACC up 100–150bps per DCF-valued segment
- Terminal growth down 50–100bps per segment
- Conglomerate discount widened by 3–5pp

**2. FCF stress:**
- EBITDA margin compression per segment (state bps)
- Capex intensity increase per segment
- Revenue miss per segment

State which segment is the binding constraint in the bear case.

### Distress Scenario (per segment, if applicable)
For any segment with meaningful distress probability: apply probability-weighted recovery value.
```
Blended Segment Bear = (1 − p_distress) × Going Concern Bear + p_distress × Recovery Value
```

**Active guardrails:**
- **G-02 [HARD STOP]** Weights must sum to 100%.
- **G-03 [HARD STOP]** Bear SOTP ≥ base SOTP, or bull SOTP ≤ base SOTP: logically inverted. Correct before proceeding.
- **G-29 [FLAG]** All three scenarios imply upside. Bear case does not stress the thesis.
- **G-30 [FLAG]** Bull and bear within 10% of base. Differentiation is insufficient.

---

## Step 8: Consensus Tension Flags

Run all checks after building assumptions. Each flag requires MD confirmation before output is finalized.

| Check | Condition | Action |
|-------|-----------|--------|
| Segment terminal growth | Any segment g > 150bps above that segment's peer median | Flag: "Segment [X] g of [Y]% is [Z]bps above peers. Justify or reduce." |
| Segment WACC | Any segment WACC > 100bps outside sector range | Flag and confirm |
| Near-term growth vs. consensus | Any segment Year 1–3 growth > 2× reported consensus | Flag: "Is this deliberate differentiation or a model error?" |
| EBITDA margin vs. comps | Any segment margin > 300bps above or below sector comps | Flag with benchmark; ask for structural justification |
| SOTP vs. market cap | Total SOTP > 40% above current market cap | Flag: "Is there a catalyst that closes this gap? If not, revisit assumptions." |
| Conglomerate discount | Discount outside 0%–20% | Flag and confirm (S-12) |
| Segment concentration | Single segment > 60% of gross SOTP | Flag concentration risk (S-10, S-11) |
| Market-implied back-solve | At current price, what does the market imply? | Always state per-segment and consolidated implied WACC, g, or multiple |

---

## Step 9: Peer Valuation and SOTP Benchmarking

For each material segment, present implied multiple versus segment pure-play comparable set.

- DCF-implied EV/EBITDA for each segment vs. segment pure-play peers
- DCF-implied EV/EBIT or P/E where appropriate
- Consolidated SOTP-implied EV/EBITDA vs. diversified industrial or sector-relevant peers

**For each comparison, address:**
- Is the segment premium or discount justified? (growth differential, ROIC, competitive moat, management track record)
- Which 2–3 variables drive the gap? Bold those in the output.
- What does the current market price imply per segment?

---

## Step 10: Risk Factor Page

Generate as a separate section. Always include. Quantify where possible.

### Per-Segment Risks (material segments only)

For each material segment:
- **Upside (2–3 bullets):** Quantify magnitude where possible
- **Downside (2–3 bullets):** Quantify magnitude where possible

### Portfolio-Level Risks
- Conglomerate discount widening (capital misallocation, investor fatigue, activist pressure)
- Capital allocation risk (cross-subsidization of weaker segments destroying value in higher-quality segments)
- Separation execution risk (if spin-off or divestiture is a thesis component: timeline, tax structure, management capacity)
- Macro sensitivity of the combined portfolio (weighted average cycle exposure)
- Balance sheet risk if leverage is held at HoldCo and cash flows are distributed unevenly across segments

### Key Model Assumptions — Sensitivity Ranking
State the 5–7 most consequential assumptions across the full SOTP. Rank by impact: which assumption, if wrong by 10%, moves the price target most?

---

## Step 11: Disclosure Language

### Methodology Disclosure (always include)
> "Our SOTP valuation assigns separate methodologies to [N] segments. [Segment A] is valued via a [X]-year DCF at a WACC of [Y]% and terminal growth of [g]%. [Segment B] is valued at [M]x forward EBITDA vs. [comp set]. We apply a [D]% conglomerate discount to gross SOTP value of $[gross]/share, arriving at a [fully diluted] equity value of $[PT]/share. All projections are estimates subject to material uncertainty."

### Forward-Looking Statements (client-facing documents)
> "This analysis contains forward-looking statements based on assumptions and estimates. Actual results may differ materially."

### Research Independence
Routing question: "Is this for external distribution? Should I include your firm's standard research independence disclosure? [Yes / No / Add manually]"

---

## Step 12: Output Format

### One-Page Memo (default)
Rigid structure — no exceptions:

1. **Headline (1 sentence):** [Rating] [Ticker]: Price target $[X], implying [Y]% [upside/downside]
2. **Thesis (3 bullets):** Why buy/sell/hold. Most important bullet first.
3. **SOTP bridge (compact):** Segment values, corporate overhead, conglomerate discount, net debt, equity value per share
4. **Scenario table:** Bull PT / Base PT / Bear PT / Probability weights / Current price / % upside or downside
5. **Key segment assumptions (4–6 lines):** One line per material segment with methodology, key driver, and implied multiple
6. **Conglomerate discount rationale (2 lines):** Basis and whether it is expected to compress or persist
7. **Top 2 upside / top 2 downside risks**
8. **Disclosure (1–2 lines)**

### 2–3 Slide Format
- **Slide 1:** Headline, thesis (3 bullets), SOTP bridge waterfall, scenario PT table
- **Slide 2:** Segment detail table (methodology, WACC, g or multiple, EV, per share), consolidated sensitivity table, TV concentration flags
- **Slide 3:** Risk factors (per-segment + portfolio-level), peer comp table (segment-level), conglomerate discount analysis, disclosure

### Non-Negotiable Output Rules
- First sentence contains price target and thesis.
- SOTP bridge is always shown — never present a PT without the segment build behind it.
- Conglomerate discount is always explained — never just a number.
- Every segment multiple or growth rate has a stated reason.
- Answers "what is priced in at current levels per segment."
- Digestible in under 5 minutes.

---

## Quality Benchmark

A passing SOTP output:
- Shows where value is created and destroyed across the portfolio
- Makes the conglomerate discount legible, quantified, and defensible
- Calculates the separation unlock if a gap exists
- Names which segment is the swing factor in bull vs. bear
- Addresses every bridge line (overhead, minority interests, net debt) explicitly
- Can be presented to a buy-side PM in a 10-minute meeting without leaving any question unanswered
