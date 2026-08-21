---
name: purdue-smif-brand-guidelines
description: Apply Purdue Student Managed Investment Fund (SMIF) brand guidelines — colors, typography, logo usage, imagery, voice. Use whenever creating any .docx, .pptx, .xlsx, or .html file, regardless of topic or whether SMIF is named. Also for any chart, infographic, PDF, email, or visual asset for SMIF.
---

# Purdue SMIF Brand Guidelines

**Standing rule.** Apply to ALL .docx, .pptx, .xlsx, and .html files regardless of topic, audience, or intent — final deliverables, drafts, and test versions alike. Apply to PDFs, charts, infographics, and emails for SMIF. Honor opt-outs only when explicit ("no SMIF branding," "unbranded").

---

## GUARDRAILS — read first, apply always

**Never fabricate brand assets.** Do not invent hex values, logo filenames, or template paths not listed in this skill. If an asset is missing, flag it and ask.

**Never alter the logo.** Do not recolor, rescale non-uniformly, rotate, crop, or rebuild any SMIF or Purdue logo element. If a logo file is unavailable, use a text placeholder and note the gap.

**Never use colors outside this palette.** Do not introduce new colors for aesthetic reasons. If a use case isn't covered, use the closest named color from the Supporting palette.

**Accessibility is non-negotiable.** Do not place text in any color combination that fails the WCAG AA contrast rules listed below. If a design choice creates a failing pair, substitute the nearest compliant option.

**Brand vs. user conflict.** When a user requests something that violates these guidelines (e.g., a red accent, a widescreen-to-4:3 switch), apply the guideline and note the substitution. Do not silently override brand rules.

**Scope carve-out.** Do not apply brand formatting to raw code blocks, API output, terminal snippets, or data-only exports (.csv, .json). Brand rules apply to human-readable deliverables only.

**Do not apply the de-slop gate to financial data, legal disclosures, or compliance language.** Substance and register of those elements must be preserved exactly.

---

## Fast-Exit for Simple Queries

For queries that only need a color or font value (e.g., "what hex is Purdue Gold?"), answer directly from the Colors or Typography section and stop. Do not load or narrate the full skill.

---

## Colors

Defined here only. Reference by name in all other sections and in generated code.

### Primary

| Name | Hex | RGB | Usage |
|---|---|---|---|
| Purdue Gold | `#CEB888` | 206, 184, 136 | Primary brand anchor — headers, header bars, callouts, chart primary series, interactive elements |
| Black | `#000000` | 0, 0, 0 | Structural anchor — cover backgrounds, bold headers on light fields, high-contrast text |
| Purdue Gray | `#6F727B` | 111, 114, 123 | All body copy and secondary text — never use pure Black for running text |
| Light Purdue Gold | `#E8D9A0` | 232, 217, 160 | Backgrounds, table row stripes, section fills only — never as text color |
| White | `#FFFFFF` | 255, 255, 255 | Content area backgrounds; reversed text on Black or dark panels |

### Supporting (dashboards, infographics, multi-category charts)

Dark Black `#1A1A1A` · Near Black `#2C2C2C` · Dark Gray `#4A4C52` · Medium Gray `#9B9EA4` · Light Gray `#D4D5D8` · Off White `#F5F2EC` · Warm White `#FAF8F3`

Extended (callouts, chevrons, secondary highlights): Deep Gold `#B8A070` · Muted Gold `#D4C090` · Slate `#5C6370` · Sand `#E8E0CC`

### Contrast Rules (WCAG AA — enforced)

| Pair | Result |
|---|---|
| Black on White | ✓ pass |
| Black on Light Purdue Gold | ✓ pass |
| Purdue Gold on Black | ✓ pass |
| Purdue Gray on White | ✓ pass |
| Light Purdue Gold on White (text) | ✗ fail — backgrounds only |
| Purdue Gray on Light Purdue Gold (text) | ✗ fail — do not combine |

---

## Voice

Analytical, not promotional. Confident in method, measured about outcomes. Academic rigor with professional presentation.

**Use:** disciplined, rigorous, objective, thesis-driven, risk-adjusted, conviction, alpha, intrinsic value, sector rotation, duration, credit quality, portfolio construction, due diligence.

