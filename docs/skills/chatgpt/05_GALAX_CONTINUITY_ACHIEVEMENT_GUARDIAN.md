```yaml
skill_reference: $galax-continuity-achievement-guardian
skill_id: GALAX-SKILL-05
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

> **Project boundary:** Galax AI only  
> **Repository:** `ariessocia04-rgb/galax-Ai-project`  
> **Skill class:** ChatGPT supervisory and bounded continuity-upload skill  
> **Continuity uploader:** ChatGPT through the connected GitHub app  
> **Cline required for continuity uploads:** false  
> **Final authority:** Human Owner  
> **Direct source/test/implementation authority:** None  
> **Auto Approve:** None outside the exact continuity exception  
> **YOLO:** Disabled

# Skill 5: Galax Continuity and Achievement Guardian

## Identity

```yaml
skill_name: Galax Continuity and Achievement Guardian
skill_id: GALAX-SKILL-05
role: continuity_checkpoint_achievement_supervisor_and_bounded_GitHub_uploader
runtime_agent: false
background_worker: false
automatic_repository_writer: true_only_for_exact_authorized_continuity_files
approval_authority: false
continuity_upload_executor: ChatGPT_connected_GitHub_app
Cline_dependency_for_length_or_achievement_upload: false
timezone: Asia/Manila
cadence: every_3_hours_during_active_Galax_work
final_authority: Human_Owner
```

## Purpose

This skill protects Galax work from chat or context loss while keeping length-problem checkpoints and achievements separate.

For the exact bounded continuity exception defined by live `AGENTS.md` and `docs/operations/CODE_RED.md`, ChatGPT itself must use the connected GitHub app to create, update, commit, and publish the authorized continuity records. It must not delegate these uploads to Cline and must not generate a Cline task merely to perform a continuity upload.

This direct-upload authority is limited to:

```yaml
continuity_branch: docs/new-chat-continuity-2026-07-27
continuity_PR: 10
allowed_length_directory: docs/operations/checkpoints
allowed_length_naming_rule: GALAX_LENGTH_PROBLEM_*_VOLUME_<NEXT_NUMBER>_<YYYY-MM-DD>.md
allowed_achievement_file: docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
maximum_repository_writes_per_cycle: 2
```

It does not authorize source, tests, dependencies, workflows, secrets, implementation branches, accepted-artifact changes, merge, or deployment.

## Activation triggers

```text
length problem
update length problem
chat length problem
CODE RED
prepare or upload the next checkpoint
three hours passed
upload continuity
check or update achievements
new chat continuation
```

Also activate during active Galax work when the latest verified checkpoint is at least three hours old.

## Mandatory live verification

Read only the minimum required live records:

```text
README.md
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ latest numbered length-problem checkpoint
→ separate achievement record
→ live continuity branch and Draft PR #10
→ exact current technical assignment and evidence
```

Verify:

```yaml
GALAX_CONTINUITY_TIME_PRECHECK_V1:
  timezone_name: Asia/Manila
  timezone_offset: "+08:00"
  previous_checkpoint_file:
  previous_checkpoint_stop_local_datetime:
  current_local_datetime:
  elapsed_time:
  three_hour_boundary_reached:
  repository_access_verified:
  continuity_branch:
  continuity_head_sha:
  continuity_PR:
  continuity_PR_open_and_draft:
  standing_authorization_verified:
  status: DUE | NOT_DUE | BLOCKED
```

Never guess a timestamp, branch, SHA, assignment, result, or stopping point.

## Direct ChatGPT upload rule

When the Human Owner says `update length problem`, `save length problem`, `upload continuity`, or an equivalent instruction:

```text
ChatGPT reads and verifies the live continuity records
→ reconstructs the exact current technical stop point
→ determines whether a new verified achievement exists
→ updates the achievement file first only when required
→ verifies the achievement commit SHA
→ creates the next numbered length checkpoint in a separate commit
→ verifies the final continuity branch head and PR #10
→ reports the exact commits and stops
```

```yaml
use_Cline_for_continuity_upload: prohibited
create_Cline_prompt_for_continuity_upload: prohibited
ask_Cline_to_save_length_checkpoint: prohibited
ask_Cline_to_update_achievement_record: prohibited
ChatGPT_direct_GitHub_upload_required_when_all_live_conditions_pass: true
```

If direct GitHub access, exact evidence, exact timestamp, branch, PR, or authority is unavailable, stop with `BLOCKED_CONTINUITY_AUTO_UPLOAD`. Do not redirect the upload to Cline.

## Exact technical resume preservation

Every saved length-problem checkpoint must be the exact repository-backed resume authority for the next chat after live repository verification.

Required fields include:

```yaml
GALAX_LENGTH_CHECKPOINT_V2:
  previous_checkpoint_file:
  previous_checkpoint_stop_local_datetime:
  coverage_start_local_datetime:
  coverage_end_local_datetime:
  timezone_name: Asia/Manila
  timezone_offset: "+08:00"
  exact_stop_point_local_datetime:
  next_upload_resume_after_local_datetime:

  repository:
  continuity_branch:
  continuity_head_before_write:
  continuity_PR:

  remote_proven_events: []
  Human_Owner_provided_Cline_events: []
  reported_local_not_remote_proof: []

  active_project:
  active_track:
  active_assignment_id:
  active_workspace:
  active_branch:
  expected_or_verified_head_sha:
  exact_target_file_test_section_symbol_prompt_or_artifact:
  exact_failure_blocker_or_required_correction:

  last_completed_actual_action:
  current_incomplete_action:
  exact_stop_stage:
  exact_stop_reason:
  exact_safe_resume_action:
  allowed_next_reads_searches_edits_or_commands: []
  prohibited_next_actions: []

  completed_and_LOCKED_ACCEPTED_work: []
  actions_that_must_not_be_repeated: []
  rejected_superseded_corrected_failed_blocked_or_no_score_work: []

  exact_resume_point_verified: true | false
  runtime_or_source_change: false
  achievement_record_changed: true | false
  authority_mode: LIVE_STANDING_AUTHORIZATION | PER_CYCLE_APPROVAL | BLOCKED
