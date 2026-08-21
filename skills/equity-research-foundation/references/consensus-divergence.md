# Consensus Divergence and Cognitive Convergence

Load for Path 6 step 8, and any time the question is whether a view is actually differentiated.

## The mechanism

Grossman-Stiglitz says a costly-information equilibrium requires that research be rewarded, which
requires that some prices be wrong and that not everyone see the same thing at the same time. That
condition weakens when the cost of producing structured analysis collapses and when analysis is
produced by overlapping architectures reading overlapping inputs.

Two distinct risks follow, and they need separating because the responses differ:

**Convergence risk (systemic).** When many participants run similar models over similar data, analytical
outputs correlate. Interpretive diversity, which is what makes a market resilient, compresses. This is
the "monoculture" concern in the systemic-risk literature. It is not something a single analyst controls.

**Derivative-view risk (yours).** Your own output drifts toward consensus without you noticing, because
the same sources, the same framing, and the same tooling produce the same conclusion. You then hold a
consensus view while believing you hold a researched one. This is entirely within your control and it
is what this gate exists to catch.

The failure is specific and worth naming: an AI-assisted process is very good at producing a
well-argued restatement of the prevailing view. It reads like research because it is well-argued. It is
not research, because it carries no information the price does not already contain.

## Path 6, Step 8: the divergence gate

Runs after the falsification step, before synthesis. Four questions, answered explicitly. An answer of
"I do not know" is a valid finding and stops the gate.

### 1. What is consensus, stated as a number?
Not "the market likes it." The specific figures: consensus revenue and EPS for the next two fiscal
years, the analyst price-target range and its median, the current multiple against the company's own
history and against peers. Live-sourced and dated. A divergence claim measured against a vague sense of
market mood is not measurable and cannot be graded later.

### 2. Where exactly does the view differ, and by how much?
Name the line item and the magnitude. "I model 2027 gross margin at 41% against consensus 38%, and
that 300bp gap is 70% of the valuation difference." A view that differs on tone rather than on a number
is not a variant view.

If every line sits inside the consensus range, say so plainly. Agreeing with consensus is a legitimate
conclusion. It is only a problem when it is unacknowledged, because then the position is sized as
though it carried edge.

### 3. Why does the gap persist?
The hard question, and the one most often skipped. If the insight were both correct and available, why
has the price not moved? Acceptable answers name a mechanism:

- **Time-horizon mismatch.** The gap resolves beyond the window most holders are compensated on.
- **Structural exclusion.** Index constraints, market-cap or liquidity screens, or mandate rules keep
  natural buyers out.
- **Interpretive difficulty.** The evidence requires work most participants will not do: segment
  reconstruction, footnote forensics, channel checks.
- **Recency of the disconfirming evidence.** The datapoint is genuinely new and not yet diffused.

Not acceptable: "the market is short-sighted," "investors are irrational," or nothing at all. If no
mechanism can be named, the most likely explanation is that the view is not actually variant and the
gap is a modeling artifact.

### 4. Could this view just be the model's restatement of consensus?
The self-audit. Check, concretely:

- Did any part of the thesis come from a source that itself aggregates sell-side output (a summary
  page, a consensus feed, an AI-generated overview)? Those routes import consensus and disguise it as
  independent reasoning.
- Does any conclusion rest on a fact that appears in the last two quarters' sell-side notes and nowhere
  else in the working set?
- Was the peer set model-selected? If so, it likely reproduces a standard screen, which encodes the
  standard framing along with it.
- Would a competent analyst using the same tooling and the same public inputs reach the same
  conclusion in an afternoon? If yes, the conclusion may be correct and is unlikely to be edge.

Record the answer. It is not a rhetorical prompt.

## Output format

Six lines in the brief, immediately before the synthesis:

```
CONSENSUS: {revenue/EPS estimates, PT range and median, current multiple vs. history and peers, dated}
VARIANT VIEW: {the line item, the magnitude of the gap, the share of the valuation difference it drives}
PERSISTENCE MECHANISM: {why the gap survives, or "none identified"}
DERIVATIVE-VIEW CHECK: {which inputs could be importing consensus, and what was done about it}
IF NO EDGE: {say so plainly, and what the name would need to look like to become interesting}
CONFIDENCE: {high / medium / low, and what the gap rests on}
```

The variant view and the persistence mechanism carry into the call ledger
(`decision-provenance/references/call-ledger.md`), where they are graded against outcome. That link is
what eventually turns this gate from an assertion into a measurement: a process that repeatedly claims
variant views which do not play out is producing narrative, not edge.

## Guardrails

1. **No manufactured divergence.** Do not stretch an assumption to create a gap. A fabricated variant
   view is worse than an honest consensus view because it invites sizing that the evidence does not
   support.
2. **Disagreement is not edge.** Differing from consensus is necessary and not sufficient. Without a
   persistence mechanism, a gap is more likely to be your error than the market's.
3. **The gate fires even when the conclusion is "no edge."** Its purpose is to produce an honest label,
   not to certify a thesis. Most names, most of the time, have no edge, and a process that never says
   so is not running the gate.
4. **State consensus before forming the view where sequencing allows.** Reading consensus first anchors
   you. Where the work is already done, at minimum record when in the process you first saw it.