**Never use:** "premier," "world-class," "best-in-class," "cutting-edge," "groundbreaking," or any hyperbole. Do not overstate certainty on forward-looking statements.

**By audience:**
- Internal / faculty: candid, educational — surface assumptions and reasoning.
- External / institutional: structured, formal — lead with thesis, support with data.

**AI writing patterns banned in all SMIF copy** (see also `purdue-smif-editorial-style` and the de-slop references in `write`):
- Significance inflation: "testament to," "pivotal moment," "evolving landscape," "underscores"
- Finance-specific AI tells: "robust portfolio," "dynamic market conditions," "headwinds and tailwinds," "navigate volatility," "unlock value," "positioned for growth"
- Filler openers: "It is worth noting," "At its core," "In today's market environment"
- Vague attributions: "analysts believe," "the market expects," "observers note" — cite the source or delete
- Generic conclusions: "the future looks bright," "exciting times ahead," "a major step forward"

---

## Typography

`.docx` / `.pptx` / `.xlsx` / `.eml` → **Calibri**. HTML and designed PDFs → **Georgia** (body) + **Calibri** (data labels). Regular/Light for body; Bold for headings. Do not substitute other fonts.

### Calibri Hierarchy (Office)

| Style | Font | Size | Color |
|---|---|---|---|
| Cover headline | Calibri Bold | 36 pt | White (on Black) |
| Section title | Calibri Light | 24 pt | Purdue Gold |
| Slide / page title | Calibri Light | 18 pt | Black or Purdue Gold |
| Paragraph heading | Calibri Bold | 11 pt | Black |
| Body copy | Calibri Regular | 10–11 pt | Purdue Gray |
| Footnote / caption | Calibri Regular | 8–9 pt | Purdue Gray |
| Table header | Calibri Bold | 9–10 pt | White on Black, or Black on Light Purdue Gold |
| Table body | Calibri Regular | 9–10 pt | Purdue Gray |

### Georgia + Calibri Hierarchy (HTML, Designed PDFs)

| Style | Font | Size / Leading | Color |
|---|---|---|---|
| Cover headline | Georgia Regular | 36 / 40 pt | White (on Black overlay) |
| Page title | Georgia Regular | 21 / 26 pt | Purdue Gold |
| Section header | Calibri Light | 16 / 20 pt | Purdue Gold |
| Paragraph heading | Calibri Bold | 10 / 13 pt | Black |
| Body copy | Georgia Regular | 9 / 14 pt | Purdue Gray |
| Data / metric label | Calibri Regular | 8 / 12 pt | Purdue Gray |

---

## Logo

Files live in `assets/logos/`. **Logo files are provided by the user — do not fabricate filenames.** Prefer SVG; fall back to PNG only when the renderer cannot handle SVG. If no file is available, insert a bracketed placeholder: `[SMIF LOGO]`.

### Routing

| File | When |
|---|---|
| `smif-logo-primary` | Default — light backgrounds, top-left of slides and letterheads |
| `smif-logo-on-dark` | Reversed (white/gold) — Black backgrounds and dark panels |
| `smif-logo-mono-black` | B&W printing only |
| `smif-wordmark-only` | When the Purdue Block P cannot be reproduced |
| `smif-mark-only` | Compact mark — tight placements under 1.5 in wide |

**Quick rule:** light bg → `-primary`. Dark/Black → `-on-dark`. Under 1.5 in → `-mark-only`.

### Hard Rules

- Never alter, recolor, stretch, rotate, or rebuild the logo.
- Never place Purdue Gold logo on Light Purdue Gold background — insufficient contrast.
- Never use the Block P as a decorative element.
- Minimum width for full logo: 1.5 in. Below that, use `-mark-only`.
- Clear space: ≥ 0.125 in on all sides.

### Aspect Ratios

**Set width only. Never set both width and height — the logo will compress.**

| File family | Approx. ratio (w:h) | Notes |
|---|---|---|
| `logo-primary` / `logo-mono-*` | ~5.5 : 1 | Update once actual files are measured |
| `logo-on-dark` | ~5.5 : 1 | Update once actual files are measured |
| `mark-only` (Block P) | ~1 : 1.1 | Verify against actual file |

