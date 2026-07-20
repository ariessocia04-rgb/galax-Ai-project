# Free LLM Provider Screening — 2026-07-20

**Status:** `DRAFT_MUTABLE`  
**Purpose:** Select the hosted free LLM candidate for the Galax CrewAI agents.  
**Discovery source:** [cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources)  
**Discovery README blob reviewed:** `90471952f5b3029d41128f3c1d144bf00c35e0b7`

## 1. Source rule

The discovery repository is a curated directory, not the final source of truth. Every provider and model decision below was checked against official provider, model, privacy, rate-limit, and CrewAI implementation sources.

## 2. Required selection criteria

A provider/model can be selected only when all mandatory criteria are supported by official evidence or exact implementation tests.

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
  secure_server_side_api_key: true
  inputs_outputs_not_used_for_training_by_default_or_explicit_safe_control: true
  crewai_connection_path_verified: true
  sequential_use_supported: true
  automatic_provider_fallback_disabled: true
```

## 3. Provider screening summary

| Provider | Candidate model | Result | Main reason |
|---|---|---|---|
| Cerebras Inference | `gpt-oss-120b` | `SELECTED_FOR_VALIDATION` | Strong free quota, reasoning, tool calling, strict structured outputs, 131K context, direct CrewAI provider path, no input/output retention stated |
| Groq | `openai/gpt-oss-120b` | `RESERVE_CANDIDATE_NOT_ACTIVE` | Strong capabilities and privacy controls, but lower free daily token quota than Cerebras |
| Google AI Studio | Gemini free models | `REJECTED_FOR_REPOSITORY_CONTENT` | Free-tier content is used to improve Google products |
| OpenRouter | free variants/router | `REJECTED_AS_PRIMARY` | 50 free requests/day without a paid top-up; free model availability and routing can vary |
| Mistral Free/Experiment | Mistral models | `REJECTED_FOR_INITIAL_BUILD` | Free-plan data controls require explicit opt-out and ZDR is not available on the free plan |
| Hugging Face Inference Providers | Various | `REJECTED_AS_PRIMARY` | Free monthly credits are too small for a 15-agent development system |
| Cohere trial keys | Command models | `REJECTED_AS_PRIMARY` | Shared trial quota is too restrictive for repeated sequential development runs |
| GitHub Models | Various | `REJECTED_AS_PRIMARY` | Free prototype limits vary by model and Copilot plan and are not intended as a stable production quota |
| Cloudflare Workers AI | `@cf/openai/gpt-oss-120b` | `REJECTED_AS_PRIMARY` | Free allocation is neuron-based and provides materially less predictable daily text capacity for this model |
| NVIDIA NIM | Various | `BLOCKED_INSUFFICIENT_MODEL_SPECIFIC_EVIDENCE` | Discovery list gives a general request limit, but Galax requires exact model-level context, tool, structured-output, privacy, and token limits |
| Cerebras trial/paid alternatives | Other models | `NOT_REQUIRED` | One common model reduces integration and operational complexity |

## 4. Selected validation candidate

```yaml
provider: Cerebras Inference
model_id_for_provider_api: gpt-oss-120b
model_id_for_crewai: cerebras/gpt-oss-120b
model_developer: OpenAI
status: SELECTED_FOR_VALIDATION
approved_for_agents: false
automatic_fallback: false
```

## 5. Verified model capabilities

Official Cerebras model metadata currently reports:

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

- [Cerebras supported models](https://inference-docs.cerebras.ai/models/overview)
- [Cerebras public model metadata](https://inference-docs.cerebras.ai/api-reference/models/public-models)
- [Cerebras chat completions](https://inference-docs.cerebras.ai/api-reference/chat-completions)
- [Cerebras tool calling](https://inference-docs.cerebras.ai/capabilities/tool-use)
- [Cerebras structured outputs](https://inference-docs.cerebras.ai/capabilities/structured-outputs)

## 6. Verified free limits

Official Cerebras free-tier documentation currently lists the following general limits for `gpt-oss-120b`:

```yaml
requests_per_minute: 30
requests_per_hour: 900
requests_per_day: 14400
tokens_per_minute: 64000
tokens_per_hour: 1000000
tokens_per_day: 1000000
```

Exact account limits must still be read from the connected Cerebras account because the provider states that specific cases may vary.

Source:

- [Cerebras rate limits](https://inference-docs.cerebras.ai/support/rate-limits)

## 7. Privacy and security screening

Cerebras states that inputs and outputs associated with training, inference, and chatbot services are not retained. Its terms state that Service Content is not used for model training or fine-tuning, while usage data excludes user content and outputs.

Sources:

- [Cerebras Cloud privacy policy](https://cloud.cerebras.ai/privacy)
- [Cerebras terms of service](https://www.cerebras.ai/terms-of-service)
- [Cerebras cloud data ownership statement](https://www.cerebras.ai/cloud)

Galax will still apply these restrictions:

```text
- Never send API keys, tokens, passwords, private keys, or `.env` contents.
- Never send unrestricted repository contents.
- Never send customer personal information or production data.
- Retrieve only task-relevant files.
- Scan context for secrets before every hosted LLM request.
- Keep API keys only in environment variables or a local secret store.
- Disable third-party observability callbacks that log prompts or outputs.
```

## 8. CrewAI compatibility evidence

CrewAI's current source code explicitly includes `cerebras` as a provider, expects the model name to start with `cerebras/`, uses `CEREBRAS_API_KEY`, and queries `https://api.cerebras.ai/v1/models` as an OpenAI-compatible endpoint.

