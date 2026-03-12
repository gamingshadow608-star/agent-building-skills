# Memory Decision Checklist

Use this reference only when the memory decision, trust model, or retention plan needs a compact checklist.

## Required Decision

- [ ] State whether memory is `Yes` or `No`
- [ ] Explain why that choice fits the system
- [ ] State where transient execution state lives even when durable memory is `No`

## Storage And Scope

- [ ] Type: ephemeral, durable, vector, key-value, SQL, or equivalent
- [ ] Scope: per user, per org, per thread, global, or equivalent
- [ ] Shared or isolated state: who can read it and what separation rule applies

## Write Path And Provenance

- [ ] What writes memory
- [ ] Under what conditions writes are allowed
- [ ] Provenance fields: who, why, source, timestamp
- [ ] What review or promotion step occurs before normal retrieval

## Trust And Quarantine

- [ ] What content is untrusted
- [ ] How new writes are quarantined
- [ ] How untrusted or retrieved content is filtered, quoted, or separated from instructions

## Lifecycle

- [ ] Retention window
- [ ] Deletion or forget path
- [ ] Recovery behavior for replay, retry, or resume
