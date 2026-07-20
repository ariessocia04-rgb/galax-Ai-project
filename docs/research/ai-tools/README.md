# AI Development Contributor Research Index

**Status:** `RESEARCH_ONLY_NOT_RUNTIME_AUTHORIZATION`  
**Branch:** `research/ai-qualification-framework`

## Reading order

1. `../../rules/AI_DEVELOPMENT_CONTRIBUTOR_QUALIFICATION_GATE.md`
   - Mandatory classification, evidence, permission, cost, security, and live-test gates.
2. `AI_DEVELOPMENT_TOOL_STRICT_RESCREEN_V2_2026-07-21.md`
   - Current strict decision. Re-screens the candidate pool, adds omitted open-source candidates, and separates open-source candidates from hosted services.
3. `AI_DEVELOPMENT_TOOL_CANDIDATE_AUDIT_2026-07-21.md`
   - Historical V1 candidate audit retained as evidence. Superseded where it conflicts with the strict V2 decision.
4. `../../plan/AI_DEVELOPMENT_CONTRIBUTOR_COORDINATION_PLAN_DRAFT.md`
   - Single-writer, branch-lock, handoff, review, and quota-exhaustion workflow.
5. `../../sources/ai-tools/AI_DEVELOPMENT_TOOL_SOURCE_INDEX_2026-07-21.md`
   - Original source index.
6. `../../sources/ai-tools/AI_DEVELOPMENT_TOOL_SOURCE_ADDENDUM_V2_2026-07-21.md`
   - Current Cline, mini-SWE-agent, OpenCode, goose, OpenHands, benchmark, and maintenance evidence.

## Current strict open-source shortlist

```yaml
strict_open_source_top_five:
  - Cline
  - OpenHands_Core
  - Aider
  - mini_SWE_agent
  - OpenCode_anomalyco

strong_reserve:
  - goose_custom_distribution
  - PR_Agent_read_only

hosted_tools_outside_open_source_list:
  current_operator:
    - Jules
  standby:
    - Codex

live_tested_in_Galax: []
activated_for_repository_write: []
```

## Why the V1 shortlist changed

```yaml
newly_added:
  Cline:
    reason: active Apache-2.0 SDK/CLI/IDE agent with explicit approvals and checkpoints
  mini_SWE_agent:
    reason: current MIT successor candidate with reproducible SWE-bench harness evidence
  OpenCode_anomalyco:
    reason: active MIT project with deny/ask/allow permissions and AGENTS.md support

downgraded:
  PR_Agent:
    reason: useful specialized reviewer but community/transition risk and narrower value

not_open_source:
  - Jules
  - Codex
```

## Important classification and exclusion decisions

```yaml
LangGraph: ORCHESTRATION_FRAMEWORK_NOT_TEAM_WORKER
PostgreSQL_pgvector: DATA_INFRASTRUCTURE_NOT_TEAM_WORKER
SWE_agent_original: SUPERSEDED_FOR_NEW_ADOPTION
mini_SWE_agent: SEPARATE_CURRENT_CANDIDATE
Continue: BLOCKED_MAINTENANCE_STATUS
Roo_Code: BLOCKED_ARCHIVED
opencode_ai_opencode: BLOCKED_ARCHIVED_NAME_COLLISION
anomalyco_opencode: CURRENT_OPENCODE_CANDIDATE
Antigravity_account_rotation: PROHIBITED_QUOTA_EVASION
goose: RESERVE_CUSTOM_ALLOWLISTED_DISTRIBUTION_ONLY
```

## Current safety state

```yaml
one_active_writer_per_task: required
parallel_writers_on_overlapping_paths: prohibited
direct_main_write: prohibited
automatic_merge: prohibited
force_push: prohibited
runtime_activation: not_authorized
universal_accuracy_claim: prohibited
exact_Galax_trial_required: true
Agents_02_to_15: disabled
```
