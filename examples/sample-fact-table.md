# Fact Table Sample

Source plan: `uploaded-plan: 炬火AI实践月_AIx分享会1_大创专题暨模拟路演_新版策划案.docx`

Extraction date: 2026-05-08

This sample applies `references/fact-table-schema.md` to a real Juhuo AI activity plan. It is intended as a reference output for the future `juhuo-ai-event-promo` skill.

## Source Metadata

| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|
| source_file | `uploaded-plan: 炬火AI实践月_AIx分享会1_大创专题暨模拟路演_新版策划案.docx` | user-provided file | INTERNAL | CONFIRMED | Original Word/WPS activity plan. |
| extraction_date | 2026-05-08 | system date | INTERNAL | CONFIRMED | Extracted during skill design. |
| document_title | 炬火 AI 实践月 \| "AI×"分享会#1 大创专题暨模拟路演 活动策划书 | document cover/title | INTERNAL | CONFIRMED | Title appears across multiple cover lines. |
| document_version | 新版策划案(改) | filename | INTERNAL | INFERRED | Version inferred from filename rather than document body. |
| confidence_notes | Text extraction is complete enough for public fact extraction. Tables were flattened into paragraph text. | extraction process | INTERNAL | CONFIRMED | Table structure should be preserved manually when needed for agenda/form fields. |

## Event Basics

| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|
| event_full_name | 炬火 AI 实践月 \| "AI×"分享会#1 大创专题暨模拟路演 | 五、活动主题 | PUBLIC | CONFIRMED | Official activity name. |
| event_short_name | "AI×"分享会#1 / AI×大创模拟路演 | 五、活动主题 | PUBLIC | INFERRED | Useful for social copy; derived from official title. |
| series_name | 炬火 AI 实践月 | 一、活动背景；五、活动主题 | PUBLIC | CONFIRMED | Series begins with this event. |
| session_number | "AI×"分享会#1 | document title；五、活动主题 | PUBLIC | CONFIRMED | First event in the series. |
| organizer | 炬火 AI 研究协会 | cover；六、活动单位 | PUBLIC | CONFIRMED | Main organizer. |
| co_organizer | 未定 | cover；六、活动单位 | SENSITIVE | TENTATIVE | Do not mention co-organizer publicly unless later confirmed. |
| event_type | 分享会、模拟路演、圆桌交流 | 五、活动主题；七、活动流程；八、活动内容 | PUBLIC | CONFIRMED | Can be described as a campus AI practice sharing session plus simulated roadshow. |
| event_date | 2026 年 5 月 10 日 | 三、活动时间 | PUBLIC | CONFIRMED | Required public fact. |
| weekday | 周日 | computed from 2026-05-10 | PUBLIC | INFERRED | Date calculation says Sunday. Mark inferred unless user supplies publication wording. |
| start_time | 14:00 | 三、活动时间 | PUBLIC | CONFIRMED | Required public fact. |
| end_time | 17:00 | 三、活动时间 | PUBLIC | CONFIRMED | Required public fact. |
| location | 活动地点暂定。备选方向包括校内会议厅、双创院相关活动空间，或校外孵化园路演厅。最终地点以后续场地申请与协调结果为准。 | 四、活动地点 | SENSITIVE | TENTATIVE | Public copy must preserve uncertainty, e.g. "地点将通过报名群通知". |
| location_status | 暂定 | 四、活动地点 | SENSITIVE | TENTATIVE | This is a blocker for final public copy unless user confirms venue. |
| registration_method | 飞书报名入口 / 飞书报名工具 | 七、活动流程；附件一 | PUBLIC | CONFIRMED | The plan says publicity posts should provide Feishu registration entry. |
| registration_status | 报名入口 planned, specific QR/link not included in the plan | 七、活动流程；附件一 | SENSITIVE | TENTATIVE | Need actual QR/link before final material production. |
| registration_deadline | 未提供 | document | SENSITIVE | MISSING | Do not invent. |
| walk_in_policy | 未提供 | document | SENSITIVE | MISSING | Do not claim "可空降" unless user confirms. |
| contact_method | 报名群或通知渠道 | 七、活动流程 | SENSITIVE | TENTATIVE | The plan mentions reminders through group/notification channel but does not provide a public contact method. |

## Event Positioning

| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|
| background | 协会已开展三期 AI 沙龙，本次以实践月为起点，把活动重心从工具体验推进到项目实践。 | 一、活动背景 | ADAPT | CONFIRMED | Use as friendly narrative, not bureaucratic plan wording. |
| purpose | 提供面向 AI+大创项目和 AI+创业项目的展示、交流与撮合平台，连接项目组、兴趣小白和自由组队成员。 | 二、活动目的 | ADAPT | CONFIRMED | Strong public-facing purpose. |
| core_theme | AI×大创；AI+项目落地 | 五、活动主题 | PUBLIC | CONFIRMED | Required public fact. |
| promotion_angle | 从"AI 工具怎么用"推进到"AI 项目怎么做"，邀请正在做项目的人和想加入项目的人现场交流、组队、找落地路径。 | 一、活动背景；二、活动目的 | ADAPT | INFERRED | Distilled angle for cross-platform copy. |
| keywords | 炬火 AI 实践月、AI×大创、模拟路演、项目落地、自由组队、技术支持、圆桌讨论、VibeCoding、Hackathon | 一、活动背景；二、活动目的；七、活动流程 | PUBLIC | CONFIRMED | Use selectively by platform. |
| tone | 校园、亲近、实践导向、低门槛、同学互助 | plan intent | ADAPT | INFERRED | Inferred from "轻松交流", "自由聊", "同学之间互相交流". |
| relationship_to_previous_events | 承接前三期 AI 沙龙的交流基础。 | 一、活动背景 | ADAPT | CONFIRMED | Good WeChat intro material. |
| relationship_to_future_events | 为后续 VibeCoding、小程序开发、AI 写作、Hackathon 等活动积累参与基础。 | 一、活动背景；七、活动后期 | ADAPT | CONFIRMED | Public copy can mention future activities generally. |

## Audience

| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|
| primary_audience | 西南大学在读学生，重点面向正在参与大创、创新创业项目，并已融入或计划引入 AI 技术的同学。 | 八、活动内容（一）参与对象 | PUBLIC | CONFIRMED | Main audience. |
| presenter_groups | 已融入 AI 能力或具有 AI 赋能潜力的大创项目、创业项目、实践项目。 | 八、活动内容；九、注意事项 | PUBLIC | CONFIRMED | Can invite as "路演项目组". |
| free_agents | 有意参与大创或创业项目、希望被项目组招募的独立同学。 | 八、活动内容（一）参与对象 | PUBLIC | CONFIRMED | Can write as "懂技术/产品/运营/表达的同学". |
| general_audience | 普通观众 / 兴趣小白，可参与旁听、交流和后续活动意向登记。 | 八、活动内容（一）参与对象 | PUBLIC | CONFIRMED | Supports "小白也欢迎" copy. |
| external_participants_policy | 活动也接受校外 AI+项目、孵化园团队、创业团队参与交流。 | 八、活动内容（一）参与对象 | SENSITIVE | CONFIRMED | Confirm whether to publicize externally; may affect报名/场地容量. |
| excluded_or_deprioritized_audience | 传统非 AI 项目不作为本期邀请和路演重点。 | 八、活动内容；九、注意事项 | PUBLIC | CONFIRMED | Use gentle wording: "本期更优先 AI 相关项目". |
| beginner_friendliness | 兴趣小白可旁听、交流、登记后续活动意向。 | 八、活动内容（一）参与对象 | ADAPT | CONFIRMED | Good for Xiaohongshu/QQ tone. |

## Content And Agenda

| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|
| core_segments | 开场介绍；小组自我介绍；小组轮流模拟路演；圆桌讨论；收尾反馈。 | 七、活动流程；八、活动内容 | PUBLIC | CONFIRMED | Required public fact. |
| agenda | 14:00-14:10 开场；14:10-14:40 自我介绍；14:40-15:55 模拟路演；15:55-16:55 圆桌讨论；16:55-17:00 收尾。 | 七、活动流程（二）时间安排 | PUBLIC | CONFIRMED | Public agenda excludes staff setup unless writing internal runbook. |
| internal_setup_time | 13:30-14:00 工作人员到场，设备调试、物资摆放、签到准备。 | 七、活动流程（二）时间安排 | INTERNAL | CONFIRMED | Do not publish by default. |
| presenter_group_limit | 最多 5 组 | 七、活动流程；九、注意事项 | PUBLIC | CONFIRMED | Public recruitment rule. |
| expected_presenter_count | 预计 4 组，最多 5 组 | 七、活动流程；八、活动内容 | PUBLIC | CONFIRMED | Can say "预计 4-5 组". |
| per_group_duration | 每组 15 分钟 | 七、活动流程；八、活动内容 | PUBLIC | CONFIRMED | Includes project presentation, discussion, needs request. |
| discussion_duration | 圆桌讨论预计 1 小时 | 七、活动流程；八、活动内容 | PUBLIC | CONFIRMED | Good public selling point. |
| has_judges | 不设置正式评委 | 二、活动目的；九、注意事项 | PUBLIC | CONFIRMED | Important for relaxed tone. |
| has_guest | 不设置正式评委或嘉宾，暂定为纯同学之间互相交流。 | 八、活动内容（四）圆桌讨论；九、注意事项 | PUBLIC/SENSITIVE | TENTATIVE | Later user-supplied guest info would override this. For this plan, do not advertise guests. |
| guest_info | 未提供 | document | SENSITIVE | MISSING | Do not invent special guest. |
| special_topic | 未提供 | document | SENSITIVE | MISSING | The plan does not include AI image generation special talk. |
| has_snacks_or_drinks | 准备零食饮料，延续炬火 AI 沙龙轻松交流氛围。 | 七、活动流程（一）物资准备 | PUBLIC | CONFIRMED | Can mention lightly if intended for participants. |
| feedback_or_followup | 活动后收集反馈，整理后续活动意向，为 VibeCoding、小程序开发、AI 写作、Hackathon 建立参与基础。 | 七、活动后期；附件二 | ADAPT | CONFIRMED | Do not expose detailed feedback fields. |

