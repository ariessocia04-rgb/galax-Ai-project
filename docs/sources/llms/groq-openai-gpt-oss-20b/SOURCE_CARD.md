# LLM Source Card — Groq OpenAI GPT-OSS 20B

**Source ID:** `LLM-groq-openai-gpt-oss-20b`  
**Status:** `SELECTED_FOR_LOW_AND_MEDIUM_COMPLEXITY_VALIDATION`  
**Approved for agents:** No  
**Verified:** 2026-07-20

## Identity

```yaml
provider: Groq
provider_type: hosted_inference_api
exact_model_id: openai/gpt-oss-20b
crewai_model_id: groq/openai/gpt-oss-20b
model_developer: OpenAI
model_family: gpt-oss
cost_status: durable_limited_free_plan_available
runtime_status: DISABLED_PENDING_PER_AGENT_CREWAI_TESTS
```

## Exact official links

- [Exact model page](https://console.groq.com/docs/model/openai/gpt-oss-20b)
- [Rate limits](https://console.groq.com/docs/rate-limits)
- [Local tool calling](https://console.groq.com/docs/tool-use/local-tool-calling)
- [OpenAI compatibility](https://console.groq.com/docs/openai)
- [Customer data and retention](https://console.groq.com/docs/your-data)
- [Model permissions](https://console.groq.com/docs/model-permissions)
- [CrewAI LLM concepts](https://docs.crewai.com/concepts/llms)
- [CrewAI versioned LLM source](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/llms.mdx)
- [OpenAI GPT-OSS repository](https://github.com/openai/gpt-oss)
- [OpenAI GPT-OSS license](https://github.com/openai/gpt-oss/blob/main/LICENSE)

## Provider-documented capability

```yaml
context_window_tokens: 131072
maximum_output_tokens: 65536
reasoning_effort:
  - low
  - medium
  - high
tool_use: true
json_object_mode: true
json_schema_mode: true
free_plan_base_limits:
  requests_per_minute: 30
  requests_per_day: 1000
  tokens_per_minute: 8000
  tokens_per_day: 200000
```

The actual connected Groq organization limits are the runtime source of truth. A 131K model context does not permit a 131K free-tier request when the active token-per-minute limit is 8K.

## Intended Galax use

This model is a validation candidate for bounded low- and medium-complexity tasks such as:

```text
- Agent 01 preflight interpretation
- Agent 02 requirements transformation
- Agent 05 bounded UX specification
- Agent 12 routine test triage
- Agent 13 bounded build configuration work
```

It is not automatically accepted for architecture, security, database migration, complex integration, or final release audit work. Those tasks require separate quality tests and may require the 120B profile.

## Data handling decision

Groq states that inference customer data is not retained by default except for limited reliability/abuse circumstances or features requiring retention. Groq also provides a Zero Data Retention control and states that inputs and outputs are not used for model training unless the customer explicitly permits it.

Galax must still:

```text
- enable the strongest available data controls;
- remove credentials, secrets, personal data, and unrelated repository content;
- send only task-scoped excerpts;
- record only usage metadata and hashes in Galax evidence;
- prohibit provider-hosted browser or code-execution tools.
```

## CrewAI candidate profile

```python
from crewai import LLM

llm = LLM(
    model="groq/openai/gpt-oss-20b",
    reasoning_effort="low",
    temperature=1.0,
    timeout=120,
    max_retries=1,
)
```

Dependency candidate:

```bash
uv add 'crewai[litellm]'
```

## Important limitations

```text
- The free token limits are currently the same published base limits as GPT-OSS 120B.
- The main expected benefit is lower latency and compute cost, not a larger free token quota.
- Groq is mostly, not completely, OpenAI compatible.
- Unsupported request fields can return HTTP 400.
- Tool calling, typed tool results, and strict task output must pass through the exact CrewAI/LiteLLM path.
- The model must not be approved for an agent merely because the same model passed for another agent.
```

## Required tests

```text
- authentication and exact model availability
- system-instruction adherence
- low/medium/high reasoning parameter behavior
- one assigned CrewAI tool selection
- valid arguments for the exact Pydantic schema
- actual invocation ID and tool-result round trip
- output_pydantic or output_json behavior
- result_as_answer behavior where selected
- PRE_MODEL_CALL and PRE_TOOL_CALL policy enforcement
- unsupported-parameter rejection
- timeout and HTTP 429 checkpoint behavior
- token usage and current account-limit capture
- secret/data-classification protection
- two-agent Process.sequential handoff
- agent-specific quality acceptance suite
```

## Current decision

```yaml
identity_verified: true
limited_free_plan_verified: true
CrewAI_LiteLLM_path_found: true
privacy_review_completed: true
CrewAI_live_test_completed: false
tool_calling_live_test_completed: false
structured_output_live_test_completed: false
approved_for_any_agent: false
```
