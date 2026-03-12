# Secret-Safe Delivery

Use this file when verifying deployment pipelines, release artifacts, and runtime configuration.

## Runtime Injection Rules

- Inject production secrets and credentials at runtime through environment variables, secret managers, workload identity, or equivalent secure mechanisms.
- Keep secrets out of repository files, release notes, prompts, artifacts, and final reports.
- Prefer short-lived credentials and scoped access where the platform supports them.

## Pipeline And Config Checks

- Check CI configuration, deployment manifests, and runtime config for hard-coded credentials, private keys, tokens, or connection strings.
- Check build logs, failed job logs, debug output, and retained artifacts for secret exposure.
- Check release packaging steps so secrets are not baked into container images, archives, or generated config files.
- Check that secret names or references are acceptable to log, but secret values are never emitted.

## Environment Hygiene

- Keep environment-specific configuration separate from committed defaults when sensitive data is involved.
- Prefer secret references over copied values.
- Verify that rollback paths do not require unsafe manual secret handling under incident pressure.

## Anti-Patterns

- committing `.env` files with production values
- echoing secrets in CI or deployment scripts
- embedding credentials in Dockerfiles, manifests, or release artifacts
- pasting secret values into changelogs, incident notes, or prompts
