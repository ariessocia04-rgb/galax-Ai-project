# Compatibility Redirect — CODE RED and New-Chat Continuity Guide

**Status:** `COMPATIBILITY_REDIRECT`  
**Previous role:** canonical conversation-length continuity protocol  
**Canonical protocol:** `docs/operations/CODE_RED.md`  
**Current exact handoff guide:** `docs/operations/GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md`  
**Latest exact checkpoint:** `docs/operations/checkpoints/GALAX_LENGTH_PROBLEM_TIMESTAMP_AND_RESUME_VOLUME_10_2026-08-01.md`  
**Previous detailed checkpoint:** `docs/operations/checkpoints/GALAX_LENGTH_PROBLEM_ACHIEVEMENTS_AND_CURRENT_STATUS_VOLUME_9_2026-08-01.md`  
**Current achievements from start:** `docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md`  
**Do not use this file alone as the source of truth.**

The owner renamed the Galax continuity and recovery protocol to:

```text
CODE RED
```

Every repository-aware AI or human that reaches this file must immediately read, in this order:

```text
README.md
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ docs/operations/GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md
→ docs/operations/checkpoints/GALAX_LENGTH_PROBLEM_ACHIEVEMENTS_AND_CURRENT_STATUS_VOLUME_9_2026-08-01.md
→ docs/operations/checkpoints/GALAX_LENGTH_PROBLEM_TIMESTAMP_AND_RESUME_VOLUME_10_2026-08-01.md
→ docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
→ the active assignment, pull requests, issues, branch heads, tests, and newest continuity evidence
```

`CODE_RED.md` defines the canonical recovery protocol. The dated continuity guide records the earlier material history. The latest numbered volume records the newest exact stop point, date, time, minute, and safe resume boundary. The achievements file records completed work from project start to the current verified stop. Live GitHub and local evidence must still be verified because no checkpoint grants authority or freezes future branch movement.

Legacy and current trigger phrases all route to this procedure:

```text
CODE RED
length chat problem
chat length problem
conversation length problem
continue exact Galax flow
operation length problem solve
operatiion length problem solve
backread the repo because the chat is full
new chat continuation
where did we stop
resume the latest Galax work
```

## Mandatory response to a length problem

On any trigger above, the new chat must:

```text
stop relying on remembered chat fragments
→ verify repository access
→ verify the current research, implementation, plan, continuity, and active work branch HEAD SHAs
→ read CODE RED completely
→ read the current new-chat continuity guide completely
→ read Volume 9 completely when detailed prior state is needed
→ read Volume 10 completely for the exact minute-level stop and resume boundary
→ read the current achievements-from-start record completely
→ inspect active Draft PRs and assignment issues
→ separate remote-proven facts from Human Owner-provided local evidence
→ reconstruct completed, rejected, corrected, active, blocked, locked, and pending work
→ determine the exact selected work track, stop timestamp, resume timestamp, and next safe action
→ return GALAX_NEW_CHAT_CONTINUATION_RECEIPT_V1
→ continue only when repository evidence and Human Owner authorization agree
```

Do not ask the owner to repeat repository history when repository access exists. Do not create another plan merely because the conversation changed. Do not repeat completed or locked work.

## Mandatory date, time, and minute rule

Every new length-problem, chat-length, new-chat continuation, or checkpoint upload must record an exact local coverage boundary.

Required timezone:

```yaml
timezone_name: Asia/Manila
timezone_offset: "+08:00"
```

Required fields:

```yaml
previous_checkpoint_file:
previous_checkpoint_stop_local_datetime:
coverage_start_local_datetime:
coverage_start_date_local:
coverage_start_time_local_24h:
coverage_start_minute_local:
coverage_end_local_datetime:
coverage_end_date_local:
coverage_end_time_local_24h:
coverage_end_minute_local:
exact_stop_point_local_datetime:
next_upload_resume_after_local_datetime:
last_completed_actual_action:
exact_safe_resume_action:
actions_that_must_not_be_repeated: []
```

Formatting rules:

