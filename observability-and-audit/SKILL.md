---
name: observability-and-audit
description: Require observability and auditability for services, agent systems, tools, and automations that run beyond a one-off local script. Use when a project is deployed as a service, interacts with external systems or tools, runs scheduled or background work, or needs tracing, debugging, incident analysis, or auditable execution; enforce structured logging, tracing, metrics, privacy-aware retention, and separate immutable audit trails.
---

# Observability And Audit

Treat observability as required engineering infrastructure for debugging, incident response, and auditability. Keep the implementation stack-agnostic, correlate logs, traces, metrics, and audit records, and prefer open standards such as OpenTelemetry where practical.

Use progressive disclosure. Read only the support file that matches the current need:

- `references/logging-guide.md`
- `references/trace-metric-guide.md`
- `references/audit-privacy-guide.md`
- `assets/templates/what-was-logged.md`

## Workflow

1. Classify the observability need.
   - Identify whether the work covers a service, orchestrator, tool integration, background job, incident path, or audit-sensitive state change.
   - Identify the operational boundary to follow end to end, such as a request, workflow, job, tool call, or approval path.
2. Define one correlation strategy before instrumenting.
   - Choose the request, job, or workflow identifier plus trace and span identifiers.
   - Use the same correlation identifiers across logs, traces, and audit records so one action can be reconstructed consistently.
   - Do not place per-request identifiers such as trace IDs in metric labels. Use stable operational dimensions for metrics instead.
3. Instrument the four required signal types.
   - Add structured logs for state changes, tool calls, retries, approvals, and failures.
   - Add trace spans around orchestrators, tool invocations, critical functions, background jobs, queue boundaries, and external requests.
   - Add metrics for latency, error, retry, approval, and security-relevant events with bounded cardinality.
   - Add a separate audit trail for tool calls, model decision summaries, approval decisions, and accountability-relevant state changes.
4. Apply privacy, sampling, and retention controls explicitly.
   - Redact secrets, credentials, tokens, personal data, private documents, and other sensitive payloads before emission.
   - Record sampling decisions for traces and retention decisions for logs, traces, metrics, and audit records.
   - Prohibit logging hidden reasoning, chain-of-thought, raw prompts, raw completions, or other sensitive internals.
5. Report what was logged and what is still missing.
   - Summarize trace IDs, correlation IDs, log sinks, metrics, audit stores, anomalies, and missing telemetry in the final report.
   - Use `assets/templates/what-was-logged.md` when the repo does not already define a better final-report format.

## Structured Logging

- Emit structured logs in JSON or stable key-value form. Do not rely on free-form text as the primary log format.
- Include timestamps, severity, service or component name, environment, and the chosen request, job, or workflow identifier on every event.
- Include trace IDs and span IDs whenever tracing is enabled so logs can be correlated with spans.
- Record tool names, operation names, concise input and output summaries, outcome fields, latency, retry count, approval result, and error category for tool calls and state-changing actions.
- Summarize payloads instead of dumping raw inputs. Never log secrets, credentials, session data, raw prompts, raw model outputs, hidden reasoning, or personal data.
- Use `references/logging-guide.md` for field requirements, examples, and OpenTelemetry-aligned naming guidance.

## Tracing And Metrics

- Instrument orchestrators, tool calls, critical functions, async boundaries, service-to-service hops, retries, and background jobs with trace spans.
- Propagate trace context across HTTP calls, queues, task runners, tool invocations, and worker boundaries so one action can be reconstructed end to end.
- Choose trace sampling explicitly. Increase or force sampling for errors, approvals, retries, incidents, and security-relevant paths when feasible.
- Collect metrics for latency, throughput, timeout rate, error rate, retry rate, approval volume, approval denial rate, and security-violation counts.
- Prefer counters, gauges, and histograms with bounded label cardinality so telemetry remains queryable and sustainable.
- Use `references/trace-metric-guide.md` for span boundaries, propagation rules, sampling, metric sets, and label-cardinality guidance.

## Audit Logs

- Maintain a separate audit trail for tool calls, approval decisions, model decision summaries, and accountability-relevant state changes.
- Keep audit logs immutable or append-only and store them separately from application logs.
- Protect audit logs with stricter access controls than ordinary debugging logs.
- Record at least the actor or system identity, action, target resource, outcome, approval decision, source component, timestamp, and correlation identifiers needed to reconstruct the event.
- Record concise decision summaries rather than hidden reasoning, raw prompt internals, or sensitive payloads.
- Use `references/audit-privacy-guide.md` for the minimum audit schema, retention, deletion, access control, and privacy guidance.

## Privacy And Compliance

- Minimize collected data. Log only what is needed to debug, operate, and audit the system.
- Define retention windows for application logs, traces, metrics, and audit records separately when their compliance requirements differ.
- Define deletion, forgetting, or purge procedures for data that must expire or be removed under policy or legal obligations.
- Re-check observability outputs whenever schemas, prompts, tools, memory stores, or external integrations change, because new fields often create privacy leaks.

## Final Report

- Include a `What was logged` summary in the final report.
- List the relevant trace IDs, correlation IDs, and audit identifiers created or used during the task.
- List the log files, sinks, or stores that captured application logs, traces, metrics, and audit logs.
- List the metrics collected or added, especially latency, error, retry, approval, and security-event metrics.
- Call out anomalies, missing telemetry, redaction failures, suspicious events, and security-relevant observations explicitly.

## Boundaries

- Do not define test procedures or test execution requirements.
- Do not define security review procedures or replace the security skill.
- Do not design CI/CD workflows, deployment pipelines, or rollout processes here.
- Do not assume a specific logging, tracing, metrics, or audit vendor stack.
- Do focus on structured logging, tracing, metrics, auditability, privacy, retention, and final telemetry reporting.