```js
// pptxgenjs — update LOGO_PRIMARY_AR once files are measured
const LOGO_PRIMARY_AR = 5.5;
const logoH = (w, ar) => w / ar;
slide.addImage({ path: LOGO_PRIMARY, x, y, w: 2.0, h: logoH(2.0, LOGO_PRIMARY_AR) });
```

### Typical Placements

| Location | File | Width |
|---|---|---|
| Report cover, Black panel | `logo-on-dark` | 3.0–3.5 in |
| Closing slide, bottom-right | `logo-on-dark` | 2.0–2.5 in |
| Content slide, bottom-left (standard) | `logo-primary` | **1.10 in** |
| Page footer compact | `mark-only` | 0.4 in |
| HTML dashboard, top-left | `logo-primary` | 140–180 px (width only) |

### HTML Logo Implementation

Deployed (with asset pipeline):
```html
<img src="/assets/logos/smif-logo-primary.svg"
     alt="Purdue Student Managed Investment Fund"
     style="width: 160px; height: auto; display: block;">
```

Standalone HTML (single-file artifacts):
```html
<span class="logo" role="img" aria-label="Purdue Student Managed Investment Fund">
  <!-- Paste smif-logo-primary.svg contents here. Remove source width="100%". -->
</span>
```
```css
.logo { display: block; width: 160px; }
.logo svg { width: 100%; height: auto; display: block; }
```

Tailwind: `w-40 h-auto`. Never `w-40 h-12`.

---

## Charts

| Element | Color |
|---|---|
| Primary series | Purdue Gold |
| Secondary series | Black |
| Tertiary / additional | Purdue Gray → Medium Gray → Light Gray (in order) |
| Highlight / outperformance | Deep Gold `#B8A070` |
| Underperformance / decline | Purdue Gray (avoid red unless regulatory convention requires it) |
| Axis labels | Purdue Gray |
| Gridlines | Light Gray |
| Chart titles | Calibri Bold (Office) or Georgia Bold (designed) in Black |
| Data labels on dark fill | White |
| Data labels on light fill | Black |
| Chart area background | White or Off White — never dark |

---

## Imagery

**Subjects:** financial markets, trading floors, data visualization, Purdue campus, students in professional settings, Bloomberg terminals, research materials.

**Tone:** authentic student/professional photography. Avoid generic stock imagery.

**Overlays:** Black → external-facing and cover materials. Deep Gold / Purdue Gold → internal reports and section dividers. Never combine both on the same piece. Opacity: 65–80%.

**Portraits:** neutral or campus background, professional attire, shallow depth of field.

**Charts and data graphics** are primary imagery — design them with the same care as photographs.

---

## Icons

Line-icon style, ~2px stroke, sharp edges with rounded accents, default color Purdue Gold. Subject library: equity, bond/fixed income, portfolio, sector, benchmark, alpha/beta, risk, return, duration, thesis, screening, committee, university/academic, semester calendar. Match this style when generating inline SVG.

---

## Templates

Start from `assets/templates/`. Do not build from scratch when a template exists.

| File | Use for |
|---|---|
| `SMIF-Standard-Deck.potx` | Investment pitches, committee reviews, class presentations |
| `SMIF-Semester-Report-Template.pptx` | Semester performance reports |
| `SMIF-Annual-Report-Template.pptx` | Annual portfolio review |
| `SMIF-Memo-Template.docx` | IC memos, research briefs, internal communications |

**Slide size: 13.33 × 7.5 in (16:9).** Never default to 4:3 unless the venue explicitly requires it.

### PowerPoint Workflow

Use **python-pptx** when starting from a template (inherits slide master). Use pptxgenjs only for fully custom designs, and reproduce chrome manually.

```python
from pptx import Presentation
prs = Presentation('assets/templates/SMIF-Semester-Report-Template.pptx')
# Duplicate an existing slide; replace text and data.
```

### Standard Slide Chrome

**Layout grid (13.33 × 7.5 in):**

