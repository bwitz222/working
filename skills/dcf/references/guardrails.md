# Guardrail Registry — Full Reference

Load this file at Step 0 and before writing any model cell.

---

## Mathematical / Structural Integrity

- **G-01 [HARD STOP]** WACC ≤ g → TV denominator ≤ 0. Model is broken.
- **G-02 [HARD STOP]** Scenario weights ≠ 100%.
- **G-03 [HARD STOP]** Bear IV ≥ Base IV, or Bull IV ≤ Base IV. Scenarios logically inverted.
- **G-04 [HARD STOP]** WACC < Rf. Cost of capital below risk-free rate.
- **G-05 [HARD STOP]** Net debt sign error: net cash being subtracted rather than added.
- **G-06 [HARD STOP]** Share count not fully diluted (options, RSUs, converts, warrants missing).
- **G-07 [HARD STOP]** Mixed discounting convention in same model (mid-year and year-end simultaneously).
- **G-08 [HARD STOP]** Currency mismatch across inputs without explicit FX conversion and stated rate.
- **G-09 [HARD STOP]** Ke < Kd (after-tax). Equity must carry more risk than debt.
- **G-16 [HARD STOP]** g > long-run nominal GDP growth of primary market. Absolute ceiling.
- **G-17 [HARD STOP]** Terminal year FCF ≤ 0. Negative/zero perpetuity destroys model validity.

## WACC Component Guardrails

- **G-10 [FLAG]** β < 0.5 or > 2.0 for industrials/standard companies. Confirm comp set.
- **G-11 [FLAG]** ERP outside 3.0%–8.0%. State source and date.
- **G-12 [FLAG]** WACC > 100bps outside sector reference range.
- **G-13 [FLAG]** Effective tax rate < 15% or > 38% without stated justification.
- **G-14 [FLAG]** D/(D+E) > 65% for non-financial industrial. Covenant/refinancing risk.
- **G-15 [ALERT]** Spot capital structure distorted by recent recapitalization.

## Terminal Value Guardrails

- **G-18 [FLAG]** WACC − g < 1.0%. TV hyper-sensitive; widen sensitivity range.
- **G-19 [FLAG]** TV > 85% of total EV. Near-term FCFs not supporting valuation.
- **G-20 [FLAG]** GGM-implied exit multiple and stated exit multiple diverge > 2.0x EBITDA.
- **G-21 [FLAG]** Exit multiple > 20x EBITDA without a named current comparable at that level.
- **G-22 [ALERT]** TV between 65%–85% of EV. Note sensitivity dependence.

## FCF Projection Guardrails

- **G-23 [FLAG]** Base FCF negative 3+ consecutive years without stated inflection catalyst.
- **G-24 [FLAG]** Terminal D&A > terminal capex for capital-intensive business.
- **G-25 [FLAG]** Terminal year revenue growth ≠ g used in GGM.
- **G-26 [FLAG]** Terminal EBITDA margin has no sector precedent.
- **G-27 [FLAG]** Perpetual WC release assumed in terminal year.
- **G-28 [ALERT]** FCF conversion (FCF/EBITDA) < 30% in terminal year without stated reason.

## Scenario and Stress Guardrails

- **G-29 [FLAG]** All three scenarios imply upside. Bear case is not stressing the thesis.
- **G-30 [FLAG]** Bull and bear within 10% of base. Scenarios lack differentiation.
- **G-31 [ALERT]** Bear case implies > 40% downside. Confirm stress level is intentional.

## Data and Input Guardrails

- **G-32 [FLAG]** Valuation date > 6 months stale.
- **G-33 [FLAG]** Shares changed > 10% YoY without explanation.
- **G-34 [FLAG]** Net debt > 3.0x EBITDA for investment-grade company.
- **G-35 [ALERT]** Macro data source older than 90 days.

## Real Estate–Specific Guardrails

- **RE-01 [HARD STOP]** Using standard FCFF DCF for REIT without AFFO adjustment. Depreciation is non-economic.
- **RE-02 [HARD STOP]** Cap rate ≤ 0 or cap rate > discount rate (implies permanent NOI decline).
- **RE-03 [FLAG]** Terminal cap rate < entry cap rate without stated rent growth or compression rationale.
- **RE-04 [FLAG]** Vacancy assumption < 3% for any property type without named contractual backing.
- **RE-05 [FLAG]** Debt yield (NOI/Loan) < 6% on stabilized asset without stated lender concession.
- **RE-06 [ALERT]** Exit cap rate sensitivity range < ±50bps. Minimum ±75bps required.

## SOTP–Specific Guardrails

- **S-01 [HARD STOP]** Segment revenues/EBIT don't sum to ~100% of consolidated.
- **S-02 [HARD STOP]** Single WACC applied across all segments. Each DCF segment requires segment-appropriate WACC.
- **S-03 [HARD STOP]** Intercompany revenues, cost allocations, or transfer pricing not identified and eliminated.
- **S-07 [FLAG]** Corporate overhead not deducted from gross SOTP value.
- **S-12 [FLAG]** Conglomerate discount outside 0%–20% without named structural justification.
