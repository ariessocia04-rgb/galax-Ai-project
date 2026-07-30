# Galax New-Chat Continuity and Exact Resume Guide

```yaml
document_id: GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026_07_27
document_status: ACTIVE_OPERATIONAL_HANDOFF_ON_DEDICATED_BRANCH
created_at: 2026-07-27
repository: ariessocia04-rgb/galax-Ai-project
guide_branch: docs/new-chat-continuity-2026-07-27
guide_base_sha: d3dffcfe12e8e5664336bc76dcc03da7b37f14b2
canonical_continuity_protocol: docs/operations/CODE_RED.md
replaces_CODE_RED: false
purpose:
  - solve_chat_or_conversation_length_loss
  - give_a_new_chat_the_material_project_history
  - separate_completed_work_from_pending_work
  - identify_the_exact_safe_resume_point
  - prevent_duplicate_or_unauthorized_work
```

## 1. Mandatory use

Read this guide when the owner says any close variation of:

```text
CODE RED
length chat problem
chat length problem
conversation length problem
continue exact Galax flow
read the repo because the chat is full
new chat continuation
where did we stop
resume the latest Galax work
```

This guide is a current handoff snapshot. `docs/operations/CODE_RED.md` remains the canonical recovery protocol.

A new chat must not rely on this snapshot alone. It must verify the live GitHub state because branches, pull requests, issues, and SHAs may change after this document is written.

## 2. Strict new-chat rules

```yaml
new_chat_rules:
  repository_first: required
  guess_from_old_chat_memory: prohibited
  ask_owner_to_repeat_known_repository_history: prohibited_when_repository_access_exists
  silently_continue_previous_work: prohibited
  assume_issue_activation_started_Cline: prohibited
  assume_displayed_patch_was_saved: prohibited
  assume_local_work_exists_remotely: prohibited
  repeat_completed_action: prohibited
  restore_rejected_code: prohibited
  modify_LOCKED_ACCEPTED_work_without_unlock_contract: prohibited
  infer_commit_or_push_authority: prohibited
  infer_merge_or_deployment_authority: prohibited
  start_Agents_02_to_15: prohibited
  simultaneous_writers: prohibited
```

Before answering with a status or performing work, the new chat must:

```text
verify repository identity
→ verify the current branch and exact HEAD required by the active assignment
→ read README.md
→ read AGENTS.md
→ read docs/operations/CODE_RED.md completely
→ read this guide completely
→ read the active Foundation and Agent 01 contracts
→ read the active Phase 2A plan
→ inspect Draft PR #7
→ inspect Draft PR #8
→ inspect GitHub Issue #9 and its newest comments
→ separate remote-proven facts from reported local facts
→ return the required continuation receipt
→ continue only from the exact safe resume action
```

## 3. Source-of-truth order

Use this priority when records conflict:

```text
current README readiness
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ this current continuity guide after live-state verification
→ Foundation Agent 01 Flow execution contract
→ CrewAI 1.15.4 remediation blueprint
→ accepted Phase 2A external-review plan
→ exact active GitHub assignment
→ current branches, commits, PRs, issues, comments, and test evidence
→ historical plans and records
→ old conversation memory or summaries
```

Conflict rules:

```yaml
conflict_handling:
  unresolved_higher_authority_conflict: BLOCKED_SUPERSESSION_CONFLICT
  repository_access_missing: BLOCKED_REPOSITORY_ACCESS_REQUIRED
  branch_or_SHA_mismatch: BLOCKED_REPOSITORY_STATE_MISMATCH
  local_claim_without_remote_or_artifact_evidence: REPORTED_LOCAL_NOT_REMOTE_PROOF
  issue_or_PR_text_alone_proves_execution: false
```

## 4. Material history from the beginning to the current stop point

This section records the completed material milestones. It is not a verbatim chat transcript and contains no private chain-of-thought.

### Milestone 1 — Repository-first governance established

The project was organized as a controlled CrewAI research and implementation repository rather than an unrestricted one-shot build.

