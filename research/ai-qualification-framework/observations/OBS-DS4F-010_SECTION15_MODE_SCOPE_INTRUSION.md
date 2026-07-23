# OBS-DS4F-010 — Section 15 mode and scope intrusion

```yaml
profile_id: CLINE-DS4F-XHIGH-001
short_name: DS4F-XH
task_freshness: FRESH
requested_mode: PLAN
actual_mode: ACT
requested_action: read only Section 15 from its heading through end of file and return SECTION_15_CURRENT_BLOCK_V1
immediate_instruction_pickup: PARTIAL
selected_tools:
  - read_file_on_6_files
  - pending_terminal_command
tool_selection_compliance: FAIL
anchor_compliance: FAIL
scope_compliance: FAIL
old_task_memory_intrusion: CONFIRMED
semantic_content_accuracy: FAIL
patch_serialization_accuracy: NOT_APPLICABLE
stop_condition_compliance: FAIL
first_failure_stage: T0
review_decision: Reject
repository_change_saved: false
commands_run: []
evidence_summary: The task opened in Act Mode despite the requested Plan Mode. Cline invoked the repository startup/governance workflow, read README.md, CODE_RED.md, three planning documents, and a prompt pack, then requested a git branch/HEAD/status command. It did not return the requested literal Section 15 block and did not remain within read-only Section 15 scope.
reasoning_pattern_observed:
  - mode mismatch detected but not treated as a hard stop
  - governance startup memory overrode the narrow inspection request
  - broad repository bootstrapping occurred before target-section extraction
  - unauthorized command proposal followed the broad read
remedy_selected:
  - reject the command
  - close the contaminated Act task
  - create a genuinely fresh Plan task
  - place a hard mode-mismatch stop at the top of the next prompt
  - forbid reading README, AGENTS, plans, prompts, or any file other than CODE_RED.md
```

## New DS4F-XH control rule

```yaml
section_read_only_inspection:
  required_mode: PLAN
  on_actual_mode_not_plan: return BLOCKED_MODE_MISMATCH without reading files
  allowed_files:
    - docs/operations/CODE_RED.md
  maximum_file_reads: 1
  terminal_command_proposal_allowed: false
  repository_startup_workflow_allowed: false
```
