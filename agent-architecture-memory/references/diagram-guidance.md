# Diagram Guidance

Use this reference only when deciding which diagrams to produce or what each diagram must show.

## System Overview

Require when the work changes major components or boundaries.

Minimum content:

- Orchestrator
- Tool layer
- Data stores
- External services
- Major trust boundaries

## Sequence Diagram

Require when control flow, approvals, retries, or side effects matter.

Minimum content:

- Main request path
- Tool calls
- Approval points
- Retry or timeout branches
- Response or failure end state

## State Or Lifecycle Diagram

Require when the agent has resumability, durable execution, interrupts, retries, or phase changes.

Minimum content:

- States
- Transitions
- Retry or interrupt paths
- Terminal success and failure states

## Data-Flow And Trust-Boundary Diagram

Require when the work handles untrusted inputs, retrieved content, secrets, or external writes.

Minimum content:

- Trusted and untrusted sources
- Data movement between components
- Secret or sensitive-data paths
- Boundaries where data changes trust level

## Tool Topology Diagram

Require when the work adds or changes tools, MCP surfaces, or external capabilities.

Minimum content:

- Tool host or orchestrator
- Tool categories or nodes
- Read-only versus side-effecting tools
- External systems each tool can touch
