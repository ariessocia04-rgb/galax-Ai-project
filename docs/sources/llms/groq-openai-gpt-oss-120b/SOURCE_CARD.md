# LLM Source Card — Groq OpenAI GPT-OSS 120B

**Source ID:** `LLM-groq-openai-gpt-oss-120b`  
**Status:** `RESERVE_CANDIDATE_NOT_ACTIVE`  
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
planned_agent_ids: []
manual_reserve_for:
  - cerebras/gpt-oss-120b
cost_status: free_plan_available_but_limited
runtime_status: blocked_pending_tests
automatic_fallback: false
```

Groq is a direct provider. FreeLLM and other provider directories may be discovery sources only.

## Exact official links

### Provider and model

- [Exact Groq model page: openai/gpt-oss-120b](https://console.groq.com/docs/model/openai/gpt-oss-120b)
- [Groq API reference](https://console.groq.com/docs/api-reference)
- [Groq OpenAI compatibility](https://console.groq.com/docs/openai)
- [Groq local tool calling](https://console.groq.com/docs/tool-use/local-tool-calling)
- [Groq model permissions](https://console.groq.com/docs/model-permissions)

### Limits and cost

- [Groq rate limits](https://console.groq.com/docs/rate-limits)
- [Groq spend limits](https://console.groq.com/docs/spend-limits)

### Privacy and data

- [Groq customer data and retention](https://console.groq.com/docs/your-data)

### Model source and license

- [Official OpenAI GPT-OSS repository](https://github.com/openai/gpt-oss)
- [Official GPT-OSS license](https://github.com/openai/gpt-oss/blob/main/LICENSE)
- [Official GPT-OSS usage policy](https://github.com/openai/gpt-oss/blob/main/USAGE_POLICY)

### CrewAI compatibility

- [CrewAI LLM concepts](https://docs.crewai.com/concepts/llms)
- [CrewAI annotations for LLM and tool separation](https://docs.crewai.com/learn/using-annotations)
- [CrewAI sequential process](https://docs.crewai.com/learn/sequential-process)

## Provider-documented capacity

```yaml
context_window_tokens: 131072
maximum_output_tokens: 65536
capabilities:
  - tool_use
  - json_object_mode
  - json_schema_mode
  - reasoning
free_plan_documented_limits:
  requests_per_minute: 30
  requests_per_day: 1000
  tokens_per_minute: 8000
  tokens_per_day: 200000
monthly_token_limit: NOT_DOCUMENTED_AS_A_FIXED_FREE_QUOTA
```

The exact limits for the connected Groq organization must be read from the account because provider documentation states that exceptions may exist.

## Security and privacy notes

- Customer inference data is not retained by default except for the limited cases described by Groq.
- Groq documents a Zero Data Retention setting.
- Usage metadata is retained.
- Repository secrets, credentials, personal data, and unrestricted private files must not be sent to the hosted model.
- Provider-managed browser search and code execution are disabled in the Galax design.

## Why it is not active

Cerebras GPT-OSS 120B is being validated first because its documented free token and request quotas are larger. Using two active providers during the initial build would increase integration, testing, monitoring, and failure-handling complexity.

Groq may be selected later only through this sequence:

```text
owner approves provider switch
→ source card revalidated
→ Groq-specific live tests pass
→ affected agent profiles updated
→ no automatic fallback enabled
```

## Compatibility risks

```text
- Groq is mostly, not fully, OpenAI compatible.
- Unsupported OpenAI parameters can return HTTP 400.
- CrewAI compatibility must be tested with exact pinned versions.
- Tool calling and structured output must be tested separately and together.
- Rate-limit handling and checkpoint recovery must be tested.
```

## Current decision

```yaml
identity_verified: true
official_links_recorded: true
free_plan_verified: true
crewai_runtime_verified: false
tool_calling_verified: false
structured_output_verified: false
security_tests_passed: false
active_for_agents: false
automatic_fallback: false
approved: false
```
