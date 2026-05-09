# Quality Gates

This reference defines the checks that `juhuo-ai-event-promo` must run after extracting a fact table and before delivering promotional copy. The goal is not to make the writing cautious and dull. The goal is to make the copy accurate, publishable, and consistent across WeChat, Xiaohongshu, and the unified QQ channel post.

## Gate Result Levels

Use three result levels.

| Level | Meaning | Required Action |
|---|---|---|
| BLOCKER | The copy cannot be safely finalized. | Stop and ask the user for confirmation, or draft only with explicit placeholders/uncertainty if the user requested that. |
| WARNING | The copy can be drafted, but must use careful wording. | Continue, but include the issue in the final "Need Confirmation" note. |
| NOTE | The issue affects style, fit, or polish rather than factual safety. | Continue and improve the output if possible. |

## Required Gate Output

Before writing promotional copy, produce a short gate report:

```markdown
## Quality Gate Report

| Gate | Result | Issue | Action |
|---|---|---|---|
| Required Facts | BLOCKER | location is TENTATIVE | Ask for venue or write "地点以报名群通知为准" |
```

If all checks pass, still include:

```markdown
Quality gates passed. No blockers found.
```

For normal user-facing output, keep the report brief. For skill testing or debugging, include the full table.

## Gate 1: Source Readiness

Run this before trusting the fact table.

| Check | BLOCKER | WARNING | Action |
|---|---|---|---|
| Source exists and is readable | No readable plan or uploaded content exists. | File can be read but tables/sections are partially flattened. | Ask for the plan or tell the user extraction may be incomplete. |
| Source identity is clear | Multiple plans are present and the user did not specify which one is SSOT. | Filename suggests an old/draft version. | Ask which version to use, or mark version risk. |
| Extraction quality | Text is mostly unreadable or OCR-like. | Some table structure is lost but core facts are recoverable. | Do not invent missing table values; mark ambiguous fields. |
| User supplements are tracked | User gave corrections but they are not represented in `facts_added_outside_plan`. | User supplements are represented but conflict notes are weak. | Update the fact table before generating copy. |

## Gate 2: Required Public Facts

These fields must exist for a complete v1 promotion package.

Required fields:

- `event_full_name`
- `organizer`
- `event_date`
- `start_time`
- `end_time`
- `location`
- `location_status`
- `registration_method`
- `registration_status`
- `core_theme`
- `primary_audience`
- `core_segments`
- `agenda`

| Check | BLOCKER | WARNING | Action |
|---|---|---|---|
| Missing required fact | Any required field is `MISSING`. | A non-required but useful field is missing, such as deadline or cover visual note. | Ask for the missing fact unless the user requested placeholder drafts. |
| Tentative required fact | `location`, `time`, `registration_method`, or `registration_status` is `TENTATIVE`. | Optional fact is tentative, such as co-organizer or future activity list. | Preserve uncertainty or ask user to confirm. |
| Conflicting required fact | A required field is `CONFLICTING`. | Minor naming variants exist but meaning is same. | Stop and resolve the conflict before final copy. |
| Inferred required fact | A required field is only `INFERRED`. | Weekday or casual relative date is inferred. | Use exact date; avoid relative wording unless checked. |

## Gate 3: Publicity Filter

No public output should leak internal execution details.

| Check | BLOCKER | WARNING | Action |
|---|---|---|---|
| INTERNAL fact in public copy | Staff roles, worker arrival time, equipment list, internal form fields, internal follow-up database, or host script appears in final public copy. | A harmless internal detail appears indirectly, such as "我们会提前布置好现场". | Remove or adapt the detail. |
| SENSITIVE fact used as confirmed | Tentative venue, unconfirmed guest, undetermined co-organizer, personal contacts, or unpublished project details are written as confirmed. | Sensitive fact appears in generalized form. | Rewrite to preserve uncertainty or omit. |
| Privacy leakage | Personal contact fields, private WeChat IDs, participant lists, unpublished project content, or photo consent details are exposed. | Privacy is mentioned too heavily and makes the event feel risky. | Remove private fields; use a light reassurance only if needed. |
| Form field leakage | Full registration/feedback field schema appears in public copy. | Copy says "表单会收集基础信息" without listing sensitive details. | Keep public copy to registration method and purpose only. |

