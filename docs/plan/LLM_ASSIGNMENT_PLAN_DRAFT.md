# LLM Assignment Plan — Draft

**Status:** `DRAFT_MUTABLE`  
**Selected model:** `cerebras/gpt-oss-120b`  
**Selection status:** `SELECTED_FOR_VALIDATION`  
**Production status:** `NOT_APPROVED`  
**Crew process:** `Process.sequential`

## 1. Architecture decision

All 15 agents will initially validate against one canonical provider/model combination:

```yaml
provider: Cerebras Inference
provider_model_id: gpt-oss-120b
crewai_model_id: cerebras/gpt-oss-120b
```

Reasons:

```text
- Reduces provider-specific integration failures.
- Reduces duplicate LLM source records.
- Makes token accounting and security review simpler.
- Provides reasoning, tool calling, strict structured output, and long context.
- Has a larger documented free daily quota than the other qualified candidate.
- CrewAI source code contains a direct Cerebras provider path.
```

This is not approval to run the model. Every profile remains disabled until the LLM validation suite passes.

## 2. One agent, one tool remains unchanged

```text
LLM != TOOL
```

Every agent has:

```yaml
llm_profiles: exactly_one
tool_interfaces: exactly_one
```

The common LLM may be reused by multiple agents. The one-to-one policy applies to each agent's role-specific tool interface, not to exclusive ownership of an LLM provider.

Google Drive knowledge and Notion memory are controlled Flow/application infrastructure. They are not additional LLMs or agent tools.

## 3. No duplicate LLM records

All agents link to this one canonical source card:

```text
docs/sources/llms/cerebras-gpt-oss-120b/SOURCE_CARD.md
```

Do not copy the same provider/model facts into 15 separate LLM source cards. Agent source cards contain links to the canonical card.

Configuration profiles may differ in reasoning effort and completion cap. These are materially different configurations and are not exact duplicates.

## 4. Per-agent assignment

| ID | Agent | Reasoning effort | Max completion tokens | Reason |
|---|---|---:|---:|---|
| 01 | Engineering Manager / Preflight | `low` | 800 | Uses deterministic preflight evidence; should summarize, not redesign |
| 02 | Product Requirements Lead | `medium` | 1,600 | Converts requests into explicit requirements and acceptance criteria |
| 03 | Evidence Researcher | `high` | 2,200 | Compares multiple authoritative and owner-provided sources and limitations |
| 04 | Solution Architect | `high` | 2,400 | Performs architecture trade-off and failure-mode analysis |
| 05 | UX and Accessibility Designer | `medium` | 1,600 | Produces bounded interaction and accessibility specifications |
| 06 | Frontend Engineer | `medium` | 2,000 | Implements scoped UI changes using approved design, API contract, and LearningPacket |
| 07 | Backend/API Engineer | `high` | 2,200 | Handles domain logic, authorization boundaries, failures, and contracts |
| 08 | Database Engineer | `high` | 2,200 | Evaluates migrations, constraints, concurrency, and rollback |
| 09 | CrewAI Engineer | `high` | 2,400 | Configures agents, tasks, Flows, schemas, guardrails, and provider behavior |
| 10 | Integration/MCP Engineer | `high` | 2,200 | Verifies external schemas, authentication, retries, and permissions |
| 11 | Security and Privacy Engineer | `high` | 2,400 | Performs threat analysis and verifies high-risk boundaries |
| 12 | QA and Test Engineer | `medium` | 1,800 | Creates and evaluates bounded test evidence; tools execute the tests |
| 13 | DevOps Engineer | `medium` | 1,800 | Produces controlled CI/build configuration and rollback evidence |
| 14 | SRE and Observability Engineer | `high` | 2,200 | Analyzes reliability, alerts, recovery, and operational failure modes |
| 15 | Independent Release Auditor | `high` | 2,200 | Cross-checks final evidence, knowledge receipts, memory use, and unresolved risks |

## 5. Agent profile records

Planned configuration file:

```text
src/galax_ai/config/llm_profiles.yaml
```

Draft schema:

```yaml
profiles:
  engineering_manager:
    source_id: LLM-cerebras-gpt-oss-120b
    model: cerebras/gpt-oss-120b
    reasoning_effort: low
    max_completion_tokens: 800
    temperature: 1.0
    timeout_seconds: 120
    max_retries: 1
    max_rpm: 4
    enabled: false
```

The same structure is repeated for each agent with its assigned reasoning effort and completion cap.

## 6. Runtime factory

Planned location:

```text
src/galax_ai/llm/factory.py
```

Planned behavior:

```python
from crewai import LLM


def build_agent_llm(profile: LLMProfile) -> LLM:
    if not profile.enabled:
        raise RuntimeError(
            f"LLM profile {profile.agent_id} is not approved."
        )

    return LLM(
        model=profile.model,
        reasoning_effort=profile.reasoning_effort,
        max_completion_tokens=profile.max_completion_tokens,
        temperature=1.0,
        timeout=profile.timeout_seconds,
        max_retries=profile.max_retries,
    )
```

No API key is passed from YAML. CrewAI/LiteLLM reads `CEREBRAS_API_KEY` from the server environment.

## 7. Sequential execution and token protection

