# Fact Table Schema

This reference defines how `juhuo-ai-event-promo` extracts structured facts from a Juhuo AI event plan. The event plan, usually a Word/WPS document, is the single source of truth. Do not generate promotional copy before producing the fact table and checking fact status.

## Purpose

The fact table turns an internal event plan into a controlled source for public promotional writing.

Use it to:

- Separate confirmed public facts from internal execution details.
- Preserve uncertainty when the plan says "tentative", "TBD", "未定", or "以后续通知为准".
- Prevent hallucinated event details.
- Make WeChat, Xiaohongshu, and QQ-channel copy consistent.
- Record facts added by the user outside the plan.

## Core Rule

Always treat the uploaded Word/WPS event plan as the SSOT unless the user explicitly provides a correction or supplement.

If the user provides information outside the plan, mark it as `USER_SUPPLIED` and include it in `facts_added_outside_plan`.

Do not silently replace tentative facts with confident facts.

## Publicity Levels

Assign every extracted fact one publicity level.

### PUBLIC

The fact can be used directly in public promotional copy.

Examples:

- Activity name
- Activity time
- Confirmed activity location
- Organizer
- Target participants
- Core agenda
- Registration method
- Route/presentation rules if intended for participants
- Snacks/drinks if intended to attract participants

### ADAPT

The fact should not be copied verbatim, but can be transformed into friendlier promotional language.

Examples:

- "建立 AI+大创项目实践的活动标签" -> "这次想把 AI 从工具体验推进到真实项目实践"
- "发现持续参与 AI 实践、项目开发和组织共建的同学" -> "也欢迎想持续参与 AI 实践的同学来认识大家"
- "资料与意向整理" -> "后续也会继续组织实践月系列活动"

### INTERNAL

The fact is for internal execution and should not appear in public promotional copy unless the user explicitly asks.

Examples:

- Staff roles
- Worker arrival time
- Equipment checklist
- Photography assignment
- Logistics details
- Host script preparation
- Feedback form field design
- Registration form field design
- Internal follow-up database or participant pool management

### SENSITIVE

The fact concerns privacy, uncertainty, unpublished project content, contact collection, or risk-prone claims. It must be handled carefully.

Examples:

- Tentative location
- Undetermined co-organizer
- Personal contact collection
- Photography/recording consent
- Unpublished project content
- External teams if participation policy is unclear
- Guest identity if not confirmed
- Claims about benefits, opportunities, or outcomes that could be overstated

## Fact Status

Assign every extracted fact one status.

### CONFIRMED

The plan clearly states the fact without uncertainty.

Example:

```text
活动时间：2026 年 5 月 10 日 14:00-17:00
```

### TENTATIVE

The plan marks the fact as tentative, undetermined, pending approval, or subject to later notice.

Trigger words:

```text
暂定
未定
待定
以后续通知为准
以报名群通知为准
最终地点将另行通知
后续确认
备选
```

### MISSING

The plan does not provide the fact.

### CONFLICTING

The plan contains two or more inconsistent values for the same fact.

Examples:

- Cover says location is "未定", body says a specific room.
- Agenda says 4 groups, notes say 5 groups, with no clarification.

### INFERRED

The fact is inferred from context but not explicitly stated. Do not use as a confirmed public fact.

Example:

- Inferring "本周日" from a date without checking current publication date.
- Inferring "允许空降" from casual wording without explicit policy.

### USER_SUPPLIED

The user provides the fact outside the plan, such as in chat, an updated note, or a correction.

Example:

```text
User says: 活动地点改为西南大学产业技术研究院 2 号楼 701。
```

## Field Record Format

Use this record shape for important fields, especially required facts and risky facts.

```text
field:
value:
source:
publicity_level:
status:
notes:
```

Example:

```text
field: location
value: 活动地点暂定。备选方向包括校内会议厅、双创院相关活动空间，或校外孵化园路演厅。
source: 四、活动地点
publicity_level: SENSITIVE
status: TENTATIVE
notes: Do not write a confirmed location in final copy. Ask user for update or preserve "以报名群通知为准".
```

