# LLM Assignment Plan — Draft

**Status:** `DRAFT_MUTABLE`  
**Production status:** `NOT_APPROVED`  
**Crew process:** `Process.sequential`  
**Active agents:** `0`

## 1. Corrected architecture decision

The earlier one-provider Cerebras plan is superseded because current official pricing classifies Cerebras access as trial credits. Trial-only providers are not active Galax candidates.

Galax now uses separately validated routing classes:

```yaml
private_repository_and_code:
  primary_candidate: groq/openai/gpt-oss-120b
  hosted_fallback_candidate: cloudflare/@cf/openai/gpt-oss-120b
  optional_local_fallback: ollama/gpt-oss:20b

public_or_fully_redacted_long_context:
  candidate: gemini/gemini-2.5-flash

conditional_research_only:
  candidate: mistral/mistral-small-2603

rejected_active:
  - cerebras/gpt-oss-120b
  - openrouter/free
  - trial_credit_only_providers
```

No provider profile is enabled until it passes per-agent tests.

## 2. One agent, one tool remains unchanged

```text
LLM != TOOL
```

Every active agent has:

```yaml
active_llm_profile: exactly_one
assigned_tool_interface: exactly_one
```

A validated fallback is not simultaneously attached to the agent. The deterministic Flow replaces the active LLM profile only from a safe checkpoint after an approved provider failure.

Google Drive knowledge, Supabase memory, and optional Notion mirror are controlled Flow infrastructure, not additional agent tools.

## 3. Canonical source records

```text
docs/sources/llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md
docs/sources/llms/cloudflare-gpt-oss-120b/SOURCE_CARD.md
docs/sources/llms/google-gemini-2.5-flash/SOURCE_CARD.md
docs/sources/llms/ollama-gpt-oss-20b/SOURCE_CARD.md
docs/sources/llms/cerebras-gpt-oss-120b/SOURCE_CARD.md  # rejected history
```

Do not copy provider facts into 15 agent cards. Agent cards link to canonical source cards and define only their task-specific profile.

## 4. Per-agent reasoning and output ceilings

These are Galax internal ceilings, not provider capacity claims.

| ID | Agent | Reasoning | Maximum output tokens | Default data class |
|---:|---|---|---:|---|
| 01 | Engineering Manager / Preflight | Low | 800 | Private scoped repository metadata |
| 02 | Product Requirements Lead | Medium | 1,600 | Private owner requirements |
| 03 | Evidence Researcher | High | 2,200 | Public sources and redacted owner material |
| 04 | Solution Architect | High | 2,400 | Private scoped architecture context |
| 05 | UX and Accessibility Designer | Medium | 1,600 | Private scoped design context |
| 06 | Frontend Engineer | Medium | 2,000 | Private scoped code |
| 07 | Backend/API Engineer | High | 2,200 | Private scoped code |
| 08 | Database Engineer | High | 2,200 | Private schema and disposable test data |
| 09 | CrewAI Engineer | High | 2,400 | Private CrewAI/config source |
| 10 | Integration/MCP Engineer | High | 2,200 | Private adapters and public protocol docs |
| 11 | Security and Privacy Engineer | High | 2,400 | Sensitive scoped security evidence |
| 12 | QA and Test Engineer | Medium | 1,800 | Private scoped tests/results |
| 13 | DevOps Engineer | Medium | 1,800 | Private CI/build configuration |
| 14 | SRE and Observability Engineer | High | 2,200 | Redacted telemetry only |
| 15 | Independent Release Auditor | High | 2,200 | Private bounded evidence package |

## 5. Default provider class by agent

### Private repository agents

Agents 01, 02, 04–15 default to the Groq candidate profile because Groq provides a direct CrewAI/LiteLLM path, a durable free plan, tool calling, structured output modes, and stronger free-plan data handling than Gemini.

```yaml
primary_source_id: LLM-groq-openai-gpt-oss-120b
primary_model: groq/openai/gpt-oss-120b
status: DISABLED_PENDING_PER_AGENT_TESTS
```

### Research agent

Agent 03 may use either:

```yaml
private_or_owner_scoped_research:
  model: groq/openai/gpt-oss-120b

public_large_learning_packet:
  model: gemini/gemini-2.5-flash
  restriction: public_or_fully_redacted_only
```

Only one profile is active for a task.

### Hosted fallback

```yaml
source_id: LLM-cloudflare-gpt-oss-120b
model: '@cf/openai/gpt-oss-120b'
connection: custom_OpenAI_compatible
status: DISABLED_PENDING_PER_AGENT_TESTS
```

