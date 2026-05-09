# Output Format

Use this reference to format `juhuo-ai-event-promo` outputs.

## Default Full Package

When the user does not specify a platform, output:

```markdown
# Juhuo AI Event Promo Package

## Fact Table Summary

Short summary of the most important public facts and risky facts.

## Quality Gate Report

Brief gate table. Include blockers, warnings, and actions.

## 微信公众号文案

Full publication-ready WeChat article copy. Default output should be a mature article, not a short event summary.

## 小红书文案

Short Xiaohongshu post.

## QQ 渠道复用说明

State that QQ Channel, QQ group notices, and QQ campus wall submissions reuse the Xiaohongshu copy and materials by default. If useful, add tiny platform notes such as "QQ群可去掉话题标签".

## Need Confirmation

List unresolved facts before final publication.
```

## Single Platform Output

When the user requests only one platform, output:

```markdown
## Fact Check Summary

Only the facts and risks that affect this platform.

## Quality Gate Report

Brief gate result.

## Platform Copy

The requested copy.

## Need Confirmation

Only if needed.
```

## WeChat HTML Output

When the user explicitly requests WeChat HTML layout, output:

````markdown
## Fact Check Summary

Only facts and risks relevant to the WeChat article.

## Quality Gate Report

Include copy and HTML compatibility gates.

## Frontend Design Plan

Purpose, audience, tone, bold aesthetic direction, differentiation, memorable motif, information hierarchy, component system, and compatibility translation. This internal WeChat frontend design pass must happen before HTML generation.

## Full Article Rendering Plan

Explain how the complete approved WeChat article will be rendered into HTML without summarizing or omitting substantive text.

## Text Preservation Check

Report source text units, rendered text units, omitted substantive units, rewritten/summarized units, and PASS/FAIL. Omitted and rewritten/summarized units must be 0.

## Component Blueprint

Selected blueprint and concrete component decisions for first screen, intro, golden sentence, headings, participant blocks, rules/checklist, agenda/timeline, info block, QR placeholder, and CTA.

## Frontend Design Capability Mapping

Map purpose, tone, bold aesthetic direction, differentiation, typography, color/theme, spatial composition, background/visual details, and polish into concrete WeChat-safe design decisions.

## WeChat Compatibility Translation

Explain how richer frontend ideas such as motion, hover states, external fonts, complex backgrounds, pseudo-elements, SVG/icons, fixed layout, or remote assets are translated into static inline HTML.

## WeChat HTML Style Choice

Chosen style family and why.

## 微信公众号 HTML

```html
...
```

## Copy/Paste Notes

Static, inline-style based, no JS/animation/external CSS. List QR placeholders or facts that still need confirmation.
````

For multi-style HTML comparison, repeat `Frontend Design Plan`, `Full Article Rendering Plan`, `Text Preservation Check`, `Component Blueprint`, `Frontend Design Capability Mapping`, `WeChat Compatibility Translation`, `WeChat HTML Style Choice`, `微信公众号 HTML`, and `Copy/Paste Notes` for each style version, then add:

```markdown
## Style Difference Summary

Compare how the versions differ in first screen, heading system, highlighted sentence, audience cards, rules block, agenda block, info block, and closing CTA. If the versions only differ by colors or labels, redesign before delivery.
```

## Placeholder Rules

Use clear placeholders only when the user wants a draft despite missing facts.

Approved placeholders:

- `[此处放报名二维码]`
- `[此处填写报名链接]`
- `地点以报名群通知为准`
- `活动地点待确认`

Do not hide placeholders inside polished final copy without also listing them in `Need Confirmation`.

## Final Consistency Note

When delivering a completed package, add a short note:

```markdown
Consistency check: time, location, registration method, audience, and CTA are aligned across requested platforms.
```

If not aligned because facts are missing or tentative, state that clearly.

## Visual Prompt Output

When the user explicitly requests cover images, posters, visual materials, image prompts, or v3 outputs, output:

```markdown
## Visual Prompt Fact Check

Facts that may appear in images, plus tentative/missing facts that must not be shown as confirmed.

## WeChat Cover Prompt

**Use case:** WeChat Official Account cover image
**Size:** 900 x 383 px
**Aspect ratio:** 2.35:1 horizontal
**Safe area:** central 80% width and central 76% height
**Main text:** ...
**Secondary text:** ...
**Optional time text:** ...
**Hierarchy:** dominant element / secondary element / optional metadata
**Visual direction:** ...
**Composition:** ...
**Color palette:** ...
**Style details:** ...
**Negative prompt / avoid:** ...

## Xiaohongshu Poster Prompt

**Use case:** Xiaohongshu vertical poster
**Size:** 1242 x 1660 px
**Aspect ratio:** 3:4 vertical
**Safe area:** central 84% width and central 86% height
**Main text:** ...
**Secondary text:** ...
**Info text:** ...
**Hierarchy:** dominant element / secondary element / optional metadata
**Visual direction:** ...
**Composition:** ...
**Color palette:** ...
**Style details:** ...
**Negative prompt / avoid:** ...

## QQ Material Reuse Note

State that QQ channels reuse WeChat/Xiaohongshu visual materials by default.

## Image Generation Confirmation

Ask the user to confirm which prompt to generate before calling image generation.
```

If the user asks for only one platform, output only that platform's visual prompt plus confirmation.

Do not output extra visual prompts for QQ, banners, thumbnails, story images, or multi-size exports unless the user explicitly asks for them.
