---
name: equity-risk-report
description: >
  Generates a comprehensive, single-file HTML5 dark-mode equity risk report for any publicly
  traded stock ticker. Use this skill whenever the user asks to analyze a stock, research a
  company's financials, build a risk dashboard, generate an equity report, assess investment
  risk for a ticker, or requests any combination of financial analysis + HTML output. Trigger
  even for casual phrasings like "run a report on AAPL", "what does MSFT look like financially",
  "build me a risk card for NVDA", or "analyze Tesla for me". The skill always performs live
  web research before writing any HTML — it never uses stale training data for financial figures.
  Always use this skill when a ticker symbol appears alongside any request for analysis, scoring,
  a dashboard, a report, or financial data visualization.
---

# Equity Risk Report Skill

Produces a two-page, single-file HTML5 dark-mode equity risk report. The output includes
a scored risk gauge, KPI strip, price trend chart, pillar breakdowns, quarterly trend table,
earnings recap, and a risk/catalyst matrix. All data is sourced live from web searches before
any HTML is written.

---

## Input

The user provides a ticker symbol, referred to below as `{{TICKER}}`.

---

## Execution Protocol

Execute in two strict sequential phases. Do not begin Phase 2 until Phase 1 is complete.

---

## Phase 1: Data Collection and Scoring

Open a `<scratchpad>` block. Complete every step inside it before writing any HTML.

### Step 0: Input Validation

Confirm `{{TICKER}}` is a valid, currently traded equity. If it appears invalid, delisted,
or unrecognizable after a quick search, output exactly:
> "Ticker `{{TICKER}}` could not be validated. Please provide a valid US-listed equity ticker."
Then stop. Do not proceed to HTML generation.

---

### Step 1: Market Data Collection

Search all three sources in priority order. Record each field with its source URL.

**Priority 1:** SEC EDGAR — search `{{TICKER}} 10-K 10-Q site:sec.gov`
**Priority 2:** Yahoo Finance — `{{TICKER}} yahoo finance statistics`
**Priority 3:** Macrotrends — `{{TICKER}} macrotrends revenue margins`

**Required fields (mark "DATA UNAVAILABLE" if not found after all three sources):**

| Field | Notes |
|---|---|
| Company full name | |
| Current price | Include date |
| Daily change ($) | |
| Daily change (%) | |
| 52-week high | |
| 52-week low | |
| Market cap | |
| P/E ratio (TTM) | If negative due to net loss, record as "Negative (unprofitable)" |
| EV/EBITDA | |
| Free Cash Flow TTM | In millions |
| Debt-to-Equity ratio | |
| Current ratio | |
| YoY Revenue growth (%) | Most recent full fiscal year vs. prior year |
| YoY Net Income growth (%) | Same period |
| Operating margin | Most recent quarter + prior year same quarter |
| Revenue — last 4 quarters | Label with fiscal period (e.g., Q1 FY2025) |
| Net Income — last 4 quarters | Same labeling |
| Operating Margin — last 4 quarters | Same labeling |

Do not estimate or interpolate any field. If a field cannot be confirmed, write "DATA UNAVAILABLE".

---

### Step 2: Sector Baseline (Required)

Search: `"{{TICKER}} sector average P/E EV/EBITDA [current year]"`

Record:
- Sector name
- Sector median P/E
- Sector median EV/EBITDA
- Source URL

**Fallback defaults** (use only if search returns nothing; label them as defaults):

| Sector | Median P/E | Median EV/EBITDA |
|---|---|---|
| Technology | 28x | 20x |
| Healthcare | 22x | 14x |
| Consumer Discretionary | 19x | 12x |
| Consumer Staples | 21x | 13x |
| Financials | 12x | 9x |
| Energy | 14x | 8x |
| Industrials | 18x | 11x |
| Utilities | 17x | 10x |
| Real Estate | 30x | 18x |
| Materials | 16x | 10x |

---

### Step 3: Recent News (Required for Risk/Catalyst Section)

Search: `"{{TICKER}} earnings news risks catalysts [current month and year]"`

Record 3–5 specific, dated findings with source. Each finding must be concrete (not generic).
If no news exists within 60 days, use the most recent available and note the date.

---

### Step 4: Earnings Summary

Search: `"{{TICKER}} latest earnings call transcript OR earnings release [current year]"`

