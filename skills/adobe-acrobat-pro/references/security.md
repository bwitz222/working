# PDF Security Reference

Covers: permanent redaction, digital signatures, certificate encryption, permission matrix.

---

## Redaction (Permanent Removal of Sensitive Content)

Redaction in Acrobat = permanently remove text/images from the document.
Two-step process in PyMuPDF: (1) mark redaction areas, (2) apply (burns in black boxes).

### Redact by search term

```python
import fitz

def redact_by_search(doc: fitz.Document, terms: list, fill_color=(0, 0, 0)) -> int:
    """
    Search for terms and redact all matches.
    Returns total number of redactions applied.
    """
    total = 0
    for page in doc:
        for term in terms:
            matches = page.search_for(term)
            for rect in matches:
                # Expand rect slightly for visual coverage
                page.add_redact_annot(rect, fill=fill_color)
                total += 1

        # Commit redactions on this page
        page.apply_redactions()

    return total

doc = fitz.open("sensitive_document.pdf")

# Redact SSNs, phone numbers, emails
import re

def redact_by_regex(doc: fitz.Document, pattern: str, fill_color=(0, 0, 0)) -> int:
    """Search text by regex and redact matching positions."""
    total = 0
    regex = re.compile(pattern)

    for page in doc:
        page_text = page.get_text("text")
        # find all matches; then search_for each unique hit
        matches = set(regex.findall(page_text))
        for match in matches:
            for rect in page.search_for(match):
                page.add_redact_annot(rect, fill=fill_color)
                total += 1
        page.apply_redactions()

    return total

# Common PII patterns
SSN_PATTERN     = r"\b\d{3}-\d{2}-\d{4}\b"
PHONE_PATTERN   = r"\b(?:\+1\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b"
EMAIL_PATTERN   = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
CREDIT_PATTERN  = r"\b(?:\d{4}[\s-]?){3}\d{4}\b"

doc = fitz.open("report_with_pii.pdf")
n = redact_by_regex(doc, EMAIL_PATTERN)
print(f"Redacted {n} email addresses")
doc.save("redacted.pdf", garbage=4, clean=True)
```

### Redact a rectangular region manually

```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]

# Specify region to redact (x0, y0, x1, y1) in points
rect = fitz.Rect(72, 150, 400, 190)

# Optional: "text" parameter adds replacement text over black box
page.add_redact_annot(rect, text="[REDACTED]", fill=(0, 0, 0),
                      fontname="helv", fontsize=10,
                      text_color=(1, 1, 1))
page.apply_redactions()
doc.save("redacted.pdf")
```

### Redact images on a page

```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]

# Get all image positions on the page
for img_info in page.get_image_info():
    bbox = img_info["bbox"]   # (x0, y0, x1, y1)
    rect = fitz.Rect(bbox)
    page.add_redact_annot(rect)

page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_REMOVE)  # also remove embedded image data
doc.save("images_redacted.pdf")
```

> **Critical**: After `apply_redactions()`, the content is permanently gone.
> Always save to a NEW file. Never overwrite the original.

---

## Permissions Reference

Combine flags with bitwise OR when calling `doc.save(permissions=...)`.

```python
import fitz

# Full permissions
FULL = (
    fitz.PDF_PERM_PRINT          |   # printing allowed
    fitz.PDF_PERM_PRINT_HQ       |   # high-quality printing
    fitz.PDF_PERM_COPY           |   # copy/paste text
    fitz.PDF_PERM_ANNOTATE       |   # add/modify annotations
    fitz.PDF_PERM_FORM           |   # fill form fields
    fitz.PDF_PERM_ASSEMBLE       |   # insert/delete/rotate pages
    fitz.PDF_PERM_MODIFY         |   # modify content
    fitz.PDF_PERM_ACCESSIBILITY  |   # accessibility tools access
)

# Read-only (view only, no print, no copy)
VIEW_ONLY = fitz.PDF_PERM_ACCESSIBILITY   # minimum useful set

# Print-only (common for invoices)
PRINT_ONLY = fitz.PDF_PERM_PRINT | fitz.PDF_PERM_PRINT_HQ | fitz.PDF_PERM_ACCESSIBILITY

# Comment-only (reviewers can annotate but not edit content)
REVIEW = fitz.PDF_PERM_ANNOTATE | fitz.PDF_PERM_FORM | fitz.PDF_PERM_ACCESSIBILITY

# Apply
doc = fitz.open("input.pdf")
doc.save(
    "protected.pdf",
    encryption=fitz.PDF_ENCRYPT_AES_256,
    user_pw="viewpassword",
    owner_pw="adminpassword",
    permissions=PRINT_ONLY,
)
```

