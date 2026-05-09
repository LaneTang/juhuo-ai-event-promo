# Article To HTML Mapping

Use this reference for every v2 WeChat HTML task.

Core rule: the complete generated WeChat article is the only content source for v2 HTML. The fact table remains the truth source for checking facts, but it must not be used to replace, compress, or rewrite the article during HTML generation.

## Required Mapping Step

Before writing HTML, break the approved WeChat article into article units.

Article units usually include:

- title and subtitle/opening line
- hook questions or opening scene
-导语 paragraphs
- golden sentence
- numbered sections
- participant invitation paragraphs
- rules/checklist paragraphs
- agenda paragraphs with explanations
- time/location/registration block
- closing invitation
- QR placeholder

Then map each unit to an HTML component.

Use this format:

```markdown
## Article-to-HTML Mapping

| Article unit | Source content summary | HTML component | Keep / Merge / Omit |
|---|---|---|---|
| Title | ... | first screen title block | Keep |
| Opening hook | ... | intro letter block | Keep |
```

## Article Coverage Check

- Source article units: N
- HTML-covered units: N
- Omitted units: 0 or list with reason
- Coverage result: PASS / FAIL
```

## Coverage Requirements

Default requirement:

- Cover all major article units.
- Omit no section unless it is duplicated, unsafe, or explicitly excluded by the user.
- Do not compress a mature article into an event-info page.
- Do not reduce participant invitation paragraphs into one-line labels.
- Do not reduce agenda explanations into only time labels.

Hard fail:

- HTML drops the opening hook/scene.
- HTML drops activity background or value explanation.
- HTML drops participant invitation detail.
- HTML drops rules/participation notes when the article has them.
- HTML drops agenda explanations and keeps only times.
- HTML keeps less than about 80% of the article's substantive units.
- HTML reads like it was generated from the fact table instead of the approved article.

## How To Preserve Long Articles

If the article is long, preserve it through layout rather than summarizing:

- Use collapsible-like visual grouping without actual interaction: section bands, note blocks, timeline rows.
- Keep paragraph text real and visible.
- Merge only adjacent paragraphs that repeat the same point.
- Use visual hierarchy to make long text readable; do not delete the text.
- Use section rhythm, callouts, labels, and spacing to support scanning.

## Relationship To Fact Table

Use the fact table only to:

- verify facts in the article
- preserve uncertainty
- avoid unsupported claims
- check consistency across channels

Do not use the fact table as the content source for HTML once WeChat copy exists.