Record the 3 most specific factual highlights: guidance revisions, beat/miss magnitude,
key management commentary. If no transcript is available, search for the most recent 8-K.
Record the source and date.

---

### Step 5: Scoring Rubric

Score each pillar 0–100 (100 = safest/lowest risk). Show all arithmetic explicitly.

#### Valuation Pillar (weight: 35%)

Sub-criterion A — P/E vs. Sector Median (50% of pillar weight):

| Condition | Score range |
|---|---|
| P/E is negative (unprofitable) | 20 |
| P/E > 2× sector median | 10–30 |
| P/E 1.5×–2× sector median | 30–50 |
| P/E 1×–1.5× sector median | 50–70 |
| P/E at or below sector median | 70–90 |
| DATA UNAVAILABLE | 50 (note it) |

Sub-criterion B — EV/EBITDA vs. Sector Median (50% of pillar weight):
Same scale as Sub-criterion A.

**Pillar score = (Sub-A × 0.50) + (Sub-B × 0.50)**

---

#### Financial Health Pillar (weight: 35%)

Sub-criterion A — Debt-to-Equity (40% of pillar):

| D/E | Score |
|---|---|
| < 0.3 | 85–100 |
| 0.3–0.8 | 65–84 |
| 0.8–1.5 | 40–64 |
| > 1.5 | 0–39 |
| DATA UNAVAILABLE | 50 (note it) |

Sub-criterion B — Current Ratio (30% of pillar):

| Current Ratio | Score |
|---|---|
| > 2.0 | 85–100 |
| 1.5–2.0 | 65–84 |
| 1.0–1.5 | 40–64 |
| < 1.0 | 0–39 |
| DATA UNAVAILABLE | 50 (note it) |

Sub-criterion C — Free Cash Flow (30% of pillar):

| FCF Status | Score |
|---|---|
| Positive and growing YoY | 75–100 |
| Positive and flat | 50–74 |
| Negative but improving YoY | 25–49 |
| Negative and worsening | 0–24 |
| DATA UNAVAILABLE | 50 (note it) |

**Pillar score = (A × 0.40) + (B × 0.30) + (C × 0.30)**

---

#### Growth Pillar (weight: 30%)

Sub-criterion A — YoY Revenue Growth (60% of pillar):

| Rev Growth | Score |
|---|---|
| > 20% | 85–100 |
| 10–20% | 65–84 |
| 0–10% | 40–64 |
| Negative | 0–39 |
| DATA UNAVAILABLE | 50 (note it) |

Sub-criterion B — YoY Net Income Growth (40% of pillar):

| NI Growth | Score |
|---|---|
| > 20% | 85–100 |
| 0–20% | 50–84 |
| Negative from profitable base | 20–49 |
| Negative from loss base (deeper loss) | 0–19 |
| DATA UNAVAILABLE | 50 (note it) |

**Pillar score = (A × 0.60) + (B × 0.40)**

---

### Step 6: Final Score Calculation

Write out explicitly:

```
Valuation Pillar Score  = ___
Health Pillar Score     = ___
Growth Pillar Score     = ___

Overall Score = (Valuation × 0.35) + (Health × 0.35) + (Growth × 0.30) = ___
```

Assign risk label and color:

| Score | Label | Hex color |
|---|---|---|
| 0–39 | HIGH RISK | `#EF4444` |
| 40–69 | MODERATE RISK | `#F59E0B` |
| 70–100 | LOWER RISK | `#22C55E` |

Close `</scratchpad>` only after all six steps are fully completed.

---

## Phase 2: HTML Output

After closing `</scratchpad>`, output raw HTML only.

**Hard rules for output format:**
- No markdown code fences around the HTML
- No introductory text before `<!DOCTYPE html>`
- No trailing text, explanation, or commentary after `</html>`
- Every number in the HTML must originate from the scratchpad — no new values introduced in Phase 2

---

### Technical Specification

```html
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{TICKER}} Risk Report</title>
  <style>/* All CSS inline. No external stylesheet, no CDN — see Guardrail 3. */</style>
</head>
<body class="bg-gray-950 text-gray-100 min-h-screen font-sans antialiased">
  <main class="max-w-6xl mx-auto px-4 py-10 space-y-16">
    <!-- PAGE 1 -->
    <!-- PAGE 2 -->
  </main>
</body>
</html>
```

