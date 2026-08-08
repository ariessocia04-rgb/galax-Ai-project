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
cadence: event_driven_terminal_PASS_persistence_plus_every_3_hours_during_active_Galax_work
final_authority: Human_Owner
```

## Purpose

This skill protects Galax work from chat or context loss while keeping length-problem checkpoints and achievements separate.

For the exact bounded continuity exception defined by live `AGENTS.md` and `docs/operations/CODE_RED.md`, ChatGPT itself must use the connected GitHub app to create, update, commit, and publish the authorized continuity records. It must not delegate these uploads to Cline and must not generate a Cline task merely to perform a continuity upload.

A new qualifying terminal `PASS` from another repository-backed Galax skill is a mandatory event-driven achievement-persistence trigger. The PASS must be persisted before any later technical workflow stage is routed, so completed work becomes repository-backed `DO_NOT_REPEAT` evidence instead of being rediscovered after context loss.

This direct-upload authority is limited to:

```yaml
continuity_branch: docs/new-chat-continuity-2026-07-27
continuity_PR: 10
allowed_length_directory: docs/operations/checkpoints
allowed_length_naming_rule: GALAX_LENGTH_PROBLEM_*_VOLUME_<NEXT_NUMBER>_<YYYY-MM-DD>.md
allowed_achievement_file: docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
maximum_repository_writes_per_cycle: 2
maximum_repository_writes_per_terminal_PASS_event: 1
```

It does not authorize source, tests, dependencies, workflows, secrets, implementation branches, accepted-artifact changes, merge, or deployment.

## Human Owner direct-command interpretation

When the Human Owner gives a direct command in the active Galax conversation, ChatGPT must execute the exact bounded GitHub update itself when the target and scope are already clear from the immediately preceding context and live repository evidence.

```yaml
DIRECT_UPDATE_COMMANDS_V1:
  update:
    meaning: execute_the_exact_current_bounded_repository_update_already_under_discussion
    require_unambiguous_current_target: true
    delegate_to_Cline: false

  update_my_repo:
    meaning: execute_the_exact_current_bounded_repository_update_already_under_discussion
    require_unambiguous_current_target: true
    delegate_to_Cline: false

  update_length_problem:
    meaning: directly_create_and_publish_the_next_valid_numbered_length_checkpoint
    executor: ChatGPT_connected_GitHub_app
    Cline_required: false

  update_achievement:
    meaning: directly_check_for_and_append_only_new_verified_achievements
    executor: ChatGPT_connected_GitHub_app
    update_when_none_exists: false
    Cline_required: false

  update_length_problem_and_achievement:
    meaning: perform_the_separate_achievement_check_and_length_checkpoint_cycle
    commit_order:
      - achievement_first_only_when_new_verified_achievement_exists
      - length_checkpoint_second
    combine_into_one_file_or_commit: false
    executor: ChatGPT_connected_GitHub_app
    Cline_required: false
```

A direct command is execution authority for the exact current bounded target; it is not merely a request to draft instructions or create a Cline prompt.

When `update` or `update my repo` is ambiguous because no exact current target is established, ChatGPT must reconstruct the smallest live repository context needed and return `BLOCKED_AMBIGUOUS_UPDATE_TARGET` rather than guessing, broadening scope, or delegating to Cline.

Direct update commands never authorize source, tests, dependencies, workflows, secrets, implementation branches, merge, deployment, or changes to `LOCKED_ACCEPTED` work unless the Human Owner separately names and authorizes that exact consequential target.

## Activation triggers

```text
update
update my repo
length problem
update length problem
save length problem
chat length problem
CODE RED
prepare or upload the next checkpoint
three hours passed
upload continuity
update achievement
check or update achievements
update length problem and achievement
update my length problem and achievement
new chat continuation
new qualifying terminal PASS from another repository-backed Galax skill
mandatory post-PASS achievement persistence routing cycle
```

Also activate during active Galax work when the latest verified checkpoint is at least three hours old.

## Mandatory terminal-PASS achievement persistence

When the router hands off a terminal PASS event, Skill 5 must treat achievement persistence as a synchronous mandatory documentation action in the active conversation. It is not background work and does not create a scheduler.

A PASS event qualifies only when all of these are proven:

```yaml
GALAX_TERMINAL_PASS_EVENT_V1:
  source_primary_skill_alias:
  source_task_or_assignment_id:
  source_terminal_status: PASS
  bounded_objective_completed: true
  new_material_result: true
  evidence_class:
  exact_completed_result:
  exact_evidence_reference:
  already_present_in_achievement_record: false
  source_is_Skill_5: false
```

Qualifying PASS results include completed bounded read-only, analysis, evidence-review, remote-review, lock-review, cleanup-audit, or other repository-supervision tasks when their exact terminal result is `PASS` and the result is materially new.

The following are not qualifying PASS events:

- router `SELECTED`;
- Cline permission `APPROVE` recommendations;
- Human Owner clicking an approval control without a completed result;
- plans, prompts, or proposed corrections merely prepared;
- unsaved previews;
- pending approvals;
- `BLOCKED`, `FAIL`, `CHANGES_REQUIRED`, or equivalent non-PASS results;
- identical PASS evidence already present in the achievement record;
- Skill 5's own persistence or continuity result.

Required terminal-PASS sequence:

```text
receive the exact qualifying PASS event from the router
→ verify live AGENTS.md and CODE_RED standing authorization
→ verify continuity branch docs/new-chat-continuity-2026-07-27 and Draft PR #10
→ fetch the current achievement record
→ prove the PASS event is not already recorded
→ preserve the exact evidence class; never upgrade local evidence to remote proof
→ append exactly one new achievement entry
→ include the source skill, assignment/task id, exact PASS result, evidence class, factual completed result, and explicit DO_NOT_REPEAT boundary
→ commit only the achievement record through the connected GitHub app
→ verify the new achievement commit remotely
→ return PASS_ACHIEVEMENT_PERSISTED and stop
```

For this event-driven sequence:

```yaml
length_checkpoint_required_in_same_event: false
length_checkpoint_side_effect: prohibited_unless_independently_due_or_directly_requested
maximum_files_changed: 1
maximum_repository_writes: 1
allowed_file: docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
allowed_branch: docs/new-chat-continuity-2026-07-27
Cline_required: false
next_technical_task_before_verified_achievement_commit: prohibited
recursive_achievement_from_Skill_5_result: prohibited
```

A stable dedupe key must be derived from the exact source identity and result boundary. Use the smallest available combination that uniquely identifies the completion, normally:

```text
source_primary_skill_alias
+ source_task_or_assignment_id
+ terminal_status PASS
+ exact_completed_result_or_receipt_identity
```

Do not create a second achievement for the same PASS merely because it is pasted again in another chat.

If the PASS qualifies but cannot be persisted because required repository access, branch/PR identity, exact evidence, timestamp, or duplicate status cannot be verified, return:

```text
BLOCKED_PASS_ACHIEVEMENT_PERSISTENCE
```

Do not route or authorize the next technical stage until the persistence blocker is resolved or the Human Owner explicitly changes the governance rule.

## Mandatory live verification

Read only the minimum required live records:

```text
README.md
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ latest numbered length-problem checkpoint when continuity state is relevant
→ separate achievement record
→ live continuity branch and Draft PR #10
→ exact current technical assignment and evidence
```

For a terminal-PASS-only persistence event, a new length checkpoint is not required merely to save the PASS. Read the latest checkpoint only when needed to disambiguate the task/result identity or when the three-hour continuity cycle is independently due.

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

Never guess a timestamp, branch, SHA, assignment, result, target, or stopping point.

## Direct ChatGPT upload rule

When the Human Owner says `update length problem`, `save length problem`, `upload continuity`, or an equivalent instruction:

```text
ChatGPT reads and verifies the live continuity records
→ reconstructs the exact current technical stop point
→ creates the next numbered length checkpoint directly through the connected GitHub app
→ verifies the final continuity branch head and PR #10
→ reports the exact commit and stops
```

When the Human Owner says `update achievement`:

```text
ChatGPT reads and verifies the achievement record and current evidence
→ determines whether a genuinely new verified achievement exists
→ when yes, appends it to the achievement file and commits through the connected GitHub app
→ when no, leaves the achievement file unchanged
→ reports the exact result and stops
```

When the router supplies a new qualifying terminal PASS:

```text
ChatGPT performs the Mandatory terminal-PASS achievement persistence sequence
→ commits only the achievement record
→ verifies the exact commit
→ stops before any later technical stage
```

When the Human Owner says `update length problem and achievement`, `update my length problem and achievement`, or equivalent:

```text
ChatGPT verifies the live repository and exact current evidence
→ performs the separate achievement check first
→ when a new verified achievement exists, updates and commits the achievement record first
→ verifies the achievement commit SHA
→ creates the next numbered length checkpoint in a separate second commit
→ when no new verified achievement exists, leaves the achievement record unchanged and creates only the length checkpoint
→ verifies the final continuity branch head and PR #10
→ reports exact evidence and stops
```

```yaml
use_Cline_for_continuity_upload: prohibited
create_Cline_prompt_for_continuity_upload: prohibited
ask_Cline_to_save_length_checkpoint: prohibited
ask_Cline_to_update_achievement_record: prohibited
ChatGPT_direct_GitHub_upload_required_when_all_live_conditions_pass: true
ChatGPT_direct_GitHub_upload_required_for_new_qualifying_terminal_PASS: true
```

If direct GitHub access, exact evidence, exact timestamp, branch, PR, or authority is unavailable, stop with `BLOCKED_CONTINUITY_AUTO_UPLOAD` for continuity cycles or `BLOCKED_PASS_ACHIEVEMENT_PERSISTENCE` for mandatory PASS persistence. Do not redirect the upload to Cline.

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

## Mandatory current-chat and Cline stop snapshot

Every time a length-problem checkpoint is saved, ChatGPT must capture the exact end of the current chat work and the exact state of the Cline work being supervised. This snapshot is mandatory even when no file was edited and even when the current task stopped at investigation, prompt preparation, permission review, preview, save, validation, correction, commit, push, or remote review.

```yaml
GALAX_EXACT_CHAT_AND_CLINE_STOP_SNAPSHOT_V1:
  current_chat_last_material_owner_instruction:
  current_chat_last_completed_ChatGPT_action:
  current_chat_unfinished_request:

  Cline_active: true | false
  Cline_task_id:
  Cline_mode:
  Cline_workspace:
  Cline_branch:
  Cline_expected_or_verified_head_sha:
  Cline_exact_target:
  Cline_exact_problem_being_fixed:
  Cline_last_completed_action:
  Cline_current_pending_action:
  Cline_current_permission_or_waiting_state:
  Cline_edit_preview_status: NOT_REQUESTED | PENDING | PROVIDED_NOT_SAVED | SAVED
  Cline_validation_status: NOT_AUTHORIZED | NOT_RUN | PASS | FAIL | BLOCKED
  Cline_commit_status: NOT_AUTHORIZED | NOT_CREATED | CREATED_LOCAL
  Cline_push_status: NOT_AUTHORIZED | NOT_PUSHED | PUSHED_REMOTE_PROVEN

  exact_resume_instruction_for_new_chat:
  first_action_new_chat_must_take:
  first_action_new_chat_must_not_take:
  continuation_requires_new_owner_authorization: true | false
