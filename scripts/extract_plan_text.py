#!/usr/bin/env python
"""Extract text from event plan files for juhuo-ai-event-promo.

Supported input types:
- Word OOXML: .docx, .docm
- Legacy Word / WPS Writer: .doc, .wps, .wpt via external converters, optional olefile fallback, or Word/WPS-compatible COM on Windows
- PDF: pypdf/PyPDF2 when installed, otherwise Word COM fallback on Windows

The script intentionally extracts plain text only. Tables may be flattened; mark
that as a source-readiness warning in the fact table.
"""

from __future__ import annotations

import argparse
import re
import site
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET


WORD_OOXML_EXTS = {".docx", ".docm"}
COM_EXTS = {".doc", ".wps", ".wpt", ".pdf"}
LEGACY_WORD_EXTS = {".doc", ".wps", ".wpt"}
PDF_EXTS = {".pdf"}
SUPPORTED_EXTS = WORD_OOXML_EXTS | COM_EXTS


def ensure_user_site_on_path() -> None:
    """Make --user installs visible in embedded/managed Python environments."""

    try:
        user_site = site.getusersitepackages()
    except Exception:
        return
    if user_site and user_site not in sys.path:
        sys.path.append(user_site)


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
    ensure_user_site_on_path()

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


def run_command(command: list[str], timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def extract_with_libreoffice(path: Path) -> str | None:
    executable = shutil.which("soffice") or shutil.which("libreoffice")
    if executable is None:
        return None

    with tempfile.TemporaryDirectory(prefix="juhuo_plan_extract_") as tmp:
        outdir = Path(tmp)
        command = [
            executable,
            "--headless",
            "--convert-to",
            "txt:Text",
            "--outdir",
            str(outdir),
            str(path),
        ]
        result = run_command(command, timeout=90)
        if result.returncode != 0:
            return None

        txt_files = list(outdir.glob("*.txt"))
        if not txt_files:
            return None

        for txt_file in txt_files:
            for encoding in ("utf-8-sig", "utf-16", "gb18030"):
                try:
                    text = txt_file.read_text(encoding=encoding)
                except UnicodeError:
                    continue
                if text.strip():
                    return normalize_text(text)

    return None


def extract_with_pandoc(path: Path) -> str | None:
    executable = shutil.which("pandoc")
    if executable is None:
        return None

    result = run_command([executable, str(path), "-t", "plain"], timeout=90)
    if result.returncode == 0 and result.stdout.strip():
        return normalize_text(result.stdout)
    return None


def extract_with_antiword_like(path: Path) -> str | None:
    for name in ("antiword", "catdoc"):
        executable = shutil.which(name)
        if executable is None:
            continue
        result = run_command([executable, str(path)], timeout=60)
        if result.returncode == 0 and result.stdout.strip():
            return normalize_text(result.stdout)
    return None


def extract_with_external_converters(path: Path) -> tuple[str, str] | None:
    attempts = [
        ("LibreOffice/soffice", extract_with_libreoffice),
        ("pandoc", extract_with_pandoc),
        ("antiword/catdoc", extract_with_antiword_like),
    ]
    for name, extractor in attempts:
        try:
            text = extractor(path)
        except Exception:
            text = None
        if text and text.strip():
            return text, name
    return None


def candidate_text_from_bytes(data: bytes) -> list[str]:
    """Best-effort string extraction from legacy OLE streams.

    This is not a complete Word binary parser. It is a practical fallback for
    activity plans when COM/external converters are unavailable. It extracts
    long readable runs from common encodings and filters obvious binary noise.
    """

    candidates: list[str] = []
    encodings = ("utf-16le", "utf-16be", "gb18030", "utf-8")

    for encoding in encodings:
        try:
            decoded = data.decode(encoding, errors="ignore")
        except Exception:
            continue

        decoded = decoded.replace("\x00", "")
        runs = re.findall(
            r"[\u4e00-\u9fffA-Za-z0-9，。；：、（）《》“”‘’！？|·/\\\-—_:,.()[\]#%+ \t\n]{4,}",
            decoded,
        )
        for run in runs:
            run = re.sub(r"[ \t]{2,}", " ", run)
            run = re.sub(r"\n{3,}", "\n\n", run).strip()
            if not run:
                continue
            chinese_count = len(re.findall(r"[\u4e00-\u9fff]", run))
            alpha_count = len(re.findall(r"[A-Za-z]", run))
            if chinese_count >= 2 or alpha_count >= 8:
                candidates.append(run)

    return candidates


ACTIVITY_TERMS = (
    "活动",
    "时间",
    "地点",
    "目的",
    "对象",
    "主办",
    "协办",
    "承办",
    "流程",
    "形式",
    "嘉宾",
    "分享",
    "交流",
    "报名",
    "参与",
    "开篇",
    "介绍",
    "学生",
    "创业",
    "科创",
    "园区",
    "社区",
    "炬火",
    "AI",
    "负责",
    "合影",
)


def looks_like_plan_line(line: str) -> bool:
    line = line.strip()
    if len(line) < 4 or len(line) > 180:
        return False

    if re.search(r"\d{4}\s*年\s*\d{1,2}\s*月\s*\d{1,2}\s*日", line):
        return True
    if re.search(r"\d{1,2}:\d{2}\s*[-—]\s*\d{1,2}:\d{2}", line) and len(line) < 80:
        return True

    cjk_count = len(re.findall(r"[\u4e00-\u9fff]", line))
    ascii_letters = len(re.findall(r"[A-Za-z]", line))
    visible = len(re.findall(r"[\u4e00-\u9fffA-Za-z0-9]", line))
    if visible == 0:
        return False

    if cjk_count < 3 and ascii_letters < 2:
        return False

    if cjk_count < 4 and not re.search(r"\d", line):
        return False

    non_ai_terms = [term for term in ACTIVITY_TERMS if term != "AI"]
    if "AI" in line and not any(term in line for term in non_ai_terms) and len(line) < 14:
        return False

    if not any(term in line for term in ACTIVITY_TERMS):
        return False

    # Binary noise decoded as CJK often has very little normal punctuation and
    # many rare characters. Event-plan lines usually have common section words,
    # punctuation, digits, or ASCII topic terms such as AI.
    normal_marks = len(re.findall(r"[，。；：、（）《》“”！？:()0-9A-Za-z]", line))
    if normal_marks == 0 and cjk_count > 12:
        return False

    return True


def clean_ole_text_candidates(candidates: list[str]) -> list[str]:
    lines: list[str] = []
    for chunk in candidates:
        chunk = chunk.replace("\t", " ")
        for raw_line in re.split(r"\n+| {2,}", chunk):
            line = raw_line.strip(" \t\r\n-—_.,;:|/\\")
            line = re.sub(r"\s+", " ", line)
            if looks_like_plan_line(line):
                lines.append(line)

    seen: set[str] = set()
    unique_lines: list[str] = []
    for line in lines:
        key = re.sub(r"\s+", "", line)
        if key in seen:
            continue
        seen.add(key)
        unique_lines.append(line)
    return unique_lines


def score_text_candidate(text: str) -> int:
    chinese_count = len(re.findall(r"[\u4e00-\u9fff]", text))
    useful_punctuation = len(re.findall(r"[，。；：、（）《》“”！？]", text))
    replacement_count = text.count("\ufffd")
    control_count = len(re.findall(r"[\x00-\x08\x0e-\x1f]", text))
    return chinese_count * 3 + useful_punctuation - replacement_count * 10 - control_count * 5


def extract_with_olefile_strings(path: Path) -> str | None:
    ensure_user_site_on_path()
    try:
        import olefile  # type: ignore
    except Exception:
        return None

    if not olefile.isOleFile(str(path)):
        return None

    streams_to_try = [
        ("WordDocument",),
        ("1Table",),
        ("0Table",),
        ("Data",),
        ("\x05SummaryInformation",),
        ("\x05DocumentSummaryInformation",),
    ]

    chunks: list[str] = []
    with olefile.OleFileIO(str(path)) as ole:
        for stream in streams_to_try:
            if not ole.exists(stream):
                continue
            data = ole.openstream(stream).read()
            chunks.extend(candidate_text_from_bytes(data))

    if not chunks:
        return None

    useful_lines = clean_ole_text_candidates(chunks)
    if not useful_lines:
        return None

    text = normalize_text("\n".join(useful_lines))
    if len(re.findall(r"[\u4e00-\u9fff]", text)) < 20:
        return None
    return text


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
        external_pdf = extract_with_external_converters(path)
        if external_pdf is not None:
            return external_pdf
        return extract_with_word_com(path), "Word COM PDF fallback"

    external = extract_with_external_converters(path)
    if external is not None:
        return external

    if ext in LEGACY_WORD_EXTS:
        ole_text = extract_with_olefile_strings(path)
        if ole_text is not None:
            return ole_text, "olefile string fallback"

    try:
        return extract_with_word_com(path), "Word COM"
    except Exception as exc:
        raise RuntimeError(
            "Could not extract legacy Word/WPS text. Tried external converters "
            "(LibreOffice/soffice, pandoc, antiword/catdoc), optional olefile fallback, and Word COM. "
            "If Word COM reports a login-session error, convert the file to .docx "
            "or install optional dependencies from requirements-optional.txt."
        ) from exc


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