## Recruitment And Matching

| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|
| project_requirements | 项目组可提出技术开发、AI 能力接入、产品设计、运营推广、路演表达、队友招募等需求。 | 八、活动内容（三）；附件一 | PUBLIC | CONFIRMED | High-value public detail. |
| teammate_recruitment | 路演项目组可现场提出是否需要招募队友、希望招募什么方向。 | 八、活动内容；附件一 | PUBLIC | CONFIRMED | Can be framed as "现场找队友". |
| skill_directions | 技术开发、AI 工具使用、产品设计、运营推广、文案写作、视觉设计、路演表达。 | 附件一 | PUBLIC | CONFIRMED | Public copy may adapt this list. |
| matching_mechanism | 通过自我介绍、项目路演、现场需求提出和圆桌讨论进行自由撮合。 | 二、活动目的；八、活动内容 | ADAPT | CONFIRMED | Avoid sounding too formal. |
| followup_pool | 根据报名表和反馈表整理后续活动意向名单，为系列活动建立基础参与池。 | 七、活动后期 | INTERNAL/ADAPT | CONFIRMED | Public copy can only say "后续还会继续组织实践活动". |

## Publicity Notes

| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|
| preferred_platforms | 微信公众号、小红书、QQ 频道/QQ群/校园墙统一文案 | user design decision | INTERNAL | USER_SUPPLIED | This is not from the plan; it is part of the skill design. |
| title_candidates | 炬火 AI 实践月；"AI×"分享会#1；大创专题暨模拟路演 | document title | INTERNAL | CONFIRMED | Can derive platform-specific titles. |
| required_mentions | 活动时间、地点状态、报名方式、参与对象、路演规则、交流性质。 | schema + plan | INTERNAL | INFERRED | Required by quality gate, not explicit in plan. |
| forbidden_mentions | 未确认协办单位、未确认地点、个人联系方式、详细报名/反馈字段、工作人员安排。 | schema + plan | INTERNAL | INFERRED | Derived from sensitivity classification. |
| visual_notes | 无明确视觉要求。 | document | INTERNAL | MISSING | Image/HTML modules should ask or use Juhuo defaults. |
| brand_voice | 校园 AI 社群；轻松交流；实践导向；同学互助。 | plan wording | INTERNAL | INFERRED | Useful style anchor for copy. |

## Internal-Only Info

| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|
| staff_roles | 现场统筹、签到引导、路演组织、摄影宣发、后勤物资。 | 七、活动流程（二）人员安排 | INTERNAL | CONFIRMED | Internal execution only. |
| worker_arrival_time | 13:30 工作人员到场。 | 七、活动流程（二）时间安排 | INTERNAL | CONFIRMED | Do not publish by default. |
| logistics | 场地确认、设备确认、签到二维码、活动群二维码、报名数据、反馈二维码、后续活动意向收集表、零食饮料、场地整理。 | 七、活动流程（一）；七、活动流程（二） | INTERNAL | CONFIRMED | Keep out of promotional copy except snacks/drinks if desired. |
| equipment | 投影设备、音响设备、麦克风、插排、网络环境。 | 七、活动流程（一）物资准备 | INTERNAL | CONFIRMED | Internal only. |
| photography_arrangement | 安排摄影记录人员，活动现场拍照录像应注意参与者意愿。 | 七、活动流程（一）；九、注意事项 | INTERNAL/SENSITIVE | CONFIRMED | Use only as privacy reminder, not public copy. |
| host_script_preparation | 准备主持稿和流程单。 | 七、活动流程（一）内容准备 | INTERNAL | CONFIRMED | Internal only. |
| registration_form_fields | 姓名、学校/单位、学院/专业/年级、联系方式/微信、报名身份；路演项目、自由组队、普通观众分流字段。 | 附件一 | INTERNAL/SENSITIVE | CONFIRMED | Do not publish detailed fields. |
| feedback_form_fields | 参与身份、整体感受、最有帮助部分、后续参与意向、后续活动方向、期待、联系方式。 | 附件二 | INTERNAL/SENSITIVE | CONFIRMED | Do not publish detailed fields. |
| emergency_plan | 通道畅通；设备问题时调整形式；人员不适或突发情况及时处理。 | 九、注意事项 | INTERNAL | CONFIRMED | Internal only. |