For compact output, a markdown table is acceptable:

```markdown
| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|
| location | 活动地点暂定... | 四、活动地点 | SENSITIVE | TENTATIVE | 需确认后再公开 |
```

## Required Fact Groups

Extract facts into the groups below.

### A. Source Metadata

These fields help track where the facts came from.

| Field | Required | Publicity | Description |
|---|---:|---|---|
| source_file | yes | INTERNAL | Original document path or filename. |
| extraction_date | yes | INTERNAL | Date of fact extraction. |
| document_title | yes | INTERNAL | Title found in the plan. |
| document_version | no | INTERNAL | Version marker if present in filename or document. |
| confidence_notes | no | INTERNAL | Notes about extraction quality, OCR issues, or ambiguous document structure. |

### B. Event Basics

These are the most important public facts.

| Field | Required | Default Publicity | Description |
|---|---:|---|---|
| event_full_name | yes | PUBLIC | Full official activity name. |
| event_short_name | no | PUBLIC | Short name for titles and social copy. |
| series_name | no | PUBLIC | Parent series, e.g. "炬火 AI 实践月". |
| session_number | no | PUBLIC | Session number, e.g. "AI×分享会#1". |
| organizer | yes | PUBLIC | Main organizer. |
| co_organizer | no | PUBLIC/SENSITIVE | Co-organizer. Mark SENSITIVE if "未定". |
| event_type | no | PUBLIC | Workshop, salon, sharing session, simulated roadshow, hackathon, etc. |
| event_date | yes | PUBLIC | Calendar date. |
| weekday | no | PUBLIC/INFERRED | Weekday. If not stated, compute only if safe and mark INFERRED unless user confirms. |
| start_time | yes | PUBLIC | Start time. |
| end_time | yes | PUBLIC | End time. |
| location | yes | PUBLIC/SENSITIVE | Activity location. Mark SENSITIVE if tentative. |
| location_status | yes | SENSITIVE | Confirmed/tentative/missing/conflicting. |
| registration_method | yes | PUBLIC/SENSITIVE | QR code, link, Feishu form, group registration, walk-in, etc. |
| registration_status | yes | SENSITIVE | Confirmed/tentative/missing. |
| registration_deadline | no | PUBLIC | Deadline if provided. |
| walk_in_policy | no | PUBLIC/SENSITIVE | Whether participants may come without registration. |
| contact_method | no | SENSITIVE | Contact person, group, or account. Avoid publishing personal data unless intended. |

### C. Event Positioning

These fields define the message angle.

| Field | Required | Default Publicity | Description |
|---|---:|---|---|
| background | no | ADAPT | Why the event exists. Summarize, do not copy long internal wording. |
| purpose | no | ADAPT | What the event hopes to accomplish. |
| core_theme | yes | PUBLIC | Main topic. |
| promotion_angle | yes | ADAPT | The strongest public-facing angle distilled from the plan. |
| keywords | no | PUBLIC | 5-10 keywords for cross-platform consistency. |
| tone | no | ADAPT | Default tone if not specified: campus, friendly, practical, low-barrier, AI community. |
| relationship_to_previous_events | no | ADAPT | How this event continues previous salons or activities. |
| relationship_to_future_events | no | ADAPT | Follow-up activities such as VibeCoding, Hackathon, AI writing, etc. |

### D. Audience

These fields determine how to invite participants.

| Field | Required | Default Publicity | Description |
|---|---:|---|---|
| primary_audience | yes | PUBLIC | Main target audience. |
| presenter_groups | no | PUBLIC | Project groups that will roadshow or present. |
| free_agents | no | PUBLIC | Individuals who want to join project teams. |
| general_audience | no | PUBLIC | Observers, beginners, interested students. |
| external_participants_policy | no | SENSITIVE | Whether external students, incubator teams, or startup teams may join. |
| excluded_or_deprioritized_audience | no | PUBLIC | Groups not prioritized, e.g. traditional non-AI projects. Use gentle wording. |
| beginner_friendliness | no | ADAPT | Whether "小白友好" or "旁听也欢迎" is supported by the plan. |

