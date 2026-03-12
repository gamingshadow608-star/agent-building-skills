# Protocol Hardening

When to read this: Read this after triage whenever the API uses REST, GraphQL, WebSocket, or webhook receivers and needs protocol-specific safeguards.

## REST

- Enforce allowed methods and reject unexpected verbs.
- Align idempotent methods and cache headers with actual side effects.
- Validate content type and accept headers before parsing.
- Constrain CORS to the origins, methods, and headers the browser contract actually needs.
- Apply authorization and response shaping to list endpoints, nested resources, and expansions, not just top-level routes.

## GraphQL

- Apply authorization at the field and resolver level, not just at the transport entry point.
- Enforce depth, complexity, or cost limits before executing expensive selections.
- Prefer persisted queries or operation allowlists for higher-risk public graphs.
- Decide introspection policy explicitly by environment and exposure level.
- Validate variables and input objects with the same strictness as REST bodies.

## WebSocket

- Authenticate at connection establishment and re-check authorization for channel joins and message types.
- Treat every inbound message as untrusted input with its own schema validation.
- Rate-limit messages per connection and per subject.
- Define session expiry or revocation behavior for long-lived connections.
- Do not trust client claims about room membership, tenant context, or message fan-out scope.

## Webhook Receivers

- Verify signatures against the exact raw request body before parsing business fields.
- Enforce timestamp tolerance and reject stale deliveries.
- Store replay identifiers or delivery IDs for the replay window.
- Return success only after signature, freshness, and minimal schema checks pass.
- Keep a clear separation between acknowledgement logic and downstream processing so retries are safe.

## Cross-Protocol Reminders

- Apply request IDs and stable error codes without leaking internals.
- Keep payload size and execution limits bounded.
- Treat retries and duplicate delivery as normal behavior to design for.
- Hand off interface-contract design to `$tool-design` when the shape of the surface itself is changing.