1. Date must use `YYYY-MM-DD`.
2. Time must use 24-hour `HH:MM` format.
3. Minute must also be recorded separately as an integer from `0` to `59`.
4. Full timestamps must use ISO 8601 with the Philippine offset, for example `2026-08-01T02:51:00+08:00`.
5. The next upload must resume only after the previous checkpoint's `next_upload_resume_after_local_datetime`.
6. Events already covered at or before the previous stop timestamp must not be repeated.
7. When the exact minute is unavailable, use `UNKNOWN_EXACT_MINUTE` and do not claim an exact resume point.
8. A timestamp records continuity only. It grants no edit, test, commit, push, merge, deployment, reviewer-trigger, or work-track authority.

## Current multi-track stop point

The latest checkpoint separates independent work tracks:

```yaml
Track_A_Phase_2B_local_contract_tests:
  exact_stop_point: AFTER_test_completion_requires_pass_preflight_PASS_AND_LOCKED
  full_suite_post_fix: NOT_RUN
  remote_publication_proven: false

Track_B_Cline_prompt_method_research:
  method: EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT
  clean_PASS_count: 3_of_10
  status: PROVISIONAL_NOT_VALIDATED_DEFAULT

Track_C_new_chat_continuity:
  prompting_control_replacement_commit: 1562b04cc6d4a439c417d878e07a9fb119cc1c3d
  achievement_update_commit: 9fe328fd96be78af7c2382546613551a4da80222
  latest_volume_file: docs/operations/checkpoints/GALAX_LENGTH_PROBLEM_TIMESTAMP_AND_RESUME_VOLUME_10_2026-08-01.md
  latest_exact_stop_local_datetime: 2026-08-01T02:51:00+08:00
  next_upload_resume_after_local_datetime: 2026-08-01T02:51:00+08:00
  PR_10_state: OPEN_DRAFT_UNMERGED
```

A new chat must not confuse the Phase 2B local test-correction track, Cline prompting-method research, and continuity-documentation track.

## Owner standing checkpoint directive

When the owner explicitly indicates that the current conversation or task will stop, pause, continue later, move to a new chat, or has reached a conversation-length problem, the active AI must enter `SAVE_CURRENT_TASK_CHECKPOINT` mode before starting or resuming another assignment.

The checkpoint must record exact observable evidence without guessing:

```yaml
SAVE_CURRENT_TASK_CHECKPOINT_V1:
  recorded_at_utc:
  recorded_date_local:
  recorded_time_local_24h:
  recorded_minute_local:
  timezone_name: Asia/Manila
  timezone_offset: "+08:00"
  coverage_start_local_datetime:
  coverage_end_local_datetime:
  exact_stop_point_local_datetime:
  next_upload_resume_after_local_datetime:
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

1. Distinguish proposed, displayed, approved, executed, saved, committed, pushed, reviewed, and accepted.
2. Never treat a displayed patch as a saved edit.
3. Never treat an active issue as proof that its contributor started.
4. Never repeat an already completed, accepted, saved, or locked action.
5. Never restore or reuse rejected work.
6. Preserve the exact assignment ID, branch, starting SHA, and allowed scope.
7. Preserve the exact local date, hour, minute, timezone, coverage start, coverage end, stop point, and next resume boundary.
8. A continuity checkpoint grants no edit, validation, commit, push, merge, deployment, reviewer-trigger, or new-assignment authority.
9. Store the durable checkpoint in the active GitHub issue or PR when tracked-file mutation is not separately authorized.
10. Update CODE RED only through a separately authorized bounded repository change.
11. Resume only after the exact recorded stop timestamp and from the exact recorded safe action after verifying live repository state.

Capability boundary:

```yaml
silent_chat_close_event_available: false
background_inactivity_trigger_available: false
explicit_stop_or_length_message_trigger: required
controlled_stage_boundary_checkpoint: required
```

The AI cannot detect a silent browser close or user inactivity when no message is received. Checkpoint behavior therefore starts from an explicit owner message or a controlled stage reaching a human-approval boundary.

This redirect is retained because older repository documents, prompts, issues, and conversations may still reference the old path.

Do not delete it until:

```text
all inbound references are inventoried
→ every active reference is migrated to CODE RED, the current continuity guide, the latest timestamped volume, and the current achievement record
→ historical evidence is preserved
→ link and repository checks pass
→ the human owner explicitly authorizes removal
→ deletion is recorded in CODE RED
```
