# Full Article HTML Rendering

Use this reference for every WeChat HTML layout task.

Core rule: WeChat HTML must render the complete generated WeChat article. The HTML task is layout and visual treatment, not rewriting, summarizing, or reselecting content.

The fact table remains the truth source for checking facts, but once WeChat copy exists, the WeChat article is the sole body-content source for HTML.

## Non-Negotiable Text Preservation

Every substantive text unit from the approved WeChat article must appear in the HTML.

Substantive units include:

- title
- subtitle/opening visual line if present
- every heading
- every paragraph
- every list item
- golden sentence / highlighted sentence
- participant category names and descriptions
- rules/checklist items
- agenda items and their explanations
- time/location/registration information
- closing invitation
- QR or link placeholder

Allowed:

- Wrap text in styled `section`, `p`, `span`, `strong`, or similar HTML elements.
- Split a long paragraph into smaller visual lines if all words remain.
- Promote an existing sentence into a highlight block.
- Add small decorative labels such as `INVITATION`, `BUILD LOG`, or `FIELD NOTE`.
- Add section wrappers, dividers, labels, callouts, and visual hierarchy.

Not allowed:

- Delete substantive text.
- Summarize paragraphs.
- Rewrite the article in shorter wording.
- Replace paragraphs with fact-table bullets.
- Collapse participant descriptions into one-line labels.
- Keep agenda times but remove agenda explanations.
- Drop the opening hook, background, rules, closing invitation, or placeholders.
- Use "major unit coverage" as permission to omit smaller paragraphs.

## Required Rendering Step

Before writing HTML, split the approved WeChat article into text units and render all of them.

Use this output format:

```markdown
## Full Article Rendering Plan

The HTML will render the complete approved WeChat article without summarizing or omitting substantive text.

| Source text unit | HTML treatment |
|---|---|
| Title | First screen title block |
| Opening paragraph 1 | Intro letter paragraph |
| Rule item 1 | Checklist row |
```

## Text Preservation Check

- Source text units: N
- Rendered text units: N
- Omitted substantive units: 0
- Rewritten/summarized units: 0
- Result: PASS
```

If `Omitted substantive units` or `Rewritten/summarized units` is not 0, the HTML fails.

## Design Relationship

Apply visual design around the article, not instead of the article.

- Component blueprints decide how to wrap and emphasize text.
- Frontend-design principles decide hierarchy, rhythm, and visual concept.
- They must not be used to shorten the article.

## Relationship To Fact Table

Use the fact table only to:

- verify facts in the article
- preserve uncertainty
- avoid unsupported claims
- check consistency across channels

Do not use the fact table as the body-content source for HTML once WeChat copy exists.
