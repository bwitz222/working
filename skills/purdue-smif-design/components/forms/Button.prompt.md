One-line: the action control — use `accent` for the single most important action in a view and `primary` for everything else consequential.

```jsx
<Button variant="accent" size="md" onClick={send}>Send order</Button>
<Button variant="secondary">Export</Button>
<Button variant="ghost">Cancel</Button>
```

Variants: `primary` (inverted surface — black on light, light on dark), `accent` (Purdue Gold fill, black label), `secondary` (1px strong border), `ghost` (muted text). Sizes `sm | md | lg`. In Bell Tower the radius resolves to 2px; in Vault it resolves to 0.
