# PDF Annotations Reference

All annotation work uses PyMuPDF (`fitz`). Annotations are non-destructive overlays.
For permanent content stamping, use `insert_text`/`insert_image` in SKILL.md instead.

---

## Annotation Types Quick Reference

| Acrobat Name | PyMuPDF Type | fitz Constant |
|-------------|-------------|---------------|
| Highlight | Highlight | `fitz.PDF_ANNOT_HIGHLIGHT` |
| Underline | Underline | `fitz.PDF_ANNOT_UNDERLINE` |
| Strikethrough | StrikeOut | `fitz.PDF_ANNOT_STRIKE_OUT` |
| Squiggly underline | Squiggly | `fitz.PDF_ANNOT_SQUIGGLY` |
| Sticky note | Text | `fitz.PDF_ANNOT_TEXT` |
| Free text box | FreeText | `fitz.PDF_ANNOT_FREE_TEXT` |
| Arrow / line | Line | `fitz.PDF_ANNOT_LINE` |
| Rectangle | Square | `fitz.PDF_ANNOT_SQUARE` |
| Ellipse | Circle | `fitz.PDF_ANNOT_CIRCLE` |
| Ink (freehand) | Ink | `fitz.PDF_ANNOT_INK` |
| Stamp | Stamp | `fitz.PDF_ANNOT_STAMP` |
| File attachment | FileAttachment | `fitz.PDF_ANNOT_FILE_ATTACHMENT` |

---

## Highlight Text

```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]

# Search for text to highlight
search_results = page.search_for("IMPORTANT")

for rect in search_results:
    annot = page.add_highlight_annot(rect)
    annot.set_colors(stroke=(1, 1, 0))   # yellow highlight (RGB 0-1)
    annot.set_info(content="Review this section")  # tooltip text
    annot.update()

doc.save("highlighted.pdf")
```

### Highlight a custom rectangle (manual selection equivalent)

```python
# Define your own rectangle (x0, y0, x1, y1) in page points
rect = fitz.Rect(72, 200, 400, 220)
annot = page.add_highlight_annot(rect)
annot.set_colors(stroke=(0, 1, 0))   # green
annot.update()
```

### Multiple colors highlight pass

```python
colors = {
    "urgent": (1, 0.2, 0.2),    # red
    "review": (1, 1, 0),          # yellow
    "done":   (0.5, 1, 0.5),     # green
}
for keyword, color in colors.items():
    for rect in page.search_for(keyword):
        annot = page.add_highlight_annot(rect)
        annot.set_colors(stroke=color)
        annot.update()
```

---

## Sticky Notes (Pop-up Comments)

```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]

# Sticky note at position (x, y)
annot = page.add_text_annot(
    (100, 200),                           # anchor point
    "Please review this paragraph",       # comment text
    icon="Note"                           # Note, Comment, Key, Help, NewParagraph,
)                                         # Paragraph, Insert, Cross, Circle, Check

annot.set_info(
    title="Reviewer Name",       # author shown in comment
    content="Please review this paragraph",
)
annot.set_colors(stroke=(1, 0.8, 0), fill=(1, 1, 0.5))  # icon border and fill
annot.update()

doc.save("with_notes.pdf")
```

---

## Free Text Box (Visible Comment / Call-out)

```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]

# Place a visible text box
rect = fitz.Rect(100, 300, 350, 360)
annot = page.add_freetext_annot(
    rect,
    "This clause needs legal review.",
    fontsize=11,
    fontname="helv",
    text_color=(0, 0, 0),
    fill_color=(1, 1, 0.8),   # light yellow background
    border_color=(0.8, 0.6, 0),
    border_width=1,
)
annot.update()

doc.save("with_freetext.pdf")
```

---

## Shape Annotations (Rectangle, Ellipse, Line, Arrow)