**No external requests of any kind.** The Tailwind Play CDN and jsDelivr were previously specified
here; both are blocked by the artifact CSP and by restricted networks, and the Play CDN is not
production-grade in any case. Write the CSS inline — the class names used throughout this spec are
a naming convention for that stylesheet, not a Tailwind dependency. The report must render fully
with the network off.

---

### Page 1: Executive Dashboard

**Header block:**
- Company full name: `text-3xl font-bold text-gray-100`
- Ticker badge: `bg-gray-800 text-green-400 font-mono text-sm px-2 py-0.5 rounded inline-block`
- Current price: `text-4xl font-bold`
- Daily change pill: green (`bg-green-900/50 text-green-400`) if positive, red (`bg-red-900/50 text-red-400`) if negative. Format: `+$X.XX (+X.XX%)`
- 52-week range: render as a visual bar
  ```html
  <div class="relative h-2 bg-gray-800 rounded-full w-full">
    <div class="absolute top-0 h-2 w-1 bg-blue-400 rounded-full" style="left: {{POSITION_PCT}}%"></div>
  </div>
  ```
  Where `POSITION_PCT = ((currentPrice - 52wLow) / (52wHigh - 52wLow)) * 100`

**Score Gauge (SVG arc):**

```html
<svg viewBox="0 0 200 120" class="w-64 mx-auto">
  <!-- Background arc -->
  <path d="M 20 100 A 80 80 0 0 1 180 100"
        fill="none" stroke="#1f2937" stroke-width="16" stroke-linecap="round"/>
  <!-- Score arc — set stroke-dasharray to arc length (~251), dashoffset = 251 * (1 - score/100) -->
  <path d="M 20 100 A 80 80 0 0 1 180 100"
        fill="none" stroke="{{SCORE_COLOR}}" stroke-width="16" stroke-linecap="round"
        stroke-dasharray="251" stroke-dashoffset="{{DASHOFFSET}}"/>
  <!-- Score number -->
  <text x="100" y="85" text-anchor="middle" font-size="32" font-weight="bold"
        fill="{{SCORE_COLOR}}">{{OVERALL_SCORE}}</text>
  <!-- Risk label -->
  <text x="100" y="108" text-anchor="middle" font-size="11"
        fill="#9ca3af">{{RISK_LABEL}}</text>
</svg>
```

Where `DASHOFFSET = 251 * (1 - overallScore / 100)`.

**KPI Strip** (`grid grid-cols-2 md:grid-cols-4 gap-4`):

4 cards: P/E Ratio, Debt-to-Equity, Free Cash Flow (TTM), Operating Margin

Each card:
```html
<div class="bg-gray-900 rounded-xl p-4 border border-gray-800">
  <p class="text-xs text-gray-400 uppercase tracking-wide mb-1">{{LABEL}}</p>
  <p class="text-2xl font-bold text-gray-100">{{VALUE}}</p>
</div>
```

**Price Chart:**
```html
<div class="bg-gray-900 rounded-2xl p-6 border border-gray-800">
  <h2 class="text-lg font-semibold text-gray-100 mb-4">12-Month Price Trend</h2>
  <canvas id="priceChart" style="width:100%;height:320px;"></canvas>
</div>
```

**Never synthesise the price series.** An interpolated or noise-generated line is a fabricated
figure wearing a chart's clothes, and it is barred by this skill's own no-fabrication rule, by
`equity-research-foundation` Phase 0, and by `smif-initiation-pipeline` Compliance 3. It also has
no valid `decision-provenance` tag, because there is no source to name.

Add a Step 1b to Phase 1: pull 12 real monthly closes (SEC EDGAR, Yahoo Finance, or Macrotrends —
same priority order as Step 1) and record each with its date and source. Then draw them as an
inline `<svg>` polyline sized to the data — no charting library, no CDN, no build step:

```html
<!-- 12 monthly closes, {{FIRST_DATE}} – {{LAST_DATE}}, source: {{SOURCE}} -->
<svg viewBox="0 0 600 200" class="w-full h-52" role="img"
     aria-label="12-month closing price, {{LOW}} to {{HIGH}}">
  <polyline fill="none" stroke="#22c55e" stroke-width="2"
            points="{{X,Y PAIRS SCALED FROM THE REAL CLOSES}}"/>
</svg>
<p class="text-xs text-gray-500 mt-2">Monthly closes · {{SOURCE}} · as of {{DATE}}</p>
```

If 12 real closes cannot be sourced, **omit the chart** and render the 52-week range bar alone.
A missing chart is a correct report; an invented one is not.

