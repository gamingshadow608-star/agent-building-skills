---
name: testing-and-evals
description: Design and run tests, evals, and runtime checks as a mandatory verification gate whenever code, prompts, or skills are added or modified, or when the runbook reaches the test gate. Use to derive repo-native verification commands, enforce the write-run-fix-rerun loop, require startup checks and eval harnesses, and record evidence before security review.
---

# Testing And Evals

Treat tests, evals, and runtime checks as a hard gate before completion and before security review. Do not move past the test gate until the relevant verification passes and the evidence is recorded.

Use progressive disclosure. Read only the support file that matches the current verification task:

- [references/test-selection.md](references/test-selection.md)
- [references/risk-surface-checklist.md](references/risk-surface-checklist.md)
- [references/eval-harness.md](references/eval-harness.md)
- [assets/templates/evals.json](assets/templates/evals.json)
- [assets/templates/test-eval-evidence.md](assets/templates/test-eval-evidence.md)

## Workflow

Follow this sequence every time behavior changes:

1. Derive repo-native verification commands from the repo scan.
   - Prefer existing test scripts, task runners, CI commands, and documented entrypoints before generic examples.
   - Use generic stack examples only when the repo does not define a better command path.
   - Use [references/test-selection.md](references/test-selection.md) to choose commands and check types.
2. Map the changed behavior to the required checks.
   - Use unit tests for function-level logic and pure rules.
   - Use integration tests for tool interactions, side effects, boundary crossings, auth flows, and multi-step behavior.
   - Use smoke or startup checks to prove the runnable entrypoint starts without crashing.
   - Use evals when behavior depends on prompts, skills, orchestration, tool choice, or retrieval trajectories.
   - Use [references/risk-surface-checklist.md](references/risk-surface-checklist.md) when the change touches high-risk behavior.
3. Require an eval harness when deterministic tests alone are not enough.
   - Store prompts and expected outputs in `evals/evals.json`.
   - Run each case twice: `with_skill` and `without_skill`.
   - Add deterministic assertions and record pass or fail evidence.
   - Use [references/eval-harness.md](references/eval-harness.md) and [assets/templates/evals.json](assets/templates/evals.json).
4. Run the test loop.
   - Write or update the relevant tests.
   - Run the relevant tests and checks.
   - Fix failures, regressions, and broken assumptions.
   - Re-run until all relevant checks pass.
5. Verify that the build actually runs.
   - Start the real web server, CLI, worker, job runner, or equivalent entrypoint when one exists.
   - Treat import-only or boot-only checks as fallback evidence, not the preferred proof, when a real startup path is available.
6. Record verification evidence in the final report.
   - Record commands, pass or fail status, key logs, startup results, eval outcomes, and blockers.
   - Use [assets/templates/test-eval-evidence.md](assets/templates/test-eval-evidence.md) when the repo does not define its own format.
7. Only then allow security review.

## Gate Rules

- Do not stop after writing tests.
- Do not stop after the first failing run.
- Do not treat unrun tests as acceptable coverage.
- Do not hand off to security review until testing, evals, and runtime verification are complete.

## Blocked Verification

If a required test, eval, or startup check cannot run:

- Record the exact command attempted.
- Record the blocker, such as missing dependencies, missing credentials, unavailable infrastructure, or missing approval.
- Record what remains unverified and the risk of shipping without that evidence.
- Leave the verification gate unsatisfied. Blocked verification is not completion.

## Risk-Surface Coverage

Cover the highest-risk surfaces changed by the work. Require targeted tests or eval cases for:

- Auth and session handling
- Tool side effects
- Idempotency and replay behavior
- Memory or RAG retrieval behavior
- Injection resistance

Expand coverage when the change touches privileged flows, retries, remote calls, background jobs, or boundary-crossing behavior.

## Boundaries

- Do not design tool schemas or tool contracts here.
- Do not perform or define security review procedure here.
- Do not enforce architecture decisions here.
- Do not assume a particular language; adapt commands to the detected stack from the repo scan.
- Do focus on verification design, test execution, eval harnesses, runtime verification, blocker reporting, and recording results before completion.
