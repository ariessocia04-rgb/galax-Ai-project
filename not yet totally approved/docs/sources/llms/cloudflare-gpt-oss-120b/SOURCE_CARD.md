# LLM Source Card — Cloudflare Workers AI GPT-OSS 120B

**Source ID:** `LLM-cloudflare-gpt-oss-120b`  
**Status:** `SELECTED_FOR_VALIDATION_AS_HOSTED_FALLBACK`  
**Approved for agents:** No  
**Verified:** 2026-07-20

## Identity

```yaml
provider: Cloudflare Workers AI
exact_model_id: '@cf/openai/gpt-oss-120b'
crewai_connection: custom_OpenAI_compatible_endpoint
model_developer: OpenAI
context_window_tokens: 128000
function_calling: true
reasoning: true
structured_JSON: true
free_allocation: 10000_neurons_per_day
runtime_status: DISABLED_PENDING_TESTS
```

## Official links

- [Model page](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/)
- [OpenAI-compatible API](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/)
- [Function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/)
- [Traditional function calling](https://developers.cloudflare.com/workers-ai/features/function-calling/traditional/)
- [JSON mode and schemas](https://developers.cloudflare.com/workers-ai/features/json-mode/)
- [Free allocation and pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/)
- [Customer data usage](https://developers.cloudflare.com/workers-ai/platform/data-usage/)
- [CrewAI custom OpenAI-compatible endpoint](https://docs.crewai.com/concepts/llms)

## Free-allocation interpretation

Cloudflare provides 10,000 neurons/day, not a fixed request or token quota. Current unit rates for this model are 31,818 neurons per million input tokens and 68,182 neurons per million output tokens.

Approximate maximums when used exclusively:

```yaml
input_only_tokens: approximately_314000
output_only_tokens: approximately_146000
```

Real requests consume both input and output allocations.

## Privacy decision

Cloudflare states that it does not use Workers AI Customer Content to train AI models or improve Cloudflare or third-party services without explicit consent.

Galax restrictions still prohibit secrets, credentials, unrestricted repository content, customer personal data, and production records from being sent without an approved data classification.

## CrewAI connection candidate

```python
from crewai import LLM

llm = LLM(
    model="@cf/openai/gpt-oss-120b",
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

The exact `LLM` parameter translation, model naming, tool calls, and structured outputs must be live-tested. The example is not enabled.

## Known risks

```text
- CrewAI does not list Cloudflare as a named provider profile in the inspected version.
- Integration relies on the custom OpenAI-compatible path.
- Free allocation is compute-based and may be exhausted by long outputs.
- Current model/API behavior and account permissions must be captured.
- Tool-call round trips and JSON schemas require exact live tests.
```

## Current decision

```yaml
provider_and_model_verified: true
permanent_free_allocation_verified: true
privacy_reviewed: true
CrewAI_connection_path_found: true
CrewAI_live_test_completed: false
tool_calling_live_test_completed: false
structured_output_live_test_completed: false
approved: false
```