```yaml
completed_decisions:
  repository_must_be_folderized_and_clean: true
  README_and_repository_rules_must_be_read_before_work: true
  prompts_and_assignments_must_be_specific_not_vague: true
  unsupported_CrewAI_capabilities_must_not_be_assigned: true
  external_facts_must_be_verified_before_architecture_changes: true
  no_agent_implementation_without_explicit_approval: true
```

### Milestone 2 — CrewAI remediation direction selected

The CrewAI `1.15.4` remediation blueprint selected a deterministic and strictly sequential baseline.

```yaml
CrewAI_runtime_baseline:
  process: sequential
  planning: false
  reasoning: false
  memory: false
  allow_delegation: false
  allow_code_execution: false
  async_execution: false
  parallel_agents: false
  parallel_tool_calls: false
  generic_or_unfiltered_MCP: prohibited
  role_scoped_gateways: required
  Agents_02_to_15: disabled
```

This baseline must not be silently replaced by newer framework features, remembered examples, or a different architecture.

### Milestone 3 — Foundation and Agent 01 architecture fixed

The active Foundation Agent 01 Flow contract established:

```yaml
Foundation_Agent_01_invariants:
  RepositoryPreflightTool_owner: GalaxFoundationFlow
  RepositoryPreflightTool_invoked_before_Agent_01: true
  RepositoryPreflightTool_calls_per_run: 1
  engineering_manager_tools: []
  Agent_01_direct_tool_calls: 0
  Agent_01_LLM_calls: 1
  Agent_01_output: AgentTaskResult
  result_as_answer_for_this_path: prohibited
  hidden_second_agent_call: prohibited
  HumanReviewRequest_builder: pure_Python_Pydantic
  explicit_router_for_every_branch: required
  blocked_route_reaches_success: prohibited
  LLM_profiles_enabled: false
  Agents_02_to_15_enabled: false
```

No current documentation task may change these runtime invariants.

### Milestone 4 — CODE RED became canonical

On `2026-07-22`, the old operation-length protocol was replaced by `CODE RED` as the canonical repository continuity system.

```yaml
canonical_file: docs/operations/CODE_RED.md
legacy_file: docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md
legacy_file_status: COMPATIBILITY_REDIRECT
```

CODE RED defines the required reconstruction procedure, receipt, action ledger, cleanup policy, accepted-work protection, current stage, and exact next action.

### Milestone 5 — Foundation Stage 0 setup was recorded

The existing CODE RED ledger records the material Foundation setup stages:

```yaml
Stage_0A:
  status: PASS_REPORTED_LOCAL
  commit: e214e665651d6a9694e161c65f22762a251043df

Stage_0B:
  status: COMPLETED_WITH_OWNER_PROVIDED_OFFICIAL_EVIDENCE
  python: ">=3.10,<3.14"
  crewai: "1.15.4"
  pydantic: "2.12.5"
  pytest: "9.0.3"
  ruff: "0.15.1"
  uv: "0.11.29"

Stage_0C:
  status: PASS_REPORTED_LOCAL
  known_head: e382246d0b6b80636b1c4307e5c0e4ee66a76425

Stage_0D:
  status: PASS_REPORTED_LOCAL
  uv_resolved_packages: 152

Stage_0E:
  status: PASS_REPORTED_LOCAL
  python_runtime: 3.13.14
  actual_import_evidence: IMPORTS_OK
```

These historical local-stage records must be interpreted together with the newer remote implementation evidence below.

### Milestone 6 — Phase 2A governance contracts were implemented and pushed

The first remote Phase 2A implementation commit is:

```yaml
commit: 0f02475df29b567253131f53c8fa5b162c12ec94
message: "feat(foundation): add Phase 2A governance contracts"
branch: implementation/foundation-agent-01
```

Material changed paths recorded for that commit:

```text
docs/operations/CODE_RED.md
src/galax/__init__.py
src/galax/foundation/__init__.py
src/galax/foundation/models.py
tests/test_foundation_contracts.py
```

