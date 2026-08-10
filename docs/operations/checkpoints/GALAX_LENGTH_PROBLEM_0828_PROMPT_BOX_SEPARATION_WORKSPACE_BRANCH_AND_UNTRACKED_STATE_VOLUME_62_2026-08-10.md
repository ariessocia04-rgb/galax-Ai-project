# Galax Length-Problem 08:28 — Prompt-Box Separation Workspace, Branch, and Untracked-State Recovery — Volume 62

```yaml
document_id: GALAX_LENGTH_PROBLEM_0828_PROMPT_BOX_SEPARATION_WORKSPACE_BRANCH_AND_UNTRACKED_STATE_VOLUME_62_2026_08_10
record_type: LENGTH_PROBLEM_APPEND_ONLY_CURRENT_STATE
recorded_date_local: 2026-08-10
recorded_time_local_24h: "08:28:00"
timezone_name: Asia/Manila
timezone_offset: "+08:00"
recorded_local_datetime: 2026-08-10T08:28:00+08:00
repository: ariessocia04-rgb/galax-Ai-project
continuity_branch: docs/new-chat-continuity-2026-07-27
continuity_PR: 10
continuity_head_before_write: 33ea940d62ee22217798b4437c5d5d8c3b188a19
previous_checkpoint_file: docs/operations/checkpoints/GALAX_LENGTH_PROBLEM_0717_ASSIGNMENT_060_R7_UNTRACKED_SCOPE_PASS_AND_HEADER_RULE_VERIFICATION_VOLUME_61_2026-08-10.md
previous_checkpoint_stop_local_datetime: 2026-08-10T07:17:32+08:00
coverage_start_local_datetime: 2026-08-10T07:17:32+08:00
coverage_end_local_datetime: 2026-08-10T08:28:00+08:00
exact_stop_point_local_datetime: 2026-08-10T08:28:00+08:00
next_upload_resume_after_local_datetime: 2026-08-10T08:28:00+08:00
elapsed_since_previous_checkpoint_stop: 1h10m28s
one_hour_boundary_reached: true
direct_Human_Owner_update_command: true
new_verified_nonduplicate_material_events_after_previous_boundary: 7
achievement_record_changed_by_this_cycle: false
latest_achievement_entry_number_present: 71
runtime_or_source_change_by_this_checkpoint: false
implementation_branch_changed_by_this_checkpoint: false
locked_accepted_work_changed_by_this_checkpoint: false
authority_mode: LIVE_STANDING_AUTHORIZATION
```

## 1. Continuity decision and achievement duplicate check

The Human Owner explicitly instructed `lenth problem update`, which is treated as `update length problem` under the active Galax continuity contract. Skill 5 therefore performs the bounded continuity upload directly through the connected GitHub app and does not delegate the checkpoint write to Cline.

The live achievement record still ends at Achievement 71. The current main-repository worktree status result is materially the same local-state family already preserved by prior achievements, especially Achievement 32 and the later commit-scope/state reconciliation records: the same `implementation/foundation-agent-01` local HEAD `0f02475df29b567253131f53c8fa5b162c12ec94` and the same five untracked top-level paths are again visible. The new `git status --short --branch` receipt adds the current `[behind 1]` upstream relationship, but the one-commit remote lead is also consistent with prior ancestry evidence and the live remote branch head `f41f53beffabd5f9ac1f83920e0141f5925cedbb`, whose parent is the local HEAD.

Therefore no new Achievement 72 is appended in this cycle. This checkpoint records the current continuation boundary without duplicating a materially equivalent achievement.

## 2. New verified material after Volume 61

### 2.1 Router branch advanced to the one-hour continuity cadence commit

```yaml
evidence_classification: REMOTE_PROVEN
branch: docs/chatgpt-skill-router-2026-08-02
current_head_sha: 8334535625227098043ac04043991b5a950a75a1
commit_message: docs(router): route one-hour continuity cadence
commit_datetime_utc: 2026-08-09T23:25:40Z
commit_datetime_Asia_Manila: 2026-08-10T07:25:40+08:00
parent_sha: 0253a7bab7e84f7836c6839c00b1118b9887be06
compare_status: ahead
commits_ahead_of_parent: 1
changed_files:
  - docs/skills/chatgpt/00_GALAX_SKILL_ROUTER_MANAGER.md
changed_file_additions: 2
changed_file_deletions: 2
```

This is a documentation/governance event only. It changes no Galax runtime, source, tests, implementation branch, CrewAI architecture, merge state, or deployment state.

### 2.2 Prompt-box-separation PLAN task initially blocked on the wrong workspace

```yaml
evidence_classification: HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE
assignment_id: GALAX_CHATGPT_CLINE_PROMPT_BOX_SEPARATION_PLAN_20260810_01
mode: PLAN_ONLY
required_workspace: C:\Users\socia\Desktop\repo clone GALAX\galax-Ai-project
initial_observed_workspace: C:\Users\socia\Desktop\repo clone GALAX\galax-phase-2b-agent01-runtime
blocker: BLOCKED_REPOSITORY_STATE_MISMATCH
files_read_from_wrong_workspace: []
commands_run_to_discover_or_switch_workspace: []
files_modified: []
tests_run: []
Git_mutations: []
preview_started: false
```

The Human Owner rejected the attempted `/AGENTS.md` read from the wrong workspace and rejected a proposed PowerShell workspace-discovery command. The exact correction preserved the task and required Cline to stop rather than search, switch, or run commands automatically.

### 2.3 Human Owner manually switched Cline to the correct repository folder

```yaml
evidence_classification: HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE
Human_Owner_action: manually_switched_Cline_workspace
reported_workspace_after_switch: C:\Users\socia\Desktop\repo clone GALAX\galax-Ai-project
automatic_Cline_workspace_switch: false
```

The workspace switch itself did not prove the local branch or HEAD, so a separate bounded identity-validation task was required.

### 2.4 Local repository identity validation completed with branch/HEAD mismatch

```yaml
evidence_classification: HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE
assignment_id: GALAX_CHATGPT_CLINE_PROMPT_BOX_SEPARATION_LOCAL_IDENTITY_VERIFY_20260810_02
mode: VALIDATION_ONLY
exact_command: Write-Output $PWD.Path; git remote get-url origin; git branch --show-current; git rev-parse HEAD
observed_workspace: C:\Users\socia\Desktop\repo clone GALAX\galax-Ai-project
observed_remote: https://github.com/ariessocia04-rgb/galax-Ai-project.git
observed_branch: implementation/foundation-agent-01
observed_head_sha: 0f02475df29b567253131f53c8fa5b162c12ec94
expected_target_branch: docs/chatgpt-skill-router-2026-08-02
expected_target_head_sha: 8334535625227098043ac04043991b5a950a75a1
workspace_match: true
repository_match: true
branch_match: false
head_match: false
final_status: BLOCKED_REPOSITORY_STATE_MISMATCH
files_read: []
files_modified: []
tests_run: []
Git_mutations: []
```

The wrapper reported that command completion could not be observed through shell integration, but the same terminal visibly contained all four requested values. Those values are retained as Human Owner-provided Cline evidence and are not upgraded into remote proof.

### 2.5 Remote implementation branch proves the local branch is one commit behind

```yaml
evidence_classification: REMOTE_PROVEN
remote_branch: implementation/foundation-agent-01
remote_head_sha: f41f53beffabd5f9ac1f83920e0141f5925cedbb
remote_head_commit_message: docs(governance): add owner checkpoint directive
remote_head_parent_sha: 0f02475df29b567253131f53c8fa5b162c12ec94
local_head_from_Cline_evidence: 0f02475df29b567253131f53c8fa5b162c12ec94
safe_relationship_conclusion: local_HEAD_is_direct_parent_of_current_remote_head
```

This remote evidence supports the later short-status `[behind 1]` report. It does not authorize pull, fast-forward, checkout, switch, merge, rebase, reset, clean, stash, or any other Git mutation.

### 2.6 Current worktree-status task completed PASS and stopped without mutation

```yaml
evidence_classification: HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE
source_primary_skill: $galax-evidence-validation-acceptance-guardian
assignment_id: GALAX_PROMPT_BOX_SEPARATION_CURRENT_WORKTREE_STATUS_20260810_03
mode: GIT_ONLY
authorized_command: git status --short --branch
executed_command: git status --short --branch
observed_branch_header: "## implementation/foundation-agent-01...origin/implementation/foundation-agent-01 [behind 1]"
tracked_modified_paths: []
staged_paths: []
deleted_paths: []
renamed_paths: []
conflicted_paths: []
untracked_paths:
  - .clinerules/workflows/
  - .vscode/
  - research/
  - src/galax/__pycache__/
  - src/galax/foundation/__pycache__/
untracked_path_count: 5
worktree_clean: false
local_changes_present: true
branch_switch_safety_conclusion: LOCAL_CHANGES_REQUIRE_SEPARATE_REVIEW
files_modified_by_task: []
Git_mutations: []
unauthorized_actions: []
review_status: PASS
```

