# Method Validation — 10 Consecutive PASS Rule

**Status:** ACTIVE_CANONICAL_QUALIFICATION_RULE  
**Applies to:** every Cline model profile, reasoning level, task mode, and execution method

## Core rule

A method becomes the default approved method only after it produces **10 consecutive clean PASS observations** under the same controlled conditions.

```yaml
METHOD_VALIDATION_10_CONSECUTIVE_PASS_V1:
  required_consecutive_passes: 10
  sequence_must_be_unbroken: true
  adopt_method_after_pass_number: 10
  any_model_caused_failure_resets_counter_to: 0
  user_setup_error_resets_counter: false
  infrastructure_or_UI_failure_resets_counter: false
  ambiguous_root_cause:
    action: do_not_increment
    reset_counter: false
  mixed_methods_can_share_counter: false
  mixed_models_can_share_counter: false
  mixed_reasoning_levels_can_share_counter: false
  mixed_modes_can_share_counter: false
```

## What counts as one clean PASS

One observation increments the counter only when all applicable checks pass:

```yaml
clean_pass_requirements:
  correct_model_profile: true
  correct_reasoning_setting: true
  correct_task_mode: true
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
  reviewer_decision: Save_OR_No_Action
```

A locally saved edit counts only after the user confirms Save or a valid post-save readback confirms the exact saved content.

## Counter separation

Each method has its own independent counter key:

```text
MODEL_PROFILE + REASONING_LEVEL + MODE + METHOD_ID + TASK_CLASS
```

Examples:

```text
DS4F-XH + ACT + SINGLE_LINE_EXACT_REPLACEMENT + MARKDOWN_EMBEDDED_TEXT
DS4F-XH + PLAN + ONE_SECTION_READ_ONLY_INSPECTION + MARKDOWN_DOCUMENT
STEP37F-H + PLAN + EXACT_ANCHOR_RECEIPT + MARKDOWN_DOCUMENT
```

Success from one key must never be transferred to another key.

## Failure and non-model event handling

```yaml
model_caused_failure:
  examples:
    - wrong tool
    - scope expansion
    - semantic error
    - malformed patch
    - unauthorized command
    - failure to stop
  counter_action: RESET_TO_ZERO

user_setup_error:
  examples:
    - reused old task when a fresh task was required
    - selected Act instead of Plan
    - pasted the wrong prompt
    - manually changed the approved content
  counter_action: NO_INCREMENT_NO_RESET
  model_fault: NOT_CONFIRMED

platform_or_UI_failure:
  examples:
    - blank tool card with no evidence that the model omitted the payload
    - provider outage
    - token exhaustion
  counter_action: NO_INCREMENT_NO_RESET

ambiguous_event:
  counter_action: NO_INCREMENT_NO_RESET
  required_label: ROOT_CAUSE_UNRESOLVED
```

## Promotion states

```yaml
0_to_2_passes: EXPERIMENTAL
3_to_6_passes: PROVISIONAL
7_to_9_passes: NEAR_VALIDATED
10_consecutive_passes: VALIDATED_DEFAULT_METHOD
```

After validation, the exact successful prompt structure and execution sequence become the preferred default for that method key.

## Post-validation monitoring

Validation does not make a method permanently infallible.

```yaml
validated_method_failure:
  retain_historical_validation: true
  active_status: SUSPENDED_FOR_REVIEW
  new_consecutive_pass_counter: 0
  automatic_use: false
  required_action: diagnose_and_revalidate
```

## Recording requirement

Every observation must record:

```yaml
method_id:
method_counter_key:
result: PASS | FAIL | NO_SCORE
root_cause: MODEL | USER_SETUP | PLATFORM | AMBIGUOUS
consecutive_pass_count_before:
consecutive_pass_count_after:
method_status_after:
```

The repository observation ledger and individual observation records are the evidence source. Issue or PR comments may mirror the result but are not the canonical qualification record.
