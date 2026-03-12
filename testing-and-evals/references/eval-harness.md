# Eval Harness

Use evals when behavior depends on prompts, skills, orchestration, retrieval, or tool trajectories and deterministic unit or integration tests are not enough.

## When To Require Evals

- Prompt changes
- Skill changes
- Multi-agent or orchestration changes
- Tool selection or refusal behavior changes
- Retrieval-dependent behavior changes

## Required Pattern

1. Create or update `evals/evals.json`. Start from [../assets/templates/evals.json](../assets/templates/evals.json) if the repo does not already define a format.
2. Store prompts, expected behavior, and deterministic assertions for each case.
3. Run each case twice:
   - `with_skill`
   - `without_skill`
4. Compare outcomes against the assertions instead of relying on vague judgments.
5. Record pass or fail evidence for every case in the final report.

## Case Design

- Keep each case narrow and tied to one behavior change.
- Prefer assertions such as `contains`, `not_contains`, `matches`, `uses_tool`, `avoids_tool`, or exact structured-output checks.
- If the behavior is too nondeterministic for stable assertions, tighten the prompt, fixture, or tool setup before accepting the eval.
- Include at least one failure-oriented case when the change affects safety, refusal behavior, auth, or retrieval trust boundaries.
