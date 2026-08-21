---
name: finance-educator
description: >
  Master teaching skill for finance educators. Use whenever preparing to teach a finance class, building a lecture slide deck, creating lesson plans, designing student activities, or explaining any financial concept to students at any level. Triggers on: "prepare my lecture", "build slides for class", "I'm teaching [topic] tomorrow", "explain [concept] to students", "create a session on [topic]", "make a deck for my class", "teaching materials for [topic]", or any request involving educational content for finance courses. Always invoke this skill for ANY teaching task — never build lecture content, slides, or lesson plans without it.
---

# Finance Educator

## Step 1 — Intake (Required Every Session)

Ask before building anything:

1. **Topic?** Be specific. "Bonds" and "duration risk in a rising rate environment" are different sessions.
2. **Specific angle or forward link?** (e.g., "connect to their DCF work last week" or "anchor to March 2023 SVB collapse")

Optional:
3. **Audience level?** Default: undergrad, Finance 101. State if different.
4. **Current market event to use?** If none given, pull a relevant historical anchor.

No topic = no output. Stop and ask.

---

## Teaching Philosophy

**Lead with the problem, not the framework.** Open every session with a scenario, market event, or question that makes students want the tool. Never open with a definition or formula.

**One real anchor per concept, minimum.** Use actual companies, real tickers, real dates, real magnitudes. "Rates rose sharply" is useless. "TLT fell 31% in 2022 as 10Y yields moved from 1.5% to 4.2%" is a lesson.

**Assume zero pre-reading.** Build every deck so someone who skipped the reading follows completely. Never shame, never reference what they "should know."

**Three concepts taught deeply beat six taught shallowly.** Prioritize ruthlessly. Excess content belongs in the handout, not the slides.

**The real goal is self-improving thinkers.** Every session needs at least one moment where students form and defend their own view on a real market situation. This is the bottleneck of the whole teaching process — if you skip it, the session produces memorization, not judgment.

---

## Session Architecture (60–90 min)

Treat each session as a repeatable process with defined stages and handoffs:

```
HOOK              [5–10 min]  Real market problem or event. No agenda slides. No housekeeping.
PREREQUISITE RECAP [5 min]   The critical 20% of pre-reading — tight, no shame.
MODULE 1          [15 min]   Concept → real-world anchor → check question
MODULE 2          [15 min]   Concept → real-world anchor → check question
BREAK             [10 min]   Hard stop. Non-negotiable.
MODULE 3          [15 min]   Concept OR synthesis of Modules 1+2
INTUITION CHALLENGE [10–15 min] Scenario debate, "what would you do?", or historical inquest
WRAP-UP           [5 min]    Three takeaways + forward bridge to next session
```

**Bottleneck:** the intuition challenge. This is where understanding either forms or doesn't. Protect this time at the expense of modules, never the other way.

**What breaks:**
- Skipping the break → attention crashes in Module 3
- Running long on prerequisites → Modules 1+2 get compressed; intuition challenge gets cut
- Skipping the intuition challenge → students leave with information, not judgment
- Padding content to fill time → cut a concept, don't dilute

---

## Slide Design

### Aesthetic Direction — Purdue Palette, Simplistic

All decks use the Purdue University brand color system. The aesthetic is minimal and data-forward: no gradients, no decorative elements, no competing colors. Every design decision serves clarity.

**Color system — fixed (contrast-verified against WCAG 2.1 AA):**

| Role | Color | Hex | Safe on | Contrast | Use |
|---|---|---|---|---|---|
| Background (dark) | Black | `#000000` | — | — | Preferred for projected delivery |
| Background (light) | White | `#FFFFFF` | — | — | Handout / print version |
| Purdue Old Gold | `#CFB991` | Black bg | 11.0:1 ✅ | Titles, callouts, key data, chart highlights — **dark slides only** |
| Aged Gold | `#8E6F3E` | White bg | 4.7:1 ✅ | Subheadings, secondary data on light slides; large text (24pt+) only on dark |
| Body text (on dark) | White | `#FFFFFF` | Black bg | 21.0:1 ✅ | All body text on dark slides |
| Body text (on light) | Black | `#000000` | White bg | 21.0:1 ✅ | All body text on light slides |
| Captions / labels | Railway Gray | `#555960` | White bg | 7.0:1 ✅ | Axis labels, source citations — white slides only |

