# Sheet Specs — Steps 3–9

Load this file when building individual sheets.

---

## Step 3: Assumptions Sheet

Build in labeled sections with bold header rows.

### Company Information
Company name, ticker, industry, currency, valuation date, analyst name.

### Market Data
Current share price, 52W high, 52W low, basic shares, options + RSUs outstanding, treasury shares (TSM), diluted share count (formula), market cap (formula).

### Revenue Assumptions
- Base Year Revenue (Yr 0, $mm) — LTM actual
- Phase 1 Growth Rate (Yr 1–3)
- Phase 2 Growth Rate (Yr 4–7)
- Phase 3 Growth Rate (Yr 8–10)
- Terminal Growth Rate (g) — labeled "≤ long-run nominal GDP"
- Revenue mix memos (product/service split if relevant)

**G-16 embed:** If g input > 4.5%, adjacent yellow cell: `"⚠️ G-16: g exceeds long-run nominal GDP ceiling. Verify before proceeding."`

### Margin & Profitability Assumptions
- Gross Margin: Year 1, Year 5, Year 10
- EBITDA Margin: Year 1, Year 5, Year 10
- D&A as % of Revenue
- SBC as % of Revenue (Damodaran: real expense — subtract from FCFF)
- Interest Income Rate (on cash)
- Effective Tax Rate
- NOL Benefit (Yr 1–3 only; set to 0 for Yr 4+)

### Reinvestment & CapEx Assumptions
- CapEx as % of Revenue: Phase 1, Phase 2, Phase 3
- Change in NWC as % of ΔRevenue
- NWC Base (Year 0)
- Acquisition Spend as % of Revenue (0 if none)
- Sales-to-Capital Ratio (Damodaran reinvestment check)

### WACC Assumptions (cross-checked on WACC Builder)
- Risk-Free Rate (10Y UST) — state observation date in adjacent note cell
- Equity Risk Premium (ERP) — state Damodaran source and date
- Beta (levered) — state whether regression or Hamada re-levered; note comp set
- Small Company Premium (Duff & Phelps / Kroll — 0 if large-cap)
- Company-Specific Risk Premium
- Cost of Equity: `=Rf + β×ERP + SCP + CSRP`
- Pre-Tax Cost of Debt (Kd) — blended YTM
- After-Tax Kd: `=Kd×(1−t)`
- Equity Weight (market value)
- Debt Weight: `=1−We`
- WACC: `=Ke×We + Kd_at×Wd`

**Embedded guardrail check cells (yellow background if triggered):**
```
=IF(C_WACC<=C_g,"⛔ G-01: WACC≤g — TV invalid","OK")
=IF(C_WACC<C_Rf,"⛔ G-04: WACC<Rf — invalid","OK")
=IF(C_Ke<C_Kd_at,"⛔ G-09: Ke<Kd — invalid","OK")
=IF(C_g>0.045,"⚠️ G-16: g exceeds GDP ceiling","OK")
```

### Terminal Value Assumptions
- Terminal Growth Rate g (link to Revenue section — single source)
- Terminal EBITDA Margin
- Terminal CapEx as % of Revenue
- Terminal ROIC (Damodaran reinvestment check)
- TV Method toggle: "Gordon Growth" or "Exit Multiple" (text input)
- EV/EBITDA Exit Multiple (for exit multiple TV)

### Equity Bridge — Balance Sheet Adjustments ($mm)

Each item in its own labeled row with sign-convention note:
- Cash & Equivalents (+)
- Short-Term Investments (+)
- Total Debt, Gross (−)
- Pension Underfunding (−)
- Operating Lease Obligations PV (−) [ASC 842 / IFRS 16]
- Finance Lease Obligations (−) [SEPARATE ROW — do not combine with operating leases]
- Minority Interest (market value) (−)
- Equity Stakes / Investments (+)
- Deferred Tax Liability, net (−)
- Options Value BSM (−)

### Scenario Weighting & Conventions
- Scenario Probability: Base, Bear, Bull
- Probability check: `=SUM(p_base, p_bear, p_bull)` — adjacent: `=IF(sum=1,"OK","⛔ G-02: Weights ≠ 100%")`
- Mid-Year Convention toggle: "Y" or "N"

---

## Step 4: Historicals Sheet

5-year history + LTM column.

**Income Statement section:**
Revenue, YoY Growth %, Gross Profit, Gross Margin %, Operating Expenses, EBITDA, EBITDA Margin %, D&A, EBIT, EBIT Margin %, Interest Expense, EBT, Taxes (`=EBT × tax_rate`), Net Income, Net Margin %.

**Cash Flow & FCF section:**
Net Income, +D&A, +SBC, ±ΔWC, Operating Cash Flow, CapEx, Free Cash Flow, FCF Margin %, FCF/Net Income conversion ratio.

All rows are hardcoded historical inputs (blue text) except calculated margin/growth rows (black formula).

---

## Step 5: DCF Engine Sheet

