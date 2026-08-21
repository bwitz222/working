---
name: purdue-smif-design
description: Use this skill to generate well-branded dashboards, screens, and assets for the Purdue Student Managed Investment Fund (SMIF), for production code or throwaway prototypes/mocks. Contains two token-scoped, production-hardened design systems — Bell Tower (light, serif, institutional research) and Vault (dark, mono, trading desk) — sharing one Purdue palette and one React component library (17 primitives with real hover/focus/keyboard states). Trigger whenever the user asks for a SMIF dashboard, holdings/positions screen, IC memo layout, portfolio UI, or any interface that should carry Purdue SMIF branding, even if they don't name the design system directly.
---

Read `readme.md` in this skill first — it has the full foundations doc (color, type, layout, motion, content rules) and a file index. Then explore the other files as needed; you rarely need to read everything.

## Pick the register before you pick components

- **Bell Tower** (`data-system="bell-tower"`) — research notes, IC memos, committee decks, anything printed or read closely. Serif headings, warm paper, 34px rows, 2px radius.
- **Vault** (`data-system="vault"`) — live monitoring, trading, ops dashboards. Dark by default, mono figures, 26px rows, 0 radius. Use `data-theme="light"` for print or projection.

Both are token-scoped: the same component renders correctly under either just by changing the `data-system` (and optional `data-theme`) attribute on an ancestor element — never fork a component per system.

## How to build with it

1. Link `styles.css` (it `@import`s the full token chain, including `components/interactions.css` for hover/focus states) and set `data-system` on the root element of whatever you're building.
2. Compose screens from `components/` — import from `components/index.js` (a barrel export of all 17 primitives) rather than reaching into individual files. Read the `.prompt.md` beside any component for its usage pattern and variant options, and its `.d.ts` for the exact prop types.
3. `ui_kits/` holds two full screens (`bell-tower-research/HoldingsDashboard.jsx`, `vault-desk/PositionMonitor.jsx`) worth copying as starting points — but they're written as global-script components for a design-tool preview harness (`window.React`, no imports/exports). Don't copy them verbatim into a real app.
4. **`reference-app/` is the one to actually copy from.** It's a working Vite + React app where both dashboards are ported to real ES modules, imported from `components/index.js`, with working dialog→toast flows and light/dark toggles wired up. It demonstrates the two integration details that aren't obvious from the component source alone:
   - `reference-app/vite.config.js` — when `components/` lives outside the consuming app's own `node_modules` tree (e.g. this skill's files copied next to, not inside, the app), bare `import "react"` fails to resolve. The `resolve.alias` + `dedupe` block there is the fix.
   - `reference-app/src/dashboards/PositionMonitor.jsx` — shows how to apply Vault's optional market-convention (red/green) override by setting `--signal-up`/`--signal-down` inline as a CSS custom property on a wrapping element, scoped to just that subtree, rather than forking the token file.

If you're starting a genuinely new app (not adding a screen to an existing one), `reference-app/` is also a reasonable scaffold to copy wholesale and rename.

## Hard rules — not negotiable

Only Purdue palette colors (see `tokens/colors.css`); Purdue Gold is the sole accent; no red or green for direction unless the user explicitly asks for market convention, and then flag it as a documented brand deviation; Light Purdue Gold and Sand are backgrounds, never text; body copy never pure black; no emoji; no icon library — every glyph is a text character (✓ ▾ ✕ ▲ ▼ ← → ● / ›). Dense by design — don't add breathing room to a table to make it look calmer; if it feels crowded, remove a column instead.

## Output mode

- **Visual artifact** (slide, mock, throwaway prototype): copy the token files and produce static HTML for the user to view — don't wire up a build.
- **Production code**: copy `tokens/`, `components/`, and `styles.css` into the target codebase (or add this skill's folder as a dependency path), then follow the `reference-app/` integration pattern.

If invoked with no other guidance, ask what the user wants to build, which register it belongs to (research vs. desk), and who reads it — then act as an expert designer and output HTML artifacts or production code as the need dictates.

## What's reference-only, not compiled

`Bell Tower.dc.html`, `Vault.dc.html`, `Boiler.dc.html`, `Lattice.dc.html`, and `Design Systems Overview.dc.html` are the original four design-tool prototype exports, kept for historical context (`support.js` is their preview runtime — nothing here needs to execute it). Only Bell Tower and Vault were ever compiled into `tokens/`/`components/`; Boiler and Lattice are design docs only — there's no token scope or component variant for either. Don't build a "Boiler" or "Lattice" screen from this skill; if a user wants one, it needs to be compiled first (extend `tokens/` with a new `[data-system="boiler"]` block following the pattern in `tokens/system-bell-tower.css`).

The `guidelines/*.card.html` and `components/*/*.card.html` files are design-tool preview cards — they reference a `_ds_bundle.js` file and CDN React/Babel that don't exist in this packaged skill, so they won't render standalone. Their content (palette swatches, type scale, component pairings) is fully reproduced and actually running in `reference-app/src/pages/Foundations.jsx` — read that instead if you want to see the specimens rendered.
