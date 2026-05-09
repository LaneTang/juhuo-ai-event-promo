# Visual Prompt Style

Use this reference when the user asks for cover images, posters, social media visuals, visual materials, image prompts, or v3 outputs.

v3 outputs image generation prompts first. Do not call image generation until the user confirms a prompt.

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

- aspect ratio: 2.35:1 or WeChat cover-friendly horizontal composition
- strong title readability
- clear event identity
- not too much text
- works as a first impression above the article

Prompt fields:

```markdown
## WeChat Cover Prompt

**Use case:** WeChat Official Account cover image
**Aspect ratio:** 2.35:1 horizontal
**Main text:** ...
**Secondary text:** ...
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

- aspect ratio: 3:4 or 4:5 vertical
- stronger social/community energy
- enough event info to be understood quickly
- still avoid text overload

Prompt fields:

```markdown
## Xiaohongshu Poster Prompt

**Use case:** Xiaohongshu vertical poster
**Aspect ratio:** 3:4 or 4:5 vertical
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

QQ Channel, QQ groups, and QQ campus wall reuse WeChat cover or Xiaohongshu poster materials. Do not generate separate QQ image prompts unless the user explicitly asks.

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

## Confirmation Rule

After outputting prompts, ask for confirmation before image generation.

Use this wording:

```markdown
如果你确认，我可以基于其中某一条 prompt 继续生成图片。默认建议先生成小红书海报，因为它也可复用于 QQ 渠道。
```

Do not call image generation before confirmation.
