# Attribution Ledger

Load when tagging figures or building the provenance block. Tags are assigned at capture, never
retrofitted at write-up.

## Tag syntax

Inline (prose, cell comments, HTML tooltips):

```
Revenue CY2025A $4.82 Billion [SRC: 10-K FY2025 p.47 | filed 2026-02-11 | pulled 2026-08-16]
FCF margin 14.2% [CALC: (CFO - capex) / revenue | DCF tab, D38]
Terminal growth 2.4% [MODEL: anchored to 10Y UST 4.31% ceiling and 10-yr sector median volume growth]
  - [HUMAN: Ian, 2026-08-16. Accepted. 2.4% sits below the 2.75% used on the last industrial name
     because this one has no pricing power in a deflationary input cycle.]
Peer set (6 names) [HUMAN: Ian, 2026-08-16. Dropped two the model proposed on revenue-scale mismatch.]
```

Ratification nests directly under the item it ratifies. A `[MODEL]` line with no `[HUMAN]` child beneath
it is unratified by construction, which makes the gap visible rather than something to audit for.

## Materiality test (decides whether ratification is required)

An item is material if a reasonable move in it changes any of:

- the Rating or Recommendation
- the price target by more than 5%
- an allocation, sizing, or rebalancing recommendation
- a risk classification (a green score turning amber, a covenant passing to failing)

Run the test by perturbation, not intuition. Nudge the input, recalc, read the delta. If the perturbation
cannot be run, treat the item as material. Immaterial `[MODEL]` items still carry their tag, they just do
not block distribution.

## Provenance block template

```markdown
## Provenance and Attribution

**Prepared:** {date} | **Analyst of record:** {name} | **Pipeline:** {skill + depth mode}

### Data sources
| Figure class | Primary source | Secondary | As-of | Vintage skew |
|---|---|---|---|---|
| Price / market data | | | | |
| Financial statements | | | | |
| Consensus estimates | | | | |
| Peer multiples | | | | |
| Rates / macro | | | | |

### Model-generated inputs requiring ratification
| # | Input | Value | Basis | Sensitivity | Ratified by / date | Rationale |
|---|---|---|---|---|---|---|

### Human overrides
| # | Model proposed | Analyst set | Why |
|---|---|---|---|

### Single-sourced figures
{list, or "None"}

### Source disagreements carried forward
| Figure | Source A | Source B | Range reported | Which drove the model | Why |
|---|---|---|---|---|---|

### Unratified material items (distribution blockers)
{list by name, or "None"}

### Not verified
{figures marked DATA UNAVAILABLE or UNVERIFIED, and what they would have driven}
```

## Placement by format

| Format | Where |
|---|---|
| .md / .docx | Final appendix, after disclaimers, titled "Provenance and Attribution" |
| .xlsx | Dedicated `Provenance` tab, plus a cell comment on every blue input |
| .html | Collapsed section at page end, always present in the DOM, never lazy-loaded |
| Chat summary | Unratified items and single-sourced figures only. Never omit both. |

## Compression rules

The block scales with the deliverable. Do not pad it.

- **Quick take / 1-page memo:** four lines. Data sources (one row), unratified items, single-sourced,
  disagreements. Empty sections collapse to "None."
- **Standard (Excel + memo):** full table set on a `Provenance` tab.
- **Full initiation:** full table set. Per-exhibit source lines are already required by the SMIF editorial
  skill. Reference them, do not duplicate them into the block.

## What this block is not

Not a methodology section, not a disclaimer, not a caveat dump. It contains no prose arguing the analysis
is sound. It is a record. Why an assumption was chosen belongs in the analysis. Who chose it belongs here.

## Common failure modes

| Failure | What it looks like | Fix |
|---|---|---|
| Retro-tagging | Provenance assembled at the end from memory of where numbers came from | Tag at capture. A number with no tag does not enter the working set. |
| Ratification by exposure | Analyst read the assumption, so it is treated as approved | Ratification is a recorded decision with a rationale line, not exposure |
| Blanket ratification | "All assumptions reviewed and accepted" | Ratify item by item. A blanket line ratifies nothing. |
| Blocker summarizing | "A few inputs still pending" | Name every unratified material item |
| Tag inflation | Everything marked `[SRC]` because it appeared in a fetched page | A model-chosen peer set pulled from a screener is `[MODEL]` on selection, `[SRC]` on the underlying figures |
