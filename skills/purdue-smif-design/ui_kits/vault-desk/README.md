# Vault — desk surfaces

The desk register in use: a position monitor for the hours between the open and the close.

**Screen:** `PositionMonitor.jsx` — status bar with live feed indicator, five KPI tiles across, a 12-row position table with signal-colored change column, boxed tabs for Positions / Blotter / Risk, and a right rail carrying the intraday sparkline, an order ticket, and open orders. Sending an order opens a Dialog and resolves to a Toast.

**Composed from:** Button, Input, Select, Tabs, NavItem, StatTile, DataTable, Sparkline, Badge, StatusDot, Dialog, Toast, EmptyState.

**Theme:** `<html data-system="vault">` is dark by default. Add `data-theme="light"` for print and projection — gold drops to Deep Gold `#B8A070` automatically to hold WCAG AA on white.

**Density:** rows resolve to 26px. This is the tightest surface in the system; do not shrink type below 11px to fit more.

**On red and green:** the Purdue palette has no red, so direction defaults to gold up / gray down. Market convention is a documented exception for live desk screens only — see readme.md.
