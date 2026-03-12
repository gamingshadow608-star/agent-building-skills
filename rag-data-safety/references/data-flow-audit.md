# Data-Flow Audit

Use this file to review how untrusted or sensitive data moves through the system.

## Audit Surfaces

Check each of these when they exist:

- Ingestion
- Storage
- Embedding generation
- Retrieval
- Transformation or summarization
- Display or preview
- Export or external delivery
- Logs, traces, and debugging output
- Derived caches, indexes, or snapshots

## Trust-Boundary Questions

- Which inputs are untrusted at each stage?
- Which step can read, write, delete, or export the data?
- Where is untrusted text quoted or otherwise marked as data?
- Where are PII, secrets, or credentials redacted?
- Where can sensitive data leave the trust boundary, and what approval is required?

## Required Outcomes

- Confirm that retrieved or stored text cannot override policy or steer privileged actions.
- Confirm that redaction, provenance, quarantine, and deletion rules apply across the full flow.
- Flag any path where sensitive data can bypass approval, redaction, or access control.
- Record every unresolved egress path as a data-safety gap.
