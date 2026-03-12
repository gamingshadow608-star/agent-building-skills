# Repo Scan Signals

Use this reference only when it is unclear which specialist skills should activate or what evidence to record.

## Record Format

For each activated skill, record:

- Skill name
- Repo evidence such as path, package name, config file, or command
- Why the evidence makes the skill relevant

## Common Activation Signals

Activate `agent-architecture-memory` when the repo shows:

- `langgraph`, `langchain`, multi-agent orchestration, planners, graphs, or workflow engines
- Stateful agents, checkpoints, memory, or durable execution
- Non-trivial agent boundaries that need diagrams or explicit state handling

Activate `testing-and-evals` when the work changes:

- Code, prompts, orchestration, or model behavior
- Test suites, eval harnesses, runnable services, CLIs, or workers

Activate `security-threat-model` when the repo shows:

- Auth, secrets, privileged actions, external inputs, network access, filesystem writes, or admin flows
- Tool use that could cross trust boundaries

Activate `tool-design` when the repo shows:

- MCP servers, tool registries, agent-callable HTTP endpoints, CLIs, or external capability wrappers

Activate `rag-data-safety` when the repo shows:

- `pgvector`, vector stores, embeddings, retrievers, document ingestion, search pipelines, or long-term memory stores

Activate `observability-and-audit` when the repo shows:

- Deployed services, jobs, tracing, structured logging, audit trails, or operational debugging requirements

Activate `delivery-cicd-rollout` when the repo shows:

- CI workflows, Docker, Kubernetes, Terraform, migrations, release automation, or production rollout steps

## Evidence Standard

- Prefer deterministic evidence over guesses
- Use repo paths or config terms instead of vague summaries
- Leave a skill inactive when evidence is absent or weak
