# Galax Length-Problem 00:12 Mandatory New-Chat Auto-Continuity Rule — Volume 28

```yaml
document_id: GALAX_LENGTH_PROBLEM_0012_MANDATORY_NEW_CHAT_AUTO_CONTINUITY_RULE_VOLUME_28_2026_08_05
record_type: LENGTH_PROBLEM_CHAT_CONTINUITY_CHECKPOINT
instruction_class: MANDATORY_NEW_CHAT_EXECUTION_RULE
recorded_date_local: 2026-08-05
recorded_time_local_24h: "00:12:00"
timezone_name: Asia/Manila
timezone_offset: "+08:00"
recorded_local_datetime: 2026-08-05T00:12:00+08:00
repository: ariessocia04-rgb/galax-Ai-project
continuity_branch: docs/new-chat-continuity-2026-07-27
continuity_PR: 10
continuity_head_before_write: 1c10b8b7a8b6f01244719da4a0becd07a47b9721
previous_checkpoint_file: docs/operations/checkpoints/GALAX_LENGTH_PROBLEM_2357_NONSTOP_CURSOR_SEMICOMPLETE_INSTRUCTION_VOLUME_27_2026-08-04.md
previous_checkpoint_stop_local_datetime: 2026-08-04T23:57:00+08:00
coverage_start_local_datetime: 2026-08-04T23:57:00+08:00
coverage_end_local_datetime: 2026-08-05T00:12:00+08:00
exact_stop_point_local_datetime: 2026-08-05T00:12:00+08:00
next_upload_resume_after_local_datetime: 2026-08-05T00:12:00+08:00
replaces_previous_volumes: false
runtime_or_source_change: false
implementation_branch_changed: false
router_file_modified: false
Skill_5_file_modified: false
locked_accepted_work_changed: false
achievement_record_changed: false
authority_mode: HUMAN_OWNER_EXPLICIT_AND_LIVE_STANDING_CONTINUITY_AUTHORIZATION
```

## 1. Mandatory effect for every new Galax chat

Every new ChatGPT conversation, replacement model, reviewer, or repository-aware assistant handling Galax must treat this latest valid Length Problem checkpoint as an execution rule, not as optional background information.

After reading the mandatory repository continuity records, the new chat must immediately execute the following continuity bootstrap before giving a Galax status, preparing a Cline task, reviewing evidence, or continuing technical work:

```text
read README.md
→ read AGENTS.md
→ read docs/operations/CODE_RED.md completely
→ read docs/operations/GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md
→ locate and read the latest valid numbered Length Problem checkpoint
→ verify the live continuity branch and Draft PR #10
→ verify the existing Galax Auto-Upload scheduler
→ reconstruct or continue the exact continuity cursor
→ identify the exact active unresolved conversation chain
→ return the exact continuation boundary
→ continue only the one verified active task
```

The Human Owner no longer needs to say `update length problem` during every Galax conversation. The new chat is responsible for enforcing the cursor and three-hour continuity rule automatically.

## 2. Existing scheduler that must be verified, not duplicated

```yaml
GALAX_AUTO_UPLOAD_SCHEDULER_V1:
  title: Galax Auto-Upload
  task_id: 6a6e9ac862d08191860174abdc0ffa71
  required_enabled_state: true
  timing_mode: exact_schedule
  timezone: Asia/Manila
  schedule: |
    BEGIN:VEVENT
    DTSTART;TZID=Asia/Manila:20260805T025700
    RRULE:FREQ=HOURLY;INTERVAL=3
    END:VEVENT
  purpose: run_the_authorized_Length_Problem_continuity_cycle_every_3_hours_even_when_the_Human_Owner_is_offline
  duplicate_scheduler_creation: prohibited
```

Required new-chat behavior:

```yaml
scheduler_verification:
  check_existing_task_by_exact_task_id: required
  verify_is_enabled_true: required
  verify_three_hour_schedule: required
  verify_Asia_Manila_timing: required
  verify_prompt_targets_Galax_continuity_only: required

  when_enabled_and_matching:
    action: KEEP_EXISTING_TASK

  when_existing_task_is_disabled_and_automation_control_is_available:
    action: REENABLE_THE_EXISTING_TASK_ONLY
    create_duplicate_task: prohibited

  when_task_is_missing_or_materially_mismatched:
    status: BLOCKED_GALAX_AUTO_UPLOAD_TASK_MISSING_OR_MISMATCHED
    silent_replacement: prohibited

  when_automation_control_is_unavailable:
    status: BLOCKED_AUTOMATION_CONTROL_UNAVAILABLE
    claim_scheduler_verified: prohibited
```

A new chat must never claim that unattended three-hour execution is active merely because the repository contains a standing authorization. It must separately verify the actual scheduler state.

## 3. Meaning of nonstop cursor

`Nonstop cursor` does not mean a second-by-second background process. It means two coordinated controls:

1. During every active Galax conversation, each new material owner instruction, ChatGPT decision, Cline result, permission gate, save, validation, failure, blocker, correction, commit, push, or remote-review result is recorded immediately as a structured event.
2. Every three hours, the enabled scheduler consolidates all verified unprocessed events into one interval-complete Length Problem checkpoint even when the technical task remains incomplete.

No explicit `update length problem` command is required from the Human Owner.

## 4. Mandatory material-event record

After every material Galax task outcome, the active chat must append one concise event to the Draft PR #10 continuity channel or another exact repository-backed continuity surface authorized by the live rules.

```yaml
GALAX_TURN_EVENT_V1:
  event_id:
  event_recorded_local_datetime:
  conversation_local_start_datetime:
  conversation_local_end_datetime:
  timezone_name: Asia/Manila
  timezone_offset: "+08:00"

  Human_Owner_instruction_summary:
  task_category:
  primary_skill_alias:
  dependency_skill_aliases: []
  active_assignment_id:
  conversation_chain_id:

  exact_target:
  action_attempted:
  last_completed_actual_action:
  current_unfinished_action:
  exact_stop_stage:

  result_status: SUCCESS | FAILED | BLOCKED | PENDING | CANCELLED
  exact_failure_or_blocker:
  evidence_class: REMOTE_PROVEN | HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE | HUMAN_OWNER_PROVIDED_AUTOMATION_EVIDENCE | REPORTED_LOCAL_NOT_REMOTE_PROOF

  resolves_event_id:
  next_exact_action:
  actions_not_to_repeat: []
  requires_new_Human_Owner_authorization:
```

Non-material greetings, duplicate questions with no state change, and ordinary wording corrections do not require a cursor event.

## 5. Strict status classification

```yaml
SUCCESS:
  use_only_when:
    - the_exact_authorized_objective_is_completed
    - the_required_evidence_exists
    - the_assigned_stop_condition_is_reached

FAILED:
  use_when:
    - an_attempted_objective_produced_an_incorrect_or_materially_defective_result
    - an_authorized_validation_failed

BLOCKED:
  use_when:
    - authority_access_evidence_permission_or_required_state_is_missing

PENDING:
  use_when:
    - waiting_for_Human_Owner_permission
    - waiting_for_Cline_output
    - preview_exists_but_is_not_saved
    - save_exists_but_validation_is_not_authorized_or_not_run
    - current_action_remains_unfinished

CANCELLED:
  use_when:
    - the_Human_Owner_explicitly_stops_replaces_or_cancels_the_task
```

Preparing a prompt, requesting permission, reading a file, showing an unsaved preview, or waiting for another action must not be falsely labeled `SUCCESS`.

## 6. Mandatory cursor watermarks

