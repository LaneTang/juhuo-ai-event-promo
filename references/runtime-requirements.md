# Runtime Requirements

Use this reference when installing `juhuo-ai-event-promo` from a GitHub repo or debugging document extraction.

## Minimum Runtime

- Python 3.10+ recommended.
- `.docx` and `.docm` extraction uses only Python standard library modules.
- No external Python package is required for `.docx` plans.

## Legacy Word / WPS Files

For `.doc`, `.wps`, and `.wpt` files, `scripts/extract_plan_text.py` tries multiple extraction methods:

1. LibreOffice / `soffice`
2. `pandoc`
3. `antiword` / `catdoc`
4. Python `olefile` string fallback
5. Word-compatible COM automation on Windows

This avoids relying only on an interactive Microsoft Word login session.

Recommended Python fallback for old `.doc` files:

```powershell
python -m pip install olefile
```

`olefile` is a best-effort fallback. It does not fully parse Word binary layout, but it can often recover enough plain text from simple activity plans when COM is unavailable.

Word COM fallback requirements:

- Windows.
- Microsoft Word or another Word-compatible application that can open the file.
- Python package `pywin32`, which provides `win32com.client`.

Anaconda on Windows often already includes `pywin32`. If not, install it in the Python environment used by Codex:

```powershell
python -m pip install pywin32
```

If Word COM fails with a login-session error such as "指定的登录会话不存在", use one of these fallbacks:

- convert the file to `.docx` and rerun the skill
- install `olefile` and rerun the script
- install LibreOffice so `soffice` is available in PATH
- paste the activity plan text directly

## PDF Files

PDF support is best-effort.

Preferred optional dependency:

```powershell
python -m pip install pypdf
```

If `pypdf` or `PyPDF2` is unavailable, the script tries Word COM fallback on Windows. This may work for text PDFs, but scanned PDFs may not produce usable text.

## Quick Extraction Check

From the skill folder:

```powershell
python scripts/extract_plan_text.py path\to\plan.docx --out extracted-plan.txt
python scripts/extract_plan_text.py path\to\plan.doc --out extracted-plan.txt
```

Expected stderr contains one of:

```text
[extract_plan_text] method=OOXML
[extract_plan_text] method=Word COM
[extract_plan_text] method=LibreOffice/soffice
[extract_plan_text] method=pandoc
[extract_plan_text] method=olefile string fallback
```

The script extracts plain text only. Tables may be flattened; the fact table should mark source-readiness warnings when structure matters.
