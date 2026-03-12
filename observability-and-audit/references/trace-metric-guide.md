# Trace And Metric Guide

Use this file when instrumenting traces or defining service metrics.

## Span Boundaries

Create spans around boundaries that operators need to debug:

- top-level request, workflow, or job execution
- orchestrator or planner steps
- tool calls and external requests
- queue publish and queue consume points
- retries and approval gates
- state transitions and persistence writes

Prefer child spans for meaningful sub-steps instead of one opaque top-level span.

## Context Propagation

- Propagate trace context across HTTP calls, background workers, queues, schedulers, tool invocations, and service-to-service hops.
- Preserve the same trace ID across the logical workflow whenever the transport supports it.
- When a boundary cannot carry native trace context, record and forward a stable correlation ID explicitly.
- Mirror correlation identifiers into audit events and operational logs.

## Sampling

- Choose a baseline sampling policy explicitly instead of accepting tool defaults without review.
- Lower steady-state sampling when cost or storage requires it.
- Increase or force sampling for errors, retries, approval flows, security events, and incident-response paths when feasible.
- Record the sampling decision in code comments, config, or operational docs so operators know what is intentionally missing.

## Core Metrics

Require a minimum metric set for operational paths:

- request or job latency
- throughput or completed work count
- error count and error rate
- timeout count
- retry count and retry exhaustion count
- approval requested, approved, and denied counts
- security-violation or policy-block count

Break metrics out by stable dimensions such as service, endpoint, workflow, tool, or job type.

## Cardinality Rules

- Use bounded labels only.
- Do not use trace IDs, span IDs, user IDs, email addresses, document IDs, or prompt text as labels.
- Prefer aggregate dimensions that support dashboards and alerting without exploding storage cost.
- When per-execution detail is needed, use logs, traces, or audit events instead of high-cardinality metrics.

## Anti-Patterns

- One span for an entire multi-step workflow
- Missing spans on tool calls or external requests
- Broken trace context at queue or worker boundaries
- Metrics that cannot distinguish success, retry, timeout, and failure
- High-cardinality labels that make metrics unusable
