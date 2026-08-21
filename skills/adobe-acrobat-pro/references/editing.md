# PDF Editing Reference

Covers: text box overlays, headers/footers, page numbering, Bates numbering,
bookmarks/TOC management, and rich PDF creation with reportlab.

---

## Add Headers and Footers

```python
import fitz

def add_header_footer(
    doc: fitz.Document,
    header_text: str = "",
    footer_text: str = "",
    fontname: str = "helv",
    fontsize: float = 10,
    color: tuple = (0.3, 0.3, 0.3),
    margin: float = 30,   # points from edge
):
    """Add header and/or footer to every page."""
    for page in doc:
        w = page.rect.width
        h = page.rect.height

        if header_text:
            # Center at top
            text = header_text.replace("{n}", str(page.number + 1)).replace("{total}", str(doc.page_count))
            tw = fitz.get_text_length(text, fontname=fontname, fontsize=fontsize)
            page.insert_text(
                ((w - tw) / 2, margin),
                text,
                fontname=fontname,
                fontsize=fontsize,
                color=color,
            )

        if footer_text:
            text = footer_text.replace("{n}", str(page.number + 1)).replace("{total}", str(doc.page_count))
            tw = fitz.get_text_length(text, fontname=fontname, fontsize=fontsize)
            page.insert_text(
                ((w - tw) / 2, h - margin + fontsize),
                text,
                fontname=fontname,
                fontsize=fontsize,
                color=color,
            )

    return doc

# Usage
doc = fitz.open("input.pdf")
add_header_footer(
    doc,
    header_text="Confidential — Internal Use Only",
    footer_text="Page {n} of {total}",
)
doc.save("with_header_footer.pdf")
```

---

## Page Numbers Only (Simple)

```python
import fitz

doc = fitz.open("input.pdf")

for page in doc:
    page_num_str = str(page.number + 1)
    w = page.rect.width
    h = page.rect.height
    tw = fitz.get_text_length(page_num_str, fontname="helv", fontsize=10)
    # Bottom-center
    page.insert_text(
        ((w - tw) / 2, h - 20),
        page_num_str,
        fontname="helv",
        fontsize=10,
        color=(0.4, 0.4, 0.4),
    )

doc.save("numbered.pdf")
```

---

## Bates Numbering (Legal)

Bates numbers stamp sequential identifiers on each page (e.g., `CASE-000001`).

```python
import fitz

def apply_bates_numbers(
    doc: fitz.Document,
    prefix: str = "DOC",
    start: int = 1,
    digits: int = 6,
    position: str = "bottom-right",   # "bottom-right", "bottom-left", "top-right", "top-left"
    fontsize: float = 8,
    color: tuple = (0, 0, 0),
    margin: float = 30,
) -> fitz.Document:
    for i, page in enumerate(doc):
        bates = f"{prefix}-{str(start + i).zfill(digits)}"
        tw = fitz.get_text_length(bates, fontname="cour", fontsize=fontsize)
        w, h = page.rect.width, page.rect.height

        pos_map = {
            "bottom-right": (w - tw - margin, h - margin + fontsize),
            "bottom-left":  (margin, h - margin + fontsize),
            "top-right":    (w - tw - margin, margin),
            "top-left":     (margin, margin),
        }
        x, y = pos_map[position]
        page.insert_text((x, y), bates, fontname="cour", fontsize=fontsize, color=color)

    return doc

doc = fitz.open("legal_brief.pdf")
apply_bates_numbers(doc, prefix="SMITH-CASE", start=1, digits=6)
doc.save("bates_stamped.pdf")
```

---

## Bookmarks / Outline / Table of Contents

### Read existing bookmarks

```python
import fitz

doc = fitz.open("document.pdf")
toc = doc.get_toc(simple=True)  # returns [[level, title, page_number], ...]

for level, title, page in toc:
    print(f"{'  ' * (level - 1)}{title} (page {page})")
```

### Add bookmarks

```python
import fitz

doc = fitz.open("document.pdf")

# Format: [level, "Title", page_number (1-indexed), optional_y_position]
new_toc = [
    [1, "Executive Summary", 1],
    [1, "Introduction", 3],
    [2, "Background", 3],
    [2, "Scope", 5],
    [1, "Methodology", 7],
    [2, "Data Collection", 7],
    [2, "Analysis Approach", 9],
    [1, "Results", 11],
    [1, "Conclusion", 18],
    [1, "Appendix", 20],
]
doc.set_toc(new_toc)
doc.save("with_bookmarks.pdf")
```

### Auto-generate TOC from heading detection

