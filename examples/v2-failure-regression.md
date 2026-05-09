# v2 Failure Regression

Use this regression when evaluating future changes to `juhuo-ai-event-promo`.

## Failed Forward-Test Symptoms

The failed output had two major issues:

1. WeChat copy was too short and abstract.
2. Three HTML versions shared the same skeleton with different colors and labels.
3. A later forward test improved WeChat copy, but HTML still appeared to be generated from the fact table or summary instead of the complete WeChat article.

## Why It Should Fail Now

### WeChat Copy

The failed WeChat article was structured like:

- short intro
- suitable audiences
- activity info
- agenda
- closing sentence

It lacked:

- strong title hook
- scene-setting introduction
- explanation of why the event matters
- mature campus community voice
- human participant invitations
- rule/agenda expansion
- warm closing scene

Expected gate: `WeChat article is publishable` should fail.

### HTML

The three failed HTML versions shared the same layout:

- title card
- one highlight
- activity info card
- audience cards
- process list
- registration placeholder
- CTA card

The differences were mostly palette and labels:

- campus blue
- dark/cyan maker
- gray editorial

Expected gates:

- `HTML follows component blueprint` should fail.
- `Style drift in multi-version output` should fail.

## Passing Behavior

A passing output must:

- generate a full WeChat article from `wechat-golden-copy-style.md`
- render that full article in HTML without omitting, rewriting, or summarizing substantive text
- produce a `Frontend Design Plan`
- produce `Full Article Rendering Plan`
- produce `Text Preservation Check`
- select and follow a `Component Blueprint`
- provide `Frontend Design Capability Mapping`
- provide `WeChat Compatibility Translation`
- make multi-style HTML versions structurally distinct

## Second Failure Pattern: Good Copy, Bad HTML Source

Observed symptom:

- WeChat article contained a mature hook,导语, background, participant invitations, rules, agenda, and closing invitation.
- HTML kept only title, one sentence, participant labels, agenda times, and info block.

Expected gates:

- `Full article rendered` should fail.
- `Missing full article rendering plan` should fail.
- `Text preservation failed` should fail.
- `Compressed source copy` should fail.

Correct behavior:

- HTML must display the full article's hook questions,导语 paragraphs, background explanation, participant details, rule notes, agenda explanations, and closing invitation.
- HTML may add design wrappers, but may not delete, summarize, or rewrite substantive article text.
- The fact table may verify facts, but must not become the HTML content source after WeChat copy exists.
