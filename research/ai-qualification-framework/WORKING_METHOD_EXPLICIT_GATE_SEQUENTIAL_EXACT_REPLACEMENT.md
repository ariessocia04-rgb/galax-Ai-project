# Working Method — Explicit-Gate Sequential Exact Replacement

**Status:** `WORKING_OBSERVED`  
**Validation counter:** `1/10` consecutive clean full-method PASS results  
**Validated default:** `false`

## Method identity

```yaml
method_id: EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT
method_key: DS4F-XH + XHIGH + ACT + EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT + RESEARCH_FIXTURE
profile_id: CLINE-DS4F-XHIGH-001
provider_model: deepseek-v4-flash
reasoning_setting: xhigh
mode: ACT
```

## Proven scope

The method has one clean full-run PASS only for this controlled scope:

```yaml
fresh_isolated_task: required
authorized_files: 1
file_class: low-risk research fixture
logical_change_per_patch: 1
patch_shape: exact visible SEARCH/REPLACE block
maximum_pending_edits: 1
human_save_checkpoint: required
explicit_continue_token_between_subtasks: required
explicit_final_verification_token: required
automatic_retry: prohibited
full_file_fallback: prohibited
terminal_commands: prohibited
tests: prohibited
git_operations: prohibited
application_code: prohibited
parallel_execution: prohibited
```

## Required flow

1. Start a fresh isolated Cline task with the exact profile, reasoning, and Act mode.
2. Authorize one low-risk fixture file only.
3. Propose one exact logical-block patch and stop for human Save or Reject.
4. After Save, Cline must return only the exact waiting token.
5. The human sends the exact continuation token before the next subtask.
6. Repeat one subtask at a time. Save never authorizes automatic continuation.
7. After the final saved edit, Cline waits for the exact final-verification token.
8. Final verification reads the authorized fixture exactly once and returns a structured receipt.
9. The run counts only when every required field is correct and `overall_status: PASS`.

## Required review rules

```yaml
complete_visible_diff_required: true
exact_search_anchor_required: true
unrelated_content_allowed: false
additional_file_read_allowed: false
second_pending_edit_allowed: false
anchor_mismatch_action: stop_immediately
read_after_anchor_mismatch: prohibited
retry_after_anchor_mismatch: prohibited
human_checkpoint_bypass: prohibited
```

## First clean PASS evidence

```yaml
experiment_id: DS4F-XH_ACT_002
observation_id: OBS-DS4F-023
result: PASS
setup_saved: true
subtask_1_saved: true
subtask_2_saved: true
subtask_3_saved: true
all_explicit_gates_respected: true
maximum_simultaneous_pending_edits: 1
automatic_retries_performed: 0
unauthorized_files_read: []
unauthorized_files_changed: []
commands_run: []
tests_run: []
git_operations: []
all_exact_blocks_verified: true
overall_status: PASS
counter_after: 1/10
```

## Why the explicit gate is required

ACT 001 failed because Save was treated as permission to continue automatically. After an anchor mismatch, the model retried, reread the fixture repeatedly, and produced a full-file state instead of the required exact block patch. ACT 002 corrected this by requiring an exact continuation token after every Save and an exact final-verification token after the final edit.

## Promotion and reset rule

- Promote this method to `VALIDATED_DEFAULT_FOR_PROVEN_SCOPE` only after `10/10` consecutive clean full-method PASS results under the exact same method key.
- Any model-caused failure resets this method counter to `0/10`.
- User setup errors, platform errors, and ambiguous instructions neither increment nor reset the counter when clearly classified as non-model causes.
- Do not combine this counter with single-line, YAML-block, Plan-mode, different-model, different-reasoning, multiple-file, command, test, Git, application-code, or parallel-execution results.

## Current restrictions

This method is not validated for:

- application or production code;
- multiple files;
- simultaneous or parallel writers;
- autonomous continuation;
- terminal commands, tests, Ruff, pytest, or Git;
- architecture, schema, migration, security, deployment, or MCP changes;
- high-risk edits or imprecise natural-language transformations.

## Next qualification action

Run a fresh isolated repetition of the same complete method with a new dedicated research fixture. Keep the exact method key and controls unchanged. The next clean full-method PASS advances the counter to `2/10`. Do not run the ten-task ACT 003 stress test until this method reaches `10/10`.
