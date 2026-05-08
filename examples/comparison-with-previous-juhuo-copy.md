# Comparison With Previous Juhuo Copy

This compares `examples/sample-full-promo-pack.md` with the previous Juhuo WeChat and Xiaohongshu drafts provided by the user.

## Overall Finding

The previous Juhuo copy is stronger as a public-facing promotional draft. It is warmer, more confident, and more platform-native.

The new skill-generated sample is stronger as a controlled SSOT-based output. It avoids inventing facts, surfaces publication blockers, and keeps internal details out of public copy.

The best v1 behavior should combine both:

- Use the plan as the fact source.
- Use previous Juhuo posts as style references.
- Use user-supplied updates, such as confirmed venue, only when explicitly marked as newer facts.

## WeChat Comparison

| Dimension | Previous Juhuo WeChat Copy | Skill Sample | Analysis |
|---|---|---|---|
| Opening | Strong visual start: "炬火AI实践月启动：寻找被AI赋能的真实项目。" + `INVITATION`. | Direct but simpler: "炬火 AI 实践月启动。" | Previous version has stronger ceremony and invitation feel. The skill should preserve this kind of opening when generating final WeChat copy. |
| Tone | Warm, confident, polished: "一封给实干者的邀请信", "期待你的赴约". | Warmer than策划案, but more cautious because facts are unresolved. | Good safety, but final public draft can borrow the previous version's confidence once blockers are resolved. |
| Core angle | Very clear: from "AI工具怎么用" to "AI项目怎么做". | Same angle appears and is preserved. | This should become a reusable Juhuo AI signature angle. |
| Participant section | More vivid: "极客", "新手", "求贤若渴", "直接喊出你的需求". | More controlled and slightly flatter. | Skill should allow lively wording, but avoid guaranteed matching claims like "我们帮你现场对接" unless the plan supports it. |
| Rules section | Friendly and persuasive: "几个小小的规则", "绝不辜负你的热情". | Accurate, slightly procedural. | Previous style is better for WeChat. Keep the friendliness while preserving exact rule logic. |
| Activity info | Uses a confirmed venue: "西南大学(重庆)产业技术研究院2号楼701..." | Uses "地点以报名群通知为准". | The skill sample is correct for plan-only generation. The previous copy likely includes a later user-supplied update. The skill must record that as `USER_SUPPLIED` before using it. |
| Publication readiness | Feels close to publishable. | Clearly a draft with blockers. | This is expected: the sample follows quality gates. Final publication needs venue and QR. |

## Xiaohongshu Comparison

| Dimension | Previous Juhuo Xiaohongshu Copy | Skill Sample | Analysis |
|---|---|---|---|
| Platform fit | Very good: short, scannable, emoji bullets, immediate CTA. | Also scannable, but slightly more cautious and formal in places. | Previous copy is an excellent style exemplar for the skill. |
| Hook | "启动啦！" + direct invitation to AI×大创模拟路演. | "这周日，来现场看看 AI 怎么从工具箱变成真实项目。" | Both work. Previous is more community-notice-like; sample is more idea-led. |
| Length | Compact and highly repostable. | Similar, but includes QR placeholder and uncertainty. | For final posts, once facts are confirmed, prefer the previous compactness. |
| Audience clarity | Strong: four clear `📌` bullets. | Strong and similar. | This pattern should be retained as the default Xiaohongshu/QQ reuse structure. |
| CTA | "带上项目，或者带上好奇心。我们现场见！" | Same closing logic. | This is now a stable reusable ending. |
| Facts | Uses confirmed venue. | Preserves tentative venue. | Same issue as WeChat: old copy includes facts not in the plan. |
| Tags | Good mix of brand, campus, topic, action. | Reuses a similar tag pool. | Keep this tag pool in `xiaohongshu-copy-style.md`. |

## What The Skill Should Learn From Previous Copy

Keep these style traits:

- Invitation-first framing.
- A clear movement from "AI 工具" to "AI 项目".
- Low-pressure event identity: not答辩, no formal judge, real project discussion.
- Three audience groups explained in friendly language.
- Short Xiaohongshu bullets with `✅` and `📌`.
- Closing phrase: "带上项目，或者带上好奇心。"

Avoid or gate these risks:

- Do not use a confirmed venue unless it appears in the plan or user explicitly supplies it.
- Do not say "空降现场" unless walk-in policy is confirmed.
- Do not say "我们帮你现场对接" as a guaranteed result; safer wording is "现场一起聊聊对接可能".
- Do not mention co-organizer if it is `未定`.
- Do not imply formal guest/special topic if not in the plan.

## Recommended Adjustment For Future Runs

Before generating final copy, ask or accept a small "publication update block" from the user:

```markdown
更新事实：
- 地点：
- 报名二维码/链接：
- 是否允许未报名到场：
- 是否有嘉宾/特别分享：
- 是否有必须保留的标题或口号：
```

Then mark those as `USER_SUPPLIED` in the fact table and regenerate. This would let the skill produce copy closer to the previous Juhuo public draft while preserving the safety of SSOT checking.