```

The checkpoint must use factual values. When Cline is not active, record `Cline_active: false` and identify the actual active track instead of inventing a Cline task.

The `exact_resume_instruction_for_new_chat` must be written as one executable continuation boundary, not a vague summary. It must state exactly:

- what was being fixed or investigated;
- the exact file, test, section, symbol, prompt, receipt, permission, or command involved;
- what Cline already completed;
- what Cline has not yet completed;
- what the Human Owner already approved;
- what still requires separate approval;
- the first and only next action;
- the exact stop condition for that next action.

The new chat must continue from this snapshot after verifying the live repository. It must not go back to an older checkpoint merely because it contains more history. It must not choose another track while this recorded task remains incomplete.

```yaml
new_chat_resume_priority:
  latest_valid_length_checkpoint_exact_snapshot: first
  live_repository_verification: required
  older_checkpoint_history: reference_only
  old_chat_memory: last

resume_same_incomplete_part: required
change_track_before_current_task_is_completed_or_factually_blocked: prohibited
repeat_Cline_completed_action: prohibited
skip_Cline_pending_gate: prohibited
assume_pending_preview_was_saved: prohibited
assume_saved_edit_was_validated: prohibited
assume_local_commit_was_pushed: prohibited
```

If the exact current chat stop or Cline state cannot be proven, the checkpoint must stop with `BLOCKED_EXACT_RESUME_POINT_UNVERIFIED`. It must not save a guessed continuation instruction.

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
  terminal_PASS_is_mandatory_achievement_trigger: true
  persist_terminal_PASS_before_next_technical_task: true
  dedupe_terminal_PASS_before_append: true
  preserve_exact_evidence_class: true
  mark_persisted_PASS_as_DO_NOT_REPEAT: true
  keep_current_achievement_boundary_until_new_verified_completion: true
  unfinished_current_task_does_not_replace_or_remove_prior_achievements: true
  replace_length_checkpoint: false
  modify_runtime_or_source: false
  modify_LOCKED_ACCEPTED_artifacts: false
```

The current achievement record and its latest verified achievement remain unchanged while the current technical task is unfinished, pending, blocked without a completed bounded audit result, awaiting permission, awaiting save, awaiting validation, or awaiting commit or push evidence **unless a separate bounded subtask itself has already ended in a new qualifying terminal PASS**. A completed qualifying PASS must be persisted even when a larger parent assignment remains unfinished.

These are not achievements:

