# LLM Source Card — Cerebras GPT-OSS 120B

**Source ID:** `LLM-cerebras-gpt-oss-120b`  
**Status:** `SELECTED_FOR_VALIDATION`  
**Approved for agents:** No  
**Verified:** 2026-07-20  
**Discovery source:** [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources)

## Identity

```yaml
provider: Cerebras Inference
provider_type: hosted_inference_api
provider_model_id: gpt-oss-120b
crewai_model_id: cerebras/gpt-oss-120b
model_developer: OpenAI
model_family: gpt-oss
license: Apache-2.0
cost_status: free_plan_available_but_limited
runtime_status: blocked_pending_tests
```

## Exact official links

### Provider and model

- [Cerebras Inference documentation](https://inference-docs.cerebras.ai/)
- [Supported models](https://inference-docs.cerebras.ai/models/overview)
- [Public model metadata](https://inference-docs.cerebras.ai/api-reference/models/public-models)
- [Chat Completions API](https://inference-docs.cerebras.ai/api-reference/chat-completions)
- [Authentication](https://inference-docs.cerebras.ai/api-reference/authentication)

### Capabilities

- [Tool calling](https://inference-docs.cerebras.ai/capabilities/tool-use)
- [Structured outputs](https://inference-docs.cerebras.ai/capabilities/structured-outputs)
- [Prompt caching](https://inference-docs.cerebras.ai/capabilities/prompt-caching)

### Limits, changes, and security

- [Rate limits](https://inference-docs.cerebras.ai/support/rate-limits)
- [Change log](https://inference-docs.cerebras.ai/support/change-log)
- [Cerebras Cloud privacy](https://cloud.cerebras.ai/privacy)
- [Cerebras terms of service](https://www.cerebras.ai/terms-of-service)
- [Cerebras cloud data ownership statement](https://www.cerebras.ai/cloud)

### Model source and license

- [Official OpenAI GPT-OSS repository](https://github.com/openai/gpt-oss)
- [Official GPT-OSS license](https://github.com/openai/gpt-oss/blob/main/LICENSE)
- [Official GPT-OSS usage policy](https://github.com/openai/gpt-oss/blob/main/USAGE_POLICY)

### CrewAI compatibility

- [CrewAI LLM configuration](https://docs.crewai.com/concepts/llms)
- [CrewAI LLM annotations](https://docs.crewai.com/learn/using-annotations)
- [CrewAI sequential process](https://docs.crewai.com/learn/sequential-process)
- [CrewAI provider constants source](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/lib/crewai/src/crewai/constants.py)
- [CrewAI Cerebras model discovery source](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/lib/cli/src/crewai_cli/model_catalog.py)
- [LiteLLM Cerebras adapter source](https://github.com/BerriAI/litellm/blob/bd44c9e305b89526d4c5d773ee39ca935561b9c8/litellm/llms/cerebras/chat.py)

## Verified capacity

```yaml
context_window_tokens: 131072
maximum_completion_tokens: 40960
reasoning: true
reasoning_effort:
  - low
  - medium
  - high
function_calling: true
structured_outputs: true
json_schema_strict: true
json_mode: true
parallel_tool_calls: false
vision: false
```

## Documented free-plan limits

```yaml
requests_per_minute: 30
requests_per_hour: 900
requests_per_day: 14400
tokens_per_minute: 64000
tokens_per_hour: 1000000
tokens_per_day: 1000000
monthly_token_limit: NOT_DOCUMENTED_AS_A_FIXED_FREE_QUOTA
```

The runtime must read the actual connected account limits before every run group. The repository values are planning ceilings, not permanent provider guarantees.

## Data handling decision

```yaml
inputs_outputs_retained: provider_states_no
used_for_model_training: provider_terms_state_no
usage_metadata: may_be_collected
secrets_allowed_in_prompts: false
unrestricted_repository_context: false
customer_or_production_data: false
```

## Planned CrewAI configuration

This configuration is not enabled until the validation suite passes:

```python
from crewai import LLM


def build_cerebras_llm(
    *,
    reasoning_effort: str,
    max_completion_tokens: int,
) -> LLM:
    return LLM(
        model="cerebras/gpt-oss-120b",
        reasoning_effort=reasoning_effort,
        max_completion_tokens=max_completion_tokens,
        temperature=1.0,
        timeout=120,
        max_retries=1,
    )
```

Required environment variable:

```env
CEREBRAS_API_KEY=
```

Required project dependency:

```bash
uv add 'crewai[litellm]'
```

## API version transition

Cerebras announced that version patch 2 becomes the default on 2026-07-21. The following test must run before approval:

```python
extra_headers = {
    "X-Cerebras-Version-Patch": "2",
}
```

The exact way this header is passed through the pinned CrewAI/LiteLLM combination must be proven by a live test. It must not be assumed.

## Required validation suite

```text
LLM-CER-001 API key loaded only from environment.
LLM-CER-002 Exact model appears in provider model list.
LLM-CER-003 Plain system/user completion succeeds.
LLM-CER-004 Version patch 2 request succeeds.
LLM-CER-005 Version 2 default succeeds after 2026-07-21.
LLM-CER-006 Low reasoning effort succeeds.
LLM-CER-007 Medium reasoning effort succeeds.
LLM-CER-008 High reasoning effort succeeds.
LLM-CER-009 One function tool call returns valid JSON arguments.
LLM-CER-010 Tool result round-trip succeeds.
LLM-CER-011 Parallel tool calls remain disabled.
LLM-CER-012 Strict JSON schema output validates.
LLM-CER-013 Pydantic task output validates through CrewAI.
LLM-CER-014 CrewAI single-agent run succeeds.
LLM-CER-015 CrewAI one-agent-one-tool run succeeds.
LLM-CER-016 Two-task Process.sequential run preserves order.
LLM-CER-017 Task context passes only approved output.
LLM-CER-018 Token usage is recorded.
LLM-CER-019 Account rate limits are read and recorded.
LLM-CER-020 HTTP 429 saves checkpoint and stops.
LLM-CER-021 Retry count never exceeds one.
LLM-CER-022 Timeout stops safely.
LLM-CER-023 Secret redaction prevents credential submission.
LLM-CER-024 Prompt injection in repository content is ignored.
LLM-CER-025 Provider or model change triggers revalidation.
```

Approval requires 25 of 25 tests.

## Current decision

```yaml
identity_verified: true
official_sources_recorded: true
crewai_provider_path_found: true
free_limits_verified_from_docs: true
reasoning_capability_verified_from_docs: true
tool_calling_verified_from_docs: true
structured_output_verified_from_docs: true
privacy_review_completed: true
live_api_test_completed: false
crewai_integration_test_completed: false
api_v2_test_completed: false
approved: false
```
