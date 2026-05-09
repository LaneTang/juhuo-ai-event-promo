# Sample v4 Intake Dialogue

This sample shows the expected behavior when the user asks for a broad promotion package without specifying outputs.

## User

```text
请使用 juhuo-ai-event-promo，根据我上传的活动策划案生成宣传包。
```

## Expected Assistant Response

```markdown
我先确认一下这次要生成哪些内容：

1. 只生成宣传文案：微信公众号文案、小红书文案、QQ复用说明
2. 文案 + 公众号HTML：再选择一种HTML风格或三风格对比
3. 文案 + 视觉prompt：额外给公众号封面和小红书海报prompt
4. 文案 + HTML + 视觉prompt
5. 完整宣传包：文案 + 三风格公众号HTML + 视觉prompt + 实际生成公众号封面图和小红书海报图

如果要公众号HTML，请同时指定风格：校园手作科技邀请函 / 创客极客 / 学术实验室田野笔记 / 三风格对比。
```

## Notes

- Do not start generating copy before the user chooses scope.
- Do not ask this question if the user explicitly says "完整宣传包" or "全部都生成出来".
- If the user asks for only one module, skip intake and generate only that module after fact checks.
