# Call Ledger and Grading Protocol

Load when logging a new call or grading past ones. The ledger is a CSV the analyst owns, not a file this
skill generates fresh each time.

## Why a ledger

When analytical production is cheap and abundant, output volume stops proxying for skill. The only way to
know whether an AI-augmented research process adds alpha rather than pages is to record every call before
the outcome is known and grade it on a fixed schedule. A ledger written after the fact is a story.

Two properties make it work: entries are immutable once written, and the grading date is set at entry, not
chosen later when the result is known.

## Schema

Default path: `~/research/call-ledger.csv`. One row per call, appended, never edited except the
outcome columns at grading time.

| Column | Type | Filled at | Notes |
|---|---|---|---|
| `call_id` | string | entry | `YYYY-MM-DD_TICKER` |
| `date_entered` | ISO date | entry | |
| `ticker` | string | entry | |
| `direction` | enum | entry | `long`, `short`, `avoid`, `hold` |
| `conviction` | int 1-5 | entry | Sized honestly. If everything is a 4, the scale is dead. |
| `entry_price` | float | entry | With as-of timestamp |
| `price_target` | float | entry | |
| `horizon_months` | int | entry | Sets the grade date |
| `benchmark` | string | entry | The benchmark the call must beat. Default SPY, sector ETF where the thesis is sector-neutral. |
| `thesis_one_line` | string | entry | One sentence. If it takes three, the thesis is not formed. |
| `primary_driver` | string | entry | The single variable the call rests on |
| `kill_criteria` | string | entry | The dated, observable events that end the thesis (from equity-research-foundation Path 6, step 7) |
| `variant_view` | string | entry | Where this differs from consensus, and what consensus was on the entry date |
| `consensus_pt_at_entry` | float | entry | Positioning context, never a model input |
| `pipeline_used` | string | entry | Which skill/depth produced it |
| `model_share` | enum | entry | `low`, `medium`, `high`. How much of the thesis came from `[MODEL]` items vs. human judgment. This is the column that eventually answers whether the AI layer helps. |
| `grade_date` | ISO date | entry | `date_entered` + `horizon_months` |
| `exit_price` | float | grading | |
| `benchmark_return` | float | grading | Over the same window |
| `outcome` | enum | grading | `right`, `wrong`, `right_wrong_reason`, `killed`, `open` |
| `driver_played_out` | bool | grading | Did `primary_driver` actually move as expected |
| `post_mortem` | string | grading | Two sentences maximum |

**`right_wrong_reason` matters more than the other outcomes.** A call that made money for a reason the
thesis never named is a coin flip that paid, and counting it as a win corrupts the whole record.

## Entry protocol

Log at the moment of the call, before any outcome is observable. The entry is complete or it is not made.
An incomplete row is worse than no row because it looks like a record.

Two hard rules:
- `kill_criteria` and `variant_view` cannot be blank. A call with neither is not a call, it is a lean.
- `entry_price` carries its timestamp. Backdating an entry price invalidates the row.

## Grading protocol (quarterly)

Run `scripts/grade_calls.py` against the ledger. It computes, for all rows past their grade date:

- Hit rate, overall and by conviction bucket
- Average excess return vs. the row's own benchmark, not a single index for the whole book
- Calibration: does conviction 5 actually outperform conviction 3, or is the scale noise
- `right_wrong_reason` share, which is the process-quality read
- Driver accuracy: how often `primary_driver` moved as forecast
- Split by `model_share`, which is the only direct read on whether the AI-augmented path is adding value

What to do with the output:

| Finding | Read |
|---|---|
| Hit rate fine, driver accuracy poor | The process is picking winners for reasons it does not understand. Not repeatable. |
| Conviction 5 underperforms conviction 3 | The conviction scale is measuring enthusiasm, not edge. Recalibrate or drop it. |
| `high` model_share underperforms `low` | The AI layer is adding volume, not judgment. Tighten the ratification rule. |
| `high` model_share outperforms | Worth knowing, and worth checking whether it is concentrated in a few names before generalizing |
| Small sample | Say so. Under roughly 20 graded calls, report the numbers and refuse to draw conclusions from them. |

**Sample-size discipline.** Hit rate on 8 calls is not a track record. Report the count next to every
statistic, always. Never present a percentage without its denominator.

## Interaction with other skills

- Thesis, kill criteria, and variant view come from `equity-research-foundation` Path 6 (steps 7 and 8).
- Price target and scenario weights come from `dcf`.
- The plugin skill `equity-research:thesis-tracker` handles ongoing thesis maintenance between entry and
  grading. This ledger is the scoreboard, not the running commentary. Do not duplicate.
