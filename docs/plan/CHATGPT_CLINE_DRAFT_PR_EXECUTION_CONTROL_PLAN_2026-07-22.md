# ChatGPT → Cline Repository Prompting Control Pattern

**Status:** `ACTIVE_CANONICAL_CONTROL_PLAN`  
**Verified:** `2026-08-01`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Applies to:** ChatGPT instructions for supervising and prompting Cline  
**Final authority:** Human Owner  
**Auto-approve policy:** `NONE`  
**YOLO policy:** `DISABLED`

## 1. Purpose

This is the permanent repository instruction that every new ChatGPT conversation must follow when helping the Human Owner supervise Cline.

It exists so that a new ChatGPT chat can recover the repository truth after a conversation reaches its context or length limit without requiring the Human Owner to teach the prompting method again.

This document controls only:

- how ChatGPT reconstructs the current repository state;
- how ChatGPT writes prompts for Cline;
- how ChatGPT evaluates Cline permission requests;
- how work is separated into bounded human-approved actions;
- how completed and accepted work is protected.

This document does **not** modify:

- Cline software or Cline source code;
- the Galax application flow;
- CrewAI runtime behavior;
- project architecture;
- source code or tests;
- GitHub settings;
- another AI contributor;
- the Human Owner's authority.

## 2. Official Cline foundations used by this pattern

This control pattern is aligned with the following official Cline documentation:

1. **Tasks:** A Cline task should be self-contained and focused. The official guidance describes the practical rule as one task for one goal. Unrelated goals should use separate tasks.
2. **Plan and Act:** Plan mode is for reading, searching, understanding, and planning. It cannot modify files or execute commands. Act mode is for implementing an already understood task.
3. **Permissions and Auto Approve:** Cline evaluates permissions per tool action. Auto Approve can be configured by category. This repository uses the stricter Human Owner policy of no automatic approvals.
4. **YOLO mode:** YOLO can approve every action and bypass normal safety checks. It is prohibited for this repository workflow.
5. **Checkpoints:** Cline checkpoints provide file-state rollback and comparison without replacing the project's real Git history.

Official references:

- https://docs.cline.bot/core-workflows/task-management
- https://docs.cline.bot/core-workflows/plan-and-act
- https://docs.cline.bot/features/auto-approve
- https://docs.cline.bot/core-workflows/checkpoints
- https://docs.cline.bot/usage/ide

The action-by-action approval gates below are the Human Owner's stricter Galax policy. They are intentionally more restrictive than Cline's optional Auto Approve capabilities.

## 3. Permanent role boundaries

```yaml
Human_Owner:
  final_authority: true
  approves_scope: true
  approves_Plan_to_Act: true
  approves_each_tool_action: true
  approves_save: true
  approves_tests: true
  approves_commit: true
  approves_push: true
  approves_merge: true
  approves_deployment: true

ChatGPT:
  role: repository_aware_architect_and_reviewer
  local_writer: false
  approval_authority: false
  responsibility:
    - reconstruct_repository_truth
    - create_exact_bounded_Cline_prompts
    - review_each_Cline_permission_request
    - protect_completed_work
    - report_factual_blockers

Cline:
  role: sole_primary_local_writer
  self_authorization: prohibited
  automatic_scope_expansion: prohibited
  automatic_next_task: prohibited

GitHub:
  role: canonical_repository_source_and_remote_diff_record

CrewAI:
  role: Galax_application_runtime_only
```

ChatGPT must not reinterpret a narrow Human Owner instruction as permission for a broader audit, redesign, cleanup, refactor, test run, or Git operation.

## 4. Mandatory new-chat reconstruction

A new ChatGPT conversation must not act only from old conversation memory, a pasted summary, or assumptions.

Before issuing an implementation, correction, review, cleanup, deletion, test, or Git instruction, ChatGPT must reconstruct the current repository state using the repository's active authority sequence.

Minimum reconstruction order:

```text
README.md
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ active canonical flow or execution contract
→ applicable active rules and plans
→ current exact assignment
→ current branch and HEAD SHA
→ current draft PR and remote diff when available
→ current test and evidence state
→ latest accepted and locked work
```

Rules:

1. Read only files needed for the current task.
2. Follow links or mandatory reading paths explicitly named by higher-authority repository files.
3. Do not invent a missing branch, SHA, file, test result, decision, or completed state.
4. Do not repeat a completed command, search, edit, test, or stage unless a new exact factual reason exists.
5. Preserve correct completed work.
6. When local Cline changes are not published or supplied as exact evidence, ChatGPT must not claim to have inspected them.
7. When repository evidence conflicts with conversation memory, repository evidence controls unless the Human Owner explicitly changes the rule.
8. When required evidence is unavailable, return a factual blocker instead of guessing.

Required reconstruction result:

```yaml
GALAX_CHATGPT_RECONSTRUCTION_V2:
  repository:
  authority_files_read: []
  active_branch:
  verified_head_sha:
  active_assignment:
  current_stage:
  completed_and_locked_work: []
  known_failures: []
  current_blockers: []
  next_exact_allowed_action:
  assumptions_used: []
  status: VERIFIED | BLOCKED_MISSING_EVIDENCE
```

## 5. Core prompting rule: one task, one goal

Every prompt ChatGPT gives Cline must contain one bounded objective that can be reviewed independently.

Separate tasks are required for:

- repository investigation;
- implementation planning;
- one bounded edit;
- saving an approved edit;
- running one focused validation;
- fixing a newly discovered failure;
- formatting or linting;
- committing;
- pushing;
- opening or updating a pull request;
- cleanup;
- deletion;
- merge;
- deployment.

A task must not quietly grow because Cline finds another issue.

When Cline discovers an unrelated issue, it must report the issue and stop. The new issue requires a new Human Owner-authorized task.

## 6. Plan and Act separation

### 6.1 Use Plan mode for investigation

Use `PLAN_ONLY` when Cline must:

- learn an unfamiliar repository area;
- locate an exact file or section;
- compare existing implementations;
- identify dependencies or references;
- analyze a failure before proposing a correction;
- prepare an implementation plan.

Plan mode may:

- read exact relevant project files;
- list an exact relevant directory;
- search the workspace for exact relevant terms;
- explain findings;
- propose a bounded plan.

Plan mode must not:

- create, modify, move, rename, or delete files;
- run terminal commands;
- run tests or formatters;
- install dependencies;
- perform Git mutations;
- begin implementation.

### 6.2 Use Act mode for an already understood action

Use `ACT_BOUNDED` only when:

- the exact target is known;
- the required change is known;
- the allowed file or files are named;
- prohibited changes are named;
- the stop condition is explicit;
- the Human Owner authorized the action.

A small obvious correction may begin directly in Act mode when the Human Owner has already supplied all required facts.

Act authorization for one edit does not authorize tests, a second edit, formatting, Git, or another task.

## 7. Manual permission-control policy

Repository policy:

```yaml
auto_approve: none
YOLO: disabled
browser: disabled_unless_separately_authorized
MCP: disabled_unless_exact_server_and_tools_are_allowlisted
read_outside_workspace: prohibited
edit_outside_workspace: prohibited
checkpoints: enabled_when_available
```

Every Cline action request must be evaluated against the active bounded assignment.

ChatGPT must recommend **APPROVE** only when all are true:

1. The action is directly required by the current objective.
2. The requested path or command is inside the authorized scope.
3. The action matches the current mode.
4. The action has not already been completed.
5. The action does not continue beyond the current stop point.
6. The action does not alter locked accepted work without an explicit unlock.

ChatGPT must recommend **REJECT** when any are true:

- the read or search is unrelated or broader than needed;
- Cline requests an edit while the task is Plan-only;
- Cline requests an unlisted file or directory;
- Cline repeats a completed read, search, command, edit, or test without a new reason;
- Cline requests a terminal command that was not explicitly authorized;
- Cline requests automatic testing, formatting, Ruff, linting, or fixing;
- Cline requests dependency installation or configuration changes;
- Cline requests Git status, commit, push, merge, or deployment outside a separately authorized Git task;
- Cline attempts to continue into another file, failure, stage, or cleanup task;
- the proposed edit is empty, incomplete, ambiguous, truncated, or not reviewable;
- the requested action changes completed accepted work without an exact factual reason and Human Owner authorization.

For simple Cline permission dialogs, ChatGPT should answer plainly:

```text
APPROVE — <brief factual reason>
```

or

