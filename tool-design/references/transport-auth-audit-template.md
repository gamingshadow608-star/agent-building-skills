# Transport, Auth, And Audit Template

Use this template after the task contract is defined.

## Transport choice

- Chosen transport: `local library` / `CLI` / `MCP STDIO` / `MCP HTTP with bearer token` / `MCP HTTP with OAuth`
- Why this transport fits the boundary:
- Why a simpler transport was insufficient:

## Remote auth decision

Fill this for remote MCP.

- Remote access required because:
- Auth choice: `bearer token` / `OAuth`
- Why this auth choice is appropriate:
- Credential scope:
- Token lifetime:
- Refresh method:
- Network justification:

## Approval model

- Default network state: `off`
- Approval required for network use: `yes` / `no`
- Approval required for sensitive reads: `yes` / `no`
- Approval required for destructive actions: `yes` / `no`
- Approval required for credential use: `yes` / `no`

## Audit log contract

| Field | Required value |
| --- | --- |
| Tool name | |
| Tool purpose | |
| Inputs | |
| Outputs | |
| Timestamp | |
| Request, job, or tool-call identifier | |
| Transport | |
| Auth mode | |
| Annotations | |
| Approval decision | |

## Final report tool inventory

| Tool | Purpose | Transport | Auth mode | Annotations | Approval rule | Audit identifiers |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |
