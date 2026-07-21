# Galax AI Source Index — Draft

**Status:** `DRAFT_MUTABLE`  
**Verified:** 2026-07-21

Canonical entry point for Galax agent, framework, LLM, tool, external contributor, knowledge, memory, infrastructure, risk, and readiness evidence.

## Current readiness

```yaml
full_build_prompt_status: BLOCKED_NOT_READY_TO_PROMPT_CREWAI
current_master_prompt_status: DO_NOT_USE_STALE_CONFLICTS
agents_enabled: 0
private_20B_profiles: DISABLED_PENDING_TESTS
private_120B_profiles: DISABLED_PENDING_TESTS
public_long_context_profile: DISABLED_PENDING_TESTS
local_profile: DISABLED_PENDING_HARDWARE_TESTS
external_contributors_fully_qualified: 0
production_ready: false
```

- [Final pre-prompt conflict audit path alias](../research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md)
- [Canonical conflict audit content](../research/readiness/PRE_PROMPT_FINAL_CONFLICT_AUDIT_2026-07-20.md)
- [Full CrewAI 1.15.4 15-agent remediation blueprint](../research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md)
- [Active decision supersession rule](../rules/ACTIVE_DECISION_SUPERSESSION_RULE_DRAFT.md)
- [Corrected LLM assignment plan](../plan/LLM_ASSIGNMENT_PLAN_DRAFT.md)
- [Final free/runtime readiness audit](../research/readiness/FINAL_FREE_TIER_READINESS_AUDIT_2026-07-20.md)
- [External AI contributor source index](EXTERNAL_AI_CONTRIBUTOR_INDEX.md)

## Canonical decision priority

```text
README current readiness
→ final pre-prompt conflict audit and canonical alias target
→ full 15-agent remediation blueprint
→ active decision supersession rule
→ validated LLM routing/failover rule
→ corrected LLM assignment plan
→ exact source cards
→ older historical research
```

Historical records cannot reactivate Cerebras, Notion-primary runtime memory, generic MCP exposure, CrewAI planning/reasoning/native memory, direct-main writes, automatic merge, or privileged Docker-in-Docker.

## Agents

| Agent ID | Role | Current LLM class | Direct tool | Status |
|---|---|---|---|---|
| [`engineering_manager`](agents/engineering_manager/SOURCE_CARD.md) | AI Engineering Manager and CrewAI Execution Planning Lead | Groq 20B bounded primary candidate | [`RepositoryPreflightTool`](tools/repository_preflight_tool/SOURCE_CARD.md) | `RESEARCHING` |

Agents 02–15 have candidate model classes, one-tool interfaces, restrictions, and remedies in the full remediation blueprint. Their individual cards are created and approved one agent at a time.

## External development contributors

These are controlled development tools, not Galax CrewAI agents.

| Contributor | Bounded role | Status | Source card |
|---|---|---|---|
| Cline | Primary supervised foundation implementer | `CANDIDATE_CONTROLLED_TRIAL` | [`TOOL-external-cline`](tools/cline/SOURCE_CARD.md) |
| OpenHands Core | Docker-isolated fallback reproducer | `CANDIDATE_CONTROLLED_TRIAL` | [`TOOL-external-openhands-core`](tools/openhands-core/SOURCE_CARD.md) |
| mini-SWE-agent | Isolated patch comparison worker | `CANDIDATE_CONTROLLED_TRIAL` | [`TOOL-external-mini-swe-agent`](tools/mini-swe-agent/SOURCE_CARD.md) |
| Aider | Surgical test or lint fixer | `CANDIDATE_CONTROLLED_TRIAL` | [`TOOL-external-aider`](tools/aider/SOURCE_CARD.md) |
| PR-Agent | Read-only stable PR reviewer | `CANDIDATE_CONTROLLED_TRIAL` | [`TOOL-external-pr-agent`](tools/pr-agent/SOURCE_CARD.md) |

Canonical contributor records:

- [Repository-wide external AI instructions](../../AGENTS.md)
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
| [`LLM-groq-openai-gpt-oss-20b`](llms/groq-openai-gpt-oss-20b/SOURCE_CARD.md) | Groq `openai/gpt-oss-20b` | Bounded low/medium private primary | `DISABLED_PENDING_TESTS` | [Model](https://console.groq.com/docs/model/openai/gpt-oss-20b) |
| [`LLM-groq-openai-gpt-oss-120b`](llms/groq-openai-gpt-oss-120b/SOURCE_CARD.md) | Groq `openai/gpt-oss-120b` | High-complexity private primary | `DISABLED_PENDING_TESTS` | [Model](https://console.groq.com/docs/model/openai/gpt-oss-120b) |
| [`LLM-cloudflare-gpt-oss-20b`](llms/cloudflare-gpt-oss-20b/SOURCE_CARD.md) | Cloudflare `@cf/openai/gpt-oss-20b` | Bounded hosted fallback | `DISABLED_PENDING_TESTS` | [Model](https://developers.cloudflare.com/workers-ai/models/gpt-oss-20b/) |
| [`LLM-cloudflare-gpt-oss-120b`](llms/cloudflare-gpt-oss-120b/SOURCE_CARD.md) | Cloudflare `@cf/openai/gpt-oss-120b` | High-complexity hosted fallback | `DISABLED_PENDING_TESTS` | [Model](https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/) |
| [`LLM-google-gemini-2.5-flash`](llms/google-gemini-2.5-flash/SOURCE_CARD.md) | Google `gemini-2.5-flash` | Public/redacted long context | `DISABLED_PENDING_TESTS` | [Model](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash) |
| [`LLM-ollama-gpt-oss-20b`](llms/ollama-gpt-oss-20b/SOURCE_CARD.md) | Local Ollama `gpt-oss:20b` | Optional local fallback | `DISABLED_PENDING_HARDWARE_TESTS` | [Model](https://ollama.com/library/gpt-oss:20b) |
| [`LLM-cerebras-gpt-oss-120b`](llms/cerebras-gpt-oss-120b/SOURCE_CARD.md) | Cerebras `gpt-oss-120b` | Historical rejected candidate | `REJECTED_TRIAL_ONLY` | [Pricing](https://www.cerebras.ai/pricing) |

Every `agent + prompt + task + tool + output + data class + model/provider` combination requires independent tests. Fallback is an explicit Flow transition from a safe checkpoint, never a simultaneous agent configuration.

## Direct tool and infrastructure source cards

| Source ID | Tool/gateway | Status | Official compatibility source |
|---|---|---|---|
| [`TOOL-repository-preflight`](tools/repository_preflight_tool/SOURCE_CARD.md) | `RepositoryPreflightTool` | `CONDITIONALLY_APPROVED` | [CrewAI custom tools](https://docs.crewai.com/learn/create-custom-tools) |
| [`TOOL-drive-knowledge-gateway`](tools/drive_knowledge_gateway/SOURCE_CARD.md) | `DriveKnowledgeGateway` | `SELECTED_FOR_VALIDATION` | [Drive search](https://developers.google.com/workspace/drive/api/guides/search-files) |
| [`TOOL-supabase-memory-gateway`](tools/supabase_memory_gateway/SOURCE_CARD.md) | `GalaxMemoryGateway` | `SELECTED_FOR_VALIDATION` | [Supabase AI](https://supabase.com/docs/guides/ai) |
| [`TOOL-notion-memory-gateway`](tools/notion_memory_gateway/SOURCE_CARD.md) | `GalaxNotionMirrorGateway` | `OPTIONAL_SELECTED_FOR_VALIDATION` | [Notion API](https://developers.notion.com/) |
| [`INFRA-docker-compose`](infrastructure/docker-compose/SOURCE_CARD.md) | Docker Engine + Compose | `SELECTED_FOR_VALIDATION` | [Docker Compose](https://docs.docker.com/compose/) |

Drive/memory/Notion, branch creation, checkpoints, routing, and draft PR creation are trusted Flow infrastructure, not extra agent tools.

## Underlying open-source component candidates

- [Open-source agent tool stack](../research/tools/OPEN_SOURCE_AGENT_TOOL_STACK_2026-07-20.md)

It currently records SearXNG, Playwright, Bandit, pip-audit, Trivy, Gitleaks, Hadolint, actionlint, OpenTelemetry, and Prometheus as **unapproved underlying components**. Each requires an exact release/image digest, license, wrapper, sandbox, schema, and tests before use.

## CrewAI governance and risk sources

- [Custom tools and typed results](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/learn/create-custom-tools.mdx)
- [Tool call hooks](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/learn/tool-hooks.mdx)
- [LLM call hooks](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/learn/llm-hooks.mdx)
- [Force tool output as result](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/learn/force-tool-output-as-result.mdx)
- [Planning limitation](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/planning.mdx)
- [Reasoning limitation](https://github.com/crewAIInc/crewAI/blob/69c0308f2cf4fa17214eab4db10071abc08602fd/docs/v1.15.4/en/concepts/reasoning.mdx)
- [Tool-fabrication issue #3154](https://github.com/crewAIInc/crewAI/issues/3154)
- [MCP SSRF issue #6504](https://github.com/crewAIInc/crewAI/issues/6504)
- [Open MCP SSRF fix PR #6519](https://github.com/crewAIInc/crewAI/pull/6519)

## GitHub integration sources

- [Official GitHub MCP Server](https://github.com/github/github-mcp-server)
- [GitHub MCP push_files schema](https://github.com/github/github-mcp-server/blob/1338dbed4a044ee26422d4212bac3a8037fdb7ff/pkg/github/__toolsnaps__/push_files.snap)
- [GitHub MCP setup](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/use-the-github-mcp-server)
- [CrewAI MCP adapter](https://github.com/crewAIInc/crewAI/blob/main/lib/crewai-tools/src/crewai_tools/adapters/mcp_adapter.py)
- [CrewAI GithubSearchTool](https://github.com/crewAIInc/crewAI/blob/main/lib/crewai-tools/src/crewai_tools/tools/github_search_tool/github_search_tool.py)
- [CrewAI FileWriterTool](https://github.com/crewAIInc/crewAI/blob/main/lib/crewai-tools/src/crewai_tools/tools/file_writer_tool/file_writer_tool.py)
- [GitHub Git Database API](https://docs.github.com/en/rest/git)

## Current rules

- [Active decision supersession](../rules/ACTIVE_DECISION_SUPERSESSION_RULE_DRAFT.md)
- [No unsupported agent work](../rules/NO_UNSUPPORTED_AGENT_WORK_RULE_DRAFT.md)
- [Per-agent LLM compatibility](../rules/PER_AGENT_LLM_COMPATIBILITY_RULE_DRAFT.md)
- [Validated LLM routing and failover](../rules/VALIDATED_LLM_FAILOVER_RULE_DRAFT.md)
- [Free-tier capacity snapshot](../rules/FREE_TIER_CAPACITY_SNAPSHOT_RULE_DRAFT.md)
- [Knowledge before implementation](../rules/KNOWLEDGE_BEFORE_IMPLEMENTATION_RULE_DRAFT.md)
- [Supabase primary memory + Notion mirror](../rules/SUPABASE_PRIMARY_MEMORY_NOTION_MIRROR_RULE_DRAFT.md)
- [Automatic revalidation research](../rules/AUTOMATIC_REVALIDATION_RESEARCH_RULE_DRAFT.md)
- [Source traceability](../rules/SOURCE_TRACEABILITY_RULE_DRAFT.md)
- [No exact duplicates](../rules/NO_EXACT_DUPLICATES_RULE_DRAFT.md)

## Main research, architecture, and plans

- [Full 15-agent remediation blueprint](../research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md)
- [Corrected LLM assignment](../plan/LLM_ASSIGNMENT_PLAN_DRAFT.md)
- [GitHub read/write and free-LLM audit](../research/crewai/CREWAI_GITHUB_RW_FREE_LLM_AUDIT_2026-07-20.md)
- [Final pre-prompt conflict audit path alias](../research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md)
- [Canonical conflict audit content](../research/readiness/PRE_PROMPT_FINAL_CONFLICT_AUDIT_2026-07-20.md)
- [Final free/runtime readiness audit](../research/readiness/FINAL_FREE_TIER_READINESS_AUDIT_2026-07-20.md)
- [CrewAI capability matrix](../research/crewai/CREWAI_1_15_4_CAPABILITY_LIMIT_MATRIX.md)
- [Docker fact check](../research/docker/CREWAI_DOCKER_FACT_CHECK_2026-07-20.md)
- [GitHub repository read/write architecture](../architecture/GITHUB_REPOSITORY_READ_WRITE_DRAFT.md)
- [Notion vs Supabase decision](../research/memory/NOTION_VS_SUPABASE_MEMORY_DECISION_2026-07-20.md)
- [External contributor execution plan](../plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md)
- [External platform command survey](../research/ai-qualification-framework/PLATFORM_COMMAND_AND_INSTRUCTION_SURVEY_2026-07-21.md)

## Deterministic query mapping

```yaml
aliases:
  engineering_manager: agents/engineering_manager/SOURCE_CARD.md
  AGENT-01: agents/engineering_manager/SOURCE_CARD.md
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
  external-contributor-index: EXTERNAL_AI_CONTRIBUTOR_INDEX.md
  open-source-tool-stack: ../research/tools/OPEN_SOURCE_AGENT_TOOL_STACK_2026-07-20.md
  active-supersession: ../rules/ACTIVE_DECISION_SUPERSESSION_RULE_DRAFT.md
  full-agent-remediation: ../research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  pre-prompt-conflict-audit: ../research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md
  canonical-pre-prompt-conflict-audit: ../research/readiness/PRE_PROMPT_FINAL_CONFLICT_AUDIT_2026-07-20.md
  free-runtime-readiness: ../research/readiness/FINAL_FREE_TIER_READINESS_AUDIT_2026-07-20.md
```

The future `source <alias>` command returns links from these records. It must not reconstruct URLs from model memory.