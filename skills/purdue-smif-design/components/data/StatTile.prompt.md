One-line: the KPI tile — label above, tabular figure below, at most one line of context.

```jsx
<StatTile label="Market value" value="$1,482,309" meta="24 positions · 3.1% cash" emphasis />
<StatTile label="Return, semester" value="+6.28%" tone="up" meta="+118 bps vs. S&P 500" />
```

Use `emphasis` on one tile per row at most. Figures render in --font-numeric, which is the serif in Bell Tower and the mono in Vault.
