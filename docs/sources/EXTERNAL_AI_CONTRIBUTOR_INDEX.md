# External AI Contributor Source Index

**Status:** `CONTROLLED_TRIAL_CANDIDATES_ONLY`  
**Verified:** 2026-07-21

These tools are external software-development contributors. They are not Galax CrewAI Agents 01–15 and are not production-approved.

## Selected controlled-trial candidates

| Contributor | Assigned role | Paper score | Current status | Source card |
|---|---|---:|---|---|
| Cline | Primary supervised foundation implementer | 86 | `CANDIDATE_CONTROLLED_TRIAL` | [Source card](tools/cline/SOURCE_CARD.md) |
| OpenHands Core | Docker-isolated fallback reproducer | 84 | `CANDIDATE_CONTROLLED_TRIAL` | [Source card](tools/openhands-core/SOURCE_CARD.md) |
| mini-SWE-agent | Isolated patch comparison worker | 83 | `CANDIDATE_CONTROLLED_TRIAL` | [Source card](tools/mini-swe-agent/SOURCE_CARD.md) |
| Aider | Surgical test or lint fixer | 82 | `CANDIDATE_CONTROLLED_TRIAL` | [Source card](tools/aider/SOURCE_CARD.md) |
| PR-Agent | Read-only stable PR reviewer | 82 | `CANDIDATE_CONTROLLED_TRIAL` | [Source card](tools/pr-agent/SOURCE_CARD.md) |

The scores are Galax paper-compatibility scores, not accuracy percentages. A score of 80 or higher makes a candidate eligible for its exact controlled trial only.

## Declined or deferred candidates

| Contributor | Paper score | Decision | Exact blocker | Source card |
|---|---:|---|---|---|
| OpenCode | 74 | `DECLINED` | `SECURITY_BOUNDARY_NOT_PROVEN` | [Source card](tools/opencode/SOURCE_CARD.md) |
| goose | 77 | `DECLINED_NOW_RESEARCH_LATER` | `SCOPE_TOO_BROAD_AND_ROLE_DUPLICATION` | [Source card](tools/goose/SOURCE_CARD.md) |

Declined candidates receive no repository, MCP, credential, writer, reviewer, or production permission. Their source cards preserve the factual screening trail and reconsideration gates; they do not create additional active contributor roles.

## Canonical operating records

- [Repository-wide AI instructions](../../AGENTS.md)
- [Foundation and Agent 01 Flow execution contract](../plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md)
- [External contributor execution plan](../plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md)
- [Platform command and instruction survey](../research/ai-qualification-framework/PLATFORM_COMMAND_AND_INSTRUCTION_SURVEY_2026-07-21.md)
- [Platform-specific command pack](../prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md)
- [Authorized Foundation and Agent 01 prompt](../prompts/GALAX_FOUNDATION_AGENT01_IMPLEMENTATION_VALIDATION_PROMPT.md)

Where the older Foundation prompt or Agent 01 records describe a direct Agent 01 tool call or `result_as_answer`, the active Flow execution contract above supersedes only those conflicting instructions.

## Deterministic role aliases

```yaml
external-cline: tools/cline/SOURCE_CARD.md
external-openhands-core: tools/openhands-core/SOURCE_CARD.md
external-mini-swe-agent: tools/mini-swe-agent/SOURCE_CARD.md
external-aider: tools/aider/SOURCE_CARD.md
external-pr-agent: tools/pr-agent/SOURCE_CARD.md
external-opencode-declined: tools/opencode/SOURCE_CARD.md
external-goose-deferred: tools/goose/SOURCE_CARD.md
```

## Approval boundary

A paper score does not activate repository permissions. Each selected role requires an exact pinned release/configuration, isolated environment, model/provider profile, negative tests, evidence-contract validation, reproducibility test, and human acceptance.

```yaml
fully_qualified_contributors: 0
simultaneous_writers: prohibited
direct_agent_to_agent_MCP_mesh: prohibited
production_use: prohibited
current_next_gate: controlled_Galax_trial
```
