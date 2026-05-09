---
name: juhuo-ai-event-promo
description: Use when creating Juhuo AI event promotion copy from an activity plan, Word/WPS document, or structured event brief for WeChat Official Account, Xiaohongshu, QQ channel/group/campus-wall reposts, or a full campus AI community promo package.
---

# Juhuo AI Event Promo

## Scope

Use this skill to turn a Juhuo AI event plan into a publishable promotion package.

v1 output focuses on mature, publishable copywriting:

- WeChat Official Account article copy. Default WeChat copy must be a complete 1200-2200 Chinese-character article when facts are sufficient, not a short event summary.
- Xiaohongshu post copy.
- QQ Channel, QQ group, and QQ campus wall reuse the Xiaohongshu copy and materials by default.

v2 supports WeChat Official Account HTML layout as an explicit downstream task.

v3 supports visual material prompts as an explicit downstream task. v3.1 narrows the default visual scope to exactly two deliverables: WeChat Official Account cover prompt and Xiaohongshu poster prompt.

v4 adds an intake step for broad package requests. If the user says only "生成宣传包" or another broad request without specifying outputs, ask what to generate before producing the package. If the user explicitly says "生成完整宣传包", "全套宣传包", or "全部都生成出来", generate the complete package without asking another scope question.

Do not generate WeChat HTML, posters, cover images, or image assets by default. If the user explicitly requests those assets, treat them as separate downstream tasks after the copy package is fact-checked. For v3, output image-generation prompts first and ask for confirmation before generating images. When the user asks for visual materials without naming a platform, output only the WeChat cover and Xiaohongshu poster prompts. Exception: complete package requests generate both final images directly after prompts.

## Core Rule

Treat the activity plan as the single source of truth. Do not write promotional copy before extracting a fact table and running quality gates.

If the user gives corrections outside the plan, record them as user-supplied facts and make conflicts visible.

If the user provides previous Juhuo posts or published drafts, use them as style references by default. Do not treat them as factual updates unless the user explicitly says they are newer confirmed facts.

## Workflow

1. Classify the request:
   - For broad "生成宣传包" requests without specified outputs, read `references/package-intake-flow.md` and ask the intake question before generating.
   - For "生成完整宣传包" or equivalent full-package requests, read `references/package-intake-flow.md` and proceed with the complete package defaults.
   - For specific platform/module requests, proceed only with that requested output.
2. Read the user's activity plan or structured brief.
3. Read `references/fact-table-schema.md`.
4. Extract a fact table with publicity levels and statuses.
5. Read `references/quality-gates.md`.
6. Run a quality gate report before writing copy.
7. If a `BLOCKER` affects final publication, ask for confirmation unless the user requests a placeholder draft.
8. Read platform references only for requested outputs:
   - WeChat: `references/wechat-copy-style.md` and `references/wechat-golden-copy-style.md`
   - Xiaohongshu and QQ reuse: `references/xiaohongshu-copy-style.md`
   - WeChat HTML layout: `references/wechat-html-layout.md`
     - When generating WeChat HTML, also read `references/article-to-html-mapping.md`, `references/frontend-design-core.md`, `references/wechat-frontend-design.md`, and `references/wechat-component-blueprints.md` before writing HTML.
   - Visual prompts / covers / posters: `references/visual-prompt-style.md`
9. Read `references/output-format.md`.
10. Generate the requested package.
11. Run a final consistency pass across all outputs:
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
- For legacy `.doc`, `.wps`, and `.wpt`, try external converters before Word COM when possible. Word COM may fail in non-interactive Codex environments with login-session errors. If all extraction methods fail, ask the user for a `.docx` version or pasted text instead of guessing.
- For `.pdf`, use a PDF text parser when available; otherwise use the script's Word COM fallback on Windows.
- Do not keep converter scratch files inside the final skill unless they are intentional examples or scripts.

## Default Output Behavior

If the user says "生成宣传包", "根据策划案写推文", or similar broad wording without specifying outputs, ask the package intake question from `references/package-intake-flow.md` before generating.

If the user chooses copy only, or asks for a normal copy package, generate the full v1 package:

- Fact table summary.
- Quality gate report.
- WeChat Official Account copy.
- Xiaohongshu copy.
- QQ reuse note for QQ Channel, QQ group, and QQ campus wall.
- Need Confirmation list, if any.

If the user specifies one platform, generate only that platform's copy, but still perform fact extraction and quality gates first.

If the user explicitly asks for "生成完整宣传包", "全套宣传包", "完整走一遍", or "全部都生成出来", generate the complete v4 package:

- Fact table summary.
- Quality gate report.
- WeChat Official Account mature article copy.
- Xiaohongshu copy.
- QQ reuse note.
- Three WeChat HTML versions: campus handmade tech invitation, maker geek workshop, and academic lab field notes.
- WeChat cover prompt.
- Xiaohongshu poster prompt.
- WeChat cover image.
- Xiaohongshu poster image.
- Need Confirmation list, if any.
- File manifest.

