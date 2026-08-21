---
name: decision-provenance
description: >
  Attribution, data-sourcing, and call-tracking layer for every analytical deliverable. Answers three
  questions no other skill owns: where did this number come from, who decided it (model vs. human),
  and was the call right. Use whenever a deliverable contains figures a client, IC, committee, auditor,
  or compliance reviewer could question; whenever routing a data pull across vendors; and whenever
  logging or grading an investment call. Triggers on: "provenance", "where did this number come from",
  "audit trail", "who decided this", "attribution block", "which data source", "vendor fallback",
  "reconcile sources", "log this call", "grade my calls", "was my thesis right", "track record",
  "hit rate", "compliance review this". Mandatory appendix layer for smif-initiation-pipeline, dcf,
  equity-risk-report, and any client-facing wealth-management deliverable.
---

# Decision Provenance

Three modules, loaded independently. Never load all three at once.

| Need | Module | Load |
|---|---|---|
| Tag and attribute figures in a deliverable | Attribution ledger | `references/ledger.md` |
| Choose a data vendor, set a fallback, reconcile a disagreement | Vendor routing | `references/vendor-map.md` |
| Log an investment call, grade past calls | Call ledger | `references/call-ledger.md` + `scripts/grade_calls.py` |

---

## Why this exists

As analytical production gets cheaper, the scarce good is not the analysis. It is the ability to say,
under challenge, which parts of a conclusion came from filed data, which from a formula, which from a
model's judgment, and which a human ratified. A deliverable that cannot answer that is not defensible
regardless of how good the numbers are. Fiduciary duty presumes responsibility can be traced.

Two failure modes this layer exists to prevent:

1. **Laundering.** A model-generated assumption gets restated in prose, then quoted in a summary, and
   by the third restatement reads like sourced fact. Attribution tags survive restatement; adjectives
   do not.
2. **Silent vendor drift.** Two vendors disagree, one gets picked without a record, and the deliverable
   inherits an unlabeled choice. The reconciliation rule below forces the choice into the open.

---

## The four attribution classes

Every figure, assumption, and judgment in a deliverable belongs to exactly one class.

| Tag | Means | Must carry |
|---|---|---|
| `[SRC]` | External data pulled from a third party or filing | Vendor/document, endpoint or page, period tag, as-of date, retrieval date |
| `[CALC]` | Derived arithmetically from `[SRC]` inputs | The formula and where it runs (cell reference, script name) |
| `[MODEL]` | Produced by an AI system: a forecast, an assumption, a synthesis, a narrative judgment | The basis it was reasoned from, and its sensitivity if it moves the answer |
| `[HUMAN]` | An analyst set it, overrode it, or ratified it | Who, when, and one line of rationale |

**The ratification rule (non-negotiable).** No `[MODEL]` item that materially moves a conclusion ships
without a `[HUMAN]` tag above it. Materiality test: if changing the item by a reasonable amount changes
the rating, the price target by more than 5%, or an allocation recommendation, it is material. A model
may propose. Only a human ratifies. Unratified material `[MODEL]` items are distribution blockers, listed
by name, not summarized as "some assumptions pending."

**Never invert.** A `[MODEL]` figure that a human merely read is still `[MODEL]`. Ratification requires a
recorded decision, not exposure.

---

## Provenance block (goes in every deliverable)

Placement by format:
- **.md / .docx**: final appendix, after disclaimers, titled "Provenance and Attribution."
- **.xlsx**: dedicated `Provenance` tab, plus cell comments on every blue input.
- **.html**: collapsed section at page end, always present in the DOM (not lazy-loaded).
- **Chat/verbal summary**: the Unratified and Single-sourced lines only. Never omit both.

Schema and the fill template: `references/ledger.md`.

---

## Two-source reconciliation

Any figure that drives a conclusion needs a second independent source or an explicit single-sourced label
that survives into the deliverable, not just the run log.

When two sources disagree:
1. Record both values with their as-of dates and period tags. Vintage skew explains most disagreements.
2. Check definitional difference before assuming error (total debt with vs. without leases; GAAP vs.
   adjusted EPS; TTM vs. MRQ). A definitional gap is not a discrepancy, it is a labeling failure.
3. If the gap survives steps 1 and 2, report the range in the deliverable and use the higher-tier source
   for the model. Log the choice and the tier rationale.
4. Never silently pick one. Never average them.

Tier hierarchy and the connector routing table: `references/vendor-map.md`.

---

## Guardrails

1. **Tag at capture, not at write-up.** Retrofitting attribution is how laundering happens. Every number
   gets its tag the moment it enters the working set.
2. **Provenance passes are additive only.** This layer never edits a figure, a conclusion, or compliance
   language. It records and blocks. If it finds an error, it raises a blocker, it does not fix.
3. **Absence is a finding.** "No provenance block" is never an acceptable state for a shipped deliverable.
   If the block cannot be completed, the gaps get named in it.
4. **Client-facing overlay.** For anything a client may see, the block additionally confirms: no performance
   guarantee language, balanced risk language present where a recommendation appears, and past-performance
   framing that does not imply future results. Flag anything reading as personalized advice for human review
   before it goes out.
5. On any failure or friction while using this skill, log it via `skill-improver`.
