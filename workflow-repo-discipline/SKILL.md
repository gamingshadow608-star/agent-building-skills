---
name: workflow-repo-discipline
description: Enforce gated workflow and repo discipline for agentic coding work that follows an AGENTS.md runbook or control-file chain. Use when repo scan or a project manager indicates workflow discipline is needed, a runbook is present, work is multi-phase, or the user requests enterprise-grade rigor; operate strict by default, record active skills and gate evidence, and do not skip steps. Do not trigger for casual one-off work unless the user explicitly asks for strict workflow discipline.
---

# Workflow Repo Discipline

Enforce process. Follow the effective `AGENTS` control-file chain as the source of truth for workflow order, tracker location, and required deliverables. Keep this skill focused on workflow discipline, state tracking, and delegation.

## Workflow

1. [ ] Identify the effective control-file chain for the current working directory and confirm the authoritative runbook, gate order, tracker location, and required deliverables. Read [references/control-file-discovery.md](references/control-file-discovery.md) only when precedence or tracker ownership is unclear.
2. [ ] Reconcile current state before acting: read prior progress, determine the earliest unsatisfied gate, and resume there instead of restarting or silently skipping ahead.
3. [ ] Perform a repo scan and record which skills are active, why they activated, and what repo evidence supports them. Read [references/repo-scan-signals.md](references/repo-scan-signals.md) only when activation evidence is unclear.
4. [ ] Update the designated live tracker before starting work, after each meaningful step, and before any gate transition.
5. [ ] Adhere to `Gate 0` through `Gate 5` in order, or the repo-defined equivalents. Read [references/gate-rules.md](references/gate-rules.md) only when the runbook omits gate meaning or handoff expectations.
6. [ ] Record blockers and risks continuously as they appear, change, or are resolved.
7. [ ] Produce a final report summary that captures workflow progression, activated skills, gate completion evidence, blockers, risks, and remaining follow-up items. Reuse [assets/final-report-template.md](assets/final-report-template.md) when the repo does not provide its own format.

## Missing Runbook Behavior

- Stop and ask if no authoritative runbook exists.
- Stop and ask if the control-file chain does not resolve a clear gate order, tracker location, or owner for workflow updates.
- Do not invent gates, tracker fields, or workflow status rules when the repo-level control system is ambiguous.

## Status Tracking

Maintain the designated live tracker throughout the task. Update the runbook itself only when it is clearly the live tracker; otherwise update the tracker file, section, or task log that the runbook names.

Update these fields:

- `Current gate`
- `Percent complete`
- `Active skills`
- `Completed in this gate`
- `Remaining tasks`
- `Next required step`
- `Blockers`
- `Risks`
- `Gate evidence`

Use [assets/status-tracker-template.md](assets/status-tracker-template.md) only when the runbook does not already define a tracker format.

## Gate Discipline

- Treat `Gate 0`, `Gate 1`, `Gate 2`, `Gate 3`, `Gate 4`, and `Gate 5` as hard gates.
- Before moving to the next gate, write a short acknowledgement in the tracker or working notes that the current gate is satisfied.
- Cite the artifact, decision, or delegated-skill output that satisfied the gate.
- Do not advance while required outputs, open blockers, or unresolved gate criteria remain.
- Preserve explicit gate order and reporting even when rigor is lowered; only reduce artifact depth when the user explicitly requests lighter process.

## Rigor

- Default to `STRICT`.
- Lower rigor only if the user explicitly says `casual`, `small`, or `personal`, or gives an equally clear instruction to reduce process.
- In `STRICT` mode, enforce the full runbook sequence, status updates, blocker and risk logging, active-skill logging, and final reporting.

## Delegation

Require the relevant specialist-skill outputs before closing the corresponding gate. Push detailed execution rules into the appropriate skills instead of duplicating them here:

- Use `agent-architecture-memory` for architecture briefs, diagrams, state handling, and memory decisions that satisfy the design gate.
- Use `testing-and-evals` for tests, startup checks, verification loops, and eval evidence that satisfy the verification gate.
- Use `security-threat-model` for security review, findings, residual risk, and fix guidance that satisfy the security gate.
- Use `tool-design` for tool contracts, schemas, validation, auth, and interface details.
- Use `rag-data-safety`, `observability-and-audit`, and `delivery-cicd-rollout` when the repo scan shows retrieval, deployed services, or rollout concerns.

## Boundaries

- Do not define or assume memory models.
- Do not perform security reviews.
- Do not run tests.
- Do not write code.
- Do enforce process, control-file discovery, tracker updates, gate order, blocker and risk logging, and final workflow reporting.

Final reminder: the end-of-project report must summarize control files used, activated skills, gate completion evidence, blockers, risks, and remaining follow-up items.
