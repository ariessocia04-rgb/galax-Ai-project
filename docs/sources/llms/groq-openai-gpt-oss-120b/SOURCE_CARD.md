# LLM Source Card — Groq OpenAI GPT-OSS 120B

**Source ID:** `LLM-groq-openai-gpt-oss-120b`  
**Status:** `SELECTED_FOR_VALIDATION_AS_PRIVATE_REPOSITORY_PRIMARY`  
**Approved for agents:** No  
**Verified:** 2026-07-20

## Identity

```yaml
provider: Groq
provider_type: hosted_inference_api
exact_model_id: openai/gpt-oss-120b
crewai_model_id: groq/openai/gpt-oss-120b
model_developer: OpenAI
model_family: gpt-oss
cost_status: durable_free_plan_available_but_limited
runtime_status: DISABLED_PENDING_CREWAI_TESTS
```

## Exact official links

- [Exact model page](https://console.groq.com/docs/model/openai/gpt-oss-120b)
- [Rate limits](https://console.groq.com/docs/rate-limits)
- [Local tool calling](https://console.groq.com/docs/tool-use/local-tool-calling)
- [OpenAI compatibility](https://console.groq.com/docs/openai)
- [Customer data and retention](https://console.groq.com/docs/your-data)
- [Groq services agreement](https://console.groq.com/docs/legal/services-agreement)
- [CrewAI LLM concepts](https://docs.crewai.com/concepts/llms)
- [CrewAI versioned LLM source](https://github.com/crewAIInc/crewAI/blob/main/docs/v1.15.4/en/concepts/llms.mdx)

## Provider-documented capacity

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

The actual connected organization limits are the runtime source of truth.

## Data handling decision

Groq states that inference customer data is not retained by default except for limited reliability/abuse circumstances or features requiring retention. It also provides a Zero Data Retention control. Groq states that inputs/outputs are not used for model training unless the customer explicitly permits it.

Galax must enable the strongest available data controls and still redact secrets, credentials, customer personal data, and unrelated private repository content.

## CrewAI candidate profile

```python
from crewai import LLM

llm = LLM(
    model="groq/openai/gpt-oss-120b",
    reasoning_effort="low",
    temperature=1.0,
    timeout=120,
    max_retries=1,
)
```

Dependency:

```bash
uv add 'crewai[litellm]'
```

## Important limitations

```text
- 8K tokens/minute is the main throughput bottleneck despite the 131K model context.
- Groq is mostly, not completely, OpenAI compatible.
- Unsupported parameters can produce HTTP 400.
- Tool calling and strict structured output must be tested through CrewAI/LiteLLM.
- Provider built-in browser/code tools remain disabled; Galax uses controlled tools.
- No agent may be enabled from documentation evidence alone.
```

## Required tests

```text
- exact model authentication and completion
- system instruction handling
- low/medium/high reasoning
- one Galax tool call with valid arguments
- actual tool-result round trip
- structured AgentTaskResult output
- unsupported parameter rejection
- timeout and HTTP 429 checkpoint behavior
- exact usage/rate header recording
- two-agent Process.sequential handoff
- prompt-injection and secret-redaction tests
```

## Current decision

```yaml
identity_verified: true
permanent_free_plan_verified: true
privacy_review_completed: true
CrewAI_provider_path_found: true
CrewAI_live_test_completed: false
tool_calling_live_test_completed: false
structured_output_live_test_completed: false
active_for_agents: false
approved: false
```