---

### HR Separator

```html
<hr class="border-gray-800 my-12">
```

---

### Page 2: Deep Dive Assessment

**Pillar Breakdown** (3 cards, one per pillar: Valuation, Financial Health, Growth):

Each pillar card structure:
```html
<div class="bg-gray-900 rounded-2xl p-6 border border-gray-800 space-y-4">
  <!-- Header row -->
  <div class="flex items-center justify-between">
    <h3 class="text-lg font-semibold text-gray-100">{{PILLAR_NAME}}</h3>
    <span class="text-sm font-bold px-3 py-1 rounded-full"
          style="background:{{SCORE_COLOR}}20; color:{{SCORE_COLOR}}">
      {{SUB_SCORE}} / 100
    </span>
  </div>
  <!-- Progress bar -->
  <div class="h-2 bg-gray-800 rounded-full">
    <div class="h-2 rounded-full transition-all"
         style="width:{{SUB_SCORE}}%; background:{{SCORE_COLOR}}"></div>
  </div>
  <!-- Explainer paragraph (2–4 sentences from scratchpad data) -->
  <p class="text-sm text-gray-300 leading-relaxed">{{EXPLAINER}}</p>
  <!-- Beginner Take -->
  <aside class="border-l-4 rounded-r-lg p-3"
         style="border-color:{{SCORE_COLOR}}; background:rgba(255,255,255,0.03)">
    <p class="text-sm italic text-gray-300">
      <span class="font-semibold not-italic text-gray-400">Beginner Take: </span>
      {{ONE_SENTENCE_PLAIN_ENGLISH}}
    </p>
  </aside>
  <!-- 3 metric cards -->
  <div class="grid grid-cols-3 gap-3">
    <!-- 3× metric card -->
    <div class="bg-gray-950 rounded-xl p-3 border border-gray-800">
      <p class="text-xs text-gray-400 mb-1">{{METRIC_LABEL}}</p>
      <p class="text-lg font-bold text-gray-100">{{METRIC_VALUE}}</p>
    </div>
  </div>
</div>
```

Metric cards per pillar:
- **Valuation:** P/E Ratio, EV/EBITDA, Sector P/E Avg
- **Health:** Debt-to-Equity, Current Ratio, FCF TTM
- **Growth:** YoY Revenue Growth, YoY Net Income Growth, Operating Margin

---

**Quarterly Trend Table:**

```html
<div class="bg-gray-900 rounded-2xl p-6 border border-gray-800">
  <h3 class="text-lg font-semibold text-gray-100 mb-4">Quarterly Trend</h3>
  <table class="w-full text-sm border-collapse">
    <thead>
      <tr class="bg-gray-800 text-gray-400 text-xs uppercase tracking-wide">
        <th class="p-3 text-left rounded-tl-lg">Quarter</th>
        <th class="p-3 text-right">Revenue</th>
        <th class="p-3 text-right">Net Income</th>
        <th class="p-3 text-right rounded-tr-lg">Op. Margin</th>
      </tr>
    </thead>
    <tbody>
      <!-- 4 rows, alternating bg-gray-900 / bg-gray-950 -->
      <!-- Net Income: text-green-400 if positive, text-red-400 if negative -->
    </tbody>
  </table>
</div>
```

---

**Earnings Recap:**

```html
<div class="bg-gray-900 rounded-2xl p-6 border border-gray-800">
  <h3 class="text-lg font-semibold text-gray-100 mb-4">Latest Earnings Recap</h3>
  <ul class="space-y-3">
    <!-- 3× -->
    <li class="flex gap-3">
      <span class="w-2 h-2 rounded-full bg-green-500 mt-2 shrink-0"></span>
      <span class="text-sm text-gray-300">{{SPECIFIC_FACTUAL_BULLET}}</span>
    </li>
  </ul>
  <p class="text-xs text-gray-500 mt-4">Source: {{SOURCE_NAME}} · {{DATE}}</p>
</div>
```

---

**Risk / Catalyst Matrix:**

