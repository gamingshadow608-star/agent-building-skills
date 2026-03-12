# Test Selection

Use this file after the repo scan chooses the stack and likely entrypoints.

## Command Discovery Order

Prefer commands in this order:

1. Repo runbooks and docs such as `AGENTS.md`, `README`, `CONTRIBUTING`, or test notes.
2. Repo-native task runners and scripts such as `Makefile`, `justfile`, `tox`, `nox`, `package.json`, `pyproject.toml`, or solution-level test commands.
3. Commands already used by CI for the same checks.
4. Generic stack examples only when the repo does not define a better command path.

Record the chosen commands and why they fit the changed behavior.

## Check Types

- Unit tests: pure functions, transforms, validators, parsers, and business rules.
- Integration tests: tool interactions, side effects, auth/session flows, retries, network boundaries, and multi-step orchestration.
- Smoke or startup checks: real runnable entrypoints such as web servers, CLIs, workers, schedulers, or jobs.
- Evals: prompt, skill, orchestration, retrieval, or tool-selection behavior that depends on model trajectories.
- Static checks: lint, type checks, or compile checks when the repo already treats them as required quality gates.

## Stack Examples

Use these only as fallback examples when the repo does not already define better commands.

### Python

- `python -m pytest -q`
- `python -m ruff check .`
- `python -m mypy .`
- `python -c "import app; print('import ok')"`

### Node And TypeScript

- `npm test`
- `pnpm test`
- `npm run lint`
- `npm run typecheck`
- `npm run start -- --help`

### .NET

- `dotnet test`
- `dotnet build`
- `dotnet run -- --help`
