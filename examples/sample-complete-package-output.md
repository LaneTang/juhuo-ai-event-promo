# Sample Complete Package Output

This sample shows the expected structure when the user explicitly asks for a complete package.

## User

```text
请使用 juhuo-ai-event-promo，根据我上传的活动策划案生成完整宣传包。
```

## Expected Output Shape

```markdown
# Juhuo AI Complete Event Promo Package

## Fact Table Summary

Summarize public confirmed facts, tentative facts, and missing facts.

## Quality Gate Report

Brief table with blockers, warnings, and actions.

## 微信公众号文案

Full mature WeChat article, not a short summary.

## 小红书文案

Short social copy with campus community tone.

## QQ 渠道复用说明

QQ频道、QQ群、QQ校园墙默认复用小红书文案和小红书海报。

## 公众号 HTML

Generated files:

- `wechat-style-campus-handmade.html`
- `wechat-style-maker-geek.html`
- `wechat-style-academic-field-notes.html`

## Visual Prompts

Include:

- WeChat Cover Prompt: `900 x 383 px`, `2.35:1`, safe area, hierarchy
- Xiaohongshu Poster Prompt: `1242 x 1660 px`, `3:4`, safe area, hierarchy

## Generated Images

Generated files:

- `wechat-cover.png`
- `xiaohongshu-poster.png`

## File Manifest

List every generated markdown, HTML, and image file.

## Need Confirmation

List unresolved facts such as final venue, QR code, registration link, or public guest permission.
```

## Notes

- Complete package requests do not need another scope-confirmation question.
- The HTML must render the full WeChat article.
- The generated images must follow the visual prompts and must not invent QR codes, venues, guests, sponsors, or logos.