```python
import fitz
import re

def auto_generate_toc(doc: fitz.Document) -> list:
    """
    Detect headings by font size and generate a TOC.
    Heuristic: larger text = higher heading level.
    """
    toc = []
    heading_sizes = set()

    # Pass 1: collect all distinct large font sizes
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if b["type"] != 0:
                continue
            for line in b["lines"]:
                for span in line["spans"]:
                    if span["size"] > 11:
                        heading_sizes.add(round(span["size"]))

    if not heading_sizes:
        return toc

    sorted_sizes = sorted(heading_sizes, reverse=True)
    size_to_level = {sz: i + 1 for i, sz in enumerate(sorted_sizes[:3])}  # top 3 → h1/h2/h3

    # Pass 2: build TOC
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if b["type"] != 0:
                continue
            for line in b["lines"]:
                for span in line["spans"]:
                    sz = round(span["size"])
                    if sz in size_to_level:
                        text = span["text"].strip()
                        if text:
                            toc.append([size_to_level[sz], text, page_num + 1])
    return toc

doc = fitz.open("report.pdf")
toc = auto_generate_toc(doc)
doc.set_toc(toc)
doc.save("with_auto_toc.pdf")
```

---

## Insert a Rich Text Box (Multi-line)

```python
import fitz

doc = fitz.open("input.pdf")
page = doc[0]

# Rich text via HTML-like markup in insert_htmlbox (PyMuPDF 1.21+)
rect = fitz.Rect(72, 100, 500, 300)
html = """
<p style="font-family:helvetica; font-size:12pt;">
  <b>Important Notice</b><br/>
  This document contains <i>proprietary information</i>.
  Unauthorized distribution is strictly prohibited.
</p>
"""
page.insert_htmlbox(rect, html, scale_low=0)  # scale_low=0 = don't shrink below page

# Or use textbox for plain multi-line text
rect2 = fitz.Rect(72, 320, 500, 420)
excess = page.insert_textbox(
    rect2,
    "This is a block of wrapped text that will flow within the given rectangle bounds.",
    fontname="helv",
    fontsize=11,
    color=(0, 0, 0),
    align=fitz.TEXT_ALIGN_LEFT,
)
# excess < 0 means text was clipped

doc.save("with_textbox.pdf")
```

---

## Rich PDF Creation with reportlab

Use reportlab when creating documents from scratch with complex layouts.

### Multi-page report with table and image

```python
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    Image, PageBreak, HRFlowable
)

styles = getSampleStyleSheet()
custom_heading = ParagraphStyle(
    "CustomHeading",
    parent=styles["Heading1"],
    fontSize=16,
    textColor=colors.HexColor("#1A3557"),
    spaceAfter=12,
)
custom_body = ParagraphStyle(
    "CustomBody",
    parent=styles["Normal"],
    fontSize=11,
    leading=16,
    spaceAfter=8,
)

doc = SimpleDocTemplate(
    "report.pdf",
    pagesize=letter,
    leftMargin=inch,
    rightMargin=inch,
    topMargin=inch,
    bottomMargin=inch,
)

story = []

# Title page
story.append(Spacer(1, 2 * inch))
story.append(Paragraph("Quarterly Report — Q2 2025", styles["Title"]))
story.append(Spacer(1, 0.3 * inch))
story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#1A3557")))
story.append(PageBreak())

# Section
story.append(Paragraph("Executive Summary", custom_heading))
story.append(Paragraph(
    "Revenue grew 14% year-over-year driven by strong performance in "
    "the enterprise segment and improved retention rates across all tiers.",
    custom_body,
))
story.append(Spacer(1, 0.2 * inch))

# Table
data = [
    ["Segment", "Q2 2024", "Q2 2025", "YoY Growth"],
    ["Enterprise", "$4.2M", "$5.1M", "+21%"],
    ["SMB", "$2.8M", "$3.0M", "+7%"],
    ["Consumer", "$1.1M", "$1.0M", "-9%"],
    ["Total", "$8.1M", "$9.1M", "+12%"],
]
table = Table(data, colWidths=[2.2*inch, 1.2*inch, 1.2*inch, 1.2*inch])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1A3557")),
    ("TEXTCOLOR",  (0, 0), (-1, 0), colors.white),
    ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE",   (0, 0), (-1, -1), 10),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#EEF2F7")]),
    ("GRID",       (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
    ("FONTNAME",   (0, -1), (-1, -1), "Helvetica-Bold"),
    ("ALIGN",      (1, 0), (-1, -1), "CENTER"),
]))
story.append(table)

doc.build(story)
print("report.pdf created")
```

---

## Insert Pages from Another PDF

```python
import fitz

main = fitz.open("main.pdf")
insert_source = fitz.open("appendix.pdf")

# Append all pages of appendix after page 5 (0-indexed position 5)
main.insert_pdf(insert_source, from_page=0, to_page=-1, start_at=5)
# start_at=-1 means append at end

main.save("with_appendix.pdf")
```

## Replace a Page

```python
import fitz

doc = fitz.open("input.pdf")
replacement_src = fitz.open("new_cover.pdf")

# Replace page 0 with the first page of new_cover.pdf
doc.delete_page(0)
doc.insert_pdf(replacement_src, from_page=0, to_page=0, start_at=0)

doc.save("updated.pdf")
```
