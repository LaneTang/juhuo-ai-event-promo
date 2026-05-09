# WeChat Frontend Design Engine

Use this reference before generating any v2 WeChat HTML.

This file makes the v2 HTML module self-contained. Do not depend on an external `frontend-design` skill being installed or explicitly invoked. The goal is to preserve strong frontend-design thinking, then translate it into static WeChat-compatible inline HTML.

## Core Rule

Every v2 HTML output must prove that it was designed before it was coded.

Do not generate HTML until these three sections are complete:

1. `Frontend Design Pass`
2. `Frontend Design Capability Mapping`
3. `Compatibility Downgrade Notes`

If any section is missing, generic, or not reflected in the HTML, revise before delivery.

## Frontend Design Pass

Produce a concise design pass with these fields:

| Field | Requirement |
|---|---|
| Purpose | What should readers understand, feel, and do after reading? |
| Audience | Who is reading: project owners, builders, beginners, guests, campus peers? |
| Tone | Choose a clear tone such as friendly invitation, hands-on workshop, academic field note, community notice, or serious salon. |
| Bold Aesthetic Direction | Name a specific visual concept, not just a color palette or style family. Make it memorable. |
| Differentiation | Explain what makes this version visually distinct from ordinary WeChat templates and from other requested versions. |
| Memorable Motif | Define one repeatable visual idea readers will remember. |
| Information Hierarchy | Identify the first-screen message, highlighted sentence, scannable sections, and conversion block. |
| Component System | Define how title, intro, quote, headings, audience, rules, agenda, info, QR placeholder, and CTA look. |
| Compatibility Translation | Explain how the design will stay static, inline-style based, and WeChat-compatible. |

## Frontend Design Capability Mapping

Map frontend-design capability into WeChat-safe decisions. This is required even when the external `frontend-design` skill is unavailable.

| Capability | WeChat-safe implementation |
|---|---|
| Purpose | Make the first screen and CTA answer: what is this, who should come, what should they do? |
| Tone | Choose a strong editorial direction, not a neutral notice. The tone must match the event and Juhuo AI community identity. |
| Bold Aesthetic Direction | Commit to one visual concept. Examples: hand-annotated invitation letter, maker workbench, lab field note, campus notice board, zine-style briefing. |
| Differentiation | Define the one thing readers will remember: marker strokes, boot console, field-log rows, blueprint panels, memo labels, etc. |
| Typography | Use font weight, size, line-height, spacing, labels, and contrast to create hierarchy. Do not rely on external fonts. |
| Color & Theme | Use a limited but confident palette. Use dominant color, accent color, and neutrals with purpose. Avoid timid or evenly distributed colors. |
| Spatial Composition | Create rhythm with blocks, margins, indents, dividers, asymmetry, dense/quiet alternation, and section contrast. |
| Background & Visual Details | Use WeChat-safe details: inline backgrounds, borders, dashed rules, ruled-paper rows, labels, corner tags, shadow-like border offsets, simple repeated motifs. |
| Polish | Check every component: title, intro, quote, headings, cards, checklist, timeline, info block, QR placeholder, CTA. Nothing should feel like leftover Markdown. |

## Compatibility Downgrade Notes

Translate ambitious frontend ideas into static WeChat HTML:

| Frontend idea | WeChat-compatible substitute |
|---|---|
| Motion / page reveal | Static layered rhythm, alternating density, strong first screen, clear scroll sequence. |
| Hover / interaction | Always-visible states: labels, badges, dividers, highlighted rows, callout blocks. |
| External fonts | System fonts plus weight/size/spacing hierarchy. Avoid depending on font personality. |
| CSS variables / classes | Inline repeated style values; keep palette and spacing consistent manually. |
| Gradient mesh / complex background | Solid blocks, subtle pale sections, borders, dashed lines, simple background colors. |
| Pseudo-elements | Real `span` / `section` elements with inline style. |
| SVG or icon systems | Text labels, simple symbols, bordered chips, numbered tags. |
| Fixed/sticky layout | Normal document flow with repeated anchors and clear section starts. |
| Remote images/assets | Optional local/uploaded `img` placeholders only; important text remains real text. |

Do not lower the design ambition. Lower only the implementation technique.

## Design Quality Bar

The HTML should feel intentionally designed, not like a Markdown article wrapped in cards.

Require:

- a strong first screen that immediately signals the event identity
- readable mobile typography with clear section rhythm
- a limited but confident color system
- recurring visual motifs that connect sections
- component choices that match the event tone
- visual hierarchy that helps readers scan time, audience, rules, and registration
- real text for all important information
- visible craft in spacing, contrast, and repeated details

Avoid:

- generic card stacks
- same layout with different colors
- timid palettes with no clear accent
- oversized decoration that weakens readability
- corporate SaaS aesthetics for campus community events
- cold tech conference layouts unless the event truly calls for that tone
- relying on animations, JavaScript, external CSS, external fonts, SVG, remote images, or hover states

## Multi-Style Comparison Rule

When generating multiple style versions, each version must have a different design pass and capability mapping.

Each version must differ in at least five of these eight areas:

- first screen/title block
- heading system
- highlighted quote/core sentence treatment
- audience/participant blocks
- rules/checklist block
- agenda/timeline block
- time-location-registration block
- closing CTA and QR placeholder

If the versions only change colors, border styles, English labels, or small decorative text, fail the style-drift check and redesign.

## Style-Specific Design Prompts

### Campus AI Community Handmade Tech Invitation

Design direction:

A hand-annotated campus invitation letter. It should feel warm, close, student-facing, and slightly techy.

Possible motifs:

- invitation card / letter paper
- marker highlight
- hand-label sticker
- checklist note
- taped caption
- friendly closing card
- notice-board pin / memo strip

Component tendencies:

- soft paper-like blocks
- black or ink-like borders
- warm highlight around the core sentence
- audience cards that feel like notes to different classmates
- rules as friendly checklist
- agenda as lightweight activity timeline
- CTA as invitation card

### Maker Geek Workshop

Design direction:

A hands-on build session or project workbench. It should feel practical, slightly geeky, energetic, and oriented toward making things.

Possible motifs:

- terminal boot screen
- build board
- status tags
- role assignment cards
- config panel
- progress log
- blueprint / debug lane

Component tendencies:

- strong dark or ink header used sparingly
- signal accent color for action labels
- audience blocks as roles
- rules as status/check items
- agenda as build/test/share timeline
- event info as configuration block
- CTA as launch/join block

### Academic Lab Field Notes

Design direction:

A campus lab field note or seminar handout. It should feel credible, calm, organized, and still accessible.

Possible motifs:

- field note
- observation log
- protocol sheet
- subject cards
- metadata table
- ruled paper
- research index labels

Component tendencies:

- restrained paper/blue-gray palette
- observation/protocol/log headings
- audience blocks as subject groups
- rules as protocol list
- agenda as field log
- time/location as event metadata
- CTA as concluding note

## Self-Check Before Delivery

Before delivering HTML, answer these internally:

1. Can I describe the visual concept in one sentence?
2. Did I map frontend-design capabilities into concrete WeChat-safe decisions?
3. Did I explain the compatibility downgrade from richer frontend ideas?
4. Is the first screen distinct from the other style versions?
5. Do section headings, cards, agenda, info block, and CTA match the chosen concept?
6. Would the article still look designed if all motion and external assets were stripped?
7. Is every important event fact preserved exactly?
8. Are placeholders visible and honest?
9. For multi-style output, did I include a style-difference summary?

If any answer is no, revise before delivering.
