# Galax AI Project

Galax AI is being designed as a fact-checked CrewAI multi-agent software development system.

## Current Phase

The repository is currently in planning, research, and minimum-runtime validation mode. Agent roles, tools, LLMs, prompts, rules, knowledge, memory, Docker infrastructure, and execution behavior are not final until individually researched, implemented, tested, and approved.

## Current Readiness Decision

```yaml
full_build_prompt_status: BLOCKED_NOT_READY_TO_PROMPT_CREWAI
full_free_tier_runtime_proven: false
agents_enabled: 0
production_ready: false
```

Do not issue or execute the complete Galax build prompt yet. The current architecture is technically possible, but the exact CrewAI + LiteLLM + provider + tool + Docker + knowledge + memory chain has not passed the minimum integration tests.

Readiness audit:

- `docs/research/readiness/FINAL_FREE_TIER_READINESS_AUDIT_2026-07-20.md`

## Required Reading Order

Before proposing, changing, or implementing any agent, LLM, tool, prompt, knowledge source, memory behavior, infrastructure, or workflow:

1. Read `README.md`.
2. Read all applicable files under `docs/rules/`.
3. Read the applicable files under `docs/plan/`.
4. Read `docs/sources/SOURCE_INDEX.md`.
5. Read the current agent record under `docs/research/agents/`.
6. Read the relevant CrewAI, LLM, tool, knowledge, memory, Docker, or readiness research under `docs/research/`.
7. Verify current external facts using authoritative sources.
8. Inspect relevant official source code and current official issues when documentation is insufficient.
9. Define and pass the required live tests in the exact pinned environment.
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

The agent must not simulate success, fabricate tool output, invent missing evidence, or claim it studied a file that was not actually retrieved.

## Automatic Revalidation

Changes to CrewAI, LiteLLM, Cerebras API/model behavior, agent prompts, tool schemas, permissions, repository structure, provider limits, security rules, memory schemas, or Docker image/configuration fingerprints set affected capabilities to:

```text
REVALIDATION_REQUIRED
```

The deterministic Flow disables affected agents and starts Agent 03 in a separate research stage with one temporary-lifecycle, official-source-only research interface. Research does not automatically enable implementation.

Rule: `docs/rules/AUTOMATIC_REVALIDATION_RESEARCH_RULE_DRAFT.md`.

## Current Draft Rules

- `docs/rules/NO_UNSUPPORTED_AGENT_WORK_RULE_DRAFT.md`
- `docs/rules/PER_AGENT_LLM_COMPATIBILITY_RULE_DRAFT.md`
- `docs/rules/VALIDATED_LLM_FAILOVER_RULE_DRAFT.md`
- `docs/rules/FREE_TIER_CAPACITY_SNAPSHOT_RULE_DRAFT.md`
- `docs/rules/KNOWLEDGE_BEFORE_IMPLEMENTATION_RULE_DRAFT.md`
- `docs/rules/SUPABASE_PRIMARY_MEMORY_NOTION_MIRROR_RULE_DRAFT.md`
- `docs/rules/NOTION_MEMORY_RULE_DRAFT.md` — retained only for Notion mirror details where not superseded
- `docs/rules/AUTOMATIC_REVALIDATION_RESEARCH_RULE_DRAFT.md`
- `docs/rules/SOURCE_TRACEABILITY_RULE_DRAFT.md`
- `docs/rules/NO_EXACT_DUPLICATES_RULE_DRAFT.md`

Exact duplicates are removed in favor of one canonical record. Similar records with materially different roles, responsibilities, permissions, inputs, outputs, or workflow stages may remain.

## Current Framework Direction

- Framework candidate: CrewAI `1.15.4`.
- Python candidate: `>=3.10,<3.14`.
- Process: `Process.sequential` only.
- Framework status: selected for pinned validation, not approved.
- Capability record: `docs/research/crewai/CREWAI_1_15_4_CAPABILITY_LIMIT_MATRIX.md`.
- Exact CrewAI + LiteLLM dependency pair has not yet passed the Galax Docker integration tests.

## Current LLM Direction

### Primary candidate

```yaml
provider: Cerebras
model: cerebras/gpt-oss-120b
status: DISABLED_PENDING_API_V2_AND_ACCOUNT_TESTS
```

### Controlled fallback candidate

```yaml
provider: Groq
model: groq/openai/gpt-oss-120b
status: DISABLED_PENDING_SEPARATE_TESTS
```

