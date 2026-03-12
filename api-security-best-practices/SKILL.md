---
name: api-security-best-practices
description: "Implement secure API design patterns including authentication, authorization, input validation, rate limiting, and protection against common API vulnerabilities"
---

# API Security Best Practices

Use this skill to choose and implement API-specific security controls. Keep it focused on the API surface itself: authentication, authorization, request validation, abuse controls, safe data handling, and protocol hardening for REST, GraphQL, WebSocket, and webhook receivers.

## When To Use This Skill

- Use when designing or hardening an API endpoint, route group, schema, subscription, socket channel, or webhook receiver.
- Use when selecting authentication or session patterns for an API caller.
- Use when adding authorization checks for resource access, workflow access, or response shaping.
- Use when deciding request validation, file-upload handling, URL handling, or safe error responses.
- Use when setting limits for brute force, replay, pagination, concurrency, or expensive operations.

## When To Pair It With Other Skills

- Use `$tool-design` when the change introduces or reshapes an HTTP endpoint, CLI surface, MCP tool, or other public contract.
- Use `$security-threat-model` when code changes affect security posture or when the task becomes a structured security review.
- Use `$testing-and-evals` after behavior changes so auth flows, validation, replay protection, and abuse controls are actually verified.
- Use `$observability-and-audit` when the API runs as a service and needs logging, tracing, metrics, or audit records.
- Use `$delivery-cicd-rollout` when the secured API change is heading to staging or production.

## Boundaries

- Do focus on API implementation controls and API-facing attack surfaces.
- Do not replace generic threat modeling, security-only review, test-gate enforcement, observability design, or release discipline.
- Do not lock the work to a single framework unless the repository already requires one.
- Do not treat third-party API responses or tool output as trusted; validate and constrain them before reuse.

## Workflow

Follow this sequence:

1. Triage the API surface.
2. Load only the references that match the surface.
3. Choose controls for authentication, authorization, validation, abuse resistance, and protocol hardening.
4. Produce the reusable artifacts for the endpoint or API surface.
5. Hand off adjacent concerns to the dedicated skills instead of duplicating them here.

## Step 1: Triage The Surface

Start with [references/api-surface-triage.md](references/api-surface-triage.md).

Record:

- exposure: public, partner, internal, or admin-only
- caller type: browser, server-to-server, third-party integration, device, or background job
- protocol: REST, GraphQL, WebSocket, or webhook receiver
- operation shape: read, write, bulk, export, async trigger, or streaming
- tenant model: single-tenant, multi-tenant, or mixed
- sensitive data: credentials, financial data, health data, PII, secrets, or regulated records
- untrusted payloads: file uploads, URLs, HTML, raw JSON, callbacks, or webhook bodies

Use the triage output to decide which references to load next and which other skills must be invoked.

## Step 2: Load The Matching References

Choose only what matches the surface:

- [references/authentication-and-session-controls.md](references/authentication-and-session-controls.md)
  Read when choosing between session cookies, bearer tokens, OAuth/OIDC, API keys, or mTLS.
- [references/authorization-control-patterns.md](references/authorization-control-patterns.md)
  Read when any user, tenant, role, scope, or workflow restriction applies.
- [references/validation-and-data-handling.md](references/validation-and-data-handling.md)
  Read for any user-controlled input, file upload, callback URL, response shaping, or safe error contract.
- [references/abuse-and-resource-controls.md](references/abuse-and-resource-controls.md)
  Read when the API is public, expensive, write-heavy, brute-forceable, or replayable.
- [references/protocol-hardening.md](references/protocol-hardening.md)
  Read for REST, GraphQL, WebSocket, and webhook-specific controls.
- [references/owasp-api-top-10-control-map.md](references/owasp-api-top-10-control-map.md)
  Read at the end to cross-check coverage against common API failure modes.

## Step 3: Choose Controls

### Authentication And Session Controls

- Bind the caller identity to the narrowest practical audience, scope, tenant, and lifetime.
- Choose a revocation and rotation story before treating the auth method as complete.
- Prefer server-managed sessions for browser-first apps when you control both client and server.
- Prefer short-lived bearer tokens for non-browser clients when stateless transport matters.
- Use API keys only for service or partner access that can tolerate narrow scope, rotation, and explicit inventory.
- Use mTLS only when you can operate certificate issuance, rotation, and revocation.

### Authorization Controls

- Enforce authorization on every request, not just at login.
- Check object, function, and property-level access separately when the resource model requires it.
- Bind authorization to tenant, ownership, workflow state, and intended action.
- Treat batch operations, exports, search results, and asynchronous jobs as high-risk authz surfaces.
- Use a matrix artifact when multiple roles, tenants, or policy branches exist.

### Validation And Safe Data Handling

