One-line: the workhorse — a CSS-grid table where numeric columns right-align in the system's numeric face.

```jsx
<DataTable
  columns={[
    { key: "ticker", label: "Ticker", width: "62px", numeric: true, strong: true },
    { key: "name", label: "Name", width: "1.5fr" },
    { key: "value", label: "Value", align: "right", numeric: true },
    { key: "chg", label: "Chg", align: "right", numeric: true, tone: r => (String(r.chg).startsWith("-") ? "down" : "up") }
  ]}
  rows={holdings}
/>
```

Always right-align figures. State the sort in the toolbar above the table and mark the sorted column with ↓ / ↑ — a table that misstates its own order is worse than an unsorted one.
