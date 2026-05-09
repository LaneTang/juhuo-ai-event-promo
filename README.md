# juhuo-ai-event-promo

> **输入一份活动策划案，只需要一句话，生成全套的炬火 AI 社媒矩阵宣传包。**
> **Upload an event plan and get a complete Juhuo AI social media promotion package with just one sentence.**

`juhuo-ai-event-promo` is a reusable agent workflow for turning a Juhuo AI event plan into a fact-checked, publication-ready campus promotion package.

It is designed for association event operations where the activity plan is the single source of truth, and the final package needs to stay accurate across WeChat Official Account, Xiaohongshu, QQ reposting channels, HTML layout, and visual materials.

## From Plan To Promo Package

| Input | Output |
|---|---|
| Word / WPS / PDF activity plan | Fact table and quality gate report |
| Confirmed event facts | WeChat Official Account article |
| Campus activity tone | Xiaohongshu post and QQ reuse note |
| Approved WeChat article | Copyable static WeChat HTML |
| Visual direction | WeChat cover and Xiaohongshu poster prompt/image |
| Missing or tentative facts | Need Confirmation list |

The workflow is intentionally conservative about factual claims. It should not invent venues, registration links, guests, organizers, deadlines, QR codes, logos, or benefits that are not present in the plan or explicitly supplied by the user.

## What You Get

| Module | Deliverables |
|---|---|
| Copy package | Fact Table Summary, Quality Gate Report, 微信公众号文案, 小红书文案, QQ 渠道复用说明, Need Confirmation |
| WeChat HTML layout | Full-article static HTML, frontend design plan, component blueprint, compatibility notes |
| Visual materials | WeChat cover prompt/image, Xiaohongshu poster prompt/image, QQ reuse note |
| Complete package | Copy package, three WeChat HTML styles, visual prompts, generated images, file manifest |

Default platform behavior:

- WeChat receives a mature long-form article, not a short event notice.
- Xiaohongshu receives a shorter, warmer, more social post.
- QQ Channel, QQ groups, and QQ campus wall reuse Xiaohongshu copy and WeChat/Xiaohongshu visual materials by default.
- Visual materials are limited to one WeChat cover and one Xiaohongshu poster unless the user explicitly asks for more.

## How It Works

1. Classify the request.
2. Parse the activity plan.
3. Extract a fact table.
4. Run quality gates.
5. Generate the requested copy, HTML, prompt, or image outputs.
6. Run a final consistency pass across all deliverables.

Broad and complete package requests are handled differently:

- If the user says only `生成宣传包`, the agent first asks which outputs to generate.
- If the user says `生成完整宣传包`, the agent generates the full deliverable set by default.
- If the user asks for one platform or one module, the agent generates only that requested output after fact checks.

## Quick Start

Install or attach this repository to your agent platform, then ask:

```text
请使用 juhuo-ai-event-promo，根据我上传的活动策划案生成宣传包。
```

For the complete workflow:

```text
请使用 juhuo-ai-event-promo，根据我上传的活动策划案生成完整宣传包。
```

For a single module:

```text
请使用 juhuo-ai-event-promo，只根据这份策划案生成小红书文案。
```

## Cross-Platform Use

This repository is written as a portable instruction pack: `SKILL.md` is the main entrypoint, `references/` contains the workflow rules, `scripts/` contains helper tooling, and `examples/` contains compact reference outputs.

| Platform | Recommended use | Notes |
|---|---|---|
| Codex | Use as a skill repository | This is the primary packaging style for the current repo. |
| Claude Code | Use as a Skills directory | Copy or install the folder under `~/.claude/skills/juhuo-ai-event-promo/` or project `.claude/skills/`. The `SKILL.md` + YAML frontmatter structure matches Claude Skills conventions. |
| Cursor | Use as project rules/context | Reference `SKILL.md` and the key `references/` files from `.cursor/rules` or `AGENTS.md`. Cursor rules are not the same as Codex/Claude Skills, so treat this repo as an instruction source. |
| CodeBuddy | Use as rules or skill context | Adapt the workflow through `.codebuddy/rules`, `CODEBUDDY.md`, or `.codebuddy/skills/`, depending on the workspace setup. |
| Trae | Use as rules/context material | Reference the workflow through project rules or context. Do not assume native automatic Skill discovery unless the platform setup explicitly supports it. |

Useful platform docs:

- [Claude Code Skills](https://docs.claude.com/en/docs/claude-code/skills)
- [Claude Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)
- [Cursor Rules](https://docs.cursor.com/en/context)
- [CodeBuddy Overview](https://www.codebuddy.ai/docs/ide/User-guide/Overview)
- [CodeBuddy Rules](https://www.codebuddy.ai/docs/zh/ide/User-guide/Rules)
- [Trae rules note](https://traeide.com/news/6)

Compatibility notes:

- Native loading behavior differs by platform.
- Image generation, file creation, and script execution depend on the target agent's tools and permissions.
- `.doc`, `.wps`, and `.pdf` extraction requires local Python/tool access; if unavailable, paste the extracted plan text directly.
- The workflow can still be used as plain instructions even when the platform does not support Skills as a first-class feature.

## Output Matrix

| Request | Expected behavior |
|---|---|
| `生成宣传包` | Ask which outputs to generate before writing content |
| `生成完整宣传包` | Generate copy, three WeChat HTML styles, visual prompts, images, and file manifest |
| `只生成微信公众号文案` | Generate only WeChat copy after fact checks |
| `只生成小红书文案` | Generate only Xiaohongshu copy after fact checks |
| `生成公众号HTML` | Generate HTML from the full approved WeChat article |
| `生成视觉物料prompt` | Generate WeChat cover and Xiaohongshu poster prompts first |
| `生成小红书海报图` | Generate or prepare the Xiaohongshu poster according to platform size and fact safety rules |

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
