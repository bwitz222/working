# Slide Design Reference

## The Visual-First Rule

Before writing any slide: can you show this instead of say it?

| Replace | With |
|---|---|
| "Rates rose sharply in 2022" | Line chart of Fed Funds rate, 2020–2023 |
| "Diversification reduces risk" | Scatter plot: portfolio volatility vs. number of assets |
| "Bond prices fall when rates rise" | Annotated TLT price vs. 10Y yield (inverted axis) |
| "HY spreads widened in March 2020" | HY spread chart with the event circled |
| "Company A is more expensive" | Side-by-side P/E, EV/EBITDA comparison table |

If a chart exists for the claim, use it. Never describe a chart in words.

---

## Aesthetic Execution — Purdue Palette

### Typography

Two fonts. Fixed.

**Titles:** Montserrat Bold (Purdue's brand typeface). Fallback: IBM Plex Sans Bold.
**Body / labels:** Source Sans Pro Regular. Fallback: DM Sans.

- Titles: 36–44pt, left-aligned, never centered
- Body: 20–24pt minimum on projected slides
- Captions / axis labels: 16–18pt (18pt floor for projection)
- Never use Inter, Arial, Calibri, Roboto, or Helvetica

### Color — Verified Contrast Ratios

All pairs below are WCAG 2.1 AA verified.

**On dark slides (black `#000000` background):**

| Element | Color | Hex | Ratio |
|---|---|---|---|
| Titles, key callouts | Purdue Old Gold | `#CFB991` | 11.0:1 ✅ |
| Body text, bullets | White | `#FFFFFF` | 21.0:1 ✅ |
| Subheadings (24pt+) | Aged Gold | `#8E6F3E` | 4.5:1 ✅ large only |
| Chart highlight / primary series | Purdue Old Gold | `#CFB991` | 11.0:1 ✅ |
| Secondary data series | White | `#FFFFFF` | 21.0:1 ✅ |

**On light slides (white `#FFFFFF` background — handouts only):**

| Element | Color | Hex | Ratio |
|---|---|---|---|
| Titles, body text | Black | `#000000` | 21.0:1 ✅ |
| Subheadings, primary series | Aged Gold | `#8E6F3E` | 4.7:1 ✅ |
| Captions, axis labels | Railway Gray | `#555960` | 7.0:1 ✅ |
| Chart secondary series | Black | `#000000` | 21.0:1 ✅ |

**Hard rules from contrast testing:**
- Purdue Gold (`#CFB991`) on white = 1.9:1 — **never use as text on white backgrounds**
- Railway Gray (`#555960`) on black = 3.0:1 — **never use as text on dark backgrounds**
- Aged Gold on black is borderline — **large text (24pt+) only**, never body text

### Layout

Left-anchor all text. Charts sit right or fill the lower half. No centered layouts.

Generous negative space. A sparse slide reads as confident. A cramped slide reads as unprepared.

**The memorable moment.** Every deck needs one slide that stops the room: a price series with one inflection circled in Purdue Gold and nothing else, a single question in large Montserrat Bold, or a stark comparison. Design this slide first — it sets the visual register for the rest of the deck.

---

## Slide Types

### Title / Section Separator
- Module name + a short provocative question or statement
- Example: "Module 2: Duration — The Risk Nobody Warned You About"

### Concept Explainer
- One definition, one plain-English sentence, one numeric example
- If you need more than 3 bullets: split it

### Real-World Anchor
- Follows concept introduction. Always
- Must include: real company/ticker, real date, real magnitude
- Example: "Duration in practice — TLT fell 31% in 2022 as 10Y yields rose from 1.5% to 4.2%"

### Intuition Challenge
- Scenario + question only. No answer on this slide
- Answer goes on the next slide (collapsed) or in speaker notes only

### Data / Chart Slide
- One chart per slide
- Label every axis. Always
- Include date range
- Highlight the relevant part (annotation, callout, contrasting color)
- Source in small text at the bottom

### Summary / Takeaway
- Max 3 points
- Written as full sentences, not topic labels
- Wrong: "Duration, Convexity, Yield Curve"
- Right: "Duration tells you how much a bond's price changes per 1% rate move. Longer duration means more price risk in a rising rate environment. The yield curve shows where this risk concentrates."

---

## Common Slide Failures

**The lecture-notes slide** — five bullets, each a paragraph. Cut to 8 words per bullet; put the rest in speaker notes.

**The sourceless stat** — "studies show that 70% of active managers underperform." Which study? When? On what benchmark? Source it or cut it.

**The orphaned formula** — a formula with no setup problem. Introduce the problem that requires the formula first, then present the formula as the solution.

**The decorative chart** — a chart that looks nice but doesn't directly support the slide's point. If you can't state in one sentence what the chart proves, remove it.

**The module jump without a bridge** — jumping from Module 1 to Module 2 without a one-sentence transition. Breaks the narrative thread.

---

## Build Order

Build every deck in this order — not front-to-back:

1. Write the session objective (what should students be able to do after?)
2. Find the real-world anchor(s)
3. Write the intuition challenge(s) — these define the target level of understanding
4. Build backward from the challenge: what must students understand to solve it?
5. Write the hook that sets up the need for those concepts
6. Build the content slides
7. Write speaker notes
8. Write the post-class handout last (distills what actually ended up in the deck)

Building front-to-back is how you end up with 40 content slides and no time for the intuition challenge.
