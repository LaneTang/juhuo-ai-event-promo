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

Full WeChat article copy.

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