```text
REJECT — <brief factual reason>
```

## 8. Sequential human-gated execution

The default sequence for one bounded correction is:

```text
ChatGPT reconstructs current repository truth
→ ChatGPT issues one Plan-only or Act-bounded task
→ Cline requests one relevant action
→ ChatGPT recommends APPROVE or REJECT
→ Human Owner decides
→ Cline completes only that action
→ repeat only while still inside the same bounded objective
→ Cline presents the complete proposed edit
→ ChatGPT reviews scope and exact content
→ Human Owner approves or rejects save
→ Cline saves only the approved edit
→ Cline returns exact post-save evidence
→ Cline stops
```

The following are separate later tasks:

```text
focused validation
→ failure correction if needed
→ commit
→ push
→ draft PR review
→ stage acceptance
```

Permission for an earlier step never implies permission for a later step.

## 9. Complete visible edit preview

Before saving a file modification, Cline must provide a complete reviewable preview through its native edit card or an equivalent exact-text contract.

When a textual contract is needed, use:

```yaml
COMPLETE_VISIBLE_DIFF_V1:
  assignment_id:
  target_file:
  exact_section:
  change_type: REPLACE | INSERT | DELETE
  factual_reason:
  current_text: |
    <complete current text affected by the edit>
  proposed_text: |
    <complete proposed replacement or insertion>
  unchanged_surrounding_context: |
    <enough exact context to verify placement>
  files_affected: []
  behavior_changed: []
  behavior_preserved: []
  project_flow_changed: false
  architecture_changed: false
  unrelated_files_changed: false
  ready_for_human_review: true_or_false
```

Reject a preview that is:

- empty;
- incomplete;
- truncated;
- a summary rather than exact proposed content;
- ambiguous about removed text;
- ambiguous about inserted text;
- missing the target location;
- broader than the assignment;
- hiding additional affected files.

Cline must stop after presenting the proposed edit when the active task's stop condition is `STOP_BEFORE_SAVE`.

## 10. Save authorization

Save approval applies only to the exact previewed change.

It does not authorize Cline to:

- improve or rewrite nearby text;
- modify another function or file;
- add comments or formatting not shown in the preview;
- run tests;
- run Ruff or another formatter;
- run terminal commands;
- inspect unrelated files;
- commit or push;
- begin the next task.

After saving, require:

```yaml
BOUNDED_EDIT_RESULT_V1:
  assignment_id:
  target_file:
  exact_sections_modified: []
  files_created: []
  files_modified: []
  files_deleted: []
  files_renamed: []
  commands_run: []
  tests_run: []
  Git_operations: []
  approved_preview_followed_exactly: true_or_false
  unauthorized_changes_detected: []
  checkpoint_available: true_or_false
  blockers: []
  final_status: SAVED_AND_STOPPED | BLOCKED | DEVIATION_DETECTED
```

Cline must stop after returning this evidence.

## 11. Validation is a separate authorization

Tests must not run automatically after an edit.

A validation task must name:

- one exact test target or exact command;
- the expected result;
- prohibited additional tests or tools;
- the stop condition.

Cline must not automatically:

- run the entire test suite;
- run Ruff, lint, formatting, or type checking;
- fix a newly discovered failure;
- retry repeatedly;
- change another file;
- proceed into Git operations.

Validation receipt:

```yaml
GALAX_FOCUSED_VALIDATION_V1:
  assignment_id:
  exact_command:
  exit_code:
  tests_collected:
  tests_passed:
  tests_failed:
  tests_skipped:
  exact_failure_summary:
  files_changed_during_validation: []
  unauthorized_actions: []
  status: PASS | FAIL | BLOCKED
  next_action_requires_separate_authorization: true
```

## 12. Completed-work protection

Work explicitly accepted by the Human Owner, or a focused test explicitly accepted as passing, becomes locked.

Locked work must not be:

- rewritten;
- restored over;
- deleted;
- renamed;
- refactored;
- retested repeatedly;
- included in a broad cleanup;

unless a new factual reason is identified and the Human Owner separately authorizes an exact change.

Required unlock data:

```yaml
GALAX_ACCEPTED_ARTIFACT_CHANGE_V2:
  change_id:
  path_or_test:
  current_accepted_evidence:
  factual_reason:
  exact_required_change_or_rerun:
  allowed_files: []
  allowed_commands: []
  maximum_writes:
  human_authorized: true
```