- Validate path, query, header, cookie, body, file, and URL inputs against explicit schemas.
- Reject unknown fields by default unless the contract explicitly allows them.
- Enforce content types and size limits before expensive parsing.
- Shape responses so clients only receive fields they are allowed to see.
- Keep error bodies stable and useful without leaking stack traces, secrets, or backend internals.

### Abuse And Resource Controls

- Rate-limit by the actor or surface that actually reflects abuse: account, API key, tenant, IP, or session.
- Apply stricter controls to login, reset, upload, export, and other expensive or brute-forceable paths.
- Cap pagination, request body size, concurrency, and execution time.
- Require idempotency or replay protection for retriable write paths and signed callbacks.
- Treat GraphQL complexity, WebSocket message volume, and webhook replay as resource-control problems.

### Protocol Hardening

- REST: align verbs, idempotency, content-type enforcement, CORS, and cache behavior with the contract.
- GraphQL: enforce field auth, depth or complexity limits, operation allowlists or persisted queries, and schema exposure policy.
- WebSocket: authenticate at connect time, authorize channels and message types, validate every message, and rate-limit long-lived connections.
- Webhooks: verify signatures over the raw body, enforce timestamp windows, store replay identifiers, and fail closed on verification errors.

## Step 4: Produce Artifacts

Use the bundled templates rather than rewriting the same documents from scratch:

- [assets/templates/endpoint-security-profile.md](assets/templates/endpoint-security-profile.md)
  Use for a single endpoint, operation, or API surface.
- [assets/templates/authorization-matrix.csv](assets/templates/authorization-matrix.csv)
  Use when roles, scopes, tenants, or ownership rules need to be explicit.
- [assets/templates/error-response-contract.json](assets/templates/error-response-contract.json)
  Use as the safe default error envelope.
- [assets/templates/abuse-controls-matrix.md](assets/templates/abuse-controls-matrix.md)
  Use to capture endpoint-class limits and replay controls.

## Step 5: Use The Scripts When The Artifact Should Be Generated

- [scripts/render_api_security_checklist.py](scripts/render_api_security_checklist.py)
  Generates a scoped markdown checklist from the surface, protocol, auth mode, and risk flags.
- [scripts/render_authz_matrix.py](scripts/render_authz_matrix.py)
  Generates a CSV or markdown authorization matrix from JSON or YAML rules.

Use the scripts when the task needs a fast, repeatable artifact. Read or patch them before extending their behavior.

## Reference Guide

Use the references in this order for most endpoint work:

1. [references/api-surface-triage.md](references/api-surface-triage.md)
2. [references/authentication-and-session-controls.md](references/authentication-and-session-controls.md)
3. [references/authorization-control-patterns.md](references/authorization-control-patterns.md)
4. [references/validation-and-data-handling.md](references/validation-and-data-handling.md)
5. [references/abuse-and-resource-controls.md](references/abuse-and-resource-controls.md)
6. [references/protocol-hardening.md](references/protocol-hardening.md)
7. [references/owasp-api-top-10-control-map.md](references/owasp-api-top-10-control-map.md)

Common patterns:

- Public REST endpoint with bearer auth:
  - triage
  - auth/session controls
  - authorization controls
  - validation and data handling
  - abuse and resource controls
  - protocol hardening
  - OWASP cross-check
- GraphQL API with mixed read and write operations:
  - triage
  - auth/session controls
  - authorization controls
  - abuse and resource controls
  - protocol hardening
  - OWASP cross-check
- Webhook receiver:
  - triage
  - validation and data handling
  - abuse and resource controls
  - protocol hardening
  - OWASP cross-check

## Outputs This Skill Should Produce

The end result should usually include:

- a clear statement of the API surface and caller model
- the chosen authentication and authorization pattern
- the validation and response-shaping rules
- the abuse-control set for that surface
- the protocol-specific hardening steps
- the supporting template artifacts when the task benefits from them

## Hand-Off Rules

- If the work asks for a threat model, exploit analysis, prompt-injection review, or structured findings, switch to `$security-threat-model`.
- If the work asks for test cases, evals, or runtime verification, switch to `$testing-and-evals`.
- If the work asks for logs, trace IDs, metrics, or audit records, switch to `$observability-and-audit`.
- If the work asks for rollout, release readiness, CI green status, rollback, or migration discipline, switch to `$delivery-cicd-rollout`.
- If the work asks for endpoint or tool-contract design details, pair with `$tool-design`.

## Defaults

- Default to deny-by-default authorization.
- Default to schema-first validation with unknown-field rejection.
- Default to short-lived credentials with explicit revocation or rotation paths.
- Default to bounded pagination, bounded payload sizes, and bounded execution time.
- Default to safe error contracts and minimal response fields.

## Final Reminder

This skill is strongest when it stays narrow: secure the API surface, produce the concrete control artifacts, and hand off the adjacent disciplines instead of duplicating them.
