# Compress

CLEAN removes what the piece never needed. COMPRESS removes things the piece did need, because
the piece has to be shorter than it is. That is a different job with a different guardrail, and
conflating them is how good material disappears without anyone noticing.

Guardrail 2 (preserve substance) is suspended in this mode, and only in this mode. In exchange,
COMPRESS carries an obligation the other modes do not: everything cut above the trivial line is
reported.

## Contents
- When this mode runs
- The target
- The cut ladder
- What never gets cut
- The drop report
- Output

## When this mode runs

A supplied draft plus a length instruction: "cut this to 400 words," "make it one page," "this
has to fit on a slide," "half the length," "tighten for the email body," "trim 30%."

A length instruction with no draft is DRAFT with a length constraint, not COMPRESS.

A draft plus "tighten this" with no target is CLEAN, not COMPRESS. Tighten means remove slack.
Compress means remove content. When the ask is ambiguous, run CLEAN first and report the
resulting length; if it is still over, say so and ask for the target rather than guessing which
substance to lose.

## The target

Get a number before cutting. Words, pages, characters, slide lines, or a percentage. "Shorter"
is not a target and produces an arbitrary result the author has to redo.

If the author gives a target the material cannot survive, say so before cutting rather than
after. A 900-word IC memo compressed to 200 words is a different document, not a shorter one.
State what the piece becomes at that length and what it can no longer do, then either cut to the
target with the drop report making the loss visible, or propose the shortest length that keeps
the argument intact. Do not silently deliver a version that no longer supports its own
conclusion.

## The cut ladder

Work top to bottom. Stop when you hit the target. Never start below rung 3.

1. **Slop.** Run the quick tier of GATE v1 first. Filler, throat-clearing, hedge stacks,
   restatement, and glued transitions typically return 10 to 20% with zero substance loss. Most
   requests that sound like compression are satisfied here.
2. **Redundancy.** The point made twice in different words. The example that proves what the
   previous example already proved. The summary paragraph restating the section above it. The
   caveat repeated in three places.
3. **Supporting detail behind a claim already carried.** Second and third pieces of evidence for
   a point the first one established. Keep the strongest, cut the rest, and note the cut.
4. **Secondary claims.** Arguments that support the thesis but are not load-bearing. Cut whole,
   never half: a claim reduced to a fragment is worse than a claim removed.
5. **Context and background.** Material the reader can supply themselves or already has. Cut
   more aggressively as reader expertise rises.
6. **Nuance and qualification.** Last, and reluctantly, because this is where compression starts
   changing what the piece asserts. Every cut here goes in the drop report with the risk named.

Compression is structural before it is lexical. Cutting one paragraph beats shaving nine
sentences, and it leaves prose that still reads like prose. A piece compressed word by word ends
up uniformly dense and unreadable, which defeats the purpose.

**Decks and other non-prose.** When the unit is a slide, a section, or a table row rather than a
sentence, the ladder still runs top to bottom but the operations change. Rung 1 is the slide that
says nothing, the agenda, the divider, the thank-you. Rung 2 is the chart repeating a number
already on an earlier slide. Rung 3 is the second and third supporting exhibit behind a point the
first exhibit made. Rung 4 is the whole secondary section, cut entire, never left as an orphan
header. Rung 5 is background the audience already has. Rung 6, last, is the qualifying footnote,
and every one of those goes in the drop report. Merging two thin slides counts as a cut and gets
reported as a merge. Never solve a slide count by shrinking type or stacking bullets. The drop
report names slides and sections, not sentences, and the artifact rule runs on the rebuilt file.

## What never gets cut

- Any figure, date, source, as-of stamp, or proper noun.
- Any `[TK: ...]` placeholder. A compressed draft with a missing fact still has a missing fact.
- Compliance language required by `domain-finance.md` or `domain-wealth.md`. If the target
  cannot be met with the required disclosure in place, the target is wrong. Say so.
- The balanced risk language attached to any recommendation.
- The conclusion, the ask, and the next step with its owner and date.
- The strongest counterargument, where the piece engages one. Cutting the objection to save
  words converts an honest argument into a one-sided one.

## The drop report

Two to five lines, delivered with the output. It names what left at rungs 3 through 6, not the
slop and redundancy from rungs 1 and 2. The author needs to know what they lost so they can veto
it, and they cannot veto what they cannot see.

```
Cut to 412 words from 890.
Dropped: the second and third margin comparisons (kept the peer-median one), the
2023 background paragraph, the qualification on the tax assumption.
Risk: the tax qualification was load-bearing for the after-tax number. Recommend
restoring it as a footnote.
```

## Output

The compressed text, the word or page count against the target, the drop report, then GATE v1 on
the compressed version. Never reprint the original. Never show intermediate lengths.

If the piece hit its target at rung 1 or 2, say that explicitly. "Reached 400 words on slop and
redundancy alone; no substance removed" is the best outcome this mode produces, and the author
should know when they got it.
