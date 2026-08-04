# Working Method — Explicit-Gate Sequential Exact Replacement

**Status:** `WORKING_OBSERVED_PROVISIONAL`  
**Clean PASS count:** `3/10` accumulated clean full-method PASS results  
**Validated default:** `false`

## Method identity

```yaml
method_id: EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT
method_key: DS4F-XH + XHIGH + ACT + EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT + RESEARCH_FIXTURE
profile_id: CLINE-DS4F-XHIGH-001
provider_model: deepseek-v4-flash
reasoning_setting: xhigh
mode: ACT
counting_model: cumulative_clean_PASS_count
method_status: PROVISIONAL
```

## Proven scope

The method has three clean full-run PASS observations only for this controlled scope:

```yaml
fresh_isolated_task: required
assume_zero_prior_task_knowledge: required
authorized_files: 1
file_class: low-risk_research_fixture
logical_change_per_patch: 1
patch_shape: exact_visible_SEARCH_REPLACE_block
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

## Persistent Cline memory

Cline automatically loads:

```text
.clinerules/00-galax-memory.md
```

That rule requires Cline to read:

```text
memory-bank/MEMORY.md
```

before continuing Cline qualification work. The memory files do not replace the canonical CODE RED records or exact active assignment.

## Required new-task starting contract

Every fresh Cline qualification task must follow:

`research/ai-qualification-framework/NEW_TASK_ZERO_KNOWLEDGE_PROMPT_REQUIREMENTS.md`

A new task must be treated as having zero inherited task knowledge. The prompt must explicitly name:

- repository and workspace starting point;
- exact authorized target file;
- exact first action;
- exact permitted native file tool sequence;
- file-exists branch;
- file-not-found branch;
- exact blocker when the native file tool is unavailable;
- prohibition on terminal or shell fallback;
- complete Save, wait, continuation, and verification state machine.

A scenario description alone is insufficient.

## Required flow

1. Start a fresh isolated Cline task with the exact profile, reasoning, and Act mode.
2. State that the task has zero prior task knowledge.
3. Authorize one low-risk research fixture only.
4. Use the native file read/existence tool on the exact target path.
5. When the file is absent, propose the exact fixture creation and stop for human Save or Reject.
6. After Save, return the exact waiting token and do not continue.
7. Continue only after the human sends the exact continuation token.
8. Read the authorized fixture exactly once for that subtask.
9. Show one complete exact logical-block SEARCH/REPLACE patch and stop for Save or Reject.
10. Repeat one subtask at a time. Save never authorizes automatic continuation.
11. After the final saved patch, wait for the exact final-verification token.
12. Read the authorized fixture exactly once and return the structured final receipt.
13. Stop permanently.

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
shell_existence_check: prohibited
native_file_tool_unavailable_action: BLOCKED_NATIVE_FILE_TOOL_REQUIRED
```

## Confirmed clean PASS evidence

### PASS 1 — ACT 002

```yaml
experiment_id: DS4F-XH_ACT_002
observation_id: OBS-DS4F-023
result: PASS
clean_pass_count_before: 0/10
clean_pass_count_after: 1/10
```

ACT 002 proved that exact continuation tokens prevent Save from being interpreted as permission to continue automatically.

### PASS 2 — ACT 004

```yaml
experiment_id: DS4F-XH_ACT_004
observation_id: OBS-DS4F-026
result: PASS
clean_pass_count_before: 1/10
clean_pass_count_after: 2/10
```

ACT 004 preserved every setup, Save, waiting, continuation, patch, and final-verification gate with no retry, command, unrelated file, or Git action.

### PASS 3 — ACT 005

```yaml
experiment_id: DS4F-XH_ACT_005
observation_id: OBS-DS4F-027
result: PASS
clean_pass_count_before: 2/10
clean_pass_count_after: 3/10
```

ACT 005 repeated the same method key and completed the full sequence with a clean PASS receipt.

## ACT 006 state

```yaml
experiment_id: DS4F-XH_ACT_006
status: ABANDONED_HUMAN_ERROR
result: NO_SCORE
model_failure: false
clean_pass_count_before: 3/10
clean_pass_count_after: 3/10
```

Related ACT 006 setup collisions, incomplete capture, close-file ambiguity, and the first real-world prompt/tool-starting-point trial remain preserved as evidence. None incremented or reduced the clean PASS count.

## Owner-approved cumulative counting rule

The old consecutive-reset rule is superseded.

```yaml
required_clean_passes: 10
counting_model: cumulative
PASS_effect: increment_by_1
FAIL_effect: keep_current_count_and_record_failure
NO_SCORE_effect: keep_current_count
reset_to_zero: prohibited
```

Example:

```yaml
counter_before_failure: 3/10
failure_result: FAIL
counter_after_failure: 3/10
next_clean_PASS_target: 4/10
```

Failures are still recorded, diagnosed, and remedied. They do not erase previously confirmed clean PASS evidence.

## Qualification and post-validation behavior

```yaml
0_to_2_clean_passes: EXPERIMENTAL
3_to_6_clean_passes: PROVISIONAL
7_to_9_clean_passes: NEAR_VALIDATED
10_clean_passes: VALIDATED_DEFAULT_METHOD_FOR_PROVEN_SCOPE
```

A failure after validation suspends automatic use pending review but does not erase the historical clean PASS count.

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

Draft and owner-review one complete fresh ACT 006 prompt that treats Cline as having zero prior task knowledge and follows `NEW_TASK_ZERO_KNOWLEDGE_PROMPT_REQUIREMENTS.md` exactly.

```yaml
run_before_owner_approval: prohibited
clean_pass_count_before: 3/10
target_after_next_clean_PASS: 4/10
ACT_003_stress_test: postponed_until_10_of_10
```
