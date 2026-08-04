# LLM Assignment Plan — Draft

**Status:** `DRAFT_MUTABLE`  
**Production status:** `NOT_APPROVED`  
**Crew process:** `Process.sequential`  
**Active agents:** `0`  
**Canonical remediation:** `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`

## 1. Corrected architecture decision

The active Galax plan does not use one model for every agent. Provider/model selection is based on the exact agent task, data class, tool schema, output contract, quality tests, and current free/account capacity.

```yaml
low_and_medium_bounded_private_work:
  primary_candidate: groq/openai/gpt-oss-20b
  hosted_fallback_candidate: cloudflare/@cf/openai/gpt-oss-20b
  optional_local_fallback: ollama/gpt-oss:20b

high_complexity_private_work:
  primary_candidate: groq/openai/gpt-oss-120b
  hosted_fallback_candidate: cloudflare/@cf/openai/gpt-oss-120b
  optional_local_fallback: none_until_quality_equivalent_profile_is_proven

public_or_fully_redacted_long_context:
  candidate: gemini/gemini-2.5-flash

conditional_research_only:
  candidate: mistral_free_mode_account_specific

rejected_active:
  - cerebras/gpt-oss-120b
  - openrouter/free
  - trial_credit_only_providers
```

No profile is enabled from documentation evidence alone.

## 2. CrewAI controls

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

CrewAI `planning=True` is not used because it creates an extra AgentPlanner call and defaults to an OpenAI planning model unless explicitly changed. CrewAI `reasoning=True` is not used because it creates an additional refinement loop and CrewAI documents that a reasoning-stage failure can continue into task execution. Galax uses provider-native `reasoning_effort` plus explicit structured planning tasks and deterministic Flow validation.

## 3. One agent, one LLM, one tool

```text
LLM != TOOL
```

For one active task:

```yaml
active_agent: exactly_one
active_llm_profile: exactly_one
assigned_tool_interface: exactly_one
```

Fallback profiles may be stored, but they are not simultaneously attached to the agent. Deterministic Flow may explicitly replace the active profile only from a safe checkpoint, only when no external mutation is active, and only when the alternate is approved for the same agent and data class.

Google Drive knowledge, Supabase memory, Notion mirroring, branch creation, checkpoints, agent selection, and draft PR creation remain trusted Flow/application infrastructure.

## 4. Canonical source records

```text
docs/sources/llms/groq-openai-gpt-oss-20b/SOURCE_CARD.md
docs/sources/llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md
docs/sources/llms/cloudflare-gpt-oss-20b/SOURCE_CARD.md
docs/sources/llms/cloudflare-gpt-oss-120b/SOURCE_CARD.md
docs/sources/llms/google-gemini-2.5-flash/SOURCE_CARD.md
docs/sources/llms/ollama-gpt-oss-20b/SOURCE_CARD.md
docs/sources/llms/cerebras-gpt-oss-120b/SOURCE_CARD.md  # rejected history
```

Provider facts are stored once in canonical source cards. Individual agent cards contain only the agent-specific profile, tests, limits, and decision.

## 5. Per-agent model allocation candidates

These are validation candidates, not approvals.

