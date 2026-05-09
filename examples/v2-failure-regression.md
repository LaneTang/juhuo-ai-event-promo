# v2 Failure Regression

Use this regression when evaluating future changes to `juhuo-ai-event-promo`.

## Failed Forward-Test Symptoms

The failed output had two major issues:

1. WeChat copy was too short and abstract.
2. Three HTML versions shared the same skeleton with different colors and labels.

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
- select and follow a `Component Blueprint`
- provide `Frontend Design Capability Mapping`
- provide `WeChat Compatibility Translation`
- make multi-style HTML versions structurally distinct