The shell-integration wrapper again stated that completion could not be observed, while the same terminal visibly showed the full `git status --short --branch` output. No numeric exit code is inferred from the wrapper. The bounded review accepts the visible Git-status facts only.

### 2.7 No prompt-box-separation governance patch has been previewed or saved yet

```yaml
evidence_classification: HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE
parent_assignment_id: GALAX_CHATGPT_CLINE_PROMPT_BOX_SEPARATION_PLAN_20260810_01
three_file_preview_completed: false
three_file_preview_saved: false
files_modified: []
source_or_tests_changed: false
runtime_or_CrewAI_changed: false
Git_commit_or_push_for_prompt_box_rule: false
```

The intended governance target remains a synchronized three-file rule only:

```yaml
target_files:
  - AGENTS.md
  - docs/skills/chatgpt/02_GALAX_STRICT_CLINE_PROMPT_GUARDIAN.md
  - docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md
required_rule:
  - the three-line Cline handoff header is Human-Owner-facing metadata only
  - the header must remain outside every copyable Cline prompt/payload
  - NEW copyable payload begins directly with GALAX_CLINE_TASK_V2 unless another exact authorized schema controls
  - STAY copyable payload begins directly with the exact correction/action/review instruction without repeating the header inside
  - owner metadata and copyable payload remain visually and semantically separate
```

No part of that three-file patch is accepted as previewed, edited, saved, committed, pushed, or remotely published yet.

## 3. Current exact active track

```yaml
active_project: Galax_AI
active_track: ChatGPT_Cline_governance_prompt_box_separation
parent_assignment_id: GALAX_CHATGPT_CLINE_PROMPT_BOX_SEPARATION_PLAN_20260810_01
latest_completed_support_assignment: GALAX_PROMPT_BOX_SEPARATION_CURRENT_WORKTREE_STATUS_20260810_03
active_workspace: C:\Users\socia\Desktop\repo clone GALAX\galax-Ai-project
current_local_branch_from_Cline_evidence: implementation/foundation-agent-01
current_local_head_from_Cline_evidence: 0f02475df29b567253131f53c8fa5b162c12ec94
current_remote_implementation_branch_head: f41f53beffabd5f9ac1f83920e0141f5925cedbb
target_governance_branch: docs/chatgpt-skill-router-2026-08-02
target_governance_branch_head: 8334535625227098043ac04043991b5a950a75a1
local_target_branch_match: false
local_target_head_match: false
local_worktree_clean: false
untracked_paths_requiring_preservation_review:
  - .clinerules/workflows/
  - .vscode/
  - research/
  - src/galax/__pycache__/
  - src/galax/foundation/__pycache__/
three_file_governance_preview_status: NOT_STARTED
branch_switch_authorized: false
cleanup_authorized: false
stash_authorized: false
fetch_or_pull_authorized: false
```

## 4. Completed and protected work

```yaml
completed_work:
  - Volume_61_checkpoint_and_Achievement_71_persistence
  - rejected_wrong_workspace_AGENTS_read_with_exact_correction
  - rejected_unlisted_PowerShell_workspace_discovery_command_with_exact_correction
  - GALAX_CHATGPT_CLINE_PROMPT_BOX_SEPARATION_LOCAL_IDENTITY_VERIFY_20260810_02
  - GALAX_PROMPT_BOX_SEPARATION_CURRENT_WORKTREE_STATUS_20260810_03
  - Skill_3_review_of_current_worktree_status_PASS
  - verification_that_no_new_duplicate_achievement_should_be_appended
LOCKED_ACCEPTED:
  - tests/test_foundation_contracts.py::TestFoundationFlowState::test_completion_requires_pass_preflight
```

The existing Assignment 060 completed/locked work from Volume 61 remains preserved. Nothing in the current governance task unlocks, changes, invalidates, or restarts that technical work.

## 5. Actions that must not be repeated

