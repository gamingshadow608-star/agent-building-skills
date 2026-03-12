# Threat Model Template

Use this template during implementation before finishing any change that writes or modifies code, tools, or memory.

## Repo trust check

- Repo trust state: `trusted` / `partially trusted` / `untrusted` / `unknown`
- Untrusted external inputs in scope:
- Network state by default: `off` / `approved`
- Tool or execution restrictions until approval:
- Approval boundary that would be crossed next:

## Untrusted inputs

| Input source | Why it is untrusted | Confusable deputy path | Guard |
| --- | --- | --- | --- |
| `web page` |  |  |  |
| `tool output` |  |  |  |
| `RAG chunk` |  |  |  |

## Privileged actions and consequences

| Tool or action | Classification | Material parameters or scope | Consequence of misuse | Approval required | Guard |
| --- | --- | --- | --- | --- | --- |
|  | `read-only` / `write` / `delete` / `network` / `secret-bearing` / `memory trust-promotion` |  |  |  |  |

## Roles and capability boundaries

| Actor | Allowed capabilities | Forbidden capabilities | Approval or policy gate |
| --- | --- | --- | --- |
|  |  |  |  |

## Prompt injection and tool abuse checks

- [ ] Retrieved text, tool-returned text, logs, and external documents are treated as data, not instructions.
- [ ] Instruction and data are separated by policy, quoting, or structure.
- [ ] Each tool has allowed parameters, forbidden parameters, `data allowed`, and `data forbidden`.
- [ ] Tool inputs are schema-validated before execution.
- [ ] Destructive, networked, credentialed, or secret-bearing actions require explicit approval.

## Memory and RAG checks

- [ ] Every memory write records who wrote it, why, source, and timestamp.
- [ ] New memory stays quarantined until reviewed or trust-promoted.
- [ ] Retrieval output is filtered and marked as untrusted.
- [ ] Secrets and sensitive data are redacted or blocked.
- [ ] Retrieval and storage paths enforce access control.
- [ ] A forget path and retention window are defined.

## Secrets and logging

- [ ] Secrets, tokens, passwords, and credentials are absent from prompts, memory, and logs.
- [ ] Credential use is explicit, least-privilege, and time-bounded.
- [ ] Logs and audit trails avoid storing secret material.

## Approvals, residual risk, and notes

- Pending approvals:
- Residual risk:
- Notes for security review:
