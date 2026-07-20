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
6. Read the relevant LLM or tool research under `docs/research/`.
7. Verify current external facts using authoritative sources.
8. Only then prepare or execute an approved change.

## Current Draft Rules

- `docs/rules/SOURCE_TRACEABILITY_RULE_DRAFT.md`
- `docs/rules/NO_EXACT_DUPLICATES_RULE_DRAFT.md`

Exact duplicates are removed in favor of one canonical record. Similar records with materially different roles, responsibilities, permissions, inputs, outputs, or workflow stages may remain.

## Current LLM Direction

- Discovery list reviewed: `cheahjs/free-llm-api-resources`.
- Selected validation candidate: `cerebras/gpt-oss-120b`.
- Status: `SELECTED_FOR_VALIDATION`, not approved.
- Manual reserve candidate: Groq `openai/gpt-oss-120b`.
- Automatic provider fallback: prohibited.
- Canonical source links: `docs/sources/SOURCE_INDEX.md`.

## Current Execution Direction

- CrewAI process: sequential.
- Only necessary agents are selected per run.
- Only one agent and one LLM operation run at a time.
- Each agent receives exactly one role-specific tool interface.
- LLM configuration is separate from tool configuration.
- Agent specifications remain editable until approved.
- External claims must be supported by current authoritative evidence.
- Repository writes must use dedicated run branches; direct writes to `main` are prohibited.

No agent is approved for implementation unless its decision record explicitly says `APPROVED_FOR_IMPLEMENTATION`.
