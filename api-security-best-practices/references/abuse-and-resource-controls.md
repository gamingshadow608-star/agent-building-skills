# Abuse And Resource Controls

When to read this: Read this when the API is public, expensive, brute-forceable, replayable, or otherwise exposed to resource abuse.

## Baseline Controls

Set limits for:

- request rate per actor and per network origin
- burst behavior and cooldown windows
- request body size and upload size
- pagination size and total export size
- concurrency and long-running job fan-out
- execution timeouts and downstream retry budgets

## Choose The Right Limiting Key

- Prefer authenticated subject, API key, service identity, or tenant when available.
- Fall back to IP or network range only when no stronger identity exists.
- Use stricter per-surface keys for login, password reset, OTP verification, and similar flows.
- Apply separate limits to admin and support actions even when the caller is trusted.

## High-Risk Endpoint Classes

- Authentication endpoints:
  - low attempt budgets
  - lockout or progressive delay strategy
  - monitoring for credential stuffing
- Upload endpoints:
  - file-count caps
  - size caps
  - type validation
  - storage quotas
- Export and reporting endpoints:
  - queueing
  - concurrency limits
  - result expiration
- Expensive queries:
  - pagination caps
  - query complexity caps
  - narrowed filters

## Idempotency And Replay Defense

- Require idempotency keys for retriable create or mutate operations.
- Bind idempotency state to subject, route, and payload fingerprint when possible.
- Reject stale or conflicting reuse of an idempotency key.
- For signed callbacks and webhooks, store replay identifiers and timestamp windows.

## Timeout And Backpressure Rules

- Define server-side execution deadlines.
- Stop fan-out when downstream systems are degraded.
- Prefer explicit queueing or async jobs over unbounded synchronous work.
- Return stable overload or retry responses instead of letting timeouts leak internal behavior.

## Artifacts

Use `assets/templates/abuse-controls-matrix.md` to capture limits for:

- auth endpoints
- uploads
- GraphQL operations
- WebSocket messages
- webhook receivers

## Common Failure Modes

- One global rate limit is used for all routes, so login and export paths get the wrong protection.
- Idempotency is skipped for retried writes, causing duplicate charges or side effects.
- Pagination and export paths allow unbounded reads for trusted users.
- Webhook replay is checked by timestamp only, with no replay identifier store.
