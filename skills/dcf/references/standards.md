# Standards — Token Optimization, No AI Slop, Constant Verification

Load this file at the start of every modeling session. These rules apply to every response, every cell, every output.

---

## 1. Token Optimization

**Principle:** Every token must earn its place. Length is not quality. Dense, precise output beats padded prose every time.

### In Chat Responses
- Lead with the answer. Context after, never before.
- One sentence per idea. No compound sentences hiding two points.
- Numbers go in tables or labeled cells, never buried in paragraphs.
- If a point can be a label + value, do not write a sentence about it.
- Omit: "As you can see...", "It's worth noting...", "This is important because...", "In order to..."
- Never restate what the user asked before answering it.

### In Model Narration
When directing the user to the model, use:
```
→ DCF Engine!C18 — Base FCFF Yr3: $142mm
→ Sensitivity!D4 — WACC 9.5% × g 3.0%: $47.20/sh
```
Not:
```
"If you navigate to the DCF Engine tab and look at cell C18, you will find the Base case FCFF for Year 3, which comes out to $142 million."
```

### In Assumption Summaries
Use the Scenario Driver Table format (Step 12). Never prose-summarize a table that already exists in the model.

### In Memos
Follow the Step 14 memo structure exactly. No section may exceed its stated length. If you feel the urge to add a sixth bullet to a "top 3" list, cut the weakest three instead.

---

## 2. No AI Slop

**Definition:** AI slop is output that sounds thorough but adds no information — filler that exists to fill space, not to inform.

### Banned Phrases (never use)
- "Certainly!", "Absolutely!", "Great question!", "Of course!"
- "It's important to note that..."
- "This is a complex topic, but..."
- "I'll walk you through..."
- "Let's dive in."
- "In summary..." (followed by a repeat of what was just said)
- "As an AI language model..."
- "I hope this helps!"
- "Please let me know if you have any questions."
- "Feel free to reach out..."
- Any variation of "I want to make sure I understand your question correctly before I answer it" when the question was clear.

### Banned Structural Patterns
- Opening a response by restating the user's request
- Ending a response with a generic offer to "do more"
- Padding a 3-point answer to 7 points because 7 feels more thorough
- Adding a "disclaimer" paragraph that says nothing legally meaningful
- Listing assumptions twice (once in prose, once in a table)
- Stating a formula in English prose AND in cell notation — pick one

### What to Do Instead
- State the finding. Then the evidence. Then stop.
- If you have three things to say, say three things.
- Hedges belong on legitimate uncertainty only: "Terminal margin assumes tech-sector reversion; no peer currently operates above 38% EBITDA at scale."
- Every sentence must be cut-able only at the cost of losing information.

### Quality Test (apply before sending any response)
For each sentence: *"If I deleted this, would the user lose information they need?"*
- Yes → keep it
- No → cut it

---

## 3. Constant Verification

**Principle:** Never trust a prior output. Every number presented to the user must be traceable to a source right now, not assumed to be correct from a prior step.

### Verify Before Quoting
Before citing any number from the model in chat:
1. State the source cell (e.g., `DCF Engine!F31`)
2. Confirm the formula chain is intact (no hardcoded values in derived cells)
3. Confirm the active scenario toggle matches the scenario being discussed

Never write "the base case IV is $52.40/sh" without checking `Dashboard!C8` or equivalent in that moment.

### Verify Guardrail Status Before Each Section
Before beginning each of Steps 3–9, re-check:
- G-01: WACC > g check cell = "OK"
- G-02: Probability sum = 100% check cell = "OK"
- G-03: Bull > Base > Bear check cell = "OK"
- G-04: WACC > Rf check cell = "OK"
- G-09: Ke > Kd(at) check cell = "OK"

If any check is not "OK" — stop, surface the error by guardrail code, fix it, recheck before proceeding.

### Verify Cross-Sheet Integrity
At completion of each tab:
- Confirm all cross-sheet links resolve (no `#REF!`)
- Confirm the WACC Builder cross-check cell = 0.000 exactly
- Confirm diluted shares in Cap Structure = diluted shares in Assumptions (must match to the unit)

### Verify Scenario Switches Live
After building the DCF Engine, before moving to Sensitivity:
- Set C4 = "Bear" → check IV moves down from Base
- Set C4 = "Bull" → check IV moves up from Base
- Set C4 = "Base" → restore
- If any switch fails to move the output, find the broken IF chain before proceeding

### Verify Sensitivity Grids Are Not Frozen
After building Sensitivity grids:
- Manually change WACC in Assumptions by +50bps → confirm grid center cell updates
- Restore WACC → confirm grid returns to base value
- If grid does not update: there is a hardcoded value or broken reference — find and fix it

### Verify Terminal Value Logic
Before finalizing:
- Compute GGM TV by hand (or in a scratch cell): `=Terminal_FCFF × (1+g) / (WACC−g)`
- Confirm it matches the model output to within rounding
- If TV Method = "Exit Multiple": confirm `=Terminal_EBITDA × exit_multiple` matches model output
- Confirm PV of TV = TV / (1+WACC)^10, not discounted at mid-year period

### Verify Equity Bridge Sign Conventions
Walk the bridge line by line:
- Cash items: positive (adding to equity value)
- Debt / liability items: negative (subtracting from equity value)
- Operating Lease and Finance Lease: separate rows, both negative
- Net result: Equity Value = EV + cash − debt − all liabilities

If Equity Value > EV for a net-debt company: sign error — find and fix before reporting.

### The Dead-Cell Rule
If any cell is hardcoded and it is not a labeled blue-text input in the Assumptions sheet, it is a dead cell — it will silently break when assumptions change. Before any output:
- Search for hardcoded numbers in formula cells (exclude Assumptions sheet and Historicals sheet blue inputs)
- Zero dead cells is the standard. One dead cell is a failure.

### Pre-Output Final Check (runs after Step 15 quality gate)
Ask once, out loud (in your reasoning), for every number in the summary output:
1. Where does this number come from? (Name the cell.)
2. Is that cell a formula or a hardcoded value?
3. Has the scenario toggle been verified to affect this number?
4. Has this guardrail check been confirmed "OK" in the last pass?

If you cannot answer all four for any number: do not include that number in output until you can.
