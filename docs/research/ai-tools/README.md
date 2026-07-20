# AI Development Contributor Research Index

**Status:** `RESEARCH_AND_ROLE_DESIGN_COMPLETE_NOT_RUNTIME_AUTHORIZATION`  
**Branch:** `research/ai-qualification-framework`

## Reading order

1. `../../rules/AI_DEVELOPMENT_CONTRIBUTOR_QUALIFICATION_GATE.md`
   - Mandatory classification, evidence, permission, cost, security, and live-test gates.
2. `AI_DEVELOPMENT_CONTRIBUTOR_FINAL_QUALIFICATION_REVIEW_V3_2026-07-21.md`
   - Current final paper-qualification decision, 80-point threshold, MCP compatibility matrix, conflict-free workflow, duration estimate, and quality conditions.
3. `AI_CONTRIBUTOR_COMMAND_DESIGN_SURVEY_2026-07-21.md`
   - Official-platform survey used to define professional, repository-first commands.
4. `../../prompts/external-ai-contributors/README.md`
   - Canonical external contributor role package index.
5. `../../prompts/external-ai-contributors/SHARED_EXECUTION_PROTOCOL.md`
   - Shared repository, safety, execution, stop, testing, and handoff protocol.
6. The exact selected role charter:
   - `../../prompts/external-ai-contributors/CLINE_ROLE_CHARTER.md`
   - `../../prompts/external-ai-contributors/OPENHANDS_CORE_ROLE_CHARTER.md`
   - `../../prompts/external-ai-contributors/AIDER_ROLE_CHARTER.md`
   - `../../prompts/external-ai-contributors/MINI_SWE_AGENT_ROLE_CHARTER.md`
   - `../../prompts/external-ai-contributors/PR_AGENT_ROLE_CHARTER.md`
7. `../../plan/EXTERNAL_AI_CONTRIBUTOR_WORK_ASSIGNMENT_PLAN.md`
   - Agent 01 work packages, ownership locks, transitions, schedule, and quality target.
8. `../../prompts/external-ai-contributors/CONTROLLED_TASK_PACKET_TEMPLATE.md`
   - Required task input before any contributor may start.
9. `AI_DEVELOPMENT_TOOL_STRICT_RESCREEN_V2_2026-07-21.md`
   - Historical strict re-screen. Superseded where it conflicts with V3.
10. `AI_DEVELOPMENT_TOOL_CANDIDATE_AUDIT_2026-07-21.md`
    - Historical V1 candidate audit retained as evidence.
11. `../../plan/AI_DEVELOPMENT_CONTRIBUTOR_COORDINATION_PLAN_DRAFT.md`
    - Original single-writer coordination research.
12. `../../sources/ai-tools/AI_DEVELOPMENT_TOOL_SOURCE_INDEX_2026-07-21.md`
    - Original source index.
13. `../../sources/ai-tools/AI_DEVELOPMENT_TOOL_SOURCE_ADDENDUM_V2_2026-07-21.md`
    - Cline, mini-SWE-agent, OpenCode, goose, OpenHands, benchmark, and maintenance evidence.

## Current final paper-qualified five

```yaml
qualification_threshold: 80

passed_to_controlled_trial:
  - candidate: Cline
    contributor_id: CLINE-01
    score: 86
    role: supervised_primary_implementation_engineer
  - candidate: OpenHands_Core
    contributor_id: OPENHANDS-01
    score: 84
    role: Docker_isolated_fallback_and_reproduction_engineer
  - candidate: mini_SWE_agent
    contributor_id: MSWE-01
    score: 83
    role: isolated_independent_patch_and_trajectory_analyst
  - candidate: Aider
    contributor_id: AIDER-01
    score: 82
    role: surgical_test_and_lint_repair_specialist
  - candidate: PR_Agent
    contributor_id: PRAGENT-01
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

## Designated ownership flow

```text
CLINE-01 plans and implements
→ AIDER-01 may repair one exact failure after Cline stops
→ MSWE-01 may compare on an isolated frozen snapshot
→ OPENHANDS-01 may reproduce or replace a stopped writer when explicitly activated
→ PRAGENT-01 reviews a stable draft PR read-only
→ human decision
```

OpenHands is a fallback/reproduction role, not an automatic second implementation pass. No contributor may edit overlapping paths concurrently.

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

## Current safety and activation state

```yaml
roles_defined: true
work_packages_defined: true
canonical_commands_defined_in_individual_charters: true
one_active_writer_per_task: required
parallel_writers_on_overlapping_paths: prohibited
direct_main_write: prohibited
automatic_merge: prohibited
force_push: prohibited
runtime_activation: not_authorized
universal_accuracy_claim: prohibited
exact_Galax_trial_required: true
MCP_mesh_approved: false
candidate_tools_installed_by_repository: false
credentials_added: false
repository_write_access_granted: false
Agents_02_to_15: disabled
```
