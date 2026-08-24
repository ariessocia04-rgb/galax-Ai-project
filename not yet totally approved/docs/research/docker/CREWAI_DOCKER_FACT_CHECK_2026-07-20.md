# CrewAI + Docker Fact Check — 2026-07-20

**Status:** `RESEARCH_RECORD`  
**Decision:** A CrewAI application can run as a containerized Python service, and a Galax multi-service application can be orchestrated with Docker Compose. CrewAI does not provide a built-in secure Docker topology or a built-in production code sandbox.

## Fact 1 — CrewAI is the agent/Flow framework, not the container orchestrator

CrewAI provides agents, Crews, tasks, tools, and Flows. Docker or another deployment platform owns process isolation, networking, storage, secrets, and container lifecycle.

Sources:

- [CrewAI documentation](https://docs.crewai.com/)
- [CrewAI Flows and agents overview](https://docs.crewai.com/core-concepts/Agents)

## Fact 2 — Deterministic Flow control remains inside the application

CrewAI Flows provide structured execution paths and state. Galax may run that Python Flow inside a container, but Compose does not replace the Flow and the LLM must not control Compose service selection.

Sources:

- [CrewAI documentation](https://docs.crewai.com/)
- [CrewAI Flows](https://docs.crewai.com/en/concepts/flows)

## Fact 3 — There is no approved official CrewAI OSS turnkey secure Compose blueprint for Galax

CrewAI's documented managed production platform is CrewAI AMP. The open-source framework can be packaged like a normal Python application, but Galax must design, test, and own its Compose files and security controls.

Source:

- [CrewAI AMP](https://docs.crewai.com/enterprise/introduction)

## Fact 4 — Existing Dockerized agent examples do not automatically prove CrewAI compatibility

Cerebras publishes a Docker-based multi-agent development example that uses `gpt-oss-120b`, Docker MCP Gateway, Docker Compose, and sandbox containers. It is useful infrastructure evidence, but it is not a CrewAI implementation and cannot approve Galax's CrewAI integration.

Source:

- [Cerebras Docker integration](https://inference-docs.cerebras.ai/integrations/docker)

Community CrewAI Docker/Compose repositories can demonstrate that CrewAI Python applications have been containerized, but they are not authoritative production-security references.

## Fact 5 — CrewAI built-in code execution is not the selected sandbox

CrewAI 1.15.4 documents `allow_code_execution` and `code_execution_mode` as deprecated and states that `CodeInterpreterTool` was removed. Coding agents require a separately tested sandbox service through their single role-specific workspace tool.

Source:

- [CrewAI 1.15.4 agent documentation](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/agents.mdx)

## Fact 6 — Rootless Docker reduces daemon and runtime privileges

Docker rootless mode runs both the Docker daemon and containers without root privileges. This reduces risk but does not remove the need for permission, network, secret, and resource boundaries.

Source:

- [Docker rootless mode](https://docs.docker.com/engine/security/rootless/)

## Fact 7 — Rootless Docker-in-Docker still requires privileged mode

Docker's own rootless DIND guidance uses `--privileged` because seccomp, AppArmor, and mount masks must be disabled. Galax rejects privileged DIND as the default code-sandbox design.

Source:

- [Docker rootless mode tips](https://docs.docker.com/engine/security/rootless/tips/)

## Fact 8 — Compose supports conditional service activation

Docker Compose profiles can keep optional research, migration, audit, and sandbox-controller services inactive until explicitly selected by trusted application or operator commands.

Source:

- [Docker Compose profiles](https://docs.docker.com/reference/compose-file/profiles/)

## Fact 9 — Compose provides dependency health gates

`depends_on` with `condition: service_healthy` makes Compose wait for a declared healthcheck before starting a dependent service. This is required for Galax API, Flow runner, and memory gateway startup ordering.

Sources:

- [Compose service dependencies and health checks](https://docs.docker.com/reference/compose-file/services/)
- [Compose startup order](https://docs.docker.com/compose/how-tos/startup-order/)

## Fact 10 — Compose secrets are explicitly granted per service

Docker Compose secrets are mounted only into services that declare them, normally under `/run/secrets`. This is safer than exposing every API key to every container through a shared environment file.

Sources:

- [Docker Compose secrets reference](https://docs.docker.com/reference/compose-file/secrets/)
- [Using secrets in Compose](https://docs.docker.com/compose/how-tos/use-secrets/)

## Fact 11 — Container resource limits must be explicit

Without limits, containers can consume host resources according to host availability. Galax sandbox and worker containers require CPU, memory, process-count, and execution-time limits.

Source:

- [Docker resource constraints](https://docs.docker.com/engine/containers/resource_constraints/)

## Fact 12 — Docker security controls are service-specific

Compose supports controls including `security_opt: no-new-privileges`, read-only filesystems, dropped capabilities, temporary filesystems, healthchecks, internal networks, and service-specific secrets. Galax must verify support in the selected Docker Engine and Compose versions.

Source:

- [Compose services reference](https://docs.docker.com/reference/compose-file/services/)

## Fact 13 — Full self-hosted Supabase is a substantial Compose stack

Supabase officially supports self-hosting through Docker Compose, but its documented full-stack minimum is 4 GB RAM, 2 CPU cores, and 40 GB SSD; recommended resources are higher. Optional services can be removed. Therefore, full Supabase should be an explicit profile or separate stack, not silently added to every small Galax installation.

Source:

- [Self-hosting Supabase with Docker](https://supabase.com/docs/guides/self-hosting/docker)

## Fact 14 — Self-hosting transfers operational responsibility to the owner

A self-hosted Supabase operator owns hardening, updates, database maintenance, backups, disaster recovery, monitoring, uptime, and scaling. This work cannot be delegated to an unapproved CrewAI agent.

Source:

- [Supabase self-hosting responsibilities](https://supabase.com/docs/guides/self-hosting)

## Fact 15 — A single Compose file cannot make an unsafe architecture safe

Containerization does not prove tool authorization, factual correctness, prompt-injection resistance, repository permission safety, or secure code execution. Every gateway and agent profile still requires its own tests.

# Existing-use evidence and its limits

| Evidence | What it proves | What it does not prove |
|---|---|---|
| Official Cerebras Docker multi-agent integration | Docker, Compose, MCP gateway, sandbox, and GPT-OSS can be combined | CrewAI compatibility or Galax security |
| Community CrewAI Compose projects | A CrewAI Python app can run in containers | Current CrewAI version support, secure permissions, or production readiness |
| CrewAI AMP | CrewAI has a managed deployment platform | That the open-source framework includes an equivalent local Compose stack |
| Supabase official Docker Compose | Supabase can be self-hosted through containers | That it is a native CrewAI memory backend |

# Corrected conclusion

```yaml
CrewAI_application_in_container: FACT_CHECKED_SUPPORTED
Galax_application_services_in_Docker_Compose: FACT_CHECKED_SUPPORTED_BY_NORMAL_CONTAINERIZATION
CrewAI_native_Docker_orchestration: NOT_A_CREWAI_FEATURE
CrewAI_native_secure_code_sandbox: REJECTED_DEPRECATED_PATH
privileged_Docker_in_Docker: REJECTED_DEFAULT
rootless_external_sandbox_boundary: SELECTED_FOR_VALIDATION
single_compose_file_guarantees_security: false
production_status: NOT_IMPLEMENTED
```