## WeChat Copy Behavior

Default WeChat copy must be a mature public article, not a notice or abstract.

Rules:

- Read both `references/wechat-copy-style.md` and `references/wechat-golden-copy-style.md`.
- Use the complete public/adaptable fact table, not only title/time/audience/CTA.
- Include a hook, scene-setting introduction, activity value, participant invitations, rules/notes, agenda explanations, time/location/registration, and closing invitation.
- Do not output a 500-800 character summary unless the user explicitly asks for a short version.
- If the article looks like an outline, event notice, QQ group notice, or fact summary, revise it before delivering.

## WeChat HTML Behavior

Only generate WeChat HTML when the user explicitly asks for HTML, 公众号排版, or a copyable WeChat backend layout.

Rules:

- Base the HTML on fact-checked WeChat copy.
- Read `references/wechat-html-layout.md`.
- Read `references/article-to-html-mapping.md`.
- Read `references/frontend-design-core.md`.
- Read `references/wechat-frontend-design.md`.
- Read `references/wechat-component-blueprints.md`.
- Use the full mature WeChat article as the HTML source. HTML must render the complete WeChat article, not generate a shorter version from a compressed summary, fact table, or rewritten copy.
- Before writing HTML, produce `Full Article Rendering Plan` and `Text Preservation Check`. Every substantive source text unit must appear in HTML.
- If any substantive text is omitted, rewritten, or summarized, revise the HTML before delivery. Do not shorten the article to make layout easier.
- Before writing HTML, select a component blueprint from `references/wechat-component-blueprints.md` for each requested style version.
- Before writing HTML, perform the internal WeChat frontend design pass: define purpose, audience, tone, bold aesthetic direction, differentiation, memorable motif, information hierarchy, component system, and compatibility translation.
- Output a `Frontend Design Plan`.
- Output a `Component Blueprint` that names the required first screen, heading system, participant blocks, rules/checklist, agenda/timeline, info block, QR placeholder, and CTA treatment.
- Output a `Frontend Design Capability Mapping` that translates frontend-design capabilities into WeChat-safe decisions.
- Output `WeChat Compatibility Translation` that explains how richer frontend ideas such as motion, hover states, external fonts, complex backgrounds, pseudo-elements, or assets become static inline HTML.
- Translate the design pass into WeChat-compatible static HTML. Keep the design ambition, but remove incompatible implementation techniques.
- Choose a style family from that reference unless the user specifies one.
- When generating multiple HTML style versions, make the versions structurally distinct. Do not deliver three outputs that only change palette, border colors, headings, or label text.
- For multi-style HTML output, run the style-drift gate: compare first screen, heading system, highlighted sentence, audience blocks, rules/checklist, agenda/timeline, info block, closing CTA, and QR placeholder treatment. If those areas are mostly identical, redesign before delivering.
- Do not output a generic template. The HTML should show intentional typography hierarchy, spacing rhythm, color discipline, section contrast, and a recognizable visual point of view.
- Keep the HTML static, mostly inline-style, and WeChat-compatible.
- Do not use JavaScript, animation, external CSS, or remote assets.

## Visual Prompt Behavior

Only generate visual prompts when the user explicitly asks for cover images, posters, social media visuals, image prompts, visual materials, or v3 outputs.

Rules:

- Read `references/visual-prompt-style.md`.
- Base prompts on the fact-checked promotion package, not raw assumptions.
- Output prompts for requested platforms.
- If the user asks for a full visual package, visual materials, poster/cover, 配图, or v3 outputs without naming a platform, output exactly two prompts: WeChat Cover Prompt and Xiaohongshu Poster Prompt.
- WeChat Cover Prompt must specify `900 x 383 px`, `2.35:1 horizontal`, and a safe text area.
- Xiaohongshu Poster Prompt must specify `1242 x 1660 px`, `3:4 vertical`, and a safe text area.
- QQ Channel, QQ group, and QQ campus wall reuse WeChat or Xiaohongshu visuals by default; do not create separate QQ prompts unless explicitly requested.
- Do not create extra banners, thumbnails, story images, QQ posters, or multi-size export prompts unless the user explicitly asks.
- Do not call image generation immediately for normal visual requests. Ask for confirmation after presenting prompts.
- For complete package requests, generate the WeChat cover image and Xiaohongshu poster image directly after producing their prompts.
- If the user confirms a specific prompt, then image generation can be used as a separate action.

## Writing Principles

- Default copy should be publication-ready, not a compressed summary. If the plan has enough public information, produce a complete article/post that the user can publish after filling only confirmed missing facts such as venue or QR code.
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
