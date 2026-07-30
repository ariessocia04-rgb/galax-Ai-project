# HOW TO PROPER CREATE PROMPT FOR CLINE

```yaml
document_id: HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE
status: ACTIVE_CANONICAL_CLINE_PROMPT_CREATION_RULE
repository: ariessocia04-rgb/galax-Ai-project
applies_to:
  - ChatGPT
  - every_new_chat
  - every_repository_aware_assignment_author
  - every_Cline_prompt_revision
controls: HOW_TO_WRITE_THE_EXACT_PROMPT_GIVEN_TO_CLINE
replaces_for_Cline_prompt_creation:
  - generic_Cline_Stage_A_one_line_prompt
  - generic_Cline_Stage_B_one_line_prompt
  - generic_nested_assignment_template_used_without_the_owner_section_pattern
replaces_CODE_RED: false
replaces_execution_control_plan: false
human_owner_final_authority: true
```

> [!IMPORTANT]
> **Every new chat must read this file before creating, correcting, reviewing, or approving any prompt for Cline.**
>
> The required path is:
>
> `docs/prompts/HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE.md`

## 1. Purpose

This file defines the required Galax prompt-writing pattern for Cline.

The prompt must follow the flat, strict, sectioned pattern established by the Human Owner's accepted assignments. It must not be replaced by a vague one-line command, a generic all-purpose YAML object, or a remembered template from an older chat.

This file controls prompt construction only. Repository authority, architecture, accepted work, current state, and execution permissions still come from the current repository evidence and exact Human Owner authorization.

## 2. Mandatory reading path before writing a Cline prompt

Before drafting any new Cline prompt, a new chat or assignment author must read and verify, in this order:

```text
README.md
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ docs/operations/GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md
→ the latest file under docs/operations/checkpoints/
→ docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md
→ the exact active plan and parent assignment
→ docs/prompts/HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE.md
→ the current branch, HEAD, Git status, PR, issue, and exact evidence
→ the latest owner-uploaded Cline receipt or conversation when supplied
```

Do not ask the Human Owner to repeat facts that are already available through the repository or the supplied receipt.

Do not use old chat memory as repository truth.

## 3. Mandatory prompt identity block

Every Cline prompt must begin with this flat identity pattern:

```text
GALAX_AI_ASSIGNMENT_V1

assignment_id: <EXACT_UNIQUE_ASSIGNMENT_ID>
parent_assignment_id: <EXACT_PARENT_ASSIGNMENT_ID_WHEN_APPLICABLE>
parent_plan_id: <EXACT_PARENT_PLAN_ID_WHEN_APPLICABLE>

contributor: Cline
role: <EXACT_BOUNDED_ROLE>
mode: <EXACT_MODE>
repository: ariessocia04-rgb/galax-Ai-project
branch: <EXACT_BRANCH>
```

Rules:

1. Replace every placeholder before giving the prompt to Cline.
2. Use the exact current branch and SHA supported by evidence.
3. Do not reuse a stale assignment ID.
4. Do not omit the parent assignment or plan when the task continues an existing controlled stage.
5. The role must describe the one bounded job, not a broad permanent identity.
6. The mode must match the actual authority granted.

## 4. Allowed assignment modes

Use one exact mode only:

```text
PLAN_ONLY_CONTENT_CORRECTION
PLAN_ONLY_READ_ONLY_DISCOVERY
PLAN_ONLY
ACT_BOUNDED
VALIDATION_ONLY
COMMIT_ONLY
PUSH_ONLY
REVIEW_ONLY
CHECKPOINT_ONLY
```

Mode rules:

- `PLAN_ONLY_CONTENT_CORRECTION` returns complete corrected proposed content but performs no file mutation or command.
- `PLAN_ONLY_READ_ONLY_DISCOVERY` performs only separately approved reads or searches and returns a factual receipt.
- `PLAN_ONLY` prepares one bounded plan and performs no edit.
- `ACT_BOUNDED` performs only the exact authorized mutation and stops before validation unless validation is explicitly part of that same authorized stage.
- `VALIDATION_ONLY` runs only exact allowlisted validation commands and performs no unrelated mutation.
- `COMMIT_ONLY` creates only the exact Human Owner-authorized commit.
- `PUSH_ONLY` pushes only the exact authorized branch and commit.
- `REVIEW_ONLY` performs no mutation.
- `CHECKPOINT_ONLY` records continuity facts and grants no implementation authority.

