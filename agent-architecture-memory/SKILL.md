---
name: agent-architecture-memory
description: Design or modify orchestrators, agent graphs, tool surfaces, workflows, state, retrieval, durable execution, or memory for non-trivial agentic systems. Use when architecture, trust boundaries, approvals, side effects, persistent context, or external-write flows change; require explicit architecture briefs, diagrams, and memory decisions before coding. Do not trigger for simple non-agentic bugfixes or one-off local edits unless they change orchestration, tools, state, or memory.
---

# Agent Architecture Memory

Design robust agent architecture before implementation. Require explicit decisions for orchestration, tools, state, memory, trust boundaries, and failure handling. Treat this skill as essential for any non-trivial agentic system.

## Required Outputs Before Coding

Produce these outputs before writing code or changing the orchestration:

- An architecture brief. Reuse [assets/architecture-brief-template.md](assets/architecture-brief-template.md) when the repo does not already define a format.
- The applicable Mermaid diagrams. Reuse [assets/mermaid-starter-snippets.md](assets/mermaid-starter-snippets.md) and read [references/diagram-guidance.md](references/diagram-guidance.md) only when you need diagram-specific guidance.
- An explicit state and memory decision. Read [references/memory-decision-checklist.md](references/memory-decision-checklist.md) only when the memory choice or trust model is unclear.
- Orchestration graph notes covering nodes, transitions, side effects, and recovery behavior.
- Tool and boundary rationale covering untrusted inputs, privileged actions, approvals, and trust-boundary handling.

## Architecture Brief

Produce an architecture brief before writing code. Include all of these sections:

- `Goals and non-goals`
- `Components and boundaries`
- `Orchestration and control flow`
- `State and memory decision`
- `Synchronous versus asynchronous work`

Fill the brief with required fields:

- `Components and boundaries`
  - Orchestrator
  - Tool layer
  - Data stores
  - External services
- `Orchestration and control flow`
  - Main happy path
  - Retries
  - Timeouts
  - Human approvals
  - Failure paths
- `State and memory decision`
  - Memory used? `Yes` / `No`
  - If `Yes`: type, scope, shared or isolated state, write path, provenance, quarantine status, promotion or review rule, trust model, retention and deletion window, explicit forget path
- `Synchronous versus asynchronous work`
  - What runs inline
  - What runs in background jobs

State `No memory` explicitly when that is the decision and explain what transient execution state still exists.

## When Diagrams Are Mandatory

Produce the relevant Mermaid diagrams whenever the work introduces or changes:

- A new orchestration graph or workflow
- A new tool surface or external capability
- Persistent memory, retrieval, or durable state
- Writes to external systems, databases, or SaaS APIs
- A trust boundary, approval path, or side-effect path

Update existing repo diagrams when they already exist and are the source of truth; otherwise create new ones.

## Mermaid Diagrams

Produce the relevant subset of these diagrams whenever the work is agentic, changes trust boundaries, adds tools, or changes state or memory:

- `System overview` diagram
- `Sequence` diagram
- `State or lifecycle` diagram
- `Data-flow and trust-boundary` diagram
- `Tool topology` diagram

Use multiple diagrams when different concerns need separate views. Keep long examples out of this file and link to `references/` material instead.

## Memory Decisions

Make memory an explicit choice every time. Do not assume a default pattern.

- Choose `Yes` or `No`.
- If `Yes`, document:
  - Type: ephemeral, durable, vector store, key-value, SQL, or equivalent
  - Scope: per user, per org, per thread, global, or equivalent
  - Shared or isolated state: who can read the state and how separation is enforced
  - Write path: what writes memory, under what conditions, and after which approval or validation step
  - Provenance: who wrote it, why, source, timestamp
  - Quarantine status for new writes before they are trusted
  - Promotion or review rule for moving quarantined memory into normal retrieval
  - Trust model for untrusted content and retrieved text
  - Retention window
  - Deletion and forget path
- If `No`, state why durable memory is not needed and where transient state still lives during execution.
- Treat memory and retrieved content as trust-boundary decisions, not convenience features.

## Orchestration Requirements

Document how the orchestration works before implementation:

- Name the graph, workflow, or node structure.
- List nodes or steps and their responsibilities.
- Describe state transitions and lifecycle states.
- Mark what runs synchronously and what runs asynchronously.
- Explain determinism requirements.
- Explain idempotency requirements for replay, retries, and resume behavior.
- Identify side effects and how they are isolated, wrapped, or compensated.
- Describe resilience strategy: retries, fallbacks, interrupts, timeouts, error handling, and failure paths.
- Explain where approvals occur and what they block or allow.
- Record assumptions that affect correctness or recovery.

## Tool And Boundary Design

For each tool or external capability used in the orchestration, explain:

- Why the tool is invoked
- What boundary it crosses
- How approvals are handled
- What side effects are allowed
- What privileged actions it can trigger
- Which inputs are untrusted
- How untrusted data is separated from instructions
- How tool output and retrieved content are treated as data rather than control

Inventory untrusted inputs and privileged actions explicitly. If the work needs tool-schema or authorization detail, hand that off to `tool-design` instead of duplicating it here.

## Model-Specific Notes

If model-specific tool-calling or orchestration differences matter, capture them in [references/model-notes.md](references/model-notes.md).

- Use that file for GPT-5.x, Claude, and Gemini differences that affect planning, approvals, or orchestration shape.
- Keep this skill focused on the shared architecture workflow.

## Boundaries

- Do not define one default memory architecture.
- Do not include test commands.
- Do not include security review procedures.
- Do not duplicate detailed tool-schema or authorization design rules from other skills.
- Do require explicit architecture, memory, orchestration, side-effect, and trust-boundary decisions before coding.
