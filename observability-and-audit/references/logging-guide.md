# Logging Guide

Use this file when defining or reviewing structured application logs.

## Required Fields

Require these fields on every operational log event unless a field is genuinely unavailable:

- `timestamp`
- `severity`
- `service.name` or equivalent stable service identifier
- `component`
- `environment`
- `event.name`
- `correlation_id` for the request, job, or workflow
- `trace_id` and `span_id` when tracing is enabled
- `status`

Add these fields when relevant:

- `user.id` or a pseudonymous actor identifier
- `tool.name`
- `operation.name`
- `input_summary`
- `output_summary`
- `latency_ms`
- `retry_count`
- `approval_result`
- `error.type`
- `error.code`

## Naming Guidance

- Prefer stable machine-readable field names over prose.
- Prefer OpenTelemetry semantic conventions when they fit the system.
- Keep field names consistent across services so dashboards and queries remain portable.
- Use summaries for inputs and outputs. Do not mix raw payloads and summaries under the same field name.

## JSON Example

```json
{
  "timestamp": "2026-03-09T10:15:22.184Z",
  "severity": "INFO",
  "service.name": "agent-api",
  "component": "tool-runner",
  "environment": "prod",
  "event.name": "tool_call.completed",
  "correlation_id": "wf_01HQ2GQYQ5Q8P3",
  "trace_id": "4f6d0d9dc2bb4df887c57f0bca8d9a3c",
  "span_id": "8a5f17f3c13d5e0c",
  "tool.name": "crm_lookup",
  "operation.name": "fetch_customer_summary",
  "input_summary": "customer_id present; 2 safe filter fields",
  "output_summary": "customer summary returned; 4 fields",
  "status": "success",
  "latency_ms": 184,
  "retry_count": 0
}
```

## Key-Value Example

```text
timestamp=2026-03-09T10:15:22.184Z severity=INFO service.name=agent-api component=tool-runner environment=prod event.name=tool_call.completed correlation_id=wf_01HQ2GQYQ5Q8P3 trace_id=4f6d0d9dc2bb4df887c57f0bca8d9a3c span_id=8a5f17f3c13d5e0c tool.name=crm_lookup operation.name=fetch_customer_summary status=success latency_ms=184 retry_count=0 input_summary="customer_id present; 2 safe filter fields" output_summary="customer summary returned; 4 fields"
```

## Redaction Rules

- Redact or drop secrets, credentials, tokens, session values, connection strings, signing keys, and raw personal data before emission.
- Never log hidden reasoning, chain-of-thought, raw prompts, raw completions, private documents, or full retrieved chunks.
- Prefer pseudonymous identifiers over email addresses, phone numbers, or legal names.
- Log that a redaction occurred when it helps explain missing detail, but do not log the removed value.

## Anti-Patterns

- Free-form prose as the primary format
- Dumping request or response bodies by default
- Logging trace IDs in metrics labels
- Using user-controlled strings as field names
- Creating different field names for the same concept in different components
