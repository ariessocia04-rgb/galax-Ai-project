# Galax AI Source Index — Draft

**Status:** `DRAFT_MUTABLE`  
**Verified:** 2026-07-20

This index is the canonical human-readable entry point for agent, LLM, framework, and tool sources. It must contain links only to existing source cards.

## Agents

| Agent ID | Role | LLM | Tool | Status |
|---|---|---|---|---|
| [`engineering_manager`](agents/engineering_manager/SOURCE_CARD.md) | AI Engineering Manager and CrewAI Execution Planning Lead | [`cerebras/gpt-oss-120b`](llms/cerebras-gpt-oss-120b/SOURCE_CARD.md) | [`RepositoryPreflightTool`](tools/repository_preflight_tool/SOURCE_CARD.md) | `RESEARCHING` |

Agents 02–15 will be added only after their individual role, LLM profile, and tool inspections begin.

## Frameworks

| Source ID | Framework/version | Status | Official package source |
|---|---|---|---|
| [`FRAMEWORK-crewai-1.15.4`](frameworks/crewai-1.15.4/SOURCE_CARD.md) | CrewAI `1.15.4` | `SELECTED_FOR_PINNED_VALIDATION` | [CrewAI 1.15.4 on PyPI](https://pypi.org/project/crewai/) |

## LLMs

| Source ID | Provider/model | Status | Official model source |
|---|---|---|---|
| [`LLM-cerebras-gpt-oss-120b`](llms/cerebras-gpt-oss-120b/SOURCE_CARD.md) | Cerebras `gpt-oss-120b` | `SELECTED_FOR_VALIDATION` | [Cerebras public model metadata](https://inference-docs.cerebras.ai/api-reference/models/public-models) |
| [`LLM-groq-openai-gpt-oss-120b`](llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md) | Groq `openai/gpt-oss-120b` | `RESERVE_CANDIDATE_NOT_ACTIVE` | [Groq exact model page](https://console.groq.com/docs/model/openai/gpt-oss-120b) |

## Tools

| Source ID | Tool | Status | Official compatibility source |
|---|---|---|---|
| [`TOOL-repository-preflight`](tools/repository_preflight_tool/SOURCE_CARD.md) | `RepositoryPreflightTool` | `CONDITIONALLY_APPROVED` | [CrewAI custom tools](https://docs.crewai.com/learn/create-custom-tools) |

## Core rules

- [No unsupported agent work rule](../rules/NO_UNSUPPORTED_AGENT_WORK_RULE_DRAFT.md)
- [Per-agent LLM compatibility rule](../rules/PER_AGENT_LLM_COMPATIBILITY_RULE_DRAFT.md)
- [Source traceability rule](../rules/SOURCE_TRACEABILITY_RULE_DRAFT.md)
- [No exact duplicates rule](../rules/NO_EXACT_DUPLICATES_RULE_DRAFT.md)

## Research and plans

- [CrewAI 1.15.4 capability and limitation matrix](../research/crewai/CREWAI_1_15_4_CAPABILITY_LIMIT_MATRIX.md)
- [15-agent capability mapping](../plan/AGENT_CAPABILITY_MAPPING_DRAFT.md)
- [Free provider screening — 2026-07-20](../research/llms/FREE_PROVIDER_SCREENING_2026-07-20.md)
- [LLM assignment plan](../plan/LLM_ASSIGNMENT_PLAN_DRAFT.md)
- [GitHub repository read/write architecture](../architecture/GITHUB_REPOSITORY_READ_WRITE_DRAFT.md)

## Deterministic query mapping

The future source lookup command maps aliases as follows:

```yaml
aliases:
  engineering_manager: agents/engineering_manager/SOURCE_CARD.md
  AGENT-01: agents/engineering_manager/SOURCE_CARD.md
  agent_01: agents/engineering_manager/SOURCE_CARD.md
  crewai: frameworks/crewai-1.15.4/SOURCE_CARD.md
  crewai-1.15.4: frameworks/crewai-1.15.4/SOURCE_CARD.md
  cerebras-gpt-oss-120b: llms/cerebras-gpt-oss-120b/SOURCE_CARD.md
```

Expected queries:

```text
source engineering_manager
source crewai
source cerebras-gpt-oss-120b
```

The command must return the links stored in the mapped source card. It must not ask an LLM to remember or recreate source URLs.
