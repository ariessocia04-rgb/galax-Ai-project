# Galax AI Source Index — Draft

**Status:** `DRAFT_MUTABLE`  
**Verified:** 2026-07-21

Canonical entry point for Galax agent, framework, LLM, tool, external contributor, knowledge, memory, infrastructure, risk, and readiness evidence.

## Current readiness

```yaml
full_build_prompt_status: BLOCKED_NOT_READY_TO_PROMPT_CREWAI
current_master_prompt_status: DO_NOT_USE_STALE_CONFLICTS
Foundation_Agent01_Flow_contract: ACTIVE_CANONICAL
agents_enabled: 0
private_20B_profiles: DISABLED_PENDING_TESTS
private_120B_profiles: DISABLED_PENDING_TESTS
public_long_context_profile: DISABLED_PENDING_TESTS
local_profile: DISABLED_PENDING_HARDWARE_TESTS
external_contributors_fully_qualified: 0
production_ready: false
```

Canonical readiness and execution records:

- [Final pre-prompt conflict audit path alias](../research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md)
- [Canonical conflict audit content](../research/readiness/PRE_PROMPT_FINAL_CONFLICT_AUDIT_2026-07-20.md)
- [Foundation and Agent 01 Flow execution contract](../plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md)
- [Full CrewAI 1.15.4 remediation blueprint](../research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md)
- [Active decision supersession rule](../rules/ACTIVE_DECISION_SUPERSESSION_RULE_DRAFT.md)
- [Corrected LLM assignment plan](../plan/LLM_ASSIGNMENT_PLAN_DRAFT.md)
- [Final free/runtime readiness audit](../research/readiness/FINAL_FREE_TIER_READINESS_AUDIT_2026-07-20.md)
- [External AI contributor source index](EXTERNAL_AI_CONTRIBUTOR_INDEX.md)

## Canonical decision priority

```text
README current readiness
→ final pre-prompt conflict audit and alias target
→ Foundation and Agent 01 Flow execution contract
→ full 15-agent remediation blueprint
→ active rules and plans
→ exact source cards
→ historical research
```

The active Flow contract supersedes only older conflicting instructions that assign `RepositoryPreflightTool` directly to Agent 01, require an Agent 01 tool call, or use `result_as_answer` for that path.

Historical records cannot reactivate Cerebras, Notion-primary runtime memory, generic MCP exposure, CrewAI planning/reasoning/native memory, direct-main writes, automatic merge, privileged Docker-in-Docker, or direct Agent 01 preflight-tool ownership.

## Agents

| Agent ID | Role | Current LLM class | Direct tools | Upstream Flow dependency | Status |
|---|---|---|---:|---|---|
| [`engineering_manager`](agents/engineering_manager/SOURCE_CARD.md) | AI Engineering Manager and CrewAI Execution Planning Lead | Groq 20B bounded primary candidate | 0 | [`RepositoryPreflightTool`](tools/repository_preflight_tool/SOURCE_CARD.md), invoked once by Flow | `RESEARCHING_NOT_APPROVED` |

Agents 02–15 remain disabled. Their candidate model classes, boundaries, and remedies remain research records only until implemented and approved one at a time.

## External development contributors

Selected candidates are controlled development tools, not Galax CrewAI agents:

| Contributor | Bounded role | Paper score | Status | Source card |
|---|---|---:|---|---|
| Cline | Primary supervised foundation implementer | 86 | `CANDIDATE_CONTROLLED_TRIAL` | [`TOOL-external-cline`](tools/cline/SOURCE_CARD.md) |
| OpenHands Core | Docker-isolated fallback reproducer | 84 | `CANDIDATE_CONTROLLED_TRIAL` | [`TOOL-external-openhands-core`](tools/openhands-core/SOURCE_CARD.md) |
| mini-SWE-agent | Isolated patch comparison worker | 83 | `CANDIDATE_CONTROLLED_TRIAL` | [`TOOL-external-mini-swe-agent`](tools/mini-swe-agent/SOURCE_CARD.md) |
| Aider | Surgical test or lint fixer | 82 | `CANDIDATE_CONTROLLED_TRIAL` | [`TOOL-external-aider`](tools/aider/SOURCE_CARD.md) |
| PR-Agent | Read-only stable PR reviewer | 82 | `CANDIDATE_CONTROLLED_TRIAL` | [`TOOL-external-pr-agent`](tools/pr-agent/SOURCE_CARD.md) |

Declined or deferred candidates:

