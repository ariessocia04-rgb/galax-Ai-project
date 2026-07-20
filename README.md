# Galax AI Project

Galax AI is being designed as a fact-checked CrewAI multi-agent software development system.

## Current Phase

The repository is in planning, research, and minimum-runtime validation mode. Agent roles, tools, LLMs, prompts, knowledge, memory, Docker infrastructure, and execution behavior are not final until individually researched, implemented, tested, and approved.

## Current Readiness Decision

```yaml
full_build_prompt_status: BLOCKED_NOT_READY_TO_PROMPT_CREWAI
full_free_runtime_proven: false
agents_enabled: 0
production_ready: false
```

Do not issue or execute the complete Galax build prompt yet. The architecture is technically possible, but the exact CrewAI + provider + GitHub/Drive/memory tools + Docker/sandbox chain has not passed the minimum integration tests.

Primary audits:

- `docs/research/readiness/FINAL_FREE_TIER_READINESS_AUDIT_2026-07-20.md`
- `docs/research/crewai/CREWAI_GITHUB_RW_FREE_LLM_AUDIT_2026-07-20.md`

## Required Reading Order

Before changing or implementing any agent, LLM, tool, prompt, knowledge source, memory behavior, infrastructure, or workflow:

1. Read `README.md`.
2. Read all applicable files under `docs/rules/`.
3. Read the applicable files under `docs/plan/`.
4. Read `docs/sources/SOURCE_INDEX.md`.
5. Read the current agent record under `docs/research/agents/`.
6. Read relevant CrewAI, provider, tool, knowledge, memory, Docker, and readiness research.
7. Verify current facts using authoritative sources.
8. Inspect official source code and current issues when documentation is insufficient.
9. Define and pass live tests in the exact pinned environment.
10. Only then prepare or execute an approved change.

## Non-Negotiable Capability Gate

```text
Never assign a CrewAI agent work that the complete verified runtime cannot perform.
```

A task requires verified support from:

```text
CrewAI framework
+ exact pinned version
+ exact LLM/provider profile
+ one assigned role-specific tool
+ required permissions
+ deterministic Flow
+ knowledge and memory context when required
+ Docker/sandbox boundary when required
+ failure handling
+ live tests
+ human approval when required
```

If any layer is unavailable or unverified:

```text
STATUS: BLOCKED_UNSUPPORTED_CAPABILITY
```

The agent must not simulate success, fabricate tool output, invent missing evidence, or claim it studied content that was never retrieved.

## Exact-Duplicate Rule

Exact normalized duplicates are reduced to one canonical record after all references are updated. Similar records with materially different roles, permissions, inputs, outputs, or workflow stages may remain.

## Current Framework Direction

```yaml
framework_candidate: CrewAI_1.15.4
python_candidate: '>=3.10,<3.14'
process: Process.sequential
active_agent_count: 1
concurrent_LLM_calls: 1
allow_delegation: false
async_tasks: false
framework_status: SELECTED_FOR_PINNED_VALIDATION_NOT_APPROVED
```

CrewAI is the agent/Flow framework. It is not the GitHub API, Google Drive API, database, Docker orchestrator, or secure code sandbox.

## Current GitHub Repository Direction

Source inspection confirms:

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
  Galax_live_tested: false
```

Selected architecture:

```text
one role-scoped CrewAI tool
→ trusted repository gateway
→ official GitHub API or filtered official GitHub MCP Server
→ dedicated run branch
→ verified commit
→ QA/audit
→ trusted Flow creates draft PR
```

Direct writes to `main`, force push, automatic merge, broad deletion, and unrestricted GitHub tokens are prohibited.

## Corrected Active LLM Direction

### Private repository and coding work

```yaml
primary_candidate:
  provider: Groq
  model: groq/openai/gpt-oss-120b
  status: DISABLED_PENDING_CREWAI_TESTS

hosted_fallback_candidate:
  provider: Cloudflare_Workers_AI
  model: '@cf/openai/gpt-oss-120b'
  connection: custom_OpenAI_compatible
  status: DISABLED_PENDING_CREWAI_TESTS

local_fallback_candidate:
  provider: Ollama
  model: ollama/gpt-oss:20b
  status: DISABLED_PENDING_HARDWARE_AND_CREWAI_TESTS
