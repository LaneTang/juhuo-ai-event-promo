# juhuo-ai-event-promo

`juhuo-ai-event-promo` is a Codex skill for turning a Juhuo AI event plan into a complete campus promotion package.

It is designed for association/internal event operations where the activity plan is the single source of truth, and the final output needs to stay accurate across WeChat Official Account, Xiaohongshu, and QQ reposting channels.

## What It Does

Given a Word/WPS/PDF event plan, the skill helps Codex:

- extract a structured fact table from the plan
- identify confirmed, tentative, missing, internal, and sensitive facts
- run publicity quality gates before writing public copy
- generate mature, publication-ready WeChat Official Account article copy
- generate Xiaohongshu promotional copy
- reuse Xiaohongshu copy and visual materials for QQ Channel, QQ groups, and QQ campus wall
- generate copyable static WeChat HTML layout when requested
- generate WeChat cover and Xiaohongshu poster prompts/images when requested
- list facts that still need confirmation before publication

The skill is intentionally conservative about factual claims. It should not invent venues, registration links, guests, organizers, deadlines, QR codes, or benefits that are not present in the plan or explicitly supplied by the user.

## How It Works

The skill follows a fact-first workflow:

1. Classify the request.
2. Parse the activity plan.
3. Extract a fact table.
4. Run quality gates.
5. Generate requested copy, HTML, prompt, or image outputs.
6. Run a final consistency pass across all deliverables.

Broad package requests behave differently from complete package requests:

- If the user says only "生成宣传包", Codex first asks which outputs to generate.
- If the user says "生成完整宣传包", Codex generates the full deliverable set by default.
- If the user asks for one platform or one module, Codex generates only that requested output after fact checks.

## Install

Use your Codex skill installer with this repository:

```text
https://github.com/LaneTang/juhuo-ai-event-promo
```

If using the Codex skill installer script directly, the command is typically shaped like:

```powershell
python install-skill-from-github.py --repo LaneTang/juhuo-ai-event-promo --path .
```

After installation, ask Codex to use the skill on an uploaded event plan.

## Usage

Ask for a scoped package:

```text
请使用 juhuo-ai-event-promo，根据我上传的活动策划案生成宣传包。
```

Codex should first ask what outputs to generate.

Ask for the full package:

```text
请使用 juhuo-ai-event-promo，根据我上传的活动策划案生成完整宣传包。
```

Codex should generate copy, three WeChat HTML layouts, visual prompts, WeChat cover image, Xiaohongshu poster image, and a file manifest.

Ask for a single module:

```text
请使用 juhuo-ai-event-promo，只根据这份策划案生成小红书文案。
```

Codex should still extract facts and run quality gates, but it should not generate unrequested HTML or images.

## Outputs

Copy package:

- Fact Table Summary
- Quality Gate Report
- 微信公众号文案
- 小红书文案
- QQ 渠道复用说明
- Need Confirmation

WeChat HTML layout:

- Frontend Design Plan
- Full Article Rendering Plan
- Text Preservation Check
- Component Blueprint
- Frontend Design Capability Mapping
- WeChat Compatibility Translation
- WeChat HTML Style Choice
- 微信公众号 HTML
- Copy/Paste Notes

Visual materials:

- Visual Prompt Fact Check
- WeChat Cover Prompt
- Xiaohongshu Poster Prompt
- QQ Material Reuse Note
- Image Generation Confirmation, except when the user explicitly requests a complete package

Complete package:

- copy package
- three WeChat HTML files
- visual prompts
- `wechat-cover.png`
- `xiaohongshu-poster.png`
- file manifest

## Runtime Requirements

For `.docx` and `.docm` plans, the extraction script uses Python standard library modules only.

For legacy `.doc`, `.wps`, or `.wpt` files, the script tries several methods:

1. LibreOffice / `soffice`
2. `pandoc`
3. `antiword` / `catdoc`
4. Python `olefile` string fallback
5. Word-compatible COM automation on Windows

Recommended Python fallback for old `.doc` files:

```powershell
python -m pip install olefile
```

Word COM fallback requires:

- Windows
- Microsoft Word or another compatible application that can open the document
- `pywin32`

Optional dependencies can be installed with:

```powershell
python -m pip install -r requirements-optional.txt
```

For better PDF text extraction, install `pypdf`:

```powershell
python -m pip install pypdf
```

If `.doc` extraction fails with a login-session error such as `指定的登录会话不存在`, install `olefile`, convert the file to `.docx`, install LibreOffice, or paste the plan text directly.

See [runtime-requirements.md](references/runtime-requirements.md) for details.

## Repository Layout

```text
juhuo-ai-event-promo/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── fact-table-schema.md
│   ├── article-to-html-mapping.md
│   ├── frontend-design-core.md
│   ├── package-intake-flow.md
│   ├── quality-gates.md
│   ├── output-format.md
│   ├── runtime-requirements.md
│   ├── visual-prompt-style.md
│   ├── wechat-component-blueprints.md
│   ├── wechat-copy-style.md
│   ├── wechat-frontend-design.md
│   ├── wechat-golden-copy-style.md
│   ├── wechat-html-layout.md
│   └── xiaohongshu-copy-style.md
├── scripts/
│   └── extract_plan_text.py
├── examples/
│   ├── sample-complete-package-output.md
│   ├── sample-fact-table.md
│   ├── sample-file-manifest.md
│   ├── sample-full-promo-pack.md
│   ├── sample-intake-dialogue.md
│   ├── sample-visual-prompts.md
│   └── sample-wechat-html.md
└── requirements-optional.txt
```

## Examples

The `examples/` directory contains compact reference outputs for:

- fact table extraction
- copy package structure
- package intake dialogue
- complete package output
- file manifest
- visual prompts
- WeChat HTML layout

## Safety Rules

- Treat the activity plan as the single source of truth.
- Preserve uncertainty instead of inventing confirmations.
- Never expose internal logistics, private contacts, unpublished participant information, or sensitive form fields.
- Do not promise guaranteed teammates, funding, awards, revenue, traffic, or project success.
- Do not invent QR codes, venues, guests, sponsors, co-organizers, or logos.
- QQ channels reuse Xiaohongshu copy and WeChat/Xiaohongshu visual materials by default.
- WeChat HTML must render the full approved article, not a summary.
- Visual materials should be concise, hierarchical, and platform-sized.
