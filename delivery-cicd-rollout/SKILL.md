---
name: delivery-cicd-rollout
description: Enforce safe deployment and release discipline when a project is preparing to deploy, release a new version, run migrations, perform rollout steps, or otherwise change production-facing delivery state. Use to require prior gate completion, CI green status, migration planning, staged rollout, rollback readiness, release documentation, and secret-safe delivery practices.
---

# Delivery CICD Rollout

Treat delivery as a gated release discipline. Deploy only when the change is verified, reversible, documented, and adapted to the detected stack and release tooling rather than to a hard-coded platform recipe.

Use progressive disclosure. Read only the support file that matches the current delivery task:

- `references/release-gate-checklist.md`
- `references/migration-and-rollout.md`
- `references/secret-safe-delivery.md`
- `assets/templates/release-report.md`
- `assets/templates/release-notes.md`

## Workflow

1. Confirm release scope and prior gates.
   - Verify the exact target revision, environment, and rollout target before any release work starts.
   - Do not deploy, release, tag, or run migrations until the architecture, test, and security review gates are satisfied.
   - Record which prior gates were satisfied and what evidence proves readiness for the exact revision being released.
2. Prove CI is green for the target revision.
   - Derive repo-native CI commands, required checks, and workflow definitions from the repo before falling back to generic stack assumptions.
   - Require tests, lint, type checks, build steps, and other release-blocking checks that the repository treats as mandatory.
   - Require relevant CI workflows to pass for the target revision, not for an older or different commit.
3. Plan migrations only when persistent state changes exist.
   - Activate migration planning only for database, storage, index, queue, contract, or other persistent-state changes that require coordinated rollout.
   - Require a written migration plan, staging rehearsal or equivalent pre-production validation, and explicit idempotency and reversibility expectations.
4. Define rollout control before execution.
   - Choose a rollout strategy such as staged rollout, canary deployment, feature flags, or another controlled pattern that fits the detected stack and risk level.
   - Define monitoring signals, stop conditions, rollback triggers, and rollback verification steps before deployment starts.
5. Prepare release artifacts.
   - Update version numbers according to the repository's release scheme.
   - Create release tags when the workflow uses them.
   - Produce release notes and a final report that separate user-visible changes from operational and migration changes.
6. Verify secret-safe delivery before rollout.
   - Verify that production secrets and credentials are injected at runtime through environment variables, secret managers, or equivalent secure mechanisms.
   - Verify that the delivery pipeline, build logs, deployment logs, prompts, and release artifacts do not expose secrets.

## Blocked Release Path

- Block deployment or release when prior-gate evidence is missing, stale, or inconsistent with the target revision.
- Block deployment or release when CI is partial, stale, failing, or missing required workflows.
- Block deployment or release when migrations are unrehearsed, non-idempotent where reruns are possible, or lack a restore or rollback path.
- Block deployment or release when rollout stop conditions, rollback triggers, or rollback verification steps are undefined.
- Block deployment or release when secrets handling depends on committed credentials, unsafe pipeline output, or other insecure delivery practices.
- Record the exact blocker, the affected revision or environment, and what remains unsafe or unverified.

## CI Green

- Run the full repo-relevant CI suite before deployment or release.
- Prefer repo-native CI and deployment evidence over generic commands or assumptions.
- Include tests, lint, type checks, build steps, and other stack-appropriate verification that the repository treats as release-blocking.
- If the repo includes CI workflows such as GitHub Actions, GitLab CI, or equivalent pipeline definitions, ensure the relevant workflows run successfully for the target revision.
- Do not treat partially passing pipelines, skipped required checks, or stale results from an older commit as acceptable.
- Use `references/release-gate-checklist.md` for repo-scan signals, CI evidence, stale-check handling, and blocked-release reporting.

## Migration And Rollout

- Activate migration planning only when the change modifies persistent state that requires coordinated rollout.
- Require migration preconditions, execution order, expected impact, failure handling, idempotency expectations, and rollback or restore paths.
- Test migrations in staging or an equivalent pre-production environment before production rollout.
- Choose and document a rollout strategy that fits the detected stack and risk level.
- Define what will be monitored during rollout, including service health, error rates, latency, user impact, and migration side effects where relevant.
- Define explicit stop conditions, rollback triggers, and rollback verification steps before deployment starts.
- Prefer the fastest safe revert path over an optimistic fix-forward assumption when production impact is unclear.
- Use `references/migration-and-rollout.md` for migration-plan shape, rollout patterns, monitoring signals, and rollback criteria.

## Versioning And Release Notes

- Update version numbers according to the repository's release scheme before publishing a release.
- Create or update release tags when the workflow uses them.
- Produce release notes or changelog entries that summarize user-visible changes, operational changes, migration notes, CI results, and security findings relevant to the release.
- Keep release documentation consistent with the exact revision that was deployed.
- Use `assets/templates/release-notes.md` when the repo does not define a better release-notes format.

## Secrets And Credential Handling

- Verify that production secrets and credentials are injected at runtime through environment variables, secret managers, or equivalent secure delivery mechanisms.
- Do not commit secrets, credentials, tokens, or private keys to the repository, release artifacts, or changelog content.
- Do not echo secrets into CI logs, deployment logs, prompts, or final reports.
- Check that the delivery pipeline does not expose secret values through configuration, debug output, failed-step logs, or retained build artifacts.
- Stop and remediate before release if the deployment path requires unsafe secret handling.
- Use `references/secret-safe-delivery.md` for config hygiene, runtime injection rules, and pipeline anti-patterns.

## Final Report

- Include rollback notes in the final report.
- Describe how to undo the deployment, disable the rollout, or restore the previous version quickly.
- Describe how to restore prior state when migrations or persistent data changes were involved.
- Describe how to verify that rollback succeeded and the system returned to a healthy state.
- Record the released version, target revision, deployment target, rollout strategy used, CI evidence, and any residual delivery risks.
- Use `assets/templates/release-report.md` when the repo does not already define a better final-report format.

## Boundaries

- Do not design architecture details here.
- Do not design test strategy or replace the testing skill.
- Do not design tool interfaces or tool contracts here.
- Do not define memory models or memory decisions here.
- Do not assume a specific CI platform, cloud provider, deployment command, or release system.
- Do focus on safe release gates, CI readiness, migration safety, rollout control, rollback readiness, versioning, changelogs, and secret-safe delivery.
