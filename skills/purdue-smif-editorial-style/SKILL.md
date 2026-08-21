---
name: purdue-smif-editorial-style
description: Apply Purdue Student Managed Investment Fund (SMIF) editorial style — capitalization, number formatting, financial metrics, abbreviations, hyphenation, period terminology, and voice — to all copy in downloadable deliverables. Use whenever generating or editing any .docx, .pptx, .xlsx, .html, .pdf, .md, or other file the user can download or save, regardless of topic or whether SMIF is named. Triggers include investment memos, pitch decks, portfolio commentary, semester and annual reports, committee materials, research briefs, dashboards, and internal communications. Sister skill to purdue-smif-brand-guidelines (which covers visual brand). Honor opt-outs only when the user is explicit ("ignore style guide," "unedited," "raw text").
---

# Purdue SMIF Editorial Style

**Standing rule.** Apply to all copy in any downloadable deliverable (.docx, .pptx, .xlsx, .html, .pdf, .md, and similar), regardless of topic or whether SMIF is named. Sister skill to `purdue-smif-brand-guidelines`, which handles visuals. This skill governs wording, grammar, and formatting of numbers, metrics, and financial terminology.

**[Formal] tag.** Rules marked [Formal] apply to external/institutional deliverables (Annual Report, externally distributed Semester Report, presentations to faculty or institutional audiences). Base rules apply everywhere else. When in doubt, apply base rules.

---

## GUARDRAILS — read first, apply always

**Never fabricate financial data.** Do not invent figures, returns, valuations, portfolio weights, or benchmark values. If a number is unknown, write `[TBD]` or ask.

**Never invent securities.** Do not fabricate ticker symbols, company names, benchmark names, CUSIP numbers, or fund identifiers. Use only what the user provides.

**Never present forward-looking statements as fact.** All projections, targets, and estimates must be preceded by hedging language: "we expect," "our thesis assumes," "as of [date], our model projects." See Voice section.

**Do not apply style rules to verbatim quoted material.** If reproducing an exact quote, preserve its original wording, capitalization, and punctuation. Flag the quote clearly.

**Disclosure placeholders must be resolved.** The disclosure block contains `[date]`. Do not publish a deliverable with an unfilled placeholder — confirm the date with the user or fill it from context.

**Style vs. user conflict.** When a user instruction conflicts with this guide (e.g., they want "FY2025" or "$2.5M"), apply the style rule and note the substitution. Do not silently override.

**Scope carve-out.** Do not apply editorial style rules to raw code, API output, terminal text, or data-only exports. Style governs human-readable copy only.

---

## Writing quality: de-slop gate integration

Run both passes before finalizing any body-copy deliverable. Neither pass applies to financial data tables, legal disclosures, or verbatim quoted material.

### Quick tier (GATE v1, from `write`)

Run the five passes in order: banned phrases → structural patterns → false agency → rhythm traps → soul check.

**Finance-specific banned phrases for SMIF copy** (extend the de-slop phrase list in `write`):

| Cut this | Replace with |
|---|---|
| robust portfolio | well-constructed portfolio, or describe specifically |
| dynamic market conditions | name the actual conditions |
| headwinds and tailwinds | name the specific factors |
| navigate volatility / navigate uncertainty | handle, manage, or be specific |
| unlock value | describe the mechanism |
| positioned for growth | describe what the thesis actually is |
| it is worth noting | state the point directly |
| at its core | cut; open with the substance |
| going forward | next, over the coming semester |
| in terms of | rewrite the sentence |
| the market is pricing in | name the specific expectation |
| consensus expects | cite the actual consensus source |

**Structural patterns to eliminate:**
- Binary negations: "Not because X. Because Y." → "Because Y."
- Dramatic fragmentation: "Risk. That's the word that defines this semester." → one direct sentence.
- Rule of three for its own sake: if three items don't each add value, cut to two or one.
- Em dash overuse: maximum one em dash per paragraph. Use commas or periods instead.

### Deep tier (GATE v1, 24-pattern catalog, from `write`)

Check the 24 patterns. Key ones for financial writing:

| Pattern | SMIF manifestation | Fix |
|---|---|---|
| Significance inflation | "testament to," "pivotal," "landmark," "indelible" | Specific fact or cut |
| Vague attributions (pattern 5) | "analysts believe," "the market expects" | Cite source or delete |
| Formulaic challenges (pattern 6) | "Despite challenges, the Portfolio continues to..." | Replace with what actually happened |
| AI vocabulary (pattern 7) | "delve," "garner," "interplay," "tapestry," "underscore" | Simpler word or restructure |
| Generic conclusions (pattern 24) | "The outlook remains constructive." | Name what specifically supports or threatens the thesis |
| Excessive hedging (pattern 23) | "could potentially possibly suggest" | One qualifier maximum |

