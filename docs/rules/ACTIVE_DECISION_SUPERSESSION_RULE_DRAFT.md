# Active Decision Supersession Rule — Draft

**Status:** `DRAFT_MUTABLE`  
**Purpose:** Preserve historical research while preventing obsolete instructions from becoming active Galax configuration.  
**Verified:** 2026-07-20

## 1. Core rule

```text
A newer explicit canonical decision may supersede an older materially different
draft without deleting the older evidence. Superseded content is read for history
and risk context only; it cannot be used as active implementation instruction.
```

Exact duplicates follow the separate no-exact-duplicates rule and may be removed only after references are updated and verified.

## 2. Canonical priority

```text
README current readiness
→ FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md
→ CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
→ VALIDATED_LLM_FAILOVER_RULE_DRAFT.md
→ LLM_ASSIGNMENT_PLAN_DRAFT.md
→ SOURCE_INDEX.md and exact source cards
→ older historical drafts and research
```

A lower-priority file cannot override a higher-priority active decision.

## 3. Superseded provider decisions

The following active decisions are invalid wherever they appear in older drafts:

```yaml
Cerebras_as_primary_or_fallback:
  active: false
  reason: current_offer_classified_as_trial_only
  canonical_replacement:
    bounded_private_primary: groq/openai/gpt-oss-20b
    bounded_hosted_fallback: cloudflare/@cf/openai/gpt-oss-20b
    high_complexity_private_primary: groq/openai/gpt-oss-120b
    high_complexity_hosted_fallback: cloudflare/@cf/openai/gpt-oss-120b

OpenRouter_free_router_as_fallback:
  active: false

trial_credit_provider_as_durable_runtime:
  active: false
```

Historical Cerebras capability facts may remain as evidence, but no `CEREBRAS_API_KEY`, Cerebras model ID, rate budget, failover instruction, revalidation fingerprint, or first-run test may enter active implementation configuration.

## 4. Superseded CrewAI feature decisions

```yaml
CrewAI_planning:
  active: false
  replacement: explicit_structured_planning_tasks_plus_deterministic_Flow

CrewAI_reasoning_loop:
  active: false
  replacement: provider_native_reasoning_effort_plus_explicit_plan_validation

CrewAI_native_memory:
  active: false
  replacement: bounded_Supabase_Postgres_MemoryContext_from_Flow

CrewAI_built_in_code_execution:
  active: false
  replacement: separate_rootless_external_sandbox_through_role_tool

hierarchical_or_dynamic_delegation:
  active: false
  replacement: Flow_selects_agents_then_Process_sequential
```

## 5. Superseded memory decisions

```yaml
Notion_as_primary_machine_runtime_memory:
  active: false
  replacement: Supabase_Postgres_or_self_hosted_Postgres

Notion_as_native_CrewAI_memory:
  active: false

Notion_as_optional_curated_human_mirror:
  active: true_pending_validation
```

The file `docs/rules/NOTION_MEMORY_RULE_DRAFT.md` remains historical and may provide optional mirror implementation detail only when it does not conflict with:

```text
docs/rules/SUPABASE_PRIMARY_MEMORY_NOTION_MIRROR_RULE_DRAFT.md
docs/research/memory/NOTION_VS_SUPABASE_MEMORY_DECISION_2026-07-20.md
```

## 6. Superseded MCP and GitHub decisions

```yaml
full_unfiltered_GitHub_MCP_catalog_to_agent:
  active: false

arbitrary_URL_MCP_tool:
  active: false

MCP_connection_implies_security:
  active: false

direct_push_files_as_complete_Galax_concurrency_control:
  active: false
```

Replacement:

```text
one role-scoped BaseTool
→ trusted gateway
→ exact filtered GitHub API/MCP operation
→ expected branch/blob hash validation
→ force=false commit/ref transaction
→ post-write verification
```

Current open CrewAI MCP SSRF/DNS-rebinding risk records must remain part of the security gate until a patched version is pinned and tested.

## 7. Files containing historical/superseded active instructions

The following files must be treated as historical where they conflict with the canonical priority:

```text
docs/prompts/GALAX_CREWAI_IMPLEMENTATION_MASTER_PROMPT_DRAFT.md
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

This registry does not declare each entire file invalid. Only conflicting sections are inactive. Materially different historical evidence, source links, risks, and test ideas remain useful.

## 8. Runtime enforcement

The future preflight must load a machine-readable supersession registry and reject active configuration containing a superseded value.

Required checks:

```text
SUPER-001 reject active Cerebras provider/model/key
SUPER-002 reject CrewAI planning=true
SUPER-003 reject CrewAI reasoning=true
SUPER-004 reject CrewAI memory=true
SUPER-005 reject hierarchical process or delegation
SUPER-006 reject direct agent Notion/Supabase/Drive credentials
SUPER-007 reject Notion primary runtime memory
SUPER-008 reject generic/full MCP tool exposure
SUPER-009 reject arbitrary URL MCP operations
SUPER-010 reject stale master prompt execution
SUPER-011 report exact canonical replacement
SUPER-012 preserve historical records without treating them as instructions
```

## 9. Source and prompt behavior

When an agent reads a superseded file, the task context must include:

```yaml
historical_record: true
active_instruction_authority: false
canonical_replacement_paths: []
```

The model must not resolve conflicts by guessing. It must cite the higher-priority record or return `BLOCKED_SUPERSESSION_CONFLICT`.

## 10. Current status

```yaml
supersession_registry_documented: true
machine_readable_registry_implemented: false
preflight_enforcement_implemented: false
stale_master_prompt_executable: false
historical_files_deleted: false
production_ready: false
```
