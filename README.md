# Galax AI Project

Galax AI is being designed as a fact-checked, strictly sequential CrewAI multi-agent software-development assistant system.

## Current Phase

The repository is in planning, research, conflict-reconciliation, and minimum-runtime validation mode. Agent roles, tools, LLMs, prompts, knowledge, memory, Docker infrastructure, and execution behavior are not final until individually researched, implemented, live-tested, audited, and approved.

## Current Readiness Decision

```yaml
full_build_prompt_status: BLOCKED_NOT_READY_TO_PROMPT_CREWAI
current_master_prompt_status: DO_NOT_USE_STALE_CONFLICTS
full_free_runtime_proven: false
agents_enabled: 0
production_ready: false
```

Do not execute the complete Galax build prompt. The architecture is technically possible, but the exact CrewAI + LLM + GitHub/Drive/memory gateways + Docker/sandbox chain has not passed the minimum integration tests.

Canonical current records:

- `docs/research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md`
- `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`
- `docs/plan/LLM_ASSIGNMENT_PLAN_DRAFT.md`
- `docs/sources/SOURCE_INDEX.md`
- `docs/research/readiness/FINAL_FREE_TIER_READINESS_AUDIT_2026-07-20.md`

## Canonical Decision Priority

When an older draft conflicts with a newer record, use:

```text
README current readiness
→ final pre-prompt conflict audit
→ full CrewAI 1.15.4 remediation blueprint
→ validated LLM routing/failover rule
→ corrected LLM assignment plan
→ framework/provider/tool source cards
→ older historical research
```

Historical files remain evidence. They cannot reactivate Cerebras, Notion-primary runtime memory, generic MCP exposure, CrewAI planning, CrewAI reasoning, native CrewAI memory, direct-main writes, automatic merge, or privileged Docker-in-Docker.

## Required Reading Order

Before changing or implementing any agent, LLM, tool, prompt, knowledge source, memory behavior, infrastructure, or workflow:

1. Read `README.md`.
2. Read the final pre-prompt conflict audit.
3. Read the full CrewAI 1.15.4 remediation blueprint.
4. Read all applicable files under `docs/rules/`.
5. Read the applicable files under `docs/plan/`.
6. Read `docs/sources/SOURCE_INDEX.md` and exact source cards.
7. Read the current agent record under `docs/research/agents/`.
8. Verify current facts using authoritative sources and exact pinned source code/adapters.
9. Inspect current official issues/security notices when documentation is insufficient.
10. Define and pass live tests in the exact pinned environment.
11. Only then prepare or execute an approved change.

## Meaning of 100% Fact-Checked

Galax does not promise perfect AI behavior. The allowed claim is:

```text
100% of the defined documentation, source-code or adapter, compatibility,
security, and live execution tests passed for the exact pinned environment
and recorded date.
```

Any material fingerprint change returns affected capabilities to `REVALIDATION_REQUIRED`.

## Non-Negotiable Capability Gate

```text
Never assign a CrewAI agent work that the complete verified runtime cannot perform.
```

A task requires verified support from:

```text
CrewAI framework and exact version
+ exact agent prompt/task/output contract
+ exact LLM/provider profile
+ exactly one assigned role-specific tool interface
+ required permissions and data classification
+ deterministic Flow and stage ordering
+ knowledge and memory context when required
+ Docker/sandbox boundary when required
+ hooks, guardrails, invocation evidence, and checkpoint
+ live tests
+ human approval when required
```

If any layer is missing, incompatible, or unverified:

```text
STATUS: BLOCKED_UNSUPPORTED_CAPABILITY
```

The agent must not simulate success, fabricate tool output, invent missing evidence, or claim it studied content that was never retrieved.

## Exact-Duplicate Rule

Exact normalized duplicates are reduced to one canonical record only after every reference is updated and removal is safely verified. Similar records with materially different roles, permissions, inputs, outputs, workflow stages, or historical evidence may remain.

## Current CrewAI Direction

