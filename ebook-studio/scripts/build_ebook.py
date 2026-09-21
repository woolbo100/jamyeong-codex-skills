#!/usr/bin/env python3
"""Build an editable Korean A4 ebook DOCX from book.json."""
from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


def rgb(value: str) -> RGBColor:
    return RGBColor.from_string(value.lstrip("#").upper())


def shade(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill.lstrip("#").upper())


def set_cell_margins(cell) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for margin, value in [("top", 180), ("start", 220), ("bottom", 180), ("end", 220)]:
        node = tc_mar.find(qn("w:" + margin))
        if node is None:
            node = OxmlElement("w:" + margin)
            tc_mar.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def resolve_image(path: str | None, base: Path) -> Path | None:
    if not path:
        return None
    image = Path(path)
    if not image.is_absolute():
        image = base / image
    return image if image.exists() else None


def setup_section(section, image_page: bool) -> None:
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    if image_page:
        section.top_margin = Cm(0)
        section.bottom_margin = Cm(0)
        section.left_margin = Cm(0)
        section.right_margin = Cm(0)
    else:
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.0)
        section.right_margin = Cm(2.0)


def configure_styles(doc: Document, design: dict) -> dict:
    font = design.get("font", "Malgun Gothic")
    accent = design.get("accent", "#3770B2")
    text = design.get("text", "#2F2B26")
    muted = design.get("muted", "#EEF3F2")

    for name, size, bold, color in [
        ("Normal", 12, False, text),
        ("Subtitle", 12, False, text),
        ("Quote", 12, False, accent),
    ]:
        style = doc.styles[name]
        style.font.name = font
        style._element.rPr.rFonts.set(qn("w:eastAsia"), font)
        style.font.size = Pt(size)
        style.font.bold = bold
        style.font.color.rgb = rgb(color)

    doc.styles["Normal"].paragraph_format.space_after = Pt(7)
    doc.styles["Normal"].paragraph_format.line_spacing = 1.5
    return {"accent": accent, "text": text, "muted": muted, "font": font}


def add_full_page_image(doc: Document, path: Path | None, first: bool = False) -> bool:
    if path is None:
        return False
    if not first:
        setup_section(doc.add_section(WD_SECTION.NEW_PAGE), True)
    paragraph = doc.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(0)
    paragraph.paragraph_format.space_after = Pt(0)
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.add_run().add_picture(str(path), width=Cm(21.0), height=Cm(29.7))
    return True


def add_text_section(doc: Document) -> None:
    setup_section(doc.add_section(WD_SECTION.NEW_PAGE), False)


def add_title(doc: Document, text: str, level: int = 1, colors: dict | None = None) -> None:
    sizes = {1: 22, 2: 18, 3: 14}
    before = {1: 14, 2: 12, 3: 10}
    after = {1: 12, 2: 9, 3: 7}
    paragraph = doc.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(before.get(level, 10))
    paragraph.paragraph_format.space_after = Pt(after.get(level, 7))
    paragraph.paragraph_format.line_spacing = 1.15
    run = paragraph.add_run(text)
    run.bold = True
    run.font.name = (colors or {}).get("font", "Malgun Gothic")
    run.font.size = Pt(sizes.get(level, 14))
    run.font.color.rgb = rgb((colors or {}).get("accent", "#3770B2"))


def add_paragraph(doc: Document, text: str, style: str | None = None) -> None:
    paragraph = doc.add_paragraph(style=style)
    paragraph.paragraph_format.line_spacing = 1.5
    paragraph.paragraph_format.space_after = Pt(7)
    run = paragraph.add_run(text)
    run.font.name = "Malgun Gothic"