### E. Content And Agenda

These fields become the core of promotional copy.

| Field | Required | Default Publicity | Description |
|---|---:|---|---|
| core_segments | yes | PUBLIC | Main sections: intro, roadshow, roundtable, special sharing, etc. |
| agenda | yes | PUBLIC | Time schedule if available. |
| presenter_group_limit | no | PUBLIC | Max number of roadshow groups. |
| expected_presenter_count | no | PUBLIC | Expected number if stated. |
| per_group_duration | no | PUBLIC | Duration per presenter group. |
| discussion_duration | no | PUBLIC | Roundtable duration. |
| has_judges | no | PUBLIC | Whether formal judges exist. |
| has_guest | no | PUBLIC/SENSITIVE | Whether a guest exists. Mark SENSITIVE if not confirmed. |
| guest_info | no | PUBLIC/SENSITIVE | Guest name/title/topic. Use only if confirmed or user-supplied. |
| special_topic | no | PUBLIC/SENSITIVE | Special sharing topic, if confirmed. |
| has_snacks_or_drinks | no | PUBLIC | Can be used to signal relaxed atmosphere if intended. |
| feedback_or_followup | no | ADAPT | Follow-up survey or future activities. Avoid exposing internal fields. |

### F. Recruitment And Matching

These fields support project/team matching copy.

| Field | Required | Default Publicity | Description |
|---|---:|---|---|
| project_requirements | no | PUBLIC | What presenter groups can request: tech, product, design, teammates, etc. |
| teammate_recruitment | no | PUBLIC | Whether project groups may recruit teammates. |
| skill_directions | no | PUBLIC | Skills welcomed: coding, product, ops, writing, visual design, roadshow expression. |
| matching_mechanism | no | ADAPT | How on-site matching happens. Keep high-level and friendly. |
| followup_pool | no | INTERNAL/ADAPT | Internal participant pool should not be exposed directly. Can be adapted as "后续活动继续对接". |

### G. Publicity Notes

These fields guide generation but may not appear directly.

| Field | Required | Default Publicity | Description |
|---|---:|---|---|
| preferred_platforms | no | INTERNAL | Target platforms. Default: WeChat, Xiaohongshu, unified QQ channel copy. |
| title_candidates | no | INTERNAL | Existing title ideas from the plan or user. |
| required_mentions | no | INTERNAL | Facts or phrases the user requires. |
| forbidden_mentions | no | INTERNAL | Facts or phrases the user forbids. |
| visual_notes | no | INTERNAL | Cover/poster visual guidance if present. |
| brand_voice | no | INTERNAL | Juhuo AI tone notes. |

### H. Internal-Only Info

Extract these if present, but do not use in public copy by default.

| Field | Required | Default Publicity | Description |
|---|---:|---|---|
| staff_roles | no | INTERNAL | Staffing and role assignment. |
| worker_arrival_time | no | INTERNAL | Staff arrival/preparation time. |
| logistics | no | INTERNAL | Venue setup, materials, snacks, cleanup. |
| equipment | no | INTERNAL | Projector, microphone, extension cords, network. |
| photography_arrangement | no | INTERNAL/SENSITIVE | Photography staff and publication considerations. |
| host_script_preparation | no | INTERNAL | Host script and run-of-show preparation. |
| registration_form_fields | no | INTERNAL/SENSITIVE | Detailed registration fields. |
| feedback_form_fields | no | INTERNAL/SENSITIVE | Detailed feedback fields. |
| emergency_plan | no | INTERNAL | Safety or equipment fallback plans. |

### I. Risks And Unknowns

This group drives quality gates.

