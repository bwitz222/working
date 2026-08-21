---
name: adobe-acrobat-pro
description: >
  Full-featured PDF suite replicating Adobe Acrobat Pro, including a LIVE
  BROWSER-BASED PDF EDITOR (highlight, text, shapes, freehand draw, erase,
  multi-page, zoom, download with annotations baked in — launch it with
  show_widget using assets/live-editor.html). Also covers: PDF creation,
  merge/split/rotate/reorder pages, text and image overlays, annotations,
  redaction, digital signatures, password protection, OCR on scanned documents,
  PDF comparison (visual diff), compression/optimization, format conversion
  (PDF to Word, Excel, images; HTML to PDF), Bates numbering, bookmarks/TOC,
  headers/footers, PDF/A compliance, and batch processing. Trigger on ANY of:
  editing a PDF live, annotating, redacting, signing, compressing, comparing,
  converting to/from PDF, stamping, page numbers, bookmarks, or accessibility.
  Always prefer over the basic pdf or pdf-reading skills for modification,
  annotation, conversion, or any interactive PDF editing request.
---

# Adobe Acrobat Pro — PDF Skill

## Live Browser Editor

When the user wants to **visually edit a PDF right now** (annotate, highlight,
draw, add text, then download), launch the live editor using `show_widget`.

**Triggers:** "open the PDF editor", "edit this PDF live", "annotate my PDF",
"I want to highlight things", "launch the editor", or any request for an
interactive/visual editing experience.

**How to launch:**

1. Read `assets/live-editor.html` from this skill's directory.
2. Pass the full file contents as `widget_code` to `show_widget`.
3. Use loading messages like: `["Loading PDF engine…", "Wiring up tools…", "Prepping the canvas…"]`
4. Set `title` to `pdf_live_editor`.

The editor is fully self-contained (loads PDF.js + pdf-lib from CDN). The user
drops or uploads a PDF, annotates it with the toolbar, then clicks the download
button to save the annotated PDF back to their computer.

**Editor capabilities:**
- Highlight (drag to paint semi-transparent color over any region)
- Text (click to place typed label anywhere on the page)
- Rectangle (drag to draw a border box)
- Freehand draw (pencil strokes)
- Erase (click any annotation to remove it)
- 5 color swatches: yellow, red, blue, green, black
- Undo
- Multi-page navigation
- Zoom in/out
- Download — annotations are coordinate-mapped and baked permanently into the PDF

---

## Primary Library: PyMuPDF

PyMuPDF (`fitz`) is the workhorse for 90% of Acrobat-equivalent tasks. It is
faster and more capable than pypdf for editing, rendering, and annotations.

```bash
pip install pymupdf --break-system-packages       # PyMuPDF (fitz)
pip install pypdf --break-system-packages          # fallback for some form ops
pip install reportlab --break-system-packages      # rich PDF creation from scratch
pip install pdfplumber --break-system-packages     # table extraction
pip install pillow --break-system-packages         # image support
pip install pdf2image pytesseract --break-system-packages  # OCR pipeline
```

---

## Task Router

