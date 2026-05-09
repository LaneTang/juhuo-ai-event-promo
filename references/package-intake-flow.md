# Package Intake Flow

Use this reference when the user asks to "生成宣传包", "根据策划案做宣传", "做一套宣发", or similar broad package requests.

v4 turns the skill into an interactive final package generator. The key rule is simple:

- If the user asks for a normal promotion package but does not specify outputs, ask one short intake question before generating.
- If the user explicitly asks for a complete package, generate the full package without asking another scope question.
- If the user asks for a specific platform or module, generate only that requested module after fact extraction and quality gates.

## Request Classification

### Normal Package Request

Examples:

- "生成宣传包"
- "根据这个策划案做宣传包"
- "帮我做活动宣发"
- "做一套社媒宣传"

Behavior:

Ask a short intake question before generating content.

Recommended wording:

```markdown
我先确认一下这次要生成哪些内容：

1. 只生成宣传文案：微信公众号文案、小红书文案、QQ复用说明
2. 文案 + 公众号HTML：再选择一种HTML风格或三风格对比
3. 文案 + 视觉prompt：额外给公众号封面和小红书海报prompt
4. 文案 + HTML + 视觉prompt
5. 完整宣传包：文案 + 三风格公众号HTML + 视觉prompt + 实际生成公众号封面图和小红书海报图

如果要公众号HTML，请同时指定风格：校园手作科技邀请函 / 创客极客 / 学术实验室田野笔记 / 三风格对比。
```

If the user does not answer and asks you to decide, default to option 1 unless they used words like "完整", "全套", "所有物料", or "一次性全部".

### Complete Package Request

Examples:

- "生成完整宣传包"
- "生成全套宣传包"
- "全部都生成出来"
- "完整走一遍"

Behavior:

Generate the complete package without asking another scope question.

Default complete package contents:

- Fact table summary
- Quality gate report
- WeChat Official Account mature article copy
- Xiaohongshu copy
- QQ reuse note
- Three WeChat HTML versions
- WeChat cover prompt
- Xiaohongshu poster prompt
- WeChat cover image
- Xiaohongshu poster image
- Need Confirmation list
- File manifest

Complete package defaults:

- WeChat HTML style: three-style comparison
- WeChat cover: `900 x 383 px`
- Xiaohongshu poster: `1242 x 1660 px`
- QQ visual materials: reuse WeChat cover or Xiaohongshu poster
- Image generation: generate both images directly after prompts, without a second confirmation

### Specific Module Request

Examples:

- "只生成小红书文案"
- "只要公众号HTML"
- "给我公众号封面prompt"
- "生成小红书海报图"

Behavior:

Generate only the requested module, but still:

- read the plan
- extract facts
- run fact safety gates
- preserve missing/tentative facts

Do not generate unrequested HTML, prompts, or images.

## Output Routing

Use this routing after the intake decision is known:

| User choice | Outputs |
|---|---|
| Copy only | Fact summary, gates, WeChat copy, Xiaohongshu copy, QQ reuse note, Need Confirmation |
| Copy + HTML | Copy package, selected WeChat HTML style(s), HTML files |
| Copy + visual prompt | Copy package, WeChat cover prompt, Xiaohongshu poster prompt, QQ reuse note |
| Copy + HTML + visual prompt | Copy package, selected HTML style(s), visual prompts |
| Complete package | Full copy package, three HTML versions, visual prompts, two generated images, file manifest |
| Single platform/module | Only requested output plus fact safety report |

## File Output Defaults

When files are created, use stable descriptive filenames:

- Main package: `promo-package.md`
- Visual prompts: `visual-prompts.md`
- WeChat HTML:
  - `wechat-style-campus-handmade.html`
  - `wechat-style-maker-geek.html`
  - `wechat-style-academic-field-notes.html`
- Images:
  - `wechat-cover.png`
  - `xiaohongshu-poster.png`

If similar files already exist, add a short event slug or numeric suffix instead of overwriting unrelated user files.

## Image Generation Rule

Normal visual requests:

- Output prompts first.
- Ask for confirmation before generating images.

Complete package requests:

- Output prompts.
- Generate both images directly using those prompts.
- Record the generated image filenames in the file manifest.

Never generate image assets before fact checks.
