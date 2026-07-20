# Galax AI Source Index — Draft

**Status:** `DRAFT_MUTABLE`  
**Verified:** 2026-07-20

This index is the canonical human-readable entry point for agent, LLM, framework, tool, knowledge, memory, infrastructure, and readiness sources. It contains links only to existing repository records or official sources.

## Current readiness

```yaml
full_build_prompt_status: BLOCKED_NOT_READY_TO_PROMPT_CREWAI
agents_enabled: 0
primary_llm: DISABLED_PENDING_TESTS
fallback_llm: DISABLED_PENDING_TESTS
production_ready: false
```

- [Final free-tier readiness audit](../research/readiness/FINAL_FREE_TIER_READINESS_AUDIT_2026-07-20.md)

## Agents

| Agent ID | Role | LLM | Tool | Status |
|---|---|---|---|---|
| [`engineering_manager`](agents/engineering_manager/SOURCE_CARD.md) | AI Engineering Manager and CrewAI Execution Planning Lead | [`cerebras/gpt-oss-120b`](llms/cerebras-gpt-oss-120b/SOURCE_CARD.md) | [`RepositoryPreflightTool`](tools/repository_preflight_tool/SOURCE_CARD.md) | `RESEARCHING` |

Agents 02–15 have candidate profiles in the 15-agent plans. Individual source cards will be added only after each agent's role, LLM profile, and single-tool inspection begins.

## Frameworks