## Gate 4: Overclaim And Compliance

The event can sound exciting, but it must not promise outcomes the plan cannot guarantee.

| Check | BLOCKER | WARNING | Action |
|---|---|---|---|
| Guaranteed outcome | Copy promises guaranteed teammates, resources, awards, funding, commercialization, publication, revenue, or project success. | Copy strongly implies an outcome without guarantee. | Use "有机会", "可以交流", "可能找到", "一起探索". |
| Inflated authority | Copy claims official judging, expert review, certified training, or institutional endorsement not in the plan. | "专业评审" wording appears despite no formal judges. | Replace with "同学间建设性交流". |
| Guest overstatement | A guest, title, or topic is advertised but not confirmed in fact table. | Guest exists but source is user-supplied and not in plan. | Mark `USER_SUPPLIED`; ask if the guest can be publicized. |
| Commercial claim | Copy makes revenue, traffic, monetization, or entrepreneurial success claims not supported by the plan. | Copy uses business language that feels too commercial for a campus公益 activity. | Ground it in practical learning and project exploration. |

## Gate 5: Time, Date, And Relative Wording

Because event promotion is time-sensitive, date wording must be concrete.

| Check | BLOCKER | WARNING | Action |
|---|---|---|---|
| Relative date mismatch | Copy says "今天", "明天", "本周日", or "两天后" without checking against publication date. | Exact date is present but relative date is also used. | Use exact date by default. Add relative wording only when publication date is known. |
| Wrong weekday | Weekday does not match the event date. | Weekday is inferred but not marked. | Correct or remove weekday. |
| Time inconsistency | Different platforms show different start/end times. | One platform omits end time. | Normalize all platforms to the same time format. |
| Agenda mismatch | Agenda durations exceed or contradict the event time. | Agenda is summarized loosely. | Preserve the official schedule or write "以现场安排为准". |

## Gate 6: Cross-Platform Consistency

Run this after generating all requested channels.

| Check | BLOCKER | WARNING | Action |
|---|---|---|---|
| Core fact mismatch | Event name, date, time, location, registration method, or organizer differs across platforms. | A platform uses a shorter name but still clearly refers to same event. | Normalize facts immediately. |
| CTA mismatch | WeChat says scan QR, Xiaohongshu says comment/DM, QQ says directly arrive, with no factual basis. | Different CTAs are adapted but compatible. | Align CTA to confirmed registration method. |
| Audience mismatch | One platform invites groups excluded or deprioritized by the plan. | A platform overemphasizes one audience but remains accurate. | Rewrite to reflect the same audience policy. |
| Promise mismatch | One platform promises a stronger benefit than others. | Tone differs by platform but claims are aligned. | Reduce the strongest claim to match the fact table. |

## Gate 7: Platform Fit

Use these checks only for platforms requested by the user.

### WeChat Official Account

| Check | BLOCKER | WARNING | Action |
|---|---|---|---|
| Missing event basics | The article lacks time, location/location status, registration method, or organizer. | Basics appear only at the end and are easy to miss. | Add a clear "时间与地点/报名方式" section. |
| Too short for publication | Full WeChat article is only an outline or under about 1000 Chinese characters despite rich source facts. | Article is readable but omits useful background, rules, audience motivation, or agenda detail. | Expand into a publication-ready article using `wechat-copy-style.md`. |
| Low information density | Article ignores important public/adaptable facts such as background, roadshow rules, participant categories, agenda, or follow-up context. | Some facts are present but collapsed into generic bullets. | Reuse more fact-table content while preserving public/internal filters. |
| Too mechanical | Article reads like a copied策划案 with bureaucratic section names. | Some plan wording remains. | Rewrite as a campus invitation with narrative flow. |
| Weak hierarchy | Readers cannot quickly scan sections, audience, rules, and agenda. | Headings are present but repetitive. | Use numbered sections, highlighted quotes, cards, or checklists as appropriate. |
| Incompatible format request | User asks for WeChat HTML but output depends on animation, JS, external CSS, pseudo-elements, or remote assets. | Static HTML exists but styles are not mostly inline. | For HTML module, keep static, inline-style, WeChat-compatible layout. |

