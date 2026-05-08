# End-to-End Test Report

Test date: 2026-05-08

Skill under test: `juhuo-ai-event-promo`

## Inputs

| Case | Source File | Format | Read Result |
|---|---|---|---|
| Mingyuehu AI entrepreneurship event | `uploaded-plan: 明月湖科创园科创情报局系列-AI赋能创业交流活动方案-对接炬火.doc` | `.doc` | Read successfully through `scripts/extract_plan_text.py` using Word COM extraction. |
| Juhuo AI practice month roadshow | `uploaded-plan: 炬火AI实践月_AIx分享会1_大创专题暨模拟路演_新版策划案.docx` | `.docx` | Read successfully through `scripts/extract_plan_text.py` using OOXML extraction. |

## Outputs

| Case | Output File |
|---|---|
| Mingyuehu AI entrepreneurship event | `examples/e2e-test-mingyuehu-promo-pack.md` |
| Juhuo AI practice month roadshow | `examples/e2e-test-juhuo-promo-pack.md` |

## Gate Findings

| Case | Gate Result | Main Issues |
|---|---|---|
| Mingyuehu | BLOCKER + warnings | Registration method missing; start/end time comes from agenda; internal division of labor excluded; avoid overpromising resource matching. |
| Juhuo | BLOCKER + warnings | Location is tentative; registration QR/link missing; co-organizer undetermined; internal form fields excluded; avoid overpromising project outcomes. |

## Skill Behavior Checked

- Fact extraction happened before copywriting.
- Facts were labeled as public, sensitive, internal, confirmed, tentative, or missing.
- Public copy did not expose staff roles, equipment lists, form field designs, or internal division of labor.
- Tentative location in the Juhuo plan was not replaced with an invented venue.
- Missing registration methods were represented as explicit placeholders.
- WeChat, Xiaohongshu, and QQ outputs were generated separately.
- QQ output uses a unified QQ copy rather than reusing Xiaohongshu hashtags by default.
- Cross-platform facts stayed aligned inside each event package.

## Issues Found In The Skill

The end-to-end run exposed one useful design issue that has now been addressed:

- The skill can complete `.docx` extraction with lightweight OOXML parsing.
- Old `.doc` files need Word COM, LibreOffice, antiword, or another converter.
- The skill now includes `scripts/extract_plan_text.py`, which supports `.docx`, `.docm`, `.doc`, `.wps`, `.wpt`, and `.pdf` with OOXML, optional PDF libraries, optional `olefile` fallback, external converters, and Word COM fallback.

Recommended follow-up:

- Test the script on real `.wps` and `.pdf` plans when those appear.
- If PDF plans become common, consider adding a bundled PDF dependency recommendation such as `pypdf`.

## Verdict

The skill is usable for v1 copy-package generation.

It correctly blocks final publication when required facts are missing, while still producing clearly marked draft copy with placeholders.
