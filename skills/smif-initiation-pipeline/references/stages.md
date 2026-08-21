# Stage Playbook

Load before executing each stage. Depth variants noted inline.

## Stage 1: Foundation Brief (all depths)

Invoke `equity-research-foundation`, Path 6. Run Phase 0 gates (asset
class, sector special cases, live-data mandate, edge-case math), all six lenses, and the
mandatory falsification block: specific bear thesis argued through the same lenses, 2–3
dated observable kill criteria, and a pre-mortem. Verify every computed ratio (Sloan
accrual, CFO/NI, EV/EBITDA, B/M, SBC/FCF, off-high/off-low) in bash. Write the brief and
open the run log in the same step. No directive language — the recommendation exists only
in Stage 4. Report lens conflicts as conflicts (e.g., "4-vs-2"); never force alignment.

## Stage 2: Valuation

**Quick depth:** Python shadow model only — three scenarios, prob-weighted IV, TV%,
market-implied back-solves (implied g at base WACC; implied WACC at base g). Results go
into the quick-take memo with an "estimates, no audit-grade model built" label. Skip the
rest of this stage.

**Standard/full depth:**
1. Invoke the personal `dcf` skill, NOT `daloopa:dcf` (a bare `dcf` may resolve to `daloopa:dcf`,
   which outputs HTML and requires an unauthenticated MCP). Route: Excel, single entity
   (SOTP only if segments report divergent economics), ER-initiation, FCFF, weights
   Bull 25 / Base 55 / Bear 20 unless overridden.
2. SBC: if EBITDA is GAAP (SBC already expensed within), set the FCFF SBC line to zero
   with a written note. Never subtract SBC twice.
3. **Shadow model BEFORE Excel.** Calibrate against reality: Year-1 assumptions must
   respect already-reported quarters and standing guidance (a bear case cannot assume a
   Year-1 miss of revenue that is substantially locked). Entry margins must reconcile to
   what consensus implies (back the EBITDA margin out of consensus NI + taxes + interest
   + D&A). If the shadow IV lands >2× or <0.5× the market price, re-examine assumptions
   once, honestly; if it persists, the verdict is the verdict — state the market-implied
   back-solve rather than bending inputs toward the price.
4. Excel build (openpyxl per the dcf skill's sheet specs): all seven tabs, scenario
   toggle via IF chains to helper param cells, hidden per-scenario compute block feeding
   Dashboard, sensitivity grids as direct SUMPRODUCT formulas. Known build traps:
   - Label cells must NEVER begin with "=" ("= Enterprise Value" → #VALUE!).
   - No hardcoded values in formula cells; blue inputs only in Assumptions/Historicals.
   - Grid cells cannot use =TABLE().
   - Source comments on every hardcoded input (provider + date).
5. **Verification loop, all mandatory, in order:** recalc via the xlsx skill's
   `scripts/recalc.py` to zero errors → key cells vs shadow model → live toggle test
   (Bear → recalc → IV matches hidden compute → restore Base → recalc) → WACC-builder
   cross-check = 0 → READ the full sensitivity grids and record actual min/max. Grid
   numbers quoted anywhere downstream come from this read, never from memory (a live run
   caught a misquoted range exactly here).
6. Surface every guardrail hit (G-13/15/19/20/22/29/30/31/33...) in-model with yellow
   note cells and in the run log. G-20 divergence between GGM-implied and comp exit
   multiples is usually the thesis tension — feature it, don't fix it.

## Stage 3: Risk Dashboard (full depth only)

Invoke `equity-risk-report`. Reuse Stage 0 data; add the quarterly
financials page if not yet pulled. Score strictly per rubric with arithmetic shown.
Label fallback sector medians as defaults. Risks/catalysts must each be specific and
dated — no generic entries. Keep implied-growth/WACC statements consistent with Stage 2
back-solves to the same decimal.

## Stage 4: Report

**Quick depth:** 1-page memo (.md): headline verdict framing (no directive language),
scenario IV table from the shadow model, market-implied back-solve, top 2 risks / top 2
catalysts, kill criteria, educational disclaimer. Done.

**Standard/full depth:**
1. Load `purdue-smif-brand-guidelines`,
   `purdue-smif-editorial-style`, and `docx` first.
2. Structure (SMIF_B_1 initiation): Cover → Investment Thesis → Recommendation
   (Exhibit 1 box + Exhibit 2 Key Statistics) → Business Overview → Industry Overview →
   Financial Breakdown → Discounted Cash Flow Analysis (DCF) → Comparable Company
   Analysis → Management & Governance → Portfolio Strategy → Risks & Mitigation →
   Sources → Covering Analysts (+ verbatim educational disclaimer) → Appendix (DCF
   assumptions exhibit, sensitivity summary, external disclaimer with date filled).
3. Price target = stated blend of DCF prob-weighted IV and market anchor (comp-justified
   forward multiple × consensus EPS), weighting printed in the exhibit source line.
   Rating (Overweight/Neutral/Underweight) AND Recommendation (BUY/HOLD/SELL) both
   required, with balanced risk language. If no live peer multiple set was pulled, say so
   and anchor to the name's own forward curve + PT dispersion — never fabricate a comp
   table.
4. Editorial hard rules: CY never FY · "Q1 2026" body / "Q126" tables · $X Million /
   $X Billion spelled out · multiples as 18.2× · zero-before-decimal · em dashes ≤1 per
   paragraph (prefer zero) · no banned finance phrases · numbered Exhibits with source
   lines · active voice · hedged forward-looking statements.
5. Build mechanics: docx-js via LOCAL npm install (`npm install -g` fails on sandbox
   permissions; `cd /tmp/x && npm init -y && npm install docx` works). US Letter,
   1.0in/1.25in margins, Calibri, gold CEB888 H2s, gray 6F727B body. Validate with the
   docx skill's `validate.py`. Missing logo asset → literal `[SMIF LOGO]` placeholder +
   blocker entry.
6. Anti-hallucination: every prose sentence quoting model output traces to a recalced
   cell read in Stage 2 step 5. Unsourceable required fields (e.g., 50-week MA with no
   price series) → [TBD] + blocker entry.

## Stage 5: QC, Challenge, Delivery

1. `write` GATE v1 deep tier on all prose deliverables. Recurring catches:
   binary contrasts, paired em dashes, meta-commentary openers, inanimate actors, FY
   notation. Patch the build script and rebuild; re-validate after every rebuild.
2. Consistency sweep: identical price, as-of dates, IVs, and implied-growth figures (to
   the decimal) across every deliverable.
3. **Challenge mode ON:** run a red-team pass before delivery — attack the recommendation
   with the three strongest counterarguments from the work itself (usually: the other
   valuation regime, the strongest kill criterion, the weighting sensitivity of the PT).
   If any counterargument survives contact, adjust the report or disclose the tension
   explicitly. If the user stated a directional prior and the work disagrees, the
   delivery summary LEADS with the disagreement and the evidence — do not bury it.
4. Finish the run log: discrepancies, frictions, spec deviations, and a Distribution
   blockers section. Run `references/qa-checklist.md` — every unchecked box is either
   fixed or listed as a blocker with a reason. Present files; close with the call in one
   line, the central tension, blockers, and the overridable judgment calls.
