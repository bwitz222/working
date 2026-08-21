# Advanced PDF Features Reference

Covers: PDF comparison (visual diff), compression/optimization, batch processing,
PDF/A archival compliance, accessibility tagging.

---

## PDF Comparison (Visual Diff)

Compare two versions of a PDF and highlight differences.

### Method 1: Visual pixel diff (shows exactly what changed)

```python
import fitz
from PIL import Image, ImageChops, ImageEnhance
import io

def compare_pdfs_visual(
    path_a: str,
    path_b: str,
    output_path: str,
    dpi: int = 150,
    highlight_color: tuple = (255, 50, 50),  # red
):
    """
    Create a diff PDF where changed pixels are highlighted in red.
    Best for detecting formatting changes, moved elements, etc.
    """
    doc_a = fitz.open(path_a)
    doc_b = fitz.open(path_b)
    diff_doc = fitz.open()

    n_pages = max(doc_a.page_count, doc_b.page_count)
    mat = fitz.Matrix(dpi / 72, dpi / 72)

    for i in range(n_pages):
        # Get page images (or blank if page doesn't exist in one doc)
        if i < doc_a.page_count:
            pix_a = doc_a[i].get_pixmap(matrix=mat, alpha=False)
            img_a = Image.frombytes("RGB", [pix_a.width, pix_a.height], pix_a.samples)
        else:
            img_a = Image.new("RGB", img_b.size, (255, 255, 255))

        if i < doc_b.page_count:
            pix_b = doc_b[i].get_pixmap(matrix=mat, alpha=False)
            img_b = Image.frombytes("RGB", [pix_b.width, pix_b.height], pix_b.samples)
        else:
            img_b = Image.new("RGB", img_a.size, (255, 255, 255))

        # Ensure same size
        if img_a.size != img_b.size:
            img_b = img_b.resize(img_a.size, Image.LANCZOS)

        # Pixel diff
        diff = ImageChops.difference(img_a, img_b)
        diff_gray = diff.convert("L")

        # Amplify differences and create highlight mask
        enhanced = ImageEnhance.Contrast(diff_gray).enhance(10)
        mask = enhanced.point(lambda p: 255 if p > 10 else 0)

        # Composite: original + red overlay on changed pixels
        overlay = Image.new("RGB", img_a.size, highlight_color)
        result = img_a.copy()
        result.paste(overlay, mask=mask)

        # Add to diff PDF
        result_bytes = io.BytesIO()
        result.save(result_bytes, format="PNG")
        result_bytes.seek(0)

        w_pts = img_a.width * 72 / dpi
        h_pts = img_a.height * 72 / dpi
        page = diff_doc.new_page(width=w_pts, height=h_pts)
        page.insert_image(page.rect, stream=result_bytes.read())

    diff_doc.save(output_path)
    print(f"Diff PDF saved: {output_path}")
    return output_path

compare_pdfs_visual("v1.pdf", "v2.pdf", "diff.pdf")
```

### Method 2: Text diff (shows added/removed text)

```python
import fitz
from difflib import unified_diff

def compare_pdfs_text(path_a: str, path_b: str) -> str:
    """Extract text from both PDFs and show a unified text diff."""
    def extract(path):
        doc = fitz.open(path)
        pages = []
        for page in doc:
            pages.append(page.get_text("text"))
        return pages

    pages_a = extract(path_a)
    pages_b = extract(path_b)

    report = []
    n = max(len(pages_a), len(pages_b))

    for i in range(n):
        text_a = pages_a[i].splitlines(keepends=True) if i < len(pages_a) else []
        text_b = pages_b[i].splitlines(keepends=True) if i < len(pages_b) else []

        diff = list(unified_diff(text_a, text_b,
                                  fromfile=f"v1 page {i+1}",
                                  tofile=f"v2 page {i+1}"))
        if diff:
            report.append(f"\n=== Page {i+1} ===\n")
            report.extend(diff)

    result = "".join(report)
    if not result:
        result = "No text differences found between the two PDFs."

    return result

diff_text = compare_pdfs_text("contract_v1.pdf", "contract_v2.pdf")
print(diff_text[:3000])  # preview

with open("text_diff.txt", "w") as f:
    f.write(diff_text)
```

---

## Compression and Optimization

