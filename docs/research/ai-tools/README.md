# AI Development Contributor Research Index

**Status:** `RESEARCH_ONLY_NOT_RUNTIME_AUTHORIZATION`  
**Branch:** `research/ai-qualification-framework`

## Reading order

1. `../../rules/AI_DEVELOPMENT_CONTRIBUTOR_QUALIFICATION_GATE.md`
   - Mandatory classification, evidence, permission, cost, security, and live-test gates.
2. `AI_DEVELOPMENT_CONTRIBUTOR_FINAL_QUALIFICATION_REVIEW_V3_2026-07-21.md`
   - Current final paper-qualification decision, 80-point threshold, MCP compatibility matrix, conflict-free workflow, duration estimate, and quality conditions.
3. `AI_DEVELOPMENT_TOOL_STRICT_RESCREEN_V2_2026-07-21.md`
   - Historical strict re-screen. Superseded where it conflicts with V3.
4. `AI_DEVELOPMENT_TOOL_CANDIDATE_AUDIT_2026-07-21.md`
   - Historical V1 candidate audit retained as evidence.
5. `../../plan/AI_DEVELOPMENT_CONTRIBUTOR_COORDINATION_PLAN_DRAFT.md`
   - Single-writer, branch-lock, handoff, review, and quota-exhaustion workflow.
6. `../../sources/ai-tools/AI_DEVELOPMENT_TOOL_SOURCE_INDEX_2026-07-21.md`
   - Original source index.
7. `../../sources/ai-tools/AI_DEVELOPMENT_TOOL_SOURCE_ADDENDUM_V2_2026-07-21.md`
   - Cline, mini-SWE-agent, OpenCode, goose, OpenHands, benchmark, and maintenance evidence.

## Current final paper-qualified five

```yaml
qualification_threshold: 80

passed_to_controlled_trial:
  - candidate: Cline
    score: 86
    role: supervised_primary_local_implementer
  - candidate: OpenHands_Core
    score: 84
    role: autonomous_Docker_fallback_implementer
  - candidate: Aider
    score: 82
    role: surgical_fix_and_test_repair
  - candidate: mini_SWE_agent
    score: 83
    role: isolated_issue_resolution_and_patch_comparison
  - candidate: PR_Agent
    score: 82
    role: pinned_self_hosted_read_only_PR_reviewer

declined_below_threshold:
  - candidate: OpenCode_anomalyco
    score: 74
    reason: no_built_in_security_sandbox_and_security_boundary_not_proven
  - candidate: goose
    score: 77
    reason: duplicate_general_scope_and_large_MCP_surface_in_current_phase

live_tested_in_Galax: []
activated_for_repository_write: []
```

## MCP decision

```yaml
native_MCP_clients:
  - Cline
  - OpenHands_Core

no_official_native_MCP_found_for_current_role:
  - Aider
  - mini_SWE_agent
  - PR_Agent

direct_agent_to_agent_MCP_mesh: prohibited
future_pattern: narrow_GalaxDevelopmentContributorGateway
future_gateway_status: research_only_not_implemented
```

MCP is not the coordination mechanism for concurrent repository writes. Each contributor remains an external development tool behind a dedicated task branch/worktree and returns bounded artifacts.

## Duration and quality decision

```yaml
Agent01_foundation_estimate:
  best_case_working_days: 10
  realistic_working_days: 14_to_20
  blocked_or_high_rework_case: 21_to_35

before_live_trials:
  output_quality_percentage: not_established

after_all_role_trials_and_gates_pass:
  expected_internal_process_quality_band: 85_to_92_out_of_100
  guarantee_of_defect_free_output: false
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
anomalyco_opencode: DECLINED_BELOW_80_CURRENT_PHASE
Antigravity_account_rotation: PROHIBITED_QUOTA_EVASION
goose: DECLINED_BELOW_80_CURRENT_PHASE
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
MCP_mesh_approved: false
Agents_02_to_15: disabled
```
