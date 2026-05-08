---
name: juhuo-ai-event-promo
description: Use when creating Juhuo AI event promotion copy from an activity plan, Word/WPS document, or structured event brief for WeChat Official Account, Xiaohongshu, QQ channel/group/campus-wall reposts, or a full campus AI community promo package.
---

# Juhuo AI Event Promo

## Scope

Use this skill to turn a Juhuo AI event plan into a publishable promotion package.

v1 output focuses on copywriting:

- WeChat Official Account article copy.
- Xiaohongshu post copy.
- QQ Channel, QQ group, and QQ campus wall reuse the Xiaohongshu copy and materials by default.

Do not generate WeChat HTML, posters, cover images, or image assets by default. If the user explicitly requests those assets, treat them as separate downstream tasks after the copy package is fact-checked.

## Core Rule

Treat the activity plan as the single source of truth. Do not write promotional copy before extracting a fact table and running quality gates.

If the user gives corrections outside the plan, record them as user-supplied facts and make conflicts visible.

If the user provides previous Juhuo posts or published drafts, use them as style references by default. Do not treat them as factual updates unless the user explicitly says they are newer confirmed facts.

## Workflow

1. Read the user's activity plan or structured brief.
2. Read `references/fact-table-schema.md`.
3. Extract a fact table with publicity levels and statuses.
4. Read `references/quality-gates.md`.
5. Run a quality gate report before writing copy.
6. If a `BLOCKER` affects final publication, ask for confirmation unless the user requests a placeholder draft.
7. Read platform references only for requested outputs:
   - WeChat: `references/wechat-copy-style.md`
   - Xiaohongshu and QQ reuse: `references/xiaohongshu-copy-style.md`
8. Read `references/output-format.md`.
9. Generate the requested package.
10. Run a final consistency pass across all outputs:
    - event name
    - date and time
    - location or location uncertainty
    - registration method
    - audience policy
    - CTA
    - promises and claims

## Source Reading Notes

- Prefer `scripts/extract_plan_text.py` when the input is a WPS, Word, or PDF file.
  - Example: `python scripts/extract_plan_text.py <plan.docx> --out extracted-plan.txt`
  - Supported types: `.docx`, `.docm`, `.doc`, `.wps`, `.wpt`, `.pdf`.
- Read `references/runtime-requirements.md` when installing the skill on a new machine, debugging document extraction, or preparing a GitHub-based forward test.
- For `.docx`, extract text through normal document tooling or OOXML text extraction.
- For legacy `.doc`, use Word/WPS/LibreOffice conversion or Word COM text extraction when available. Mark this as a source-readiness warning because table structure may be flattened.
- For `.pdf`, use a PDF text parser when available; otherwise use the script's Word COM fallback on Windows.
- Do not keep converter scratch files inside the final skill unless they are intentional examples or scripts.

## Default Output Behavior

If the user says "生成宣传包", "根据策划案写推文", or does not specify a platform, generate the full v1 package:

- Fact table summary.
- Quality gate report.
- WeChat Official Account copy.
- Xiaohongshu copy.
- QQ reuse note for QQ Channel, QQ group, and QQ campus wall.
- Need Confirmation list, if any.

If the user specifies one platform, generate only that platform's copy, but still perform fact extraction and quality gates first.

## Writing Principles

- Keep facts stable across platforms.
- Preserve uncertainty instead of inventing confirmations.
- Separate style references from fact sources.
- Adapt internal planning language into friendly public language.
- Make the voice campus-based, practical, warm, and slightly energetic.
- Avoid corporate SaaS tone, official bureaucratic tone, and exaggerated promises.
- Avoid leaking internal logistics, form fields, personal contacts, participant lists, unpublished project content, or staff arrangements.

## When Facts Are Missing

If a required fact is missing or tentative:

- For final publication: ask the user to confirm.
- For draft output: use explicit placeholders or uncertainty wording.

Examples:

- Use: `地点以报名群通知为准`
- Use: `[此处放报名二维码]`
- Do not use: a specific venue that is not in the fact table.

## QQ Reuse Policy

For v1, do not create a separate QQ copy by default.

Reuse the Xiaohongshu copy and materials for:

- QQ Channel
- QQ group notices
- QQ campus wall submissions

Only make light adaptation if the user asks, such as removing hashtags for a QQ group, shortening the copy for a group notice, or adding a campus-wall submission note.
