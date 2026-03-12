## Architecture Brief

### Goals and non-goals

- Goals:
- Non-goals:

### Components and boundaries

- Orchestrator:
- Tool layer:
- Data stores:
- External services:
- Trust boundaries:

### Orchestration and control flow

- Main happy path:
- Retries:
- Timeouts:
- Human approvals:
- Failure paths:

### State and memory decision

- Memory used: `Yes` / `No`
- Type:
- Scope:
- Shared or isolated state:
- Write path:
- Provenance:
- Quarantine status:
- Promotion or review rule:
- Trust model:
- Retention window:
- Deletion and forget path:

### Synchronous versus asynchronous work

- Runs inline:
- Runs in background jobs:

### Orchestration graph notes

- Graph or workflow name:
- Nodes or steps:
- State transitions:
- Determinism and idempotency:
- Side effects and isolation:
- Recovery and resume behavior:

### Tool and boundary rationale

- Tools and why they are invoked:
- Untrusted inputs:
- Privileged actions:
- Approval points:
- Instruction versus data separation:
