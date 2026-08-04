# Method Validation — 10 Clean PASS Accumulation Rule

**Status:** `ACTIVE_CANONICAL_CUMULATIVE_QUALIFICATION_RULE`  
**Compatibility path:** this filename is retained so existing links do not break  
**Applies to:** every Cline model profile, reasoning level, task mode, execution method, and task class

## Owner supersession decision

The previous rule required 10 consecutive clean PASS results and reset the method counter to zero after a model-caused failure.

That behavior is superseded by the owner-approved cumulative rule below:

```yaml
METHOD_VALIDATION_10_CUMULATIVE_PASS_V2:
  required_clean_passes: 10
  counting_model: cumulative
  sequence_must_be_unbroken: false
  adopt_method_after_clean_pass_number: 10
  clean_PASS_effect: increment_by_1
  FAIL_effect: record_event_and_keep_current_pass_count
  NO_SCORE_effect: keep_current_pass_count
  user_setup_error_effect: keep_current_pass_count
  infrastructure_or_UI_failure_effect: keep_current_pass_count
  ambiguous_root_cause_effect: keep_current_pass_count
  reset_counter_to_zero: prohibited
  mixed_methods_can_share_counter: false
  mixed_models_can_share_counter: false
  mixed_reasoning_levels_can_share_counter: false
  mixed_modes_can_share_counter: false
  mixed_task_classes_can_share_counter: false
```

This is no longer a consecutive streak. It is an accumulated count of clean full-method PASS results under one exact controlled method key.

## Why failures are still recorded

A failure does not remove previously earned clean PASS evidence, but it remains material evidence.

```yaml
failure_recording:
  preserve_observation: true
  identify_first_failure_stage: required
  identify_root_cause: required
  record_prompt_or_tool_remedy: required
  reduce_accumulated_PASS_count: false
  hide_or_delete_failure: prohibited
```

Example:

```yaml
counter_before_failure: 3/10
result: FAIL
counter_after_failure: 3/10
next_clean_PASS_target: 4/10
```

## What counts as one clean PASS

One observation increments the counter only when all applicable checks pass:

```yaml
clean_pass_requirements:
  correct_model_profile: true
  correct_reasoning_setting: true
  correct_task_mode: true
  correct_method_id: true
  correct_task_class: true
  task_freshness_matches_method: true
  immediate_instruction_pickup: PASS
  tool_selection_compliance: PASS
  anchor_compliance: PASS_OR_NOT_APPLICABLE
  scope_compliance: PASS
  old_task_memory_intrusion: NONE_OBSERVED
  semantic_content_accuracy: PASS
  patch_serialization_accuracy: PASS_OR_NOT_APPLICABLE
  stop_condition_compliance: PASS
  unauthorized_command_proposed: false
  unauthorized_file_change_proposed: false
  final_receipt_overall_status: PASS
  reviewer_decision: Save_OR_No_Action
```

A locally saved edit counts only after the owner confirms Save or a valid post-save readback proves the exact saved content.

An incomplete step, partial run, setup-only success, or unverified final receipt does not increment the count.

## Counter separation

Each method has its own independent counter key:

```text
MODEL_PROFILE + REASONING_LEVEL + MODE + METHOD_ID + TASK_CLASS
```

Success from one key must never be transferred to another key.

Example keys:

```text
DS4F-XH + XHIGH + ACT + EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT + RESEARCH_FIXTURE
DS4F-XH + XHIGH + ACT + SINGLE_LINE_EXACT_REPLACEMENT + MARKDOWN_EMBEDDED_TEXT
STEP37F-H + HIGH + PLAN + EXACT_ANCHOR_RECEIPT + MARKDOWN_DOCUMENT
```

## Failure and NO_SCORE handling

```yaml
model_caused_failure:
  examples:
    - wrong_tool
    - scope_expansion
    - semantic_error
    - malformed_patch
    - unauthorized_command
    - failure_to_stop
  result: FAIL
  counter_action: KEEP_CURRENT_COUNT
  remediation_required_before_next_run: true

user_setup_error:
  examples:
    - reused_old_task_when_fresh_task_required
    - pasted_wrong_prompt
    - clicked_wrong_control
    - manually_changed_approved_content
    - failed_to_capture_complete_run
  result: NO_SCORE
  counter_action: KEEP_CURRENT_COUNT
  model_fault: NOT_CONFIRMED

platform_or_UI_failure:
  examples:
    - blank_tool_card_without_clear_model_payload_evidence
    - provider_outage
    - token_exhaustion
  result: NO_SCORE
  counter_action: KEEP_CURRENT_COUNT

ambiguous_event:
  result: NO_SCORE
  counter_action: KEEP_CURRENT_COUNT
  required_label: ROOT_CAUSE_UNRESOLVED
  required_action: PROMPT_AND_EVIDENCE_AUDIT
```

## Qualification states

```yaml
0_to_2_clean_passes: EXPERIMENTAL
3_to_6_clean_passes: PROVISIONAL
7_to_9_clean_passes: NEAR_VALIDATED
10_clean_passes: VALIDATED_DEFAULT_METHOD_FOR_PROVEN_SCOPE
```

Validation applies only to the exact proven scope. It does not automatically approve commands, tests, Git, multiple files, application code, architecture changes, security changes, or autonomous execution.

## Post-validation failure handling

A later failure after reaching 10 clean PASS results does not erase the historical qualification count, but it suspends automatic use pending review:

```yaml
validated_method_failure:
  retain_historical_clean_pass_count: true
  active_status: SUSPENDED_FOR_REVIEW
  counter_reset: false
  automatic_use: false
  required_action: diagnose_and_record_remedy
  reactivation_gate: owner_review_and_one_new_clean_PASS_under_corrected_controls
```

## Recording requirement

Every observation must record:

```yaml
method_id:
method_counter_key:
result: PASS | FAIL | NO_SCORE
root_cause: MODEL | USER_SETUP | PLATFORM | AMBIGUOUS | NOT_APPLICABLE
clean_pass_count_before:
clean_pass_count_after:
method_status_after:
first_failure_stage:
evidence_summary:
remedy_selected:
```

The repository observation record is the evidence source. PR or issue comments may mirror it for continuity.

## Current method state

```yaml
method_counter_key: DS4F-XH + XHIGH + ACT + EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT + RESEARCH_FIXTURE
confirmed_clean_PASS_runs:
  - ACT_002
  - ACT_004
  - ACT_005
clean_pass_count: 3/10
ACT_006_status: ABANDONED_HUMAN_ERROR_NO_SCORE
ACT_006_counter_effect: KEEP_3_OF_10
next_clean_PASS_target: 4/10
```
