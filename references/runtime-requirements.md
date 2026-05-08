# Runtime Requirements

Use this reference when installing or forward-testing `juhuo-ai-event-promo` from a GitHub repo.

## Minimum Runtime

- Python 3.10+ recommended.
- `.docx` and `.docm` extraction uses only Python standard library modules.
- No external Python package is required for `.docx` plans.

## Legacy Word / WPS Files

For `.doc`, `.wps`, and `.wpt` files, `scripts/extract_plan_text.py` uses Word-compatible COM automation on Windows.

Requirements:

- Windows.
- Microsoft Word or another Word-compatible application that can open the file.
- Python package `pywin32`, which provides `win32com.client`.

Anaconda on Windows often already includes `pywin32`. If not, install it in the Python environment used by Codex:

```powershell
python -m pip install pywin32
```

## PDF Files

PDF support is best-effort in v1.

Preferred optional dependency:

```powershell
python -m pip install pypdf
```

If `pypdf` or `PyPDF2` is unavailable, the script tries Word COM fallback on Windows. This may work for text PDFs, but scanned PDFs may not produce usable text.

## Quick Extraction Test

From the skill folder:

```powershell
python scripts/extract_plan_text.py path\to\plan.docx --out extracted-plan.txt
python scripts/extract_plan_text.py path\to\plan.doc --out extracted-plan.txt
```

Expected stderr contains one of:

```text
[extract_plan_text] method=OOXML
[extract_plan_text] method=Word COM
```

The script extracts plain text only. Tables may be flattened; the fact table should mark source-readiness warnings when structure matters.