**Critical constraints:**
- Purdue Gold (`#CFB991`) **cannot be used as text on white** — contrast 1.9:1 (fails). Use it only on black backgrounds or as a graphic/chart element color.
- Aged Gold (`#8E6F3E`) on black is borderline (4.49:1) — restrict to titles 24pt+ only, never body text.
- Railway Gray (`#555960`) on black — contrast 3.0:1 — fails body text; don't use as text on dark slides.

**Default layout:** Dark background (`#000000`) for projected slides. White background version generated alongside it for the student handout. Never mix backgrounds within the same deck.

**Typography — two fonts, fixed:**
- **Titles:** Montserrat Bold — Purdue's brand typeface, clean, strong at display size. If unavailable: IBM Plex Sans Bold.
- **Body / labels:** Source Sans Pro Regular — legible at small sizes, pairs cleanly with Montserrat. If unavailable: DM Sans.
- Title size: 36–44pt. Body: 20–24pt. Captions/labels: 16–18pt (18pt floor for projected slides).
- Titles left-aligned. Never centered. Body left-aligned or split-layout.

**Layout principles:**
- Left-anchor all text. Charts and visuals sit right or fill the lower half.
- Generous negative space — a slide that looks sparse reads as confident.
- Asymmetric preferred over centered. One strong element beats three weak ones.

**Memorable moment.** Every deck needs one slide that stops the room: a historical price chart with one inflection circled in gold and nothing else, a single question in large Montserrat Bold, or a stark comparison table. Design this slide first — it sets the visual register for the rest of the deck.

**What to avoid:** gradients, shadows, decorative borders, clip art, stock illustrations, colored backgrounds other than black or white, any font not listed above.

### Slide-Level Rules

- One idea per slide. If a slide makes two distinct points, split it.
- Slide titles state the takeaway, not the topic. "Duration Risk" → "Rising Rates Punish Long Bonds Most"
- Maximum 5 bullet points. Maximum 8 words per bullet. Everything else goes in speaker notes.
- Every chart: labeled axes, date range, source, annotated highlight on the relevant part
- Never describe a chart in bullets when you can just show the chart
- Slide must stand alone — a student reading it 6 months later with no context understands the point

### Chart Type Guidance

| Data you're showing | Chart type |
|---|---|
| Price/yield/rate over time | Line chart |
| Period-over-period comparison (quarterly, annual) | Bar chart |
| Risk vs. return, correlation | Scatter plot |
| Portfolio return attribution | Waterfall chart |
| Multiple asset classes across time | Small multiple line charts |
| Single dramatic number | Large type, no chart needed |

### Accessibility Standards (WCAG 2.1 AA applied to slides)

These are not optional — a stand-alone deck that students can't read or navigate fails its purpose.

**Contrast ratios:**
- Body text on backgrounds: minimum 4.5:1 ratio
- Display/title text (24pt+): minimum 3:1 ratio
- Chart lines, data markers, icon-only indicators: minimum 3:1 against their background

**Color independence:** Never use color as the only way to convey information. In charts, add direct labels, dashed vs. solid line styles, or distinct marker shapes alongside color. A student who is red-green colorblind must read your chart without confusion.

**Safe chart data series pairs within the Purdue palette:**
- On dark slides: Purdue Gold (`#CFB991`) and White (`#FFFFFF`) — 11.0:1 and 21.0:1 respectively
- On light slides: Aged Gold (`#8E6F3E`) and Black (`#000000`) — 4.7:1 and 21.0:1 respectively
- For three-series charts: add Railway Gray (`#555960`) on white only (7.0:1)
- Never use red vs. green as the sole differentiator; add labels or line styles alongside color

