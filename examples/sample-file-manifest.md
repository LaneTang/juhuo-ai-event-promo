# Sample File Manifest

Use this manifest shape when a complete package or file-generating workflow creates multiple artifacts.

```markdown
## File Manifest

| File | Type | Purpose | Notes |
|---|---|---|---|
| promo-package.md | Markdown | Main promotion package | Includes fact summary, gates, copy, QQ reuse note, prompts, and confirmation items |
| visual-prompts.md | Markdown | Visual prompt archive | May be omitted if prompts are included in `promo-package.md` |
| wechat-style-campus-handmade.html | HTML | WeChat layout style A | Campus handmade tech invitation |
| wechat-style-maker-geek.html | HTML | WeChat layout style B | Maker geek workshop |
| wechat-style-academic-field-notes.html | HTML | WeChat layout style C | Academic lab field notes |
| wechat-cover.png | Image | WeChat Official Account cover | 900 x 383 px |
| xiaohongshu-poster.png | Image | Xiaohongshu poster | 1242 x 1660 px |
```

Rules:

- Use readable file names.
- Add an event slug or numeric suffix if a file already exists.
- Do not overwrite unrelated user files.
- List every generated artifact, including images.
