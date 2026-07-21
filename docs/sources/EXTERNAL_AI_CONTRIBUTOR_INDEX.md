# External AI Contributor Source Index

**Status:** `CONTROLLED_TRIAL_CANDIDATES_ONLY`  
**Verified:** 2026-07-21

These tools are external software-development contributors. They are not Galax CrewAI Agents 01–15 and are not production-approved.

| Contributor | Assigned role | Paper score | Current status | Source card |
|---|---|---:|---|---|
| Cline | Primary supervised foundation implementer | 86 | `CANDIDATE_CONTROLLED_TRIAL` | [Source card](tools/cline/SOURCE_CARD.md) |
| OpenHands Core | Docker-isolated fallback reproducer | 84 | `CANDIDATE_CONTROLLED_TRIAL` | [Source card](tools/openhands-core/SOURCE_CARD.md) |
| mini-SWE-agent | Isolated patch comparison worker | 83 | `CANDIDATE_CONTROLLED_TRIAL` | [Source card](tools/mini-swe-agent/SOURCE_CARD.md) |
| Aider | Surgical test or lint fixer | 82 | `CANDIDATE_CONTROLLED_TRIAL` | [Source card](tools/aider/SOURCE_CARD.md) |
| PR-Agent | Read-only stable PR reviewer | 82 | `CANDIDATE_CONTROLLED_TRIAL` | [Source card](tools/pr-agent/SOURCE_CARD.md) |

## Canonical operating records

- [Repository-wide AI instructions](../../AGENTS.md)
- [External contributor execution plan](../plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md)
- [Platform command and instruction survey](../research/ai-qualification-framework/PLATFORM_COMMAND_AND_INSTRUCTION_SURVEY_2026-07-21.md)
- [Platform-specific command pack](../prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md)
- [Authorized Foundation and Agent 01 prompt](../prompts/GALAX_FOUNDATION_AGENT01_IMPLEMENTATION_VALIDATION_PROMPT.md)

## Deterministic role aliases

```yaml
external-cline: tools/cline/SOURCE_CARD.md
external-openhands-core: tools/openhands-core/SOURCE_CARD.md
external-mini-swe-agent: tools/mini-swe-agent/SOURCE_CARD.md
external-aider: tools/aider/SOURCE_CARD.md
external-pr-agent: tools/pr-agent/SOURCE_CARD.md
```

## Approval boundary

A paper score does not activate repository permissions. Each role requires an exact pinned release/configuration, isolated environment, model/provider profile, negative tests, evidence-contract validation, reproducibility test, and human acceptance.

```yaml
fully_qualified_contributors: 0
simultaneous_writers: prohibited
direct_agent_to_agent_MCP_mesh: prohibited
production_use: prohibited
```