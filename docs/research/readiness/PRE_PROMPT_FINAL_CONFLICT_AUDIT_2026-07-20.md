# Final Pre-Prompt Conflict Audit — 2026-07-20

**Status:** `BLOCKED_NOT_READY_TO_USE_MASTER_PROMPT`  
**Decision:** Do not paste or execute the current full Galax CrewAI master prompt.  
**Evidence standard:** official documentation → official source/adapter → live test in the exact Galax environment.

## 1. Executive verdict

```yaml
framework_level_capability_path_found: true
github_read_write_path_found: true
provider_connection_paths_found: true
exact_Galax_runtime_implemented: false
exact_Galax_runtime_live_tested: false
all_readiness_gates_passed: false
current_master_prompt_conflict_free: false
full_prompt_authorized: false
```

The architecture is factually possible, but it is not yet factual to claim that the complete Galax system works. Documentation and source code prove capability paths; they do not prove the unimplemented Galax gateways, credentials, Docker stack, model profiles, permissions, or sequential workflow.

## 2. Source-confirmed facts

### CrewAI and GitHub

```yaml
CrewAI_custom_tools: source_confirmed
CrewAI_MCP_adapter: source_confirmed
CrewAI_exact_MCP_tool_filtering: source_confirmed
CrewAI_Process_sequential: source_confirmed
CrewAI_builtin_GithubSearchTool_write: unsupported
CrewAI_builtin_FileWriterTool_Git_operations: unsupported
official_GitHub_MCP_repository_read_write: source_confirmed_with_permissions
```

Sources:

- https://github.com/crewAIInc/crewAI/blob/main/lib/crewai-tools/src/crewai_tools/tools/github_search_tool/github_search_tool.py
- https://github.com/crewAIInc/crewAI/blob/main/lib/crewai-tools/src/crewai_tools/tools/file_writer_tool/file_writer_tool.py
- https://github.com/crewAIInc/crewAI/blob/main/lib/crewai-tools/src/crewai_tools/adapters/mcp_adapter.py
- https://github.com/crewAIInc/crewAI/blob/main/docs/v1.15.4/en/mcp/overview.mdx
- https://github.com/github/github-mcp-server

### Active LLM candidates

```yaml
private_primary_candidate: groq/openai/gpt-oss-120b
private_hosted_fallback_candidate: cloudflare/@cf/openai/gpt-oss-120b
public_redacted_long_context_candidate: gemini/gemini-2.5-flash
optional_local_fallback_candidate: ollama/gpt-oss:20b
rejected_trial_only_candidate: cerebras/gpt-oss-120b
```

Every candidate remains disabled until its exact CrewAI profile passes agent-specific tool calling, tool-result round trip, structured output, rate/allocation, privacy, timeout, and sequential handoff tests.

## 3. Current master-prompt conflicts

The existing file below is not authorized for use:

```text
docs/prompts/GALAX_CREWAI_IMPLEMENTATION_MASTER_PROMPT_DRAFT.md
```

It still contains superseded active configuration, including:

```text
- Cerebras as the selected provider/model.
- CEREBRAS_API_KEY in the environment template.
- Cerebras-specific LLM failure instructions.
- Cerebras-specific revalidation fingerprints.
- A first-run instruction to verify Cerebras.
```

These conflict with the newer active routing decision that rejects Cerebras as trial-only and selects Groq, Cloudflare, Gemini-for-public/redacted-only, and optional Ollama candidates.

## 4. Other stale or superseded records requiring reconciliation

The following records contain historical decisions that must not override the current README, source index, readiness audit, and routing rule:

```text
docs/architecture/FULLY_DOCKERIZED_CREWAI_FLOW_DRAFT.md
docs/architecture/GOOGLE_DRIVE_KNOWLEDGE_NOTION_MEMORY_DRAFT.md
docs/plan/AGENT_CAPABILITY_MAPPING_DRAFT.md
docs/research/llms/FREE_PROVIDER_SCREENING_2026-07-20.md
docs/rules/AUTOMATIC_REVALIDATION_RESEARCH_RULE_DRAFT.md
docs/rules/FREE_TIER_CAPACITY_SNAPSHOT_RULE_DRAFT.md
docs/rules/NO_UNSUPPORTED_AGENT_WORK_RULE_DRAFT.md
docs/rules/PER_AGENT_LLM_COMPATIBILITY_RULE_DRAFT.md
docs/rules/NOTION_MEMORY_RULE_DRAFT.md
```

Required treatment:

```text
- Update active references to the current routing and Supabase-primary-memory decision.
- Mark historical sections explicitly as superseded when they remain useful for audit history.
- Do not delete materially different historical evidence merely because it is old.
- Remove only exact normalized duplicates after references are updated.
```

## 5. Missing live proof

```text
READY-001 Pin Python, CrewAI, crewai-tools, MCP/mcpadapt, and provider integrations.
READY-002 Build and audit the base Docker image.
READY-003 Start and stop a pinned GitHub MCP Server image.
READY-004 Enumerate exact GitHub MCP tool names and schemas.
READY-005 Implement and test RepositoryPreflightTool.
READY-006 Prove an authorized run-branch write.
READY-007 Reject direct-main, force-push, secret-path, and unauthorized writes.
READY-008 Test Groq through CrewAI with one tool and structured output.
READY-009 Test Cloudflare through CrewAI custom OpenAI mode.
READY-010 Test Gemini only with public/redacted fixtures.
READY-011 Qualify Ollama hardware before local fallback approval.
READY-012 Implement Drive search/read and LearningPacket evidence.
READY-013 Implement Supabase exact-filter/keyword memory and safe checkpointing.
READY-014 Pass a real two-agent Process.sequential smoke test.
READY-015 Confirm every unsupported operation returns a factual blocker and remedy.
```

All 15 gates must pass before the complete implementation prompt is authorized.

## 6. Next permitted action

The next prompt must be a limited **foundation bootstrap and validation prompt**, not the complete 15-agent build prompt.

It may instruct a coding assistant to:

```text
1. Reconcile stale planning and prompt conflicts.
2. Pin and install the minimum dependency set.
3. Build the test Docker image.
4. Start and enumerate the GitHub MCP Server.
5. Implement RepositoryPreflightTool only.
6. Run GitHub read/write negative and positive tests on a temporary run branch.
7. Test one primary LLM profile and one validated fallback profile.
8. Run one minimal two-agent sequential smoke test.
9. Report blockers and remedies without enabling the remaining agents.
```

It must not claim the full platform is complete, enable all 15 agents, merge, deploy, or access production data.

## 7. Authorization rule

```yaml
current_full_master_prompt: DO_NOT_USE
foundation_bootstrap_prompt: MAY_BE_PREPARED_AFTER_STALE_RECORD_RECONCILIATION
full_build_prompt: MAY_BE_PREPARED_ONLY_AFTER_15_OF_15_GATES_PASS
```

## 8. Final status

```yaml
final_fact_check_result: TECHNICALLY_SUPPORTED_BUT_NOT_WORKING_AS_ONE_GALAX_RUNTIME
GitHub_read_write_fact: SUPPORTED_WITH_MCP_OR_CUSTOM_GATEWAY_AND_PERMISSIONS
CrewAI_full_Galax_flow_fact: NOT_YET_PROVEN
prompt_now: NO
required_next_step: RECONCILE_CONFLICTS_THEN_BUILD_AND_RUN_MINIMUM_RUNTIME_TESTS
```