```yaml
GALAX_CONTINUITY_CURSOR_V1:
  latest_recorded_event_id:
  last_compacted_event_id:
  current_compaction_cutoff_event_id:
  last_checkpoint_file:
  last_checkpoint_local_datetime:
  next_checkpoint_due_local_datetime:

  active_conversation_chain_id:
  active_assignment_id:
  exact_target:
  current_stage:
  last_completed_actual_action:
  current_unfinished_action:
  exact_next_action:

  unresolved_event_ids: []
  resolved_event_ids_since_last_checkpoint: []
  events_waiting_for_next_compaction: []

  last_verified_continuity_branch_head:
  last_verified_router_sha:
  last_verified_Skill_5_sha:
  scheduler_task_id: 6a6e9ac862d08191860174abdc0ffa71
  scheduler_enabled_verified_at:
```

The cursor must not be advanced based on a draft, guess, failed write, or unverified commit.

## 7. Exact three-hour semi-complete compaction

At each three-hour run:

```text
verify repository, continuity branch, PR #10, standing authorization, and latest checkpoint
→ verify the existing scheduler task and exact Asia/Manila time
→ read last_compacted_event_id
→ freeze latest_recorded_event_id as current_compaction_cutoff_event_id
→ continue accepting newer events without pausing the cursor
→ fetch every unprocessed event after last_compacted_event_id through the cutoff
→ validate timestamps, sequence, evidence classes, duplicates, gaps, assignments, and conversation-chain relationships
→ connect FAILED or BLOCKED events to later verified resolving events
→ determine the latest unresolved active technical conversation chain
→ create one COMPLETE_FOR_INTERVAL Length Problem checkpoint
→ preserve the technical task as INCOMPLETE, PENDING, FAILED, or BLOCKED when that is the factual state
→ commit the checkpoint to docs/new-chat-continuity-2026-07-27
→ verify the remote commit and PR #10 head
→ only then advance last_compacted_event_id to the cutoff
→ leave events after the cutoff for the next cycle
```

```yaml
three_hour_checkpoint_contract:
  checkpoint_record_status: COMPLETE_FOR_INTERVAL
  technical_task_status: COMPLETE | INCOMPLETE | PENDING | FAILED | BLOCKED | CANCELLED
  every_unprocessed_event_through_cutoff_accounted_for: required
  exact_active_conversation_chain_identified: required
  exact_resume_point_identified: required
  historical_failures_preserved: required
  duplicate_events_prohibited: true
  cursor_advance_before_remote_verification: prohibited
```

If the technical work is unfinished, the checkpoint is still successful only when it completely records the interval and exact continuation boundary.

## 8. Failure and resolution preservation

A failed or blocked event must never be deleted from history.

When a later verified event resolves it:

```yaml
resolution_behavior:
  historical_event_status: RESOLVED
  resolved_by_event_id: required
  resolution_local_datetime: required
  remove_from_active_blockers: true
  remove_from_current_pending_work_when_no_longer_pending: true
  delete_historical_failure: false
```

If compaction, event validation, checkpoint write, commit, scheduler verification, or remote verification fails:

```yaml
compaction_failure_behavior:
  last_compacted_event_id: UNCHANGED
  current_unprocessed_events: PRESERVED
  events_deleted: false
  cursor_reset: prohibited
  status: BLOCKED_CONTINUITY_AUTO_UPLOAD
```

## 9. Mandatory continuation selection

The next chat must not blindly continue the latest message. It must continue the latest unresolved active technical chain unless the Human Owner explicitly pauses, cancels, replaces, or changes it.

```yaml
GALAX_CONTINUATION_PRIORITY_V1:
  priority_order:
    - Human_Owner_explicitly_selected_assignment
    - latest_unresolved_active_assignment
    - exact_pending_permission_preview_save_validation_commit_or_push_gate
    - latest_factually_blocked_assignment
    - newest_task_only_when_no_prior_active_task_remains
```

Every interval checkpoint must include:

