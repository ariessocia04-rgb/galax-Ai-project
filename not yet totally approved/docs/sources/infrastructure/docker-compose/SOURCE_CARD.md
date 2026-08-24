# Infrastructure Source Card — Docker Compose

**Source ID:** `INFRA-docker-compose`  
**Status:** `SELECTED_FOR_VALIDATION`  
**Approved for production:** No  
**Verified:** 2026-07-20

## Identity

```yaml
runtime: Docker_Engine_rootless_candidate
orchestrator: Docker_Compose
purpose: containerize_Galax_application_services
privileged_DIND: rejected
sandbox_boundary: separate_rootless_daemon_or_host
```

## Official sources

- [Docker Compose](https://docs.docker.com/compose/)
- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Compose services](https://docs.docker.com/reference/compose-file/services/)
- [Compose profiles](https://docs.docker.com/reference/compose-file/profiles/)
- [Compose secrets](https://docs.docker.com/reference/compose-file/secrets/)
- [Using Compose secrets](https://docs.docker.com/compose/how-tos/use-secrets/)
- [Startup order and health checks](https://docs.docker.com/compose/how-tos/startup-order/)
- [Docker rootless mode](https://docs.docker.com/engine/security/rootless/)
- [Rootless Docker-in-Docker limitation](https://docs.docker.com/engine/security/rootless/tips/)
- [Docker resource constraints](https://docs.docker.com/engine/containers/resource_constraints/)
- [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

## Related CrewAI evidence

- [CrewAI documentation](https://docs.crewai.com/)
- [CrewAI AMP managed deployment](https://docs.crewai.com/enterprise/introduction)
- [CrewAI 1.15.4 agent/code execution limitation](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/agents.mdx)

## Existing agent-stack evidence

- [Cerebras Docker multi-agent integration](https://inference-docs.cerebras.ai/integrations/docker)

This example is not CrewAI and is recorded only as Docker/Cerebras multi-agent infrastructure evidence.

## Current decision

```yaml
CrewAI_app_containerization: supported_as_normal_Python_container
Compose_multi_service_stack: supported
CrewAI_native_compose_blueprint: not_found
privileged_DIND_default: rejected
unrestricted_Docker_socket_mount: rejected
rootless_separate_sandbox: selected_for_validation
live_tests: not_run
```

## Revalidation triggers

- Docker Engine version.
- Docker Compose version.
- Base image digest.
- Compose service schema.
- Network or secret policy.
- Sandbox daemon/controller design.
- Host OS or rootless prerequisites.