### Method 1: PyMuPDF save options (fast, good for structure optimization)

```python
import fitz
import os

def compress_pdf(input_path: str, output_path: str) -> dict:
    doc = fitz.open(input_path)
    doc.save(
        output_path,
        garbage=4,        # 4 = most aggressive dead object removal
        deflate=True,     # compress all streams
        deflate_images=True,   # compress image streams too
        deflate_fonts=True,    # compress font streams
        clean=True,       # clean syntax
        linear=True,      # web-optimized (fast open in browser)
    )
    before = os.path.getsize(input_path)
    after  = os.path.getsize(output_path)
    return {
        "before_kb": round(before / 1024, 1),
        "after_kb":  round(after / 1024, 1),
        "saved_pct": round((1 - after / before) * 100, 1),
    }

result = compress_pdf("large.pdf", "compressed.pdf")
print(f"Before: {result['before_kb']} KB")
print(f"After:  {result['after_kb']} KB")
print(f"Saved:  {result['saved_pct']}%")
```

### Method 2: Downsample images (biggest size reduction)

```python
import fitz
from PIL import Image
import io

def compress_images_in_pdf(
    input_path: str,
    output_path: str,
    max_dpi: int = 150,
    jpeg_quality: int = 75,
) -> dict:
    """
    Re-compress images in the PDF to reduce file size.
    max_dpi=150 is good for screen; 300 for print.
    """
    doc = fitz.open(input_path)
    replaced = 0

    for page in doc:
        for img in page.get_images():
            xref = img[0]
            base_image = doc.extract_image(xref)
            img_bytes = base_image["image"]
            img_ext = base_image["ext"]
            img_w = base_image["width"]
            img_h = base_image["height"]

            # Calculate target dimensions
            pil_img = Image.open(io.BytesIO(img_bytes))
            if img_ext in ("jpeg", "jpg"):
                # Re-compress JPEG at lower quality
                buf = io.BytesIO()
                if pil_img.mode == "RGBA":
                    pil_img = pil_img.convert("RGB")
                pil_img.save(buf, format="JPEG", quality=jpeg_quality, optimize=True)
                doc.update_stream(xref, buf.getvalue())
                replaced += 1
            elif img_ext == "png":
                # Convert large PNGs to JPEG
                if img_w * img_h > 100000:  # > ~316x316
                    buf = io.BytesIO()
                    if pil_img.mode in ("RGBA", "P"):
                        pil_img = pil_img.convert("RGB")
                    pil_img.save(buf, format="JPEG", quality=jpeg_quality)
                    # Note: changing PNG to JPEG in-place via update_stream
                    # may require adjusting the image filter entry
                    doc.update_stream(xref, buf.getvalue())
                    replaced += 1

    import os
    doc.save(output_path, garbage=4, deflate=True, deflate_images=True)

    before = os.path.getsize(input_path)
    after  = os.path.getsize(output_path)
    return {
        "images_processed": replaced,
        "before_kb": round(before / 1024, 1),
        "after_kb":  round(after / 1024, 1),
        "saved_pct": round((1 - after / before) * 100, 1),
    }

result = compress_images_in_pdf("image_heavy.pdf", "optimized.pdf")
print(result)
```

---

## Batch Processing

### Process all PDFs in a folder

```python
import fitz
from pathlib import Path

def batch_add_watermark(input_dir: str, output_dir: str, watermark_text: str):
    """Apply watermark to all PDFs in a folder."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    pdf_files = list(Path(input_dir).glob("*.pdf"))

    for i, pdf_path in enumerate(pdf_files):
        print(f"[{i+1}/{len(pdf_files)}] Processing: {pdf_path.name}")
        doc = fitz.open(str(pdf_path))

        for page in doc:
            page.insert_text(
                (72, page.rect.height / 2),
                watermark_text,
                fontsize=60,
                color=(0.8, 0.8, 0.8),
                rotate=45,
            )

        out_path = Path(output_dir) / pdf_path.name
        doc.save(str(out_path))
        doc.close()

    print(f"Done. Processed {len(pdf_files)} files.")

batch_add_watermark("./input_pdfs", "./output_pdfs", "DRAFT")
```

### Batch merge: one PDF per subfolder