Columns: Year 1–10 (explicit projection) + Terminal Year.

**Scenario toggle:** Single cell `C4` = "Base" / "Bear" / "Bull". Every assumption row:
```
=IF($C$4="Base",Assumptions!C_x,IF($C$4="Bear",Assumptions!D_x,Assumptions!E_x))
```

### Section A — Revenue & Growth
- YoY Growth Rate (reads from Assumptions Phase 1/2/3 by year)
- Revenue: `=prior_year_revenue × (1 + growth_rate)`; Year 1: `=Yr0_revenue × (1 + Yr1_growth)`

### Section B — Margins → EBITDA → EBIT → NOPAT
- Gross Margin % — linear interpolation between Year 1, Year 5, Year 10 anchor points
- Gross Profit: `=Revenue × GrossMargin%`
- EBITDA Margin % — linear interpolation between Year 1, Year 5, Year 10 anchor points
- EBITDA: `=Revenue × EBITDA_Margin%`
- D&A: `=Revenue × DA_pct`
- EBIT: `=EBITDA − D&A`
- Taxes: Years 1–3: `=EBIT × (tax_rate − NOL_benefit)`; Years 4+: `=EBIT × tax_rate`
- NOPAT: `=EBIT − Taxes_on_EBIT`

**Linear interpolation formula for margin fade (e.g., EBITDA Margin Year n):**
- Years 1–5: `=Yr1_margin + (Yr5_margin − Yr1_margin) × (n−1)/4`
- Years 6–10: `=Yr5_margin + (Yr10_margin − Yr5_margin) × (n−5)/5`
- Terminal Year: `=Yr10_margin` (steady state)

### Section C — FCFF Build
- NOPAT (link from Section B)
- + D&A (non-cash add-back)
- − CapEx: `=−Revenue × capex_pct_phase`
- − ΔWC: `=−(ΔRevenue × NWC_pct)`
- − Acquisitions: `=−Revenue × acq_pct`
- **FCFF = NOPAT + D&A − CapEx − ΔWC − Acquisitions**
- FCFF Margin %: `=FCFF/Revenue`
- Reinvestment Rate: `=1 − FCFF/NOPAT` (Damodaran)
- Invested Capital (cumulative): rolling sum of reinvestment
- ROIC: `=NOPAT / prior_year_IC`

**Terminal Year:** Same FCFF components using terminal assumptions. Terminal ΔWC = 0 (no perpetual WC release — **G-27**).

### Section D — Discounting & Present Value
- Discount Period: `=IF(mid_year_toggle="Y", n−0.5, n)`
- Discount Factor: `=1/(1+WACC)^discount_period`
- PV of FCFF: `=FCFF × discount_factor`
- TV discounting: always `=TV / (1+WACC)^10` (end-of-year regardless of mid-year toggle)

### Section E — Terminal Value
- Terminal Year FCFF (link from Section C)
- Terminal Year EBITDA (link from Section B)
- Gordon Growth TV: `=Terminal_FCFF × (1+g) / (WACC−g)`
- Exit Multiple TV: `=Terminal_EBITDA × exit_multiple`
- **TV USED**: `=IF(TV_method="Gordon Growth", GGM_TV, EM_TV)`
- PV of TV: `=TV_used / (1+WACC)^10`
- TV % of EV: `=PV_TV / (PV_TV + sum_PV_FCFFs)`

**Embedded checks:**
```
=IF(TV_pct>0.85,"⛔ G-19: TV>85% of EV — confirm assumptions","OK")
=IF(AND(TV_pct>0.65,TV_pct<=0.85),"⚠️ G-22: TV 65–85% of EV — widen sensitivity","OK")
```

### Section F — Equity Bridge
All values are formulas linking to Assumptions equity bridge section:
- Sum of PV FCFFs (Yr 1–10)
- + PV of Terminal Value
- **= Enterprise Value**
- + Cash & Equivalents
- + Short-Term Investments
- + Equity Stakes / Investments
- − Total Debt (Gross)
- − Pension Underfunding
- − Operating Lease Obligations *(separate row)*
- − Finance Lease Obligations *(separate row — do not combine)*
- − Minority Interest
- − Deferred Tax Liability
- − Options Value (BSM)
- **= Equity Value**
- ÷ Diluted Shares Outstanding
- **= Intrinsic Value / Share**
- Upside / (Downside) %: `=IV/current_price − 1`
- Implied EV/EBITDA (Yr 1): `=EV / EBITDA_Yr1`
- Implied EV/Revenue (Yr 1): `=EV / Revenue_Yr1`

### Section G — Value-Creation & Sanity Checks
- Terminal ROIC − WACC Spread (positive = value creation)
- Implied Terminal Reinvestment: `=g / terminal_ROIC`
- Model Terminal Reinvestment Rate (from Section C terminal year)
- Reinvestment Consistency Gap = model − implied; adjacent: `=IF(ABS(gap)>0.03,"⚠️ Gap >3% — terminal ROIC inconsistent with g","OK")`
- TGR vs Risk-Free Rate Check: `=IF(g<Rf,"OK","⚠️ G-16: g≥Rf — review")`

