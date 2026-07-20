# LLM Source Card — Groq OpenAI GPT-OSS 120B

**Source ID:** `LLM-groq-openai-gpt-oss-120b`  
**Status:** `CANDIDATE_NOT_USED`  
**Approved for agents:** No  
**Verified:** 2026-07-20

## Identity

```yaml
provider: Groq
provider_type: hosted_inference_api
exact_model_id: openai/gpt-oss-120b
model_developer: OpenAI
model_family: gpt-oss
planned_agent_ids:
  - engineering_manager
cost_status: free_plan_available_but_limited
runtime_status: blocked_pending_tests
```

FreeLLM is not the provider for this model. It may only be recorded as a discovery directory. The planned connection, if approved, is directly from Galax to Groq.

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

- [CrewAI LLM concepts](https://docs.crewai.com/v1.15.4/en/concepts/llms.md)
- [CrewAI LLM connections](https://docs.crewai.com/v1.15.4/en/learn/llm-connections.md)
- [CrewAI annotations for LLM and tool separation](https://docs.crewai.com/v1.15.4/en/learn/using-annotations.md)
- [CrewAI sequential process](https://docs.crewai.com/v1.15.4/en/learn/sequential-process.md)

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
```

The exact limits for the connected Groq organization must be read from the Groq account because provider documentation states that account-specific exceptions may exist.

## Security and privacy notes

- Customer inference data is not retained by default except for limited reliability or abuse-monitoring circumstances described by Groq.
- Groq documents a Zero Data Retention control.
- Usage metadata is still retained.
- Repository secrets, credentials, personal data, and unrestricted private files must not be sent to the hosted model.
- Provider-managed browser search and code execution are disabled in the initial Galax design; Galax uses its own controlled tools.

## Compatibility risks

```text
- Groq is mostly, not fully, OpenAI compatible.
- Unsupported OpenAI parameters can return HTTP 400.
- CrewAI compatibility must be tested with the exact pinned CrewAI and provider-library versions.
- Tool calling and structured output must be tested separately and together.
- Rate-limit handling and checkpoint recovery must be tested.
```

## Required tests before status can become APPROVED

```text
- Direct authentication test.
- Exact model availability test.
- Plain completion test.
- System-message test.
- One local function-call test.
- JSON object test.
- JSON schema or Pydantic test.
- CrewAI single-agent test.
- CrewAI one-agent-one-tool test.
- Two-task sequential CrewAI test.
- 429 and retry-after handling test.
- Token accounting test.
- Secret-redaction test.
- Checkpoint resume test.
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
approved: false
```

This model must not be added to production `agents.yaml` while the status remains `CANDIDATE_NOT_USED`.
