# API Surface Triage

When to read this: Use this first for any API task so you classify the surface before choosing controls or loading other references.

## Capture The Surface

Record these facts before proposing controls:

| Signal | Values to record | Why it matters | Load next | Also invoke |
| --- | --- | --- | --- | --- |
| Exposure | `public`, `partner`, `internal`, `admin` | Changes attacker reach and abuse assumptions | `validation-and-data-handling`, `abuse-and-resource-controls` | `$security-threat-model` for posture-changing work |
| Caller type | `browser`, `server`, `third-party`, `device`, `job` | Drives auth and session choice | `authentication-and-session-controls` | `$tool-design` if the contract changes |
| Protocol | `rest`, `graphql`, `websocket`, `webhook` | Changes protocol-specific hardening | `protocol-hardening` | `$tool-design` for new or changed interfaces |
| Operation shape | `read`, `write`, `bulk`, `export`, `stream`, `async trigger` | Changes authz, replay, and limit design | `authorization-control-patterns`, `abuse-and-resource-controls` | `$testing-and-evals` after implementation |
| Tenant model | `single-tenant`, `multi-tenant`, `mixed` | Changes object and property authz | `authorization-control-patterns` | `$security-threat-model` if isolation boundaries change |
| Sensitive data | credentials, secrets, PII, financial, health, regulated data | Changes response shaping and error discipline | `validation-and-data-handling` | `$observability-and-audit` for deployed services |
| Untrusted payloads | uploads, URLs, HTML, callbacks, raw webhook bodies | Changes validation and SSRF or replay risk | `validation-and-data-handling`, `protocol-hardening` | `$security-threat-model` for risky ingest paths |

## Triage Questions

- Who can reach this surface today, and who should be able to reach it after the change?
- Is the caller a browser, a server, a partner, or an automated system?
- Is the surface read-only, write-capable, or both?
- Does the request or response cross tenant boundaries?
- Does the request carry uploads, URLs, raw JSON, HTML, or third-party callbacks?
- Could retries, batching, or long-running work duplicate or amplify side effects?

## Surface-To-Reference Mapping

- Public or partner-facing surface:
  - Read `validation-and-data-handling`.
  - Read `abuse-and-resource-controls`.
  - Read `protocol-hardening`.
- Authenticated or scoped surface:
  - Read `authentication-and-session-controls`.
  - Read `authorization-control-patterns`.
- Multi-tenant or ownership-sensitive surface:
  - Read `authorization-control-patterns`.
  - Use `assets/templates/authorization-matrix.csv`.
- Upload, callback URL, or webhook surface:
  - Read `validation-and-data-handling`.
  - Read `protocol-hardening`.
- Expensive or replayable write path:
  - Read `abuse-and-resource-controls`.
  - Use `assets/templates/abuse-controls-matrix.md`.

## Hand-Off Decisions

- Invoke `$tool-design` when the endpoint, schema, or contract itself is being created or reshaped.
- Invoke `$security-threat-model` when the task needs a threat model, trust-boundary analysis, or a security-only review.
- Invoke `$testing-and-evals` when controls are chosen and behavior must be verified.
- Invoke `$observability-and-audit` when the service needs logging, tracing, metrics, or audit records.
- Invoke `$delivery-cicd-rollout` when the change is preparing for release or rollout.

## Triage Output Template

Use this shape in notes or drafts:

```text
surface:
  exposure:
  caller_type:
  protocol:
  operation_shape:
  tenant_model:
  sensitive_data:
  untrusted_payloads:
load_references:
  - ...
invoke_skills:
  - ...
artifacts:
  - endpoint-security-profile
  - authorization-matrix
  - abuse-controls-matrix
```
