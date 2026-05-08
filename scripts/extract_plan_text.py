#!/usr/bin/env python
"""Extract text from event plan files for juhuo-ai-event-promo.

Supported input types:
- Word OOXML: .docx, .docm
- Legacy Word / WPS Writer: .doc, .wps, .wpt via Word/WPS-compatible COM on Windows
- PDF: pypdf/PyPDF2 when installed, otherwise Word COM fallback on Windows

The script intentionally extracts plain text only. Tables may be flattened; mark
that as a source-readiness warning in the fact table.
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET


WORD_OOXML_EXTS = {".docx", ".docm"}
COM_EXTS = {".doc", ".wps", ".wpt", ".pdf"}
PDF_EXTS = {".pdf"}
SUPPORTED_EXTS = WORD_OOXML_EXTS | COM_EXTS


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\x07", "\n").replace("\x0b", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def iter_text_from_ooxml_xml(xml_bytes: bytes) -> Iterable[str]:
    root = ET.fromstring(xml_bytes)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

    for paragraph in root.findall(".//w:p", ns):
        parts: list[str] = []
        for node in paragraph.iter():
            tag = node.tag.rsplit("}", 1)[-1]
            if tag == "t" and node.text:
                parts.append(node.text)
            elif tag == "tab":
                parts.append("\t")
            elif tag == "br":
                parts.append("\n")
        line = "".join(parts).strip()
        if line:
            yield line


def extract_docx(path: Path) -> str:
    xml_paths = ["word/document.xml"]
    lines: list[str] = []

    with zipfile.ZipFile(path) as archive:
        for xml_path in xml_paths:
            try:
                xml_bytes = archive.read(xml_path)
            except KeyError:
                continue
            lines.extend(iter_text_from_ooxml_xml(xml_bytes))

    if not lines:
        raise RuntimeError("No text found in OOXML document body.")

    return normalize_text("\n".join(lines))


def extract_pdf_with_python(path: Path) -> str | None:
    reader_cls = None
    errors: list[str] = []

    try:
        from pypdf import PdfReader  # type: ignore

        reader_cls = PdfReader
    except Exception as exc:  # pragma: no cover - optional dependency
        errors.append(f"pypdf unavailable: {exc}")

    if reader_cls is None:
        try:
            from PyPDF2 import PdfReader  # type: ignore

            reader_cls = PdfReader
        except Exception as exc:  # pragma: no cover - optional dependency
            errors.append(f"PyPDF2 unavailable: {exc}")

    if reader_cls is None:
        return None

    reader = reader_cls(str(path))
    pages: list[str] = []
    for index, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        if page_text.strip():
            pages.append(f"--- Page {index} ---\n{page_text.strip()}")

    if not pages:
        raise RuntimeError("PDF parser ran but found no extractable text.")

    return normalize_text("\n\n".join(pages))


def extract_with_word_com(path: Path) -> str:
    if sys.platform != "win32":
        raise RuntimeError("Word COM fallback is only available on Windows.")

    try:
        import pythoncom  # type: ignore
        import win32com.client  # type: ignore
    except Exception as exc:
        raise RuntimeError(
            "win32com.client is required for .doc/.wps/.pdf COM extraction on Windows."
        ) from exc

    word = None
    document = None
    pythoncom.CoInitialize()
    try:
        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False
        word.DisplayAlerts = 0
        document = word.Documents.Open(
            str(path),
            ConfirmConversions=False,
            ReadOnly=True,
            AddToRecentFiles=False,
        )
        text = document.Content.Text
        if not text or not text.strip():
            raise RuntimeError("Word COM opened the file but returned no text.")
        return normalize_text(text)
    finally:
        if document is not None:
            document.Close(False)
        if word is not None:
            word.Quit()
        pythoncom.CoUninitialize()


def extract_text(path: Path) -> tuple[str, str]:
    ext = path.suffix.lower()
    if ext not in SUPPORTED_EXTS:
        raise ValueError(
            f"Unsupported file type '{ext}'. Supported: {', '.join(sorted(SUPPORTED_EXTS))}"
        )

    if ext in WORD_OOXML_EXTS:
        return extract_docx(path), "OOXML"

    if ext in PDF_EXTS:
        pdf_text = extract_pdf_with_python(path)
        if pdf_text is not None:
            return pdf_text, "PDF parser"
        return extract_with_word_com(path), "Word COM PDF fallback"

    return extract_with_word_com(path), "Word COM"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract plain text from WPS/Word/PDF activity plan files."
    )
    parser.add_argument("input", help="Path to .docx, .doc, .wps, .wpt, or .pdf file")
    parser.add_argument("--out", help="Optional UTF-8 text output path")
    parser.add_argument(
        "--print",
        action="store_true",
        help="Print extracted text to stdout even when --out is provided",
    )
    args = parser.parse_args()

    path = Path(args.input).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(path)

    text, method = extract_text(path)
    sys.stderr.write(f"[extract_plan_text] method={method}; chars={len(text)}\n")
    sys.stderr.write(
        "[extract_plan_text] note=plain-text extraction may flatten tables; preserve uncertainty in fact table.\n"
    )

    if args.out:
        out_path = Path(args.out).expanduser().resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(text, encoding="utf-8")

    if args.print or not args.out:
        sys.stdout.write(text)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        sys.stderr.write(f"[extract_plan_text] ERROR: {exc}\n")
        raise SystemExit(1)

