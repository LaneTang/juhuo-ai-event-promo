# WeChat Component Blueprints

Use this reference when generating v2 WeChat HTML.

The purpose is to prevent three style versions from becoming the same skeleton with different colors. Each style family has its own component blueprint. Use these as structural requirements, not decorative suggestions.

## Shared Rule

All HTML must be based on the complete WeChat article copy, not a compressed summary. Preserve important paragraphs, section rhythm, agenda explanations, participant invitations, and CTA.

For each style version, output:

- `Frontend Design Plan`
- `Component Blueprint`
- `WeChat Compatibility Translation`
- HTML
- Copy/Paste Notes

## Blueprint A: Campus AI Community Handmade Tech Invitation

Visual concept:

A hand-annotated campus invitation letter sent to classmates who might bring projects, skills, or curiosity.

Required component system:

- **First screen**: invitation card or letter-paper block with date/time ribbon, event title, subtitle, and one warm slogan.
- **Intro**: letter-style paragraphs with a margin label such as "写给正在做东西的你".
- **Golden sentence**: warm-yellow marker highlight or bordered note.
- **Section headings**: large outlined numbers, handwritten-style labels, or left-corner tags.
- **Participant blocks**: separate friendly note cards for project owners, free agents, and beginners.
- **Rules**: checklist note with visible check marks or stamped labels.
- **Agenda**: lightweight activity timeline, not a table.
- **Info block**: notice-card style time/location/registration section.
- **QR placeholder**: dashed paper card, visually obvious.
- **CTA**: invitation card that feels warm and human.

Must avoid:

- cold tech dashboard
- pure blue corporate card stack
- same title/info/audience/agenda skeleton as other versions

## Blueprint B: Maker Geek Workshop

Visual concept:

A project workbench or build session where ideas are booted, tested, debugged, and connected with collaborators.

Required component system:

- **First screen**: boot panel, launch board, or console-like header with event identity and "build" hook.
- **Intro**: mission brief with problem/goal framing.
- **Golden sentence**: command/output block or signal strip.
- **Section headings**: build steps, terminal prompts, or pipeline labels.
- **Participant blocks**: role assignment cards such as project owner, builder, observer.
- **Rules**: status/check items, e.g. PASS / LIMIT / QUEUE / OPEN.
- **Agenda**: build pipeline or progress log, e.g. boot -> sync -> demo -> roundtable -> ship.
- **Info block**: config panel for time/location/registration.
- **QR placeholder**: registration endpoint or deploy target block.
- **CTA**: launch/join block, not a soft invitation card.

Must avoid:

- using only black header and cyan labels while keeping the campus invitation layout
- excessive dark mode that hurts WeChat long-form reading
- pretending English labels are enough to make it "geek"

## Blueprint C: Academic Lab Field Notes

Visual concept:

A campus lab field note or seminar handout recording an AI practice session with clarity, credibility, and curiosity.

Required component system:

- **First screen**: field-note cover with issue number, research object, event title, and metadata strip.
- **Intro**: observation note, written calmly but accessibly.
- **Golden sentence**: finding / thesis / observation callout.
- **Section headings**: observation, subject, protocol, field log, metadata.
- **Participant blocks**: subject cards or cohort notes.
- **Rules**: protocol list with ordered labels.
- **Agenda**: field log rows or lab notebook timeline.
- **Info block**: event metadata table or research-card block.
- **QR placeholder**: appendix / registration specimen block.
- **CTA**: concluding note, not a launch button or handmade invitation.

Must avoid:

- becoming gray card stack
- overusing English labels without changing structure
- losing warmth; it should be credible, not cold

## Multi-Style Acceptance Rule

When three versions are requested:

- Their first screens must be visibly different.
- Their heading systems must be different.
- Their participant sections must use different component logic.
- Their agenda sections must use different component logic.
- Their info/registration blocks must not share the same skeleton.
- Their CTAs must express different interaction metaphors.

If a user could describe the difference as "blue version, dark version, gray version", fail and redesign.
