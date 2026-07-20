# Agent Source Card — Engineering Manager

**Agent ID:** `engineering_manager`  
**Roster ID:** `AGENT-01`  
**Role:** AI Engineering Manager and CrewAI Execution Planning Lead  
**Status:** `RESEARCHING`  
**Verified:** 2026-07-20

## Framework

- [CrewAI 1.15.4 source card](../../frameworks/crewai-1.15.4/SOURCE_CARD.md)
- [CrewAI package](https://pypi.org/project/crewai/)
- [CrewAI versioned agent documentation](https://github.com/crewAIInc/crewAI/blob/main/docs/v1.15.4/en/concepts/agents.mdx)
- [CrewAI sequential process](https://docs.crewai.com/en/concepts/processes)

Current framework status: `SELECTED_FOR_PINNED_VALIDATION_NOT_APPROVED`

## LLM profiles

### Private primary candidate

- [Groq GPT-OSS 120B source card](../../llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md)
- [Exact Groq model](https://console.groq.com/docs/model/openai/gpt-oss-120b)

```yaml
profile_id: engineering_manager_groq_gpt_oss_120b_v1
model: groq/openai/gpt-oss-120b
status: DISABLED_PENDING_TESTS
reasoning_effort: low
max_completion_tokens: 800
timeout_seconds: 120
max_retries: 1
max_iter: 4
max_execution_time_seconds: 120
```

### Private hosted fallback candidate

- [Cloudflare GPT-OSS 120B source card](../../llms/cloudflare-gpt-oss-120b/SOURCE_CARD.md)

```yaml
profile_id: engineering_manager_cloudflare_gpt_oss_120b_v1
model: '@cf/openai/gpt-oss-120b'
connection: custom_OpenAI_compatible
status: DISABLED_PENDING_TESTS
```

### Optional local fallback

- [Ollama GPT-OSS 20B source card](../../llms/ollama-gpt-oss-20b/SOURCE_CARD.md)

```yaml
status: DISABLED_PENDING_HARDWARE_AND_AGENT_TESTS
```

### Rejected historical candidate

- [Cerebras GPT-OSS 120B source card](../../llms/cerebras-gpt-oss-120b/SOURCE_CARD.md)

```yaml
status: REJECTED_TRIAL_ONLY
```

No alternate profile is attached simultaneously to the agent. Deterministic Flow may switch profiles only from a safe checkpoint after both profiles are independently approved for Agent 01.

## Assigned tool

- [Repository Preflight Tool source card](../../tools/repository_preflight_tool/SOURCE_CARD.md)
- [CrewAI custom tools](https://docs.crewai.com/learn/create-custom-tools)

```yaml
assigned_tool_interface: RepositoryPreflightTool
maximum_distinct_tool_interfaces: 1
write_permission: false
network_permission: false
repository_scope: configured_Galax_repository_only
tool_status: CONDITIONALLY_APPROVED_NOT_IMPLEMENTED
```

## Knowledge and memory infrastructure

- [Drive Knowledge Gateway source card](../../tools/drive_knowledge_gateway/SOURCE_CARD.md)
- [Supabase Memory Gateway source card](../../tools/supabase_memory_gateway/SOURCE_CARD.md)
- [Optional Notion mirror source card](../../tools/notion_memory_gateway/SOURCE_CARD.md)

```yaml
Drive_direct_agent_access: false
LearningPacket_from_Flow: allowed_when_required
Supabase_direct_agent_access: false
bounded_MemoryContext_from_Flow: allowed
Notion_direct_agent_access: false
Notion_role: optional_curated_mirror_only
repository_over_memory: true
```

These gateways are trusted Flow/application infrastructure, not additional Agent 01 tools.

## Research records

- [Agent 01 tool inspection](../../../research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md)
- [CrewAI capability and limitation matrix](../../../research/crewai/CREWAI_1_15_4_CAPABILITY_LIMIT_MATRIX.md)
- [CrewAI GitHub read/write and free-LLM audit](../../../research/crewai/CREWAI_GITHUB_RW_FREE_LLM_AUDIT_2026-07-20.md)
- [15-agent runtime limits](../../../plan/15_AGENT_RUNTIME_LIMITS_DRAFT.md)
- [15-agent LLM/tool/knowledge/memory matrix](../../../plan/AGENT_LLM_TOOL_KNOWLEDGE_MEMORY_MATRIX_DRAFT.md)
- [GitHub repository read/write architecture](../../../architecture/GITHUB_REPOSITORY_READ_WRITE_DRAFT.md)
- [Validated LLM routing and failover](../../../rules/VALIDATED_LLM_FAILOVER_RULE_DRAFT.md)

## Exact supported work

Agent 01 may:

```text
- receive the actual structured RepositoryPreflightTool result
- receive bounded verified Supabase memory prepared by the Flow
- receive a verified LearningPacket when required
- identify passed, failed, and blocked checks
- summarize why the run may or may not continue
- return a structured preflight decision and self-diagnostic
```

Agent 01 may not:

```text
- select or add agents dynamically
- reorder tasks
- delegate work
- directly search Google Drive
- directly query Supabase or write Notion
- modify the repository
- create a branch
- approve an agent, LLM, tool, architecture, or release
- claim a missing file or failed check passed
- continue after a blocking preflight result
```

The deterministic Flow creates the run manifest, selects approved agents, retrieves knowledge/memory, creates the run branch, controls provider selection, and enforces execution order.

## Required LLM proof

Each candidate profile must independently prove:

```text
system instruction adherence
single RepositoryPreflightTool selection
valid input arguments
actual tool-result round trip
structured RepositoryPreflightResult interpretation
structured AgentTaskResult output
usage and capacity recording
timeout and HTTP 429 behavior
data-classification enforcement
bounded LearningPacket and MemoryContext handling
sequential stop on blocking result
```

## Self-diagnostic boundary

Agent 01's self-diagnostic is advisory until it passes:

```text
structured output
→ deterministic guardrail
→ actual preflight evidence comparison
→ knowledge/memory evidence comparison when present
→ downstream release audit
```

Its own `PASS` value is not final approval.

## Current decision

```yaml
role_concept: supported
strict_sequential_execution: supported
dynamic_delegation: rejected
assigned_tool_count: 1
repository_preflight_read: conditionally_supported
repository_write_for_agent_01: rejected_not_required
Flow_supplied_knowledge_and_memory: specified_not_tested
Groq_profile: selected_not_tested
Cloudflare_fallback_profile: selected_not_tested
Ollama_local_profile: optional_not_tested
Cerebras_profile: rejected_trial_only
agent_implementation: not_started
final_status: CONDITIONALLY_COMPATIBLE_NOT_APPROVED
```

## Source query

```text
source engineering_manager
```

must return this card and its exact framework, LLM, tool, knowledge, memory, and research links. It must not recreate URLs from model memory.

## Revalidation triggers

- Agent role, goal, task, prompt, or boundaries change.
- Active or alternate LLM provider/model/profile changes.
- Tool schema or implementation changes.
- Knowledge or memory schema changes.
- CrewAI, MCP adapter, provider SDK, or LiteLLM version changes.
- GitHub repository integration or permissions change.
- Rate, allocation, context, security, privacy, or data-use behavior changes.
