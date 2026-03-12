# Provenance And Trust Model

Use this file when defining which RAG or memory data can be used and under what trust conditions.

## Required Provenance Fields

Require these fields for every stored or retrieved chunk:

- `source`
- `author`
- `timestamp`
- `checksum`
- `trust_level`

Require these additional fields for memory writes when the repo uses durable or shared memory:

- `write_reason`
- `review_status`

Use [../assets/templates/provenance-record.md](../assets/templates/provenance-record.md) when the repo does not already define a format.

## Trust Levels

- `untrusted`: default state for newly ingested or retrieved content. It can inform analysis but must not steer privileged actions.
- `quarantined`: stored for review but not approved for future reasoning or action.
- `trusted_for_scope`: reviewed and approved only for the stated scope and retention window.

## Missing Or Partial Provenance

- Do not use the data for privileged reasoning or action.
- Quarantine the entry and record the gap.
- Record which store, pipeline, or memory surface produced the incomplete record.
- Require the missing provenance or delete the unsafe data before promotion.

## Trust Model Checklist

Document all three of these:

- Untrusted inputs: retrieved chunks, uploads, logs, tool outputs, cached data, or imported memory.
- Privileged actions: writes, deletes, exports, network egress, memory promotion, or sensitive reads.
- Guards: instruction-data separation, quoting, redaction, approvals, access control, and quarantine review.
