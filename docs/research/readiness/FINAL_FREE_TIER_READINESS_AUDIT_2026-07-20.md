# Final Free-Tier Readiness Audit — 2026-07-20

**Status:** `BLOCKED_NOT_READY_TO_PROMPT_CREWAI`  
**Purpose:** Final factual audit before issuing the Galax implementation prompt.  
**Decision:** Do not issue the full build prompt yet.

## 1. Executive decision

The architecture is technically possible, but the complete free-tier runtime is not yet proven as one working CrewAI system.

```yaml
ready_to_generate_full_build_prompt: false
agents_enabled: 0
primary_llm_live_tested: false
fallback_llm_live_tested: false
repository_gateway_implemented: false
drive_gateway_implemented: false
memory_gateway_implemented: false
sandbox_implemented: false
docker_stack_implemented: false
```

CrewAI must not be instructed to claim completion or install the entire platform until the blockers in this audit are resolved.

## 2. What is fact-checked as technically supported

| Component | Supported fact | Free status | Current Galax status |
|---|---|---|---|
| CrewAI 1.15.4 | Python framework supports agents, tools, Flows, sequential Crews, structured outputs, guardrails, and MCP tools | Open-source package; external services may cost | Selected, not live tested |
| LiteLLM | CrewAI uses LiteLLM for Cerebras, Groq, and OpenRouter providers | OSS portion is MIT; provider usage has separate limits | Version not pinned with CrewAI tests |
| `Process.sequential` | Tasks execute in declared order when each task has an assigned agent | Framework feature | Supported, not integrated |
| One agent / one tool | CrewAI permits assigning one tool; Galax Flow must enforce the maximum | No additional framework cost | Policy only, not implemented |
| Docker Compose | Can containerize the Python application and gateways | Docker Engine is open source; Docker Desktop is free only under its license conditions | Architecture only |
| Google Drive API | Can search/read owner-authorized files; standard use is currently no additional cost below quotas | Free under current standard-use thresholds; charging model may change later in 2026 | Gateway not implemented |
| Supabase Postgres | Provides Postgres, pgvector, RLS, semantic/hybrid search primitives | Free plan: 500 MB, shared CPU/500 MB RAM, two active projects, pauses after low activity, no included automatic backups | Selected as memory candidate, not implemented |
| Notion API | Can read/create/update dedicated pages and data sources | API access exists, but plan/account permissions still apply | Optional mirror only, not implemented |
| Notion hosted MCP | Can read/write through user OAuth | Requires an interactive user OAuth flow; unsuitable as mandatory unattended memory | Rejected as primary runtime memory |
| Cerebras `gpt-oss-120b` | Supports reasoning, tool calling, and strict structured outputs | Free tier exists with account/model limits | Blocked pending Version 2 and capacity tests |
| Groq `openai/gpt-oss-120b` | Supports reasoning, local tool calls, JSON object/schema modes | Free plan exists with 30 RPM, 1,000 RPD, 8K TPM, 200K TPD base limits | Selected fallback candidate, not tested |

## 3. Critical conflicts that block the prompt

### Blocker A — Cerebras API Version 2 transition

Cerebras documents that API Version 2 becomes the default on **2026-07-21** and older behavior reaches end-of-life. Version 2 applies stricter tool and JSON Schema validation.

Required action:

```text
wait for or explicitly test Version 2
→ regenerate every strict schema with additionalProperties: false
→ test tool calls
→ test structured task output
→ test CrewAI/LiteLLM translation
```

### Blocker B — Cerebras free-tier context ambiguity

Official Cerebras model metadata documents a 131,072-token model context, while the official pricing page states that the free tier supports an 8,192-token context. The actual connected organization limit must be treated as the source of truth.

Therefore the current Galax assumptions of 12K–20K input context are not approved for free-tier execution.

```yaml
current_capacity_status: BLOCKED_CAPACITY_UNKNOWN
provisional_safe_total_context: 8192
previous_20000_input_hard_limit: INVALID_UNTIL_LIVE_TESTED
```

No agent-specific prompt size or output cap can be finalized until the account capacity snapshot is captured.

### Blocker C — No pinned CrewAI + LiteLLM compatibility result

CrewAI 1.15.4 is current, and LiteLLM 1.92.0 is the latest stable release found during this audit. The exact pair has not been installed and tested together in the Galax Docker image.

Required tests:

```text
install exact versions
→ import test
→ Cerebras completion
→ Cerebras strict tool call
→ Cerebras structured output
→ Groq completion
→ Groq strict tool call
→ Groq structured output
→ two-agent sequential run
→ token and error mapping
```

### Blocker D — No actual agent tools exist

Only tool designs exist. CrewAI agents cannot read/write GitHub, search Drive, query memory, execute tests, or run Docker merely because the prompt says so.

Required implementation:

```text
RepositoryPreflightTool
role-scoped repository workspace tools
DriveKnowledgeGateway
GalaxMemoryGateway
VerifiedResearchWorkspaceTool
sandbox-controller
QA/test evidence gateway
release audit gateway
```

### Blocker E — Secure sandbox is not implemented