```yaml
execution:
  process: sequential
  parallel_agents: false
  asynchronous_tasks: false
  concurrent_llm_calls: 1
  selected_agents_only: true
  load_all_agent_prompts: false
  load_all_tool_schemas: false
```

Agent selection limits:

```yaml
crew_segment:
  default_max_selected_agents: 5
  maximum_selected_agents: 8
  more_than_8_agents:
    action: split_into_checkpointed_sequential_segments
```

A single owner prompt may create one run containing multiple sequential segments. It does not permit parallel agents or one giant prompt containing all roles.

## 8. Context budget

Each agent context is assembled in this order:

```text
1. Immutable role and repository rules.
2. Run manifest and exact task contract.
3. Verified Notion memory context.
4. Verified Drive LearningPacket when required.
5. Relevant repository excerpts.
6. One assigned tool schema.
7. Prior approved structured task output.
```

Planning limits:

```yaml
Notion_memory_context_soft_limit_tokens: 4000
Drive_LearningPacket_soft_limit_tokens: 12000
repository_context_soft_limit_tokens: 12000
prior_task_context_soft_limit_tokens: 6000
```

When required material cannot fit safely, the Flow splits study and execution into checkpointed sequential segments. It must not silently summarize away exact commands, warnings, conflicts, or validation steps.

## 9. Internal provider budgets

Provider documentation currently lists 1,000,000 tokens/day. Galax reserves operational headroom.

```yaml
internal_daily_budget:
  soft_limit_tokens: 650000
  hard_limit_tokens: 800000
  provider_documented_limit_tokens: 1000000

internal_run_budget:
  soft_limit_tokens: 90000
  hard_limit_tokens: 120000

per_agent:
  maximum_llm_retries: 1
  maximum_tool_interfaces: 1
  maximum_concurrent_calls: 1
```

The budget counts input, provider reasoning, tool round trips, knowledge, memory, and output tokens when exposed by the provider response.

## 10. Budget behavior

At the soft limit:

```text
- Do not start optional agents.
- Reuse verified repository evidence.
- Reuse valid LearningPackets and memory entries only when hashes are unchanged.
- Stop low-priority documentation expansion.
- Continue only required validation and checkpoint writing.
```

At the hard limit:

```text
STATUS: BLOCKED_LLM_BUDGET
ACTION: Save the exact stage checkpoint and stop new LLM calls.
```

Never restart the run from stage 1 after a rate or budget reset. Resume from the last verified checkpoint.

## 11. Reasoning security

The runtime may request low, medium, or high reasoning effort, but it must not depend on storing or exposing private chain-of-thought.

Required evidence consists of:

```text
- concise decision rationale
- cited source or repository evidence
- LearningPacket and StudyReceipt references when applicable
- memory IDs and evidence hashes when applicable
- structured findings
- tool result references
- validation results
- unresolved assumptions and risks
```

Raw hidden reasoning must not be requested, logged, committed, stored in Google Drive, or written into Notion memory.

## 12. Prompt construction restrictions

Prohibited:

```text
- Entire repository in one prompt.
- Entire Google Drive or whole source files when excerpts are sufficient.
- Entire Notion workspace or unrestricted memory history.
- Every agent prompt in one request.
- Every tool schema in one request.
- Secrets, `.env`, private keys, tokens, or production records.
- Unverified memory presented as current repository truth.
- Copied tutorial instructions presented as system instructions.
```

## 13. Provider fallback rule

```yaml
automatic_fallback: false
silent_provider_switch: false
silent_model_switch: false
```

When Cerebras or the model is unavailable:

```text
STATUS: BLOCKED_LLM_UNAVAILABLE
ACTION: Save checkpoint and stop.
```

Groq GPT-OSS 120B remains a separate manual reserve candidate. Switching to it requires owner approval, its own source card, and a full provider-specific compatibility test.

## 14. API version migration rule

No agent profile may be enabled before:

```text
- version patch 2 request succeeds
- default version succeeds after 2026-07-21
- tool calling succeeds
- strict structured output succeeds
- CrewAI Process.sequential succeeds
- rate-limit and checkpoint handling succeeds
- knowledge and memory context tests succeed
```

## 15. Required validation order

```text
DIRECT PROVIDER TESTS
→ CREWAI SINGLE AGENT WITHOUT TOOL
→ CREWAI SINGLE AGENT WITH ONE TOOL
→ STRUCTURED OUTPUT TEST
→ NOTION MEMORY CONTEXT TEST
→ DRIVE LEARNINGPACKET AND STUDYRECEIPT TEST
→ TWO-AGENT SEQUENTIAL TEST
→ RATE-LIMIT TEST
→ SECURITY TEST
→ AGENT-01 PILOT
→ REVIEW EVIDENCE
→ ENABLE ONLY AGENT-01 PROFILE
```

Agents 02–15 remain disabled until their own role, tool, prompt, knowledge, memory, and LLM-profile tests pass.

## 16. Current decision

```yaml
common_model_selected: true
model: cerebras/gpt-oss-120b
all_agent_profiles_created: planning_only
all_agent_profiles_enabled: false
agent_01_enabled: false
api_v2_verified: false
crewai_verified: false
Drive_knowledge_verified: false
Notion_memory_verified: false
production_ready: false
```