| Contributor | Paper score | Current decision | Source card |
|---|---:|---|---|
| OpenCode | 74 | `DECLINED_SECURITY_BOUNDARY_NOT_PROVEN` | [`EXTERNAL-opencode`](tools/opencode/SOURCE_CARD.md) |
| goose | 77 | `DECLINED_NOW_RESEARCH_LATER` | [`EXTERNAL-goose`](tools/goose/SOURCE_CARD.md) |

Canonical contributor records:

- [Repository-wide instructions](../../AGENTS.md)
- [Foundation and Agent 01 Flow execution contract](../plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md)
- [Contributor execution plan](../plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md)
- [Official platform command survey](../research/ai-qualification-framework/PLATFORM_COMMAND_AND_INSTRUCTION_SURVEY_2026-07-21.md)
- [Platform-specific command pack](../prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md)

Paper scores permit controlled trials only. They do not authorize repository writes, production use, merge, deployment, or direct MCP coordination.

## Framework

| Source ID | Framework/version | Status | Official source |
|---|---|---|---|
| [`FRAMEWORK-crewai-1.15.4`](frameworks/crewai-1.15.4/SOURCE_CARD.md) | CrewAI `1.15.4` | `SELECTED_FOR_PINNED_VALIDATION` | [PyPI](https://pypi.org/project/crewai/) |

## LLMs

| Source ID | Provider/model | Candidate role | Status | Official source |
|---|---|---|---|---|
| [`LLM-groq-openai-gpt-oss-20b`](llms/groq-openai-gpt-oss-20b/SOURCE_CARD.md) | Groq `openai/gpt-oss-20b` | Bounded private primary | `DISABLED_PENDING_TESTS` | [Model](https://console.groq.com/docs/model/openai/gpt-oss-20b) |
| [`LLM-groq-openai-gpt-oss-120b`](llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md) | Groq `openai/gpt-oss-120b` | High-complexity private primary | `DISABLED_PENDING_TESTS` | [Model](https://console.groq.com/docs/model/openai/gpt-oss-120b) |
| [`LLM-cloudflare-gpt-oss-20b`](llms/cloudflare-gpt-oss-20b/SOURCE_CARD.md) | Cloudflare `@cf/openai/gpt-oss-20b` | Bounded hosted fallback | `DISABLED_PENDING_TESTS` | [Model](https://developers.cloudflare.com/workers-ai/models/gpt-oss-20b/) |
| [`LLM-cloudflare-gpt-oss-120b`](llms/cloudflare-gpt-oss-120b/SOURCE_CARD.md) | Cloudflare `@cf/openai/gpt-oss-120b` | High-complexity hosted fallback | `DISABLED_PENDING_TESTS` | [Model](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/) |
| [`LLM-google-gemini-2.5-flash`](llms/google-gemini-2.5-flash/SOURCE_CARD.md) | Google `gemini-2.5-flash` | Public/redacted long context | `DISABLED_PENDING_TESTS` | [Model](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash) |
| [`LLM-ollama-gpt-oss-20b`](llms/ollama-gpt-oss-20b/SOURCE_CARD.md) | Ollama `gpt-oss:20b` | Optional local fallback | `DISABLED_PENDING_HARDWARE_TESTS` | [Model](https://ollama.com/library/gpt-oss:20b) |
| [`LLM-cerebras-gpt-oss-120b`](llms/cerebras-gpt-oss-120b/SOURCE_CARD.md) | Cerebras `gpt-oss-120b` | Historical rejected candidate | `REJECTED_TRIAL_ONLY` | [Pricing](https://www.cerebras.ai/pricing) |

Every `agent + prompt + task + output + data class + model/provider` combination requires independent tests. Fallback is an explicit Flow transition from a safe checkpoint, never a simultaneous agent configuration.

## Direct tool and infrastructure source cards

| Source ID | Tool/gateway | Status | Ownership |
|---|---|---|---|
| [`TOOL-repository-preflight`](tools/repository_preflight_tool/SOURCE_CARD.md) | `RepositoryPreflightTool` | `CONDITIONALLY_APPROVED_FOR_IMPLEMENTATION_TEST` | Flow-owned, Agent 01 direct call prohibited |
| [`TOOL-drive-knowledge-gateway`](tools/drive_knowledge_gateway/SOURCE_CARD.md) | `DriveKnowledgeGateway` | `SELECTED_FOR_VALIDATION` | trusted Flow infrastructure |
| [`TOOL-supabase-memory-gateway`](tools/supabase_memory_gateway/SOURCE_CARD.md) | `GalaxMemoryGateway` | `SELECTED_FOR_VALIDATION` | trusted Flow infrastructure |
| [`TOOL-notion-memory-gateway`](tools/notion_memory_gateway/SOURCE_CARD.md) | `GalaxNotionMirrorGateway` | `OPTIONAL_SELECTED_FOR_VALIDATION` | trusted Flow infrastructure |
| [`INFRA-docker-compose`](infrastructure/docker-compose/SOURCE_CARD.md) | Docker Engine + Compose | `SELECTED_FOR_VALIDATION` | infrastructure candidate |

Drive/memory/Notion, repository permissions, branch creation, checkpoints, routing, and draft PR creation are trusted application/Flow infrastructure, not extra Agent 01 tools.

## Main rules, research, architecture, and plans

- [Active decision supersession](../rules/ACTIVE_DECISION_SUPERSESSION_RULE_DRAFT.md)
- [No unsupported agent work](../rules/NO_UNSUPPORTED_AGENT_WORK_RULE_DRAFT.md)
- [Per-agent LLM compatibility](../rules/PER_AGENT_LLM_COMPATIBILITY_RULE_DRAFT.md)
- [Validated LLM routing and failover](../rules/VALIDATED_LLM_FAILOVER_RULE_DRAFT.md)
- [Knowledge before implementation](../rules/KNOWLEDGE_BEFORE_IMPLEMENTATION_RULE_DRAFT.md)
- [Supabase primary memory + Notion mirror](../rules/SUPABASE_PRIMARY_MEMORY_NOTION_MIRROR_RULE_DRAFT.md)
- [Automatic revalidation research](../rules/AUTOMATIC_REVALIDATION_RESEARCH_RULE_DRAFT.md)
- [Source traceability](../rules/SOURCE_TRACEABILITY_RULE_DRAFT.md)
- [No exact duplicates](../rules/NO_EXACT_DUPLICATES_RULE_DRAFT.md)
- [Full 15-agent remediation blueprint](../research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md)
- [GitHub read/write architecture](../architecture/GITHUB_REPOSITORY_READ_WRITE_DRAFT.md)
- [External contributor execution plan](../plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md)
- [External platform command survey](../research/ai-qualification-framework/PLATFORM_COMMAND_AND_INSTRUCTION_SURVEY_2026-07-21.md)

## Deterministic query mapping

```yaml
aliases:
  engineering_manager: agents/engineering_manager/SOURCE_CARD.md
  AGENT-01: agents/engineering_manager/SOURCE_CARD.md
  repository-preflight: tools/repository_preflight_tool/SOURCE_CARD.md
  foundation-agent01-flow-contract: ../plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
  crewai-1.15.4: frameworks/crewai-1.15.4/SOURCE_CARD.md
  groq-gpt-oss-20b: llms/groq-openai-gpt-oss-20b/SOURCE_CARD.md
  groq-gpt-oss-120b: llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md
  cloudflare-gpt-oss-20b: llms/cloudflare-gpt-oss-20b/SOURCE_CARD.md
  cloudflare-gpt-oss-120b: llms/cloudflare-gpt-oss-120b/SOURCE_CARD.md
  gemini-2.5-flash: llms/google-gemini-2.5-flash/SOURCE_CARD.md
  ollama-gpt-oss-20b: llms/ollama-gpt-oss-20b/SOURCE_CARD.md
  cerebras-gpt-oss-120b: llms/cerebras-gpt-oss-120b/SOURCE_CARD.md
  external-cline: tools/cline/SOURCE_CARD.md
  external-openhands-core: tools/openhands-core/SOURCE_CARD.md
  external-mini-swe-agent: tools/mini-swe-agent/SOURCE_CARD.md
  external-aider: tools/aider/SOURCE_CARD.md
  external-pr-agent: tools/pr-agent/SOURCE_CARD.md
  external-opencode-declined: tools/opencode/SOURCE_CARD.md
  external-goose-deferred: tools/goose/SOURCE_CARD.md
  external-contributor-index: EXTERNAL_AI_CONTRIBUTOR_INDEX.md
  active-supersession: ../rules/ACTIVE_DECISION_SUPERSESSION_RULE_DRAFT.md
  full-agent-remediation: ../research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  pre-prompt-conflict-audit: ../research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md
  canonical-pre-prompt-conflict-audit: ../research/readiness/PRE_PROMPT_FINAL_CONFLICT_AUDIT_2026-07-20.md
```

The future `source <alias>` command returns links from these records. It must not reconstruct URLs from model memory.