CrewAI also states that non-native providers use the LiteLLM integration and require:

```bash
uv add 'crewai[litellm]'
```

Sources:

- [CrewAI LLM configuration](https://docs.crewai.com/concepts/llms)
- [CrewAI source: provider constants](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/lib/crewai/src/crewai/constants.py)
- [CrewAI source: dynamic Cerebras model discovery](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/lib/cli/src/crewai_cli/model_catalog.py)
- [LiteLLM Cerebras adapter](https://github.com/BerriAI/litellm/blob/bd44c9e305b89526d4c5d773ee39ca935561b9c8/litellm/llms/cerebras/chat.py)

The LiteLLM adapter identifies Cerebras Chat Completions as OpenAI-compatible and maps tools, tool choice, response format, maximum completion tokens, and reasoning effort.

## 9. Critical API transition blocker

Cerebras announced that API version patch 2 becomes the default on **2026-07-21**, with older behavior reaching end of life. This selection is being made on **2026-07-20**.

Source:

- [Cerebras change log](https://inference-docs.cerebras.ai/support/change-log)

Therefore:

```yaml
production_approval: blocked
required_before_approval:
  - test_with_header_X-Cerebras-Version-Patch_2
  - retest_after_2026-07-21_default_transition
  - pin_verified_crewai_version
  - pin_verified_litellm_version
  - save_test_evidence
```

## 10. Why Cerebras wins over Groq for the first validation

Both candidates provide GPT-OSS 120B, reasoning, tool calling, JSON/structured output, and direct API access. Cerebras is selected first because its documented free quota is materially larger:

```yaml
cerebras:
  tokens_per_day: 1000000
  requests_per_day: 14400

groq:
  tokens_per_day: 200000
  requests_per_day: 1000
```

Groq remains a manual reserve candidate because it has strong data controls, including an available Zero Data Retention setting, but Galax will not automatically fall back to it.

Groq sources:

- [Groq GPT-OSS 120B](https://console.groq.com/docs/model/openai/gpt-oss-120b)
- [Groq rate limits](https://console.groq.com/docs/rate-limits)
- [Groq data controls](https://console.groq.com/docs/your-data)

## 11. Rejected-provider details

### Google AI Studio

The Gemini Developer API pricing page states that free-tier content is used to improve Google products. Galax therefore rejects it for repository source code, architecture, security findings, and private project context.

- [Gemini API pricing and data-use table](https://ai.google.dev/gemini-api/docs/pricing)

### OpenRouter

The free-model quota is generally 50 requests per day unless at least $10 in credits has been purchased. The free router may select different available models, and free model availability may vary. This conflicts with Galax's exact-provider, exact-model, pinned-behavior, and no-paid-dependency rules.

- [OpenRouter FAQ and free limits](https://openrouter.ai/docs/faq)
- [OpenRouter free router](https://openrouter.ai/docs/guides/routing/routers/free-router)
- [OpenRouter data collection](https://openrouter.ai/docs/guides/privacy/data-collection)

### Mistral Free/Experiment

Mistral provides privacy controls, but its free plan may use API input/output data unless the user opts out. Zero Data Retention is available only for the paid Scale plan. Galax rejects it for the initial secure default because privacy must not depend on a manual account toggle that can be changed outside the repository.

- [Mistral data training controls](https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models)
- [Mistral opt-out instructions](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training)
- [Mistral ZDR availability](https://help.mistral.ai/en/articles/347612-can-i-activate-zero-data-retention-zdr)

### Cloudflare Workers AI

Workers AI provides 10,000 free neurons per day. For `@cf/openai/gpt-oss-120b`, the published rates are 31,818 neurons per million input tokens and 68,182 neurons per million output tokens. This produces a smaller and workload-dependent free daily text budget than the selected Cerebras quota.

- [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/)
- [Workers AI data usage](https://developers.cloudflare.com/workers-ai/platform/data-usage/)

### GitHub Models

GitHub describes free API usage as rate-limited prototyping access. Limits depend on the model and Copilot subscription tier. Galax requires a stable model-specific quota and direct provider behavior, so GitHub Models is not selected as the primary runtime.

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