Do not combine Plan, Act, validation, commit, push, review, cleanup, merge, or deployment into one vague prompt.

## 5. Mandatory section order

After the identity block, use the following section order. Omit a section only when it is factually not applicable, never because it is inconvenient.

```text
OBJECTIVE

CHATGPT-VERIFIED CURRENT FACTS

WHAT HAS ALREADY BEEN COMPLETED

DO NOT REPEAT

MANDATORY CORRECTIONS
or
AUTHORIZED OBJECTIVE

CANONICAL STAGE MAPPING
when the task belongs to an existing Stage 0–13 workflow

THIS ASSIGNMENT AUTHORIZES ONLY

REPOSITORY-PLAN BOUNDARY

MINIMUM-SYSTEM-MUTATION RULE
when the assignment can change the host system, tools, packages, environment, or registry

COMMAND EXECUTION CONTROL
when any command is authorized

STEP 1 — <EXACT_STEP_NAME>

AUTHORIZED EFFECTS
when the step mutates anything

REQUIRED RESULT

STOP IMMEDIATELY IF

STEP 2 — <EXACT_STEP_NAME>
only when separately ordered after STEP 1 succeeds

STRICT REPOSITORY PROHIBITIONS

REQUIRED OUTPUT

FINAL_STATUS

STOP after the output.
```

The prompt must remain readable as an operational instruction. Do not bury the assignment inside a deeply nested generic YAML document.

## 6. Meaning of each mandatory section

### OBJECTIVE

State one exact objective. Name the exact path, artifact, command, receipt, or decision.

Bad:

```text
Fix the project and continue.
```

Required style:

```text
Correct the previously proposed complete Markdown content for the exact named path. Do not create or edit the file. Return the full corrected content for Human Owner review.
```

### CHATGPT-VERIFIED CURRENT FACTS

Include only facts verified from the repository, connector evidence, or an owner-supplied exact receipt.

Normally include:

```yaml
local_worktree:
local_branch:
local_head:
tracked_local_changes:
canonical_branch:
canonical_sha:
current_Draft_PR:
Draft_PR_state:
Draft_PR_head_branch:
remote_head:
active_issue:
current_blocker:
current_stage:
```

Do not silently convert owner-reported local evidence into remote GitHub proof.

### WHAT HAS ALREADY BEEN COMPLETED

List completed actions precisely. Distinguish:

```text
proposed
displayed
approved
executed
saved
validated
committed
pushed
reviewed
accepted
LOCKED_ACCEPTED
```

### DO NOT REPEAT

Explicitly list every completed or rejected action that must not run again.

Examples:

```text
- do not restart repository reconstruction
- do not repeat completed read-only searches
- do not reread the entire repository when the required files were already read for the current receipt
- do not rerun a failed command without a new exact remedy authorization
- do not restore rejected code
- do not repeat an accepted stage
```

### MANDATORY CORRECTIONS

Use this section when Cline must correct proposed content or a previous plan without mutating files.

Number every correction. State exactly what must be removed, preserved, replaced, or reclassified.

### AUTHORIZED OBJECTIVE

Use this section for a bounded read, command, installation, edit, validation, commit, push, or review stage.

State exactly what is authorized. Anything not named remains prohibited.

### CANONICAL STAGE MAPPING

When the task belongs to the repository Stage 0–13 flow, name the current stage and internal substep. Do not invent a replacement workflow.

### THIS ASSIGNMENT AUTHORIZES ONLY

Number the allowed actions. Do not rely on implications.

### REPOSITORY-PLAN BOUNDARY

List work intentionally kept for separate future authorization.

Examples:

```text
- dependency installation
- validation
- uv.lock regeneration
- commit
- push
- PR mutation
- external reviewer trigger
- merge
- deployment
```

### MINIMUM-SYSTEM-MUTATION RULE

For host-system actions, define installation scope, administrator boundary, PATH policy, allowed files, registry policy, package-manager policy, and prohibited environment changes.

### STRICT REPOSITORY PROHIBITIONS

Use explicit verbs and paths. Include all prohibited next stages.

