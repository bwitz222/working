One-line: labelled field for text and figures; `mono` switches the value to the system's numeric face.

```jsx
<Input label="Quantity" value="250" mono suffix="shares" />
<Input label="Position size" value="6.2" invalid hint="Exceeds the 5% single-name cap." />
```

Focus is a 1px strong border plus the system focus ring (2px sand in Bell Tower, 2px dark gray in Vault). Invalid state uses Deep Gold, never red.
