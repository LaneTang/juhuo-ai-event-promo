# WeChat HTML Layout

Use this reference when the user explicitly asks for WeChat Official Account HTML layout, 微信公众号排版, 可复制进公众号后台的 HTML, or asks to turn approved WeChat copy into HTML.

This is a v2 downstream module. Do not use it before the event facts and WeChat copy have passed quality gates.

Required companion references: read `references/article-to-html-mapping.md`, `references/frontend-design-core.md`, `references/wechat-frontend-design.md`, and `references/wechat-component-blueprints.md` before writing any HTML.

## Core Rule

Generate static WeChat-compatible HTML that still looks good after animations and scripts are stripped.

Before writing HTML, apply the full internal frontend-design flow from `references/frontend-design-core.md`, then translate it through `references/wechat-frontend-design.md` and the selected component blueprint from `references/wechat-component-blueprints.md`. Do not depend on an external `frontend-design` skill being installed.

Use the complete WeChat article as source material. Do not base HTML on a compressed summary, fact table, or shortened rewrite.

Before design and HTML, produce `Article-to-HTML Mapping` and `Article Coverage Check` from `references/article-to-html-mapping.md`. If major article units are missing from the HTML, fail the coverage check and revise before delivery.

The design pass must decide:

- purpose: what the article needs readers to understand or do
- audience: who is reading and what tone makes them feel invited
- aesthetic direction: a clear visual point of view, not a generic template
- hierarchy: what appears first, what becomes a highlight, what becomes supporting detail
- memorable motif: the one visual idea readers should remember
- component system: title block, quote/highlight, section heading, cards, checklist, timeline, info block, QR placeholder, closing CTA
- compatibility translation: how the design becomes static inline HTML without unsupported frontend techniques

Then translate that design pass into WeChat-compatible static HTML. Keep the visual intent, but discard incompatible frontend techniques.

Allowed:

- semantic `section`, `p`, `span`, `strong`, `br`, `img` placeholders
- mostly inline `style`
- simple nested blocks
- static borders, backgrounds, spacing, labels, highlights, dividers
- emoji only if they fit the selected style

Avoid:

- JavaScript
- animation
- external CSS
- external fonts
- pseudo-elements
- complex hover/interactive effects
- remote assets
- SVG-only decorative systems
- layout depending on `position: fixed`, viewport units, or unsupported CSS

## Output Contract

When generating v2 HTML, output:

````markdown
## Frontend Design Plan

Purpose, audience, tone, bold aesthetic direction, differentiation, memorable motif, information hierarchy, component system, and compatibility translation.

## Article-to-HTML Mapping

Each major WeChat article unit mapped to a concrete HTML component.

## Article Coverage Check

Source article units, covered units, omitted units with reasons, and PASS/FAIL.

## Component Blueprint

Selected style blueprint and concrete component choices for first screen, headings, participant blocks, rules, agenda, info block, QR placeholder, and CTA.

## Frontend Design Capability Mapping

How frontend-design capabilities are translated into WeChat-safe decisions.

## WeChat Compatibility Translation

How richer frontend ideas are reduced to static inline HTML without losing the visual concept.

## WeChat HTML Style Choice

Chosen style and reason.

## 微信公众号 HTML

```html
...
```

## Copy/Paste Notes

- Static HTML.
- Inline-style based.
- Replace QR placeholder if needed.
````

If the user requested an `.html` file, create the file. Otherwise, provide the HTML block.

## Default HTML Container

Use a mobile-first width and readable typography:

```html
<section style="max-width: 677px; margin: 0 auto; padding: 0; box-sizing: border-box; font-size: 15px; line-height: 1.75; color: #111827;">
  ...
</section>
```

Body text defaults:

- font-size: `15px`
- line-height: `1.7` to `1.85`
- paragraph margin: `0 0 14px`
- section spacing: `28px` to `38px`
- border radius: `6px` to `12px`
- avoid tiny text below `12px`

## Style Families

Choose one style family based on the event tone, user request, or previous Juhuo style. Do not lock the design to a single fixed template. Within each family, vary the element combinations while preserving the overall mood.

The style family is not the design by itself. After choosing a family, still create a frontend-design plan that adapts the family to the specific event, copy, audience, and factual constraints.

When the user asks for multiple style versions, the versions must differ in visible structure, not only in colors or labels. Before writing HTML, define a distinct visual motif and component system for each version.

Required differentiation points for multi-style comparisons:

- first screen/title block
- heading system
- highlighted quote or core sentence treatment
- audience/participant blocks
- rules/checklist block
- agenda/timeline block
- time-location-registration block
- closing CTA and QR placeholder

If two versions share the same layout skeleton with only palette, wording labels, border colors, or icon-like text changed, fail the style-drift check and redesign one version before delivering.

### 1. Campus AI Community Handmade Tech Invitation

Use when the event is friendly, student-facing, invitation-like, low-pressure, or community-driven.

Overall description:

A warm campus AI community invitation that feels like a hand-annotated event letter. It has approachable student energy, a bit of tech structure, and enough polish for a WeChat article. It should not feel like a cold technology launch or a corporate SaaS announcement.

Suggested element pool:

- light-blue letter-paper blocks
- warm-yellow marker highlights
- black bold strokes
- outlined section numbers
- hand-label tags
- soft grid paper textures made with simple background colors/borders
- taped-note style captions
- checklist rows
- small corner labels
- thin blue dividers
- QR placeholder card
- ending invitation card

Suggested palette:

- primary: light blue / ink black / warm yellow
- optional neutral: white or very pale gray as background
- keep dominant colors to 2-3, but use opacity and border variants for hierarchy