```yaml
actions_that_must_not_be_repeated:
  - read_AGENTS_or_other_governance_target_from_galax-phase-2b-agent01-runtime_for_the_prompt_box_task
  - PowerShell_workspace_discovery_Get-ChildItem_command_rejected_in_PLAN_ONLY
  - GALAX_CHATGPT_CLINE_PROMPT_BOX_SEPARATION_LOCAL_IDENTITY_VERIFY_20260810_02_without_new_factual_identity_change
  - exact_identity_command_solely_to_reprove_the_same_workspace_remote_branch_HEAD
  - GALAX_PROMPT_BOX_SEPARATION_CURRENT_WORKTREE_STATUS_20260810_03_without_new_factual_worktree_change
  - git_status_short_branch_solely_to_reprove_the_same_five_untracked_paths_and_behind_1_state
  - automatic_git_switch_or_checkout
  - automatic_git_fetch_or_pull
  - automatic_stash_clean_restore_reset_merge_or_rebase
  - deleting_or_ignoring_any_of_the_five_untracked_paths_without_separate_review_and_authorization
  - treating_the_three_file_prompt_box_patch_as_previewed_or_saved
  - duplicate_Achievement_71_append
  - creating_Achievement_72_from_materially_duplicate_current_local_state_evidence
```

## 6. Exact stop point and safe resume boundary

```yaml
last_completed_actual_action: Skill 3 reviewed GALAX_PROMPT_BOX_SEPARATION_CURRENT_WORKTREE_STATUS_20260810_03 as PASS using the visible exact git status output and preserved shell-integration uncertainty
current_incomplete_action: determine whether the five current untracked paths would conflict with the target governance branch docs/chatgpt-skill-router-2026-08-02 before any branch switch is considered
exact_stop_stage: POST_CURRENT_WORKTREE_STATUS_PASS_BEFORE_UNTRACKED_TARGET_BRANCH_CONFLICT_REVIEW_OR_BRANCH_SWITCH
exact_stop_reason: the correct repository workspace is open and the local branch/head state is known, but the worktree contains five untracked paths and the current branch is one commit behind its own upstream; no branch-switch safety conclusion may be inferred without a separate bounded read-only conflict review
exact_safe_resume_action: after live router verification, route one separate read-only task that checks only whether the five recorded untracked paths overlap or conflict with paths present on target branch docs/chatgpt-skill-router-2026-08-02; preserve all local paths; stop with a conflict/no-conflict receipt before any git switch, checkout, cleanup, stash, fetch, pull, edit, or governance preview
allowed_next_reads_searches_edits_or_commands:
  - read_current_router
  - read_Skill_2_and_Context_Engineer_only_if_preparing_the_next_Cline_or_owner_action
  - inspect_only_the_five_recorded_untracked_path_names_against_the_exact_target_governance_branch_in_read_only_mode
  - use_current_REMOTE_PROVEN_target_branch_head_8334535625227098043ac04043991b5a950a75a1_as_the_expected_target_identity
prohibited_next_actions:
  - git_switch
  - git_checkout
  - git_fetch
  - git_pull
  - git_stash
  - git_clean
  - git_restore
  - git_reset
  - git_merge
  - git_rebase
  - git_add
  - git_commit
  - git_push
  - delete_or_modify_untracked_paths
  - start_three_file_preview_before_target_branch_safety_is_resolved
  - save_prompt_box_governance_patch
  - tests
  - Ruff_or_formatter
  - source_or_test_edit
  - merge
  - deployment
  - Agents_02_to_15
next_action_requires_Human_Owner_authorization: true
automatic_next_technical_stage_authorized: false
```

## 7. Evidence classification summary

```yaml
REMOTE_PROVEN:
  - continuity branch docs/new-chat-continuity-2026-07-27 head before this write was 33ea940d62ee22217798b4437c5d5d8c3b188a19
  - continuity PR 10 was open, draft, and unmerged at head 33ea940d62ee22217798b4437c5d5d8c3b188a19 before this write
  - target governance branch docs/chatgpt-skill-router-2026-08-02 head is 8334535625227098043ac04043991b5a950a75a1
  - router head 8334535625227098043ac04043991b5a950a75a1 is one commit ahead of 0253a7bab7e84f7836c6839c00b1118b9887be06 and changes only docs/skills/chatgpt/00_GALAX_SKILL_ROUTER_MANAGER.md
  - implementation/foundation-agent-01 remote head is f41f53beffabd5f9ac1f83920e0141f5925cedbb and its parent is local-reported HEAD 0f02475df29b567253131f53c8fa5b162c12ec94
  - current achievement record ends at Achievement 71

HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE:
  - initial prompt-box PLAN task detected wrong workspace and stopped after exact Human Owner rejections
  - Human Owner manually switched Cline to C:\Users\socia\Desktop\repo clone GALAX\galax-Ai-project
  - identity-validation terminal output shows correct workspace/remote but local branch implementation/foundation-agent-01 at 0f02475df29b567253131f53c8fa5b162c12ec94
  - current worktree status shows branch behind 1, no tracked/staged/deleted/renamed/conflicted entries, and five untracked paths
  - no prompt-box-separation file preview, edit, save, test, or Git publication occurred

REPORTED_LOCAL_NOT_REMOTE_PROOF:
  - current local Cline worktree contents inside the five untracked directories beyond the exact status path names have not been re-inspected in this task
  - the local target router branch checkout state has not been established

UNKNOWN_OR_CONFLICTING:
  - shell integration did not observe formal completion for the identity and status commands, although the same terminal visibly displayed the requested outputs
  - no numeric exit code is treated as factual for the current status command
```

