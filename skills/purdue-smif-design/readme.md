# Purdue SMIF Design System — Bell Tower & Vault

Two design languages for the Purdue Student Managed Investment Fund, built on one Purdue palette and one type family set. They are not variants of the same look: **Bell Tower** is the institutional research register (serif, ruled, warm paper), **Vault** is the desk register (dark-native, monospace figures, 26px rows). Both are token-scoped, so the same React primitive renders correctly under either.

Everything here derives from the Purdue SMIF brand guidelines (palette, typography hierarchy, chart rules, voice) plus the four exploratory directions in this project's design docs.

## Sources

| Source | What came from it |
|---|---|
| `Design Systems Overview.dc.html` | The four-direction comparison this system was cut down from |
| `Bell Tower.dc.html` | Bell Tower tokens, component states, holdings dashboard |
| `Vault.dc.html` | Vault tokens, signal treatment, position monitor |
| `Boiler.dc.html`, `Lattice.dc.html` | Not exported — kept as design docs for reference |
| Purdue SMIF brand guidelines | Palette hex values, contrast rules, chart color roles, voice |

No Figma file, codebase, or logo assets were provided. See **Gaps** below.

## The two systems

| | Bell Tower | Vault |
|---|---|---|
| Use for | Research notes, IC memos, committee decks | Live monitoring, trading, ops |
| Headings | Source Serif 4, 400, no tracking | Source Sans 3, 600, −0.028em |
| Figures | Source Serif 4, tabular | IBM Plex Mono |
| Surface | Warm White `#FAF8F3` over White panels | Black `#000000` over `#1A1A1A` panels |
| Radius | 2px | 0 |
| Row height | 34px | 26px |
| Gold means | Section rules, chart primary, key figures | Signal — live series, gains, the thing to look at |
| Elevation | Dialogs only | None |
| Default theme | Light (`data-theme="dark"` available) | Dark (`data-theme="light"` for print) |

Apply a system by setting the attribute on any ancestor — usually `<html>`:

```html
<html data-system="bell-tower">           <!-- light research -->
<html data-system="vault">                 <!-- dark desk -->
<html data-system="vault" data-theme="light"><!-- desk, printed -->
```

## Visual foundations

**Color.** Purdue Gold `#CEB888` is the only accent in either system; Deep Gold `#B8A070` is its darker, AA-safe form on white. Body copy is Dark Gray `#4A4C52` in light and Light Gray `#D4D5D8` in dark — never pure black on white, so gold rules and headings stay the darkest marks on the page. Light Purdue Gold `#E8D9A0` and Sand `#E8E0CC` are backgrounds only, never text. There is no red or green in the palette: **direction is gold up, gray down.** Market convention (red/green) exists only as a documented exception on live desk screens, and it is a deliberate brand deviation — flag it when used.

**Type.** Three faces. Source Serif 4 carries Bell Tower headings and figures. Source Sans 3 carries all body copy, all labels, and Vault headings. IBM Plex Mono carries Vault figures, column labels, timestamps, and keyboard hints. Labels are 10px, 0.12em tracking, uppercase, 600 — identical in both systems, which is what makes a mixed screen still read as one family.

**Layout and structure.** Bell Tower divides with rules: a 3px black cap on primary panels, 1px `#D4D5D8` hairlines everywhere else, and dotted `#E8E0CC` inside panels. Vault divides with 1px grid gaps in `#2C2C2C` and value contrast alone. Neither system uses cards-with-shadows as a layout device; the only shadow in the whole system is `--shadow-dialog`, and Vault sets it to `none`.

**Motion.** 100ms for control feedback, 140ms for surface changes, `cubic-bezier(0.2, 0, 0.2, 1)`. No bounces, no entrance animations, no skeleton shimmer. Hover is a background or border-color shift; press is a 2% scale down on gold buttons only.

**States.** Focus is a 2px ring — Sand in Bell Tower, Dark Gray in Vault — always visible, never removed. Active navigation is a 2px gold underline (tabs) or a 2px gold left rule (side nav). Selection is `--accent-soft` fill. Disabled is inset background plus faint text, never reduced opacity.

**Density.** These are dense systems by design (the brief called for 8 of 10). Tables carry 26–34px rows, 8–12px cell padding, 11–12px type. Do not add breathing room to a table to make it look calmer; if it feels crowded, remove a column.