**Register rule:** financial data, legal disclosures, compliance language, and verbatim quoted material are exempt from both passes. Preserve their wording exactly.

**Soul check:** after removing patterns, verify the text reacts to data rather than just reporting it. Vary sentence length. If every sentence is the same length, the writing is still AI-sounding even if technically clean.

---

## The Compound-Modifier Rule

Hyphenate two-word modifiers immediately before the noun they modify. Leave them open elsewhere.

| Term | Before a noun | Elsewhere |
|---|---|---|
| long term | long-term holding period | held for the long term |
| short term | short-term volatility | recover in the short term |
| near term | near-term catalyst | in the near term |
| year over year | year-over-year revenue growth | revenue grew year over year |
| quarter over quarter | quarter-over-quarter EPS change | EPS declined quarter over quarter |
| market cap | market-cap weighted index | weighted by market cap |
| large / mid / small cap | large-cap equities, small-cap exposure | the stock is large cap |
| investment grade | investment-grade bonds | the bonds are investment grade |
| high yield | high-yield debt | the bonds trade at high yield |
| risk adjusted | risk-adjusted return | the return, adjusted for risk |

**Always hyphenated regardless of position:** buy-and-hold · mark-to-market · price-to-earnings · price-to-book · price-to-sales · free-cash-flow (adjective) · sell-side · buy-side · bottom-up · top-down · year-to-date (when written out; abbreviate as YTD in tables).

---

## Numbers

- **Digits for all cardinals** — "3 positions," not "three positions." Includes one through nine.
- **Ordinals 1st–9th: superscript** — "1ˢᵗ quartile," "3ʳᵈ quarter." Tenth and above: plain — "10th," "25th."
- **Million / Billion: spell out, capitalize** — "$2.5 Million," "$1.3 Billion." Never M, MM, B, Bn.
- **Thousand: never abbreviate** — "$400,000," not "$400K." Commas as separators: "1,250,000."
- **Decimal precision** — EPS/beta: 2 places. P/E: 1 place acceptable. Percentages: 1–2 places. Never mix precision within a table column.

---

## Currency

- Body copy: "$2.5 Million," "$1.3 Billion," "$400,000."
- Tables/charts: same, unless the column header already specifies units (a "$ Millions" column may show "2.5").
- One form per deliverable — never mix "$2.5 Million" and "$2,500,000" in the same document.
- Use "$" for U.S. dollar. Spell out "U.S. dollar" on first mention in international-context documents.

---

## Percent and Basis Points

- **Percent** — use "%" in body copy, tables, and charts. **[Formal]** spell out "percent" in body copy; "%" stays acceptable in tables and charts.
- **Basis points** — spell out in body copy on first use; "bps" acceptable in tables/charts where column context is unambiguous. Never "bp" (singular).
- **Percentage points vs. basis points** — use "percentage points" for whole-number differences in allocations or weights. Use "basis points" for yield, spread, and rate precision.

---

## Dates and Reporting Periods

SMIF runs on a semester calendar. Apply these conventions everywhere.

### Semester Labels

| Format | Use for |
|---|---|
| `Fall 20XX` | Body copy, slide titles, report covers — spell out in full |
| `Spring 20XX` | Same |
| `F20XX` | Tight chart/table cells only — capital F + four-digit year, no apostrophe, no space |
| `S20XX` | Same for Spring |
| `AY20XX–XX` | Academic year — capital AY + four-digit start year + en dash + two-digit end year (e.g., AY2025–26) |

Never: `F'XX`, `FA2X`, `SP2X`, `fall 20XX` (lowercase), `Fall 'XX`.

### Quarter Labels (equity/fixed-income sub-reports)

- Format: `Q1XX`, `Q2XX`, `Q3XX`, `Q4XX` — quarter number + two-digit year, no apostrophe, no space.
- Never: `Q1'XX`, `Q1 XX`, `Q1-XX`.

### Full Dates

- Body copy: spell out the month — "September 30, 20XX." **[Formal]** always spell out; never abbreviate months in body copy.
- Charts/tables: "9/30/XX" or "Sep. 30, 20XX."
- Never use ordinals: "December 31," not "December 31st."

### Year References

- Calendar year: `CY20XX`.
- Academic year: `AY20XX–XX`.
- **Never `FY` for SMIF** — the fund has no separate fiscal year.

---

## Abbreviations

### Always Spell Out in Body Copy

| Wrong | Right |
|---|---|
| M, MM, million | Million |
| B, Bn, billion | Billion |
| K, k | full figure, e.g., "$400,000" |
| bp (singular) | basis point |
| YOY, YoY | year over year |
| QoQ | quarter over quarter |