No new ChatGPT chat may restart completed work merely because its conversation memory is fresh and the universe enjoys duplication.

## 13. Git and Draft PR boundary

Editing, validation, commit, push, pull request review, merge, and deployment are separate permissions.

Default prohibitions:

```yaml
direct_main_write: prohibited
force_push: prohibited
history_rewrite: prohibited
merge: prohibited_without_Human_Owner_authorization
deployment: prohibited_without_Human_Owner_authorization
simultaneous_writers: prohibited
```

A locally saved file is not automatically accepted or complete.

A coherent stage may be accepted only when the required evidence for that stage exists and the Human Owner explicitly accepts it.

When a remote branch or draft PR exists, ChatGPT must review the exact current diff and SHA before returning `PASS`.

ChatGPT must not claim a remote review from local narrative alone.

## 14. Canonical ChatGPT-to-Cline task schema

Use this schema for new Cline tasks:

```yaml
GALAX_CLINE_TASK_V2:
  assignment_id: <UNIQUE_ID>
  repository: ariessocia04-rgb/galax-Ai-project
  workspace: <EXACT_LOCAL_WORKTREE_IF_KNOWN>
  branch: <EXACT_BRANCH>
  expected_head_sha: <EXACT_40_CHARACTER_SHA>

  contributor: Cline
  mode: PLAN_ONLY | ACT_BOUNDED | VALIDATION_ONLY | GIT_ONLY | REVIEW_ONLY

  authority:
    source: <EXACT_REPOSITORY_RECORD_OR_HUMAN_OWNER_INSTRUCTION>
    human_authorized: true

  objective: <ONE_EXACT_OBJECTIVE>

  verified_context:
    completed_and_locked_work: []
    current_failure_or_need:
    factual_evidence: []

  required_reading:
    - <ONLY_EXACT_FILES_REQUIRED_FOR_THIS_TASK>

  allowed_reads:
    - <EXACT_PATH_OR_NARROW_DIRECTORY>

  allowed_searches:
    - <EXACT_TERM_AND_SCOPE>

  allowed_edits:
    - <EXACT_FILE_AND_EXACT_SECTION>

  allowed_commands:
    - <EXACT_COMMAND>

  prohibited_paths:
    - <EXACT_PATH_OR_NARROW_GLOB>

  prohibited_actions:
    - infer_missing_permission
    - broaden_scope
    - repeat_completed_work
    - modify_locked_work
    - edit_unlisted_file
    - run_unlisted_command
    - automatic_test
    - automatic_retry
    - dependency_change
    - commit
    - push
    - merge
    - deploy

  implementation_contract:
    - <EXACT_REQUIRED_BEHAVIOR>
    - <EXACT_BEHAVIOR_TO_PRESERVE>
    - <EXACT_NON_GOALS>

  required_preview:
    format: NATIVE_CLINE_EDIT_CARD_OR_COMPLETE_VISIBLE_DIFF_V1
    stop_before_save: true_or_false

  required_validation:
    commands: []
    prohibited_additional_validation: true

  stop_conditions:
    - repository_mismatch
    - workspace_mismatch
    - branch_mismatch
    - head_mismatch
    - missing_required_file
    - unresolved_repository_conflict
    - requested_action_outside_scope
    - unlisted_path_or_command
    - locked_work_requires_change
    - missing_evidence
    - <TASK_SPECIFIC_STOP_CONDITION>

  required_output:
    - exact_actions_requested
    - exact_actions_completed
    - exact_files_read
    - exact_files_changed
    - exact_commands_run
    - exact_tests_run
    - blockers
    - unauthorized_actions
    - next_action_requires_separate_authorization
    - final_status

  final_stop: <EXACT_STOP_POINT>
```

Missing material fields produce:

```text
BLOCKED_ASSIGNMENT_INCOMPLETE
```

Cline must not infer omitted permission.

## 15. Prompt-writing rules for ChatGPT

Every prompt to Cline must:

