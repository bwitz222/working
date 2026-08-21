# Output & Quality — Steps 12–15

Load this file when building scenarios, writing consensus tension checks, finalizing output, or running the pre-output quality gate.

---

## Step 12: Scenarios — Bull / Base / Bear

Probability-weighted IV is the price target: `=p_base×IV_base + p_bear×IV_bear + p_bull×IV_bull`

### Scenario Driver Table (required output)

| Driver | Bull | Base | Bear |
|--------|------|------|------|
| Revenue CAGR Yr 1–5 | | | |
| EBITDA Margin (entry → exit) | | | |
| WACC | base −50bps | base | base +100bps |
| Terminal Growth (g) | base +25bps | base | base −50bps |
| TV Method | | | |
| Implied IV/sh | | | |
| vs. Current Price | | | |

### Downside Stress (both required)
1. **Input stress:** WACC +100–150bps, g −50–100bps → state implied IV and % downside.
2. **FCF stress:** EBITDA margin compression (bps), capex step-up (% rev), revenue miss (%) → state binding constraint.

### Active Guardrails
- **G-02** Weights ≠ 100% → stop.
- **G-03** Bear IV ≥ Base IV or Bull IV ≤ Base IV → stop. Identify and correct the input error.
- **G-29** All three scenarios imply upside → rebuild bear case with genuine downside assumptions.
- **G-30** Bull and bear within 10% of base → widen scenario assumptions.

---

## Step 13: Consensus Tension Flags

Run after all assumptions are set. Each flag requires confirmation before output is finalized.

| Check | Trigger | Required Action |
|-------|---------|-----------------|
| g vs sector | g > 150bps above sector median | State gap; ask to justify or reduce |
| WACC vs sector | > 100bps outside sector floor | Flag G-12; confirm inputs |
| Revenue vs consensus | Yr 1–3 growth > 2× consensus | Ask: deliberate or error? |
| Margin vs comps | > 300bps above/below sector median | Require structural justification |
| TV concentration | TV > 75% EV | G-19 flag + widen sensitivity |
| Market-implied back-solve | Always | State: "At $[price], market implies WACC [x]%, g [y]%, exit [z]x" |
| Reinvestment consistency | Gap > 3% | Note terminal ROIC misalignment |

---

## Step 14: Output Format

### Spreadsheet (primary deliverable — always)
The model is the deliverable. Refer user to the sheet and range for every claim. Never paste wall-of-numbers in chat — narrate where to look.

### Memo / Summary (on request)

Rigid structure:
1. **Headline (1 sentence):** [Ticker]: IV $[X]/sh, implying [Y]% [upside/downside] on probability-weighted basis.
2. **Thesis (3 bullets):** Why buy/hold/sell. Most important first.
3. **Valuation summary table:** Base / Bear / Bull / Prob-weighted / Current price / % up-down
4. **Key assumptions (4–6 lines):** WACC, g, revenue CAGR, EBITDA margin trajectory, FCF convention, TV method
5. **Sensitivity (1 line):** "$[low]–$[high]/sh across WACC/g sensitivity"
6. **Implied multiples vs peers (2 lines):** EV/EBITDA implied vs comps median; premium or discount and why
7. **Top 2 upside / top 2 downside risks (quantified)**
8. **Disclosure:** Methodology statement + forward-looking language

### Non-Negotiable Output Rules
- First sentence: price target and thesis. No exceptions.
- Every number has a stated reason.
- Always answers: "What does the market need to believe for the current price to be fair?"
- No filler, no preamble, no restating the request.
- If an assumption is ±10% the biggest value driver, name it explicitly.

---

## Step 15: Pre-Output Quality Gate

Fail any check → fix before reporting done.

### Formula Integrity
- [ ] Zero `#REF!`, `#VALUE!`, `#NAME?`, `#DIV/0!` errors anywhere in the model
- [ ] All scenario switches work (change DCF Engine C4 to Bear/Bull/Base; outputs update)
- [ ] WACC Builder cross-check = 0.000
- [ ] TV % of EV shown; G-19/G-22 cells evaluated
- [ ] Probability sum = 100%; G-02 cell = "OK"
- [ ] G-01, G-03, G-04, G-09 check cells = "OK"
- [ ] Finance Lease and Operating Lease deducted as SEPARATE bridge rows

### Structural Integrity
- [ ] Every assumption in a labeled Assumptions cell — no magic numbers in formulas
- [ ] Every derived value is a formula — no hardcoded computed results
- [ ] Cross-sheet links use `='SheetName'!CellRef` (no `.` separator)
- [ ] Sensitivity grids use direct formulas (no `=TABLE()`)
- [ ] Margin interpolation consistent (linear fade, same anchor points)
- [ ] Mid-year convention applied to Years 1–10 only; TV always discounted at Year 10 end

### Scenario Integrity
- [ ] Bull IV > Base IV > Bear IV (G-03)
- [ ] Prob-weighted IV is formula, not hardcoded
- [ ] Football field ranges are ±10% of scenario midpoints (or stated differently if intentional)

### Real Estate (if applicable)
- [ ] RE-01, RE-02, RE-03, RE-04 checks embedded and evaluated
- [ ] Exit cap rate sensitivity range ≥ ±75bps (RE-06)
- [ ] Levered and unlevered IRR shown side-by-side

### SOTP (if applicable)
- [ ] Each segment has its own WACC (S-02)
- [ ] Corporate overhead deducted (S-07)
- [ ] Intercompany items eliminated (S-03)
- [ ] Conglomerate discount explained with structural basis (S-12)
- [ ] Bridge lines include minority interests and JV stakes (S-08)
- [ ] Net debt sign correct in bridge (S-05)
