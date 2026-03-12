# Gate Rules

Use this reference only when the authoritative runbook names `Gate 0` through `Gate 5` without defining them, or when status-update timing is unclear.

## Default Gate Map

- `Gate 0`: Confirm repo trust, sandbox boundaries, approvals, and the effective control-file chain.
- `Gate 1`: Complete planning or architecture artifacts required by the runbook. For non-trivial agentic work, require outputs from `agent-architecture-memory`.
- `Gate 2`: Implement only the current approved stage and keep tracker status current.
- `Gate 3`: Complete tests, evals, and runtime verification with evidence from `testing-and-evals`.
- `Gate 4`: Complete security review with evidence from `security-threat-model`.
- `Gate 5`: Publish the final workflow report and remaining follow-up items.

## Meaningful Status Updates

Update the live tracker after:

- A gate transition
- A new artifact or decision that changes completion state
- A verification result
- A blocker or risk appearing, changing, or clearing
- Re-scoping the next required step

## Blockers And Risks

- Record blockers as items that stop progress now
- Record risks as unresolved issues that could affect quality, security, delivery, or correctness
- Remove or close entries only when the reason is explicitly resolved

## Inherited Workflow Drift

When the repo already contains partial work or stale tracker state:

- Preserve existing evidence
- Reconcile the tracker to the earliest unsatisfied gate
- Record why the gate moved backward or stayed open
- Do not declare later gates complete when prerequisite evidence is missing