Reported focused validation evidence recorded in Draft PR #7:

```yaml
focused_tests: 70_passed
pytest_exit_code: 0
git_diff_cached_check: PASS
tracked_deletions: none
```

### Milestone 7 — Length-problem checkpoint directive was added

The second remote implementation-branch commit is:

```yaml
commit: f41f53beffabd5f9ac1f83920e0141f5925cedbb
message: "docs(governance): add owner checkpoint directive"
branch: implementation/foundation-agent-01
```

It expanded:

```text
docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md
```

with the standing `SAVE_CURRENT_TASK_CHECKPOINT` directive.

That directive requires every explicit stop, pause, continue-later, new-chat, or length-problem message to preserve:

```yaml
active_assignment_id:
active_mode:
last_completed_actual_action:
successfully_saved_files: []
displayed_but_not_executed_actions: []
rejected_actions: []
pending_human_approval:
actions_that_must_not_be_repeated: []
validation_status:
commit_status:
push_status:
pull_request_status:
exact_stop_point:
exact_safe_resume_action:
```

It also establishes that the AI cannot detect a silent browser close or background inactivity. An explicit owner message or a controlled stage boundary is required.

### Milestone 8 — Draft PR #7 became the implementation review surface

```yaml
Draft_PR: 7
state: open
is_draft: true
merged: false
head_branch: implementation/foundation-agent-01
current_head_sha: f41f53beffabd5f9ac1f83920e0141f5925cedbb
commits: 2
changed_files: 6
```

Draft PR #7 remains separate from the later governance-plan work. It is not merged and no deployment is authorized.

### Milestone 9 — ChatGPT, Cline, Draft PR, and external reviewer governance was designed

The selected development-control model is:

```yaml
ChatGPT:
  role:
    - repository_aware_architect
    - exact_assignment_author
    - canonical_exact_diff_reviewer

Cline:
  role: SOLE_PRIMARY_LOCAL_WRITER
  redesign_authority: false

Human_Owner:
  final_authority: true

PR_Agent:
  mode: REVIEW_ONLY
  optional: true

Codex:
  mode: REVIEW_ONLY
  optional: true

custom_bridge: deferred
custom_MCP_bridge: prohibited_now
simultaneous_writers: prohibited
```

### Milestone 10 — Initial Phase 2A external-review plan was published

```yaml
plan_branch: plan/phase-2a-external-review-layer-2026-07-27
initial_plan_commit: 32f3f0862ed67023b24067e416508d804e551920
plan_file: docs/plan/PHASE_2A_TRI_AI_ALIGNMENT_AND_RECOVERY_PLAN_2026-07-27.md
Draft_PR: 8
```

The first plan was reviewed against the original CrewAI remedy and Foundation Agent 01 contract.

### Milestone 11 — Compatibility defects were found and corrected

Three material alignment defects were corrected:

```yaml
corrections:
  - Foundation_contract_Section_11_was_added_to_the_bounded_documentation_scope
  - PR_Agent_and_Codex_were_made_strictly_sequential_when_both_are_selected
  - policy_scope_was_limited_to_new_Governance_Foundation_and_Agent_01_assignments
```

The corrected plan commit is:

```yaml
commit: d3dffcfe12e8e5664336bc76dcc03da7b37f14b2
branch: plan/phase-2a-external-review-layer-2026-07-27
```

The corrected dual-review order is:

```text
PR-Agent REVIEW_ONLY
→ verify the current PR head is unchanged
→ Codex REVIEW_ONLY on the same current head
→ ChatGPT canonical exact-diff review
→ Human Owner decision
```

Parallel external reviews are prohibited. A head change makes the previous receipt stale.

### Milestone 12 — Human Owner accepted the corrected plan

The Human Owner explicitly accepted Draft PR #8 at exact head:

```text
d3dffcfe12e8e5664336bc76dcc03da7b37f14b2
```

Acceptance authorized only the bounded Cline preparation, reading, and seven-file documentation edits defined by Issue #9.