### Local fallback

```yaml
source_id: LLM-ollama-gpt-oss-20b
model: ollama/gpt-oss:20b
status: DISABLED_PENDING_HARDWARE_AND_PER_AGENT_TESTS
```

## 6. Planned profile schema

```yaml
profiles:
  engineering_manager_groq_v1:
    agent_id: engineering_manager
    source_id: LLM-groq-openai-gpt-oss-120b
    provider: groq
    model: groq/openai/gpt-oss-120b
    data_classification: private_scoped
    reasoning_effort: low
    max_completion_tokens: 800
    temperature: 1.0
    timeout_seconds: 120
    max_retries: 1
    enabled: false

  engineering_manager_cloudflare_v1:
    agent_id: engineering_manager
    source_id: LLM-cloudflare-gpt-oss-120b
    provider: custom_openai
    model: '@cf/openai/gpt-oss-120b'
    data_classification: private_scoped
    reasoning_effort: low
    max_completion_tokens: 800
    timeout_seconds: 120
    max_retries: 1
    enabled: false
```

Fallback profiles are stored but not attached simultaneously to an agent.

## 7. Runtime factory rule

```python
from crewai import LLM


def build_agent_llm(profile: LLMProfile) -> LLM:
    if not profile.enabled:
        raise RuntimeError(
            f"LLM profile {profile.profile_id} is not approved."
        )

    return LLM(**profile.to_crewai_parameters())
```

Provider-specific parameters are generated explicitly. Unsupported parameters must not be silently forwarded.

Secrets are read only from the runtime secret store:

```env
GROQ_API_KEY=
CLOUDFLARE_API_TOKEN=
CLOUDFLARE_ACCOUNT_ID=
GEMINI_API_KEY=
OLLAMA_BASE_URL=http://127.0.0.1:11434
```

## 8. Sequential execution and token protection

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

Default segment maximum is five selected agents; hard maximum is eight. Larger runs are split into checkpointed sequential segments.

## 9. Context assembly

```text
1. Immutable repository rules.
2. Run manifest and exact task contract.
3. Bounded verified Supabase MemoryContext.
4. Verified Drive LearningPacket when required.
5. Relevant repository excerpts.
6. One assigned tool schema.
7. Prior approved structured task output.
```

Never send the whole repository, all agent prompts, all tool schemas, secrets, or unrestricted memory.

Provider context windows do not override TPM, daily allocation, account limits, privacy, or Galax internal budgets.

## 10. Provider capacity controls

### Groq

```yaml
base_free_limits:
  RPM: 30
  RPD: 1000
  TPM: 8000
  TPD: 200000
```

The 8K TPM limit means large context must be split even though the model advertises 131K context.

### Cloudflare

```yaml
free_allocation: 10000_neurons_per_day
```

Allocation is compute-based. The Flow estimates input/output neuron consumption and captures the current dashboard state.

### Gemini

Actual RPM/TPM/RPD must be captured from AI Studio. Free-tier content is public/redacted only.

### Ollama

Capacity is determined by actual local hardware, model digest, configured context, and measured latency.

## 11. Failover rule

```text
safe LLM-only stage fails
→ verify no external write is active
→ checkpoint
→ classify failure
→ verify alternate profile is approved for agent and data class
→ capture alternate capacity
→ instantiate alternate explicitly
→ rerun safe stage
→ record provider/model switch
```

No automatic switch occurs during commits, database writes, uploads, deployment, or merge.

## 12. Required validation order

```text
PIN DEPENDENCIES
→ DIRECT PROVIDER OR LOCAL MODEL TEST
→ CREWAI SINGLE AGENT WITHOUT TOOL
→ SINGLE AGENT WITH ONE TOOL
→ TOOL RESULT ROUND TRIP
→ STRUCTURED OUTPUT
→ DATA CLASSIFICATION TEST
→ RATE/ALLOCATION/CONTEXT TEST
→ TWO-AGENT SEQUENTIAL TEST
→ CHECKPOINTED FAILOVER TEST
→ SECURITY TEST
→ ENABLE ONE AGENT PROFILE ONLY
```

## 13. Current decision

```yaml
Groq_primary_candidate: selected_not_tested
Cloudflare_hosted_fallback: selected_not_tested
Gemini_public_long_context: selected_not_tested
Ollama_local_fallback: optional_not_tested
Mistral: conditional_research_only
Cerebras: rejected_trial_only
all_agent_profiles_enabled: false
production_ready: false
```
