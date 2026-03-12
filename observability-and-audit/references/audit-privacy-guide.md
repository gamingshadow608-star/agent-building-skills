# Audit And Privacy Guide

Use this file when defining audit records, retention, and privacy controls.

## Minimum Audit Event Schema

Record these fields for each audit event:

- `timestamp`
- `actor.id` or system identity
- `actor.type`
- `action`
- `target.resource`
- `target.type`
- `outcome`
- `approval_result` when applicable
- `source.component`
- `correlation_id`
- `trace_id` when tracing is enabled
- `decision_summary`

Keep `decision_summary` concise and explainable. Do not store hidden reasoning, chain-of-thought, raw prompts, raw tool payloads, or sensitive documents.

## Storage And Immutability

- Store audit records separately from application logs.
- Keep the audit store append-only or otherwise tamper-evident.
- Do not rely on ordinary log rotation as the only retention mechanism for audit data.
- Apply stricter access controls to audit data than to routine operational logs.

## Retention And Deletion

- Define retention windows separately for logs, traces, metrics, and audit records.
- Record who owns each retention decision and why it satisfies policy or legal obligations.
- Define a deletion or purge path for data that must expire, be forgotten, or be removed under policy.
- Preserve audit integrity while handling lawful deletion requirements. Do not silently delete records without a defined policy path.

## Privacy Rules

- Minimize collected data to what is needed for accountability and incident reconstruction.
- Prefer internal or pseudonymous identifiers when full personal identity is not required.
- Re-review audit fields whenever prompts, tools, schemas, memory stores, or external integrations change.
- Treat audit exports and ad hoc analyst queries as privacy-sensitive surfaces too.

## Anti-Patterns

- Storing audit events only in the same sink as application logs
- Allowing routine edits or deletes of historical audit records
- Recording raw prompts, raw completions, or full tool inputs by default
- Exposing audit stores to broad read access
- Omitting correlation identifiers that would allow event reconstruction
