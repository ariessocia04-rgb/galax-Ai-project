# Validated LLM Failover Rule — Draft

**Status:** `DRAFT_MUTABLE`  
**Primary candidate:** `cerebras/gpt-oss-120b`  
**Fallback candidate:** `groq/openai/gpt-oss-120b`

## 1. Core rule

A free-tier or trial LLM profile must have at least one separately validated fallback profile before it can be approved for Galax execution.

A fallback is not automatic model substitution. It is a deterministic Flow transition between two independently tested provider profiles.

## 2. Separate approval requirement

The same underlying model hosted by a different provider is treated as a different runtime capability.

Each provider profile must separately pass:

```text
authentication
exact model ID
system instruction handling
reasoning effort
single assigned tool selection
strict tool argument schema
actual tool-result round trip
strict structured output
usage accounting
timeout handling
HTTP 429 handling
context-limit handling
secret redaction
sequential task handoff
self-diagnostic consistency
```

## 3. Selected profiles

```yaml
primary:
  provider: Cerebras
  model: cerebras/gpt-oss-120b
  status: DISABLED_PENDING_TESTS

fallback:
  provider: Groq
  model: groq/openai/gpt-oss-120b
  status: DISABLED_PENDING_TESTS

tertiary_research_candidate:
  provider: OpenRouter
  model: openrouter/openai/gpt-oss-120b:free
  status: NOT_APPROVED_LOW_RELIABILITY_FREE_CAPACITY
```

## 4. Approved failover triggers

Failover may be considered only for:

```text
- provider connection failure
- provider service-unavailable response
- provider timeout after the one approved retry
- HTTP 429 when the required retry delay exceeds the run policy
- provider reports model temporarily unavailable
- primary account quota exhausted
```

Failover is prohibited for:

```text
- factual disagreement with the primary answer
- malformed output that indicates a prompt/schema defect
- security or permission failure
- tool authorization failure
- repository conflict
- failed tests
- blocked human approval
```

Those failures require correction, not provider switching.

## 5. Safe transition

```text
primary LLM failure
→ verify no external write transaction is active
→ save canonical checkpoint
→ record failure class and provider response
→ verify fallback profile status is APPROVED_FOR_AGENT
→ capture fallback account rate/context snapshot
→ rebuild the LLM client explicitly
→ rerun only the safe LLM stage
→ record fallback provider in every output and evidence record
```

## 6. Non-idempotent boundary

Never change providers in the middle of:

```text
- Git commit/tree update
- database migration
- external API mutation
- Notion write
- file upload
- deployment
- merge
```

The application must first reconcile the actual external state and resume from a safe checkpoint.

## 7. Parameter translation

Provider-specific unsupported parameters must be removed through an explicit profile, not silently dropped.

Groq documents that it is mostly, not fully, OpenAI-compatible and rejects unsupported fields with HTTP 400. Therefore, the Groq fallback profile must declare its exact supported parameter set.

```yaml
shared_required:
  temperature: provider_valid_value
  reasoning_effort: low_or_medium_or_high
  parallel_tool_calls: false
  strict_tool_schema: true
  structured_output: tested

prohibited_unless_tested:
  - logprobs
  - top_logprobs
  - logit_bias
  - n_greater_than_1
  - provider_builtin_browser_or_code_tools
```

Galax uses its own controlled tools and does not enable provider-built browser search or code execution in the initial profiles.

## 8. Capacity rule

The fallback cannot run solely because it has a model page with a large context window. The effective capacity is:

```text
minimum(
  provider model limit,
  connected account/plan limit,
  current rate-limit snapshot,
  Galax internal safety budget
)
```

## 9. Failure when both providers are unavailable

```yaml
status: BLOCKED_ALL_VALIDATED_LLMS_UNAVAILABLE
action:
  - preserve_checkpoint
  - preserve_repository_state
  - report_primary_failure
  - report_fallback_failure
  - do_not_use_unvalidated_provider
  - do_not_continue_agents
```

## 10. Revalidation

Any change to provider, model, LiteLLM, CrewAI, API version, prompt, tool schema, reasoning mode, structured-output schema, or rate/context limit returns the affected profile to `REVALIDATION_REQUIRED`.