### Require First-Use Definition, Then Abbreviate

| Full form | Abbreviation |
|---|---|
| enterprise value | EV |
| free cash flow | FCF |
| weighted average cost of capital | WACC |
| discounted cash flow | DCF |
| compound annual growth rate | CAGR |
| return on equity | ROE |
| return on assets | ROA |
| return on invested capital | ROIC |
| earnings before interest and taxes | EBIT |
| earnings before interest, taxes, depreciation, and amortization | EBITDA |

### Acceptable Without Definition

| Full form | Abbreviation | Notes |
|---|---|---|
| earnings per share | EPS | Industry standard |
| price-to-earnings | P/E | Slash, no spaces |
| price-to-book | P/B | Same |
| price-to-sales | P/S | Same |
| basis points | bps | Tables/charts only |
| year-to-date | YTD | |
| total return | TR | Tables/charts only |
| United States | U.S. | With periods |
| investment grade | IG | Tables/charts only |
| high yield | HY | Tables/charts only |

### Never Abbreviate

- Purdue Student Managed Investment Fund → "the Fund" or "SMIF" after first full use (not "PSM," "PSMIF," or any other form)
- the investment committee → do not abbreviate to "IC" in formal copy

---

## Capitalization

### SMIF-Specific Terms

| Lowercase (generic) | Capitalized (SMIF-specific) |
|---|---|
| the fund | the Fund |
| the portfolio | the Portfolio |
| the committee | the Committee (Investment Committee) |
| the team | the Team — e.g., Equities Team, Fixed Income Team |
| the benchmark | the Benchmark (the Fund's designated benchmark) |
| department | Department — e.g., Research Department |
| semester report | Semester Report (the Fund's official report) |
| annual report | Annual Report (the Fund's official report) |

### Additional Rules

- **Investment grade** — hyphenate as modifier only: "investment-grade bonds" but "the bonds are investment grade."
- **Large cap / mid cap / small cap** — two words; hyphenate before a noun only. Never "LargeCap," "midcap."
- **GICS sector names** — always capitalized: Information Technology, Health Care, Consumer Discretionary, Consumer Staples, Financials, Industrials, Energy, Materials, Real Estate, Communication Services, Utilities.
- **Benchmark names** — full official name on first reference: "S&P 500 Index," "Bloomberg U.S. Aggregate Bond Index." Abbreviate thereafter: "the S&P 500," "the Bloomberg Agg."

---

## Financial Metric Formatting

- **Multiples** — use × suffix: "18.2×," not "18.2x" or "18.2 times." Body copy may spell out: "trading at 18 times forward earnings."
- **Returns and yield** — always "%" — "the Portfolio returned 8.3% in Fall 20XX."
- **Alpha / beta** — lowercase always, unless opening a sentence.
- **Named ratios** — capitalize the proper name: Sharpe ratio, Sortino ratio, Treynor ratio.
- **Ranges** — en dash, no spaces: "2020–2024," "Q1–Q3," "Fall 20XX–Spring 20XX." Hyphen acceptable in tight chart cells.
- **Negative numbers** — true minus sign (−) in typeset documents; hyphen (-) acceptable in Office.

---

## SMIF Terminology Quick-Correct

| Wrong | Right |
|---|---|
| student fund / student-managed fund (first use) | Purdue Student Managed Investment Fund; then "the Fund" or "SMIF" |
| investment grade (modifier) | investment-grade |
| large cap / largecap / Large Cap (modifier) | large-cap |
| small cap / smallcap (modifier) | small-cap |
| mid cap / midcap (modifier) | mid-cap |
| high yield (modifier) | high-yield |
| buy side / buyside | buy-side |
| sell side / sellside | sell-side |
| top down / topdown | top-down |
| bottom up / bottomup | bottom-up |
| mark to market (modifier) | mark-to-market |
| free cash flow (modifier) | free-cash-flow |
| price to earnings / pricetoearnings | price-to-earnings (modifier); P/E after first use |
| year to date (modifier) | year-to-date; YTD in tables |
| Fall 'XX / fall 20XX | Fall 20XX |
| Q1'XX / Q1 XX | Q1XX |
| FY20XX | CY20XX or AY20XX–XX |
| robust portfolio | describe specifically |
| dynamic market conditions | name the conditions |
| headwinds and tailwinds | name the specific factors |

---

## Voice and Verb Forms

- **"forecast," not "forecasted"** — past tense is "forecast." Same pattern as "broadcast."
- **"return," not "returned a return"** — "the Portfolio returned 8.3%," not "produced a return of 8.3%."
- **Active voice** — "the Committee approved the position," not "the position was approved."
- **Forward-looking language** — precede all projections with hedging: "we expect," "our thesis assumes," "as of [date]." Never state estimates as fact.
- **Attribution** — "our analysis indicates," "our DCF model suggests," "based on our estimate." Do not write as though analysis is objective market fact.

---

## Punctuation

- **Oxford comma:** yes — "equities, fixed income, and cash."
- **Number ranges:** en dash, no spaces — "2020–2024," "Q1–Q3," "Fall 20XX–Spring 20XX."
- **Possessive:** "SMIF's Portfolio," "the Fund's holdings."
- **Ratio notation:** slash, no spaces — "P/E," "P/B," "EV/EBITDA."
- **Tickers:** all caps, no periods — AAPL, MSFT, AMZN.
- **Footnotes:** superscript numerals. Disclosure text: Calibri Regular 8pt Purdue Gray, bottom of each slide or page.

---

## Disclaimers and Disclosures

**Resolve the `[date]` placeholder before publishing.** Do not deliver a document with an unfilled date field.

**External deliverables** (presentations or reports distributed outside SMIF) — include verbatim in footer or final slide:

> *This material is prepared by students of the Purdue Student Managed Investment Fund for educational purposes. It does not constitute investment advice. Past performance is not indicative of future results. All data as of [date].*

**Internal deliverables** (IC memos, research briefs) — include on the cover page:

> *Confidential — For Internal Distribution Only. Purdue Student Managed Investment Fund.*

**[Formal]** Annual Report and any externally distributed Semester Report: place the full external disclosure on both the cover and the final page.

---

## Quick Reference (Alphabetical)

| Term | Rule |
|---|---|
| academic year | AY20XX–XX (e.g., AY2025–26) |
| alpha / beta | lowercase |
| Annual Report | capitalized when = SMIF's official report |
| basis points | spell out in body; bps in tables/charts only |
| Benchmark | capitalized when = SMIF's designated benchmark |
| Billion | spell out, capital B |
| Bloomberg Agg | acceptable after first full use |
| bottom-up | always hyphenated |
| buy-side | always hyphenated |
| CAGR | define on first use |
| Committee | capitalized when = SMIF Investment Committee |
| DCF | define on first use |
| dynamic market conditions | banned — name the conditions |
| EPS | no definition required |
| EV | define on first use |
| F20XX | chart/table cells only (Fall) |
| FCF | define on first use |
| forecast | not "forecasted" |
| free-cash-flow | hyphenated as modifier; "free cash flow" as noun |
| Fund | capitalized when = SMIF |
| headwinds / tailwinds | banned — name the factors |
| high-yield | hyphenated as modifier; "high yield" as noun |
| investment-grade | hyphenated as modifier; "investment grade" as noun |
| large-cap | hyphenated as modifier; "large cap" as noun |
| mark-to-market | hyphenated as modifier; "mark to market" as verb |
| mid-cap | hyphenated as modifier; "mid cap" as noun |
| Million | spell out, capital M |
| P/E | slash, no spaces; no definition required |
| percentage points | use for whole-number allocation changes |
| Portfolio | capitalized when = SMIF's Portfolio |
| price-to-earnings | hyphenated as modifier |
| Q1XX | no apostrophe or space |
| risk-adjusted | hyphenated as modifier |
| robust portfolio | banned — describe specifically |
| S&P 500 Index | full name first use; "the S&P 500" thereafter |
| S20XX | chart/table cells only (Spring) |
| sell-side | always hyphenated |
| Semester Report | capitalized when = SMIF's official report |
| Sharpe ratio | capital S, lowercase r |
| small-cap | hyphenated as modifier; "small cap" as noun |
| Team | capitalized when = a SMIF team |
| Thousand | never abbreviate — write the full figure |
| tickers | ALL CAPS, no periods (AAPL, MSFT) |
| top-down | always hyphenated |
| U.S. | with periods |
| WACC | define on first use |
| year over year | spell out; hyphenate only before a noun |
| year-to-date / YTD | hyphenate as modifier; YTD in tables |
| × (times) | suffix for multiples — "18.2×" |

---

## The artifact rule

Applying these rules to a draft does not apply them to the built file. Headings, table captions,
exhibit and chart titles, axis labels, footnotes, slide titles, and summary boxes are written
during the build and are the single most reliable place slop and style violations survive.

After the `.docx`, `.pptx`, `.xlsx`, or `.html` is built, extract its text and run this skill's
rules plus `write` GATE v1 against the extracted text. Only then is the deliverable compliant.
If text extraction cannot be run, say so and list the build-time elements as unchecked.

Body prose already cleared and untouched since is not re-checked. Check what changed and what
the build wrote.
