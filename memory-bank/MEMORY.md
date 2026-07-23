# Galax AI — Cline Qualification Memory

**Status:** `ACTIVE_OPERATIONAL_MEMORY`  
**Last updated:** `2026-07-23`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Branch:** `agent/agent-01-tool-inspection`

This file stores the current observable Cline qualification state. It is not a transcript and does not contain private chain-of-thought.

## Current profile

```yaml
profile_id: CLINE-DS4F-XHIGH-001
short_name: DS4F-XH
provider_model: deepseek-v4-flash
reasoning_setting: xhigh
mode: ACT
```

## Current method

```yaml
method_id: EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT
method_key: DS4F-XH + XHIGH + ACT + EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT + RESEARCH_FIXTURE
status: WORKING_OBSERVED_PROVISIONAL
validated_default: false
```

## Owner-approved counting rule

```yaml
qualification_target: 10_clean_full_method_PASS_results
counting_model: cumulative
current_clean_PASS_count: 3/10
PASS_effect: add_1
FAIL_effect: keep_current_count_and_record_failure
NO_SCORE_effect: keep_current_count
reset_to_zero: prohibited
```

The old rule requiring 10 consecutive PASS results and resetting to zero after a model failure is superseded.

## Confirmed scored runs

```yaml
ACT_002:
  result: PASS
  counter_after: 1/10

ACT_004:
  result: PASS
  counter_after: 2/10

ACT_005:
  result: PASS
  counter_after: 3/10
```

## ACT 006 history

```yaml
ACT_006:
  status: ABANDONED_HUMAN_ERROR
  result: NO_SCORE
  model_failure: false
  counter_before: 3/10
  counter_after: 3/10
```

Related trials preserved as evidence:

```yaml
initial_incomplete_capture:
  classification: HUMAN_ERROR
  score_effect: NO_SCORE

fixture_path_already_existed:
  classification: SETUP_COLLISION
  score_effect: NO_SCORE
  file_modified: false

close_existing_file_message:
  classification: HUMAN_AMBIGUITY
  score_effect: NO_SCORE
  file_deleted: false

real_world_prompt_terminal_proposal:
  classification: PROMPT_AND_TOOL_STARTING_POINT_REVIEW_REQUIRED
  command_executed: false
  score_effect: NO_SCORE
```

No ACT 006 trial has incremented or reduced the clean PASS count.

## Lessons from the latest trials

1. A fresh Cline task has no reliable knowledge of prior task instructions.
2. Every prompt must be self-contained.
3. The prompt must name the exact repository root, target path, first action, and permitted tool class.
4. `Check whether the file exists` is not precise enough when tool choice is being tested.
5. The prompt must say to use the native file read/existence tool and must prohibit terminal fallback.
6. When the native file tool is unavailable, the model must stop with `BLOCKED_NATIVE_FILE_TOOL_REQUIRED`.
7. Never delete an old fixture merely to reuse its name; use a unique target path.
8. Human mistakes, setup collisions, incomplete logs, platform problems, ambiguous events, and model failures do not reduce accumulated PASS credit under the new owner rule.
9. Failures remain recorded because they are evidence for prompt and model improvement.

## Required prompt state machine

```text
fresh task with zero prior knowledge
→ exact native file existence/read action
→ exact fixture creation proposal when absent
→ human Save
→ WAITING_FOR_CONTINUE_SUBTASK_1
→ CONTINUE_SUBTASK_1
→ one exact patch
→ human Save
→ WAITING_FOR_CONTINUE_SUBTASK_2
→ CONTINUE_SUBTASK_2
→ one exact patch
→ human Save
→ WAITING_FOR_CONTINUE_SUBTASK_3
→ CONTINUE_SUBTASK_3
→ one exact patch
→ human Save
→ WAITING_FOR_FINAL_VERIFICATION
→ RUN_FINAL_VERIFICATION
→ one final authorized read
→ structured receipt
→ permanent stop
```

## Current exact next action

```yaml
next_action: create_and_review_a_new_self_contained_ACT_006_prompt
counter_before_run: 3/10
target_after_clean_PASS: 4/10
prompt_must_be_owner_approved_before_running: true
```

## Files controlling this workflow

```text
.clinerules/00-galax-memory.md
memory-bank/MEMORY.md
docs/operations/CODE_RED_CLINE_QUALIFICATION_CHECKPOINT_2026-07-23.md
research/ai-qualification-framework/CURRENT_CLINE_WORKFLOW_HANDOFF.md
research/ai-qualification-framework/WORKING_METHOD_EXPLICIT_GATE_SEQUENTIAL_EXACT_REPLACEMENT.md
research/ai-qualification-framework/METHOD_VALIDATION_10_CONSECUTIVE_PASS_RULE.md
research/ai-qualification-framework/NEW_TASK_ZERO_KNOWLEDGE_PROMPT_REQUIREMENTS.md
```

## Separate implementation boundary

```yaml
Galax_application_implementation_authorized_by_this_memory: false
safe_to_continue_implementation: false
local_state_recovery_required: true
commands_tests_git_for_qualification: prohibited_without_separate_authorization
Agents_02_to_15: prohibited
push_merge_deploy: prohibited
```