**Alt text:** Every chart, image, and diagram in the .pptx gets alt text. The pptx skill adds this — specify the description when prompting. Format: "[chart type] showing [what it shows], [key finding]." Example: "Line chart showing TLT ETF price from Jan 2021 to Dec 2022, falling 31% as 10Y yields rose from 1.5% to 4.2%."

**Font size floor:** 18pt minimum on any projected slide. Speaker notes can go smaller.

**Reading order:** Slides must have a logical reading order (title → content → callouts). The pptx skill handles this — don't override it by placing text boxes out of sequence.

**Zoom test:** The deck must be legible at 150% zoom without layout breaking. Key charts should not require zooming to read axis labels.

---

## Intuition Development Framework

The intuition challenge is not a quiz. It's a structured moment of judgment formation. Run it the same way every session so students learn the rhythm:

1. **Setup (1 min):** Present the scenario. Give all the facts needed. Remove ambiguity about what you're asking.
2. **Think time (2–3 min):** Silence. Don't fill it.
3. **Collect views (2 min):** 3–4 different answers on the board. No judgment yet.
4. **Debrief (3–5 min):** Validate the correct reasoning in wrong answers. Identify the flaw in the
   incorrect ones. Who was right is secondary to why. Never cut the debrief to stay on schedule: the
   debrief is where the learning happens.
5. **Bridge (1 min):** Connect the judgment they just formed to the next session's topic.

Prompt bank, difficulty ladder, and run notes: `references/intuition-prompts.md`.

---

## Reference Files

Load only what the session needs.

- `references/investments.md` — topic anchors, real market events with dates and magnitudes, and the
  concept-to-anchor map. Load when choosing the hook or an anchor for any module.
- `references/intuition-prompts.md` — the prompt library and how to run one. Load before building the
  intuition challenge.
- `references/slide-design.md` — the visual-first rule, chart selection, slide density limits. Load
  before building any deck.
- `references/ai-structural-change.md` — a complete 75-minute session on how AI reshapes capital
  markets, built on the CFA Institute structural-forces framework. Load when teaching AI and markets,
  market structure, or when a session needs to stress-test EMH and MPT against a live scenario.

---

## Live Data Mandate

Every figure in any teaching material is pulled live and dated, never quoted from memory. This applies
with full force to teaching material: a wrong number in a lecture propagates into student work and is
repeated back for years. Anything that cannot be sourced is either cut or labeled an estimate on the
slide itself.

---

## Deliverable Routing

| Deliverable | Route |
|---|---|
| Slide deck | `pptx`, with this skill's slide-design rules and the academic typography carve-out in `purdue-smif-brand-guidelines` |
| Handout, problem set, case | `docx` |
| Reading memo or one-pager | markdown |
| Any spreadsheet exercise | `xlsx` |

Excess content belongs in the handout, never on the slides.

---

## Editorial Gate

Every prose deliverable this skill produces routes through the `write` skill before it ships.
Teaching material is not exempt from the de-slop contract; students read more carefully than
colleagues do, and slop in a lecture gets copied into their work.

| Stage | Route |
|---|---|
| Drafting lecture notes, handouts, problem sets, case walkthroughs, slide copy | `write` DRAFT, teaching materials form, loading `domain-notes.md` |
| Before any file is built | `write` GATE v1, quick tier |
| After the pptx or docx is built | `write` GATE v1 on the text extracted from the finished file. Slide titles, chart labels, table captions, and section headers are written during the build and are the most reliable place slop survives |
| Reviewing student work | `write` COACH, never CRITIQUE. COACH withholds the rewrite so the student does the revision, which is the point of assigning it |
| Cutting a session or handout to fit a time or page limit | `write` COMPRESS, with the target stated as a number |

Register for teaching material is naturalness dial 3. The gate runs the pattern scan and skips
the soul check on any slide carrying financial data, which stays neutral.

The academic typography carve-out in `purdue-smif-brand-guidelines` still governs visual design.
The editorial gate governs the words.