### Milestone 13 — GitHub Issue #9 was activated for Cline

```yaml
Issue: 9
title: "[CLINE-ACT AUTHORIZED] Implement corrected Phase 2A external review governance plan"
execution_status: ACTIVE_AUTHORIZED
assignment_id: PHASE_2A_EXTERNAL_REVIEW_GOVERNANCE_ACT_002
branch: plan/phase-2a-external-review-layer-2026-07-27
expected_head_sha: d3dffcfe12e8e5664336bc76dcc03da7b37f14b2
contributor: Cline
mode: ACT_BOUNDED
human_authorized: true
```

Exactly authorized:

```yaml
authorized_actions:
  - prepare_dedicated_worktree
  - verify_repository_branch_HEAD_and_clean_status
  - read_all_required_repository_files
  - edit_only_the_seven_allowlisted_governance_files
```

Not authorized:

```yaml
not_authorized:
  - validation_commands_beyond_initial_repository_verification
  - commit
  - push
  - Draft_PR_mutation
  - PR_Agent_trigger
  - Codex_trigger
  - merge
  - deployment
```

Issue activation does not automatically start Cline. GitHub has recorded permission, not execution. A human must still open Cline and direct it to the exact Issue #9 assignment.

## 5. Current exact remote state at this checkpoint

```yaml
checkpoint_date: 2026-07-27
repository: ariessocia04-rgb/galax-Ai-project

research_branch:
  name: agent/agent-01-tool-inspection
  head_sha: dcce208f2d83da25b655e11975705ab783791a92

implementation_branch:
  name: implementation/foundation-agent-01
  head_sha: f41f53beffabd5f9ac1f83920e0141f5925cedbb

plan_branch:
  name: plan/phase-2a-external-review-layer-2026-07-27
  accepted_head_sha: d3dffcfe12e8e5664336bc76dcc03da7b37f14b2

Draft_PR_1:
  state: open_draft
  merged: false
  head_branch: agent/agent-01-tool-inspection

Draft_PR_7:
  state: open_draft
  merged: false
  head_branch: implementation/foundation-agent-01
  head_sha: f41f53beffabd5f9ac1f83920e0141f5925cedbb
  commits: 2
  changed_files: 6

Draft_PR_8:
  state: open_draft
  merged: false
  head_branch: plan/phase-2a-external-review-layer-2026-07-27
  head_sha: d3dffcfe12e8e5664336bc76dcc03da7b37f14b2
  commits: 2
  changed_files: 1

Issue_9:
  state: open
  execution_status: ACTIVE_AUTHORIZED
  Cline_execution_proven: false
  Cline_readiness_receipt_received: false
  Cline_act_result_received: false
```

Every SHA and state above must be re-read live by a new chat. A mismatch does not authorize an update. It requires a repository-state reconciliation first.

## 6. Completed, active, and pending classification

```yaml
COMPLETED:
  - repository_first_governance_created
  - CrewAI_1_15_4_remediation_baseline_selected
  - Foundation_Agent_01_runtime_invariants_selected
  - CODE_RED_canonical_protocol_created
  - Phase_2A_governance_contract_commit_pushed_to_implementation_branch
  - owner_length_checkpoint_directive_pushed_to_implementation_branch
  - Draft_PR_7_created
  - external_review_governance_plan_created
  - plan_compatibility_defects_corrected
  - corrected_plan_pushed_to_Draft_PR_8
  - Human_Owner_accepted_corrected_plan
  - Issue_9_activated

ACTIVE_NOT_PROVEN_COMPLETE:
  - Cline_Issue_9_ACT_BOUNDED_execution

NOT_STARTED_OR_NOT_AUTHORIZED:
  - Cline_readiness_receipt
  - seven_file_edits
  - local_diff_review
  - documentation_validation
  - commit_authorization
  - commit_creation
  - push_authorization
  - push
  - final_Draft_PR_diff_review
  - optional_PR_Agent_review
  - optional_Codex_review
  - Human_final_acceptance
  - CODE_RED_LOCKED_ACCEPTED_record
  - merge
  - deployment
```

