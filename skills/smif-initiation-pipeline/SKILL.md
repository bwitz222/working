---
name: smif-initiation-pipeline
description: >
  Superskill: end-to-end initiation-of-coverage pipeline for Purdue SMIF. Given a ticker,
  produces up to five deliverables: Full Foundation Brief (.md), Damodaran DCF Excel model,
  dark-mode HTML risk dashboard, SMIF-branded initiation report (.docx), and a run log.
  Routes on depth (quick take / standard / full), checkpoint style (one-shot / gated), and
  challenge mode (red-team the thesis and the user's prior, or stay neutral). Trigger on:
  "initiate coverage on [TICKER]", "SMIF full run [TICKER]", "run the initiation pipeline",
  "one-shot initiation", "quick initiation take on [TICKER]", or any request for a SMIF
  initiation package on a single public equity. Never run any stage of this workflow
  ad hoc when this skill is installed — route through it.
---

# SMIF Initiation Pipeline v2 (Superskill)

**Read order:** this file → `references/data-sources.md` (before any data pull) →
`references/stages.md` (before each stage) → `references/qa-checklist.md` (before
delivery; the run does not end without passing it). Load references only when needed.

**Skill references:** all skills below are invoked by BARE name, with no plugin or
marketplace prefix. Never invoke a same-named plugin variant (`daloopa:dcf`, `*-dcf-model`,
`financial-analysis:*`) in place of the user's own skill.

---

## Step 0: Fork Resolution (before anything else)

Resolve every fork from the invocation text first. Ask only what remains BOTH unresolved
and material, in ONE batched AskUserQuestion (never more than one round). If the
invocation says "one shot," ask nothing and use defaults.

| Fork | Options | Resolve from | Default |
|---|---|---|---|
| **Depth** | `quick` — brief + Python shadow DCF + 1-page memo (.md), no Excel/HTML/docx. `standard` — brief + Excel DCF + docx (skip HTML dashboard). `full` — all five deliverables. | "quick take" → quick; "full run"/"initiate coverage" → full | `full` |
| **Checkpoints** | `none` (one-shot), `two` (after brief + before delivery), `kill-gate` (pause after brief ONLY if the thesis is dead; otherwise straight through) | "one shot" → none; "checkpoint" → two | `none` |
| **Challenge mode** | `on` — thesis red-team pass after drafting (see stages file); if the user stated a directional prior ("I think it's a buy"), explicitly test it and, if the work disagrees, lead the delivery summary with the disagreement. `off` — present the work; no editorializing beyond the report. | "don't push back"/"just run it" → off | `on` |
| **PT weighting** | DCF prob-weighted IV vs. market anchor blend | "--weights X/Y" or prose | `50/50`, stated in the exhibit source line |
| **Rating stance** | model-driven (let the numbers set Rating/Recommendation) or user-directed | explicit instruction only | model-driven |

**Dead-thesis rule by checkpoint mode:** `none` → never stop for a bad thesis; a
"fairly priced, no edge" verdict becomes the report's rationale. `kill-gate`/`two` →
pause with AskUserQuestion (Proceed / Proceed bear-tilted / Kill). ALL modes hard-stop on
structural failure only: invalid ticker, non-equity asset, or unsourceable financials.

**Execution discipline (all modes):** TaskCreate list matching the chosen depth at start;
run log started at Stage 1 and appended AS FRICTION HAPPENS; every figure dated,
sourced, and attribution-tagged AT CAPTURE per `decision-provenance` (retro-tagging at write-up is
the failure this rule exists to prevent); conclusion-driving figures dual-sourced or labeled single-sourced; all math
verified programmatically. File naming: `YYYY-MM-DD_TICKER_type.ext`.

---

## Pipeline Map

Skills are bare names (see Skill references above). Two editorial passes bracket the
prose: `write` GATE v1 runs DURING drafting (Stages 1, 4) so prose lands clean, and again
as the final mechanical pass in Stage 5; `write` CRITIQUE mode interrogates the written
deliverables ONCE at the end (Stage 5). These are distinct from challenge mode, which
attacks the thesis, not the writing.

| Stage | Skill(s) | Output | Depth |
|---|---|---|---|
| 0. Data acquisition | `decision-provenance` (`references/vendor-map.md`), then `references/data-sources.md` | in-context dataset, every figure tagged at capture | all |
| 1. Foundation brief | `equity-research-foundation` (Path 6), then `write` GATE v1 on the drafted brief | `_foundation-brief.md` + run log | all |
| 2. Valuation | `dcf` (YOUR skill; invoke by the exact name `dcf`, never `daloopa:dcf`) + `xlsx` | `_dcf-model.xlsx` (quick: shadow model only) | all |
| 3. Risk dashboard | `equity-risk-report` | `_risk-report.html` | full only |
| 4. Report | `purdue-smif-brand-guidelines` + `purdue-smif-editorial-style` + `docx`, then `write` GATE v1 on the drafted prose | `_initiation-report.docx` (quick: `_quick-take.md`) | all |
| 4b. Provenance | `decision-provenance` | provenance block appended to every deliverable | all |
| 5. QC + delivery | `write` CRITIQUE (written deliverables) → `write` GATE v1 on the EXTRACTED text of every built file → challenge mode (if on) → `references/qa-checklist.md` | corrected files + finished run log | all |

Stage detail, calibration rules, and known build traps: `references/stages.md`.

**The artifact rule, Stage 5.** Prose gated before the docx build is not a gated document. Table
captions, exhibit titles, chart labels, section headers, footnotes, and the executive-summary box
are written during the build and never see the gate unless someone goes back for them. Extract
the text from the finished `.docx` and `.html` and run GATE v1 on that. If extraction cannot be
run, say so in the run log and list the build-time elements as ungated.

**The gate ledger.** Body prose cleared at deep tier in Stage 1 or 4 and untouched since is NOT
re-gated in Stage 5. Gate what changed and what was written during the build. Three full passes
over the same 5,000 words produce the same text at triple the cost, and the third pass is where
over-editing starts introducing errors.

**Reviewing member work.** When the deliverable under review is an analyst's or member's own
writeup rather than a pipeline output, route to `write` COACH, not CRITIQUE. COACH withholds the
rewrite so the analyst does the revision, which is the point of assigning it.

---

## Compliance (non-negotiable, every mode)

1. No buy/sell/hold or rating language anywhere except the final report's Recommendation
   section. Quick-take memos carry analytical framing plus the educational disclaimer, no
   directive language.
2. Disclaimers verbatim per the SMIF editorial skill: internal-confidential on cover and
   footer; educational disclaimer on the Covering Analysts page; external disclaimer with
   the date filled on the final page. Unresolved `[TBD]` or `[date]` placeholders are
   distribution blockers, listed in the run log.
3. Never fabricate: no invented figures, sources, peer multiples, moving averages, or
   conversion mechanics. Missing = DATA UNAVAILABLE or [TBD] + blocker entry.
4. Rigorous-looking output on unverified numbers is the worst failure mode this pipeline
   can produce. When a check cannot be run, say so in the run log rather than skipping
   silently.
5. Editorial passes (`write` GATE v1 and CRITIQUE) touch prose craft ONLY. They may never
   alter a figure, date, source line, exhibit number, disclaimer (all three verbatim-
   locked), Rating/Recommendation wording, or balanced-risk language, and may not inject
   directive language into the brief/HTML/memo. Any rewrite re-enters the full QA checklist
   before delivery. The CRITIQUE verdict and scorecard are internal working product —
   surface only the material issues it caught in the run log and delivery summary; do not
   dump the full critique unless asked.

6. Every deliverable carries a provenance block per `decision-provenance`. Material `[MODEL]` items
   (any input whose reasonable movement changes the Rating, the PT by more than 5%, or a risk
   classification) require recorded human ratification. Unratified material items are distribution
   blockers, listed by name in the run log, never summarized as "some assumptions pending."
7. Path 6 of `equity-research-foundation` now includes the consensus divergence gate (step 8). Its
   output carries into the brief and the report. "No edge here" is a valid and common finding; a
   pipeline that never produces it is not running the gate.