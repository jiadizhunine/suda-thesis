# Format Standards — Python Code Reference

This file contains all Python formatting code for generating Suzhou University thesis
documents with python-docx. Read this file when writing formatting functions for any
document type.

## Table of Contents

1. [Required Imports](#1-required-imports)
2. [Page Setup](#2-page-setup)
3. [Header and Footer](#3-header-and-footer)
4. [Font Configuration](#4-font-configuration)
5. [Style Definitions](#5-style-definitions)
6. [Body Paragraph Format](#6-body-paragraph-format)
7. [Figure Insertion](#7-figure-insertion)
8. [Table of Contents (TOC)](#8-table-of-contents)
9. [Bookmark System](#9-bookmark-system)
10. [Citation System](#10-citation-system)
11. [References Section](#11-references-section)
12. [Metadata Erasure](#12-metadata-erasure)

---

## 1. Required Imports

```python
import sys, os, re, datetime
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
from docx.opc.constants import RELATIONSHIP_TYPE as RT
import lxml.etree as etree
```

## 2. Page Setup

```python
# Paper: A4
section.page_width = Cm(21)
section.page_height = Cm(29.7)

# Margins (thesis body, literature review, and literature translation)
MARGIN_TOP = Cm(3.3)
MARGIN_BOTTOM = Cm(2.7)
MARGIN_LEFT = Cm(2.5)
MARGIN_RIGHT = Cm(2.5)
GUTTER = Cm(0.5)  # binding margin, left side
HEADER_DISTANCE = Cm(2.6)
FOOTER_DISTANCE = Cm(2.0)

# Gutter requires XML-level operation:
sectPr = section._sectPr
pgMar = sectPr.find(qn('w:pgMar'))
if pgMar is not None:
    pgMar.set(qn('w:gutter'), str(int(GUTTER.emu / 635)))
```

Task book and midterm-check forms are table/form documents and may use their official
sample margins when provided by the user. If no official sample is provided, use A4 with
2.54 cm margins for midterm-check forms and the task-book margins required by the user's
department template when available. Do not force thesis-body gutter/page-number rules onto
these form documents.

## 3. Header and Footer

**Header**: "Suzhou University Undergraduate Thesis" — 9pt Song, centered, with bottom border line.

```python
header = section.header
header.is_linked_to_previous = False
hp = header.paragraphs[0]
hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = hp.add_run("苏州大学本科生毕业设计（论文）")
run.font.size = Pt(9)
run.font.name = '宋体'
set_run_font_eastasia(run, '宋体')

# Header bottom border (required)
hp_pPr = hp._element.find(qn('w:pPr'))
if hp_pPr is None:
    hp_pPr = parse_xml(f'<w:pPr {nsdecls("w")}></w:pPr>')
    hp._element.insert(0, hp_pPr)
pBdr = parse_xml(
    f'<w:pBdr {nsdecls("w")}>'
    f'<w:bottom w:val="single" w:sz="6" w:space="1" w:color="auto"/>'
    f'</w:pBdr>'
)
hp_pPr.append(pBdr)
```

**Footer rules**:
- Thesis Body: Arabic page numbers `-1-`, `-2-`, `-3-`..., centered, continuous
- Translation & Review: No page numbers (empty footer)

```python
footer = section.footer
footer.is_linked_to_previous = False
fp = footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
# Thesis Body: insert "-" + PAGE field + "-" for -N- format
# Translation/Review: leave footer empty
```

## 3.5. Non-Chapter Heading (References, Acknowledgement)

References and Acknowledgement are NOT chapters — they must NOT use `add_heading(level=1)`.
Use a plain paragraph styled to match Heading 1 visually:

```python
def add_non_chapter_heading(doc, text, add_toc_bookmark=True, page_break_before=False):
    """添加非章节标题（参考文献、致谢等），外观与Heading 1相同但不使用Heading样式，
    不会被Word编入章节大纲。"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.line_spacing = 1.5
    # Use line units for spacing (same as Heading styles)
    pPr = p._element.find(qn('w:pPr'))
    if pPr is None:
        pPr = parse_xml(f'<w:pPr {nsdecls("w")}></w:pPr>')
        p._element.insert(0, pPr)
    nch_sp = pPr.find(qn('w:spacing'))
    if nch_sp is None:
        nch_sp = parse_xml(f'<w:spacing {nsdecls("w")}/>')
        pPr.append(nch_sp)
    nch_sp.set(qn('w:beforeLines'), '100')
    nch_sp.set(qn('w:afterLines'), '100')

    if page_break_before:
        pPr.append(parse_xml(f'<w:pageBreakBefore {nsdecls("w")}/>'))

    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(15)
    run.font.name = 'Times New Roman'
    run.font.color.rgb = RGBColor(0, 0, 0)
    set_run_font_eastasia(run, '宋体')

    if add_toc_bookmark:
        _add_toc_bookmark_to_heading(p)

    return p
```

## 4. Font Configuration

Core principle: English = Times New Roman, Chinese = Song (via eastAsia XML attribute).

```python
def set_run_font_eastasia(run, font_name):
    """Set CJK font via XML — the KEY function for Chinese font control.
    font.name alone only sets the Latin font; this sets the eastAsia font
    which controls how Chinese characters render in Word."""
    run_el = run._element
    rpr = run_el.find(qn('w:rPr'))
    if rpr is None:
        rpr = parse_xml(f'<w:rPr {nsdecls("w")}></w:rPr>')
        run_el.insert(0, rpr)
    rFonts = rpr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")}/>')
        rpr.append(rFonts)
    rFonts.set(qn('w:eastAsia'), font_name)
```

## 5. Style Definitions

| Element | Font Size | Chinese Font | English Font | Bold | Alignment | Line Spacing |
|---------|-----------|-------------|--------------|------|-----------|-------------|
| Title | 18pt | Hei | TNR | Yes | Center | 1.5x |
| Abstract Title | 14-15pt | Hei | TNR | Yes | Center | 1.5x |
| TOC Title | 14pt (四号) | Song | TNR | Yes | Center | 1.5x |
| Heading 1 (chapter) | 15pt | Song | TNR | Yes | Center | 1.5x |
| Heading 2 (section) | 12pt | Song | TNR | Yes | Left | 1.5x |
| Body Text | 12pt | Song | TNR | No | Justify | 1.5x |
| Figure Caption | 12pt (小四) | Song | TNR | No | Center | 1.5x |
| References | 12pt (thesis) / 10.5pt (translation) | Song | TNR | No | Left | 1.5x |

## 6. Body Paragraph Format

1.5x line spacing, 0pt space before/after, first-line indent 2 characters.

```python
def add_body_paragraph(doc, text):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing = 1.5
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)

    # First-line indent: 2 characters via XML (preferred for CJK)
    pPr = p._element.find(qn('w:pPr'))
    ind = parse_xml(f'<w:ind {nsdecls("w")}/>')
    pPr.append(ind)
    ind.set(qn('w:firstLineChars'), '200')  # 200 = 2 characters

    run = p.add_run(text)
    run.font.size = Pt(12)
    run.font.name = 'Times New Roman'
    set_run_font_eastasia(run, '宋体')
```

**Heading spacing** (gap between heading and body text):
Use "line" units (beforeLines/afterLines), NOT fixed point values (before/after).
The format checker distinguishes "12磅" from "1行" — they are not equivalent.
```python
# CORRECT: use line units (100 = 1 line)
sp.set(qn('w:beforeLines'), '100')  # 1 line before
sp.set(qn('w:afterLines'), '100')   # 1 line after
# Remove any fixed-value overrides:
for attr in ['w:before', 'w:after']:
    if sp.get(qn(attr)) is not None:
        del sp.attrib[qn(attr)]

# WRONG: fixed point values will be flagged as "12磅, should be 1行"
# sp.set(qn('w:before'), '240')   # <- DO NOT USE
# sp.set(qn('w:after'), '240')    # <- DO NOT USE
```

## 7. Figure Insertion

```python
def add_figure(doc, fig_path, caption_text, width=Inches(5.0)):
    # Image paragraph: centered, no indent
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.line_spacing = 1.0
    p_img.paragraph_format.space_before = Pt(6)
    run = p_img.add_run()
    run.add_picture(fig_path, width=width)

    # Caption paragraph: centered, 12pt(小四) TNR + Song(eastAsia), 0pt spacing
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p_cap.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.line_spacing = 1.5
    run_cap = p_cap.add_run(caption_text)
    run_cap.font.size = Pt(12)
    run_cap.font.name = 'Times New Roman'
    set_run_font_eastasia(run_cap, '宋体')
```

## 8. Table of Contents

Uses Word native field codes for auto-updating:

1. TOC title paragraph ("Contents")
2. TOC field begin: `fldChar begin` -> `instrText: TOC \o "1-2" \h \z \u` -> `fldChar separate`
3. Cached entries: hyperlink paragraphs with PAGEREF fields
4. TOC field end: `fldChar end`

Each entry links to a bookmark on its corresponding heading.

## 9. Bookmark System

```python
def add_bookmark_to_paragraph(para, bookmark_name, bookmark_id):
    """Wrap all runs with bookmarkStart/bookmarkEnd"""
    p_elem = para._element
    runs = p_elem.findall(qn('w:r'))
    if runs:
        bm_start = parse_xml(
            f'<w:bookmarkStart {nsdecls("w")} w:id="{bookmark_id}" w:name="{bookmark_name}"/>'
        )
        runs[0].addprevious(bm_start)
        bm_end = parse_xml(
            f'<w:bookmarkEnd {nsdecls("w")} w:id="{bookmark_id}"/>'
        )
        runs[-1].addnext(bm_end)
```

## 10. Citation System

Citations `[1]`, `[1,2]`, `[1-3]` are converted to superscript hyperlinks pointing
to reference bookmarks:

```python
CITATION_RE = re.compile(r'(\[\d+(?:[-,]\d+)*\])')

def _add_citation_hyperlink(p, citation_text):
    # Extract reference number, create hyperlink to _Ref{N} bookmark
    # with superscript formatting, black color, no underline
    hyperlink_xml = (
        f'<w:hyperlink {nsmap} w:anchor="_Ref{ref_num}">'
        f'<w:r><w:rPr>...<w:vertAlign w:val="superscript"/>...</w:rPr>'
        f'<w:t>{citation_text}</w:t></w:r>'
        f'</w:hyperlink>'
    )
```

## 11. References Section

```python
def add_references(doc, refs):
    for ref in refs:
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.line_spacing = 1.5
        pf.alignment = WD_ALIGN_PARAGRAPH.LEFT

        # Hanging indent: 1.27cm (720 twips)
        ind.set(qn('w:hanging'), '720')
        ind.set(qn('w:left'), '720')

        # Tab after number: "[N] Text..." -> "[N]\tText..."
        ref_text = re.sub(r'^\[(\d+)\] ', r'[\1]\t', ref)

        run = p.add_run(ref_text)
        run.font.size = Pt(12)
        run.font.name = 'Times New Roman'
        set_run_font_eastasia(run, '宋体')

        # Add _Ref{N} bookmark for citation cross-references
        add_bookmark_to_paragraph(p, f'_Ref{ref_num}', 100 + int(ref_num))
```

## 12. Metadata Erasure

python-docx writes fingerprints into core properties and app.xml. All traces must be
erased before saving — visible in File > Properties in Word. Apply this to every
generated DOCX type, including thesis body, literature review, literature translation,
task book, and midterm-check form.

```python
# Place BEFORE doc.save()
core = doc.core_properties
core.title = ''
core.subject = ''
core.author = ''
core.last_modified_by = ''
core.keywords = ''
core.category = ''
core.comments = ''
core.content_status = ''
core.identifier = ''
core.language = ''
core.version = ''
core.revision = 1
core.created = datetime.datetime.now()
core.modified = datetime.datetime.now()

# Patch app.xml. Do not leave tool, company, or manager fingerprints.
app_part = doc.part.package.part_related_by(RT.EXTENDED_PROPERTIES)
app_root = etree.fromstring(app_part.blob)
ns = {'ep': 'http://schemas.openxmlformats.org/officeDocument/2006/extended-properties'}
for tag_name in ['Application', 'AppVersion', 'Company', 'Manager']:
    el = app_root.find(f'ep:{tag_name}', ns)
    if el is not None:
        if tag_name == 'Application':
            el.text = 'Microsoft Office Word'
        elif tag_name == 'AppVersion':
            el.text = '16.0000'
        else:
            el.text = ''
app_part._blob = etree.tostring(app_root, xml_declaration=True, encoding='UTF-8', standalone=True)
```
