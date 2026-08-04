# LLM Source Card — Google Gemini 2.5 Flash

**Source ID:** `LLM-google-gemini-2.5-flash`  
**Status:** `PUBLIC_OR_REDACTED_CONTEXT_ONLY_PENDING_TESTS`  
**Approved for agents:** No  
**Verified:** 2026-07-20

## Identity

```yaml
provider: Google Gemini API
exact_model_id: gemini-2.5-flash
crewai_model_id: gemini/gemini-2.5-flash
context_window_tokens: 1048576
maximum_output_tokens: 65536
function_calling: true
structured_outputs: true
thinking: true
free_tier: available
runtime_status: DISABLED_PENDING_TESTS
```

## Official links

- [Gemini 2.5 Flash model](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash)
- [Gemini API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits)
- [Gemini API pricing and free tier](https://ai.google.dev/gemini-api/docs/pricing)
- [Gemini API billing tiers](https://ai.google.dev/gemini-api/docs/billing)
- [CrewAI versioned LLM documentation](https://github.com/crewAIInc/crewAI/blob/main/docs/v1.15.4/en/concepts/llms.mdx)

## CrewAI connection

CrewAI documents a native Google Gen AI integration:

```bash
uv add 'crewai[google-genai]'
```

```python
from crewai import LLM

llm = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.2,
    timeout=120,
    max_retries=1,
)
```

Required secret:

```env
GEMINI_API_KEY=
```

## Free-tier data restriction

Google states that free-tier content may be used to improve its products. Therefore this profile is prohibited for:

```text
- private repository source that has not been approved for disclosure
- credentials or secrets
- customer personal information
- production data
- confidential owner documents
```

Allowed candidate use:

```text
- official public documentation
- open-source repository excerpts
- owner-approved public learning material
- fully redacted long-context packets
```

## Rate-limit rule

Google states that active limits vary by model, project, tier, and account status and must be viewed in AI Studio. Repository numbers cannot be treated as permanent capacity.

Before every run group:

```text
capture current account RPM/TPM/RPD
→ apply Galax headroom
→ block if the required packet cannot fit
```

## Current decision

```yaml
model_identity_verified: true
CrewAI_native_path_found: true
large_context_verified: true
function_calling_documented: true
structured_outputs_documented: true
free_tier_verified: true
private_repository_use_allowed: false
CrewAI_live_test_completed: false
approved: false
```