```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]

# Rectangle outline
rect = fitz.Rect(50, 100, 400, 300)
annot = page.add_rect_annot(rect)
annot.set_colors(stroke=(1, 0, 0), fill=None)   # red border, transparent fill
annot.set_border(width=2)
annot.update()

# Filled ellipse
rect2 = fitz.Rect(50, 350, 200, 450)
annot2 = page.add_circle_annot(rect2)
annot2.set_colors(stroke=(0, 0, 1), fill=(0.8, 0.8, 1))  # blue outline, light blue fill
annot2.update()

# Line with arrow
p1, p2 = fitz.Point(50, 500), fitz.Point(250, 500)
annot3 = page.add_line_annot(p1, p2)
annot3.set_line_ends(fitz.PDF_ANNOT_LE_NONE, fitz.PDF_ANNOT_LE_OPEN_ARROW)
annot3.set_colors(stroke=(0, 0.5, 0))
annot3.update()

doc.save("shapes.pdf")
```

Line end styles: `PDF_ANNOT_LE_NONE`, `PDF_ANNOT_LE_OPEN_ARROW`,
`PDF_ANNOT_LE_CLOSED_ARROW`, `PDF_ANNOT_LE_CIRCLE`, `PDF_ANNOT_LE_DIAMOND`,
`PDF_ANNOT_LE_SQUARE`

---

## Ink (Freehand Drawing)

```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]

# List of strokes; each stroke is a list of (x,y) points
strokes = [
    [(100, 100), (150, 120), (200, 100), (250, 130)],  # stroke 1
    [(100, 150), (300, 150)],                            # stroke 2 (straight line)
]
annot = page.add_ink_annot(strokes)
annot.set_colors(stroke=(0, 0, 0.8))  # dark blue
annot.set_border(width=2)
annot.update()

doc.save("freehand.pdf")
```

---

## Stamps

```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]

# Built-in stamp names
STAMP_NAMES = [
    "Approved", "Experimental", "NotApproved", "AsIs", "Expired",
    "NotForPublicRelease", "Confidential", "Final", "Sold",
    "Departmental", "ForComment", "TopSecret", "Draft", "ForPublicRelease",
]

rect = fitz.Rect(200, 100, 500, 200)
annot = page.add_stamp_annot(rect, stamp=14)   # 14 = "Draft" in the enum
# Or use a custom text stamp:
annot = page.add_freetext_annot(
    rect,
    "DRAFT",
    fontsize=48,
    text_color=(1, 0, 0),
    fill_color=None,
    border_color=(1, 0, 0),
    rotate=45,
)
annot.update()

doc.save("stamped.pdf")
```

---

## Read and Export Existing Annotations

```python
import fitz
import json

doc = fitz.open("annotated.pdf")
all_annots = []

for page_num, page in enumerate(doc):
    for annot in page.annots():
        entry = {
            "page": page_num + 1,
            "type": annot.type[1],          # human-readable type string
            "author": annot.info.get("title", ""),
            "content": annot.info.get("content", ""),
            "rect": list(annot.rect),
            "created": annot.info.get("creationDate", ""),
            "modified": annot.info.get("modDate", ""),
        }
        all_annots.append(entry)

with open("annotations.json", "w") as f:
    json.dump(all_annots, f, indent=2)

print(f"Exported {len(all_annots)} annotations")
```

---

## Delete Specific Annotations

```python
import fitz

doc = fitz.open("annotated.pdf")
page = doc[0]

for annot in page.annots():
    # Delete only highlights
    if annot.type[1] == "Highlight":
        page.delete_annot(annot)

doc.save("cleaned.pdf")
```

---

## Flatten Annotations (Burn In)

Flattening makes annotations permanent (visible in all viewers, not editable).

```python
import fitz

doc = fitz.open("annotated.pdf")

# Flatten all annotations on all pages
for page in doc:
    page.annots()  # load
    # Bake annotations into page content
    page.apply_redactions()   # for redactions
    # For regular annotations, use "to_pdf" with "flatten_annots" option:

doc2 = fitz.open()  # new doc
for page in doc:
    # Render page (including annotations) to pixmap, then insert back
    mat = fitz.Matrix(1, 1)   # 1x scale = 72dpi equivalent
    pix = page.get_pixmap(matrix=mat, alpha=False)
    new_page = doc2.new_page(width=page.rect.width, height=page.rect.height)
    new_page.insert_image(new_page.rect, pixmap=pix)

doc2.save("flattened.pdf")
```