Do not use every element at once. Combine 3-5 recurring elements so the article feels coherent.

### 2. Maker Geek Workshop

Use when the event emphasizes building, demos, hackathon, coding, product prototypes, tools, AI development, or project roadshows.

Overall description:

A maker-space style layout with workshop energy: practical, slightly geeky, hands-on, and action-oriented. It should feel like students gathering around a project table, debugging ideas, showing prototypes, and recruiting collaborators.

Suggested element pool:

- terminal-like labels
- mono-style small captions
- blueprint grid blocks
- component cards with hard borders
- bracketed titles
- dotted or dashed separators
- progress-step bars
- project requirement chips
- dark ink blocks used sparingly
- green or cyan signal accents
- "build / test / ship" style micro labels
- agenda as a build timeline

Suggested palette:

- ink black / electric cyan or signal green / off-white
- optional blue-gray for secondary blocks
- avoid full dark-mode pages unless the user asks; WeChat long-form reading should remain comfortable.

### 3. Academic Lab Field Notes

Use when the event is a salon, research sharing, academic-practice bridge, invited talk, entrepreneurship exchange, or more serious collaboration context.

Overall description:

A field-notes layout from a campus research lab: calm, credible, curious, and organized. It should feel like an annotated lab notebook or seminar handout, with enough warmth to remain student-friendly. Use this when the topic needs more trust and clarity than playfulness.

Suggested element pool:

- lab-note margins
- citation-like small labels
- specimen-card blocks
- thin ruled lines
- blue-gray section bands
- paper-white content areas
- keyword index chips
- "observation / question / next step" micro labels
- agenda as field log
- quote cards
- understated highlight strips
- clean info table for time/location/registration

Suggested palette:

- paper white / blue-gray / graphite black
- optional muted yellow highlight
- keep contrast strong and decoration restrained.

## Required Components

For event invitation HTML, include these components when the copy contains them:

- title block
- introduction / letter block
- 1-3 highlighted sentences
- numbered section headings
- participant/audience blocks
- rules/checklist block
- agenda/timeline block
- time-location-registration block
- QR code placeholder if registration image is missing
- closing invitation card
- Need Confirmation note only if the user wants draft-safe output; otherwise keep it outside public HTML

## Component Patterns

These patterns are starting points only. Do not mechanically repeat them. Use them as WeChat-compatible building blocks after the frontend-design plan and component blueprint have defined the page rhythm and visual motif.

### Title Block

Use a strong first viewport signal. The title must be readable on mobile.

```html
<section style="margin: 0 0 28px; padding: 28px 22px; background: #eaf5ff; border: 2px solid #111827; border-radius: 10px;">
  <p style="margin: 0 0 10px; font-size: 13px; color: #2563eb; font-weight: 700;">INVITATION / Juhuo AI</p>
  <h1 style="margin: 0; font-size: 24px; line-height: 1.35; color: #111827; font-weight: 800;">...</h1>
</section>
```

### Numbered Heading

```html
<section style="margin: 34px 0 16px;">
  <p style="margin: 0 0 6px; font-size: 18px; color: #2563eb; font-weight: 800;">01</p>
  <h2 style="margin: 0; padding-bottom: 8px; border-bottom: 2px solid #2563eb; font-size: 20px; line-height: 1.4; color: #111827;">...</h2>
</section>
```

### Highlight

```html
<p style="margin: 18px 0; padding: 12px 14px; background: #fff1a8; border-left: 4px solid #111827; font-size: 16px; line-height: 1.7; font-weight: 700;">...</p>
```

### Participant Card

```html
<section style="margin: 14px 0; padding: 16px; border: 1.5px solid #111827; border-radius: 8px; background: #ffffff;">
  <p style="margin: 0 0 8px; font-weight: 800; color: #2563eb;">路演项目组</p>
  <p style="margin: 0; line-height: 1.75;">...</p>
</section>
```

### Timeline Row

```html
<section style="margin: 12px 0; padding: 14px 16px; background: #f3f7fb; border-left: 4px solid #2563eb; border-radius: 6px;">
  <p style="margin: 0 0 4px; font-size: 13px; color: #2563eb; font-weight: 800;">14:00-14:10</p>
  <p style="margin: 0; font-weight: 700;">开场介绍</p>
  <p style="margin: 6px 0 0; color: #374151;">...</p>
</section>
```

## HTML Quality Checklist

Before delivering HTML, verify:

- A Frontend Design Plan is present before the HTML.
- The HTML is based on complete WeChat article copy, not a short summary.
- Article-to-HTML Mapping is present before the HTML.
- Article Coverage Check is present before the HTML and passes.
- A Component Blueprint is present before the HTML.
- Frontend Design Capability Mapping is present before the HTML.
- WeChat Compatibility Translation is present before the HTML.
- The design pass names a specific visual concept beyond the selected style family.
- The HTML reflects the design pass through hierarchy, spacing, recurring motifs, and component choices.
- For multi-style output, each version has a different motif and component system, not just different colors.
- For multi-style output, include a short style-difference summary comparing first screen, headings, cards, agenda, info block, and CTA.
- The article remains readable if all dynamic behavior is removed.
- No `script`, `style` block, `link rel`, `@keyframes`, `animation`, or external asset is required.
- Important text is real text, not hidden in images.
- All important event facts match the approved copy.
- Tentative facts remain tentative.
- QR placeholders are obvious.
- Mobile reading is comfortable: no cramped text, no tiny labels, no wide tables.
- The style family is recognizable but not over-decorated.
