# Security Review Template

Use this template at the security review gate. Focus on changed code, changed behavior, new tool surfaces, new memory flows, and new trust boundaries.

## Review rules

- Default confidence threshold: `0.80`
- Report only high-signal findings unless the user explicitly asks for broader coverage.
- Do not mix in generic code review feedback, architecture advice, or testing recommendations.

## Finding format

Use this exact finding shape:

```md
Security review

Finding 1: <category>: `<file>:<line>`

- Severity: High/Medium/Low
- Confidence: value between 0.0 and 1.0
- Description:
- Exploit scenario:
- Recommended patch:
- Residual risk:
- Notes (why this is high confidence):

Tool inventory

| Tool | Classification | Material parameters | Auth or scope | Approval decision | Sensitive side effects |
| --- | --- | --- | --- | --- | --- |
```

## No high-confidence findings path

If nothing meets the default confidence threshold, emit this instead of filler text:

```md
Security review

No high-confidence findings in the reviewed diff or changed behavior at the default confidence threshold of 0.80.

Tool inventory

- None.
```

## Severity rubric

- `High`: direct secret exposure, unauthorized write or delete, privilege escalation, remote code execution, or a clear path to material data exfiltration.
- `Medium`: meaningful security weakness with a plausible exploit path, but constrained by environment, approvals, or preconditions.
- `Low`: bounded hardening gap or defense-in-depth issue with limited direct impact.

## Confidence bar

- `0.90-1.00`: direct code evidence and a concrete exploit path.
- `0.80-0.89`: likely exploitable with strong evidence and limited assumptions.
- `< 0.80`: omit by default; include only if the user explicitly asks for broader or lower-confidence coverage.

## Tool inventory schema

Record every tool used during the review, including:

- tool name
- classification
- material parameters
- auth or scope used
- approval decision
- sensitive side effects, if any