### Encryption levels

| Constant | Algorithm | Notes |
|----------|-----------|-------|
| `PDF_ENCRYPT_NONE` | — | Remove encryption |
| `PDF_ENCRYPT_RC4_40` | RC4 40-bit | Weak, avoid |
| `PDF_ENCRYPT_RC4_128` | RC4 128-bit | Legacy only |
| `PDF_ENCRYPT_AES_128` | AES 128-bit | Good |
| `PDF_ENCRYPT_AES_256` | AES 256-bit | Best, use this |

---

## Digital Signatures

PyMuPDF can create unsigned signature fields; signing with a real certificate
requires `pyhanko`.

### Add a signature field (unsigned placeholder)

```python
import fitz

doc = fitz.open("contract.pdf")
page = doc[-1]  # last page

# Add a visible signature field widget
widget = fitz.Widget()
widget.rect = fitz.Rect(100, 700, 400, 760)
widget.field_type = fitz.PDF_WIDGET_TYPE_SIGNATURE
widget.field_name = "SignatureField1"
widget.field_label = "Sign here"
widget.border_color = (0, 0, 0)
widget.border_width = 1
widget.fill_color = (0.95, 0.95, 1.0)
page.add_widget(widget)

doc.save("with_signature_field.pdf")
```

### Sign with a certificate (pyhanko)

```bash
pip install pyhanko pyhanko-certvalidator --break-system-packages
# Generate a test certificate (self-signed, for testing only):
# openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes
```

```python
from pyhanko.sign import signers, fields
from pyhanko.sign.fields import SigFieldSpec
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign.signers.pdf_signer import PdfSignatureMetadata
import getpass

# Load PKCS12 certificate (.pfx / .p12 file)
# For PEM (cert.pem + key.pem):
signer = signers.SimpleSigner.load(
    "key.pem",
    "cert.pem",
    ca_chain_files=["ca.pem"],   # optional chain
    key_passphrase=None,         # or b"your_passphrase"
)

# Sign the PDF
with open("contract.pdf", "rb") as inf:
    writer = IncrementalPdfFileWriter(inf)

    # Add signature field if not present
    fields.append_signature_field(
        writer,
        sig_field_spec=SigFieldSpec(
            sig_field_name="Signature1",
            on_page=0,
            box=(100, 700, 400, 760),
        )
    )

    meta = PdfSignatureMetadata(
        field_name="Signature1",
        reason="I approve this document",
        location="New York, NY",
        name="Jane Smith",
    )

    with open("signed_contract.pdf", "wb") as outf:
        signers.sign_pdf(
            writer,
            signature_meta=meta,
            signer=signer,
            output=outf,
        )

print("Document signed successfully.")
```

### Verify a signature

```python
from pyhanko.sign.validation import validate_pdf_signature
from pyhanko.pdf_utils.reader import PdfFileReader

with open("signed_contract.pdf", "rb") as f:
    r = PdfFileReader(f)
    sigs = r.embedded_signatures
    for sig in sigs:
        status = validate_pdf_signature(sig)
        print(f"Signature: {sig.field_name}")
        print(f"  Valid:     {status.valid}")
        print(f"  Intact:    {status.intact}")
        print(f"  Signer:    {status.signing_cert.subject.human_friendly}")
        print(f"  Timestamp: {status.signer_reported_dt}")
```

---

## Watermark (Diagonal, Transparent)

```python
import fitz

def add_watermark(doc: fitz.Document, text: str, opacity: float = 0.15) -> fitz.Document:
    for page in doc:
        # Use a shape layer for transparent watermark
        shape = page.new_shape()
        w, h = page.rect.width, page.rect.height

        # Draw diagonal text across full page
        shape.insert_text(
            fitz.Point(w * 0.1, h * 0.6),
            text,
            fontname="helv",
            fontsize=72,
            rotate=45,
            color=(0.7, 0.7, 0.7),    # light gray
            fill=(0.7, 0.7, 0.7),
        )
        shape.commit(overlay=False)    # overlay=False = draw under content

    return doc

doc = fitz.open("input.pdf")
add_watermark(doc, "CONFIDENTIAL")
doc.save("watermarked.pdf")
```

---

## Certificate-Based Encryption (Public Key)

For encrypting so that only specific recipients (by their certificate) can open:

```python
# This requires PDF_ENCRYPT_AES_256 + recipient certificate
# Beyond scope of most use cases — use password encryption for normal needs.
# For enterprise use, consult pyhanko documentation.
```