| Field | Required | Publicity | Description |
|---|---:|---|---|
| tentative_items | yes | SENSITIVE | Facts marked tentative or undetermined. |
| missing_required_facts | yes | SENSITIVE | Required facts missing from the plan. |
| conflicting_facts | yes | SENSITIVE | Conflicting facts in the plan. |
| privacy_sensitive_items | yes | SENSITIVE | Contacts, forms, personal data, photos, unpublished project info. |
| potential_overclaim_items | yes | SENSITIVE | Claims that may overpromise outcomes. |
| facts_added_outside_plan | yes | SENSITIVE | User-supplied facts not present in original plan. |
| do_not_publish_items | yes | INTERNAL/SENSITIVE | Explicitly internal or prohibited facts. |

## Required Public Fact Checklist

For promotional copy, these facts are required unless the user explicitly says to draft with placeholders:

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

If any are `MISSING`, stop and ask the user for the missing facts unless the user asked for a draft with placeholders.

If any are `TENTATIVE`, either ask for confirmation or preserve the uncertainty in all copy.

## Public Copy Eligibility

Before writing promotional copy, classify facts:

```text
Use directly:
PUBLIC + CONFIRMED
PUBLIC + USER_SUPPLIED

Use with careful wording:
PUBLIC + TENTATIVE
ADAPT + CONFIRMED
ADAPT + USER_SUPPLIED

Do not use unless requested:
INTERNAL

Use only in generalized form:
SENSITIVE
```

Examples:

```text
PUBLIC + CONFIRMED:
活动时间：2026 年 5 月 10 日 14:00-17:00
Can write: 时间：2026 年 5 月 10 日 14:00-17:00

SENSITIVE + TENTATIVE:
活动地点：暂定
Can write: 地点将通过报名群通知
Do not write: 地点：西南大学产业技术研究院 2 号楼 701

INTERNAL + CONFIRMED:
工作人员 13:30 到场调试设备
Do not write in public copy.

ADAPT + CONFIRMED:
为后续 VibeCoding、小程序开发、AI 写作和 Hackathon 积累参与基础
Can write: 后续也会继续组织 VibeCoding、Hackathon 等实践活动。
```

## Handling Plan Supplements

If the user later provides updates, append them to the fact table.

Rules:

- Mark source as `user message`, `updated plan`, or named file.
- Mark status as `USER_SUPPLIED`.
- If the supplement contradicts the plan, record the conflict and prefer the newest user-supplied fact only after clearly noting it.
- Keep `facts_added_outside_plan` so later outputs can explain what came from the original plan and what came from updates.

Example:

```text
field: location
value: 西南大学产业技术研究院 2 号楼 701（三号门过马路左手边）
source: user message after plan review
publicity_level: PUBLIC
status: USER_SUPPLIED
notes: Overrides original tentative location in the plan.
```

## Output Template

When extracting facts, use this overall output structure:

```markdown
# Fact Table

## Source Metadata
| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|

## Event Basics
| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|

## Event Positioning
| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|

## Audience
| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|

## Content And Agenda
| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|

## Recruitment And Matching
| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|

## Publicity Notes
| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|

## Internal-Only Info
| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|

## Risks And Unknowns
| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|
```

## Minimal Fact Summary Template

After the detailed fact table, produce a short summary for the user:

```markdown
## Publicly Usable Facts
- ...

## Need Confirmation
- ...

## Do Not Publish By Default
- ...

## Suggested Promotion Angle
- ...
```

## Juhuo AI Defaults

If the plan does not specify style, use these defaults:

- Association voice: friendly, practical, campus community, AI practice oriented.
- WeChat priority: complete narrative and reliable information.
- Xiaohongshu priority: short, friendly, searchable, low-barrier.
- QQ unified priority: clear call-to-action, community invitation, easy participation.
- Avoid bureaucratic wording.
- Avoid corporate SaaS tone.
- Avoid overclaiming outcomes.
