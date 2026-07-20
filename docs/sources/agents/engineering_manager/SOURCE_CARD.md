# Agent Source Card — Engineering Manager

**Agent ID:** `engineering_manager`  
**Roster ID:** `AGENT-01`  
**Role:** AI Engineering Manager and CrewAI Execution Planning Lead  
**Status:** `RESEARCHING`  
**Verified:** 2026-07-20

## Assigned source records

### LLM

- [Selected validation LLM source card: Cerebras GPT-OSS 120B](../../llms/cerebras-gpt-oss-120b/SOURCE_CARD.md)
- [Exact official Cerebras model metadata](https://inference-docs.cerebras.ai/api-reference/models/public-models)
- [Free-provider screening decision](../../../research/llms/FREE_PROVIDER_SCREENING_2026-07-20.md)
- [LLM assignment plan](../../../plan/LLM_ASSIGNMENT_PLAN_DRAFT.md)

Current LLM status: `SELECTED_FOR_VALIDATION_NOT_APPROVED`

Manual reserve candidate only:

- [Groq GPT-OSS 120B source card](../../llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md)

The reserve provider is not an automatic fallback.

### Tool

- [Repository Preflight Tool source card](../../tools/repository_preflight_tool/SOURCE_CARD.md)
- [CrewAI official custom-tools documentation](https://docs.crewai.com/learn/create-custom-tools)

Current tool status: `CONDITIONALLY_APPROVED`

## Agent research records

- [Agent 01 Tool Inspection](../../../research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md)
- [GitHub Repository Read/Write Architecture](../../../architecture/GITHUB_REPOSITORY_READ_WRITE_DRAFT.md)
- [Source Traceability Rule](../../../rules/SOURCE_TRACEABILITY_RULE_DRAFT.md)
- [No Exact Duplicates Rule](../../../rules/NO_EXACT_DUPLICATES_RULE_DRAFT.md)

## CrewAI sources

- [CrewAI Agents](https://docs.crewai.com/concepts/agents)
- [CrewAI LLM configuration](https://docs.crewai.com/concepts/llms)
- [CrewAI Tools](https://docs.crewai.com/concepts/tools)
- [CrewAI Sequential Process](https://docs.crewai.com/learn/sequential-process)
- [CrewAI Annotations](https://docs.crewai.com/learn/using-annotations)
- [CrewAI MCP Overview](https://docs.crewai.com/mcp/overview)
- [CrewAI MCP Security](https://docs.crewai.com/mcp/security)

## Planned LLM profile

```yaml
model: cerebras/gpt-oss-120b
reasoning_effort: low
max_completion_tokens: 800
temperature: 1.0
timeout_seconds: 120
max_retries: 1
enabled: false
```

Agent 01 uses low reasoning effort because the repository preflight tool performs deterministic checks. The agent summarizes the structured result and must not redesign the plan.

## Current capability decision

```yaml
role_concept: supported
strict_sequential_execution: supported
dynamic_delegation: rejected
assigned_tool_count: 1
repository_preflight_read: conditionally_supported
repository_write_for_agent_01: rejected_not_required
system_repository_write: planned_for_role_scoped_writer_agents
llm_provider_path: fact_checked_supported
llm_model: selected_for_validation
api_version_2_test: not_run
crewai_live_test: not_run
agent_implementation: not_started
```

## Source query result

A future deterministic query:

```text
source engineering_manager
```

must return this card and the exact LLM and tool links above. It must not reconstruct sources from model memory.

## Revalidation required when

- Agent role, goal, or boundaries change.
- The selected LLM changes.
- The tool schema or implementation changes.
- CrewAI or LiteLLM version changes.
- Cerebras API behavior or rate limits change.
- GitHub repository integration changes.
- Any source link becomes outdated or unavailable.
