# LLM Source Card — Cloudflare Workers AI GPT-OSS 20B

**Source ID:** `LLM-cloudflare-gpt-oss-20b`  
**Status:** `SELECTED_FOR_LOW_AND_MEDIUM_COMPLEXITY_FALLBACK_VALIDATION`  
**Approved for agents:** No  
**Verified:** 2026-07-20

## Identity

```yaml
provider: Cloudflare Workers AI
exact_model_id: '@cf/openai/gpt-oss-20b'
crewai_connection: custom_OpenAI_compatible_endpoint
model_developer: OpenAI
context_window_tokens: 128000
function_calling: true
reasoning: true
structured_JSON: true
free_allocation: 10000_neurons_per_day
runtime_status: DISABLED_PENDING_PER_AGENT_TESTS
```

## Official links

- [Model page](https://developers.cloudflare.com/workers-ai/models/gpt-oss-20b/)
- [OpenAI-compatible API](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/)
- [Function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/)
- [Traditional function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/traditional/)
- [JSON mode and schemas](https://developers.cloudflare.com/workers-ai/features/json-mode/)
- [Free allocation and pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/)
- [Customer data usage](https://developers.cloudflare.com/workers-ai/platform/data-usage/)
- [CrewAI LLM configuration](https://docs.crewai.com/concepts/llms)
- [OpenAI GPT-OSS repository](https://github.com/openai/gpt-oss)
- [OpenAI GPT-OSS license](https://github.com/openai/gpt-oss/blob/main/LICENSE)

## Free-allocation interpretation

Cloudflare provides a daily neuron allocation, not a guaranteed request or token count. The 20B model uses fewer published neurons per million input/output tokens than the 120B model, but real mixed requests consume both input and output allocation.

Galax must read current official pricing and capture the connected account's remaining allocation before selecting this fallback. Repository planning numbers cannot be treated as a permanent guarantee.

## Intended Galax use

This is a hosted fallback candidate for low- and medium-complexity private tasks only after the exact agent profile passes its own tests. It is not simultaneously attached to an agent with the primary model.

```text
safe primary LLM-only failure
→ prove no external mutation is active
→ canonical checkpoint
→ validate data class and current Cloudflare allocation
→ explicitly construct the approved Cloudflare profile
→ rerun only the safe LLM stage
```

## Privacy decision

Cloudflare states that Workers AI Customer Content is not used to train models or improve Cloudflare or third-party services without explicit consent.

Galax still prohibits secrets, credentials, unrestricted repository contents, customer personal data, and production records from being sent to this profile.

## CrewAI connection candidate

```python
from crewai import LLM

llm = LLM(
    model="@cf/openai/gpt-oss-20b",
    api_key="runtime-secret-only",
    base_url=(
        "https://api.cloudflare.com/client/v4/accounts/"
        "<account-id>/ai/v1"
    ),
    custom_openai=True,
    temperature=1.0,
    timeout=120,
    max_retries=1,
)
```

This example is disabled. The exact CrewAI parameter translation, authentication headers, tool calls, reasoning fields, usage reporting, and structured outputs must be tested.

## Important limitations

```text
- CrewAI 1.15.4 does not provide a named Cloudflare profile in the inspected documentation.
- The integration depends on a custom OpenAI-compatible endpoint.
- Free capacity is compute-based and can be depleted by long outputs.
- The provider/model/account limits can change.
- A successful plain completion does not prove tool calling or structured output.
- The fallback must never activate during a Git write, database mutation, upload, deployment, or merge.
```

## Required tests

```text
- authentication and exact endpoint/model availability
- CrewAI custom OpenAI-compatible construction
- one assigned tool call and valid Pydantic arguments
- real tool-result round trip with invocation evidence
- strict structured task output
- reasoning parameter compatibility
- unsupported-field behavior
- usage/allocation accounting
- timeout and rate/allocation exhaustion handling
- secret and data-classification enforcement
- sequential handoff
- checkpointed fallback from an intentionally failed safe primary stage
- per-agent quality acceptance
```

## Current decision

```yaml
provider_and_model_verified: true
free_daily_allocation_verified: true
privacy_reviewed: true
CrewAI_connection_path_found: true
CrewAI_live_test_completed: false
tool_calling_live_test_completed: false
structured_output_live_test_completed: false
approved_for_any_agent: false
```
