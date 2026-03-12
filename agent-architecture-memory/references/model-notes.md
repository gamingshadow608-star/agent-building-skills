# Model Notes

Use this reference only when provider-specific behavior changes the architecture or orchestration plan.

## GPT-5.x

- Prefer explicit, task-shaped tool boundaries and clear success criteria in the architecture brief.
- Plan for strong instruction following, but still keep approvals, side effects, and trust boundaries explicit in the orchestration.
- Keep tool outputs and retrieved content separated from instructions in the design.

## Claude

- Expect project instructions, rules, and skills to layer through `CLAUDE.md` and related scoped files.
- Treat tool permissions and allowed-tool restrictions as part of the orchestration environment, not as an afterthought.
- Make approval points and safe read-only paths explicit when the workflow mixes planning, reading, and privileged actions.

## Gemini

- Expect function calling to favor typed tool contracts and explicit schema-friendly inputs.
- Plan for sequential or compositional tool use when the orchestration depends on multiple function calls.
- Keep the orchestration graph explicit so automatic function-calling behavior does not obscure retries, approvals, or side effects.

## Cross-Model Implications

- Keep the architecture brief provider-neutral by default.
- Move only provider-specific orchestration differences into this file.
- Update this reference when model-specific behavior changes graph shape, approval flow, or tool-calling assumptions.
