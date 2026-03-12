# OWASP API Top 10 Control Map

When to read this: Read this after choosing controls so you can cross-check coverage against common API failure modes without expanding into a full security review.

| OWASP API risk | What to confirm | Primary references |
| --- | --- | --- |
| API1 Broken Object Level Authorization | Object access is checked per resource and tenant | `authorization-control-patterns` |
| API2 Broken Authentication | Credential choice, scope, expiry, rotation, and revocation are explicit | `authentication-and-session-controls` |
| API3 Broken Object Property Level Authorization | Hidden or writable fields are filtered and authorized | `authorization-control-patterns`, `validation-and-data-handling` |
| API4 Unrestricted Resource Consumption | Limits exist for rate, size, pagination, concurrency, and expensive queries | `abuse-and-resource-controls`, `protocol-hardening` |
| API5 Broken Function Level Authorization | Admin or privileged actions are denied by default and checked server-side | `authorization-control-patterns` |
| API6 Unrestricted Access To Sensitive Business Flows | Sensitive workflows have stricter authz and abuse controls | `authorization-control-patterns`, `abuse-and-resource-controls` |
| API7 Server Side Request Forgery | URLs and outbound fetch targets are validated and constrained | `validation-and-data-handling` |
| API8 Security Misconfiguration | Content types, CORS, protocol behavior, and error exposure are explicit | `validation-and-data-handling`, `protocol-hardening` |
| API9 Improper Inventory Management | The exposed surface and auth modes are explicitly triaged and documented | `api-surface-triage` |
| API10 Unsafe Consumption Of APIs | Third-party payloads and callbacks are validated before reuse | `validation-and-data-handling`, `protocol-hardening` |

## How To Use This Map

- Use it as a coverage check, not as a replacement for implementation detail.
- If a row is weak or unanswered, reopen the matching reference before finishing.
- If the task turns into a structured threat model or security review, switch to `$security-threat-model`.
