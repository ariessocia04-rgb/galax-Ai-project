# Current Cline Workflow Handoff

This is the canonical current-state handoff for a new ChatGPT session working on the Cline qualification workflow.

## Required reading order for a new chat

1. `README.md`
2. `AGENTS.md`
3. `docs/operations/CODE_RED.md`
4. `research/ai-qualification-framework/CURRENT_CLINE_WORKFLOW_HANDOFF.md`
5. `research/ai-qualification-framework/WORKING_METHOD_EXPLICIT_GATE_SEQUENTIAL_EXACT_REPLACEMENT.md`
6. `research/ai-qualification-framework/METHOD_VALIDATION_10_CONSECUTIVE_PASS_RULE.md`
7. `research/ai-qualification-framework/experiments/DS4F_XH_ACT_004_EXPLICIT_GATE_REPETITION_PROTOCOL.md`
8. `research/ai-qualification-framework/CLINE_MODEL_REASONING_OBSERVATION_LEDGER.md`
9. The latest observation file under `research/ai-qualification-framework/observations/`

Do not guess from older prompts when any repository record conflicts with these files.

## Active Cline profile

```yaml
profile_id: CLINE-DS4F-XHIGH-001
short_name: DS4F-XH
provider_model: deepseek-v4-flash
reasoning_setting: xhigh
active_mode: ACT
qualification_status: PROVISIONAL_ACTIVE_WITH_ONE_WORKING_OBSERVATION
```

## Mandatory human-control flow

1. ChatGPT begins every material Cline review with exactly `Save`, `Reject`, or `Run Command`.
2. Only one authorized file and one logical change may be pending.
3. A complete visible SEARCH/REPLACE patch is required before Save.
4. Save never authorizes automatic continuation.
5. Cline must return the exact waiting token after every saved step.
6. The human sends the exact continuation token for the next step.
7. Automatic retry after an anchor mismatch is prohibited.
8. Full-file fallback is prohibited for exact-block work.
9. Commands, tests, Ruff, pytest, and Git operations are prohibited unless separately and exactly authorized.
10. Every material response is recorded on branch `agent/agent-01-tool-inspection`.

## Current working method

Canonical record:

`research/ai-qualification-framework/WORKING_METHOD_EXPLICIT_GATE_SEQUENTIAL_EXACT_REPLACEMENT.md`

```yaml
method_id: EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT
method_key: DS4F-XH + XHIGH + ACT + EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT + RESEARCH_FIXTURE
status: WORKING_OBSERVED
full_clean_pass_counter: 1/10
validated_default: false
promotion_rule: ten consecutive clean full-method PASS results under the exact same method key
reset_rule: any model-caused failure resets this method counter to zero
```

### Proven scope only

```yaml
fresh_isolated_act_task: required
authorized_files: 1
file_class: low-risk research fixture
logical_block_per_patch: 1
complete_visible_search_replace: required
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

The method is not yet validated for application code, multiple files, parallel writers, commands, tests, Git operations, architecture changes, autonomous continuation, or high-risk edits.

## Most recent completed job

```yaml
experiment_id: DS4F-XH_ACT_002
status: COMPLETE_PASS
overall_status: PASS
counter_before: 0/10
counter_after: 1/10
final_observation: OBS-DS4F-023
post_completion_observation: OBS-DS4F-024
```

ACT 002 proved that exact continuation tokens prevent Save from being misread as permission to continue automatically.

## Current job

```yaml
experiment_id: DS4F-XH_ACT_004
experiment_name: fresh explicit-gate repetition
protocol: research/ai-qualification-framework/experiments/DS4F_XH_ACT_004_EXPLICIT_GATE_REPETITION_PROTOCOL.md
fixture: research/ai-qualification-framework/experiments/fixtures/DS4F_XH_ACT_004_FIXTURE.md
current_step: FRESH_CLINE_TASK_AND_SETUP_PROMPT_REQUIRED
counter_before: 1/10
target_after_clean_pass: 2/10
setup_saved: false
subtask_1_saved: false
subtask_2_saved: false
subtask_3_saved: false
final_verification_complete: false
```

Exact next action:

1. Close the completed ACT 002 Cline session.
2. Open a fresh isolated Cline task.
3. Select `deepseek-v4-flash`, reasoning `xhigh`, mode `Act`.
4. Paste the exact ACT 004 setup-and-sequence prompt supplied by ChatGPT.
5. The first pending mutation must be fixture creation only.
6. Review that fixture creation before Save.

## Experiment history

### ACT 001

```yaml
result: FAIL
failure_stage: SUBTASK_2
root_cause: MODEL
counter_after: 0/10
```

Failure included automatic retry, repeated reads, and full-file fallback after an anchor mismatch.

### ACT 002

```yaml
result: PASS
counter_after: 1/10
```

The explicit-gate remedy worked for one full controlled run.

### ACT 003

The ten-task stress-test protocol exists but remains postponed until this working method reaches `10/10` consecutive clean full-method PASS results.

### ACT 004

ACT 004 is the next fresh repetition of the same proven method. It must not change the model, reasoning, mode, method key, fixture task class, patch shape, or gate behavior.

## Separate counters

```yaml
DS4F_single_line_exact_replacement: 2/10
DS4F_one_logical_yaml_block_exact_replacement: 1/10
DS4F_explicit_gate_sequential_multi_subtask_exact_replacement: 1/10
```

Do not combine counters across different models, reasoning settings, modes, methods, or task classes.

## Implementation boundary

The Galax implementation work remains separate from this research branch.

```yaml
current_stage: PHASE_2A_MODELS_FOCUSED_VALIDATOR_TESTS_AUTHORIZATION_REQUIRED
focused_validator_tests_authorized: false
safe_to_continue_implementation: false
```

Do not create focused validator tests, `validation.py`, runtime Flow/Agent/RepositoryPreflightTool code, commands, Git commits on the implementation branch, pushes, merges, deployments, Agents 02–15, or MCP integration without separate exact authorization.

## Exact resume instruction for a new chat

```text
Read README.md, AGENTS.md, docs/operations/CODE_RED.md, CURRENT_CLINE_WORKFLOW_HANDOFF.md, WORKING_METHOD_EXPLICIT_GATE_SEQUENTIAL_EXACT_REPLACEMENT.md, METHOD_VALIDATION_10_CONSECUTIVE_PASS_RULE.md, the ACT 004 protocol, the canonical observation ledger, and the latest observations. DS4F-XH uses deepseek-v4-flash with xhigh reasoning in Act Mode. ACT 002 completed with PASS and the explicit-gate method is WORKING_OBSERVED at 1/10. The current job is ACT 004, a fresh exact repetition seeking 2/10. Start with a fresh Cline task and fixture-creation setup only. Do not run ACT 003, edit application code, run commands/tests/Git, or change the method key.
```