### REQUIRED OUTPUT

Name one exact receipt. List its required fields and allowed status values.

Do not permit an unstructured narrative as the only result.

## 7. Strict command execution control

When commands are authorized, the prompt must contain this rule:

```text
Run exactly one numbered command at a time.

Before every command:

1. Show the exact visible command popup.
2. Wait for Human Owner approval.
3. Keep auto-approval disabled.
4. Do not combine the command with another numbered step.
5. Do not silently continue to the next step.
```

If a command fails:

```text
- stop immediately
- preserve the exact visible command
- preserve the exact exit code
- preserve the exact raw output
- do not improvise another method
- do not repeat automatically
- return the exact blocker to the Human Owner
```

Additional command rules:

- Do not use `&&`, `;`, pipelines, scripts, or wrappers to hide multiple separately governed steps unless the exact single approved command itself requires them.
- Do not propose a next command as though it is already authorized.
- A displayed popup is not execution proof.
- Human approval of one step does not authorize the next step.
- Keep Cline auto-approval, YOLO, browser, and MCP disabled unless separately and exactly authorized.

## 8. Required step format

Every numbered execution step must use this pattern:

```text
STEP <N> — <EXACT_STEP_NAME>

Only after STEP <N-1> passes, run exactly:

<EXACT_COMMAND_OR_EXACT_FILE_ACTION>

AUTHORIZED EFFECTS:

- <EXACT_ALLOWED_EFFECT>

REQUIRED RESULT:

- <EXACT_EXPECTED_RESULT>

STOP IMMEDIATELY IF:

- <EXACT_FAILURE_OR_MISMATCH>
```

No step may contain an undefined phrase such as:

```text
run the needed commands
fix any issue found
continue as appropriate
make the best correction
install required tools
```

## 9. Required final receipt pattern

Every prompt must end with one exact receipt contract:

```text
REQUIRED FINAL RECEIPT:

<EXACT_RECEIPT_NAME>:

assignment_id:
repository:
branch:
starting_head:
actions_completed: []
actions_not_completed: []
commands_run: []
files_read: []
files_created: []
files_edited: []
files_deleted: []
tests_run: []
blockers: []
mutations_performed:
final_status:
next_action:
```

Add task-specific fields instead of replacing the evidence fields.

End with:

```text
STOP after returning the receipt.
Do not continue into another assignment.
```

## 10. Required final status values

Define the exact allowed values inside each prompt. Use only statuses relevant to that assignment.

Examples:

```text
READY_FOR_HUMAN_FILE_CONTENT_REVIEW
PLAN_COMPLETE_AWAITING_HUMAN_OWNER_ACT_AUTHORIZATION
PASS_BOUNDED_ACTION_COMPLETED
PASS_VALIDATION_COMPLETED
BLOCKED_AUTHORITY_CONFLICT
BLOCKED_MISSING_REQUIRED_FACT
BLOCKED_REPOSITORY_STATE_MISMATCH
BLOCKED_COMMAND_FAILED
BLOCKED_UNEXPECTED_MUTATION
CHANGES_REQUIRED
```

Never allow Cline to invent an undefined success status.

## 11. Prohibited old prompt patterns

The following are no longer valid as the primary Cline prompt format:

```text
- the old generic one-line Stage A Cline command
- the old generic one-line Stage B Cline command
- a generic universal header followed by broad prose
- a deeply nested GALAX_AI_ASSIGNMENT_V1 object without the Human Owner section pattern
- placeholders left unresolved
- a prompt copied from an older branch or stage without live-state verification
- a broad instruction to read everything again
- automatic transition from Plan to Act
- automatic transition from one command to the next
- combined edit, validation, commit, and push authority
- inferred authorization from continue, fix, finish, improve, or do everything
- invented exact file content when the evidence says NOT_ESTABLISHED
```

`docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md` is retained only as a compatibility redirect and historical Git record. It is not the canonical Cline prompt-construction template.

## 12. Prompt construction procedure for ChatGPT and every new chat

Use this exact procedure:

```text
reconstruct the repository truth
→ identify the exact current assignment and stage
→ separate completed, rejected, blocked, and pending actions
→ verify live branch, SHA, PR, issue, and supplied local receipt
→ choose one exact assignment mode
→ write the flat assignment identity block
→ write OBJECTIVE
→ write CHATGPT-VERIFIED CURRENT FACTS
→ write WHAT HAS ALREADY BEEN COMPLETED
→ write DO NOT REPEAT
→ write the exact corrections or authorized objective
→ define the repository-plan boundary
→ define one-command-at-a-time control when commands exist
→ define exact numbered steps
→ define strict prohibitions
→ define one exact final receipt
→ define allowed final statuses
→ require STOP
→ compare the finished prompt against this file before giving it to Cline
```

## 13. New-chat receipt before drafting a Cline prompt

A new chat must be able to return:

```yaml
CLINE_PROMPT_CREATION_PATH_RECEIPT_V1:
  repository: ariessocia04-rgb/galax-Ai-project
  repository_access_verified:
  files_read:
    - README.md
    - AGENTS.md
    - docs/operations/CODE_RED.md
    - docs/operations/GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md
    - latest_applicable_checkpoint
    - docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md
    - exact_active_plan_and_assignment
    - docs/prompts/HOW_TO_PROPER_CREATE_PROMPT_FOR_CLINE.md
  live_state_verified:
  owner_supplied_receipt_reviewed:
  completed_actions_identified: []
  actions_that_must_not_be_repeated: []
  proposed_assignment_mode:
  proposed_single_objective:
  commands_batched: false
  automatic_continuation_allowed: false
  exact_receipt_defined:
  safe_to_draft_prompt: false
```

`safe_to_draft_prompt` becomes true only when the facts, scope, mode, and authority are complete.

## 14. Canonical prompt skeleton

Use this skeleton, replacing every placeholder and removing only factually inapplicable sections:

```text
GALAX_AI_ASSIGNMENT_V1

assignment_id: <EXACT_ID>
parent_assignment_id: <EXACT_PARENT_ID_WHEN_APPLICABLE>
parent_plan_id: <EXACT_PLAN_ID_WHEN_APPLICABLE>

contributor: Cline
role: <EXACT_BOUNDED_ROLE>
mode: <EXACT_MODE>
repository: ariessocia04-rgb/galax-Ai-project
branch: <EXACT_BRANCH>

OBJECTIVE

<ONE EXACT OBJECTIVE>

CHATGPT-VERIFIED CURRENT FACTS

<EXACT CURRENT FACTS ONLY>

WHAT HAS ALREADY BEEN COMPLETED

<NUMBERED COMPLETED ACTIONS>

DO NOT REPEAT

<EXPLICIT NON-REPEAT LIST>

MANDATORY CORRECTIONS
or
AUTHORIZED OBJECTIVE

<EXACT NUMBERED REQUIREMENTS>

CANONICAL STAGE MAPPING

<ONLY WHEN APPLICABLE>

THIS ASSIGNMENT AUTHORIZES ONLY

<NUMBERED ALLOWED ACTIONS>

REPOSITORY-PLAN BOUNDARY

<WORK RESERVED FOR SEPARATE AUTHORIZATION>

COMMAND EXECUTION CONTROL

Run exactly one numbered command at a time.
Show the exact popup and wait for Human Owner approval.
Do not enable auto-approval.
Do not combine steps.
Do not silently continue.

STEP 1 — <EXACT NAME>

Run exactly:

<EXACT COMMAND OR ACTION>

AUTHORIZED EFFECTS:

<EXACT EFFECTS>

REQUIRED RESULT:

<EXACT RESULT>

STOP IMMEDIATELY IF:

<EXACT BLOCKERS>

STRICT REPOSITORY PROHIBITIONS

<EXPLICIT PROHIBITIONS>

REQUIRED OUTPUT

<EXACT RECEIPT NAME AND FIELDS>

FINAL_STATUS

Use exactly one:

<ALLOWED STATUS 1>
<ALLOWED STATUS 2>
<ALLOWED STATUS 3>

STOP after the output.
Do not continue into another assignment.
```

## 15. Final authority rule

The Human Owner approves or rejects the prompt and every separately governed execution step.

ChatGPT may inspect the repository, reconstruct facts, and author the exact prompt. ChatGPT must not replace the Human Owner's accepted prompt pattern with an older generic template.

Cline must follow the exact assignment, request manual approval where required, return the required receipt, and stop.