- starting or continuing a task;
- reading a file when the read itself has not reached a bounded terminal PASS review;
- preparing or displaying a prompt;
- requesting permission;
- an `APPROVE` permission recommendation;
- an unsaved preview;
- pending approval;
- incomplete correction;
- an edit that has not reached its required evidence and acceptance boundary;
- failed validation by itself unless the factual bounded audit result is the completed authorized objective and receives terminal PASS under its governing skill;
- speculation;
- repeated old work;
- unsupported local claims;
- Skill 5's own successful persistence result.

When no new verified achievement exists:

```yaml
new_verified_achievement_exists: false
achievement_upload_action: DO_NOT_CHANGE_ACHIEVEMENT_RECORD
preserve_latest_verified_achievement_as_current_boundary: true
```

When a new verified achievement exists, ChatGPT updates only:

```text
docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
```

The achievement update must append only the new verified completion, preserve every prior achievement, and normally occur before the length checkpoint in its own commit. For a terminal-PASS-only event, the achievement commit stands alone; a length checkpoint is not created unless independently due or directly requested.

## Exact direct-upload sequence

For the three-hour or direct continuity cycle:

```text
verify live repository, AGENTS.md, CODE_RED.md, latest checkpoint, achievement record, continuity branch, and PR #10
→ verify the exact current Asia/Manila timestamp
→ collect only new events after the previous exact stop boundary
→ classify every event as REMOTE_PROVEN, HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE, or REPORTED_LOCAL_NOT_REMOTE_PROOF
→ reconstruct the mandatory current-chat and Cline stop snapshot
→ determine whether a genuinely new verified achievement exists
→ when yes, update and commit the achievement record first through the connected GitHub app
→ verify the achievement commit SHA
→ create and commit the next numbered length checkpoint through the connected GitHub app
→ verify the final branch head and that PR #10 remains open, draft, and unmerged
→ report exact evidence
→ stop
```

For a mandatory terminal-PASS-only persistence cycle:

```text
verify live AGENTS.md, CODE_RED.md, achievement record, continuity branch, PR #10, and exact PASS evidence
→ verify exact Asia/Manila timestamp
→ prove the PASS is new and not duplicated
→ append one achievement entry with exact evidence classification and DO_NOT_REPEAT boundary
→ commit only the achievement record through the connected GitHub app
→ verify the achievement commit SHA and current PR state
→ return PASS_ACHIEVEMENT_PERSISTED
→ stop
```

No Cline participation is required or permitted for either sequence.

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

For terminal-PASS-only persistence, `safe_to_resume` means only that the PASS is safely recorded; a new Human Owner instruction is still required before another consequential technical stage unless another exact standing authorization applies.

## Block conditions

Stop without writing and report `BLOCKED_CONTINUITY_AUTO_UPLOAD` when any of these applies to a continuity cycle:

- repository, branch, PR, file, or previous-boundary mismatch;
- exact timestamp is unavailable or would need to be guessed;
- evidence classification is uncertain;
- exact current-chat or Cline stop snapshot cannot be proven;
- exact resume point cannot be proven;
- the proposed entry would modify or reinterpret `LOCKED_ACCEPTED` work;
- a source, runtime, test, dependency, workflow, secret, implementation, or non-continuity file would change;
- a duplicate or already-covered event would be recorded;
- the achievement record would be changed without a new verified achievement;
- GitHub access or post-write verification fails.

Stop without writing and report `BLOCKED_PASS_ACHIEVEMENT_PERSISTENCE` when a new qualifying terminal PASS exists but any of these applies:

- continuity branch or PR #10 identity cannot be verified;
- exact PASS evidence or evidence class is missing or conflicting;
- exact timestamp cannot be verified;
- achievement record cannot be fetched or safely updated;
- duplicate status cannot be determined;
- the requested write would touch anything except the achievement record;
- GitHub write or post-write verification fails.

A PASS-persistence blocker does not authorize skipping the achievement and moving to the next technical stage.

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
repeat_or_duplicate_persisted_terminal_PASS: prohibited
skip_new_terminal_PASS_achievement_persistence: prohibited
continue_to_next_technical_stage_before_PASS_persistence: prohibited
recursive_achievement_from_Skill_5_result: prohibited
invent_timestamp: prohibited
invent_current_chat_or_Cline_stop_state: prohibited
modify_completed_Cline_work: prohibited
modify_LOCKED_ACCEPTED_work: prohibited
source_or_test_change: prohibited
implementation_branch_change: prohibited
merge_or_deployment: prohibited
```

## Final authority

The Human Owner retains final authority. The standing authorization permits ChatGPT to execute only the exact bounded continuity and achievement uploads described above. It does not permit ChatGPT to expand scope, alter implementation, approve itself, merge, or deploy.
