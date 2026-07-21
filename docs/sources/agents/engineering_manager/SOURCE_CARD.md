# Agent Source Card — Engineering Manager

**Agent ID:** `engineering_manager`  
**Roster ID:** `AGENT-01`  
**Role:** AI Engineering Manager and CrewAI Execution Planning Lead  
**Status:** `RESEARCHING_NOT_APPROVED`  
**Verified:** 2026-07-21

## Active execution contract

- [Foundation and Agent 01 Flow execution contract](../../../plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md)

```yaml
agent_id: engineering_manager
tools: []
direct_tool_calls: 0
receives:
  - trusted RepositoryPreflightResult
produces:
  - AgentTaskResult
LLM_calls_per_run: 1
hidden_second_agent_call: prohibited
```

`RepositoryPreflightTool` is a Flow-owned upstream dependency, not an Agent 01 assigned tool:

- [Repository Preflight Tool source card](../../tools/repository_preflight_tool/SOURCE_CARD.md)

```text
GalaxFoundationFlow invokes RepositoryPreflightTool exactly once
→ validates invocation evidence and typed result
→ checks LLM profile readiness
→ passes the trusted result to engineering_manager
→ engineering_manager performs one bounded evaluation
→ Flow validates claims and builds HumanReviewRequest deterministically
```

Older direct-tool, one-agent/one-tool, Agent 01 tool-call, and `result_as_answer` instructions are inactive only where they conflict with this exact evaluator architecture. Other security, evidence, testing, role, and repository restrictions remain active.

## Framework

- [CrewAI 1.15.4 source card](../../frameworks/crewai-1.15.4/SOURCE_CARD.md)
- [CrewAI package](https://pypi.org/project/crewai/)
- [CrewAI agents](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/agents.mdx)
- [CrewAI sequential process](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/processes.mdx)
- [CrewAI Flows](https://github.com/crewAIInc/crewAI/tree/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/flows.mdx)
- [CrewAI tasks and typed outputs](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/tasks.mdx)

Current framework status: `SELECTED_FOR_PINNED_VALIDATION_NOT_APPROVED`.

## CrewAI execution settings

```yaml
process: Process.sequential
planning: false
reasoning: false
memory: false
allow_delegation: false
allow_code_execution: false
async_execution: false
parallel_agents: false
parallel_tool_calls: false
concurrent_llm_calls: 1
respect_context_window: false
```

The deterministic Flow owns manifest validation, tool availability, tool invocation, invocation evidence validation, provider/profile readiness, routing, human-review construction, pause/resume state, and final completion.

## Role, goal, and bounded output

### Goal

Evaluate one trusted `RepositoryPreflightResult`, classify confirmed and missing evidence without fabrication, and produce one strict `AgentTaskResult` with an allowed transition recommendation.

### Agent 01 may

```text
- receive one bounded trusted RepositoryPreflightResult;
- identify PASS, BLOCKED, and FAIL findings;
- summarize only supported evidence;
- place unsupported claims in unsupported_claims[];
- return exact remedies from the trusted result;
- recommend STOP or HUMAN_REVIEW or CONTINUE_TO_TEST_ONLY_STAGE;
- return one AgentTaskResult.
```

### Agent 01 may not

```text
- call RepositoryPreflightTool or any other tool;
- create or modify invocation IDs, hashes, timestamps, or evidence;
- select or add agents;
- reorder tasks or control Flow routing;
- delegate;
- browse the web or access filesystem/network directly;
- query Drive, Supabase, Notion, GitHub, or MCP directly;
- modify repository or run state;
- create branches, commits, pull requests, merges, or deployments;
- create or modify the human decision;
- execute a second LLM call for HumanReviewRequest;
- claim missing, blocked, or failed evidence passed;
- enable Agents 02–15.
```

## LLM profiles

### Private primary candidate

- [Groq GPT-OSS 20B source card](../../llms/groq-openai-gpt-oss-20b/SOURCE_CARD.md)

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
profile_enabled: false
provider_live_tested: false
agent_profile_approved: false
```

### Private hosted fallback candidate

- [Cloudflare GPT-OSS 20B source card](../../llms/cloudflare-gpt-oss-20b/SOURCE_CARD.md)

```yaml
profile_id: engineering_manager_cloudflare_gpt_oss_20b_v1
model: '@cf/openai/gpt-oss-20b'
connection: custom_OpenAI_compatible
status: DISABLED_PENDING_TESTS
profile_enabled: false
provider_live_tested: false
agent_profile_approved: false
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

No alternate profile is attached simultaneously. No automatic or silent provider switch is allowed.

## LLM profile readiness gate

Before Agent 01 runs, trusted Flow code verifies:

```text
profile exists
profile_enabled is true
provider_live_tested is true
agent_profile_approved is true
profile matches engineering_manager
data classification is allowed
required credential is available
current capacity snapshot is valid
```

Any failure returns `BLOCKED_LLM_PROFILE_NOT_APPROVED` before token use.

Both active candidates remain disabled. CrewAI Studio must not activate them.

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

These are trusted Flow/application infrastructure, not Agent 01 tools.

## Required proof

```text
- system-instruction adherence;
- no tool is attached or invoked by Agent 01;
- one trusted RepositoryPreflightResult reaches Agent 01;
- exactly one Agent 01 LLM execution;
- strict AgentTaskResult output;
- every supported claim maps to real evidence;
- fabricated or missing evidence blocks;
- explicit Flow routers stop blocked routes;
- HumanReviewRequest is built in pure Python/Pydantic;
- no hidden second agent call;
- profile readiness blocks before token use;
- offline permission declaration is separated from live GitHub evidence;
- timeout and HTTP 429 behavior;
- token and capacity limits;
- secret and data-classification enforcement;
- no operational or tested claim without evidence.
```

## Research records

- [Full CrewAI remediation blueprint](../../../research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md)
- [Historical Agent 01 tool inspection](../../../research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md)
- [CrewAI capability matrix](../../../research/crewai/CREWAI_1_15_4_CAPABILITY_LIMIT_MATRIX.md)
- [Corrected LLM assignment plan](../../../plan/LLM_ASSIGNMENT_PLAN_DRAFT.md)
- [Validated LLM routing and failover](../../../rules/VALIDATED_LLM_FAILOVER_RULE_DRAFT.md)

## Current decision

```yaml
role_concept: supported
strict_sequential_execution: supported
Flow_owned_preflight_design: selected_for_implementation_test
assigned_direct_tool_count: 0
Agent_01_LLM_calls: 1
HumanReviewRequest_LLM_calls: 0
Groq_20B_profile: selected_not_tested
Cloudflare_20B_fallback_profile: selected_not_tested
agent_implementation: not_started
final_status: CONDITIONALLY_COMPATIBLE_NOT_APPROVED
```

## Revalidation triggers

- Agent role, prompt, task, output, or boundary change.
- Flow ownership, router, preflight, or human-review contract change.
- Active or alternate LLM provider/model/profile change.
- Result schema, evidence validation, or permission contract change.
- Knowledge or memory schema change.
- CrewAI, provider SDK, GitHub integration, rate, allocation, security, privacy, or data-use change.
