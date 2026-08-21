---
name: dcf
description: "Institutional-grade DCF valuation, all formats. THE single entry point for any discounted cash flow work: Excel model builds (Damodaran-style, audit-ready), 1-page valuation memos, and slide-ready analyses, for both single-entity and Sum-of-the-Parts (SOTP) structures across IB, Equity Research, Asset Management, and Real Estate. Always use this skill whenever the user asks to: build/run/update a DCF, derive a price target, compute intrinsic value, build a WACC, model terminal value, create sensitivity tables, run bull/base/bear scenarios, produce an equity bridge, value a company via discounted cash flows, or do an initiation/PT revision valuation section. Also triggers on: FCFF model, SOTP, sum of the parts, segment valuation, conglomerate discount, stub value, break-up analysis, spin-off valuation, NAV model, AFFO, cap rate DCF, levered IRR, distress scenario, consensus tension, or any financial valuation deliverable in Excel or memo form. Never build a DCF from scratch without this skill."
---

# DCF — Unified Valuation Skill

One skill, two deliverable formats, two structures. **Route first, then load only the reference file(s) for the chosen path.** Do not load all references upfront.

---

## Step 0: Route (mandatory, before anything else)

Answer both questions. If the user's request doesn't answer them, ask.

**Q1 — Deliverable format?**
- **Excel model** (workbook, audit-ready, every assumption in a cell) → Excel path
- **Memo / slides** (1-page valuation defense, PT derivation, initiation valuation section, digestible in 5 minutes) → Memo path
- Both requested → build Excel first, then write the memo from the model's outputs.

**Q2 — Entity structure?**
- **Single entity**: one dominant business, shared economics → single-entity path
- **SOTP**: 2+ materially distinct segments warranting separate methodologies, discount rates, or growth profiles → SOTP path
- Unclear whether segments are materially distinct → ask the routing question before proceeding. Signals for SOTP: segment-level reporting with divergent margins/growth, different capital intensity, conglomerate discount discussion, spin-off/break-up context.

## Routing Table

| Route | Load |
|---|---|
| Excel, single entity | `references/excel-build.md` |
| Excel, SOTP | `references/excel-build.md` (SOTP add-on in Block C) + `references/variants.md` |
| Excel, Real Estate (direct asset, REIT, REPE) | `references/excel-build.md` + `references/variants.md` |
| Memo/slides, single entity | `references/memo-single-entity.md` |
| Memo/slides, SOTP | `references/memo-sotp.md` |

**Always load with any Excel route:** `references/standards.md` (token discipline, verification rules) first, then `references/guardrails.md` before writing any cell. `references/sheet-specs.md` when building sheets. `references/output-quality.md` for scenarios, consensus flags, output memo, and the quality gate.

---

## Guardrail Severity System (applies to every route)

| Tier | Label | Meaning | Required Action |
|------|-------|---------|-----------------|
| 1 | **[HARD STOP]** | Mathematical impossibility, logical inversion, or data integrity failure | Halt. State the error precisely. Do not proceed until resolved. |
| 2 | **[FLAG]** | Assumption significantly outside institutional norms or consensus | Surface the tension with benchmark data. Ask routing question. Do not proceed until confirmed. |
| 3 | **[ALERT]** | Noteworthy deviation worth disclosing but not blocking | Note in output. Continue unless escalated. |

**Rule:** Any unresolved Tier 1 or Tier 2 issue blocks ALL output. Never bury a guardrail finding inside prose. Surface it as a standalone labeled line before any numbers.

Universal hard stops (all routes): WACC ≤ g (TV denominator ≤ 0), scenario weights ≠ 100%, Bear IV ≥ Base IV or Bull IV ≤ Base IV, WACC < risk-free rate. Route-specific registries live in each reference file.

---

## Pipeline Pointers

- **Upstream:** if building an investment thesis or auditing earnings quality first, run `equity-research-foundation` before valuing.
- **Downstream:** feed outputs into `equity-risk-report` (HTML dashboard) or `write` in DRAFT mode (IC memo). Every
  delivered model carries a `Provenance` tab per `decision-provenance`. SMIF deliverables must apply `purdue-smif-brand-guidelines` + `purdue-smif-editorial-style`.
- **Real estate deals:** underwrite the property-level cash flows first; this skill handles the DCF/NAV mechanics.
