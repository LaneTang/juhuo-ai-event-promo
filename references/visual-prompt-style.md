# Visual Prompt Style

Use this reference when the user asks for cover images, posters, social media visuals, visual materials, image prompts, or v3 outputs.

v3 outputs image generation prompts first. Do not call image generation until the user confirms a prompt.

v3.1 has a deliberately narrow visual scope:

- Generate only a WeChat Official Account cover prompt and a Xiaohongshu poster prompt by default.
- Do not generate separate QQ channel, QQ group, campus wall, banner, story, thumbnail, or multi-size export prompts unless the user explicitly asks.
- If the user asks for "visual materials", "poster and cover", "配图", or a "full visual package", interpret that as exactly these two outputs: WeChat cover + Xiaohongshu poster.

## Core Rule

Visual prompts must be based on the fact-checked promotion package.

Use:

- event name
- event theme
- confirmed time
- confirmed or tentative location wording
- organizer
- platform purpose
- approved WeChat/Xiaohongshu copy tone

Do not invent:

- venue
- guest
- QR code
- sponsor/co-organizer
- award, result, funding, or commercial promise
- real photos of people unless the user provides/requests them

## Output Types

### WeChat Cover Prompt

Purpose:

Horizontal cover image for WeChat Official Account.

Recommended shape:

- primary size: 900 x 383 px
- aspect ratio: 2.35:1 horizontal
- optional high-resolution generation size: 1800 x 766 px, then downscale/crop to 900 x 383 px
- safe text area: keep important text inside the central 80% width and central 76% height
- strong title readability
- clear event identity
- not too much text
- works as a first impression above the article

Text budget:

- main title: 8-18 Chinese characters if possible
- subtitle: one short line
- optional time line: one short line
- no QR code, no long agenda, no dense body copy

Composition guidance:

- horizontal, article-cover first
- title must remain readable after WeChat list cropping/compression
- avoid placing critical text near edges
- leave enough breathing room around the title
- prioritize cover impact over full event detail

Prompt fields:

```markdown
## WeChat Cover Prompt

**Use case:** WeChat Official Account cover image
**Size:** 900 x 383 px
**Aspect ratio:** 2.35:1 horizontal
**Safe area:** central 80% width and central 76% height
**Main text:** ...
**Secondary text:** ...
**Optional time text:** ...
**Visual direction:** ...
**Composition:** ...
**Color palette:** ...
**Style details:** ...
**Negative prompt / avoid:** ...
```

### Xiaohongshu Poster Prompt

Purpose:

Vertical poster for Xiaohongshu note cover or feed image.

Recommended shape:

- primary size: 1242 x 1660 px
- aspect ratio: 3:4 vertical
- optional alternate size: 1080 x 1440 px
- safe text area: keep important text inside the central 84% width and central 86% height
- stronger social/community energy
- enough event info to be understood quickly
- still avoid text overload

Text budget:

- main title: 10-22 Chinese characters if possible
- subtitle: one short line
- info text: 2-3 short facts max, usually time / location wording / signup cue
- no full agenda, no long paragraph, no fake QR code

Composition guidance:

- vertical, mobile-feed first
- top third should carry the hook/title
- middle can carry visual scene or symbolic activity elements
- bottom third can hold time/location/sign-up cue
- leave clear margin for platform UI overlays and cropping

Prompt fields:

```markdown
## Xiaohongshu Poster Prompt

**Use case:** Xiaohongshu vertical poster
**Size:** 1242 x 1660 px
**Aspect ratio:** 3:4 vertical
**Safe area:** central 84% width and central 86% height
**Main text:** ...
**Secondary text:** ...
**Info text:** ...
**Visual direction:** ...
**Composition:** ...
**Color palette:** ...
**Style details:** ...
**Negative prompt / avoid:** ...
```

### QQ Material Reuse Note

Default:

QQ Channel, QQ groups, and QQ campus wall reuse the WeChat cover or Xiaohongshu poster materials. Do not generate separate QQ image prompts unless the user explicitly asks.

Recommended reuse:

- QQ group / QQ channel: reuse Xiaohongshu poster.
- QQ campus wall: reuse Xiaohongshu poster.
- If a horizontal preview is needed, reuse the WeChat cover.

## Style Direction

Default Juhuo AI visual tone:

- campus AI community
- warm but capable
- project practice / real collaboration
- not corporate SaaS
- not cold tech conference
- not bureaucratic campus notice

Useful visual directions:

- hand-made campus tech invitation
- maker workshop / project workbench
- academic lab field note
- energetic campus discussion scene
- from idea to working prototype

## Text Rules

Image text must be short and accurate.

Prefer:

- main title under 18 Chinese characters when possible
- one subtitle
- one short time line
- optional platform-friendly slogan

Avoid:

- full agenda
- long paragraphs
- tentative facts presented as confirmed
- too many hashtags
- QR code unless the actual QR image is provided
- small text near the image edge
- platform-irrelevant export sizes

## Confirmation Rule

After outputting prompts, ask for confirmation before image generation.

Use this wording:

```markdown
如果你确认，我可以基于其中某一条 prompt 继续生成图片。默认建议先生成小红书海报，因为它也可复用于 QQ 渠道。
```

Do not call image generation before confirmation.