CrewAI does not provide the approved secure code-execution boundary. Privileged Docker-in-Docker and unrestricted Docker socket mounting are rejected.

Required implementation:

```text
separate rootless daemon or sandbox host
→ narrow authenticated controller API
→ ephemeral non-root containers
→ offline by default
→ scoped worktree
→ resource limits
→ command allowlist
→ forced cleanup
```

### Blocker F — Supabase memory is not native CrewAI memory

Supabase is technically suitable as external application memory, but no live Galax gateway, schema, RLS policy, backup job, or retrieval test exists.

Required implementation:

```text
keyword/exact-filter mode first
→ schema and RLS
→ idempotency and supersession
→ backup/restore test
→ bounded MemoryContext
→ optional embeddings only after provider approval
```

### Blocker G — Hosted Notion MCP cannot be mandatory unattended memory

Notion states that its hosted MCP uses user OAuth and requires human authorization. It does not support bearer-token authentication for fully automated cloud agents.

Selected remedy:

```text
Supabase/Postgres = primary runtime memory
Notion REST API internal connection = optional curated mirror
Notion hosted MCP = human-assisted operations only
```

## 4. Primary and fallback LLM decision

### Primary candidate

```yaml
provider: Cerebras
model: cerebras/gpt-oss-120b
status: DISABLED_PENDING_API_V2_AND_ACCOUNT_TESTS
```

Official links:

- https://inference-docs.cerebras.ai/models/overview
- https://inference-docs.cerebras.ai/support/rate-limits
- https://inference-docs.cerebras.ai/api-reference/versions
- https://inference-docs.cerebras.ai/capabilities/tool-use
- https://inference-docs.cerebras.ai/capabilities/structured-outputs

### Controlled fallback candidate

```yaml
provider: Groq
model: groq/openai/gpt-oss-120b
status: DISABLED_PENDING_SEPARATE_TESTS
```

Official links:

- https://console.groq.com/docs/model/openai/gpt-oss-120b
- https://console.groq.com/docs/rate-limits
- https://console.groq.com/docs/tool-use/local-tool-calling
- https://console.groq.com/docs/openai
- https://console.groq.com/docs/your-data

### Why Groq is selected over an OpenRouter free router

Groq exposes one exact direct model and exact account limits. OpenRouter free models are useful for experiments, but free availability changes and normal accounts are generally limited to 50 free-model requests per day. The random `openrouter/free` router may change the selected model per request, which conflicts with pinned agent validation.

OpenRouter `openai/gpt-oss-120b:free` may remain a tertiary research candidate, but it is not approved as the automatic production fallback.

## 5. Fallback is not silent

A backup provider is required, but switching must be deterministic and auditable.

```text
primary provider fails with approved failover error
→ checkpoint before any non-idempotent tool action
→ verify fallback profile is APPROVED_FOR_AGENT
→ verify fallback capacity and rate snapshot
→ record provider switch
→ rerun current LLM-only step or resume from safe checkpoint
```

Do not switch providers:

```text
- during a repository write transaction
- after a non-idempotent external action without reconciliation
- because the primary answer was inconvenient
- when the fallback profile is not separately tested
- when structured output or tool schema behavior differs
```

## 6. Free-tier reality

The project can be developed and tested largely with free/open-source components, but “fully free and continuously reliable” is not guaranteed.

Potential free-tier interruptions include:

```text
- Cerebras temporary rate reductions or account-specific context limits
- Groq token/day and token/minute limits
- Supabase project pausing and missing included backups
- Google Drive future over-quota billing changes
- OpenRouter free-model availability and low daily request limits
- Notion OAuth requirements for hosted MCP
- local Docker host CPU, RAM, disk, and network costs
```

## 7. Minimum gate before generating the build prompt

```text
READY-001 Pin Python, CrewAI, crewai-tools, and LiteLLM.
READY-002 Build the base Docker image successfully.
READY-003 Test Cerebras API Version 2 directly.
READY-004 Capture actual Cerebras account rate and context limits.
READY-005 Test Cerebras through CrewAI/LiteLLM.
READY-006 Test Groq through CrewAI/LiteLLM.
READY-007 Approve deterministic failover rules.
READY-008 Implement a read-only repository preflight tool.
READY-009 Implement a minimal Drive read/search gateway.
READY-010 Implement Supabase keyword/exact-filter memory gateway without embeddings.
READY-011 Implement one safe checkpoint and run ledger.
READY-012 Implement one minimal sequential two-agent smoke test.
READY-013 Produce real tool invocation evidence.
READY-014 Confirm no direct write to main and no automatic merge.
READY-015 Confirm every unsupported operation produces a blocker and remedy.
```

The full implementation prompt may be generated only after 15 of 15 readiness gates pass.

## 8. Current final status

```yaml
final_fact_check_result: PARTIALLY_SUPPORTED_NOT_INTEGRATED
full_free_tier_runtime_proven: false
full_CrewAI_prompt_authorized: false
required_action: FIX_FLOW_AND_RUN_MINIMUM_SMOKE_TESTS_FIRST
```
