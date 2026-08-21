---
name: llm-council
description: >
  5-advisor decision council: independent analysis, anonymous peer review, chairman
  synthesis. Trigger on: "council this", "run the council", "war room this",
  "pressure-test this", "stress-test this", "debate this", "should I X or Y",
  "I can't decide", "I'm torn between", "validate this", "is this the right move".
  Gate: two reasonable people must be able to defend opposite conclusions.
  Skip for factual lookups, creation tasks, trivial preferences, emotional distress.
---

# LLM Council

A 5-advisor decision framework. Advisors analyze independently, peer-review anonymously,
then a Chairman synthesizes a final verdict. See `assets/ref.md` for all prompt templates,
advisor definitions, reviewer roles, and HTML design spec.

**Architectural note:** Single-model simulation of multi-agent deliberation. Isolation is
enforced by prompt discipline, not separate model calls. This appears in every report footer.

**Independence reality (point of use, not just the footer):** Later advisors are generated
inside a context that already holds the earlier ones, so word choice and argument shape leak
forward even when nothing is explicitly passed. The mitigation is hard lens-anchoring plus a
no-cross-referencing instruction, which buys "meaningfully different lenses," not statistical
independence. The Chairman sees everything at once and is the most capture-prone role: its
default output drifts toward the model's prior, which is why the Chairman template forces a
steelman of the losing side and a falsification condition. Every quality gate is self-assessed
by the same model, so gates are forcing functions, not proofs. Full detail in `assets/ref.md`.

---

## When to Run the Council

**Primary gate:** Could two reasonable, informed people reach opposite conclusions both
of which are defensible? If no, skip the council and answer directly.

**Good questions:** Strategic tradeoffs, timing decisions, positioning choices, hiring vs.
automation, pricing options, acquisition targets, pivot decisions.

**Hard stops (respond directly instead):**
- One correct answer exists
- Pure creation task with no embedded decision
- Question is too vague to frame (ask one clarifying question first)
- Fails the "two reasonable people" gate
- User is emotionally distressed (offer support, not analysis)
- Medical/legal/financial stakes requiring professional counsel. See High Stakes Handling
  in `assets/ref.md`. The council may run only to structure the tradeoff, never to issue a
  directive, and the caveat renders at the top of the report outside any collapsible.