## 7. Seven files Cline may edit

```text
AGENTS.md
README.md
docs/operations/CODE_RED.md
docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md
docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md
docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md
```

Strict Foundation contract boundary:

```yaml
file: docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
allowed_section: Section_11_External_contributor_boundary_only
Sections_1_to_10: prohibited
Section_12: prohibited
runtime_architecture_change: prohibited
Agent_01_invariant_change: prohibited
maximum_changed_files: 7
```

## 8. Exact current stop point

```yaml
last_completed_actual_action:
  - corrected_plan_accepted_by_Human_Owner
  - Issue_9_changed_to_ACTIVE_AUTHORIZED
  - acceptance_record_added_to_Draft_PR_8

Cline_execution_status:
  permission_recorded_in_GitHub: true
  automatically_triggered: false
  worktree_preparation_proven: false
  required_files_read_proven: false
  readiness_receipt_received: false
  edits_proven: false

exact_stop_point: WAITING_FOR_CLINE_EXECUTION_READINESS_RECEIPT_V1
```

## 9. Exact safe resume action

The next chat must not create another plan and must not assign another contributor.

The exact continuation is:

```text
Human Owner opens Cline manually
→ Cline opens and reads GitHub Issue #9
→ Cline prepares the dedicated worktree without touching implementation/foundation-agent-01
→ Cline verifies repository, branch, exact HEAD d3dffcfe12e8e5664336bc76dcc03da7b37f14b2, and clean tracked status
→ Cline reads all required files completely
→ Cline returns CLINE_EXECUTION_READINESS_RECEIPT_V1 before editing
→ Human checks the receipt against Issue #9
→ Cline applies only the seven bounded documentation edits
→ Cline returns CLINE_ACT_RESULT_V1
→ Cline stops before validation, commit, push, reviewer trigger, merge, or deployment
```

One-line current next action:

```text
OPEN CLINE AND EXECUTE ISSUE #9 ONLY UNTIL CLINE_ACT_RESULT_V1; DO NOT VALIDATE, COMMIT, OR PUSH.
```

## 10. Actions that must not be repeated

```yaml
do_not_repeat:
  - recreate_the_Phase_2A_external_review_plan
  - reopen_the_same_architecture_design_question
  - change_the_original_CrewAI_remediation
  - redesign_Foundation_Agent_01
  - create_another_Cline_assignment_for_the_same_work
  - create_a_parallel_writer_branch_for_the_same_seven_files
  - reauthorize_Codex_as_a_writer
  - add_Stage_10C
  - create_an_A_to_J_workflow
  - introduce_S13LOCK
  - enable_custom_MCP_bridge
  - enable_Agents_02_to_15
  - claim_Cline_started_only_because_Issue_9_is_active
```

## 11. Current prohibited actions

Until the bounded edits and the required human gates occur:

```yaml
prohibited_now:
  - modify_the_accepted_plan_file
  - move_or_force_update_the_accepted_plan_branch
  - edit_outside_the_seven_allowlisted_files
  - edit_Foundation_contract_outside_Section_11
  - change_source_code
  - change_tests
  - change_dependencies
  - change_GitHub_workflows
  - run_unapproved_validation
  - commit
  - push
  - trigger_PR_Agent
  - trigger_Codex
  - merge
  - deploy
  - direct_write_to_main
  - force_push
  - secret_access
```

## 12. Required new-chat continuation receipt

A new chat must return this before advising or acting:

