
# DCF Model Builder — Damodaran Style (Institutional Grade)

**Standard:** Audit-ready Excel model. Every assumption in a labeled cell. Every output a formula. No hardcoded results. Matches a Damodaran-style multi-scenario DCF with WACC builder, 10-year FCFF projection, sensitivity tables, and equity bridge.

---

## Reference Files

Load these as needed — do not load all upfront:

| File | When to load |
|------|-------------|
| `references/standards.md` | **Load first, every session** — token discipline, no AI slop, verification rules |
| `references/guardrails.md` | Before writing any cell; full guardrail registry with all G-codes |
| `references/sheet-specs.md` | When building sheets (Steps 3–9); detailed cell-level specs |
| `references/variants.md` | When Real Estate or SOTP routing confirmed (Steps 10–11) |
| `references/output-quality.md` | When writing scenarios, consensus flags, output memo, or quality gate (Steps 12–15) |

---

## Guardrail Severity System

Tier definitions ([HARD STOP] / [FLAG] / [ALERT]) are in SKILL.md. Full registry: `references/guardrails.md`.

## Step 0: Routing Questions

Ask ALL questions in one compact block. Do not begin any modeling until all are answered.

### Block A — Universal (all verticals)
1. **Company + ticker?**
2. **Vertical?** IB (M&A / LevFin / Coverage) | ER (initiation / PT update / morning note) | Asset Management (long/short, fundamental) | Real Estate (direct, REIT, REPE)
3. **Use case?** Deal / Pitch / Memo / Model build / Sensitivity refresh / Valuation opinion / IC deck
4. **Tone?** Technical (formula-level, WACC derivation shown) | Executive (conclusion-first, driver callouts, no formula detail)
5. **SOTP check:** Does the company have 2+ materially distinct segments with different risk profiles, growth rates, or capital intensities? [Yes → Block C | No → continue]
6. **Scenario weights?** Default: Bull 25% / Base 55% / Bear 20%. Confirm or override.
7. **Currency?** If non-USD or multi-currency: state FX assumption and source. **(G-08)**
8. **Valuation date?** State explicitly. If > 6 months ago, flag **(G-32)** before proceeding.

### Block B — Vertical-Specific Routing

**IB:**
- B1. Transaction context? [Buyside | Sellside | Fairness opinion | LevFin | None]
- B2. Control premium? [Yes — state % | No | Ask me]
- B3. Synergies? [Include | Exclude | Standalone + synergized side by side]
- B4. Leverage? [Levered FCFE | Unlevered FCFF] — default FCFF

**ER:**
- B5. Document type? [Initiation | PT revision | Model update | Morning commentary | Sector note]
- B6. What changed? (If update: earnings, guidance, macro, rate, model refresh)
- B7. Peer comp lenses alongside DCF?
- B8. Research independence disclosure needed?

**Asset Management:**
- B9. Strategy? [Long-only | Long/short | Event-driven | Credit | Quant screen]
- B10. Catalyst? State primary thesis catalyst and expected timeline.
- B11. Position sizing context?
- B12. Hurdle rate / required return?

**Real Estate:**
- B13. Asset type? [Core | Core-plus | Value-add | Opportunistic | Development | REIT | REPE fund]
- B14. Property type? [Office | Retail | Industrial | Multifamily | Hotel | Mixed-use | Other]
- B15. Valuation approach? [NAV/DCF | AFFO (REIT) | Cap rate direct | Levered IRR | All four]
- B16. Hold period? [3Y | 5Y | 7Y | 10Y | Open-ended]
- B17. Financing? [All-equity | Levered — state LTV, rate, amortization | TBD]

### Block C — SOTP Add-on (if Block A Q5 = Yes)
- C1. Segment map? List segments; confirm % revenue and % EBIT per segment. **(S-01)**
- C2. Methodology per segment? [DCF | EV/EBITDA | NAV | P/TBV | PV10 | Other]
- C3. Corporate overhead? State unallocated central costs in $mm. **(S-07)**
- C4. Conglomerate discount? [Yes — estimate | No | Premium | Ask me] **(S-12)**
- C5. Net debt location? [HoldCo | Allocated to segments | Split] **(S-09)**
- C6. Minority interests / JV stakes? State entities and treatment.
- C7. Intercompany items? Identify and confirm elimination method. **(S-03)**

**Routing guardrails before proceeding:**
- **G-02** Weights ≠ 100% → stop and correct
- **G-08** Currency mismatch → stop and resolve
- **S-01** Segment % ≠ ~100% → stop and resolve

