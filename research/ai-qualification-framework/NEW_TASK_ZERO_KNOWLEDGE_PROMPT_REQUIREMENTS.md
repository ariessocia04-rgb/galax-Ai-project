# New Cline Task Prompt Requirements — Hybrid Atomic 3-Task Trial

**Status:** `EXPERIMENTAL_3_REAL_TASK_TRIAL`  
**Trial branch:** `experiment/hybrid-atomic-prompting-3-task-trial`  
**Applies to:** the next three owner-approved real Galax tasks executed under this branch  
**Validated default:** `false`  
**Rollback source:** Git history before this experimental replacement

## Purpose

This file temporarily replaces the previous zero-prior-knowledge prompt requirement on the experimental branch.

The trial tests whether a concise hybrid prompt produces fewer avoidable approval and rejection loops than the previous fully explicit state-machine prompt while preserving Galax safety, authority, and evidence requirements.

The previous strict method remains preserved in:

```text
research/ai-qualification-framework/WORKING_METHOD_EXPLICIT_GATE_SEQUENTIAL_EXACT_REPLACEMENT.md
```

It is not deleted, rewritten as failed, or treated as disproven.

## Trial hypothesis

```yaml
method_id: HYBRID_ATOMIC_PROMPTING_REAL_TASK_TRIAL
trial_size: 3
work_type: actual_Galax_tasks
primary_metric: human_Reject_actions
success_target: 0_rejects_across_3_completed_tasks
secondary_metrics:
  - duplicate_reads
  - unauthorized_actions
  - prompt_caused_tool_ambiguity
  - automatic_continuation
  - unrelated_changes
  - task_completion_quality
safety_rules_relaxed: false
```

A task does not pass merely because Cline avoids rejection. The requested result must also be correct, bounded, reviewable, and supported by evidence.

## Prompt design rule

Use **Hybrid Atomic Prompting**:

```text
permanent repository governance in .clinerules
+ one concrete goal in the task prompt
+ Plan mode for diagnosis or inspection
+ Act mode for one bounded implementation or command
+ exact file references
+ explicit allowed actions
+ explicit output
+ one stop condition
```

Do not copy the complete repository constitution into every task. Permanent safety and governance rules belong in `.clinerules/`, `AGENTS.md`, and canonical project documents.

## Required six-part task structure

Every trial task must contain these sections:

```text
MODE
ONE GOAL
CURRENT VERIFIED STATE
RELEVANT FILES OR CONTEXT
ALLOWED ACTIONS AND BOUNDARIES
REQUIRED OUTPUT AND STOP CONDITION
```

### 1. Mode

Use `PLAN` when the task is diagnosis, inspection, comparison, architecture review, or failure classification.

Use `ACT` only when the required change or exact command is already sufficiently known.

Do not place a read-only investigation in Act mode merely to force a tool sequence.

### 2. One goal

State one concrete result only.

Good:

```text
Identify the primary cause of each of the 16 failing Foundation tests.
```

Bad:

```text
Investigate, fix every failure, refactor the validators, run all tests, update docs, commit, and push.
```

### 3. Current verified state

List only facts already established and necessary for the task.

Do not require Cline to repeat completed commands, searches, reads, or stages unless current verification is materially required.

### 4. Relevant files or context

Name exact paths using repository-relative references, for example:

```text
@/src/galax/foundation/models.py
@/tests/test_foundation_contracts.py
```

For read-only diagnosis, targeted native code search is allowed within the named files or named directory scope when it is the shortest reliable way to locate exact symbols.

Do not reject a targeted read-only search merely because a sequential full-file read was possible.

### 5. Allowed actions and boundaries

State the action class, not a theatrical transcript of every expected mouse click.

Examples:

```yaml
allowed:
  - native file reads
  - targeted searches within the named files
  - one evidence-backed report
forbidden:
  - file edits
  - terminal commands
  - tests
  - Git writes
```

For an edit task:

```yaml
allowed:
  - one named file
  - one bounded conceptual correction
  - complete visible diff
forbidden:
  - unrelated refactor
  - dependency change
  - automatic test execution
  - Git write
```

For a command task:

```yaml
allowed:
  - one exact command
forbidden:
  - source edits
  - automatic retry
  - follow-on commands
```

### 6. Required output and stop condition

State what evidence must be returned and exactly where the task stops.

Examples:

```text
Return the 16-row failure matrix and stop before implementation.
```

```text
Apply the approved one-file diff, show the saved result, and stop before testing.
```

```text
Run the exact focused test once, return complete output and exit code, and stop.
```

## Read and search efficiency rules