```yaml
framework_candidate: CrewAI_1.15.4
python_candidate: '>=3.10,<3.14'
process: Process.sequential
active_agent_count: 1
concurrent_LLM_calls: 1
planning: false
reasoning: false
memory: false
allow_delegation: false
allow_code_execution: false
async_tasks: false
parallel_tool_calls: false
respect_context_window: false
framework_status: SELECTED_FOR_PINNED_VALIDATION_NOT_APPROVED
```

CrewAI is the agent/Flow framework. It is not the GitHub API, Google Drive API, database, Docker orchestrator, secure code sandbox, or correctness guarantee.

### Why planning and reasoning are disabled

- CrewAI `planning=True` adds an AgentPlanner call and defaults to an OpenAI planning model unless explicitly changed.
- CrewAI `reasoning=True` adds a separate refinement loop, and CrewAI documents that task execution can continue when that reasoning stage fails.
- Galax uses provider-native `reasoning_effort`, explicit structured planning/requirements tasks, and deterministic Flow validation instead.

## Governance and Evidence Direction

CrewAI 1.15.4 tool and model hooks are selected for validation:

```text
PRE_MODEL_CALL → profile, data, secret, context, and capacity gate
POST_MODEL_CALL → usage and redaction evidence
PRE_TOOL_CALL → agent/tool/operation/path/permission gate
POST_TOOL_CALL → raw result and invocation evidence
```

Hooks are not the final authority. A blocked tool hook may return control to the agent, and hook implementation errors can be unsafe if not wrapped correctly. Typed tool results, deterministic task guardrails, a Flow stop transition, and an append-only invocation ledger are required.

An agent cannot claim a tool ran without a trusted invocation ID. CrewAI issue #3154 is retained as risk evidence for fabricated Action/Observation text.

## Current GitHub Repository Direction

```yaml
GithubSearchTool:
  semantic_read_search: supported
  GitHub_write_commit_PR: unsupported

FileWriterTool:
  local_filesystem_write: supported
  GitHub_commit_push_PR: unsupported

CrewAI_MCP_adapter:
  external_MCP_tools: supported
  exact_tool_filtering: supported

Official_GitHub_MCP_Server:
  repository_read_write: supported_with_GitHub_permissions
  push_files_single_commit: supported
  direct_Galax_agent_exposure: rejected
  Galax_live_tested: false
```

The official GitHub MCP `push_files` schema does not require an expected branch-head SHA. Galax therefore uses a trusted role-scoped gateway that verifies branch/blob hashes and performs an optimistic-concurrency Git Database transaction.

```text
one role-scoped CrewAI tool
→ trusted repository gateway
→ GitHub API or filtered GitHub MCP operation
→ dedicated run branch
→ expected-head verification
→ one verified commit
→ QA/security/audit
→ trusted Flow creates or updates a draft PR
```

Direct writes to `main`, force push, automatic merge, broad deletion, workflow/secret changes, and unrestricted GitHub tokens are prohibited.

## MCP Security Direction

Current CrewAI issue #6504 reports MCP URL-argument SSRF and DNS-rebinding risks; PR #6519 is an open proposed fix. Until a patched version is pinned and tested:

```yaml
generic_remote_MCP: prohibited
arbitrary_URL_MCP_tools: prohibited
full_MCP_tool_catalog_to_agents: prohibited
local_role_scoped_gateway: required
URL_domain_and_IP_validation: required
private_link_local_metadata_IPs: blocked
write_retry: zero_automatic_retries
```

## Corrected LLM Direction

### Bounded low/medium private work

```yaml
primary_candidate: groq/openai/gpt-oss-20b
hosted_fallback_candidate: cloudflare/@cf/openai/gpt-oss-20b
optional_local_fallback: ollama/gpt-oss:20b
status: DISABLED_PENDING_PER_AGENT_TESTS
```

### High-complexity private work

```yaml
primary_candidate: groq/openai/gpt-oss-120b
hosted_fallback_candidate: cloudflare/@cf/openai/gpt-oss-120b
status: DISABLED_PENDING_PER_AGENT_TESTS
```

### Public or fully redacted long context

