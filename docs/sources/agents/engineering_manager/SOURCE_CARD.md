# Agent Source Card — Engineering Manager

**Agent ID:** `engineering_manager`  
**Roster ID:** `AGENT-01`  
**Role:** AI Engineering Manager and CrewAI Execution Planning Lead  
**Status:** `RESEARCHING`  
**Verified:** 2026-07-20

## Framework

- [CrewAI 1.15.4 source card](../../frameworks/crewai-1.15.4/SOURCE_CARD.md)
- [CrewAI package](https://pypi.org/project/crewai/)
- [CrewAI versioned agent documentation](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/agents.mdx)
- [CrewAI sequential process](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/processes.mdx)
- [CrewAI custom tools and typed results](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/learn/create-custom-tools.mdx)
- [CrewAI tool hooks](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/learn/tool-hooks.mdx)
- [Force tool output as task result](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/learn/force-tool-output-as-result.mdx)

Current framework status: `SELECTED_FOR_PINNED_VALIDATION_NOT_APPROVED`

## CrewAI execution settings

```yaml
process: Process.sequential
planning: false
reasoning: false
memory: false
allow_delegation: false
allow_code_execution: false
async_execution: false
respect_context_window: false
```

Agent 01 does not use CrewAI planning or reasoning loops. The deterministic Flow has already constructed the run manifest. Agent 01 performs one bounded interpretation of deterministic preflight evidence.

## LLM profiles

### Private primary candidate

- [Groq GPT-OSS 20B source card](../../llms/groq-openai-gpt-oss-20b/SOURCE_CARD.md)
- [Exact Groq model](https://console.groq.com/docs/model/openai/gpt-oss-20b)

```yaml
profile_id: engineering_manager_groq_gpt_oss_20b_v1
model: groq/openai/gpt-oss-20b
status: DISABLED_PENDING_TESTS
reasoning_effort: low
max_completion_tokens: 800
timeout_seconds: 120
max_retries: 1
max_iter: 4
max_execution_time_seconds: 120
```

The 20B profile is selected for validation because Agent 01 receives a deterministic structured result and performs low-complexity bounded interpretation. It is not approved until the exact quality and tool tests pass.

### Private hosted fallback candidate

- [Cloudflare GPT-OSS 20B source card](../../llms/cloudflare-gpt-oss-20b/SOURCE_CARD.md)

```yaml
profile_id: engineering_manager_cloudflare_gpt_oss_20b_v1
model: '@cf/openai/gpt-oss-20b'
connection: custom_OpenAI_compatible
status: DISABLED_PENDING_TESTS
```

### Optional local fallback

- [Ollama GPT-OSS 20B source card](../../llms/ollama-gpt-oss-20b/SOURCE_CARD.md)

```yaml
status: DISABLED_PENDING_HARDWARE_AND_AGENT_TESTS
```

### High-complexity escalation candidate

- [Groq GPT-OSS 120B source card](../../llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md)

```yaml
status: NOT_SELECTED_BY_DEFAULT
use_condition: 20B_profile_fails_defined_quality_suite_and_120B_is_separately_tested
```

### Rejected historical candidate

- [Cerebras GPT-OSS 120B source card](../../llms/cerebras-gpt-oss-120b/SOURCE_CARD.md)

```yaml
status: REJECTED_TRIAL_ONLY
```

No alternate profile is attached simultaneously. Deterministic Flow may switch only from a safe checkpoint after both profiles are independently approved for Agent 01 and no external mutation is active.

## Assigned tool

- [Repository Preflight Tool source card](../../tools/repository_preflight_tool/SOURCE_CARD.md)
- [Agent 01 Tool Inspection](../../../research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md)

```yaml
assigned_tool_interface: RepositoryPreflightTool
maximum_distinct_tool_interfaces: 1
maximum_tool_calls_per_task: 1
write_permission: false
network_permission: false
repository_scope: configured_Galax_repository_only
result_as_answer: true
tool_status: CONDITIONALLY_APPROVED_NOT_IMPLEMENTED
```

`result_as_answer=true` is selected because the trusted typed preflight result is the evidence for the task and must not be rewritten into an unsupported pass by the model.

## Tool governance

The Crew registers a scoped `PRE_TOOL_CALL` hook that verifies:

```text
agent_id == engineering_manager
tool == RepositoryPreflightTool
operation count == 1
input contains only a valid run_id
no repository write/network/subprocess capability
```

A blocked hook result is not sufficient to stop the workflow by itself. A deterministic task guardrail and Flow transition must stop when the tool status is not `PASS`.

The tool creates a trusted invocation ID. Agent prose without that invocation evidence cannot pass.

## Knowledge and memory infrastructure

- [Drive Knowledge Gateway source card](../../tools/drive_knowledge_gateway/SOURCE_CARD.md)
- [Supabase Memory Gateway source card](../../tools/supabase_memory_gateway/SOURCE_CARD.md)
- [Optional Notion mirror source card](../../tools/notion_memory_gateway/SOURCE_CARD.md)

```yaml
Drive_direct_agent_access: false
LearningPacket_from_Flow: allowed_only_when_manifest_requires
Supabase_direct_agent_access: false
bounded_MemoryContext_from_Flow: allowed
Notion_direct_agent_access: false
Notion_role: optional_curated_mirror_only
repository_over_memory: true
```

These gateways are trusted Flow/application infrastructure, not additional Agent 01 tools.

## Research records

- [Full CrewAI 1.15.4 remediation blueprint](../../../research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md)
- [Agent 01 tool inspection](../../../research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md)
- [CrewAI capability and limitation matrix](../../../research/crewai/CREWAI_1_15_4_CAPABILITY_LIMIT_MATRIX.md)
- [CrewAI GitHub read/write and free-LLM audit](../../../research/crewai/CREWAI_GITHUB_RW_FREE_LLM_AUDIT_2026-07-20.md)
- [Corrected LLM assignment plan](../../../plan/LLM_ASSIGNMENT_PLAN_DRAFT.md)
- [GitHub repository read/write architecture](../../../architecture/GITHUB_REPOSITORY_READ_WRITE_DRAFT.md)
- [Validated LLM routing and failover](../../../rules/VALIDATED_LLM_FAILOVER_RULE_DRAFT.md)

## Exact supported work

Agent 01 may:

```text
- receive the actual typed RepositoryPreflightTool result
- receive bounded verified MemoryContext prepared by the Flow
- receive a verified LearningPacket only when required by the manifest
- identify passed, failed, and blocked checks
- return the trusted preflight result and a bounded self-diagnostic
```

Agent 01 may not:

```text
- select or add agents dynamically
- reorder tasks
- delegate
- call a second tool
- directly search Drive, web, Supabase, or Notion
- modify the repository or run state
- create a branch
- approve an agent, LLM, tool, architecture, risk, or release
- claim missing or failed evidence passed
- continue the Flow after a blocking result
```

The deterministic Flow creates the run manifest, selects approved agents, retrieves knowledge/memory, creates the run branch, controls provider selection, and enforces execution order.

## Required LLM and tool proof

```text
- system-instruction adherence
- correct single RepositoryPreflightTool selection
- valid run_id-only arguments
- actual invocation ID
- typed tool-result round trip
- result_as_answer integrity
- PRE_MODEL_CALL and PRE_TOOL_CALL policy enforcement
- blocked tool result stops the Flow
- timeout and HTTP 429 behavior
- current provider capacity recording
- data-classification enforcement
- bounded LearningPacket and MemoryContext handling
- no fabricated Action/Observation
- self-diagnostic matches trusted evidence
```

## Current decision

```yaml
role_concept: supported
strict_sequential_execution: supported
planning_loop: disabled
reasoning_loop: disabled
provider_native_reasoning_effort: selected_for_validation
dynamic_delegation: rejected
assigned_tool_count: 1
repository_preflight_read: conditionally_supported
repository_write_for_agent_01: rejected_not_required
Flow_supplied_knowledge_and_memory: specified_not_tested
Groq_20B_profile: selected_not_tested
Cloudflare_20B_fallback_profile: selected_not_tested
Ollama_local_profile: optional_not_tested
Groq_120B_escalation: not_selected_by_default
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

- Agent role, task, prompt, output, or boundary change.
- Active or alternate LLM provider/model/profile change.
- Tool schema, result schema, hook, or implementation change.
- Knowledge or memory schema change.
- CrewAI, MCP adapter, provider SDK, or LiteLLM version change.
- GitHub repository integration or permission change.
- Rate, allocation, context, security, privacy, or data-use behavior change.
