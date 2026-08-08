# Galax Cline Prompt Task Continuity Declaration Rule

**Status:** `ACTIVE_ADDITIVE_CHATGPT_PROMPT_RULE`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Applies to:** `$galax-strict-cline-prompt-guardian` / GALAX-SKILL-02  
**Rule type:** additive prompt-presentation and task-continuity rule  
**Registered ChatGPT skill:** false  
**Dependency skill:** false  
**CrewAI runtime effect:** none  
**Replaces existing Skill 2 rules:** false  
**Human Owner final authority:** true

## 1. Purpose

This rule is an **additive extension** to the existing Galax Strict Cline Prompt Guardian. It does not replace, renumber, weaken, or delete any existing Skill 2 rule.

Its purpose is to make every Cline prompt visibly declare whether the next bounded prompt is:

- a continuation of the **same Galax assignment/task**; or
- a genuinely **new Galax assignment/task**.

A change of Cline mode, bounded stage, retry suffix, review step, save gate, validation gate, or Git gate does **not by itself** create a new Galax assignment.

## 2. Mandatory pre-prompt declaration

Before presenting any `GALAX_CLINE_TASK_V2` prompt to the Human Owner, ChatGPT must first classify the prompt as exactly one of:

```yaml
TASK_CONTINUITY_DECLARATION_V1:
  task_classification: SAME_TASK | NEW_TASK
  parent_assignment:
  current_bounded_stage:
  mode: PLAN_ONLY | ACT_BOUNDED | REVIEW_ONLY | VALIDATION_ONLY | GIT_ONLY
  create_new_Galax_assignment: true | false
  reason:
```

This declaration is user-facing and must appear immediately before the Cline prompt.

## 3. SAME_TASK rule

Use `SAME_TASK` when the prompt continues the same parent Galax assignment, objective, target, or correction chain.

Examples include:

- `PLAN_ONLY` analysis followed by an approved preview;
- `PLAN_ONLY` to `ACT_BOUNDED` for the same target;
- save authorization for an already-approved preview;
- a bounded fallback for the same authorized edit;
- a read-only post-command verification for the same target;
- `REVIEW_ONLY` evidence review for the same assignment;
- `VALIDATION_ONLY` for the same saved bounded change;
- `GIT_ONLY` commit or push steps for the same accepted bounded unit;
- retry suffixes such as `R1`, `R2`, or correction stages within the same assignment;
- stage labels such as `P2G`, `P2H`, `P2H-R1`, and `P2H-R2` when they remain inside the same parent assignment.

Required user-facing wording:

```text
SAME TASK — huwag lumipat o gumawa ng bagong Galax task. I-paste kay Cline:
```

Required classification:

```yaml
task_classification: SAME_TASK
create_new_Galax_assignment: false
```

Changing only the Cline mode does not change this classification.

Example:

```yaml
TASK_CONTINUITY_DECLARATION_V1:
  task_classification: SAME_TASK
  parent_assignment: Assignment_060
  current_bounded_stage: P2H-R2
  mode: REVIEW_ONLY
  create_new_Galax_assignment: false
  reason: >-
    This is a bounded continuation of Assignment 060 for the same target,
    not a new independent Galax objective.
```

Then present the existing bounded prompt, for example:

```text
# GALAX_CLINE_TASK_V2 — Assignment 060 P2H-R2
```

Do not rename the same parent assignment merely because a new bounded stage is required.

## 4. NEW_TASK rule

Use `NEW_TASK` only when there is a genuinely new independent Galax objective or target that should begin a new parent assignment.

A new task may be classified only when at least one of the following is true:

- the previous parent assignment is complete/stopped and the next objective is independent;
- the Human Owner explicitly creates or authorizes a new parent assignment;
- the new work targets a materially different independent objective that is not a bounded continuation, correction, review, validation, save, or Git stage of the current assignment;
- repository authority explicitly identifies the next work as a new assignment.

Required user-facing wording:

```text
NEW TASK — gumawa ng bagong Galax task. Mode: <MODE>. I-paste kay Cline:
```

Required classification:

```yaml
task_classification: NEW_TASK
create_new_Galax_assignment: true
```

Example:

```yaml
TASK_CONTINUITY_DECLARATION_V1:
  task_classification: NEW_TASK
  parent_assignment: Assignment_061
  current_bounded_stage: P2A
  mode: PLAN_ONLY
  create_new_Galax_assignment: true
  reason: >-
    Assignment 060 is stopped/completed and this is a different independent
    objective requiring a new parent assignment.
```

Then present the new bounded prompt, for example:

```text
# GALAX_CLINE_TASK_V2 — Assignment 061 P2A
```

## 5. Anti-false-new-task rule

ChatGPT must not label a prompt `NEW_TASK` merely because:

- a new chat message was received;
- Cline requested permission;
- the mode changed;
- a preview was approved;
- a save gate was opened;
- a command failed;
- a retry suffix was added;
- a review or verification read became necessary;
- a focused test is separately authorized;
- commit and push are separately gated;
- the bounded prompt has a new unique `assignment_id` field for receipt tracking while still belonging to the same parent Galax assignment.

The parent Galax assignment identity and independent objective control the classification, not the number of Cline prompts.

## 6. Do-not-create-new-task instruction

For every `SAME_TASK` prompt, the prompt must preserve a clear boundary equivalent to:

```yaml
task_continuity:
  parent_assignment: <CURRENT_PARENT_ASSIGNMENT>
  classification: SAME_TASK
  create_new_Galax_assignment: false
  do_not_switch_to_new_task: true
```

The prompt should also preserve completed work, locks, actions not to repeat, current stage, and exact stop condition under the existing Skill 2 rules.

## 7. New-task mode declaration

For every true `NEW_TASK`, ChatGPT must explicitly state the selected Cline mode before the prompt:

```text
NEW TASK — gumawa ng bagong Galax task. Mode: PLAN_ONLY. I-paste kay Cline:
```

or, only when the exact edit/save authority already exists:

```text
NEW TASK — gumawa ng bagong Galax task. Mode: ACT_BOUNDED. I-paste kay Cline:
```

The mode must still satisfy the existing Skill 2 mode-selection and authorization rules. This additive rule grants no implementation authority by itself.

## 8. Relationship to existing Skill 2 rules

This file is additive only.

It does not replace or weaken:

- repository-state reconstruction;
- one task / one goal / one stop condition;
- mode selection;
- exact allowlists;
- locked-artifact protection;
- permission review;
- complete visible diff requirements;
- separate save, validation, Git, merge, or deployment authorization;
- Human Owner final authority.

When this rule and Skill 2 are both applicable:

```text
existing Skill 2 safety and authorization rules
+ this task-continuity declaration rule
→ one correctly classified, explicitly labeled bounded Cline prompt
```

## 9. Required presentation examples

### Same parent assignment

```text
SAME TASK — huwag lumipat o gumawa ng bagong Galax task. I-paste kay Cline:

# GALAX_CLINE_TASK_V2 — Assignment 060 P2H-R2
```

Even if the mode changes from `PLAN_ONLY` to `ACT_BOUNDED`, `REVIEW_ONLY`, `VALIDATION_ONLY`, or `GIT_ONLY`, keep `SAME_TASK` while the same parent assignment/objective continues.

### Genuine new parent assignment

```text
NEW TASK — gumawa ng bagong Galax task. Mode: PLAN_ONLY. I-paste kay Cline:

# GALAX_CLINE_TASK_V2 — Assignment 061 P2A
```

Do not reuse an old parent assignment number merely to make a genuinely independent objective look like a continuation.

## 10. Stop condition

After classifying and presenting the one bounded prompt, stop at the existing Skill 2 boundary.

This rule does not authorize ChatGPT or Cline to automatically continue to another stage, create another assignment, edit, save, test, run commands, commit, push, merge, or deploy.