```yaml
candidate: gemini/gemini-2.5-flash
private_repository_content: prohibited_on_free_tier
status: DISABLED_PENDING_TESTS
```

### Removed active candidate

```yaml
provider: Cerebras
model: cerebras/gpt-oss-120b
status: REJECTED_TRIAL_ONLY
```

The same model/provider must pass a separate `agent + prompt + task + tool + output + data-class` test suite for every agent. Provider switching is deterministic Flow behavior only and is prohibited during non-idempotent operations.

## Current 15-Agent Direction

The roster remains unchanged. Exact candidate LLM classes, one-tool interfaces, restrictions, and remedies for all 15 agents are defined in:

```text
docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
```

No agent after Agent 01 may be implemented or enabled before Agent 01, governance hooks, invocation evidence, canonical checkpointing, and the foundation tests pass.

## Knowledge Direction

- Owner tutorials and copied website materials live in approved Google Drive folders.
- File titles are not trusted as the primary relevance signal.
- A controlled Drive gateway searches metadata and body text, reads related files, checks version/conflicts, and produces a verified `LearningPacket`.
- A selected agent produces a validated `StudyReceipt` before knowledge-dependent write work.
- Copied web content is untrusted and cannot override repository rules or permissions.
- Drive credentials are never exposed to agents.
- The gateway is specified but not implemented or live-tested.

## Memory Direction

- Supabase Postgres is selected for validation as primary machine/runtime memory.
- Keyword/exact-filter retrieval comes before embeddings.
- Notion is an optional curated human-readable mirror.
- Neither is claimed as native CrewAI memory.
- Trusted Flow infrastructure queries and writes memory; agents receive bounded validated `MemoryContext` only.
- GitHub/current evidence outranks memory.
- CrewAI native memory remains disabled.

## Docker and Sandbox Direction

- Galax application services may run in Docker Compose.
- Services must be non-root, read-only where possible, capability-dropped, resource-limited, health-checked, and use service-specific secrets.
- Privileged Docker-in-Docker and unrestricted Docker socket mounts are rejected.
- Coding/test agents require a separate rootless sandbox daemon or host through their one role-specific workspace tool.
- The Docker stack and sandbox remain unimplemented and untested.

## Automatic Revalidation

Changes to CrewAI, provider SDK/LiteLLM, model/API behavior, agent prompt, task/output schema, tool schema, hooks, permissions, repository structure, provider limits/allocation, security rules, memory schema, or Docker image/configuration fingerprints set affected capabilities to:

```text
REVALIDATION_REQUIRED
```

The Flow disables affected profiles and may run Agent 03 in a separate official-source research stage. Research never automatically enables implementation.

## Minimum Gate Before the Full Build Prompt

```text
1. Reconcile every stale active Cerebras and Notion-primary instruction.
2. Pin Python, CrewAI, crewai-tools, MCP/mcpadapt, and provider integrations.
3. Build and audit the base Docker image.
4. Implement typed statuses, invocation ledger, and fail-closed manual checkpoint.
5. Implement and test PRE/POST model and tool governance hooks.
6. Start/stop and inspect the pinned GitHub MCP Server; do not expose its full catalog.
7. Implement and test RepositoryPreflightTool and Agent 01.
8. Prove authorized run-branch read/write and reject direct-main/force/secret/role violations.
9. Test Groq 20B and 120B separately through CrewAI.
10. Test Cloudflare 20B and 120B separately through CrewAI custom OpenAI mode.
11. Test Gemini only with public/redacted fixtures and qualify Ollama hardware.
12. Pass a real two-agent read-only Process.sequential smoke test.
13. Implement Drive LearningPacket/StudyReceipt.
14. Implement Supabase memory, backup, RLS, and bounded retrieval.
15. Implement the external sandbox, then research/implement Agents 02–15 one at a time.
```

The complete implementation prompt may be prepared only after all required gates for the exact requested scope pass.

No agent is approved unless its decision record explicitly says:

```text
APPROVED_FOR_IMPLEMENTATION
```