| Source ID | Framework/version | Status | Official package source |
|---|---|---|---|
| [`FRAMEWORK-crewai-1.15.4`](frameworks/crewai-1.15.4/SOURCE_CARD.md) | CrewAI `1.15.4` | `SELECTED_FOR_PINNED_VALIDATION` | [CrewAI package](https://pypi.org/project/crewai/) |

## LLMs

| Source ID | Provider/model | Runtime role | Status | Official model source |
|---|---|---|---|---|
| [`LLM-cerebras-gpt-oss-120b`](llms/cerebras-gpt-oss-120b/SOURCE_CARD.md) | Cerebras `gpt-oss-120b` | Primary candidate | `DISABLED_PENDING_API_V2_AND_ACCOUNT_TESTS` | [Cerebras public model metadata](https://inference-docs.cerebras.ai/api-reference/models/public-models) |
| [`LLM-groq-openai-gpt-oss-120b`](llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md) | Groq `openai/gpt-oss-120b` | Controlled fallback candidate | `DISABLED_PENDING_SEPARATE_TESTS` | [Groq exact model page](https://console.groq.com/docs/model/openai/gpt-oss-120b) |

The fallback is not a silent provider switch. It must pass its own per-agent compatibility tests and may be selected only by deterministic Flow from a safe checkpoint.

## Agent tools and Flow infrastructure gateways

| Source ID | Tool/gateway | Status | Official compatibility source |
|---|---|---|---|
| [`TOOL-repository-preflight`](tools/repository_preflight_tool/SOURCE_CARD.md) | `RepositoryPreflightTool` | `CONDITIONALLY_APPROVED` | [CrewAI custom tools](https://docs.crewai.com/learn/create-custom-tools) |
| [`TOOL-drive-knowledge-gateway`](tools/drive_knowledge_gateway/SOURCE_CARD.md) | `DriveKnowledgeGateway` | `SELECTED_FOR_VALIDATION` | [Google Drive API search](https://developers.google.com/workspace/drive/api/guides/search-files) |
| [`TOOL-supabase-memory-gateway`](tools/supabase_memory_gateway/SOURCE_CARD.md) | `GalaxMemoryGateway` | `SELECTED_FOR_VALIDATION` | [Supabase AI and vectors](https://supabase.com/docs/guides/ai) |
| [`TOOL-notion-memory-gateway`](tools/notion_memory_gateway/SOURCE_CARD.md) | `GalaxNotionMirrorGateway` | `OPTIONAL_SELECTED_FOR_VALIDATION` | [Notion API](https://developers.notion.com/) |

Drive, primary memory, and Notion mirror gateways are controlled Flow/application infrastructure. They do not count as additional agent tools and are not directly exposed to agents.

## Infrastructure

| Source ID | Infrastructure | Status | Official source |
|---|---|---|---|
| [`INFRA-docker-compose`](infrastructure/docker-compose/SOURCE_CARD.md) | Docker Engine + Compose | `SELECTED_FOR_VALIDATION` | [Docker Compose](https://docs.docker.com/compose/) |

## Current core rules

- [No unsupported agent work](../rules/NO_UNSUPPORTED_AGENT_WORK_RULE_DRAFT.md)
- [Per-agent LLM compatibility](../rules/PER_AGENT_LLM_COMPATIBILITY_RULE_DRAFT.md)
- [Validated LLM failover](../rules/VALIDATED_LLM_FAILOVER_RULE_DRAFT.md)
- [Free-tier capacity snapshot](../rules/FREE_TIER_CAPACITY_SNAPSHOT_RULE_DRAFT.md)
- [Knowledge before implementation](../rules/KNOWLEDGE_BEFORE_IMPLEMENTATION_RULE_DRAFT.md)
- [Supabase primary memory + Notion mirror](../rules/SUPABASE_PRIMARY_MEMORY_NOTION_MIRROR_RULE_DRAFT.md)
- [Automatic revalidation research](../rules/AUTOMATIC_REVALIDATION_RESEARCH_RULE_DRAFT.md)
- [Source traceability](../rules/SOURCE_TRACEABILITY_RULE_DRAFT.md)
- [No exact duplicates](../rules/NO_EXACT_DUPLICATES_RULE_DRAFT.md)

Earlier rule retained for mirror details only where not superseded:

- [Earlier Notion memory draft](../rules/NOTION_MEMORY_RULE_DRAFT.md)

## Research, architecture, and plans

- [Final free-tier readiness audit](../research/readiness/FINAL_FREE_TIER_READINESS_AUDIT_2026-07-20.md)
- [CrewAI 1.15.4 capability and limitation matrix](../research/crewai/CREWAI_1_15_4_CAPABILITY_LIMIT_MATRIX.md)
- [CrewAI + Docker fact check](../research/docker/CREWAI_DOCKER_FACT_CHECK_2026-07-20.md)
- [Fully containerized Galax architecture](../architecture/FULLY_DOCKERIZED_CREWAI_FLOW_DRAFT.md)
- [Notion vs Supabase memory decision](../research/memory/NOTION_VS_SUPABASE_MEMORY_DECISION_2026-07-20.md)
- [Notion + CrewAI earlier ten facts](../research/notion/NOTION_CREWAI_10_VERIFIED_FACTS_2026-07-20.md)
- [15-agent capability mapping](../plan/AGENT_CAPABILITY_MAPPING_DRAFT.md)
- [15-agent LLM/tool/knowledge/memory matrix](../plan/AGENT_LLM_TOOL_KNOWLEDGE_MEMORY_MATRIX_DRAFT.md)
- [15-agent runtime limits](../plan/15_AGENT_RUNTIME_LIMITS_DRAFT.md)
- [Free provider screening](../research/llms/FREE_PROVIDER_SCREENING_2026-07-20.md)
- [LLM assignment plan](../plan/LLM_ASSIGNMENT_PLAN_DRAFT.md)
- [Google Drive knowledge + earlier Notion architecture](../architecture/GOOGLE_DRIVE_KNOWLEDGE_NOTION_MEMORY_DRAFT.md)
- [GitHub repository read/write architecture](../architecture/GITHUB_REPOSITORY_READ_WRITE_DRAFT.md)

## Deterministic query mapping

```yaml
aliases:
  engineering_manager: agents/engineering_manager/SOURCE_CARD.md
  AGENT-01: agents/engineering_manager/SOURCE_CARD.md
  agent_01: agents/engineering_manager/SOURCE_CARD.md
  crewai: frameworks/crewai-1.15.4/SOURCE_CARD.md
  crewai-1.15.4: frameworks/crewai-1.15.4/SOURCE_CARD.md
  cerebras-gpt-oss-120b: llms/cerebras-gpt-oss-120b/SOURCE_CARD.md
  groq-gpt-oss-120b: llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md
  drive-knowledge: tools/drive_knowledge_gateway/SOURCE_CARD.md
  supabase-memory: tools/supabase_memory_gateway/SOURCE_CARD.md
  notion-memory: tools/notion_memory_gateway/SOURCE_CARD.md
  docker: infrastructure/docker-compose/SOURCE_CARD.md
  free-tier-readiness: ../research/readiness/FINAL_FREE_TIER_READINESS_AUDIT_2026-07-20.md
```

Expected queries:

```text
source engineering_manager
source crewai
source cerebras-gpt-oss-120b
source groq-gpt-oss-120b
source drive-knowledge
source supabase-memory
source notion-memory
source docker
source free-tier-readiness
```

The command returns links stored in the mapped source card or research record. It must not ask an LLM to remember or recreate source URLs.