| Element | x | y | w | h | Notes |
|---|---|---|---|---|---|
| Section eyebrow (ALL CAPS) | 0.30 | 0.15 | 12.73 | 0.30 | Black Calibri ~11pt |
| Header bar — Black segment | 0.30 | 0.48 | ~8.50 | 0.06 | ~65% of width |
| Header bar — Deep Gold diagonal | ~8.50 | 0.48 | ~0.25 | 0.06 | Transition slice |
| Header bar — Purdue Gold segment | ~8.75 | 0.48 | ~4.28 | 0.06 | To right edge |
| Slide title | 0.30 | 0.58 | 12.73 | 0.44 | Calibri Light 18pt, Purdue Gold or Black |
| Content area | 0.30 | 1.10 | 12.73 | 5.90 | White background |
| Footer logo | 0.30 | 7.10 | 1.10 | auto | `logo-primary`, width 1.10 in, height auto |
| "Confidential" caption | 0.60 | 7.32 | 1.00 | 0.10 | Calibri Italic 8pt, Purdue Gray |
| Period label (centered) | 4.50 | 7.15 | 4.33 | 0.25 | e.g., "Fall 20XX" — Calibri Regular 8pt |
| Page number | 12.00 | 7.10 | 1.03 | 0.30 | Right-aligned, Purdue Gray |

Logo: bottom-left only on content slides. Header bar: thin Black → Deep Gold → Purdue Gold strip — never a thick colored band.

### Cover Slide

Black full-bleed background (or photo with Black overlay at 70–80% opacity); Purdue Gold diagonal accent panel; `logo-on-dark` at 3.0–3.5 in; fund name and report title in White Calibri Bold; semester/year in Purdue Gold Calibri Light; `"Confidential — For Internal Distribution Only"` in White Calibri Italic ~10pt at bottom.

### Closing Slide

Solid Black background. `logo-on-dark` centered or bottom-right at 2.0–2.5 in wide. Fund name in White Calibri Light. Optional Purdue Gold horizontal rule above.

### Word / Memos

Start from `SMIF-Memo-Template.docx`. From scratch: `logo-primary` top-left letterhead; headings Calibri Bold Black; subheadings Calibri Bold Purdue Gold; body Calibri Regular Purdue Gray 11pt; page numbers Purdue Gray bottom-right; Purdue Gold horizontal rule below the letterhead logo.

### PDFs / Reports

Cover: Black background or full-bleed photo with Black overlay, fund name Georgia Regular 36pt White, `logo-on-dark` upper- or lower-left. Interior: White background, Georgia body, Calibri data labels, Purdue Gold section headers.

---

## Layout Catalog (Semester / Annual Reports)

Match the request to a pattern. Do not reinvent unless none fits.

| # | Pattern | Use for |
|---|---|---|
| 1 | Bullet panel (left, Black/Gold header) + data table (right) | Portfolio highlights + metrics |
| 2 | 4–5 stacked callout boxes (Black, Gold, Gray, Light Gold) + side table | Multi-sector summary |
| 3 | 3 stacked rows: colored label + icon + bullets | Three thematic areas (equities, fixed income, macro) |
| 4 | 3 columns: Gold header + sub-heading + data table | Sector-by-sector comparison |
| 5 | 2-column: Black header + bullets + chart | Benchmark vs. Portfolio, before/after |
| 6 | 3-column text, Gold column headers, dense paragraphs | Text-heavy commentary, fund overview |
| 7 | 4-column process chevrons: Black / Gold / Gray / Light Gold | Investment process, semester timeline |
| 8 | Full-width chart + caption + annotation callouts | Single-chart feature slide |
| 9 | 2×2 grid of metric cards (large number + label + delta) | KPI scorecard |
| 10 | Cover / title slide | Report opening |

---

## Writing Quality Pass (apply before finalizing any body-copy deliverable)

Run in order. Stop when the text is clean; do not over-edit.

1. **De-slop pass** · remove AI writing patterns with `write`, CLEAN mode. Key targets for SMIF: significance inflation, finance AI tells (listed under Voice above), meta-commentary, dramatic fragmentation, em dash overuse, and vague attributives.
2. **Deep tier** · run the GATE v1 deep tier, the 24-pattern catalog, from `write`. Confirm the text reacts to data rather than just reporting it. Vary sentence length.
3. **Register check** — financial data, legal disclosures, compliance language, and verbatim quoted material are exempt from both passes. Preserve their substance exactly.
4. **Fabrication check** — confirm no figures, tickers, benchmark names, or company names were invented. Every specific claim must trace to a source or be flagged.

---

## Out of Scope

Physical-asset specs (printed materials, banners, apparel, building signage). Logo file creation. Refer to Purdue University brand office for official asset production.

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
