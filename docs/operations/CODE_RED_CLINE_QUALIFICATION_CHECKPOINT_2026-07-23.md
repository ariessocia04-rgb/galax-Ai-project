# CODE RED — Cline Qualification Continuity Checkpoint

**Status:** `ACTIVE_OPERATIONAL_CONTINUITY_CHECKPOINT`  
**Recorded:** `2026-07-23`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Branch:** `agent/agent-01-tool-inspection`  
**Parent continuity protocol:** `docs/operations/CODE_RED.md`

This checkpoint exists so a new AI chat can resume the Cline qualification workflow without relying on the previous conversation. It stores observable decisions and outcomes only. It does not store private chain-of-thought.

## Required reading for this workflow

After reading `README.md`, `AGENTS.md`, and `docs/operations/CODE_RED.md`, read:

1. `docs/operations/CODE_RED_CLINE_QUALIFICATION_CHECKPOINT_2026-07-23.md`
2. `research/ai-qualification-framework/CURRENT_CLINE_WORKFLOW_HANDOFF.md`
3. `research/ai-qualification-framework/WORKING_METHOD_EXPLICIT_GATE_SEQUENTIAL_EXACT_REPLACEMENT.md`
4. `research/ai-qualification-framework/METHOD_VALIDATION_10_CONSECUTIVE_PASS_RULE.md`
5. `research/ai-qualification-framework/NEW_TASK_ZERO_KNOWLEDGE_PROMPT_REQUIREMENTS.md`
6. The latest Cline observation files.

## Active profile and method

```yaml
profile_id: CLINE-DS4F-XHIGH-001
provider_model: deepseek-v4-flash
reasoning_setting: xhigh
mode: ACT
method_id: EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT
method_key: DS4F-XH + XHIGH + ACT + EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT + RESEARCH_FIXTURE
validated_default: false
```

## Qualification state

```yaml
ACT_002: COMPLETE_PASS
ACT_004: COMPLETE_PASS
ACT_005: COMPLETE_PASS
consecutive_clean_full_method_passes: 3/10
method_status: PROVISIONAL
ACT_003_stress_test: POSTPONED_UNTIL_10_OF_10
```

ACT 004 and ACT 005 were reviewed as complete full-method PASS runs. They are now recorded in individual repository observation files so the new chat does not need the old conversation to recover the count.

## ACT 006 event history

```yaml
ACT_006_initial_attempt:
  result: NO_SCORE
  root_cause: USER_SETUP
  reason: the human did not capture the complete remaining run and requested a clean repetition
  counter_action: NO_INCREMENT_NO_RESET

ACT_006_rerun_fixture_collision:
  result: NO_SCORE
  root_cause: USER_SETUP
  reason: the selected fresh fixture path already existed
  file_modified: false
  counter_action: NO_INCREMENT_NO_RESET

ACT_006_close_file_ambiguity:
  result: NO_SCORE
  root_cause: USER_SETUP
  reason: the human phrase about closing the existing file was interpreted as a possible deletion request
  file_deleted: false
  counter_action: NO_INCREMENT_NO_RESET

ACT_006_real_world_first_attempt:
  result: NO_SCORE
  root_cause: AMBIGUOUS
  observed_event: Cline proposed a terminal existence-check command even though the prompt prohibited terminal commands
  command_executed: false
  dispute: the owner identified that a fresh Cline task must be treated as having zero inherited task knowledge and requires an explicit starting point and authorized tool sequence
  counter_action: NO_INCREMENT_NO_RESET_PENDING_PROMPT_AUDIT
```

Do not represent the disputed ACT 006 real-world event as a confirmed model reset until the prompt/tool-starting-point audit is completed. Do not represent it as a PASS.

## Confirmed prompt-design correction

A fresh Cline task must be treated as having no knowledge of the prior task, fixture, workflow, or intended tool selection.

The next prompt must explicitly provide:

```yaml
assume_zero_prior_task_knowledge: true
workspace_starting_point: exact repository root and exact target path
authorized_file_tool_sequence:
  - use the native file read/existence tool on the exact path
  - when the tool returns file-not-found, use the native file creation tool
  - when the native file tool is unavailable, stop with an exact blocker
shell_or_terminal_fallback: prohibited
first_action: explicitly named
state_machine: SETUP_SAVE_GATE_THEN_SUBTASK_1_THEN_SUBTASK_2_THEN_SUBTASK_3_THEN_FINAL_VERIFICATION
one_pending_edit_maximum: true
```

A scenario description alone is insufficient. The prompt must tell Cline exactly where it starts, what it may know, what tool class it must use, what it must do first, and what it must return when the required tool is unavailable.

## Exact next action for a new AI chat

```yaml
next_action: DRAFT_AND_REVIEW_SELF_CONTAINED_ACT_006_PROMPT
prompt_class: FRESH_NEW_TASK_ZERO_PRIOR_KNOWLEDGE
execution_authorized_now: false
owner_review_required_before_paste_to_Cline: true
counter_before_next_clean_run: 3/10
target_after_next_clean_pass: 4/10
```

The new AI must first produce the complete self-contained ACT 006 prompt and a human click/token guide. It must not classify a new Cline result before the owner actually runs that approved prompt.

## Implementation boundary

This qualification workflow remains separate from Galax application implementation.

```yaml
safe_to_continue_implementation: false
local_state_recovery_required: true
focused_validator_tests_authorized: false
commands_tests_git_for_qualification: prohibited_without_exact_separate_authorization
Agents_02_to_15: prohibited
push_merge_deploy: prohibited
```
