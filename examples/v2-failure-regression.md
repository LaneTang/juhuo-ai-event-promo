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
- use that full article as the HTML source
- produce a `Frontend Design Plan`
- produce `Article-to-HTML Mapping`
- produce `Article Coverage Check`
- select and follow a `Component Blueprint`
- provide `Frontend Design Capability Mapping`
- provide `WeChat Compatibility Translation`
- make multi-style HTML versions structurally distinct

## Second Failure Pattern: Good Copy, Bad HTML Source

Observed symptom:

- WeChat article contained a mature hook,导语, background, participant invitations, rules, agenda, and closing invitation.
- HTML kept only title, one sentence, participant labels, agenda times, and info block.

Expected gates:

- `Article coverage passed` should fail.
- `Missing article mapping` should fail.
- `Compressed source copy` should fail.

Correct behavior:

- HTML must preserve the article's hook questions,导语 paragraphs, background explanation, participant details, rule notes, agenda explanations, and closing invitation.
- The fact table may verify facts, but must not become the HTML content source after WeChat copy exists.
