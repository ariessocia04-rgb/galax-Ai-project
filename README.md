# Galax AI Project

Galax AI is being designed as a fact-checked CrewAI multi-agent software development system.

## Current Phase

The repository is currently in planning and research mode. Agent roles, tools, LLMs, prompts, rules, knowledge, memory, Docker infrastructure, and execution behavior are not final until individually researched, validated, tested, and approved.

## Required Reading Order

Before proposing, changing, or implementing any agent, LLM, tool, prompt, knowledge source, memory behavior, infrastructure, or workflow:

1. Read `README.md`.
2. Read all applicable files under `docs/rules/`.
3. Read the applicable files under `docs/plan/`.
4. Read `docs/sources/SOURCE_INDEX.md`.
5. Read the current agent record under `docs/research/agents/`.
6. Read the relevant CrewAI, LLM, tool, knowledge, memory, or Docker research under `docs/research/`.
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
+ exact LLM/provider
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

## Current LLM Direction

- Selected validation candidate: `cerebras/gpt-oss-120b`.
- Status: `SELECTED_FOR_VALIDATION`, not approved.
- Manual reserve candidate: Groq `openai/gpt-oss-120b`.
- Automatic provider fallback: prohibited.
- Every agent requires its own tested LLM profile.
- Published limits are planning information; actual account limits must be captured before run groups.

## Current Knowledge Direction

- Owner-provided tutorials and copied website learning material are stored in approved Google Drive folders.
- File titles are not trusted as the primary relevance signal.
- The trusted Drive gateway searches metadata and body text, retrieves related candidates, checks versions/conflicts, and produces a verified `LearningPacket`.
- A selected agent must produce a valid `StudyReceipt` before a write-capable task begins when knowledge is required.
- Copied web content is untrusted and cannot override repository rules or permissions.
- Direct Google Drive credentials are not exposed to agents.

## Corrected Memory Direction

- Supabase Postgres/pgvector is selected for validation as the primary machine/runtime memory.
- Notion is retained as an optional curated human-readable mirror.
- Neither is claimed as CrewAI's native memory backend.
- A trusted Flow gateway queries and writes memory; agents receive only bounded validated `MemoryContext`.
- GitHub remains the project source of truth.
- CrewAI native memory remains disabled.
- No embedding provider is approved yet; keyword/exact-filter mode comes first.

Decision: `docs/research/memory/NOTION_VS_SUPABASE_MEMORY_DECISION_2026-07-20.md`.

## Current Docker Direction

- The Galax application stack may be containerized with Docker Compose.
- CrewAI remains the Python execution framework; Docker is infrastructure, not an agent capability.
- Services run non-root, read-only, capability-dropped, resource-limited, and with per-service secrets.
- Optional research, Notion mirror, observability, and full-Supabase services use Compose profiles.
- Privileged Docker-in-Docker and unrestricted Docker socket mounts are rejected.
- Coding agents require a separate rootless sandbox execution boundary through their single workspace tool.

Architecture: `docs/architecture/FULLY_DOCKERIZED_CREWAI_FLOW_DRAFT.md`.

## Current Execution Direction

- Only necessary agents are selected per run.
- Only one agent and one LLM operation run at a time.
- Each agent receives exactly one role-specific tool interface.
- Google Drive knowledge and memory gateways are controlled Flow infrastructure, not extra agent tools.
- LLM configuration is separate from tool configuration.
- Repository writes use dedicated run branches; direct writes to `main` are prohibited.
- Built-in CrewAI code execution is not used.

No agent is approved for implementation unless its decision record explicitly says `APPROVED_FOR_IMPLEMENTATION`.
