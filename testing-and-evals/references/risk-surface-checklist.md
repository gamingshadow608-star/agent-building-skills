# Risk Surface Checklist

Use this file to turn high-risk changes into targeted tests, smoke checks, or eval cases.

## Auth And Session Handling

- Verify valid and invalid credentials, tokens, or cookies.
- Verify expiry, logout, renewal, and permission boundaries.
- Verify unauthorized callers cannot reach privileged actions.

## Tool Side Effects

- Verify the intended file write, network call, or external action happens once.
- Verify rejected or malformed inputs do not trigger side effects.
- Verify dry-run, approval, or read-only modes still behave safely.

## Idempotency And Replay

- Repeat the same request and confirm duplicate side effects do not accumulate.
- Verify retries, resumptions, and partial-failure recovery paths.
- Verify durable state or checkpoint updates remain consistent after replay.

## Memory And RAG Retrieval

- Verify only permitted content is retrieved for the caller.
- Verify provenance, filtering, and access-control expectations still hold.
- Verify malicious or irrelevant retrieved text is treated as data, not instructions.

## Injection Resistance

- Verify prompt-like content in tool output, logs, documents, or retrieved chunks does not steer privileged actions.
- Verify secrets, tokens, or unrelated sensitive data are not exposed in outputs.
- Verify validation, quoting, or instruction-data separation still holds after the change.