---

## Step 6: WACC Builder Sheet

Full Damodaran methodology. Cross-check vs Assumptions Base WACC must = 0.

**Sections:**
1. Risk-Free Rate — 10Y UST, inflation expectation (10Y BEI), real Rf, Country Risk Premium
2. Equity Risk Premium — Damodaran implied ERP, historical ERP, ERP used
3. Beta Analysis — raw regression beta, Bloomberg adjusted (0.67×raw + 0.33), Damodaran industry unlevered, Hamada re-levered: `=β_u × (1 + (1−t) × D/E)`, Beta Used
4. Cost of Equity: Rf + β×ERP + CRP + SCP + CSRP = Ke
5. Cost of Debt — pre-tax YTM, effective tax rate, after-tax Kd
6. Capital Structure — We, Wd
7. WACC: Ke×We + Kd_at×Wd
8. Cross-check: Assumptions WACC (Base) vs. built-up WACC — difference must = 0

---

## Step 7: Cap Structure Sheet

**Debt Tranche Table:** Tranche name | Face Value ($mm) | Coupon/Rate | Maturity | Notes. Total Gross Debt = SUM. Weighted-avg pre-tax cost = SUMPRODUCT(face×rate)/SUM(face).

**Diluted Share Count (TSM):**
- Basic Shares Outstanding
- + In-the-money Options + RSUs
- − Treasury Shares from Proceeds
- = Diluted Share Count (cross-check vs Assumptions)

**Market Cap & EV Cross-Check:**
- Market Cap = current price × diluted shares
- + Net Debt (Gross Debt − Cash − ST Investments)
- = Trading EV vs DCF EV (Base) — premium/(discount) to DCF

**Finance Lease note:** Finance leases in total debt tranche table. Operating leases shown separately. Both deducted independently in equity bridge.

---

## Step 8: Sensitivity Sheet

Two 5×5 grids side by side. Odd dimensions so base-case falls in center cell. Center highlighted yellow. No `=TABLE()` — each cell is a direct formula.

**Grid 1 — WACC × Terminal Growth Rate (Intrinsic Value / Share):**
- Rows: TGR at [g−100bps, g−50bps, g_base, g+50bps, g+100bps]
- Cols: WACC at [WACC−100bps, WACC−50bps, WACC_base, WACC+50bps, WACC+100bps]
- Each cell: recalculate GGM TV with that WACC and g, discount back, run equity bridge, divide by shares.

**Grid 2 — Exit Multiple × WACC (Implied EV $mm):**
- Rows: WACC at [WACC−100bps, WACC−50bps, WACC_base, WACC+50bps, WACC+100bps]
- Cols: Exit Multiple at [M−2x, M−1x, M_base, M+1x, M+2x]
- Each cell: recalculate exit multiple TV, discount, add PV FCFFs.

**Below grids:** Note that base-case projected FCFFs are held constant; only discounting assumptions and terminal capitalization vary.

---

## Step 9: Dashboard Sheet

Summary only — all cells are formulas or links (no raw inputs).

### Company Information Panel
Company name, ticker, industry, currency, valuation date, analyst — all from Assumptions.

### Key Multiples & Drivers Panel
Base/Bear/Bull WACC, terminal growth, risk-free rate, diluted shares — all links.

### Valuation Summary
- Active Scenario (toggle — user changes on DCF Engine C4)
- Current Share Price
- Base / Bear / Bull Intrinsic Value / Share
- Probability-Weighted Value / Share: `=p_base×IV_base + p_bear×IV_bear + p_bull×IV_bull`
- Implied Upside / (Downside) % — labeled "vs. Probability-Weighted IV"

### Sanity Checks Panel (yellow background if triggered)
- WACC Cross-check (Build − Input) = 0 check
- TGR vs RFR: `=IF(g<Rf,"OK","⚠️ Review")`
- Probability Sum: `=IF(sum=1,"OK","⛔ G-02")`
- Terminal ROIC − WACC Spread
- Finance Lease in Bridge: `=IF(finance_lease_bridge_cell<>0,"OK","⚠️ Finance lease not bridged")`

### Football Field — Value Per Share

| Methodology | Low | High | Midpoint |
Each row a formula (±10% around base midpoint, or scenario low/high):
- DCF Bear Case
- DCF Base Case
- DCF Bull Case
- 52-Week Trading Range (from Assumptions)
- Probability-Weighted Target
- Current Price reference line (link from Assumptions)

### Hidden Compute Block (grouped/collapsed at bottom)
Pre-compute all-scenario intrinsic values so Dashboard formulas are clean single-cell references.
- Label rows: "Hidden compute — Base/Bear/Bull FCFF Yr1–10"
- Label rows: "Hidden compute — Intrinsic Value / Share per scenario"
- Year columns labeled Yr1–Yr10, TermYr
