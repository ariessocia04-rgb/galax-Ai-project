# Validated LLM Routing and Failover Rule — Draft

**Status:** `DRAFT_MUTABLE`  
**Private repository primary candidate:** `groq/openai/gpt-oss-120b`  
**Private hosted fallback candidate:** Cloudflare `@cf/openai/gpt-oss-120b`  
**Public/redacted long-context candidate:** `gemini/gemini-2.5-flash`  
**Optional local fallback candidate:** `ollama/gpt-oss:20b`  
**Rejected active candidate:** `cerebras/gpt-oss-120b` — trial only

## 1. Core rule

A provider profile is not approved merely because CrewAI can construct the LLM or the provider publishes a free plan. Every provider/model/agent combination must be separately tested.

```text
NO SILENT PROVIDER SWITCH
NO UNVALIDATED FALLBACK
NO TRIAL-ONLY ACTIVE PROVIDER
```

CrewAI does not provide the complete Galax failover policy automatically. The deterministic Flow owns provider selection, checkpointing, and safe retry boundaries.

## 2. Active routing classes

### Private repository and code tasks

```yaml
primary:
  provider: Groq
  model: groq/openai/gpt-oss-120b
  status: DISABLED_PENDING_TESTS

hosted_fallback:
  provider: Cloudflare Workers AI
  model: '@cf/openai/gpt-oss-120b'
  connection: custom_OpenAI_compatible
  status: DISABLED_PENDING_TESTS

local_fallback:
  provider: Ollama
  model: ollama/gpt-oss:20b
  status: DISABLED_PENDING_HARDWARE_AND_AGENT_TESTS
```

### Public or fully redacted long-context tasks

```yaml
candidate:
  provider: Google Gemini API
  model: gemini/gemini-2.5-flash
  status: DISABLED_PENDING_TESTS
  private_repository_content: prohibited
```

Gemini free-tier content may be used to improve Google products. It is not a failover for confidential repository work.

## 3. Rejected providers

```yaml
cerebras/gpt-oss-120b:
  reason: current_official_offer_is_free_trial_credit
openrouter/free:
  reason: selected_model_can_change_and_free_quota_is_low
trial_credit_only_providers:
  reason: not_durable_for_Galax_runtime
```

Historical source cards remain for traceability but must not appear in active agent configuration.

## 4. Separate approval requirement

Every profile must independently pass:

```text
authentication
exact model ID
current free-plan/account capacity
system instruction handling
reasoning behavior
single assigned tool selection
strict tool argument schema
actual tool-result round trip
structured output
usage accounting
timeout handling
HTTP 429 handling
context-limit handling
secret redaction
sequential task handoff
self-diagnostic consistency
privacy and data classification
```

The same GPT-OSS model hosted by Groq, Cloudflare, or Ollama is three different runtime capabilities.

## 5. Approved failover triggers

Failover may be considered only for:

```text
- provider connection failure
- service unavailable response
- timeout after one approved retry
- HTTP 429 when Retry-After exceeds the run policy
- model temporarily unavailable
- primary account quota exhausted
```

Failover is prohibited for:

```text
- factual disagreement
- malformed output caused by prompt/schema defect
- security or permission failure
- repository conflict
- failed tests
- blocked human approval
- an active non-idempotent external operation
```

Those failures require correction, not provider switching.

## 6. Safe transition

```text
primary LLM failure
→ verify no repository/database/external write is active
→ save canonical checkpoint
→ record provider response and failure class
→ verify alternate profile is APPROVED_FOR_AGENT
→ capture alternate account capacity snapshot
→ verify data-classification compatibility
→ instantiate alternate LLM explicitly
→ rerun only the safe LLM stage
→ record provider/model/profile in evidence
```

## 7. Non-idempotent boundary

Never switch providers in the middle of:

```text
Git tree/commit/ref update
database mutation or migration
Notion or Drive write
external API mutation
file upload
deployment
merge
```

The Flow must reconcile real external state before resuming.

## 8. Provider-specific restrictions

### Groq

```text
- Keep within current organization RPM/RPD/TPM/TPD.
- Do not send unsupported OpenAI parameters.
- Use Galax tools, not provider built-in browser/code tools.
- Test strict tool and structured-output behavior separately and together.
```

### Cloudflare Workers AI

```text
- Use a tested custom OpenAI-compatible CrewAI profile.
- Treat 10,000 neurons/day as compute allocation, not a fixed token quota.
- Capture remaining allocation before failover.
- Test tool-call round trips and JSON schemas through the exact endpoint.
```

### Gemini free tier

```text
- Public or fully redacted data only.
- Capture actual AI Studio RPM/TPM/RPD.
- Do not use as private-repository failover.
```

### Ollama local

```text
- Require hardware qualification and exact model digest.
- Bind only to approved local/internal interfaces.
- Enforce timeout, context, memory, and latency ceilings.
- Do not assume 128K context is usable on the available hardware.
```

## 9. Capacity rule

Effective capacity is always:

```text
minimum(
  provider/model limit,
  connected account or local hardware limit,
  current rate/allocation snapshot,
  data-classification policy,
  Galax internal token budget
)
```

## 10. Failure when no profile is available

```yaml
status: BLOCKED_ALL_VALIDATED_LLMS_UNAVAILABLE
action:
  - preserve_checkpoint
  - preserve_repository_state
  - report_each_provider_failure
  - do_not_use_unvalidated_provider
  - do_not_continue_agents
```

## 11. Revalidation

Any change to provider, model, CrewAI, LiteLLM/provider SDK, base URL, API behavior, prompt, tool schema, privacy setting, reasoning mode, structured-output schema, rate limit, free allocation, or local model digest returns the affected profile to:

```text
REVALIDATION_REQUIRED
```

## 12. Current status

```yaml
Groq_profile: SELECTED_NOT_TESTED
Cloudflare_profile: SELECTED_NOT_TESTED
Gemini_public_profile: SELECTED_NOT_TESTED
Ollama_local_profile: OPTIONAL_NOT_TESTED
Cerebras_profile: REJECTED_TRIAL_ONLY
native_CrewAI_failover_found: false
Flow_failover_implemented: false
agents_enabled: 0
```
