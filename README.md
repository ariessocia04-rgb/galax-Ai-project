# Galax AI Project

Galax AI is being designed as a fact-checked CrewAI multi-agent software development system.

## Current Phase

The repository is currently in planning and research mode. Agent roles, tools, LLMs, prompts, rules, and execution behavior are not considered final until individually researched, validated, tested, and approved.

## Required Reading Order

Before proposing, changing, or implementing any agent, LLM, tool, prompt, or workflow:

1. Read `README.md`.
2. Read all applicable files under `docs/rules/`.
3. Read the applicable files under `docs/plan/`.
4. Read `docs/sources/SOURCE_INDEX.md`.
5. Read the current agent record under `docs/research/agents/`.
6. Read the relevant CrewAI, LLM, or tool research under `docs/research/`.
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
+ failure handling
+ live tests
+ human approval when required
```

If any layer is unavailable or unverified:

```text
STATUS: BLOCKED_UNSUPPORTED_CAPABILITY
```

The agent must not simulate success, fabricate tool output, or invent missing evidence.

## Current Draft Rules

- `docs/rules/NO_UNSUPPORTED_AGENT_WORK_RULE_DRAFT.md`
- `docs/rules/PER_AGENT_LLM_COMPATIBILITY_RULE_DRAFT.md`
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
- Canonical source links: `docs/sources/SOURCE_INDEX.md`.

## Current Execution Direction

- Only necessary agents are selected per run.
- Only one agent and one LLM operation run at a time.
- Each agent receives exactly one role-specific tool interface.
- LLM configuration is separate from tool configuration.
- Agent specifications remain editable until approved.
- External claims must be supported by current authoritative evidence.
- Repository writes must use dedicated run branches; direct writes to `main` are prohibited.
- Built-in CrewAI code execution is not used; coding agents require a separately approved sandbox through their single workspace tool.
- CrewAI memory is disabled initially; repository records and Flow state remain the source of truth.

No agent is approved for implementation unless its decision record explicitly says `APPROVED_FOR_IMPLEMENTATION`.