```html
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
  <!-- Downside Risks -->
  <div class="bg-gray-900 rounded-2xl p-6 border border-red-900/30">
    <h3 class="text-base font-semibold text-red-400 mb-4">⬤ Downside Risks</h3>
    <ul class="space-y-2">
      <!-- 5× specific risks sourced from current news -->
      <li class="text-sm text-gray-300 flex gap-2">
        <span class="text-red-500 shrink-0">•</span>
        {{SPECIFIC_RISK}}
      </li>
    </ul>
  </div>
  <!-- Upside Catalysts -->
  <div class="bg-gray-900 rounded-2xl p-6 border border-green-900/30">
    <h3 class="text-base font-semibold text-green-400 mb-4">⬤ Upside Catalysts</h3>
    <ul class="space-y-2">
      <!-- 5× specific catalysts sourced from current news -->
      <li class="text-sm text-gray-300 flex gap-2">
        <span class="text-green-500 shrink-0">•</span>
        {{SPECIFIC_CATALYST}}
      </li>
    </ul>
  </div>
</div>
```

Each risk and catalyst must be specific and grounded in actual news or filing data from
the scratchpad. Generic statements like "competition may increase" or "markets could decline"
are not acceptable.

---

**Verdict Bar:**

```html
<div class="flex flex-col md:flex-row items-start md:items-center justify-between
            bg-gray-900 rounded-r-2xl p-5 border-l-4"
     style="border-color: {{SCORE_COLOR}}">
  <div>
    <p class="text-xs text-gray-400 uppercase tracking-wide mb-1">Overall Risk Profile</p>
    <span class="text-lg font-bold" style="color: {{SCORE_COLOR}}">{{RISK_LABEL}}</span>
    <span class="ml-2 text-gray-400 text-sm">Score: {{OVERALL_SCORE}} / 100</span>
  </div>
  <p class="text-sm text-gray-300 md:max-w-lg md:text-right mt-3 md:mt-0 leading-relaxed">
    {{1–2 SENTENCE SYNTHESIS based on pillar scores. No advice. No buy/sell language.}}
  </p>
</div>
```

---

**Footer:**

```html
<footer class="text-center text-xs text-gray-600 py-8 border-t border-gray-800">
  This report is for educational purposes only and does not constitute financial advice.
  Data sourced from public filings (SEC EDGAR, Yahoo Finance, Macrotrends) and may be
  delayed or contain errors. Risk scores are algorithmic estimates based on publicly
  available data, not investment recommendations. Report generated for {{TICKER}}.
</footer>
```

---

## Guardrails

**Provenance (mandatory).** Every dashboard carries a provenance section at page end, always present in
the DOM and never lazy-loaded, per `decision-provenance`. It records: source and as-of date per figure
class, which sector medians are live versus fallback defaults, every single-sourced figure, and any
`[MODEL]` input whose movement would change a score band. A score computed from fallback defaults and a
score computed from live sector medians must not look identical to the reader.


These rules apply to all output without exception:

1. **Banned vocabulary:** Do not use "buy," "sell," "hold," "overweight," "underweight,"
   "recommend," or "invest" anywhere in the HTML.
2. **Data discipline:** Every number rendered in the HTML must originate from the
   scratchpad. Do not introduce new values in Phase 2.
3. **Single file, zero network:** No external stylesheets, scripts, fonts, or images. No CDN.
   Everything inline. The report must render fully offline.
4. **No fabricated figures, anywhere, including charts:** every plotted point is a sourced,
   dated observation. If it cannot be sourced, the chart is omitted, not synthesised.
5. **Clean output:** After `</scratchpad>`, output raw HTML only. No code fences,
   no preamble, no trailing commentary.
6. **Phase gate:** Do not begin writing HTML until all six scratchpad steps are complete
   and the final score arithmetic has been verified.

---

## Editorial Gate

The narrative sections of the report (thesis, risk commentary, catalyst notes, the summary
block) route through the `write` skill before the HTML ships.

1. Draft the prose, then run `write` GATE v1 at deep tier. Deep tier is mandatory here: the
   report is a full document and it is client- or committee-facing.
2. Load `domain-finance.md` with the gate. Every price, yield, multiple, and economic figure
   carries an as-of date and a named source, and the compliance rules on recommendation
   language are blocking.
3. If the report reaches a private client or prospect rather than an internal committee, load
   `domain-wealth.md` as well and satisfy its gate too.
4. Gate the rendered text, not just the draft. Section headers, chart titles, table captions,
   and scorecard labels are written during the HTML build and never see the gate otherwise.
5. The gate touches prose craft only. It may never alter a figure, a date, a ticker, a source
   attribution, or a computed score. If a stylistic fix would change a number or a claim, it
   is flagged rather than made.
