# PDF Conversion Reference

Covers: PDF → Word, PDF → Excel, PDF → images, images/HTML → PDF, OCR to searchable PDF.

---

## PDF to Word (.docx)

### Method 1: PyMuPDF + python-docx (best for text-heavy docs)

```bash
pip install pymupdf python-docx --break-system-packages
```

```python
import fitz
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.oxml.ns import qn
import re

def pdf_to_docx(pdf_path: str, docx_path: str):
    doc_in = fitz.open(pdf_path)
    doc_out = Document()

    # Remove default empty paragraph
    for p in doc_out.paragraphs:
        p._element.getparent().remove(p._element)

    for page_num, page in enumerate(doc_in):
        if page_num > 0:
            doc_out.add_page_break()

        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block["type"] != 0:
                continue  # skip image blocks

            for line in block["lines"]:
                para = doc_out.add_paragraph()
                for span in line["spans"]:
                    run = para.add_run(span["text"])
                    run.font.size = Pt(round(span["size"]))
                    run.bold = bool(span["flags"] & 2 ** 4)
                    run.italic = bool(span["flags"] & 2 ** 1)
                    # Color
                    c = span.get("color", 0)
                    r = (c >> 16) & 0xFF
                    g = (c >> 8) & 0xFF
                    b = c & 0xFF
                    run.font.color.rgb = RGBColor(r, g, b)

    doc_out.save(docx_path)
    print(f"Saved: {docx_path}")

pdf_to_docx("input.pdf", "output.docx")
```

### Method 2: pdf2docx (higher fidelity, handles tables and images)

```bash
pip install pdf2docx --break-system-packages
```

```python
from pdf2docx import Converter

def pdf_to_docx_highfidelity(pdf_path: str, docx_path: str, pages: list = None):
    """
    pages=None converts all pages.
    pages=[0, 1, 2] converts first 3 pages only.
    """
    cv = Converter(pdf_path)
    cv.convert(docx_path, pages=pages)
    cv.close()
    print(f"Saved: {docx_path}")

pdf_to_docx_highfidelity("report.pdf", "report.docx")
```

---

## PDF to Excel (.xlsx)

Best for PDFs that contain tables.

```bash
pip install pdfplumber openpyxl --break-system-packages
```

```python
import pdfplumber
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

def pdf_tables_to_excel(pdf_path: str, xlsx_path: str):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)   # remove default sheet

    with pdfplumber.open(pdf_path) as pdf:
        table_count = 0
        for page_num, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            for t_idx, table in enumerate(tables):
                if not table:
                    continue
                table_count += 1
                ws = wb.create_sheet(title=f"P{page_num+1}_T{t_idx+1}")

                for row_idx, row in enumerate(table):
                    for col_idx, cell_val in enumerate(row):
                        cell = ws.cell(row=row_idx + 1, column=col_idx + 1)
                        cell.value = cell_val if cell_val is not None else ""

                        # Style header row
                        if row_idx == 0:
                            cell.font = Font(bold=True, color="FFFFFF")
                            cell.fill = PatternFill("solid", fgColor="1A3557")
                            cell.alignment = Alignment(horizontal="center")

                # Auto-width columns
                for col in ws.columns:
                    max_len = max((len(str(c.value or "")) for c in col), default=0)
                    ws.column_dimensions[col[0].column_letter].width = min(max_len + 4, 50)

    if table_count == 0:
        print("No tables found in PDF.")
        return

    wb.save(xlsx_path)
    print(f"Saved {table_count} table(s) to {xlsx_path}")

pdf_tables_to_excel("financial_report.pdf", "tables.xlsx")
```

---

## PDF to Images (PNG / JPEG)

### All pages to PNG

```python
import fitz
from pathlib import Path

def pdf_to_images(pdf_path: str, output_dir: str, dpi: int = 150, fmt: str = "png"):
    """
    dpi=72  → screen quality (fast)
    dpi=150 → good quality (default)
    dpi=300 → print quality (large files)
    fmt: "png" or "jpeg"
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    mat = fitz.Matrix(dpi / 72, dpi / 72)  # scale factor from 72dpi base

    paths = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=mat, alpha=False)
        out = f"{output_dir}/page_{i+1:03d}.{fmt}"
        if fmt == "jpeg":
            pix.save(out, jpg_quality=90)
        else:
            pix.save(out)
        paths.append(out)
        print(f"Saved page {i+1} → {out}")

    return paths

pdf_to_images("document.pdf", "./pages_output", dpi=150, fmt="png")
```

### Single page to image (thumbnail)

```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]
mat = fitz.Matrix(2, 2)     # 2x = 144dpi
pix = page.get_pixmap(matrix=mat)
pix.save("cover_thumb.png")
```

---

## Images to PDF

### Multiple images → single PDF

```python
import fitz
from pathlib import Path

def images_to_pdf(image_paths: list, output_path: str):
    doc = fitz.open()
    for img_path in sorted(image_paths):
        img = fitz.open(img_path)
        rect = img[0].rect
        pdf_bytes = img.convert_to_pdf()
        img_pdf = fitz.open("pdf", pdf_bytes)
        doc.insert_pdf(img_pdf)

    doc.save(output_path)
    print(f"Saved {len(image_paths)} images → {output_path}")

import glob
images_to_pdf(sorted(glob.glob("scans/*.jpg")), "scanned_doc.pdf")
```