```yaml
GALAX_EXACT_CONTINUATION_POINTER_V1:
  active_conversation_chain_id:
  active_assignment_id:
  active_target:
  current_stage:
  last_verified_success:
  latest_failure_or_blocker:
  failure_resolved: true | false
  resolved_by_event_id:
  current_unfinished_action:
  current_waiting_state:
  Human_Owner_already_authorized: []
  still_requires_Human_Owner_authorization: []
  exact_next_action:
  exact_next_action_owner: ChatGPT | Cline | Human_Owner | AUTOMATION
  exact_allowed_scope:
  exact_prohibited_scope:
  resume_from_event_id:
  do_not_resume_before_event_id:
  stop_condition_for_next_action:
```

## 10. Required new-chat execution receipt

Before continuing technical work, every new chat must return or internally establish:

```yaml
GALAX_NEW_CHAT_AUTO_CONTINUITY_EXECUTION_V1:
  latest_checkpoint_read:
  latest_checkpoint_remote_verified:
  continuity_branch:
  continuity_PR:
  continuity_PR_open_and_draft:

  scheduler_task_id: 6a6e9ac862d08191860174abdc0ffa71
  scheduler_access_available:
  scheduler_enabled:
  scheduler_schedule_verified:
  scheduler_duplicate_detected: false

  cursor_latest_recorded_event_id:
  cursor_last_compacted_event_id:
  events_waiting_for_compaction: []
  active_conversation_chain_id:
  active_assignment_id:
  exact_resume_point_verified:
  exact_next_action:

  automation_or_cursor_blockers: []
  safe_to_continue:
  status: PASS | BLOCKED
```

`safe_to_continue` remains false when the scheduler state is unverified, the latest checkpoint is missing, cursor boundaries conflict, an event gap exists, the active conversation chain is ambiguous, or the exact resume point cannot be proven.

## 11. Current factual scheduler evidence

```yaml
HUMAN_OWNER_PROVIDED_AUTOMATION_EVIDENCE:
  verified_at_local_datetime: 2026-08-05T00:10:49+08:00
  task_id: 6a6e9ac862d08191860174abdc0ffa71
  title: Galax Auto-Upload
  is_enabled: true
  timing_mode: exact_schedule
  schedule_verified: EVERY_3_HOURS_FROM_2026_08_05T02_57_00_ASIA_MANILA
```

This evidence proves the scheduler was enabled at the recorded time. Every later new chat must re-verify its current state rather than assuming it remains enabled forever.

## 12. Scope boundaries

This mandatory continuity rule authorizes only continuity recording, scheduler verification or re-enabling of the exact existing task, interval checkpoint creation, and remote verification on the continuity branch.

It does not authorize:

```yaml
not_authorized:
  - create_duplicate_Galax_scheduler
  - modify_ChatGPT_router
  - modify_Skill_5
  - modify_Cline
  - source_or_runtime_change
  - test_change_or_execution
  - dependency_change
  - workflow_or_secret_change
  - implementation_branch_commit_or_push
  - modify_LOCKED_ACCEPTED_work
  - merge
  - deployment
  - automatic_continuation_into_an_unapproved_technical_action
```

## 13. Current exact technical resume boundary

```yaml
continuity_documentation_action: COMPLETED_BY_THIS_CHECKPOINT
current_unresolved_technical_chain: SECTION_4_1_NO_BYPASS_CORRECTION_PREVIEW_RETRY
current_unresolved_target: .clinerules/00-galax-router-and-execution.md
current_unresolved_stage: SHORT_FORMAT_PREVIEW_RETRY_NOT_AUTHORIZED
last_completed_actual_action: mandatory_new_chat_auto_continuity_rule_recorded_in_Length_Problem_Volume_28
exact_next_technical_action: wait_for_separate_Human_Owner_authorization_before_preparing_or_running_the_short_format_preview_retry
technical_action_automatically_authorized_by_this_checkpoint: false
```

The automatic continuity system must preserve this unresolved technical chain but must not execute the technical correction without separate Human Owner authorization.