---

## Step 1: Methodology Selection

State the FCF convention and defend it. Never leave it implicit.

| Vertical / Sector | FCF Convention | Key Note |
|-------------------|---------------|----------|
| IB — standard | FCFF | Bridge to equity via net debt |
| IB — simple cap structure | FCFE | Discount at Ke; confirm with MD |
| ER — tech / SaaS | Unlevered FCF, SBC-adjusted | SBC is a real expense |
| ER — industrials | FCFF; maint vs. growth capex split | Normalize through cycle |
| ER — healthcare / pharma | FCFF with patent cliff model | Pipeline optionality explicit |
| AM — fundamental | FCFF or FCFE per company stage | State and defend |
| AM — event-driven | FCFF + p(event) scenario | State probability and timeline |
| RE — REIT | AFFO | Depreciation non-economic **(RE-01)** |
| RE — direct asset | NOI DCF + terminal cap rate | Hold period IRR as cross-check |
| RE — development | Residual land value or development DCF | Pre-stabilized period explicit |
| SOTP — each segment | Per segment from Block C | Never single WACC **(S-02)** |

Notify user: *"Using [method] because [reason]. Alternative [method] would imply [difference]. Override if preferred."*

Active guardrails: **G-05, G-06, G-07, G-08** — confirm net debt sign, fully diluted shares, consistent convention, single currency before writing any cell.

---

## Step 2: Sheet Architecture

**Tab order (build in this sequence):**

| # | Tab | Purpose |
|---|-----|---------|
| 1 | `📊 Dashboard` | Summary, football field, scenario table, sanity checks |
| 2 | `⚙️ Assumptions` | Single source of truth — all inputs here |
| 3 | `📈 Historicals` | 5-year IS, CF, FCF with YoY and margin calculations |
| 4 | `🔢 DCF Engine` | 10-year FCFF + terminal value + discounting + equity bridge |
| 5 | `📉 Sensitivity` | WACC × TGR and WACC × Exit Multiple grids (5×5 each) |
| 6 | `📋 WACC Builder` | Full Damodaran CAPM build; cross-checks Assumptions |
| 7 | `🏦 Cap Structure` | Debt tranches, diluted share waterfall, EV cross-check |
| RE | `🏢 Rent Roll` | NOI build, lease expiry, vacancy (Real Estate only) |
| SOTP | `🧩 Segment [Name]` | One tab per material segment DCF (SOTP only) |

**Formatting standards (apply identically to all sheets):**
- Blue text `#0000FF` — hardcoded inputs
- Black text `#000000` — formulas and calculations
- Green text `#008000` — cross-sheet links
- Yellow background `#FFFF00` — key assumptions requiring attention
- Header row: bold, `#1F3864` background, white text, 12pt
- Currency: `$#,##0;($#,##0);-` | Percentages: `0.0%` | Multiples: `0.0x`
- Years as text strings ("2024"), not numbers

**Non-negotiable formula rules:**
- Every business assumption lives in a labeled Assumptions cell — no magic numbers in formulas
- Every derived value is a formula referencing source cells — no hardcoded computed results
- Cross-sheet references use `='SheetName'!CellRef` syntax (never `.` separator)
- Sensitivity cells use direct formulas — not `=TABLE()` (Office.js cannot set TABLE arrays)

> Detailed cell-level specs for all sheets (Steps 3–9): **→ load `references/sheet-specs.md`**

---

## Vertical Quick-Reference

| Vertical | Primary FCF | TV Anchor | Key Output |
|----------|------------|-----------|------------|
| IB — M&A | FCFF | GGM + exit multiple | EV range, equity bridge, synergy overlay |
| IB — LevFin | Levered FCF | Exit multiple | Leverage, coverage, returns |
| ER — initiation | FCFF or FCFE | GGM (anchor) + exit multiple (check) | Price target + 3-scenario |
| ER — update | Same; show delta vs prior | Same | What changed and why |
| AM — long-only | FCFF or FCFE | GGM + back-solve | Conviction tier + catalyst |
| AM — event | FCFF + p(event) | GGM + event case | Probability-weighted IV |
| RE — direct | NOI DCF | Terminal cap rate + GGM | Levered IRR + NAV |
| RE — REIT | AFFO DCF | GGM (g tied to NOI growth) | NAV + AFFO yield |
| SOTP | Per-segment | Per-segment | Bridge waterfall + conglomerate discount |