## Risks And Unknowns

| Field | Value | Source | Publicity | Status | Notes |
|---|---|---|---|---|---|
| tentative_items | 协办单位未定；活动地点未定；人员安排暂定；活动过程可灵活分配时间；无正式嘉宾/评委为暂定。 | cover；四、活动地点；七、活动流程；八、活动内容 | SENSITIVE | TENTATIVE | Biggest public-copy risks are location and co-organizer. |
| missing_required_facts | 具体报名二维码/链接缺失；报名截止时间缺失；公开联系方式缺失；walk-in policy 缺失。 | document | SENSITIVE | MISSING | For v1 copy, QR/link can be represented as placeholder only if user allows. |
| conflicting_facts | No direct conflict found in the plan. | document | SENSITIVE | CONFIRMED | Later user messages may override location, guest/special topic, or walk-in policy. |
| privacy_sensitive_items | 联系方式/微信收集；报名表与反馈表；照片/视频发布；未公开项目内容。 | 九、注意事项；附件一；附件二 | SENSITIVE | CONFIRMED | Public copy should reassure lightly if needed, not expose fields. |
| potential_overclaim_items | 资源对接、项目落地、创业/收益等方向应避免保证结果。 | 二、活动目的；附件一 | SENSITIVE | INFERRED | Use "交流/尝试/对接机会", avoid "保证找到队友/拿到资源". |
| facts_added_outside_plan | preferred_platforms: 微信公众号、小红书、QQ 频道/QQ群/校园墙统一文案。 | user design decision | SENSITIVE | USER_SUPPLIED | This sample intentionally records skill-level decisions outside the plan. |
| do_not_publish_items | 工作人员到场时间、人员安排、物资清单、设备清单、详细报名字段、详细反馈字段、个人联系方式、内部参与池。 | 七、活动流程；附件一；附件二 | INTERNAL/SENSITIVE | CONFIRMED | Keep out of public copy by default. |

## Publicly Usable Facts

- 活动名称：炬火 AI 实践月 | "AI×"分享会#1 大创专题暨模拟路演。
- 主办单位：炬火 AI 研究协会。
- 时间：2026 年 5 月 10 日 14:00-17:00。
- 主题：AI×大创、AI+项目落地。
- 参与对象：AI 相关大创/创业/实践项目组、希望加入项目的自由组队成员、普通观众/兴趣小白。
- 核心环节：开场、自我介绍、4-5 组模拟路演、1 小时圆桌讨论、收尾反馈。
- 路演规则：AI 相关项目优先，最多 5 组，每组 15 分钟，超过名额可顺延。
- 活动调性：同学之间建设性交流，不设置正式评委。
- 可轻量提及：现场准备零食饮料，氛围偏轻松交流。

## Need Confirmation

- 活动地点仍是 `TENTATIVE`。策划案只写了备选方向，不能公开写成具体地点。
- 协办单位为 `未定`。公开材料中建议不提。
- 报名二维码/链接未出现在策划案正文里，最终推文需要用户补充。
- 报名截止时间未提供。
- 是否允许不报名直接到场未提供，不能写"可空降"。
- 是否邀请嘉宾或加入特别专题分享未提供。若后续宣传加入嘉宾，需要标为 `USER_SUPPLIED` 并记录覆盖关系。

## Do Not Publish By Default

- 工作人员 13:30 到场、人员分工、设备和物资清单。
- 详细飞书报名字段、反馈表字段。
- 联系方式/微信等个人数据收集细节。
- 后续活动意向池、内部名单整理。
- 未公开项目内容、照片视频发布细节。
- "协办单位未定"这类内部不确定信息。

## Suggested Promotion Angle

这场活动最适合包装成一场校园 AI 社群的实践型邀请：不再停留在"AI 工具怎么用"，而是把同学们正在做的大创、创业和实践项目拿到现场聊一聊。项目组可以获得反馈、找技术路径和队友；自由组队成员可以发现真实项目；普通观众和兴趣小白也可以低门槛旁听，认识正在把 AI 做进项目里的同学。
