# Pre-Delivery QA Gate

The run does not end until every box is checked, or unchecked boxes appear in the run
log's Distribution blockers section with a reason. No silent skips.

## Data integrity
- [ ] Every figure in every deliverable carries a source and as-of date (in-text, source
      line, or cell comment).
- [ ] Conclusion-driving figures dual-sourced, or labeled single-sourced in the
      deliverable itself (not just the log).
- [ ] No fabricated data: peer multiples, moving averages, conversion mechanics, sector
      medians all either sourced or labeled default/[TBD]/DATA UNAVAILABLE.
- [ ] GAAP vs non-GAAP basis stated wherever EPS or margins appear.
- [ ] Source-vintage skew (cached pages, PT disagreements) logged.

## Model integrity (standard/full)
- [ ] recalc.py returns zero errors on the final saved workbook.
- [ ] Scenario toggle live-tested after final save; Engine IV matches hidden compute for
      Bear and Base; toggle restored to Base.
- [ ] WACC-builder cross-check = 0; probability sum = 100%; Bull IV > Base IV > Bear IV.
- [ ] G-01/03/04/09/16 check cells all read OK; every FLAG/ALERT hit is visible in-model
      and in the run log.
- [ ] No label cell begins with "="; no hardcoded value in any formula cell outside blue
      input sections.
- [ ] Full sensitivity grids read from the recalced file; min/max recorded in-session.

## Cross-deliverable consistency
- [ ] Same price and as-of date everywhere.
- [ ] Scenario IVs, prob-weighted IV, PT, and implied back-solves identical (to the
      stated decimal) across brief, HTML, docx, and delivery summary.
- [ ] Every model number quoted in prose traces to a cell read this session.

## Editorial & compliance (SMIF)
- [ ] CY notation only; no FY anywhere. Quarters: "Q1 2026" body, "Q126" tables.
- [ ] $X Million / $X Billion spelled out; multiples 18.2×; zero before decimals;
      tickers ALL CAPS.
- [ ] Em dashes ≤1 per paragraph across all prose; no banned phrases (robust portfolio,
      headwinds/tailwinds, navigate, unlock value, positioned for growth, testament,
      underscore, delve...); no exclamation marks.
- [ ] Exhibits numbered sequentially with source lines; model exhibits carry the
      "Estimates based on SMIF internal analysis" line.
- [ ] Rating AND Recommendation both present, only in the final report; balanced risk
      language; no directive language in brief/HTML/memo.
- [ ] All three disclaimers present verbatim, dates filled: internal-confidential
      (cover + footer), educational (Covering Analysts page), external (final page).
- [ ] docx passes validate.py after the LAST rebuild (de-slop patches included).

## Provenance and attribution
- [ ] Provenance block present in every deliverable (docx appendix, xlsx `Provenance` tab, HTML
      end-of-page section, memo footer). Absence is never an acceptable state.
- [ ] Every conclusion-driving figure carries `[SRC]`, `[CALC]`, `[MODEL]`, or `[HUMAN]`, assigned at
      capture rather than reconstructed at write-up.
- [ ] Every material `[MODEL]` item has a recorded `[HUMAN]` ratification with a rationale line.
      Materiality tested by perturbation, not by intuition.
- [ ] Unratified material items listed BY NAME as distribution blockers.
- [ ] Vendor route recorded: which source supplied which figure class, and any mid-run switch.
- [ ] One vendor per figure class across the run, or the exception documented.
- [ ] Consensus divergence gate output present: consensus as a number, variant view with magnitude or
      an explicit "no edge," persistence mechanism, derivative-view check.

## Process
- [ ] Run log complete: discrepancies, frictions, spec deviations, Distribution blockers.
- [ ] Challenge-mode red-team pass done (if on); user-prior disagreement led in summary
      (if applicable).
- [ ] Files named `YYYY-MM-DD_TICKER_type.ext`; all presented via file cards.
- [ ] Delivery summary ends with the overridable judgment calls (PT weighting, rating).