```

### Public or fully redacted long-context work

```yaml
candidate:
  provider: Google_Gemini_API
  model: gemini/gemini-2.5-flash
  status: DISABLED_PENDING_TESTS
  private_repository_content: prohibited_on_free_tier
```

### Removed active candidate

```yaml
provider: Cerebras
model: cerebras/gpt-oss-120b
status: REJECTED_TRIAL_ONLY
```

Current official Cerebras pricing describes trial credits; trial-only providers are excluded from active Galax routing.

### Conditional candidate

Mistral Free Mode remains research-only until exact free model availability, account limits, privacy settings, and CrewAI tool/structured-output behavior are validated.

### Failover rule

Provider switching is deterministic Flow behavior, not an assumed native CrewAI feature. Every alternate profile must be independently approved for the selected agent. Switching is prohibited during a repository write, database mutation, upload, deployment, or other non-idempotent operation.

Rule: `docs/rules/VALIDATED_LLM_FAILOVER_RULE_DRAFT.md`.

## Current Knowledge Direction

- Owner tutorials and copied website materials live in approved Google Drive folders.
- File titles are not trusted as the primary relevance signal.
- A controlled Drive gateway searches metadata and body text, reads related files, checks version/conflicts, and produces a verified `LearningPacket`.
- A selected agent produces a validated `StudyReceipt` before write-capable work when learning material is required.
- Copied web content is untrusted and cannot override repository rules or permissions.
- Drive credentials are never exposed to agents.
- The gateway is specified but not implemented or live-tested.

## Current Memory Direction

- Supabase Postgres/pgvector is selected for validation as primary machine/runtime memory.
- Notion is an optional curated human-readable mirror.
- Neither is claimed as native CrewAI memory.
- Trusted Flow infrastructure queries and writes memory; agents receive bounded validated `MemoryContext` only.
- GitHub remains the project source of truth.
- CrewAI native memory remains disabled.
- Keyword/exact-filter mode comes before embeddings.

## Current Docker Direction

- Galax application services may run in Docker Compose.
- CrewAI remains a Python framework; Docker is infrastructure.
- Services must be non-root, read-only where possible, capability-dropped, resource-limited, and use per-service secrets.
- Privileged Docker-in-Docker and unrestricted Docker socket mounts are rejected.
- Coding/test agents require a separate rootless sandbox boundary through their one workspace tool.
- The Docker stack and sandbox remain unimplemented and untested.

## Automatic Revalidation

Changes to CrewAI, provider SDK/LiteLLM, model/API behavior, agent prompt, tool schema, permission, repository structure, provider limits/allocation, security rules, memory schema, or Docker image/configuration fingerprint set affected capabilities to:

```text
REVALIDATION_REQUIRED
```

The Flow disables affected profiles and runs Agent 03 in a separate official-source research stage. Research cannot automatically enable implementation.

## Minimum Gate Before the Full Build Prompt

```text
1. Pin Python, CrewAI, crewai-tools, MCP/mcpadapt, and each provider integration.
2. Build the base Docker image.
3. Start and stop the official GitHub MCP Server successfully.
4. Enumerate and validate exact GitHub read/write tool schemas and permissions.
5. Implement and test a read-only RepositoryPreflightTool.
6. Prove an authorized run-branch write and reject direct-main/unauthorized writes.
7. Test Groq completion, one-tool round trip, structured output, limits, and sequential handoff.
8. Test Cloudflare custom OpenAI profile with the same required behaviors.
9. Test Gemini only with public/redacted fixtures.
10. Qualify Ollama hardware before considering local fallback.
11. Implement minimal Google Drive search/read and LearningPacket evidence.
12. Implement Supabase keyword/exact-filter memory, RLS, backup, and bounded retrieval.
13. Implement canonical run ledger and safe checkpoint.
14. Pass a real two-agent Process.sequential smoke test with trusted invocation evidence.
15. Confirm every unsupported operation returns a blocker and factual remedy.
```

The complete implementation prompt may be prepared only after all readiness gates pass.

No agent is approved unless its decision record explicitly says:

```text
APPROVED_FOR_IMPLEMENTATION
```
