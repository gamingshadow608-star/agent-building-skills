# Validation And Data Handling

When to read this: Read this for any user-controlled request data, uploaded content, callback URL, third-party payload, response shaping rule, or error contract.

## Validate Every Input Class

Apply explicit validation to:

- path parameters
- query parameters
- headers and cookies
- JSON or form bodies
- uploaded files and filenames
- URLs, domains, and callback targets
- webhook bodies and signatures

## Schema-First Rules

- Parse into a strict schema before business logic.
- Reject unknown fields by default unless the contract explicitly allows extension fields.
- Normalize types once, then use the normalized representation throughout the request.
- Enforce size, length, charset, and structural limits before expensive work.

## Content-Type And Decoding Discipline

- Accept only the content types the endpoint explicitly supports.
- Fail closed on malformed encodings, duplicate keys, or ambiguous parsing cases.
- Do not silently coerce structured types when coercion can hide invalid input.
- Apply file-size and body-size limits before full buffering when possible.

## Mass Assignment And Deserialization

- Map request fields into explicit server-side fields instead of spreading raw objects into models.
- Maintain allowlists for writable fields.
- Treat nested objects and relation IDs as separate authorization decisions.
- Reject polymorphic or executable payload features unless the contract truly requires them.

## URL And Outbound Fetch Safety

- Treat client-supplied URLs as untrusted even when they look internal.
- Validate allowed schemes, hosts, ports, and redirect behavior before any outbound fetch.
- Strip credentials and fragments unless the contract explicitly needs them.
- Pair URL acceptance with SSRF controls and timeouts.

## File Upload Controls

- Validate declared type, detected type, extension, and size independently.
- Rename files on receipt; do not trust user-supplied filenames for storage paths.
- Store uploads outside executable or public-static paths unless publication is the purpose.
- Scan or quarantine uploads when the system later processes them.

## Response Shaping

- Return only fields the caller needs for the current action.
- Apply authorization after expansions, joins, or nested object loads.
- Use stable error codes and short user-facing messages.
- Keep internal IDs, stack traces, SQL errors, secret names, and infrastructure details out of error bodies.

Use `assets/templates/error-response-contract.json` as the default public error envelope.

## Minimal Validation Pattern

```text
verify content type
-> parse into strict schema
-> reject unknown or oversized fields
-> validate URLs, files, and nested objects explicitly
-> authorize writable targets
-> execute business logic
-> shape response to the allowed field set
```

## Common Failure Modes

- Hidden fields become writable because raw payloads are mapped straight into models.
- File uploads validate extension only and ignore actual content type or storage path safety.
- Callback URLs are accepted without scheme or host restrictions.
- Error bodies leak implementation details that help enumeration or exploitation.