### WeChat HTML Layout

Use these checks when the user requests HTML or 微信公众号排版.

| Check | BLOCKER | WARNING | Action |
|---|---|---|---|
| Dynamic dependency | HTML uses JavaScript, animation, external CSS, external fonts, or remote assets as required layout elements. | Minor unsupported styling may be stripped by WeChat. | Rewrite as static inline-style HTML. |
| Design engine skipped | HTML is generated without reading `wechat-frontend-design.md`. | Design reference is read but only weakly reflected in output. | Read the internal design engine and regenerate design pass, capability mapping, and compatibility downgrade notes before writing HTML. |
| Missing design pass | HTML is generated directly without a prior WeChat frontend design pass. | Design pass exists but is too generic to guide layout. | Add a design pass covering purpose, audience, tone, bold aesthetic direction, differentiation, memorable motif, information hierarchy, component system, and compatibility translation before writing HTML. |
| Generic frontend pass | Design pass uses generic words such as "clean", "modern", or "tech" without a concrete visual concept, motif, component system, or differentiation. | Design pass has a concept but weak mapping to concrete components. | Rewrite the design pass with bold aesthetic direction, differentiation, motif, hierarchy, and component system. |
| Missing capability mapping | `Frontend Design Capability Mapping` is absent. | Mapping exists but does not cover typography, color/theme, spatial composition, background/details, and polish. | Map frontend-design capabilities into concrete WeChat-safe design decisions. |
| Missing compatibility downgrade | `Compatibility Downgrade Notes` are absent. | Notes exist but do not explain how motion, hover, external fonts, complex backgrounds, pseudo-elements, assets, or layout ideas become static inline HTML. | Add downgrade notes before HTML and ensure the HTML follows them. |
| Style not selected | No clear style family is chosen. | Style is mixed but still coherent. | Choose from `wechat-html-layout.md`: handmade tech invitation, maker geek, or academic lab field notes. |
| Generic AI aesthetics | Layout looks like interchangeable cards with weak hierarchy, timid palette, or no memorable visual idea. | Design is serviceable but not distinctive. | Rework with a clearer visual point of view, stronger first screen, recurring motif, and better spacing rhythm. |
| Style drift in multi-version output | Multiple style versions share the same layout skeleton and differ only by palette, border color, labels, or small decorative text. | Two versions have some shared structure but distinct key components. | Redesign at least one version so first screen, heading system, audience cards, rule block, agenda block, info block, and CTA visibly differ. |
| Over-narrow template | HTML repeats one fixed visual pattern and ignores event tone. | Components are coherent but too monotonous. | Vary element combinations within the selected style family. |
| Weak mobile readability | Text is cramped, too small, too wide, or likely to overflow on mobile. | A few dense sections need more spacing. | Increase line-height, spacing, and responsive block layout. |
| Fact drift | HTML changes or omits important approved facts. | Minor copy compression keeps meaning. | Align HTML with fact-checked WeChat copy. |
| Placeholder hidden | QR/location/registration placeholders are buried or styled as final facts. | Placeholder is visible but not listed in notes. | Make placeholders obvious and include copy/paste notes. |

### Xiaohongshu

| Check | BLOCKER | WARNING | Action |
|---|---|---|---|
| Too long | Copy is effectively a full article, not a note. | Copy has too many paragraphs before event info. | Shorten to hook, highlights, info, CTA, tags. |
| Weak hook | First 2 lines do not say who should care and why. | Hook is accurate but plain. | Lead with low-barrier campus invitation. |
| Too neutral | Copy reads like a generic activity notice and lacks社群/学长学姐 invitation energy. | Tone is friendly but not memorable. | Add a stronger hook, campus scene, and warmer closing line. |
| Searchability missing | No useful keywords, tags, or event terms. | Tags are generic. | Add tags such as AI实践, 大创, 校园活动, 组队, 炬火AI. |
| Tone mismatch | Copy sounds like official notice or corporate launch. | Slightly formal. | Make it friendlier, more direct, and lighter. |

