# Release Gate Checklist

Use this file when confirming whether a revision is ready for release work.

## Gate Order

- Require architecture, testing, and security review gates to be complete before deployment or release work.
- Confirm the target revision, target environment, and rollout target before reading CI or release evidence.
- Treat deployment as blocked if the evidence does not map to the exact revision being released.

## Repo-Scan Signals

Look for repo-native release evidence before falling back to generic assumptions:

- CI workflow definitions such as GitHub Actions, GitLab CI, Azure Pipelines, CircleCI, or Buildkite
- repo task runners such as `Makefile`, `justfile`, `package.json`, `pyproject.toml`, `tox`, `nox`, or solution-level release scripts
- deployment manifests such as Helm charts, Kubernetes manifests, Terraform, Dockerfiles, or release directories
- migration signals such as `alembic/`, `migrations/`, `db/`, `schema/`, or storage-contract change directories

## CI Evidence Requirements

- Record the commands, workflow names, or pipeline identifiers used to verify readiness.
- Require all release-blocking checks to pass, including tests, lint, type checks, and build steps when the repo treats them as mandatory.
- Require success for the target revision. Do not accept results from a previous commit, branch, or unreproducible local state.
- Treat skipped required checks, manually ignored failures, or partial pipeline success as blocked release conditions.

## Stale Or Incomplete Evidence

- Treat evidence as stale when it references a different revision, predates relevant changes, or excludes required workflows.
- Treat evidence as incomplete when required environments, jobs, or approval steps were not executed.
- Record the missing or stale evidence explicitly rather than summarizing it as generic CI failure.

## Blocked Release Reporting

When release is blocked, record:

- target revision
- target environment
- missing or failing gate
- exact workflow, command, or artifact that failed or is missing
- what remains unsafe or unverified