**When you skip the council, say so.** Do not silently fall back to a direct answer. State in
one line that you considered the council and why you skipped it (for example, "one correct
answer exists" or "fails the two-reasonable-people gate"), then answer directly. Silent skips
hide the gate from the user and make the gate impossible to audit.

---

## Execution Protocol

### Phase 0: Guardrails Check

Run hard stops first. Then check quality forks.

**Quality forks (modify, don't abort):**
- Thin context → enrich from history; if still thin, ask one question before framing
- 4+ sub-questions → scope to highest-stakes one, flag what was set aside
- User wants validation → run anyway (council often says what they don't want to hear)
- Technical/expert domain → Outsider uses intelligent non-expert lens (see `assets/ref.md`)
- Long context block (500+ words) → compress to 100-150 word digest; preserve all numbers
- Strategic/timing/pricing decision → consider The Analogist as 6th advisor, but only if it
  passes the two-part invocation rule in `assets/ref.md` (real precedent class AND a base rate
  the abstract advisors cannot supply). Do not default to invoking it on every strategic call.

**Token budgets:**
Standard. Advisors: 150-300 words. Reviewers: under 200. Chairman: 400-600.
High-complexity (M&A, org restructure, fund structure): advisors 300-450, Chairman 600-800.
Flag high-complexity mode to the user when active.

---

### Phase 1: Frame the Question

Scan conversation history and attachments. Look for: domain, constraints, prior decisions,
numbers, stated goals, what the user has ruled out, internal contradictions.

**Bias audit (required before writing the frame):**
- Does "what's at stake" load toward one answer?
- Does context selection omit facts favoring the other side?
- Does the framing embed assumptions the user hasn't stated?
If yes to any, rewrite until neutral.

**Frame must include:**
1. Core decision or question
2. Key facts from the user's message (no spin)
3. Context from history or attachments
4. Stakes: both the upside of getting it right and the downside of getting it wrong
5. Constraints and non-negotiables
6. What the user has already tried or ruled out

**Frame validation (required):**
Show the framed question to the user before proceeding:
"Here is how I've framed your question for the council. Does this capture the situation
accurately, or should I adjust anything before proceeding?"
Wait for confirmation. Revise if needed. Do not proceed to Phase 2 without confirmation.

---

### Phase 2: Convene the Council

Run all advisors sequentially using full isolation. Complete each response before starting
the next. Do not let earlier responses bleed into later ones. Check for echo drift; if a
later advisor sounds like a softened version of an earlier one, rewrite from the raw lens.

Standard: 5 advisors. Extended: 6 (add Analogist per Phase 0 fork).

Use the advisor prompt template from `assets/ref.md`. Each advisor receives only:
their identity/style (from `assets/ref.md`), the confirmed framed question, and isolation
instructions. Nothing else.

---

### Phase 3: Peer Review

Map advisor responses to letters A-E (randomize mapping each session). Log privately for
Phase 4 de-anonymization. Do not reveal the mapping to reviewers.

Run 5 differentiated reviewers using roles and prompt template from `assets/ref.md`.
Each reviewer has a distinct lens. Do not assign the same generic task to all five.

Reviewer conflict resolution: if reviewers disagree 3-2 on strongest response, weight by
role relevance to the decision type. State the weighting rationale in the synthesis.

---

### Phase 4: Chairman Synthesis

De-anonymize. Pass to Chairman: confirmed framed question, all named advisor responses,
all 5 labeled peer reviews.

Use the Chairman prompt template from `assets/ref.md`. The template now forces two anti-capture
moves: a steelman of the losing side before the recommendation, and a falsification condition
(the single fact that would flip the call). Keep both. They exist to counter the Chairman's pull
toward the comfortable middle, which is the single largest source of lost council value.

**High stakes routing:** if the decision is medical, legal, financial, or touches safety of
others, the Chairman structures the tradeoff and routes to a professional rather than issuing a
directive (see High Stakes Handling in `assets/ref.md`).

**Internal consistency check before finalizing:**
The "One Thing to Do First" must flow logically from "The Recommendation." If they
conflict, revise until they cohere.

---

### Phase 5: Render the Report

Generate a single self-contained HTML artifact. Use `assets/report-template.html` as base:
open it, replace all `{{VARIABLE_NAME}}` placeholders with session content, paste the result.
Variable reference is in `assets/ref.md`. If filesystem access is unavailable, regenerate
from the design spec in `assets/ref.md`.

**Report structure:**
1. Header: confirmed framed question + session metadata
2. Chairman verdict (open by default)
3. Alignment grid (rows = key themes, columns = advisors, ✓ / ✗ / —)
4. Collapsible advisor responses
5. Collapsible peer review (labeled with reviewer roles)
6. Footer with timestamp + architectural limitation notice (verbatim text in `assets/ref.md`)

No CDN. No external dependencies. Fully self-contained.

---

### Phase 6: Session Log

After the artifact, post this markdown summary in the conversation:

```
**Council Session Summary**
Question: [one-line confirmed framed version]
Ran: [timestamp]
Advisors: [5 standard / 6 if Analogist invoked]
Gates: [all passed, or name any that failed and why]

Key agreement: [1-2 sentences]
Key clash: [1-2 sentences]
Recommendation: [1-2 sentences]
First step: [one sentence, must match recommendation]

Full report: [artifact above]
```

---

### Mid-Session Handling

Do not assume a clean single pass. Handle these without re-running the whole council:

- **Question changes after frame confirmation** → re-validate the frame, flag that prior phases
  are now stale, and only re-run the phases the change touches.
- **User pushes back on the Chairman's recommendation** → do not re-run all five advisors.
  Re-task the two advisors most relevant to the specific objection, then re-synthesize just that
  thread.
- **User wants to dig into one advisor** → expand that advisor's lens on the specific
  sub-question. No full re-run.
- **Context window pressure mid-run** → compress each advisor response to its single
  load-bearing claim before Chairman synthesis, rather than truncating mid-phase.
- **User disagrees with the verdict on the merits** → that is a valid output. Capture the
  disagreement, do not defend the verdict reflexively.

---

## Quality Gates

Fix all failures before delivering.

- [ ] Frame validated by user before council ran
- [ ] Framed question is neutral (no embedded assumptions, no loading)
- [ ] Chairman gave a real recommendation (not unresolved "it depends")
- [ ] Chairman steelmanned the losing side AND stated a falsification condition
- [ ] "One Thing to Do First" is a single action, not a list
- [ ] Recommendation and first step are logically consistent
- [ ] At least one genuine clash is present (if not, add consensus flag). Never fabricate a
      clash to pass this gate. Honest consensus plus the flag beats invented tension.
- [ ] Outsider response free of expert jargon (rewrite if jargon-heavy)
- [ ] All peer review blind spots addressed (not just acknowledged) in chairman synthesis
- [ ] Gap Auditor findings explicitly named in "Blind Spots the Council Caught"
- [ ] High-stakes decisions routed to a professional; caveat rendered outside any collapsible
- [ ] Gate results logged in the session summary (passed, or failures named)
- [ ] HTML is self-contained (no broken refs, no CDN, no external deps)
- [ ] Footer contains architectural limitation notice verbatim (see `assets/ref.md`)
- [ ] If Analogist invoked, parallel is named, fit is labeled, and the key disanalogy is stated

**Consensus flag (add to report if clash gate fails):**
"The council reached unusual consensus. This may indicate the decision is clearer than
it feels, or the framing did not surface meaningful tension. Consider reframing with
sharper constraints before acting."

---

## Anti-Patterns

**Triggering:** Council on trivial preferences. Council on emotional distress. Skipping the
two-reasonable-people gate.

**Framing:** Loading the stakes toward one answer. Omitting countervailing context. Skipping
the bias audit. Skipping frame validation.

**Advisors:** Passing earlier responses to later advisors. Allowing echo drift. Outsider using
jargon. Executor and First Principles converging (push both harder).

**Peer review:** All 5 reviewers using the same generic lens. Reviewers re-flagging what
advisors already said. Ignoring role weighting when picks diverge.

**Synthesis:** Smoothing over real disagreements. Chairman giving a list. Unresolved "it
depends." Peer review flagged something the chairman ignores. Misaligned recommendation and
first step.

**Output:** Recommendation buried in the report. Chairman section collapsed by default.
JS or external resources in the artifact. Missing architectural limitation notice.

---

## Reference

All canonical detail lives in `assets/ref.md`: full advisor and reviewer definitions, the
anti-collapse pairing guidance, the Analogist invocation rule, every prompt template (advisor,
analogist, reviewer, chairman), the high-stakes handling rule, the HTML design spec, the verbatim
footer notice, and the template variable map. Read it before Phase 2. Edit it there, not here,
so there is one source of truth.

> `assets/report-template.html`: self-contained HTML report with `{{VARIABLE_NAME}}` placeholders.
> `assets/ref.md`: canonical definitions, templates, design spec, and variable reference.

The quick tables below are a glance reference only. The authoritative wording is in `ref.md`.

---

### Advisor Definitions (quick reference)

| Advisor | Thinking Style |
|---|---|
| **The Contrarian** | Assumes the plan fails and hunts for the reason. Names the single fatal flaw. |
| **The First Principles Thinker** | Strips assumptions, rebuilds from base facts. Attacks the framing, not the options inside it. Asks if this is even the right problem. |
| **The Expansionist** | Finds the upside everyone discounted. Asks what compounds if this works better than the base case. |
| **The Outsider** | Zero assumed expertise, zero jargon. Receives the same framed question but reads it as a smart generalist on day one: flags terms that smuggle assumptions, asks the obvious skipped question. Not a naive bystander, not context free. |
| **The Executor** | Cares only about Monday morning. First action, who does it, what breaks first. First-order risks only. |
| **The Analogist** *(optional)* | Closest historical parallel plus the base rate. Must label fit (Strong/Partial/Loose) and name the key disanalogy. Invoke only per the two-part rule in `ref.md`. |

Anti-collapse watch: Contrarian (attacks the plan) vs First Principles (attacks the problem
definition). Expansionist vs Analogist (base rate, not cheerleading). Executor vs First
Principles (first breaks vs foundations). Full guidance in `ref.md`.

---

### Peer Reviewer Roles (quick reference)

| Reviewer | Role |
|---|---|
| Reviewer 1 | **Logic Auditor.** Fallacies, non-sequiturs, unsupported leaps. |
| Reviewer 2 | **Data Auditor.** Missing data, unverified assumptions, cherry-picked evidence. |
| Reviewer 3 | **Second Order Auditor.** Downstream and systemic effects: dependencies, sequencing, org friction, what this forecloses, what it triggers 2-3 steps later. NOT first-order Monday-morning risks (that is the Executor). Push the council to second order if only first-order risks surfaced. |
| Reviewer 4 | **Convergence Auditor.** Where advisors genuinely agree and how solid it is. If the council mostly disagrees, flip to finding fragile or false convergence; a fully fractured council is itself a finding. |
| Reviewer 5 | **Gap Auditor.** What ALL five missed. No credit for re-flagging an existing point. |

Prompt templates, high-stakes handling, HTML design spec, footer notice, and the full variable
reference are in `assets/ref.md`.