## Content fundamentals

Voice is analytical, not promotional — confident in method, measured about outcomes. Write in third person or the plural first person ("the fund"), never "we're excited to." Sentence case for headings and buttons; ALL CAPS only for 10px labels and status badges. Numbers always carry their unit or currency, percentages to two decimals, basis points spelled as "bps." Empty states name what is missing and what will fill it ("Sector allocation opens once the committee approves a pitch"), never "No data available." Dialog titles ask the question; the body states the consequence. No emoji, anywhere. Banned in all copy: "premier," "world-class," "robust portfolio," "navigate volatility," "positioned for growth," "unlock value," and every other hyperbole the brand guidelines list.

Sample figures throughout this system are illustrative. Label them as such on anything a reader might mistake for a live position.

## Iconography

**The system deliberately ships no icon set.** Every glyph in these components is a text character — `✓` for checked, `▾` for select, `✕` for dismiss, `▲ ▼` for direction, `←  →` for pagination, `●` for live state, `/` and `›` for breadcrumbs. Keyboard hints (`⌘K`, `⏎`, `F2`) render in the mono face inside a 1px bordered chip. This is a real design decision, not a gap: at 11–12px, a monospace glyph reads more precisely than a 16px stroked icon, and nothing has to be redrawn per theme.

If a future surface genuinely needs stroked icons, the brand guidelines specify line icons at ~2px stroke with sharp edges and rounded accents, default Purdue Gold. Match that, and add them under `assets/icons/` — do not import a full icon library.

## Component index

Seventeen primitives, grouped by concern. Each has `<Name>.jsx`, `<Name>.d.ts`, and `<Name>.prompt.md`; each directory has one gallery card showing both systems side by side.

- `components/forms/` — Button, Input, Select, Checkbox, Switch
- `components/data/` — StatTile, DataTable, AllocationBar, Sparkline
- `components/feedback/` — Badge, StatusDot, Dialog, Toast, EmptyState
- `components/navigation/` — Tabs, Breadcrumb, NavItem

**Intentional additions.** No source defined a component inventory, so this is an authored set sized to the two surfaces. StatTile, DataTable, AllocationBar, Sparkline, StatusDot, and EmptyState are not in the standard primitive list but appear repeatedly in both design docs and are what the dashboards are actually made of. Tooltip, Radio, and Tag were left out — nothing in either surface uses them.

## File index

- `styles.css` — the entry point consumers link. `@import` lines only.
- `tokens/` — `fonts.css`, `colors.css` (raw Purdue palette), `typography.css`, `spacing.css`, `system-bell-tower.css`, `system-vault.css` (semantic aliases per system and theme), `reset.css`.
- `components/` — the seventeen primitives and their gallery cards.
- `guidelines/` — fifteen foundation specimen cards: palette, surfaces per system, signal colors, type scales, numerals, spacing, radius, row density, focus states, elevation.
- `ui_kits/bell-tower-research/` — holdings dashboard (screen + README).
- `ui_kits/vault-desk/` — position monitor (screen + README).
- `SKILL.md` — Agent Skills entry point if you download this system.
- `*.dc.html` — the original four design directions, kept as reference.

## Gaps and substitutions

1. **Fonts are substituted.** Purdue's licensed faces (United Sans, Acumin Pro) are not distributable here. Source Serif 4 and Source Sans 3 are the Adobe families Purdue's own web standard is built on, loaded from Google Fonts in `tokens/fonts.css`. **Send the licensed files and I'll swap them into real `@font-face` rules with local binaries.**
2. **No logo assets.** Every wordmark is set in plain type. Drop `smif-logo-primary.svg` and `smif-logo-on-dark.svg` into `assets/logos/` and I'll wire them into both UI kit headers at 160px wide, height auto. Nothing here draws or approximates a Purdue mark.
3. **Hairline normalization.** The design docs used `#E5E1D8` for Bell Tower's inner rules, which is not a brand palette value. The exported tokens use Sand `#E8E0CC` and Light Gray `#D4D5D8` instead. Visually near-identical, palette-pure.
4. **Two systems, one compiled project.** The compiler indexes one design system per project, so both languages live here as `[data-system]` scopes rather than two separate downloads. If you need them fully separate, say so and I'll split them.
