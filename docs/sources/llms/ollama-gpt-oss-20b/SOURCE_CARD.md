# LLM Source Card — Local Ollama GPT-OSS 20B

**Source ID:** `LLM-ollama-gpt-oss-20b`  
**Status:** `OPTIONAL_LOCAL_FALLBACK_PENDING_HARDWARE_TESTS`  
**Approved for agents:** No  
**Verified:** 2026-07-20

## Identity

```yaml
provider: local_Ollama
exact_model_id: gpt-oss:20b
crewai_model_id: ollama/gpt-oss:20b
context_window_tokens: 128000
model_download_size: approximately_14GB
function_calling: documented
structured_outputs: documented
reasoning_effort: low_medium_high
hosted_API_quota: none
runtime_status: DISABLED_PENDING_HARDWARE_AND_CREWAI_TESTS
```

## Official links

- [Ollama GPT-OSS library page](https://ollama.com/library/gpt-oss)
- [Ollama GPT-OSS 20B](https://ollama.com/library/gpt-oss:20b)
- [Ollama GPT-OSS launch information](https://ollama.com/blog/gpt-oss)
- [CrewAI LLM documentation](https://docs.crewai.com/concepts/llms)

## Local requirements

The official Ollama model page states that the 20B model can run on systems with approximately 16 GB memory. Actual usable performance depends on RAM, VRAM, CPU/GPU, operating system, context length, concurrency, and quantization/runtime behavior.

The model download is approximately 14 GB. Full 128K context may require substantially more runtime memory than a short prompt.

## Candidate setup

```bash
ollama pull gpt-oss:20b
ollama serve
```

```python
from crewai import LLM

llm = LLM(
    model="ollama/gpt-oss:20b",
    base_url="http://127.0.0.1:11434",
    temperature=1.0,
    timeout=300,
    max_retries=1,
)
```

The exact CrewAI/LiteLLM setup and base URL must be tested in the pinned Docker/host environment.

## Security and cost decision

```yaml
provider_prompt_retention: none_for_local_execution
external_API_cost: none
local_costs:
  - RAM_or_VRAM
  - disk
  - electricity
  - processing_time
  - hardware_wear_and_maintenance
```

The Ollama endpoint must bind only to an approved local/internal interface. It must not be exposed publicly without authentication and network controls.

## Failover restriction

Ollama is not automatically valid merely because a hosted provider is unavailable.

Required proof:

```text
hardware qualification
→ exact model digest capture
→ context test
→ single-tool call test
→ tool-result round trip
→ structured output test
→ timeout/latency test
→ per-agent quality test
```

## Current decision

```yaml
model_available: true
large_context_documented: true
tool_calling_documented: true
structured_output_documented: true
CrewAI_connection_path_found: true
hardware_qualified: false
CrewAI_live_test_completed: false
approved: false
```