| ID | Agent | Primary candidate | Reasoning effort | Output cap | Hosted fallback candidate | Current status |
|---:|---|---|---|---:|---|---|
| 01 | Engineering Manager / Preflight | Groq GPT-OSS 20B | Low | 800 | Cloudflare GPT-OSS 20B | Disabled; tests missing |
| 02 | Product Requirements and Scope Lead | Groq GPT-OSS 20B | Medium | 1,600 | Cloudflare GPT-OSS 20B | Disabled; tests missing |
| 03 | Evidence and Capability Researcher | Gemini 2.5 Flash for public/redacted; Groq 120B for private scoped | High | 2,200 | Cloudflare 120B for private scoped | Disabled; gateway/tests missing |
| 04 | Solution and Systems Architect | Groq GPT-OSS 120B | High | 2,400 | Cloudflare GPT-OSS 120B | Disabled; tests missing |
| 05 | UX, UI, and Accessibility Designer | Groq GPT-OSS 20B | Medium | 1,600 | Cloudflare GPT-OSS 20B | Disabled; tests missing |
| 06 | Frontend Application Engineer | Groq GPT-OSS 20B initially | Medium | 2,000 | Cloudflare 20B; promote to tested 120B only if quality gate fails | Disabled; sandbox missing |
| 07 | Backend and API Engineer | Groq GPT-OSS 120B | High | 2,200 | Cloudflare GPT-OSS 120B | Disabled; sandbox missing |
| 08 | Data and Database Engineer | Groq GPT-OSS 120B | High | 2,200 | Cloudflare GPT-OSS 120B | Disabled; disposable DB missing |
| 09 | CrewAI and AI Systems Engineer | Groq GPT-OSS 120B | High | 2,400 | Cloudflare GPT-OSS 120B | Disabled; pinned integration missing |
| 10 | Integration and MCP Engineer | Groq GPT-OSS 120B | High | 2,200 | Cloudflare GPT-OSS 120B | Disabled; MCP security tests missing |
| 11 | Security, Privacy, and AI Safety Engineer | Groq GPT-OSS 120B | High | 2,400 | None until a sensitive-data fallback suite passes | Disabled; scanner gateway missing |
| 12 | QA and Test Automation Engineer | Groq GPT-OSS 20B | Medium | 1,800 | Cloudflare GPT-OSS 20B | Disabled; test sandbox missing |
| 13 | DevOps and CI/CD Engineer | Groq GPT-OSS 20B | Medium | 1,800 | Cloudflare GPT-OSS 20B | Disabled; build sandbox missing |
| 14 | SRE and Observability Engineer | Groq GPT-OSS 120B | High | 2,200 | Cloudflare 120B only with fully redacted telemetry | Disabled; telemetry gateway missing |
| 15 | Independent Release Auditor | Groq GPT-OSS 120B | High | 2,200 | Cloudflare GPT-OSS 120B | Disabled; evidence gateway missing |

A 20B failure against the defined quality suite may justify testing the 120B profile. It does not authorize silent promotion.

## 6. Provider capacity controls

### Groq GPT-OSS 20B and 120B

Current planning base limits recorded for both models:

```yaml
RPM: 30
RPD: 1000
TPM: 8000
TPD: 200000
```

The connected organization is the runtime source of truth. The current 8K TPM limit is the practical free-tier bottleneck despite a much larger model context. The 20B model is selected for potential latency/compute efficiency, not for a larger published free token quota.

### Cloudflare Workers AI

```yaml
free_allocation: 10000_neurons_per_day
quota_type: compute_based
```

The 20B model has lower published neuron rates than 120B, but the runtime must capture current official rates and remaining allocation. Do not convert the free allocation into a guaranteed number of requests.

### Gemini 2.5 Flash

Actual project/model RPM, TPM, and RPD must be captured from the connected account. The free profile receives public or fully redacted content only because Google states free-tier content may be used to improve its products.

### Ollama GPT-OSS 20B

Capacity is determined by actual model digest, RAM/VRAM, CPU/GPU, configured context, latency, and concurrency tests. No provider quota does not mean unlimited practical capacity.

## 7. Planned profile schema

```yaml
profiles:
  engineering_manager_groq_20b_v1:
    agent_id: engineering_manager
    source_id: LLM-groq-openai-gpt-oss-20b
    provider: groq
    model: groq/openai/gpt-oss-20b
    data_classification: private_scoped
    reasoning_effort: low
    max_completion_tokens: 800
    temperature: 1.0
    timeout_seconds: 120
    max_retries: 1
    enabled: false

  engineering_manager_cloudflare_20b_v1:
    agent_id: engineering_manager
    source_id: LLM-cloudflare-gpt-oss-20b
    provider: custom_openai
    model: '@cf/openai/gpt-oss-20b'
    data_classification: private_scoped
    reasoning_effort: low
    max_completion_tokens: 800
    timeout_seconds: 120
    max_retries: 1
    enabled: false
```

