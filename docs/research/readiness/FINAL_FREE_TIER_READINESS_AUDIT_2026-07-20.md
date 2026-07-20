# Final Free/Open Runtime Readiness Audit — 2026-07-20

**Status:** `BLOCKED_NOT_READY_TO_PROMPT_CREWAI`  
**Purpose:** Final factual audit before issuing the Galax implementation prompt.  
**Decision:** Do not issue the full build prompt yet.

## 1. Executive decision

The architecture is technically possible, but the complete free/open runtime is not yet proven as one working CrewAI system.

```yaml
ready_to_generate_full_build_prompt: false
agents_enabled: 0
Groq_live_tested: false
Cloudflare_live_tested: false
Gemini_public_profile_live_tested: false
Ollama_hardware_qualified: false
repository_gateway_implemented: false
drive_gateway_implemented: false
memory_gateway_implemented: false
sandbox_implemented: false
docker_stack_implemented: false
```

CrewAI must not be instructed to claim completion or install the entire platform until the blockers below are resolved.

## 2. Technically supported components

| Component | Supported fact | Free/open status | Current Galax status |
|---|---|---|---|
| CrewAI 1.15.4 | Agents, tools, Flows, sequential Crews, structured outputs, guardrails, MCP adapters | Open-source package; providers/infrastructure may have limits | Selected, not integrated |
| `Process.sequential` | Tasks execute in declared order | No framework usage fee | Supported, not smoke-tested |
| One agent / one tool | CrewAI can receive one tool; Galax must enforce the maximum | Policy/infrastructure cost only | Not implemented |
| `GithubSearchTool` | Semantic repository/code/PR/issue search | CrewAI tool | Read/search only; no writes |
| `FileWriterTool` | Local filesystem write with path checks | CrewAI tool | No Git commit/push/PR |
| CrewAI MCP adapter | Adapts and filters external MCP tools | Open-source dependency | Path found, not integrated |
| Official GitHub MCP Server | Real repository read/write operations under token permissions | Open source; GitHub plan/feature rules apply | Selected integration candidate, not tested |
| Docker Compose | Can containerize CrewAI application and gateways | Engine open source; Desktop licensing applies | Architecture only |
| Google Drive API | Can search/read authorized files | Standard quotas apply | Gateway not implemented |
| Supabase/Postgres | Structured memory, pgvector, RLS, keyword/vector retrieval | Free plan exists with storage/compute/pause/backup limits | Selected external memory, not implemented |
| Notion API | Can mirror approved pages/data sources | Account permissions apply | Optional mirror, not implemented |
| Groq GPT-OSS 120B | Reasoning, tool use, JSON modes, 131K model context | Durable limited free plan | Private primary candidate, not tested |
| Cloudflare GPT-OSS 120B | Reasoning, function calling, JSON, 128K model context | 10,000 neurons/day | Hosted private fallback candidate, not tested |
| Gemini 2.5 Flash | Native CrewAI path, 1M context, function calling, structured output | Free tier exists | Public/redacted only, not tested |
| Ollama GPT-OSS 20B | Local model, tool/structured output support, no provider API quota | Owner supplies hardware/electricity | Optional local fallback, not qualified |

## 3. Removed active provider

### Cerebras GPT-OSS 120B

Current official pricing describes free trial credits rather than a durable permanent free plan.

```yaml
status: REJECTED_TRIAL_ONLY
active_primary: false
active_fallback: false
```

Historical research is retained only for source traceability.

## 4. Critical blockers

### Blocker A — No pinned dependency image

The exact combination has not been installed and tested together:

```text
Python
CrewAI
crewai-tools
MCP SDK
mcpadapt
LiteLLM/provider SDKs
GitHub MCP Server image digest
```

Required proof:

```text
build image
→ import tests
→ dependency audit
→ start/stop MCP server
→ record exact versions/digests
```

### Blocker B — No real GitHub read/write integration

Built-in GitHub search cannot write, and the generic local file writer cannot commit/push/create PRs.

Required implementation:

```text
CrewAI MCP adapter or trusted custom tool
→ official GitHub MCP Server/API
→ exact tool filtering
→ least-privilege token
→ run-branch read/write
→ reject direct main write
→ verify commit and draft PR evidence
```

### Blocker C — No provider profile has passed CrewAI tests

Groq, Cloudflare, Gemini, and Ollama require separate validation for:

```text
completion
system instructions
single assigned tool
argument schema
tool-result round trip
structured output
usage/capacity accounting
context/rate/allocation handling
timeout/429 behavior
data classification
sequential handoff
```

### Blocker D — No native CrewAI failover policy was found

CrewAI constructs one LLM profile at a time. Galax provider switching must be explicit deterministic Flow logic with a safe checkpoint.

Required proof:

```text
primary safe-stage failure
→ no active external mutation
→ checkpoint
→ alternate profile approval/capacity/data-class check
→ explicit LLM reconstruction
→ safe-stage rerun
→ provider switch evidence
```

### Blocker E — Secure code sandbox is not implemented

