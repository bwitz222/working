# Diagnostics, the failure-mode catalog

The substance of the teardown. Work the layers top to bottom, argument first, polish last: a
flawless sentence serving a broken claim is wasted effort.

Each failure mode gives **Spot**, **Matters**, **Fix** (the direction, not fill-in-the-blank).
Cite the location. Calibrate severity per `critique-scorecard.md`, loaded alongside this. Most of
what follows is Major or Minor; only argument-level breaks are usually Critical.

## Contents
- L1 Argument and substance
- L2 Evidence and integrity
- L3 Structure and flow
- L4 Prose and voice
- L5 Audience and purpose fit
- Finding the load-bearing flaw

---

## L1, Argument and substance

This is where pieces actually die. If L1 is broken, nothing downstream saves it.

### No claim, just a topic
- **Spot:** Try to state the thesis in one sentence as a claim someone could disagree
  with. If the best you can do is name a subject ("this is about AI in finance"), there's
  no thesis.
- **Matters:** A piece without a contestable claim has nothing to prove and nothing to
  defend. The reader leaves with information, not conviction. Usually Critical for
  persuasive or argumentative work, fine for pure reference.
- **Fix:** Force the claim to the surface. "What do you want the reader to believe or do
  that they didn't before?" Put that sentence near the top.

### The "so what" is missing
- **Spot:** The claim is true but inert. Ask "so what?" three times. If you hit a dead
  end, there are no stakes.
- **Matters:** True-but-trivial wastes the reader. Stakes are why anyone keeps reading.
- **Fix:** Connect the claim to a consequence the reader cares about. Name who is affected
  and how.

### Logic that doesn't hold
Name the specific break. A vague "this doesn't follow" is weak; the named fault is
unarguable.
- **Non-sequitur:** conclusion doesn't follow from premises. The leap is unstated.
- **Equivocation:** a key word shifts meaning mid-argument ("risk" as volatility, then as
  permanent loss).
- **False dichotomy:** "either X or Y" when Z exists. Common in persuasion.
- **Circularity:** the conclusion is smuggled into a premise. The argument assumes what it
  claims to prove.
- **Hasty generalization:** one case or a tiny sample stands in for the rule.
- **Motte-and-bailey:** a bold claim (bailey) defended by retreating to a modest, obvious
  one (motte) when challenged. Watch for a thesis that gets quietly smaller.
- **Base-rate neglect:** a vivid specific overrides the underlying frequency. Endemic in
  finance ("this 10-bagger proves the strategy works").
- **Correlation as causation:** two things move together, so one is claimed to cause the
  other. Demand the mechanism.
- **Survivorship or selection bias:** only the winners, or the visible cases, are counted.
- **Matters:** A single load-bearing logical break is Critical; a hostile reader stops
  trusting everything after it. A break in a side point is Major.
- **Fix:** Supply the missing step, narrow the claim to what the logic supports, or cut
  the move.

### Restating consensus in a nicer suit
- **Spot:** Strip the style. Is the remaining claim something the target reader already
  believes? If yes, there's no news.
- **Matters:** Sophisticated readers punish the obvious. In research and op-ed, "no
  variant view" is close to fatal.
- **Fix:** Find the part that is non-obvious or contrarian and lead with it, or admit the
  piece is a primer and pitch it to a less-expert reader.

### Hidden load-bearing assumptions
- **Spot:** Ask "what must be true for this to work that the author never says?" List the
  unstated premises. Are any shaky?
- **Matters:** An argument is only as strong as its weakest unstated assumption, and
  readers attack exactly there.
- **Fix:** Surface the key assumption and defend it, or acknowledge it as a condition.

---

## L2, Evidence and integrity

Where credibility is won or lost. In finance, academia, and anything external, this is as
important as L1.

### Overclaiming
- **Spot:** Compare the strength of each assertion to the strength of its support.
  "Proves," "guarantees," "will," "always" over thin or absent evidence.
- **Matters:** One overclaim a knowledgeable reader catches taints every other claim.
  Often Critical for high-stakes work.
- **Fix:** Right-size the verb to the evidence: "suggests," "is consistent with," "in this
  sample." Confidence should track proof.

### Wrong, not just unsupported
- **Spot:** A claim that is not merely lacking a citation but factually incorrect: a
  misstated definition, a number that contradicts the public record, a mischaracterized
  source, a term used to mean something it doesn't. This needs domain knowledge, so judge
  only where you have it.
- **Matters:** A factual error a reader catches is worse than an unsupported one; it
  proves the author didn't check, and it's the fastest way to lose an expert audience.
- **Fix:** Correct it directly, cite the correction or mark `[TK: verify]`, and flag your
  confidence (certain vs. "I think this is off, check it"). Distinguish clearly in the
  critique between "you didn't support this" and "this is wrong."

### Weasel attributions
- **Spot:** "Studies show," "experts agree," "it's widely known," "research suggests,"
  "many believe," with no named source.
- **Matters:** Unsourced authority is no authority. It reads as bluff and invites the
  reader to supply their own counterexample.
- **Fix:** Name the source or cut the claim. Never invent a citation to fill the gap;
  insert `[TK: source]`.

### Cherry-picked data or timeframe
- **Spot:** A start date that flatters, a peer set chosen to win, one metric while the
  others stay silent, "since 2009" for an equity chart.
