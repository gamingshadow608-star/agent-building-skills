# Authentication And Session Controls

When to read this: Read this when the API needs caller identity, session continuity, delegated access, machine credentials, or credential rotation.

## Choose The Authentication Pattern

| Pattern | Best fit | Main strengths | Main hazards | Mandatory controls |
| --- | --- | --- | --- | --- |
| Session cookies | Browser-first apps you control end to end | Server-side revocation, no token parsing in clients | CSRF, cookie scope mistakes, weak session fixation handling | `HttpOnly`, `Secure`, `SameSite`, CSRF protection, session rotation |
| Bearer tokens | Mobile, SPA with a trusted backend, server-to-server | Stateless transport, easy API gateway integration | Token replay, overscoped claims, weak revocation | Short expiry, narrow audience and scope, rotation, revocation plan |
| OAuth/OIDC | Third-party delegation, enterprise identity, multi-client estates | Standard delegation and federation | Scope sprawl, weak redirect handling, token misuse | Redirect validation, issuer and audience checks, scope minimization |
| API keys | Partner or machine access with narrow capability | Simple issuance and inventory | Often over-broad, easy to copy, hard to attribute to humans | Key inventory, rotation, per-key scopes, rate limits, last-used tracking |
| mTLS | Controlled service meshes or high-trust machine channels | Strong machine identity at the transport layer | Operational complexity, cert rotation failure | Automated issuance, expiry monitoring, revocation, service mapping |

## Required Decisions

Record these before implementing:

- credential subject: human user, service account, partner client, or device
- audience: which API or resource server accepts the credential
- scope: what resources or actions the credential can request
- lifetime: default expiry and renewal behavior
- rotation: how secrets, signing keys, or certificates change without downtime
- revocation: how you block known-bad credentials before normal expiry

## Browser Versus Server Callers

- Browser callers:
  - Prefer server-managed sessions when the app and API share trust boundaries.
  - Treat cookie scope, CSRF protection, and cross-origin rules as part of the auth design.
  - Do not expose long-lived bearer tokens to browser storage without a strong reason.
- Server or service callers:
  - Prefer credentials tied to one service identity and one API audience.
  - Keep scopes narrow and machine-specific.
  - Pair retries with idempotency or replay defenses for write calls.

## Session And Token Hygiene

- Bind every credential to the narrowest practical audience, tenant, and scope.
- Keep access tokens or sessions short-lived enough that revocation is meaningful.
- Separate access credentials from renewal credentials when refresh is required.
- Rotate signing keys or shared secrets on a defined cadence and after suspected compromise.
- Log credential identifiers or key fingerprints, not raw secrets or token values.

## Minimal Auth Flow

```text
authenticate caller
-> bind stable subject identifier
-> bind tenant or account context
-> bind scope or role claims
-> evaluate authorization for the requested resource and action
-> issue only the response fields the subject may see
```

## Common Failure Modes

- Authentication is present, but authorization is left to client hints or hidden UI states.
- Tokens carry too much data or broad scopes that outlive the intended session.
- API keys are shared across environments or multiple integrations.
- Browser flows omit CSRF protection or rely on unsafe storage for long-lived credentials.
- mTLS is added without automated certificate rotation and expiry monitoring.

## What This Reference Does Not Cover

- Threat-model method or structured security review: use `$security-threat-model`.
- Endpoint contract design: use `$tool-design`.
- Verification commands and test coverage: use `$testing-and-evals`.