Provider-specific parameters must be explicitly mapped. Unsupported parameters must not be silently forwarded.

## 8. Runtime factory and hooks

```python
from crewai import LLM


def build_agent_llm(profile: LLMProfile) -> LLM:
    if not profile.enabled:
        raise RuntimeError(f"LLM profile {profile.profile_id} is not approved")
    return LLM(**profile.to_crewai_parameters())
```

A crew-scoped `PRE_MODEL_CALL` hook enforces profile identity, data classification, secret scanning, current capacity, input/output budget, and single-agent context. A `POST_MODEL_CALL` hook records usage and redacts prohibited output. Hook evidence is not sufficient by itself; the canonical invocation ledger and task guardrails remain authoritative.

Secrets are runtime-only:

```env
GROQ_API_KEY=
CLOUDFLARE_API_TOKEN=
CLOUDFLARE_ACCOUNT_ID=
GEMINI_API_KEY=
OLLAMA_BASE_URL=http://127.0.0.1:11434
```

## 9. Context assembly

```text
1. Active immutable repository rules and hashes.
2. Run manifest and exact task contract.
3. Bounded verified Supabase MemoryContext.
4. Verified Drive LearningPacket when required.
5. Relevant repository excerpts only.
6. Exactly one assigned tool schema.
7. Prior approved structured sequential output.
```

Prohibited:

```text
- full repository
- all 15 prompts
- all tool schemas
- secrets or credential files
- unrestricted memory
- raw hidden reasoning
- private content sent to the free Gemini profile
```

When required exact context exceeds the effective account/provider/hardware capacity, return `BLOCKED_CONTEXT_LIMIT` and split the task into checkpointed sequential segments.

## 10. Failover rule

```text
safe LLM-only stage fails
→ confirm no repository/database/upload/deployment mutation is active
→ write a canonical manual checkpoint
→ classify the provider failure
→ verify alternate profile approval for the same agent and data class
→ capture current alternate capacity
→ explicitly construct the alternate LLM
→ rerun only the safe stage
→ record provider/model/profile transition
```

No failover for prompt/schema defects, factual disagreement, security/permission failure, failed tests, repository conflicts, or missing human approval.

## 11. Required validation per profile

```text
LLM-001 authentication and exact model ID
LLM-002 system-instruction adherence
LLM-003 prohibited-action refusal
LLM-004 provider reasoning parameter behavior
LLM-005 correct single tool selection
LLM-006 exact Pydantic arguments
LLM-007 real invocation ID
LLM-008 tool-result round trip
LLM-009 structured task output
LLM-010 malformed output rejection
LLM-011 PRE/POST model-hook enforcement
LLM-012 token cap and usage recording
LLM-013 timeout behavior
LLM-014 HTTP 429/allocation behavior
LLM-015 context overflow stops safely
LLM-016 prompt-injection resistance
LLM-017 secret/data-classification protection
LLM-018 sequential context acceptance
LLM-019 self-diagnostic evidence consistency
LLM-020 agent-specific quality acceptance
```

Approval for one agent does not approve another agent, even with the same model.

## 12. Current decision

```yaml
Groq_20B_bounded_primary: selected_not_tested
Groq_120B_high_complexity_primary: selected_not_tested
Cloudflare_20B_bounded_fallback: selected_not_tested
Cloudflare_120B_high_complexity_fallback: selected_not_tested
Gemini_public_long_context: selected_not_tested
Ollama_local_20B: optional_not_tested
Mistral: conditional_research_only
Cerebras: rejected_trial_only
all_agent_profiles_enabled: false
production_ready: false
```
