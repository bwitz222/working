# Variants — Real Estate & SOTP (Steps 10–11)

Load this file when Real Estate (Block B Q13–17) or SOTP (Block C) routing is confirmed.

---

## Step 10: Real Estate Variant

### Rent Roll Sheet (`🏢 Rent Roll`)

Columns: Tenant | Suite/Unit | SF | Lease Expiry | Contracted Rent ($/SF) | Market Rent ($/SF) | Vacancy Flag | NOI Contribution

- In-place NOI = SUM of occupied contracted rents
- Vacancy rate = vacant SF / total SF
- Mark-to-market gap = (market rent − contracted rent) × occupied SF
- **RE-04** check: `=IF(vacancy<0.03,"⚠️ RE-04: Vacancy <3% — confirm contract backing","OK")`

### DCF Engine Modifications for Real Estate

**Replace FCFF with NOI DCF:**
- Revenue line becomes Gross Rental Income
- Subtract vacancy, OpEx, management fees, CapEx reserves → Net Operating Income

**If REIT:** Use AFFO (NOI − normalized capex − straight-line rent adjustment + real cash items) per **RE-01**. Never use standard FCFF.

**Terminal Value — compute BOTH methods:**
- Cap Rate TV: `=Terminal_NOI / exit_cap_rate`
- GGM TV: `=Terminal_NOI × (1+g) / (discount_rate − g)`
- **RE-03** check: `=IF(exit_cap_rate < entry_cap_rate,"⚠️ RE-03: Exit cap < entry cap — confirm compression rationale","OK")`

**Levered IRR:** Add debt service rows. Compute unlevered and levered IRR side-by-side.

**RE-06:** Cap rate sensitivity grid must use minimum ±75bps range (not the standard ±50bps).

### WACC / Discount Rate for Real Estate

| Asset type | Discount rate | Rationale |
|------------|--------------|-----------|
| Direct assets | Unlevered property discount rate | Property risk, not corporate |
| REITs | Corporate WACC (equity + debt) | Corporate structure applies |
| REPE / development | Hurdle rate from Block B (B12) | Fund-level return requirement |

State which rate is used and why in the Assumptions sheet.

---

## Step 11: SOTP Variant

### Segment Tabs

- Add one `🧩 Segment [Name]` tab per material segment
- Each segment tab is a mini-DCF Engine with its own WACC input cell **(S-02)**
- If > 3 segments: build segment WACCs on a dedicated WACC Builder sub-tab

### Dashboard SOTP Bridge Table (waterfall)

```
Segment A EV
+ Segment B EV
+ Segment C EV
− Corporate Overhead (PV of capitalized overhead at blended WACC)
− Conglomerate Discount
± Minority Interests / JV Stakes
± Net Debt
= Equity Value
÷ Diluted Shares
= Equity Value / Share
```

### Intercompany Eliminations (S-03)

- Dedicated row in each segment FCF labeled "Intercompany Elimination"
- Adjacent note cell: explain basis (transfer pricing, shared services, revenue netting)
- Confirm eliminations net to zero across all segments

### Corporate Overhead (S-07)

- Separate row in bridge
- PV = capitalized at blended WACC (perpetuity if ongoing: `=annual_overhead / WACC`)
- Label clearly in bridge waterfall

### Conglomerate Discount (S-12)

- Labeled row in bridge
- Adjacent note cell must state:
  - Structural basis: Structural / Cyclical / Execution
  - Expected duration
  - Reference precedent if applying > 10%
- Range 0%–20% without named justification triggers **S-12 [FLAG]**

### Net Debt (S-05)

- State location clearly: HoldCo level, allocated to segments, or split (state basis)
- If allocated: show allocation key in each segment tab
- If HoldCo: deduct in bridge as single line after segment sum

### Minority Interests / JV Stakes

- Each entity named individually in bridge
- Treatment: full consolidation with minority deduction, equity method, or partial inclusion
- State basis for each
