# OBS-DS4F-010 — Section 15 task-reuse and mode mismatch

> Correction: the user confirmed that the Section 15 prompt was pasted into an older Act task. This event must not be treated as confirmed DeepSeek memory intrusion.

```yaml
profile_id: CLINE-DS4F-XHIGH-001
short_name: DS4F-XH
task_freshness: CONTAMINATED_BY_USER_TASK_REUSE
requested_mode_in_prompt: PLAN
actual_mode: ACT
requested_action: read only Section 15 from its heading through end of file and return SECTION_15_CURRENT_BLOCK_V1
immediate_instruction_pickup: PARTIAL
selected_tools:
  - read_file_on_6_files
  - pending_terminal_command
tool_selection_compliance: FAIL
anchor_compliance: FAIL
scope_compliance: FAIL
old_task_memory_intrusion: NOT_DETERMINABLE
model_fault_confirmed: false
user_setup_error_confirmed: true
semantic_content_accuracy: FAIL
patch_serialization_accuracy: NOT_APPLICABLE
stop_condition_compliance: FAIL
first_failure_stage: T0
review_decision: Reject
repository_change_saved: false
commands_run: []
root_cause: The Section 15 Plan-mode prompt was pasted into an existing Act-mode task instead of a genuinely new Plan task.
evidence_summary: Cline was already operating inside an older Act task. It detected the Plan-versus-Act discrepancy, then followed the existing task's repository startup/governance context, read six files, and proposed a git branch/HEAD/status command. Because the task was reused, this output cannot be used as clean evidence of DeepSeek behavior in a fresh Plan task.
reasoning_pattern_observed:
  - mixed old-task context and new prompt were simultaneously present
  - actual task mode remained Act despite Plan wording in the pasted prompt
  - broad repository bootstrapping followed the older task context
  - unauthorized command proposal remained pending and was rejected
remedy_selected:
  - reject the pending command
  - do not count this event against the DS4F-XH validation profile
  - close the reused Act task
  - create a genuinely new Plan task before repeating Section 15 inspection
```

## Corrected control rule

```yaml
section_read_only_inspection:
  user_must_create_new_task: true
  required_mode: PLAN
  verify_mode_before_paste: true
  allowed_files:
    - docs/operations/CODE_RED.md
  maximum_file_reads: 1
  terminal_command_proposal_allowed: false
  repository_startup_workflow_allowed: false
```