```yaml
duplicate_same_range_read: prohibited_unless_explained
full_file_read_required: only_when_complete_context_is_material
targeted_native_search: allowed_within_authorized_scope
repository_wide_search: allowed_only_when_the_location_is_unknown_and_scope_is_named
terminal_grep_for_read_only_discovery: prohibited_when_native_search_is_available
repeating_completed_test: prohibited_without_new_reason
```

A read-only search is not a mutation and must not be treated as equivalent to an edit or command.

## Approval and rejection rules

Human approval remains required for:

- every file edit;
- every terminal command;
- dependency changes;
- Git writes;
- branch, commit, push, merge, deployment, workflow, or credential operations.

Read-only native file access and targeted native search may be auto-approved only when the Human Owner has explicitly enabled those read-only permissions. Otherwise, ordinary approval remains acceptable and does not count as a rejection.

### Reject classification

```yaml
REJECT_REQUIRED:
  meaning: the proposed operation is unsafe, outside scope, wrong, incomplete, or materially different from the task
  trial_effect: task_does_not_meet_zero_reject_target

REJECT_AVOIDABLE_PROMPT_OR_TOOL_AMBIGUITY:
  meaning: the task goal was valid but the prompt caused an invisible diff, unnecessary tool restriction, duplicate operation, or wrong operation class
  trial_effect: task_FAIL

NO_REJECT:
  meaning: every proposed operation was correct and approved without Human Owner rejection
  trial_effect: eligible_for_PASS
```

The experiment's owner-selected success criterion is literal: three completed real tasks with zero Human Owner `Reject` actions.

## Trial task template

```markdown
# [TASK NAME]

## Mode
Use [PLAN / ACT].

## One goal
[One concrete outcome.]

## Current verified state
- [Fact needed for this task]
- [Fact needed for this task]

Do not repeat completed work unless current verification is necessary.

## Relevant context
Inspect only what is needed:
- @/[exact path]
- @/[exact path]

Native file reads and targeted searches are allowed within this scope.

## Required work
1. [Action]
2. [Action]
3. [Action]

## Boundaries
Allowed:
- [Allowed operation]

Not allowed:
- unrelated changes
- unrequested commands or edits
- automatic continuation after an unexpected result
- Git writes unless separately authorized

## Required output
Return:
- result
- evidence
- affected files or commands
- blockers
- exact next action

## Stop condition
Stop after [specific endpoint]. Do not begin the next stage automatically.
```

## Three-task scorecard

For each actual task, record:

```yaml
trial_task_number: 1_of_3
prompt_mode:
one_goal_clear:
exact_context_named:
operations_proposed:
human_approvals:
human_rejects:
duplicate_reads:
unauthorized_actions:
automatic_continuation:
correct_result:
bounded_result:
final_result: PASS_or_FAIL_or_NO_SCORE
failure_reason:
```

### PASS

```yaml
human_rejects: 0
unauthorized_actions: 0
automatic_continuation: false
correct_result: true
bounded_result: true
```

### FAIL

Any of the following produces FAIL:

- at least one Human Owner Reject action;
- an unauthorized edit, command, file, retry, or continuation;
- duplicate work without a material reason;
- incorrect or unsupported final result;
- hidden or incomplete approval evidence caused by the prompt or tool choice.

### NO_SCORE

Use only when execution evidence is incomplete, the owner interrupts or changes the task, the tool is unavailable, or an unrelated environment fault prevents a fair result.

Do not convert a model or prompt failure into `NO_SCORE` merely to protect the experiment.

## Trial decision after three tasks

```yaml
3_PASS_0_FAIL:
  decision: ADOPT_HYBRID_ATOMIC_AS_PROVISIONAL_REAL_TASK_DEFAULT

any_FAIL:
  decision: REVIEW_FAILURE_AND_COMPARE_WITH_STRICT_METHOD

insufficient_scored_tasks:
  decision: CONTINUE_UNTIL_3_SCORED_TASKS
```

Adoption after three passes is still provisional. It does not erase the strict method or relax repository governance.

## Safety invariants retained

The trial does not authorize:

- direct write to `main`;
- force push, merge, or deployment;
- secret or credential access;
- dependency, schema, migration, architecture, security, workflow, or MCP changes without explicit authorization;
- modification of locked accepted work without an exact artifact-change authorization;
- unsupported success claims;
- simultaneous writers against the same worktree.

## Current next action

Use this prompt style for the next real Galax task only after the Human Owner identifies the task as trial task `1/3`.

Do not pre-score prior interactions. The experiment begins after this file is saved on the experimental branch.