```yaml
GALAX_NEW_CHAT_CONTINUATION_RECEIPT_V1:
  trigger_detected: true
  reconstructed_at_utc:
  repository: ariessocia04-rgb/galax-Ai-project
  repository_access_verified:

  files_read:
    - README.md
    - AGENTS.md
    - docs/operations/CODE_RED.md
    - docs/operations/GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md
    - docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
    - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
    - docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md
    - docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md
    - docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md
    - docs/plan/PHASE_2A_TRI_AI_ALIGNMENT_AND_RECOVERY_PLAN_2026-07-27.md

  live_remote_state:
    research_branch_head:
    implementation_branch_head:
    plan_branch_head:
    Draft_PR_7_state:
    Draft_PR_7_head:
    Draft_PR_8_state:
    Draft_PR_8_head:
    Issue_9_state:
    Issue_9_execution_status:
    latest_Issue_9_comment_summary:

  completed_milestones_confirmed: []
  reported_local_only_facts: []
  stale_or_conflicting_records: []
  Cline_readiness_receipt_available:
  Cline_act_result_available:
  current_stage:
  exact_stop_point:
  exact_next_allowed_action:
  prohibited_next_actions: []
  assumptions: []
  safe_to_continue: false
```

`safe_to_continue` may become true only after the live branch, SHA, PR, issue, and receipt evidence agree with the active assignment.

## 13. Mandatory checkpoint after every coherent job

When a task stops, reaches a human gate, moves to a new chat, or approaches the context limit, record:

```yaml
SAVE_CURRENT_TASK_CHECKPOINT_V1:
  recorded_at_utc:
  active_assignment_id:
  active_contributor:
  active_mode:
  repository:
  branch:
  starting_sha:
  current_sha_or_worktree_state:
  last_completed_actual_action:
  successfully_saved_files: []
  displayed_but_not_executed_actions: []
  rejected_actions: []
  pending_human_approval:
  actions_that_must_not_be_repeated: []
  validation_status:
  commit_status:
  push_status:
  pull_request_status:
  exact_stop_point:
  exact_safe_resume_action:
  prohibited_resume_actions: []
```

Checkpoint rules:

1. Record observable facts only.
2. Distinguish proposed, displayed, approved, executed, saved, committed, pushed, reviewed, and accepted.
3. Never mark a displayed patch as saved.
4. Never mark an active issue as executed without a contributor receipt or repository evidence.
5. Never repeat completed work.
6. Never restore rejected work.
7. A checkpoint grants no new authority.
8. Store the checkpoint in the active GitHub issue or PR when tracked-file mutation is not separately authorized.
9. Update CODE RED only through a separately authorized bounded repository change.
10. Resume only from the exact recorded safe action.

## 14. Minimal command for the next chat

```text
CODE RED / LENGTH CHAT PROBLEM.
Open repository ariessocia04-rgb/galax-Ai-project.
Read README.md, AGENTS.md, docs/operations/CODE_RED.md, and docs/operations/GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md completely.
Then read the active Foundation Agent 01 contract, CrewAI 1.15.4 remediation blueprint, corrected Phase 2A plan, Draft PR #7, Draft PR #8, and GitHub Issue #9 including its newest comments.
Verify the current research, implementation, and plan branch HEAD SHAs.
Separate remote-proven facts from reported local-only facts.
Return GALAX_NEW_CHAT_CONTINUATION_RECEIPT_V1.
Do not redesign the plan, do not duplicate completed work, do not assume Cline started, and continue only from the exact safe resume action.
```

## 15. Current status summary

```yaml
plan_and_architecture: COMPLETE
corrected_plan_publication: COMPLETE
Human_Owner_plan_acceptance: COMPLETE
Issue_9_activation: COMPLETE
Cline_execution: NOT_YET_PROVEN_STARTED
seven_file_edits: NOT_YET_PROVEN
validation: NOT_AUTHORIZED
commit: NOT_AUTHORIZED
push: NOT_AUTHORIZED
external_review: NOT_AUTHORIZED
final_acceptance: PENDING
LOCKED_ACCEPTED: false

current_stage: CLINE_ACT_BOUNDED_AUTHORIZED_WAITING_FOR_READINESS_RECEIPT
exact_next_owner: Human_Owner_then_Cline
exact_next_action: OPEN_CLINE_AND_EXECUTE_ISSUE_9_UNTIL_CLINE_ACT_RESULT_V1
```
