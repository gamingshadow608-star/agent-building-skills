# Task Contract Template

Use this template for every tool. Keep the contract task-shaped and specific to the user job.

## Contract summary

- Tool name:
- Purpose:
- Caller intent:
- Preconditions:

## Inputs and outputs

| Field | Description |
| --- | --- |
| Inputs | |
| Outputs | |
| Allowed side effects | |
| Forbidden side effects | |

## Parameter boundaries

| Parameter | `Data allowed` | `Data forbidden` | Validation rules |
| --- | --- | --- | --- |
|  |  |  |  |

## Error contract

- Recovery-friendly error fields:
- Ambiguous request handling:
- Over-broad request handling:

## Approval and annotation

- Annotations: `read-only` / `destructive` / `privileged`
- Approval rule:
- Sensitive reads:
- Network use:
- Credential use:

## Naming check

- Task-shaped name:
- Raw API mirror rejected? `yes` / `no`
- If no, documented reason:

## Naming examples

- Prefer `search_documents` instead of `GET /docs`
- Prefer `fetch_customer_invoice` instead of `GET /customers/{id}`
- Prefer `create_support_ticket` instead of a generic admin wrapper
