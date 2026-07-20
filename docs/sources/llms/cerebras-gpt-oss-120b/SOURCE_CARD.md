# LLM Source Card — Cerebras GPT-OSS 120B

**Source ID:** `LLM-cerebras-gpt-oss-120b`  
**Status:** `REJECTED_TRIAL_ONLY`  
**Approved for agents:** No  
**Verified:** 2026-07-20  
**Historical record:** retained for traceability; removed from active LLM routing

## Identity

```yaml
provider: Cerebras Inference
provider_model_id: gpt-oss-120b
crewai_model_id: cerebras/gpt-oss-120b
model_developer: OpenAI
license: Apache-2.0
current_cost_classification: finite_free_trial_credits
active_primary: false
active_fallback: false
runtime_status: rejected
```

## Why it was removed

The discovery repository previously listed Cerebras under free providers, but the current official Cerebras pricing page describes a free trial credit offer rather than a durable permanent free plan.

The owner requires trial-only providers to be disregarded from the active Galax routing plan. Therefore this profile cannot be used as primary, fallback, or automatic emergency routing.

## Exact official links

- [Cerebras pricing](https://www.cerebras.ai/pricing)
- [Cerebras Inference documentation](https://inference-docs.cerebras.ai/)
- [Supported models](https://inference-docs.cerebras.ai/models/overview)
- [Public model metadata](https://inference-docs.cerebras.ai/api-reference/models/public-models)
- [Tool calling](https://inference-docs.cerebras.ai/capabilities/tool-use)
- [Structured outputs](https://inference-docs.cerebras.ai/capabilities/structured-outputs)
- [Rate limits](https://inference-docs.cerebras.ai/support/rate-limits)
- [Change log](https://inference-docs.cerebras.ai/support/change-log)
- [Cerebras privacy](https://cloud.cerebras.ai/privacy)
- [CrewAI LLM configuration](https://docs.crewai.com/concepts/llms)

## Historical technical evidence

The provider documents GPT-OSS 120B reasoning, tool calling, structured outputs, and a large model context. CrewAI also has a Cerebras provider path through LiteLLM.

Those facts prove technical possibility only. They do not override the current cost-policy rejection.

## Prohibited actions

```text
- Do not place cerebras/gpt-oss-120b in active agents.yaml.
- Do not use it as automatic fallback.
- Do not request an API key for the current free-only Galax plan.
- Do not treat earlier free-provider directory values as current provider truth.
- Do not delete this source card; it records why the candidate was rejected.
```

## Reconsideration rule

Cerebras may be researched again only if the provider introduces a durable non-trial free plan or the owner explicitly approves paid usage.

```yaml
identity_verified: true
technical_capabilities_documented: true
CrewAI_provider_path_found: true
live_Galax_test_completed: false
rejection_reason: trial_only_cost_model
approved: false
```
