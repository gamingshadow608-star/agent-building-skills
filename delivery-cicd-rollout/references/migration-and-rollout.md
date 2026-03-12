# Migration And Rollout

Use this file when the release touches persistent state or requires controlled rollout.

## Migration Plan Shape

Require the migration plan to state:

- target revision and target environment
- preconditions and required backups or snapshots
- execution order
- expected impact on availability, latency, or data correctness
- failure handling
- rollback or restore path
- rollback verification steps

## Migration Expectations

- Rehearse migrations in staging or an equivalent pre-production environment before production rollout.
- Require idempotency when reruns are possible.
- Require reversibility when rollback is expected.
- If a migration cannot be reversed safely, require an explicit restore strategy and a clear stop condition before rollout.
- Do not rely on undocumented manual operator knowledge for critical migration steps.

## Rollout Pattern Selection

Choose a controlled rollout pattern that fits the stack and blast radius:

- staged rollout
- canary deployment
- feature flags
- blue-green or equivalent controlled cutover

Prefer the pattern that gives the fastest safe rollback without assuming fix-forward under pressure.

## Monitoring Signals

Define what will be watched during rollout:

- service availability
- error rate
- latency
- saturation or queue backlog where relevant
- user-impact indicators
- migration side effects such as replication lag, lock time, or data drift where relevant

## Stop Conditions And Rollback Criteria

- Define stop conditions before deployment starts.
- Define rollback triggers before deployment starts.
- Define the fastest safe revert path, including how to disable the rollout or restore prior state.
- Define how rollback success will be verified, not just how rollback starts.

## Anti-Patterns

- releasing schema changes without staged rehearsal
- relying on one-way migrations without a restore strategy
- starting rollout without monitoring signals
- promising fix-forward without a tested rollback path