CrewAI does not provide the approved Galax arbitrary-code execution boundary. Privileged Docker-in-Docker and unrestricted Docker socket mounting remain rejected.

Required implementation:

```text
separate rootless daemon or sandbox host
→ narrow authenticated controller
→ ephemeral non-root container
→ offline by default
→ scoped worktree
→ limits and command allowlist
→ forced cleanup
```

### Blocker F — Drive knowledge gateway is not implemented

Required implementation:

```text
approved-folder search
→ metadata + body-text related-file retrieval
→ actual content read
→ version/conflict checks
→ LearningPacket
→ StudyReceipt validation
```

### Blocker G — Supabase memory is external, not native CrewAI memory

Required implementation:

```text
schema and RLS
→ exact-filter/keyword retrieval first
→ idempotency and supersession
→ backup/restore test
→ bounded MemoryContext
→ optional embeddings only after provider approval
```

## 5. Active LLM routing decision

### Private repository primary candidate

```yaml
provider: Groq
model: groq/openai/gpt-oss-120b
status: DISABLED_PENDING_CREWAI_TESTS
base_limits:
  RPM: 30
  RPD: 1000
  TPM: 8000
  TPD: 200000
```

Official links:

- https://console.groq.com/docs/model/openai/gpt-oss-120b
- https://console.groq.com/docs/rate-limits
- https://console.groq.com/docs/tool-use/local-tool-calling
- https://console.groq.com/docs/openai
- https://console.groq.com/docs/your-data

### Private hosted fallback candidate

```yaml
provider: Cloudflare Workers AI
model: '@cf/openai/gpt-oss-120b'
connection: custom_OpenAI_compatible
status: DISABLED_PENDING_CREWAI_TESTS
free_allocation: 10000_neurons_per_day
```

Official links:

- https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/
- https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/
- https://developers.cloudflare.com/workers-ai/features/function-calling/
- https://developers.cloudflare.com/workers-ai/features/json-mode/
- https://developers.cloudflare.com/workers-ai/platform/pricing/
- https://developers.cloudflare.com/workers-ai/platform/data-usage/

### Public/redacted long-context candidate

```yaml
provider: Google Gemini API
model: gemini/gemini-2.5-flash
status: DISABLED_PENDING_TESTS
private_repository_content: prohibited_on_free_tier
```

Official links:

- https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash
- https://ai.google.dev/gemini-api/docs/rate-limits
- https://ai.google.dev/gemini-api/docs/pricing
- https://github.com/crewAIInc/crewAI/blob/main/docs/v1.15.4/en/concepts/llms.mdx

### Optional local fallback candidate

```yaml
provider: Ollama
model: ollama/gpt-oss:20b
status: DISABLED_PENDING_HARDWARE_AND_CREWAI_TESTS
```

Official links:

- https://ollama.com/library/gpt-oss
- https://ollama.com/library/gpt-oss:20b
- https://ollama.com/blog/gpt-oss

### Conditional research candidate

Mistral Free Mode is not active until exact account model availability, limits, privacy behavior, and CrewAI compatibility are verified.

## 6. Free/open reality

The project can be developed largely with free/open components, but uninterrupted zero-cost operation is not guaranteed.

Potential interruptions:

```text
- Groq TPM/TPD/RPD limits
- Cloudflare daily neuron allocation
- Gemini project/model free-tier limits and data-use restrictions
- local Ollama hardware and electricity limits
- Supabase pausing, storage limit, and missing included backups
- Google Drive quotas
- Docker host CPU/RAM/disk/network requirements
```

## 7. Minimum gate before generating the build prompt

```text
READY-001 Pin Python, CrewAI, crewai-tools, MCP/mcpadapt, and provider integrations.
READY-002 Build and audit the base Docker image.
READY-003 Start/stop the pinned official GitHub MCP Server image.
READY-004 Enumerate exact GitHub tool schemas and permissions.
READY-005 Implement and test read-only RepositoryPreflightTool.
READY-006 Prove an authorized temporary run-branch write.
READY-007 Reject direct-main, force-push, secret-path, and unauthorized-path writes.
READY-008 Test Groq completion/tool/structured output through CrewAI.
READY-009 Test Cloudflare custom OpenAI completion/tool/structured output through CrewAI.
READY-010 Test Gemini only with public/redacted fixtures.
READY-011 Qualify Ollama hardware and local tool/structured output behavior.
READY-012 Implement minimal Drive search/read and LearningPacket evidence.
READY-013 Implement Supabase exact-filter/keyword memory and safe checkpoint/run ledger.
READY-014 Pass a real two-agent Process.sequential smoke test with invocation evidence.
READY-015 Confirm every unsupported operation returns a blocker and factual remedy.
```

The full implementation prompt may be generated only after all 15 gates pass.

## 8. Current final status

```yaml
final_fact_check_result: TECHNICALLY_SUPPORTED_BUT_NOT_INTEGRATED
full_free_open_runtime_proven: false
full_CrewAI_prompt_authorized: false
required_action: IMPLEMENT_MINIMUM_RUNTIME_AND_RUN_LIVE_SMOKE_TESTS_FIRST
```