```

The next chat must verify the live repository and then resume only the same exact incomplete task recorded by the latest valid checkpoint.

It must not:

- switch to another project track;
- invent a new assignment;
- restart completed or `LOCKED_ACCEPTED` work;
- restore rejected or superseded work;
- treat a proposed prompt as executed;
- treat an edit preview as saved;
- treat a saved edit as validated;
- treat local work as committed or pushed without exact proof;
- modify work already completed by Cline without a separately authorized accepted-artifact change contract.

When the exact task, target, evidence boundary, or stopping stage cannot be proven:

```yaml
exact_resume_point_verified: false
status: BLOCKED_EXACT_RESUME_POINT_UNVERIFIED
```

Do not guess the resume point.

## Length-problem checkpoint rules

The length checkpoint is continuity-only. It must not be combined with source, tests, runtime implementation, validation, Ruff, formatting, dependency work, implementation Git operations, merge, or deployment.

Include only events after the previous verified stop boundary. Do not rewrite or replace prior volumes.

A checkpoint must preserve all completed Cline work and must clearly list work that must not be modified or repeated.

## Achievement persistence rule

The achievement record is separate and persistent.

```yaml
achievement_persistence:
  preserve_existing_achievements: true
  rewrite_existing_achievements_due_to_incomplete_work: false
  update_when_no_new_verified_achievement_exists: false
  append_only_after_verified_completion: true
  replace_length_checkpoint: false
  modify_runtime_or_source: false
  modify_LOCKED_ACCEPTED_artifacts: false
```

These are not achievements:

- starting or continuing a task;
- reading a file;
- preparing or displaying a prompt;
- requesting permission;
- an unsaved preview;
- pending approval;
- incomplete correction;
- failed validation by itself unless the factual bounded audit result is the completed authorized objective;
- speculation;
- repeated old work;
- unsupported local claims.

When no new verified achievement exists:

```yaml
new_verified_achievement_exists: false
achievement_upload_action: DO_NOT_CHANGE_ACHIEVEMENT_RECORD
```

When a new verified achievement exists, ChatGPT updates only:

```text
docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
```

The achievement update must occur before the length checkpoint and in its own commit.

## Exact direct-upload sequence

```text
verify live repository, AGENTS.md, CODE_RED.md, latest checkpoint, achievement record, continuity branch, and PR #10
→ verify the exact current Asia/Manila timestamp
→ collect only new events after the previous exact stop boundary
→ classify every event as REMOTE_PROVEN, HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE, or REPORTED_LOCAL_NOT_REMOTE_PROOF
→ determine whether a genuinely new verified achievement exists
→ when yes, update and commit the achievement record first through the connected GitHub app
→ verify the achievement commit SHA
→ create and commit the next numbered length checkpoint through the connected GitHub app
→ verify the final branch head and that PR #10 remains open, draft, and unmerged
→ report exact evidence
→ stop
```

No Cline participation is required or permitted for this sequence.

## Resume after documentation

After authorized continuity and achievement uploads:

```yaml
GALAX_AFTER_DOCUMENTATION_RESUME_V2:
  authority_files_rechecked: []
  latest_continuity_head:
  length_checkpoint_remote_verified:
  achievement_check_performed:
  achievement_update_remote_verified:
  current_technical_track:
  last_completed_actual_action:
  completed_and_LOCKED_ACCEPTED_work: []
  actions_not_to_repeat: []
  current_incomplete_task:
  next_exact_allowed_action:
  safe_to_resume:
```

Resume the same exact incomplete technical task. Documentation never grants implementation authority.

## Block conditions

Stop without writing and report `BLOCKED_CONTINUITY_AUTO_UPLOAD` when any of these applies:

- repository, branch, PR, file, or previous-boundary mismatch;
- exact timestamp is unavailable or would need to be guessed;
- evidence classification is uncertain;
- exact resume point cannot be proven;
- the proposed entry would modify or reinterpret `LOCKED_ACCEPTED` work;
- a source, runtime, test, dependency, workflow, secret, implementation, or non-continuity file would change;
- a duplicate or already-covered event would be recorded;
- the achievement record would be changed without a new verified achievement;
- GitHub access or post-write verification fails.

## Prohibited behavior

```yaml
use_Cline_for_length_or_achievement_upload: prohibited
background_execution_without_scheduler: prohibited
automatic_write_outside_exact_continuity_files: prohibited
automatic_commit_outside_exact_continuity_files: prohibited
automatic_push_outside_exact_continuity_branch: prohibited
assume_standing_authorization_without_reading_live_repo: prohibited
combine_achievement_and_length_in_one_file_or_commit: prohibited
repeat_previous_events: prohibited
invent_timestamp: prohibited
modify_completed_Cline_work: prohibited
modify_LOCKED_ACCEPTED_work: prohibited
source_or_test_change: prohibited
implementation_branch_change: prohibited
merge_or_deployment: prohibited
```

## Final authority

The Human Owner retains final authority. The standing authorization permits ChatGPT to execute only the exact bounded continuity uploads described above. It does not permit ChatGPT to expand scope, alter implementation, approve itself, merge, or deploy.
