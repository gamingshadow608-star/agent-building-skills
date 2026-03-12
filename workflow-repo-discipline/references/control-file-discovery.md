# Control-File Discovery

Use this reference only when multiple `AGENTS` files exist, precedence is unclear, or the tracker location is ambiguous.

## Discovery Order

1. Start in the current working directory.
2. Walk upward toward the repo root.
3. In each directory, check `AGENTS.override.md` before `AGENTS.md`.
4. Treat the most specific applicable file as authoritative for the current subtree.
5. Inherit parent obligations unless a more specific file clearly overrides them.

Treat this skill as Codex-primary. Ignore non-`AGENTS` control files unless the authoritative runbook explicitly points to them.

## What To Resolve

Record:

- Which control files apply
- Which file is authoritative for gate order
- Which location is the live tracker
- Which required deliverables still apply from parent files

## Stop And Ask

Stop and ask instead of guessing when:

- Two applicable files conflict and precedence does not clearly resolve the conflict
- The runbook points to a tracker or phase log that does not exist
- The current subtree has no applicable runbook but parent instructions imply one should exist

## Keep Tracker Updates Concise

- Update an existing tracker block instead of appending long narrative logs
- Keep blocker, risk, and evidence entries short and specific
- Preserve prior decisions and evidence; replace stale status, not history
