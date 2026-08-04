# Galax AI — Persistent Cline Memory and Control Rule

**Status:** `ACTIVE_AUTO_LOADED_PROJECT_RULE`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`

This file is intentionally inside `.clinerules/` so Cline loads it automatically in every new task opened from this repository workspace.

## Zero-prior-knowledge rule

Treat every new Cline task as having zero knowledge of earlier chats, tasks, checkpoints, prompts, fixtures, counters, approvals, or intended tools.

Never guess the previous state. Before answering, editing, proposing a command, or asking the owner to choose an action, read the required records below.

## Mandatory reading order

For any Galax task:

1. `README.md`
2. `AGENTS.md`
3. `docs/operations/CODE_RED.md`
4. `docs/operations/CODE_RED_CLINE_QUALIFICATION_CHECKPOINT_2026-07-23.md` when the task concerns Cline testing, qualification, prompts, model behavior, or the phrase `length chat problem`
5. `memory-bank/MEMORY.md`
6. The exact active plan, rule, handoff, protocol, or assignment named in those records

Do not rely on conversation memory when these repository records exist.

## Active Cline qualification state

```yaml
profile_id: CLINE-DS4F-XHIGH-001
provider_model: deepseek-v4-flash
reasoning_setting: xhigh
mode: ACT
method_id: EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT
method_key: DS4F-XH + XHIGH + ACT + EXPLICIT_GATE_SEQUENTIAL_MULTI_SUBTASK_EXACT_REPLACEMENT + RESEARCH_FIXTURE
clean_passes_accumulated: 3/10
validated_default: false
counting_model: CUMULATIVE_CLEAN_PASS_COUNT
```

Confirmed clean full-method PASS runs:

```yaml
ACT_002: PASS
ACT_004: PASS
ACT_005: PASS
```

ACT 006 remains:

```yaml
status: ABANDONED_HUMAN_ERROR
score_effect: NO_SCORE
model_failure: false
counter_before: 3/10
counter_after: 3/10
```

## Owner-approved scoring rule

The owner superseded the old consecutive-reset rule.

```yaml
required_clean_passes_for_validation: 10
counting_method: cumulative
clean_PASS: increment_by_1
FAIL: record_failure_and_keep_current_pass_count
NO_SCORE: keep_current_pass_count
human_error: keep_current_pass_count
platform_error: keep_current_pass_count
ambiguous_event: keep_current_pass_count
reset_to_zero: prohibited
```

Example:

```yaml
counter_before_failure: 3/10
failure_recorded: true
counter_after_failure: 3/10
next_clean_pass_target: 4/10
```

Never describe this count as an unbroken consecutive streak. It is a cumulative qualification count with failures preserved as separate evidence.

## Exact new-task prompt requirement

Before a fresh qualification run, read:

`research/ai-qualification-framework/NEW_TASK_ZERO_KNOWLEDGE_PROMPT_REQUIREMENTS.md`

A fresh prompt must explicitly provide:

- repository and workspace starting point;
- exact authorized target file;
- exact first action;
- exact permitted native file tool sequence;
- exact behavior when the file exists;
- exact behavior when it does not exist;
- exact blocker when the native file tool is unavailable;
- prohibition on terminal or shell fallback;
- complete Save/wait/continue state machine;
- exact final receipt.

A scenario description alone is insufficient.

## Qualification action boundary

During the current research-fixture qualification method:

```yaml
authorized_files: 1
file_class: low-risk_research_fixture
maximum_pending_edits: 1
complete_visible_SEARCH_REPLACE: required
human_Save_between_steps: required
exact_continue_tokens: required
automatic_retry: prohibited
full_file_fallback: prohibited
terminal_commands: prohibited
tests: prohibited
Git_operations: prohibited
application_code: prohibited
parallel_execution: prohibited
```

When the required native file tool is unavailable, stop with:

```text
BLOCKED_NATIVE_FILE_TOOL_REQUIRED
```

Do not substitute a terminal existence check.

## Human review vocabulary

Every material review instruction shown to the owner must begin with exactly one of:

```text
Save
Reject
Run Command
```

Classify only observable behavior. Do not claim access to private chain-of-thought.

## Current exact next action

```yaml
next_action: DRAFT_AND_OWNER_REVIEW_NEW_ACT_006_PROMPT
prompt_mode: FRESH_ZERO_PRIOR_KNOWLEDGE
counter_before: 3/10
target_after_next_clean_PASS: 4/10
run_before_owner_approval: prohibited
```

## Galax implementation boundary

The Cline qualification workflow does not authorize Galax application implementation.

```yaml
safe_to_continue_implementation: false
local_state_recovery_required: true
focused_validator_tests_authorized: false
Agents_02_to_15: prohibited
push: prohibited
merge: prohibited
deployment: prohibited
```
