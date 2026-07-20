# Agent Source Card — Engineering Manager

**Agent ID:** `engineering_manager`  
**Roster ID:** `AGENT-01`  
**Role:** AI Engineering Manager and CrewAI Execution Planning Lead  
**Status:** `RESEARCHING`  
**Verified:** 2026-07-20

## Assigned source records

### Framework

- [CrewAI 1.15.4 source card](../../frameworks/crewai-1.15.4/SOURCE_CARD.md)
- [CrewAI 1.15.4 package](https://pypi.org/project/crewai/)

Current framework status: `SELECTED_FOR_PINNED_VALIDATION`

### LLM

- [Candidate LLM source card: Cerebras GPT-OSS 120B](../../llms/cerebras-gpt-oss-120b/SOURCE_CARD.md)
- [Exact official model metadata](https://inference-docs.cerebras.ai/api-reference/models/public-models)
- [Free-provider screening decision](../../../research/llms/FREE_PROVIDER_SCREENING_2026-07-20.md)
- [LLM assignment plan](../../../plan/LLM_ASSIGNMENT_PLAN_DRAFT.md)

Current LLM status: `SELECTED_FOR_VALIDATION_NOT_USED`

Manual reserve candidate only:

- [Groq GPT-OSS 120B source card](../../llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md)

The reserve provider is not an automatic fallback.

### Tool

- [Repository Preflight Tool source card](../../tools/repository_preflight_tool/SOURCE_CARD.md)
- [CrewAI official custom-tools documentation](https://docs.crewai.com/learn/create-custom-tools)

Current tool status: `CONDITIONALLY_APPROVED`

## Agent research records

- [Agent 01 Tool Inspection](../../../research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md)
- [CrewAI Capability and Limitation Matrix](../../../research/crewai/CREWAI_1_15_4_CAPABILITY_LIMIT_MATRIX.md)
- [15-Agent Capability Mapping](../../../plan/AGENT_CAPABILITY_MAPPING_DRAFT.md)
- [GitHub Repository Read/Write Architecture](../../../architecture/GITHUB_REPOSITORY_READ_WRITE_DRAFT.md)
- [No Unsupported Agent Work Rule](../../../rules/NO_UNSUPPORTED_AGENT_WORK_RULE_DRAFT.md)
- [Per-Agent LLM Compatibility Rule](../../../rules/PER_AGENT_LLM_COMPATIBILITY_RULE_DRAFT.md)
- [Source Traceability Rule](../../../rules/SOURCE_TRACEABILITY_RULE_DRAFT.md)
- [No Exact Duplicates Rule](../../../rules/NO_EXACT_DUPLICATES_RULE_DRAFT.md)

## CrewAI sources

- [CrewAI 1.15.4 Agents](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/agents.mdx)
- [CrewAI Tools](https://docs.crewai.com/en/concepts/tools)
- [CrewAI Sequential Process](https://docs.crewai.com/en/concepts/processes)
- [CrewAI Tasks and Guardrails](https://docs.crewai.com/en/concepts/tasks)
- [CrewAI Flows](https://docs.crewai.com/en/concepts/flows)

## Exact supported work

Agent 01 may:

```text
- receive the actual structured result of RepositoryPreflightTool
- identify failed, blocked, and passed checks
- summarize why the run may or may not continue
- return a structured preflight decision and self-diagnostic
```

Agent 01 may not:

```text
- select or add agents dynamically
- reorder tasks
- delegate work
- modify the repository
- create a branch
- approve an agent, LLM, tool, architecture, or release
- claim a missing file or failed check passed
- continue after a blocking preflight result
```

The deterministic Flow/application creates the run manifest, selects approved agents, creates the run branch, and controls execution order.

## LLM compatibility contract

```yaml
profile_id: engineering_manager_cerebras_gpt_oss_120b_v1
status: DISABLED_PENDING_TESTS
model: cerebras/gpt-oss-120b
reasoning_effort: low
max_completion_tokens: 800
temperature: 1.0
timeout_seconds: 120
max_retries: 1
max_rpm: 4
max_iter: 4
max_execution_time_seconds: 120
respect_context_window: false
crewai_reasoning_loop: false
memory: false
allow_delegation: false
allow_code_execution: false
async_execution: false
```

Required LLM capabilities:

```text
- system instruction adherence
- one-tool function calling
- valid RepositoryPreflightInput arguments
- actual tool-result round trip
- structured RepositoryPreflightResult interpretation
- structured AgentTaskResult output
- token usage reporting
- safe timeout and HTTP 429 behavior
```

## One-tool contract

```yaml
assigned_tool_interface: RepositoryPreflightTool
maximum_distinct_tool_interfaces: 1
write_permission: false
network_permission: false
repository_scope: configured_galax_repository_only
```

## Self-diagnostic boundary

Agent 01's self-diagnostic is advisory until it passes:

```text
structured output
→ deterministic guardrail
→ actual preflight tool evidence comparison
→ downstream release audit
```

Its own `PASS` value is not final approval.

## Current capability decision

```yaml
role_concept: supported
strict_sequential_execution: supported
dynamic_delegation: rejected
assigned_tool_count: 1
repository_preflight_read: conditionally_supported
repository_write_for_agent_01: rejected_not_required
system_repository_write: planned_for_role_scoped_writer_agents
llm_profile: selected_not_tested
agent_implementation: not_started
final_status: CONDITIONALLY_COMPATIBLE_NOT_APPROVED
```

## Source query result

A future deterministic query:

```text
source engineering_manager
```

must return this card and the exact framework, LLM, and tool links above. It must not reconstruct sources from model memory.

## Revalidation required when

- Agent role, goal, task, or boundaries change.
- The selected LLM or its profile changes.
- The tool schema or implementation changes.
- CrewAI or LiteLLM version changes.
- GitHub repository integration changes.
- Rate, pricing, provider API, security, or privacy behavior changes.
- Any source link becomes outdated or unavailable.