## 8. Mandatory current-chat and Cline stop snapshot

```yaml
GALAX_EXACT_CHAT_AND_CLINE_STOP_SNAPSHOT_V1:
  current_chat_last_material_owner_instruction: "lenth problem update"
  current_chat_last_completed_ChatGPT_action: reviewed the bounded current-worktree-status result as PASS, determined that no new nonduplicate achievement should be appended, then performed this direct Skill 5 length-problem persistence cycle
  current_chat_unfinished_request: resume the prompt-box-separation governance task only after a separate read-only five-path target-branch conflict review establishes whether a safe branch switch may be considered

  Cline_active: false
  Cline_task_id: GALAX_PROMPT_BOX_SEPARATION_CURRENT_WORKTREE_STATUS_20260810_03
  Cline_mode: GIT_ONLY_COMPLETED_AND_STOPPED
  Cline_workspace: C:\Users\socia\Desktop\repo clone GALAX\galax-Ai-project
  Cline_branch: implementation/foundation-agent-01
  Cline_expected_or_verified_head_sha: 0f02475df29b567253131f53c8fa5b162c12ec94
  Cline_exact_target: inspect only the current Git working-tree and branch status before any possible branch switch
  Cline_exact_problem_being_fixed: preserve five untracked local paths while determining how to reach target governance branch docs/chatgpt-skill-router-2026-08-02 safely
  Cline_last_completed_action: ran exact authorized git status --short --branch and returned the five-untracked-path receipt; Skill 3 review status PASS
  Cline_current_pending_action: none; the last Cline task stopped correctly
  Cline_current_permission_or_waiting_state: waiting for a new Human Owner-authorized bounded conflict-review task before any branch switch
  Cline_edit_preview_status: NOT_REQUESTED
  Cline_validation_status: PASS
  Cline_commit_status: NOT_AUTHORIZED
  Cline_push_status: NOT_AUTHORIZED

  exact_resume_instruction_for_new_chat: >
    Verify the live router first. Preserve the current parent governance task
    GALAX_CHATGPT_CLINE_PROMPT_BOX_SEPARATION_PLAN_20260810_01 and the completed local-state
    evidence. Do not rerun the identity or short-status commands without a new factual change.
    The first and only next technical action is a separate read-only conflict review of exactly
    these five untracked paths: .clinerules/workflows/, .vscode/, research/,
    src/galax/__pycache__/, and src/galax/foundation/__pycache__/ against target branch
    docs/chatgpt-skill-router-2026-08-02 at remote head
    8334535625227098043ac04043991b5a950a75a1. The task must preserve every local path and stop
    with an exact conflict/no-conflict receipt. It must not switch branches, fetch, pull, stash,
    clean, restore, reset, merge, rebase, edit, save, test, commit, push, or begin the three-file
    prompt-box preview.

  first_action_new_chat_must_take: live-router verification followed by preparation/review of the one bounded read-only five-path target-branch conflict check
  first_action_new_chat_must_not_take: git switch, checkout, fetch, pull, stash, clean, deletion, or starting the three-file governance preview
  continuation_requires_new_owner_authorization: true
```

## 9. Architecture and authorization invariants

```yaml
Human_Owner_final_authority: true
Cline_primary_local_writer: true
ChatGPT_direct_continuity_uploader_only_for_authorized_continuity_files: true
main_write: prohibited
force_push: prohibited
implementation_branch_commit_or_push_by_this_checkpoint: false
merge: prohibited
deployment: prohibited
workflow_or_secret_change: prohibited
Agents_02_to_15: prohibited
CrewAI_runtime_changed: false
Galax_source_or_tests_changed: false
accepted_artifact_unlock: false
```