---

## HTML to PDF

```python
import fitz

def html_to_pdf(html_path: str, pdf_path: str):
    """
    Converts a local HTML file (with relative CSS/images) to PDF.
    PyMuPDF handles basic HTML/CSS — for complex layouts, use weasyprint.
    """
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    story = fitz.Story(html=html_content)
    writer = fitz.DocumentWriter(pdf_path)
    mediabox = fitz.paper_rect("letter")
    where = mediabox + (36, 36, -36, -36)  # margins

    more = 1
    while more:
        dev = writer.begin_page(mediabox)
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page()

    writer.close()
    print(f"Saved: {pdf_path}")

html_to_pdf("report.html", "report.pdf")
```

For complex HTML with full CSS support:

```bash
pip install weasyprint --break-system-packages
```

```python
from weasyprint import HTML

HTML(filename="complex_report.html").write_pdf("complex_report.pdf")
# Or from a URL:
HTML(url="https://example.com").write_pdf("example.pdf")
```

---

## OCR: Scanned PDF → Searchable PDF

Adds an invisible text layer over scanned images, making the PDF searchable.

```bash
pip install pytesseract pdf2image pillow --break-system-packages
sudo apt-get install -y tesseract-ocr poppler-utils 2>/dev/null || true
```

### Simple: extract text from scanned PDF

```python
from pdf2image import convert_from_path
import pytesseract

def ocr_pdf_to_text(pdf_path: str, lang: str = "eng") -> str:
    images = convert_from_path(pdf_path, dpi=300)
    full_text = ""
    for i, image in enumerate(images):
        page_text = pytesseract.image_to_string(image, lang=lang)
        full_text += f"\n--- Page {i+1} ---\n{page_text}"
    return full_text

text = ocr_pdf_to_text("scanned.pdf")
print(text[:2000])  # preview
```

### Full: create a searchable PDF (invisible text layer)

```python
import fitz
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import io
import tempfile, os

def pdf_to_searchable_pdf(input_path: str, output_path: str, lang: str = "eng", dpi: int = 300):
    """
    Creates a new PDF where each page is the original scanned image
    with an invisible OCR text layer underneath, making it searchable.
    """
    images = convert_from_path(input_path, dpi=dpi)
    output_doc = fitz.open()

    for i, img in enumerate(images):
        print(f"OCR page {i+1}/{len(images)}...")

        # Get OCR data with bounding boxes
        ocr_data = pytesseract.image_to_data(img, lang=lang, output_type=pytesseract.Output.DICT)

        # Create new PDF page matching image size
        img_w, img_h = img.size
        page_w = img_w * 72 / dpi    # convert pixels to points
        page_h = img_h * 72 / dpi

        page = output_doc.new_page(width=page_w, height=page_h)

        # Insert the original scan as background image
        img_bytes = io.BytesIO()
        img.save(img_bytes, format="JPEG", quality=85)
        img_bytes.seek(0)
        page.insert_image(page.rect, stream=img_bytes.read())

        # Overlay invisible text
        n_words = len(ocr_data["text"])
        for j in range(n_words):
            word = ocr_data["text"][j].strip()
            conf = int(ocr_data["conf"][j])
            if not word or conf < 30:
                continue

            # Pixel bounding box → page points
            x0 = ocr_data["left"][j] * 72 / dpi
            y0 = ocr_data["top"][j] * 72 / dpi
            x1 = x0 + ocr_data["width"][j] * 72 / dpi
            y1 = y0 + ocr_data["height"][j] * 72 / dpi
            font_size = max(1, (y1 - y0) * 0.8)

            page.insert_text(
                (x0, y1),
                word,
                fontname="helv",
                fontsize=font_size,
                color=(1, 1, 1, 0),    # invisible (white + 0 opacity)
                render_mode=3,          # invisible text
            )

    output_doc.save(output_path, garbage=4, deflate=True)
    print(f"Searchable PDF saved: {output_path}")

pdf_to_searchable_pdf("scanned_document.pdf", "searchable_document.pdf")
```

### OCR with language options

```python
# Common language codes
# eng = English, fra = French, deu = German, spa = Spanish
# chi_sim = Chinese Simplified, chi_tra = Chinese Traditional
# jpn = Japanese, kor = Korean, ara = Arabic, rus = Russian

text = pytesseract.image_to_string(image, lang="eng+fra")  # multi-language
```

---

## Markdown / Text to PDF

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import re

def text_to_pdf(text: str, output_path: str):
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                             leftMargin=inch, rightMargin=inch,
                             topMargin=inch, bottomMargin=inch)
    styles = getSampleStyleSheet()
    story = []

    for line in text.split("\n"):
        line = line.rstrip()
        if line.startswith("# "):
            story.append(Paragraph(line[2:], styles["Heading1"]))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:], styles["Heading2"]))
        elif line.startswith("### "):
            story.append(Paragraph(line[4:], styles["Heading3"]))
        elif line.startswith("---"):
            story.append(HRFlowable(width="100%"))
        elif line == "":
            story.append(Spacer(1, 0.15 * inch))
        else:
            # Convert **bold** and *italic* markdown
            line = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", line)
            line = re.sub(r"\*(.+?)\*", r"<i>\1</i>", line)
            story.append(Paragraph(line, styles["Normal"]))

    doc.build(story)
    print(f"Saved: {output_path}")
```