- **Matters:** Selective evidence is a credibility bomb when the reader knows the field.
- **Fix:** Show the fuller picture or justify the window. If the honest data is weaker, the
  claim has to weaken with it.

### False precision
- **Spot:** "Increases productivity by 37.4%" from a soft estimate. Decimal places the
  method can't support.
- **Matters:** Precision implies rigor; fake precision, once spotted, destroys trust.
- **Fix:** Round to the honest resolution, or show the method that earns the digits.

### Unfalsifiable claims
- **Spot:** Ask "what evidence would prove this wrong?" If nothing could, it's not an
  argument, it's a belief.
- **Matters:** Unfalsifiable claims persuade no skeptic and signal hand-waving.
- **Fix:** Make it testable, or frame it honestly as a judgment or prediction with
  conditions.

### Fabrication tells (highest priority)
- **Spot:** Suspiciously round or convenient numbers, quotes with no attributable origin,
  statistics that would be hard to actually gather, citations you can't verify, details
  too perfect.
- **Matters:** Fabrication is the one unrecoverable failure. Flag any suspected invention
  loudly and never replicate it in the rewrite.
- **Fix:** Demand a source from the author or strip the claim to `[TK: verify]`.

---

## L3, Structure and flow

### Throat-clearing opening
- **Spot:** The first paragraph is context, definitions, or "in today's world." The real
  point arrives in paragraph three.
- **Matters:** Readers decide in the first lines. A slow open loses them before the
  argument starts.
- **Fix:** Cut to the strongest, most specific thing you can lead with. Move context to
  where it's needed, not before.

### Buried lede
- **Spot:** The most interesting or important sentence is in the middle or the end.
- **Matters:** Strength hidden is strength wasted; busy readers never reach it.
- **Fix:** Promote it. Reorder so the piece opens near its peak.

### Paragraphs doing more than one job
- **Spot:** A paragraph you can't summarize in one phrase. Two ideas wrestling in one
  block.
- **Matters:** One idea per paragraph is how readers track an argument. Muddle here reads
  as muddled thinking.
- **Fix:** Split, or cut the weaker idea.

### Glued transitions
- **Spot:** "Additionally," "Moreover," "Furthermore" doing the work that logic should.
  Paragraphs in sequence with no actual connection.
- **Matters:** Connective words can't manufacture a connection that isn't there. The seams
  show.
- **Fix:** Make the link real (each beat earns the next) or reorder so the sequence is
  self-evident.

### Scope wrong
- **Spot:** Too much (three arguments fighting for one piece) or too little (a claim that
  never got its support).
- **Matters:** Over-scope dilutes; under-scope leaves the claim naked.
- **Fix:** Cut to one spine, or add the missing development. Pick the fight you can win.

### Ending that just stops, or summarizes itself
- **Spot:** A final paragraph that restates the intro, or trails off, or opens with "in
  conclusion."
- **Matters:** The last line is what the reader carries out. Waste it and the piece
  evaporates.
- **Fix:** End on the implication, the consequence, or the sharpest statement of the
  claim, not a recap.

---

## L4, Prose and voice

Mechanics belong to GATE v1: 7 rules at the quick tier, 24 patterns at the deep tier, and in
CRITIQUE `deslop-rules.md` is already loaded, so do not restate its catalog here. At the
diagnosis stage flag only prose problems severe enough to mislead the reader or bore them out of
the piece. Do not litter Critical or Major with comma notes, and do not pad Minor with a generic
tells checklist.

In COACH, where the gate does not run, name the three tells that cost this author most. Usually:
AI vocabulary and significance inflation, negative parallelism ("not just X, it's Y"), and
metronomic rhythm. Em dashes are a flat error at any tier, not a threshold.

- **Matters:** Slop signals the author did not think hard, or did not write it. For external or
  published work that is a Major credibility problem, not a Minor one.
- **Fix:** Run the gate. Preserve meaning and register; do not inject voice into copy that must
  stay neutral.

---

## L5, Audience and purpose fit

### Wrong register
- **Spot:** Casual voice in a board memo, a jargon wall for non-experts, stiff corporate
  tone in a personal essay.
- **Matters:** Register mismatch breaks trust faster than almost anything; the reader feels
  the piece wasn't written for them. Often Critical.
- **Fix:** Match the formality and vocabulary the reader and form demand.

### Doesn't move THIS reader toward THAT goal
- **Spot:** Re-read as the actual target reader (the skeptical CIO, the tired hiring
  manager, the peer reviewer). Does it do its job on them?
- **Matters:** Writing that's good in the abstract but wrong for the reader still fails.
- **Fix:** Re-aim. Cut what the reader already knows, add what they need to act, answer
  their objection.

### Disrespects the reader
- **Spot:** Over-explaining the obvious, hedging every claim, hand-holding, applause lights
  ("as we all know, innovation matters").
- **Matters:** Smart readers feel condescended to and stop trusting the author's judgment.
- **Fix:** Trust the reader. Cut the throat-clearing and the qualifiers. Say the thing.

---

## Finding the load-bearing flaw

After working the layers, name the one problem whose fix most improves the piece. It is
almost always in L1 or L2, rarely in L4. Heuristic: if you could fix exactly one thing,
what would do the most for the reader? That answer is the spine of the verdict.
Everything else ranks beneath it. Don't bury it under cosmetics.