| Task | Reference | Key Library |
|------|-----------|-------------|
| **Live in-browser PDF editor** | [Live Editor](#live-browser-editor) — read `assets/live-editor.html` and call `show_widget` | PDF.js + pdf-lib |
| Merge, split, rotate, reorder pages | [Core ops](#core-operations) | PyMuPDF |
| Add text / image overlays | [Core ops](#core-operations) | PyMuPDF |
| Highlights, comments, sticky notes, shapes | [annotations.md](references/annotations.md) | PyMuPDF |
| Redact sensitive content permanently | [security.md](references/security.md) | PyMuPDF |
| Password-protect with permissions | [security.md](references/security.md) | PyMuPDF |
| Digital signatures | [security.md](references/security.md) | pyhanko |
| PDF comparison (visual diff) | [advanced.md](references/advanced.md) | PyMuPDF |
| Compress / optimize file size | [advanced.md](references/advanced.md) | PyMuPDF |
| Bates numbering, headers, footers | [editing.md](references/editing.md) | PyMuPDF |
| Bookmarks / table of contents | [editing.md](references/editing.md) | PyMuPDF |
| Create PDF from scratch (rich layout) | [editing.md](references/editing.md) | reportlab |
| PDF to Word (.docx) | [conversion.md](references/conversion.md) | PyMuPDF + python-docx |
| PDF to Excel (.xlsx) | [conversion.md](references/conversion.md) | pdfplumber + openpyxl |
| PDF to images (PNG/JPEG) | [conversion.md](references/conversion.md) | PyMuPDF |
| Images / HTML to PDF | [conversion.md](references/conversion.md) | PyMuPDF / reportlab |
| OCR scanned PDFs (make searchable) | [conversion.md](references/conversion.md) | pytesseract |
| PDF/A archival compliance | [advanced.md](references/advanced.md) | PyMuPDF |
| Accessibility (tagged PDF, reading order) | [advanced.md](references/advanced.md) | PyMuPDF |
| Batch processing multiple PDFs | [advanced.md](references/advanced.md) | PyMuPDF |
| Fill interactive forms | [Core ops](#core-operations) | PyMuPDF / pypdf |
| Extract tables | [Core ops](#core-operations) | pdfplumber |

---

## Core Operations

### Open and inspect a PDF

```python
import fitz  # PyMuPDF

doc = fitz.open("document.pdf")
print(f"Pages:    {doc.page_count}")
print(f"Metadata: {doc.metadata}")
print(f"Encrypted: {doc.is_encrypted}")
print(f"Form fields: {doc.is_form_pdf}")

# Check bookmarks (outline/TOC)
toc = doc.get_toc()
for level, title, page in toc:
    print(f"{'  ' * (level-1)}{title} → page {page}")
```

### Merge PDFs

```python
import fitz

merged = fitz.open()
for path in ["part1.pdf", "part2.pdf", "part3.pdf"]:
    src = fitz.open(path)
    merged.insert_pdf(src)
    src.close()

merged.save("merged.pdf")
merged.close()
```

### Split PDF — by page range

```python
import fitz

doc = fitz.open("input.pdf")

# Extract pages 1-5 (0-indexed: 0-4)
part = fitz.open()
part.insert_pdf(doc, from_page=0, to_page=4)
part.save("pages_1_to_5.pdf")

# Extract specific pages list
selection = fitz.open()
for page_num in [0, 2, 5, 9]:  # 0-indexed
    selection.insert_pdf(doc, from_page=page_num, to_page=page_num)
selection.save("selected_pages.pdf")
```

### Rotate pages

```python
import fitz

doc = fitz.open("input.pdf")

# Rotate all pages 90° clockwise
for page in doc:
    page.set_rotation(90)   # absolute: 0, 90, 180, 270

# Or rotate a specific page
doc[0].set_rotation(180)

doc.save("rotated.pdf")
```

### Reorder pages (drag-and-drop equivalent)

```python
import fitz

doc = fitz.open("input.pdf")

# New order: move page 0 to end, reverse a 5-page doc, etc.
# select() takes a list of 0-based page indices in the new order
new_order = [2, 0, 1, 4, 3]
doc.select(new_order)
doc.save("reordered.pdf")
```

### Delete pages

```python
doc.delete_pages([0, 2, 5])   # list of 0-based page indices
doc.save("trimmed.pdf")
```

### Add text overlay (stamp / annotation text)

```python
import fitz

doc = fitz.open("input.pdf")
page = doc[0]

# Insert text at position (x, y) from top-left
page.insert_text(
    (72, 100),               # x, y in points (72pt = 1 inch)
    "CONFIDENTIAL",
    fontname="helv",         # built-in: helv, times, courier, symbol, zapf
    fontsize=24,
    color=(1, 0, 0),         # RGB 0-1 scale
    rotate=45,               # degrees counter-clockwise
)
doc.save("stamped.pdf")
```

### Insert image onto a page

```python
import fitz

doc = fitz.open("input.pdf")
page = doc[0]

# Define placement rectangle (x0, y0, x1, y1) in points
rect = fitz.Rect(50, 50, 250, 150)
page.insert_image(rect, filename="logo.png")

doc.save("with_image.pdf")
```

### Extract text (layout-aware)

```python
import fitz

doc = fitz.open("document.pdf")
for i, page in enumerate(doc):
    # "text" = plain text, "blocks" = structured blocks with positions
    text = page.get_text("text")
    print(f"--- Page {i+1} ---")
    print(text)
```

### Extract tables (pdfplumber)

```python
import pdfplumber
import pandas as pd

with pdfplumber.open("document.pdf") as pdf:
    all_dfs = []
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        for j, table in enumerate(tables):
            df = pd.DataFrame(table[1:], columns=table[0])
            all_dfs.append(df)
            df.to_csv(f"table_p{i+1}_t{j+1}.csv", index=False)
```

### Fill interactive form fields

```python
import fitz

doc = fitz.open("form.pdf")

# List all fields
for page in doc:
    for widget in page.widgets():
        print(f"Field: {widget.field_name!r}  Type: {widget.field_type_string}")

# Fill fields
for page in doc:
    for widget in page.widgets():
        if widget.field_name == "FirstName":
            widget.field_value = "Jane"
            widget.update()
        elif widget.field_name == "SignedCheckbox":
            widget.field_value = True
            widget.update()

doc.save("filled_form.pdf")
```

### Password-protect (open password)

```python
import fitz

doc = fitz.open("input.pdf")
doc.save(
    "protected.pdf",
    encryption=fitz.PDF_ENCRYPT_AES_256,
    user_pw="openme",          # password to open
    owner_pw="adminpassword",  # password to change permissions
    permissions=fitz.PDF_PERM_PRINT | fitz.PDF_PERM_COPY,
)
```

Permission flags (combine with `|`):
- `PDF_PERM_PRINT` — allow printing
- `PDF_PERM_COPY` — allow copy/paste
- `PDF_PERM_ANNOTATE` — allow annotations
- `PDF_PERM_FORM` — allow form filling
- `PDF_PERM_MODIFY` — allow modifications

### Decrypt / remove password

```python
import fitz

doc = fitz.open("encrypted.pdf")
if doc.is_encrypted:
    doc.authenticate("the_password")

doc.save("decrypted.pdf", encryption=fitz.PDF_ENCRYPT_NONE)
```

---

## Reference Files

Read the relevant reference file for advanced operations:

- **[references/annotations.md](references/annotations.md)** — Highlights, sticky notes,
  freehand ink, shape overlays, stamps, comment threads
- **[references/editing.md](references/editing.md)** — Rich text boxes, headers/footers,
  page numbering, Bates numbering, bookmarks, TOC, reportlab creation
- **[references/conversion.md](references/conversion.md)** — PDF↔Word, PDF↔Excel,
  PDF↔images, HTML→PDF, OCR to searchable PDF
- **[references/security.md](references/security.md)** — Redaction, digital signatures,
  certificate-based encryption, permission details
- **[references/advanced.md](references/advanced.md)** — PDF comparison, compression,
  batch processing, PDF/A compliance, accessibility

---

## Quick Diagnostic: Which approach to use?

```
Is the PDF scanned (no text layer)?
  YES → Use OCR pipeline (see conversion.md)
  NO  ↓

Do you need to modify content?
  Add overlays/stamps  → Core ops above (insert_text, insert_image)
  Add annotations      → annotations.md
  Edit existing text   → editing.md (text box overlays; true in-place edit is rare)
  Redact               → security.md

Do you need conversion?
  → conversion.md

Do you need to compare two PDFs?
  → advanced.md
```