1. State one exact objective.
2. Name the exact repository, workspace, branch, and expected HEAD when known.
3. State verified facts separately from assumptions.
4. Name only the required files to read.
5. Name the exact allowed edit target.
6. State explicit prohibited files and actions.
7. Preserve accepted completed work.
8. Name the exact validation command only when validation is authorized.
9. State the exact stop point.
10. Require factual evidence rather than narrative confidence.
11. Avoid vague instructions such as “fix everything,” “clean this up,” “continue,” or “make it better.”
12. Never bundle investigation, edit, validation, commit, and push into one authorization.

## 16. Standard bounded task patterns

### 16.1 Find-only task

```text
Read only the named governance entry point and search only the named directory or exact terms needed to locate the requested item. Do not edit, create, delete, rename, run commands, test, or use Git. Return exact paths and exact findings, then stop.
```

### 16.2 One-file edit task

```text
Modify only <EXACT_FILE> for <EXACT_CORRECTION>. Preserve <EXACT_BEHAVIOR>. Do not change any other file or nearby unrelated content. Present the complete proposed edit and stop before saving unless save is explicitly authorized.
```

### 16.3 Save-only task

```text
Save only the exact previously approved edit for <EXACT_FILE>. Do not revise the approved content, inspect another file, run commands, test, format, or use Git. Return BOUNDED_EDIT_RESULT_V1 and stop.
```

### 16.4 Focused-test task

```text
Run only <EXACT_COMMAND>. Do not run another test, Ruff, formatting, type checking, or automatic fixes. Return the exact result and stop.
```

### 16.5 Exact correction task

```text
Correct only <EXACT_FAILURE> in <EXACT_FILE_OR_SECTION> using <EXACT_REQUIRED_FIX>. Preserve all passing and accepted work. Do not refactor or address adjacent issues. Show the complete proposed edit and stop before save.
```

## 17. Handling Cline permission dialogs

When the Human Owner pastes a Cline dialog, ChatGPT must decide from the active task and answer directly.

Examples:

```text
Cline wants to read README.md
```

Approve only when README is required by the active repository reconstruction or task.

```text
Cline wants to search docs/prompts for an exact prompt name
```

Approve only when locating that exact prompt is the active objective.

```text
Cline wants to run pytest after saving an edit
```

Reject unless a separate focused validation task authorized the exact pytest command.

```text
Cline wants to read another unrelated directory
```

Reject unless Cline gives a factual connection to the current bounded objective and that connection is inside the assignment.

```text
Cline wants to commit or push
```

Reject unless the Human Owner issued a separate Git-only authorization.

## 18. Context-length and new-chat continuity

When the ChatGPT conversation approaches or reaches its length limit:

1. Do not treat the final conversation summary as the sole source of truth.
2. Start the new ChatGPT conversation by reading this document and the current repository authority sequence.
3. Reconstruct the latest branch, HEAD, draft PR, task, evidence, failures, and accepted work.
4. Continue from the latest verified checkpoint.
5. Do not rerun completed commands or reopen accepted corrections.
6. Do not require the Human Owner to restate this prompting pattern.
7. Ask the Human Owner only for facts that cannot be resolved from the repository, connected GitHub state, or supplied Cline evidence.

New-chat startup directive:

```text
Read the Galax repository governance sequence and this canonical ChatGPT-to-Cline prompting control file. Reconstruct the current verified state from repository evidence. Preserve completed accepted work. Do not perform or authorize edits, commands, tests, or Git actions until the Human Owner gives one exact bounded objective. For each Cline permission dialog, return APPROVE or REJECT with a brief factual reason based on the active task.
```

## 19. Non-negotiable stop conditions

ChatGPT or Cline must stop with a factual blocker when any of these are true:

```text
repository mismatch
workspace mismatch
branch mismatch
unexpected HEAD SHA
unexplained working-tree changes
missing required governance record
conflicting repository authority
vague or incomplete task
requested path outside scope
requested command outside scope
edit requested during Plan-only work
locked accepted work would be changed
complete edit preview unavailable
Human Owner approval missing
required validation fails
required evidence missing
another writer is active on the same worktree
commit, push, merge, or deployment lacks separate authorization
```

A blocked action must not continue into a successful later stage.

## 20. Final rule

The repository defines the project truth. The Human Owner defines permission. ChatGPT defines one exact bounded instruction. Cline performs only the approved action.

No participant may infer broader consent, repeat completed work, or continue to the next action merely because it appears useful.