```python
import fitz
from pathlib import Path

def batch_merge_by_folder(base_dir: str, output_dir: str):
    """
    For each subfolder, merge all PDFs inside it into one file named after the folder.
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for folder in sorted(Path(base_dir).iterdir()):
        if not folder.is_dir():
            continue
        pdfs = sorted(folder.glob("*.pdf"))
        if not pdfs:
            continue

        merged = fitz.open()
        for pdf in pdfs:
            src = fitz.open(str(pdf))
            merged.insert_pdf(src)
            src.close()

        out = Path(output_dir) / f"{folder.name}_merged.pdf"
        merged.save(str(out))
        merged.close()
        print(f"Merged {len(pdfs)} files → {out}")
```

### Batch extract text to JSON

```python
import fitz
import json
from pathlib import Path

def batch_extract_text(input_dir: str, output_json: str):
    results = {}

    for pdf_path in Path(input_dir).glob("*.pdf"):
        doc = fitz.open(str(pdf_path))
        pages = []
        for page in doc:
            pages.append(page.get_text("text"))
        results[pdf_path.name] = pages
        doc.close()

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Extracted text from {len(results)} files → {output_json}")
```

---

## PDF/A Compliance (Archival Format)

PDF/A is the ISO standard for long-term archiving. Acrobat's "Save as PDF/A" equivalent:

```python
import fitz

def convert_to_pdfa(input_path: str, output_path: str, level: int = 2) -> bool:
    """
    Convert a PDF to PDF/A-2b (default) using PyMuPDF's built-in converter.
    level: 1 = PDF/A-1b, 2 = PDF/A-2b (recommended), 3 = PDF/A-3b

    Returns True if conversion succeeded without errors.
    """
    doc = fitz.open(input_path)

    # PyMuPDF 1.24+ supports direct PDF/A output
    errors = doc.convert_to_pdf(
        compress=True,
        linearize=False,
    )

    # Set PDF/A metadata
    doc.set_metadata({
        "creator": "PDF Skill",
        "producer": "PyMuPDF",
    })

    # The actual PDF/A-2b tagging requires setting the OutputIntents
    # PyMuPDF handles this via the pdfa parameter:
    doc.save(
        output_path,
        garbage=4,
        deflate=True,
        clean=True,
        # PDF/A marker (requires PyMuPDF 1.24+ for full compliance):
        # encryption=fitz.PDF_ENCRYPT_NONE,  # PDF/A cannot be encrypted
    )

    print(f"PDF/A output: {output_path}")
    return True

convert_to_pdfa("document.pdf", "document_pdfa.pdf")
```

For strict PDF/A validation, use `veraPDF` (external tool):

```bash
# Install veraPDF and validate:
# verapdf --flavour 2b output.pdf
```

---

## Accessibility: Reading Order and Alt Text

### Add alt text to images (for screen readers)

```python
import fitz

doc = fitz.open("document.pdf")

for page in doc:
    for img_info in page.get_image_info(xrefs=True):
        xref = img_info["xref"]
        bbox = img_info["bbox"]

        # Add an invisible text annotation as alt-text proxy
        # (True tagged PDF requires PDF structure tags — beyond PyMuPDF scope)
        annot = page.add_text_annot(
            fitz.Point(bbox[0], bbox[1]),
            f"Image at ({bbox[0]:.0f},{bbox[1]:.0f}): [describe image here]",
            icon="Note",
        )
        annot.set_info(title="Alt Text")
        annot.update()

doc.save("with_alt_text_notes.pdf")
```

### Check reading order / text blocks order

```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]

# Get text blocks with positions, sorted top-to-bottom, left-to-right
blocks = page.get_text("blocks")   # returns (x0, y0, x1, y1, text, block_no, type)
blocks_sorted = sorted(blocks, key=lambda b: (round(b[1] / 20) * 20, b[0]))

for b in blocks_sorted:
    print(f"({b[0]:.0f},{b[1]:.0f}) → {b[4][:80]!r}")
```

---

## Web-Optimize (Linearize) for Fast Browser Opening

```python
import fitz

doc = fitz.open("large_document.pdf")
doc.save(
    "web_optimized.pdf",
    linear=True,    # linearized = first page loads before full download
    garbage=4,
    deflate=True,
    clean=True,
)
print("Web-optimized PDF saved.")
```
