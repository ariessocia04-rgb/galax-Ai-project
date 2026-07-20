# Free LLM Provider Screening — 2026-07-20

**Status:** `DRAFT_MUTABLE`  
**Purpose:** Select a hosted free LLM candidate for the Galax CrewAI agents.  
**Discovery source:** [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources)  
**Discovery README blob reviewed:** `90471952f5b3029d41128f3c1d144bf00c35e0b7`

## 1. Source rule

The discovery repository is a curated directory, not the final source of truth. Provider/model claims must be checked against current official model metadata, API documentation, rate limits, privacy terms, licenses, CrewAI documentation, and exact implementation tests.

## 2. Mandatory selection criteria

```yaml
mandatory_criteria:
  legitimate_direct_provider: true
  free_hosted_api_available: true
  exact_model_id_available: true
  reasoning_capability: true
  function_or_tool_calling: true
  structured_output_or_json_schema: true
  system_instruction_support: true
  context_window_documented: true
  maximum_output_documented: true
  rate_limits_documented: true
  token_usage_returned: true
  server_side_api_key_supported: true
  safe_default_data_handling_or_explicit_verified_control: true
  crewai_connection_path_verified: true
  sequential_use_supported: true
  automatic_provider_fallback_disabled: true
```

## 3. Screening result

| Provider | Candidate | Result | Main decision reason |
|---|---|---|---|
| Cerebras Inference | `gpt-oss-120b` | `SELECTED_FOR_VALIDATION` | Reasoning, tool calling, strict structured output, 131K context, documented free token quota, direct CrewAI/LiteLLM path, provider states inference inputs/outputs are not retained |
| Groq | `openai/gpt-oss-120b` | `RESERVE_CANDIDATE_NOT_ACTIVE` | Strong capability and privacy controls, but lower documented free daily token quota |
| Google AI Studio | Gemini free models | `REJECTED_FOR_REPOSITORY_CONTENT` | Free-tier content may be used to improve Google products |
| OpenRouter | Free models/router | `REJECTED_AS_PRIMARY` | Low free request quota without paid top-up and variable free-model routing/availability |
| Mistral Free/Experiment | Mistral models | `REJECTED_FOR_INITIAL_BUILD` | Initial secure default would depend on account-level privacy controls; ZDR is not a free-plan default |
| Hugging Face Inference Providers | Various | `REJECTED_AS_PRIMARY` | Monthly free credits are too small for repeated multi-agent development runs |
| Cohere trial keys | Command models | `REJECTED_AS_PRIMARY` | Trial quota is too restrictive for repeated sequential development runs |
| GitHub Models | Various | `REJECTED_AS_PRIMARY` | Prototype limits vary by model and plan and are not a stable primary runtime quota |
| Cloudflare Workers AI | `@cf/openai/gpt-oss-120b` | `REJECTED_AS_PRIMARY` | Neuron-based quota makes usable daily text capacity workload-dependent |
| NVIDIA NIM | Various | `BLOCKED_INSUFFICIENT_MODEL_SPECIFIC_EVIDENCE` | Exact model-specific context, output, tool, structured-output, privacy, and token limits were not all established |

## 4. Selected validation candidate

```yaml
provider: Cerebras Inference
provider_model_id: gpt-oss-120b
crewai_model_id: cerebras/gpt-oss-120b
model_developer: OpenAI
status: SELECTED_FOR_VALIDATION
approved_for_agents: false
automatic_fallback: false
```

## 5. Verified capabilities

Official Cerebras public model metadata reports:

```yaml
context_window_tokens: 131072
maximum_completion_tokens: 40960
reasoning: true
reasoning_effort:
  - low
  - medium
  - high
function_calling: true
tools: true
tool_choice: true
parallel_tool_calls: false
structured_outputs: true
json_schema: true
json_mode: true
streaming: true
vision: false
```

Official sources:

