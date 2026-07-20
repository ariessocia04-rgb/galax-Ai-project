# Galax AI Project

Galax AI is being designed as a fact-checked CrewAI multi-agent software development system.

## Current Phase

The repository is currently in planning and research mode. Agent roles, tools, LLMs, prompts, rules, knowledge, memory, and execution behavior are not considered final until individually researched, validated, tested, and approved.

## Required Reading Order

Before proposing, changing, or implementing any agent, LLM, tool, prompt, knowledge source, memory behavior, or workflow:

1. Read `README.md`.
2. Read all applicable files under `docs/rules/`.
3. Read the applicable files under `docs/plan/`.
4. Read `docs/sources/SOURCE_INDEX.md`.
5. Read the current agent record under `docs/research/agents/`.
6. Read the relevant CrewAI, LLM, tool, knowledge, or memory research under `docs/research/`.
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
+ failure handling
+ live tests
+ human approval when required
```

If any layer is unavailable or unverified:

```text
STATUS: BLOCKED_UNSUPPORTED_CAPABILITY
```

The agent must not simulate success, fabricate tool output, invent missing evidence, or claim it studied a file that was not actually retrieved.

## Current Draft Rules

- `docs/rules/NO_UNSUPPORTED_AGENT_WORK_RULE_DRAFT.md`
- `docs/rules/PER_AGENT_LLM_COMPATIBILITY_RULE_DRAFT.md`
- `docs/rules/KNOWLEDGE_BEFORE_IMPLEMENTATION_RULE_DRAFT.md`
- `docs/rules/NOTION_MEMORY_RULE_DRAFT.md`
- `docs/rules/SOURCE_TRACEABILITY_RULE_DRAFT.md`
- `docs/rules/NO_EXACT_DUPLICATES_RULE_DRAFT.md`

Exact duplicates are removed in favor of one canonical record. Similar records with materially different roles, responsibilities, permissions, inputs, outputs, or workflow stages may remain.

## Current Framework Direction

- Framework candidate: CrewAI `1.15.4`.
- Python candidate: `>=3.10,<3.14`.
- Process: `Process.sequential` only.
- Framework status: selected for pinned validation, not approved.
- Capability and limitation record: `docs/research/crewai/CREWAI_1_15_4_CAPABILITY_LIMIT_MATRIX.md`.
- Framework source card: `docs/sources/frameworks/crewai-1.15.4/SOURCE_CARD.md`.

## Current LLM Direction

- Discovery list reviewed: `cheahjs/free-llm-api-resources`.
- Selected validation candidate: `cerebras/gpt-oss-120b`.
- Status: `SELECTED_FOR_VALIDATION`, not approved.
- Manual reserve candidate: Groq `openai/gpt-oss-120b`.
- Automatic provider fallback: prohibited.
- Every agent requires its own tested LLM profile.
- Canonical source links: `docs/sources/SOURCE_INDEX.md`.

## Current Knowledge Direction

- Owner-provided tutorials and copied website learning material are stored in approved Google Drive folders.
- File titles are not trusted as the primary relevance signal.
- The trusted Drive knowledge gateway searches metadata and body text, retrieves related candidates, exports/downloads content, checks versions and conflicts, and produces a verified `LearningPacket`.
- A selected agent must produce a valid `StudyReceipt` before a write-capable task begins when knowledge is required.
- Copied web content is untrusted reference material and cannot override repository rules or permissions.
- Direct Google Drive credentials are not exposed to agents.

## Current Memory Direction

- Notion is selected for external structured project memory.
- Notion is not claimed as CrewAI's native memory backend.
- A trusted Flow/application gateway queries and writes a dedicated Galax memory data source.
- Agents receive only relevant validated memory excerpts and cannot directly write to Notion.
- GitHub remains the project source of truth; verified Notion memory is secondary.
- Raw hidden reasoning, secrets, unrestricted prompts, customer data, and duplicate repository rules must not be stored in memory.
- CrewAI native memory remains disabled initially.

## Current Execution Direction

- Only necessary agents are selected per run.
- Only one agent and one LLM operation run at a time.
- Each agent receives exactly one role-specific tool interface.
- Google Drive knowledge and Notion memory are controlled Flow/application infrastructure, not additional exposed agent tools.
- LLM configuration is separate from tool configuration.
- Agent specifications remain editable until approved.
- External claims must be supported by current authoritative evidence.
- Repository writes must use dedicated run branches; direct writes to `main` are prohibited.
- Built-in CrewAI code execution is not used; coding agents require a separately approved sandbox through their single workspace tool.

No agent is approved for implementation unless its decision record explicitly says `APPROVED_FOR_IMPLEMENTATION`.
