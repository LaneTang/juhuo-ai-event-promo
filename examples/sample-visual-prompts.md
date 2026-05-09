# Sample Visual Prompts

This sample demonstrates prompt-only visual output for a Juhuo AI event. It should not trigger image generation until the user confirms one prompt. The default visual package contains only a WeChat Official Account cover and a Xiaohongshu poster.

## Visual Prompt Fact Check

- Event: 炬火 AI 实践月｜“AI×”分享会#1 大创专题暨模拟路演
- Theme: AI 从工具体验走向真实项目实践
- Time: 2026 年 5 月 10 日 14:00-17:00
- Location: 以报名群通知为准
- Organizer: 炬火 AI 研究协会
- Missing: final QR/link

Do not show a specific venue or QR code as confirmed.

## WeChat Cover Prompt

**Use case:** WeChat Official Account cover image
**Size:** 900 x 383 px
**Aspect ratio:** 2.35:1 horizontal
**Safe area:** central 80% width and central 76% height
**Main text:** 实践月开启
**Secondary text:** 从一个想法，到一个作品
**Optional time text:** 05.10
**Hierarchy:** dominant element = "实践月开启" in large type; secondary element = "从一个想法，到一个作品"; optional metadata = tiny date tag only
**Visual direction:** campus AI community invitation, warm but capable, project practice atmosphere
**Composition:** 900 x 383 horizontal cover, one large title inside the safe area, generous whitespace, small date tag, background showing abstract students around a project table, subtle AI interface fragments, no real faces, no critical text near edges
**Color palette:** light blue, warm yellow, ink black, clean white
**Style details:** hand-made tech invitation feel, marker highlight, paper note textures, clear title hierarchy, polished WeChat cover
**Negative prompt / avoid:** no QR code, no exact venue, no corporate SaaS dashboard, no cold conference stage, no dense text, no fake sponsor logos

## Xiaohongshu Poster Prompt

**Use case:** Xiaohongshu vertical poster
**Size:** 1242 x 1660 px
**Aspect ratio:** 3:4 vertical
**Safe area:** central 84% width and central 86% height
**Main text:** AI 实战项目
**Secondary text:** 从工具箱，到作品
**Info text:** 05.10 下午｜扫码/报名见正文
**Hierarchy:** dominant element = "AI 实战项目" as the largest visual anchor; secondary element = short slogan; optional metadata = one small bottom tag
**Visual direction:** energetic campus community poster, friendly senior-student invitation, maker workshop energy
**Composition:** 1242 x 1660 vertical poster, large title in the top safe area, mid-frame project table / notes / laptop / sticky labels, small bottom tag for time and sign-up cue, leave generous quiet space and margins for mobile platform cropping
**Color palette:** light blue, ink black, warm yellow
**Style details:** youthful campus club poster, hand labels, checklist marks, subtle tech grid, readable mobile text
**Negative prompt / avoid:** no long agenda, no fake QR code, no exact venue, no celebrity/guest portrait, no overly commercial startup pitch style

## QQ Material Reuse Note

QQ Channel, QQ groups, and QQ campus wall reuse the WeChat cover or Xiaohongshu poster. Default recommendation: use the Xiaohongshu poster for QQ campus wall and group sharing because it contains more event info. Do not generate a separate QQ visual unless explicitly requested.

## Image Generation Confirmation

如果你确认，我可以基于其中某一条 prompt 继续生成图片。默认建议先生成小红书海报，因为它也可复用于 QQ 渠道。