- [Cerebras public model metadata](https://inference-docs.cerebras.ai/api-reference/models/public-models)
- [Cerebras chat completions](https://inference-docs.cerebras.ai/api-reference/chat-completions)
- [Cerebras tool calling](https://inference-docs.cerebras.ai/capabilities/tool-use)
- [Cerebras structured outputs](https://inference-docs.cerebras.ai/capabilities/structured-outputs)

## 6. Correct current free-trial limits

The current official Cerebras rate-limit page documents these general free-trial limits for `gpt-oss-120b`:

```yaml
requests_per_minute: 5
requests_per_hour: NOT_DOCUMENTED
requests_per_day: NOT_DOCUMENTED
tokens_per_minute: 30000
tokens_per_hour: 1000000
tokens_per_day: 1000000
monthly_token_limit: NOT_DOCUMENTED_AS_A_FIXED_FREE_QUOTA
```

The provider states that specific cases may vary, so the connected account's Limits page is authoritative at runtime.

- [Cerebras rate limits](https://inference-docs.cerebras.ai/support/rate-limits)

## 7. Privacy and security screening

Cerebras states that it does not retain inputs and outputs associated with training, inference, and chatbot services. Galax will still apply stricter repository-side controls.

- [Cerebras Cloud privacy policy](https://cloud.cerebras.ai/privacy)
- [Cerebras terms of service](https://www.cerebras.ai/terms-of-service)

```text
- Never send API keys, tokens, passwords, private keys, or `.env` contents.
- Never send unrestricted repository contents.
- Never send customer personal information or production data.
- Retrieve only task-relevant files.
- Scan context for secrets before every hosted LLM request.
- Keep API keys only in environment variables or a local secret store.
- Disable callbacks that export prompts or outputs to unapproved services.
```

## 8. CrewAI compatibility evidence

CrewAI's current source and documentation include Cerebras as a provider, require `CEREBRAS_API_KEY`, and use a `cerebras/<model>` model prefix. CrewAI documents LiteLLM as the connection path for Cerebras.

```bash
uv add 'crewai[litellm]'
```

Sources:

- [CrewAI LLM configuration](https://docs.crewai.com/concepts/llms)
- [CrewAI provider constants](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/lib/crewai/src/crewai/constants.py)
- [CrewAI Cerebras model discovery](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/lib/cli/src/crewai_cli/model_catalog.py)
- [LiteLLM Cerebras adapter](https://github.com/BerriAI/litellm/blob/bd44c9e305b89526d4c5d773ee39ca935561b9c8/litellm/llms/cerebras/chat.py)

The LiteLLM adapter maps tools, tool choice, response format, maximum completion tokens, and reasoning effort for Cerebras Chat Completions.

## 9. Critical API transition blocker

Cerebras announced that API version patch 2 becomes the default on **2026-07-21**, and older behavior reaches end of life.

- [Cerebras change log](https://inference-docs.cerebras.ai/support/change-log)

```yaml
production_approval: blocked
required_before_approval:
  - test_with_header_X-Cerebras-Version-Patch_2
  - retest_after_2026-07-21_default_transition
  - pin_verified_crewai_version
  - pin_verified_litellm_version
  - save_test_evidence
```

## 10. Why Cerebras is tested before Groq

Both candidates offer GPT-OSS 120B, reasoning, tool calling, and structured outputs. Cerebras is tested first because its documented free daily token quota is larger:

```yaml
cerebras:
  tokens_per_day: 1000000
  requests_per_day: NOT_DOCUMENTED

groq:
  tokens_per_day: 200000
  requests_per_day: 1000
```

Groq remains a manual reserve candidate. Galax will not automatically switch providers.

- [Groq GPT-OSS 120B](https://console.groq.com/docs/model/openai/gpt-oss-120b)
- [Groq rate limits](https://console.groq.com/docs/rate-limits)
- [Groq data controls](https://console.groq.com/docs/your-data)

## 11. Rejected-provider evidence links

### Google AI Studio

- [Gemini API pricing and data-use table](https://ai.google.dev/gemini-api/docs/pricing)

### OpenRouter

- [OpenRouter FAQ and free limits](https://openrouter.ai/docs/faq)
- [OpenRouter free router](https://openrouter.ai/docs/guides/routing/routers/free-router)
- [OpenRouter data collection](https://openrouter.ai/docs/guides/privacy/data-collection)

### Mistral

- [Mistral data training controls](https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models)
- [Mistral opt-out instructions](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training)
- [Mistral ZDR availability](https://help.mistral.ai/en/articles/347612-can-i-activate-zero-data-retention-zdr)

### Cloudflare Workers AI

- [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/)
- [Workers AI data usage](https://developers.cloudflare.com/workers-ai/platform/data-usage/)

### GitHub Models

- [GitHub Models prototyping limits](https://docs.github.com/en/github-models/prototyping-with-ai-models)
- [GitHub Models billing](https://docs.github.com/en/billing/concepts/product-billing/github-models)

## 12. Final screening decision

```yaml
selected_provider: Cerebras Inference
selected_model: gpt-oss-120b
crewai_model_string: cerebras/gpt-oss-120b
selection_status: SELECTED_FOR_VALIDATION
production_status: NOT_APPROVED
fallback_provider: none
manual_reserve_candidate: Groq openai/gpt-oss-120b
next_gate: API_V2_AND_CREWAI_COMPATIBILITY_TEST
```