## 10. Resume status

```yaml
GALAX_LENGTH_CHECKPOINT_V2:
  previous_checkpoint_file: docs/operations/checkpoints/GALAX_LENGTH_PROBLEM_0717_ASSIGNMENT_060_R7_UNTRACKED_SCOPE_PASS_AND_HEADER_RULE_VERIFICATION_VOLUME_61_2026-08-10.md
  previous_checkpoint_stop_local_datetime: 2026-08-10T07:17:32+08:00
  coverage_start_local_datetime: 2026-08-10T07:17:32+08:00
  coverage_end_local_datetime: 2026-08-10T08:28:00+08:00
  timezone_name: Asia/Manila
  timezone_offset: "+08:00"
  exact_stop_point_local_datetime: 2026-08-10T08:28:00+08:00
  next_upload_resume_after_local_datetime: 2026-08-10T08:28:00+08:00

  repository: ariessocia04-rgb/galax-Ai-project
  continuity_branch: docs/new-chat-continuity-2026-07-27
  continuity_head_before_write: 33ea940d62ee22217798b4437c5d5d8c3b188a19
  continuity_PR: 10

  active_project: Galax_AI
  active_track: ChatGPT_Cline_governance_prompt_box_separation
  active_assignment_id: GALAX_CHATGPT_CLINE_PROMPT_BOX_SEPARATION_PLAN_20260810_01
  active_workspace: C:\Users\socia\Desktop\repo clone GALAX\galax-Ai-project
  active_branch: implementation/foundation-agent-01
  expected_or_verified_head_sha: 0f02475df29b567253131f53c8fa5b162c12ec94
  exact_target_file_test_section_symbol_prompt_or_artifact: synchronized prompt-box-separation governance rule for AGENTS.md Section 15, Skill 2 Rule 15, and CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN Section 15
  exact_failure_blocker_or_required_correction: local branch/head do not match the target governance branch/head and five untracked local paths require read-only target-branch conflict review before any branch switch

  last_completed_actual_action: GALAX_PROMPT_BOX_SEPARATION_CURRENT_WORKTREE_STATUS_20260810_03 reviewed PASS
  current_incomplete_action: five-untracked-path target-branch conflict review before branch switch
  exact_stop_stage: POST_CURRENT_WORKTREE_STATUS_PASS_BEFORE_UNTRACKED_TARGET_BRANCH_CONFLICT_REVIEW_OR_BRANCH_SWITCH
  exact_stop_reason: local state is known but branch-switch safety is not yet proven
  exact_safe_resume_action: perform one separately authorized read-only conflict review of the exact five untracked paths against docs/chatgpt-skill-router-2026-08-02 at 8334535625227098043ac04043991b5a950a75a1 and stop before any mutation
  allowed_next_reads_searches_edits_or_commands:
    - current router
    - Skill 2 and Context Engineer only for the next bounded prompt/action decision
    - exact read-only target-branch existence/conflict checks for the five recorded untracked paths
  prohibited_next_actions:
    - git_switch
    - git_checkout
    - git_fetch
    - git_pull
    - git_stash
    - git_clean
    - git_restore
    - git_reset
    - git_merge
    - git_rebase
    - git_add
    - implementation_commit
    - implementation_push
    - delete_or_modify_untracked_paths
    - start_three_file_preview_before_conflict_review
    - tests
    - Ruff_or_formatter
    - source_or_test_edit
    - merge
    - deployment

  completed_and_LOCKED_ACCEPTED_work:
    - Assignment_060_completed_R7_work_from_Volume_61_preserved
    - tests/test_foundation_contracts.py::TestFoundationFlowState::test_completion_requires_pass_preflight
  actions_that_must_not_be_repeated:
    - wrong-workspace governance read attempt
    - rejected PowerShell workspace-discovery command
    - local identity validation without new factual state change
    - git status --short --branch without new factual worktree change
    - duplicate current-state achievement append
  rejected_superseded_corrected_failed_blocked_or_no_score_work:
    - initial prompt-box PLAN execution from galax-phase-2b-agent01-runtime blocked and superseded by manual workspace correction
    - proposed Get-ChildItem workspace-discovery command rejected
    - prompt-box three-file preview remains not started

  exact_resume_point_verified: true
  runtime_or_source_change: false
  achievement_record_changed: false
  authority_mode: LIVE_STANDING_AUTHORIZATION
```
