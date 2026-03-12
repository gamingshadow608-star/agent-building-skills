# Abuse Controls Matrix

| Endpoint class | Primary key | Baseline limit | Burst handling | Size or complexity cap | Idempotency or replay control | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Auth endpoints | account + IP | 5 attempts / 15 min | progressive delay | small body only | n/a | Monitor credential stuffing and password reset abuse |
| Uploads | subject + tenant | 20 uploads / hour | queue or reject | file count and total bytes capped | upload token or one-time URL | Validate detected type and storage path |
| GraphQL operations | subject + operation name | 60 ops / min | cost-based deny | depth and complexity capped | idempotency key for retried mutations | Prefer persisted queries for public graphs |
| WebSocket messages | connection + subject | 30 msgs / min | drop or disconnect | per-message size cap | message nonce for sensitive writes | Re-check channel authorization |
| Webhook receivers | provider + delivery id | provider-defined | reject stale retries | raw body size cap | signature + timestamp + replay store | Acknowledge only after minimum verification |