def add_block(doc: Document, block: dict, colors: dict) -> None:
    kind = block.get("type", "paragraph")
    if kind == "paragraph":
        add_paragraph(doc, block.get("text", ""))
    elif kind == "heading":
        add_title(doc, block.get("text", ""), int(block.get("level", 2)), colors)
    elif kind == "quote":
        paragraph = doc.add_paragraph(style="Quote")
        paragraph.paragraph_format.left_indent = Cm(0.7)
        paragraph.paragraph_format.line_spacing = 1.5
        paragraph.add_run(block.get("text", ""))
    elif kind == "bullets":
        for item in block.get("items", []):
            add_paragraph(doc, item)
    elif kind == "checklist":
        if block.get("title"):
            add_title(doc, block["title"], 3, colors)
        for item in block.get("items", []):
            add_paragraph(doc, item)
    elif kind == "callout":
        table = doc.add_table(rows=1, cols=1)
        cell = table.cell(0, 0)
        shade(cell, colors["muted"])
        set_cell_margins(cell)
        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        paragraph = cell.paragraphs[0]
        paragraph.paragraph_format.line_spacing = 1.5
        if block.get("title"):
            run = paragraph.add_run(block["title"] + "\n")
            run.bold = True
            run.font.color.rgb = rgb(colors["accent"])
        paragraph.add_run(block.get("text", ""))
        doc.add_paragraph()
    elif kind == "page_break":
        doc.add_page_break()


def add_manual_toc(doc: Document, chapters: list[dict], colors: dict) -> None:
    add_title(doc, "목차", 1, colors)
    add_paragraph(doc, "이 책은 각 장의 흐름을 따라 읽고 바로 실천할 수 있도록 구성했습니다.")
    for chapter in chapters:
        paragraph = doc.add_paragraph()
        paragraph.paragraph_format.space_after = Pt(9)
        run = paragraph.add_run(f"{chapter.get('number', '')}장. {chapter.get('title', '')}")
        run.bold = True
        run.font.name = colors["font"]
        run.font.size = Pt(12)
        if chapter.get("subtitle"):
            subtitle = paragraph.add_run(f"\n{chapter['subtitle']}")
            subtitle.font.name = colors["font"]
            subtitle.font.size = Pt(12)


def add_copyright(doc: Document, meta: dict, colors: dict) -> None:
    add_title(doc, "판권", 1, colors)
    for label, value in [
        ("제목", meta.get("title")),
        ("저자", meta.get("author")),
        ("브랜드", meta.get("brand")),
        ("발행처", meta.get("publisher")),
        ("발행일", meta.get("publication_date")),
        ("ISBN", meta.get("isbn")),
        ("연락처", meta.get("contact")),
    ]:
        if value:
            add_paragraph(doc, f"{label}: {value}")
    if meta.get("copyright"):
        add_paragraph(doc, meta["copyright"])
    if meta.get("disclaimer"):
        add_paragraph(doc, meta["disclaimer"])


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: build_ebook.py book.json output.docx")

    spec = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2]).resolve()
    data = json.loads(spec.read_text(encoding="utf-8"))
    base = spec.parent
    meta = data.get("meta", {})
    design = data.get("design", {})

    doc = Document()
    setup_section(doc.sections[0], True)
    colors = configure_styles(doc, design)

    cover = resolve_image(design.get("cover_image"), base)
    if not add_full_page_image(doc, cover, first=True):
        add_text_section(doc)
        add_title(doc, meta.get("title", "제목"), 1, colors)
        if meta.get("subtitle"):
            add_paragraph(doc, meta["subtitle"], "Subtitle")
        if meta.get("author"):
            add_paragraph(doc, meta["author"], "Subtitle")

    add_text_section(doc)
    add_manual_toc(doc, data.get("chapters", []), colors)

    if data.get("front_matter"):
        add_text_section(doc)
        for block in data.get("front_matter", []):
            add_block(doc, block, colors)

    for index, chapter in enumerate(data.get("chapters", []), 1):
        chapter_image = resolve_image(chapter.get("image"), base)
        add_full_page_image(doc, chapter_image)
        add_text_section(doc)
        add_title(doc, f"{chapter.get('number', index)}장. {chapter.get('title', '')}", 1, colors)
        if chapter.get("subtitle"):
            add_paragraph(doc, chapter["subtitle"], "Subtitle")
        for block in chapter.get("blocks", []):
            add_block(doc, block, colors)

    if data.get("back_matter"):
        add_text_section(doc)
        for block in data.get("back_matter", []):
            add_block(doc, block, colors)

    copyright_background = resolve_image(design.get("copyright_background"), base)
    add_full_page_image(doc, copyright_background)
    add_text_section(doc)
    add_copyright(doc, meta, colors)

    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out)

    with zipfile.ZipFile(out) as archive:
        bad = archive.testzip()
        if bad:
            raise SystemExit(f"DOCX zip integrity failed: {bad}")
    print(out)


if __name__ == "__main__":
    main()
