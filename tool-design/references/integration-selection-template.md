# Integration Selection Template

Use this template before defining the tool surface.

## Task summary

- User task:
- Why a tool is needed:
- Local-only or remote requirement:

## Integration decision

- Chosen option: `local library` / `CLI` / `MCP STDIO` / `MCP HTTP`
- Why this option is the safest viable choice:
- Why the rejected options are worse for this task:

## Why MCP?

Fill this only when MCP is proposed.

- Boundary MCP is crossing:
- Why a local library or CLI is insufficient:
- Server type: `local-only` / `remote`
- Shared host or cross-process requirement:

## When MCP is the wrong choice

Check each condition:

- [ ] The task is simple and local.
- [ ] MCP would add protocol surface area without a real boundary benefit.
- [ ] MCP would add avoidable auth or governance complexity.
- [ ] The same outcome is available through a narrow local integration.

If any checked item makes MCP unnecessary, reject MCP and choose a local option.

## Content trust and exposure

- Untrusted or user-controlled content in scope:
- Can the exposed content be narrowed to task-shaped tools only? `yes` / `no`
- Can instruction/data separation be preserved? `yes` / `no`
- If `no`, reject the MCP design or redesign the tool boundary:

## Network decision

- Default network state: `off`
- Does this design require network? `yes` / `no`
- If yes, justification:
