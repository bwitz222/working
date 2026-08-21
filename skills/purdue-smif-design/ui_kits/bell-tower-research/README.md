# Bell Tower — research surfaces

The institutional register in use: a holdings dashboard sized for a committee reviewing positions on screen or on paper.

**Screen:** `HoldingsDashboard.jsx` — header with breadcrumb and publish action, left nav with counts, four KPI tiles, a tabbed holdings table, sector bars against benchmark ticks, and a cumulative-return sparkline. The publish button opens a Dialog; confirming raises a Toast.

**Composed from:** Button, Input, Select, Breadcrumb, Tabs, NavItem, StatTile, DataTable, AllocationBar, Sparkline, Badge, Dialog, Toast, EmptyState. Nothing is re-implemented locally except the `Panel` wrapper, which is layout, not a primitive.

**Theme:** `<html data-system="bell-tower">`. Add `data-theme="dark"` for the dark counterpart — no other change is needed.

**Density:** rows resolve to 34px through `--row-height`. Do not override per screen.