Rules:

- A free-tier or trial primary profile requires a separately validated fallback.
- Provider switching is never silent.
- The fallback cannot run until its own per-agent tool-calling, structured-output, rate-limit, security, and sequential-context tests pass.
- OpenRouter free models may be researched but are not the automatic fallback because free availability and routing can change.
- Every agent requires its own tested LLM profile.

### Free-tier capacity correction

Published model capacity is not automatically the usable free-tier capacity.

Cerebras documentation exposes a model capacity up to 131,072 tokens, while its pricing information states an 8,192-token free-tier context. Until the connected account and API Version 2 are tested:

```yaml
provisional_effective_total_context: 8192
previous_12000_to_20000_input_limits: suspended
capacity_status: BLOCKED_CAPACITY_UNKNOWN
```

The runtime must capture the current account limits before every run group and compute the effective capacity as the minimum of model, plan/account, temporary provider limits, and Galax safety ceilings.

## Current Knowledge Direction

- Owner-provided tutorials and copied website learning material are stored in approved Google Drive folders.
- File titles are not trusted as the primary relevance signal.
- The trusted Drive gateway searches metadata and body text, retrieves related candidates, checks versions/conflicts, and produces a verified `LearningPacket`.
- A selected agent must produce a valid `StudyReceipt` before a write-capable task begins when knowledge is required.
- Copied web content is untrusted and cannot override repository rules or permissions.
- Direct Google Drive credentials are not exposed to agents.
- The Drive gateway is specified but not implemented or live tested.

## Corrected Memory Direction

- Supabase Postgres/pgvector is selected for validation as the primary machine/runtime memory.
- Notion is retained as an optional curated human-readable mirror.
- Neither is claimed as CrewAI's native memory backend.
- A trusted Flow gateway queries and writes memory; agents receive only bounded validated `MemoryContext`.
- GitHub remains the project source of truth.
- CrewAI native memory remains disabled.
- No embedding provider is approved yet; keyword/exact-filter mode comes first.
- Supabase schema, RLS, backup, retrieval, and Flow integration are not implemented or live tested.

Decision: `docs/research/memory/NOTION_VS_SUPABASE_MEMORY_DECISION_2026-07-20.md`.

## Current Docker Direction

- The Galax application stack may be containerized with Docker Compose.
- CrewAI remains the Python execution framework; Docker is infrastructure, not an agent capability.
- Services run non-root, read-only, capability-dropped, resource-limited, and with per-service secrets.
- Optional research, Notion mirror, observability, and full-Supabase services use Compose profiles.
- Privileged Docker-in-Docker and unrestricted Docker socket mounts are rejected.
- Coding agents require a separate rootless sandbox execution boundary through their single workspace tool.
- The Docker stack and sandbox are designed but not implemented or security tested.

Architecture: `docs/architecture/FULLY_DOCKERIZED_CREWAI_FLOW_DRAFT.md`.

## Current Execution Direction

- Only necessary agents are selected per run.
- Only one agent and one LLM operation run at a time.
- Each agent receives exactly one role-specific tool interface.
- Google Drive knowledge and memory gateways are controlled Flow infrastructure, not extra agent tools.
- LLM configuration is separate from tool configuration.
- Repository writes use dedicated run branches; direct writes to `main` are prohibited.
- Built-in CrewAI code execution is not used.
- No automatic merge or production deployment is permitted.

## Minimum Gate Before the Full Build Prompt

```text
1. Pin Python, CrewAI, crewai-tools, and LiteLLM.
2. Build the base Docker image.
3. Test Cerebras API Version 2 directly.
4. Capture actual Cerebras account context and rate limits.
5. Test Cerebras through CrewAI/LiteLLM.
6. Test Groq through CrewAI/LiteLLM.
7. Approve deterministic fallback behavior.
8. Implement read-only repository preflight.
9. Implement minimal Google Drive search/read gateway.
10. Implement Supabase keyword/exact-filter memory gateway.
11. Implement run ledger and safe checkpoint.
12. Pass a minimal two-agent sequential Crew smoke test.
13. Produce trusted tool invocation evidence.
14. Confirm no direct main write or automatic merge.
15. Confirm every unsupported operation returns a blocker and remedy.
```

The complete implementation prompt may be prepared only after all 15 readiness gates pass.

No agent is approved for implementation unless its decision record explicitly says `APPROVED_FOR_IMPLEMENTATION`.