### QQ Channel / QQ Group / QQ Campus Wall

| Check | BLOCKER | WARNING | Action |
|---|---|---|---|
| Wrong QQ behavior | A separate QQ copy is generated by default. | QQ output includes too much extra rewriting. | Default to reusing Xiaohongshu copy and materials; only add reuse notes. |
| Campus wall risk | Reused Xiaohongshu copy includes sensitive or unconfirmed internal details unsuitable for public wall submission. | Copy is public-safe but hashtags may need trimming. | Keep public-safe facts only; optional note says QQ groups may remove hashtags. |

## Gate 8: Juhuo AI Voice

These are style gates, not fact gates. They should improve copy without blocking delivery unless the mismatch is severe.

| Check | BLOCKER | WARNING | Action |
|---|---|---|---|
| Wrong identity | Copy makes the association sound like a company, training institution, incubator, or official authority. | Copy uses a few business/SaaS terms. | Reframe as campus AI research/practice community. |
| Too cold | Copy sounds like a tech conference press release. | Some sentences are stiff. | Add peer-to-peer invitation, concrete scene, and low-pressure language. |
| Too unserious | Copy becomes meme-like and weakens academic/practice credibility. | Emoji or jokes are slightly overused. | Keep friendly but purposeful. |
| Too bureaucratic | Copy follows策划书 wording too closely: "活动旨在", "为进一步", "形成沉淀" everywhere. | A few formal phrases remain. | Convert to natural student-facing language. |

## Gate 9: Output Completeness

Run this before final delivery.

| Check | BLOCKER | WARNING | Action |
|---|---|---|---|
| Requested platform missing | User asked for full package but one of WeChat/Xiaohongshu/QQ unified copy is missing. | Platform is present but too skeletal. | Generate the missing platform or explain why blocked. |
| Unresolved blockers hidden | The output silently ignores blockers. | Blockers are mentioned only vaguely. | Include a concise "Need Confirmation" list. |
| Placeholder misuse | Placeholder text looks like final copy, e.g. `[二维码]` buried without notice. | Placeholder exists but is clearly marked. | Surface placeholders near the end or in confirmation list. |
| No final consistency pass | Facts were generated but not checked against fact table. | Pass was informal. | Re-scan core facts across outputs. |

## Standard Actions

When a gate fails, use one of these actions.

| Situation | Action |
|---|---|
| Required fact missing and public copy cannot be accurate | Ask the user for the fact. |
| User wants draft despite missing facts | Use obvious placeholders and include a "Need Confirmation" list. |
| Fact is tentative | Preserve uncertainty exactly, e.g. "地点以报名群通知为准". |
| User-supplied update contradicts plan | Prefer the newest user-supplied update only after recording it in the fact table. |
| Sensitive/internal fact appears useful | Adapt it into generalized public language or omit it. |
| Channel tone is wrong but facts are safe | Revise tone without changing facts. |

## Example Gate Report For The Sample Plan

```markdown
## Quality Gate Report

| Gate | Result | Issue | Action |
|---|---|---|---|
| Required Facts | BLOCKER | `location` is tentative. | Ask for venue or write "地点以后续通知为准". |
| Required Facts | WARNING | Registration method is Feishu, but no QR/link is provided. | Use QR placeholder only if user asks for draft. |
| Publicity Filter | WARNING | Co-organizer is "未定". | Omit co-organizer from public copy. |
| Platform Fit | NOTE | WeChat needs a warmer student-facing narrative. | Convert plan wording into invitation style. |

Need confirmation before final publication:
- Confirm final venue.
- Provide registration QR/link.
- Confirm whether walk-in participation is allowed.
```
