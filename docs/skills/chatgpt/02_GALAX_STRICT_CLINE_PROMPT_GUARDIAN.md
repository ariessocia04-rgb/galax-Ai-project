```yaml
skill_reference: $galax-strict-cline-prompt-guardian
skill_id: GALAX-SKILL-02
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 2: Galax Strict Cline Prompt Guardian

## 1. Purpose

Skill 2 controls how ChatGPT gives bounded work to Cline whenever Cline is the authorized executor. It is no longer limited to CrewAI source implementation.

```text
Human Owner
→ ChatGPT determines exact next action
→ Context Engineer supplies verified context
→ Skill 2 fixes exact scope/mode/permissions/stop
→ Prompt Engineer packages the Human Owner + Cline instruction
→ Cline executes when capable
→ ChatGPT reviews evidence
→ Human Owner controls the next consequential stage
```

Skill 10 remains mandatory only for active CrewAI remediation-blueprint implementation tasks.

## 2. Cline-default executor rule

```yaml
Cline:
  default_repository_executor_when_capable: true
  edit_save: only_when_authorized
  validation: only_when_separately_authorized
  commit: only_when_separately_authorized
  push: only_when_separately_authorized
  self_authorization: prohibited
  automatic_scope_expansion: prohibited
  automatic_next_stage: prohibited

ChatGPT:
  architect_specification_supervisor_reviewer: true
  normal_repository_execution: prohibited_when_Cline_capable
  normal_commit: prohibited_when_Cline_capable
  normal_push: prohibited_when_Cline_capable
```

If Cline is capable and ChatGPT attempts takeover:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

Skill 12 is the only fallback exception.

## 3. Zero-coding-owner rule

Never ask the Human Owner to write code, edit files, type terminal/Git commands, choose NEW/STAY, choose PLAN/ACT, or invent technical approval/rejection wording when ChatGPT can determine it and Cline can execute it.

## 4. Mandatory Context Engineer + Prompt Engineer chain

Before emitting a real Cline instruction:

```text
verify repository-backed state
→ Context Engineer builds minimum lossless context
→ Skill 2 determines exact task/mode/scope
→ Prompt Engineer emits final package
```

Required support files:

```text
docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md
docs/skills/chatgpt/prompt/00_GALAX_CHATGPT_PROMPT_ENGINEER.md
```

## 5. Mandatory owner-facing format

Every Cline instruction must state outside the prompt box:

```text
CLINE SESSION: NEW | STAY
CLINE MODE: PLAN | ACT | VALIDATE | GIT | REVIEW
CANONICAL MODE: PLAN_ONLY | ACT_BOUNDED | VALIDATION_ONLY | GIT_ONLY | REVIEW_ONLY
OWNER ACTION: <one exact plain-language action>
DO NOT: <exact prohibitions>
EXPECTED CLINE STOP: <exact stop>
AFTER CLINE STOPS: <exact evidence to return>
CLINE PROMPT REQUIRED: YES | NO
```

ChatGPT chooses exactly one session and one mode. Never present `NEW/STAY`, `ACT/PLAN`, or similar unresolved choices to the Human Owner.

Mode mapping:

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
GIT: GIT_ONLY
REVIEW: REVIEW_ONLY
```

## 6. NEW/STAY rule

Use `STAY` for the same bounded Cline assignment/thread, including corrections, permission responses, or the next separately authorized stage of the same coherent work.

Use `NEW` for a new independent assignment, terminally completed prior work, materially stale/conflicting session state, or when a clean boundary is required.

If not safely verifiable:

```text
CLINE SESSION: UNKNOWN
BLOCKED_CLINE_SESSION_STATE_UNVERIFIED
```

Do not ask the Human Owner to decide.

## 7. Modes

### PLAN_ONLY

Reads/searches/analysis/plan only. No mutation, tests, formatter, dependency action, Git mutation, or implementation.

### ACT_BOUNDED

One exact authorized edit/action. No implicit validation, commit, push, merge, or deploy.

### VALIDATION_ONLY

Run only the exact authorized validation command. No automatic fix/retry/additional tests.

### GIT_ONLY

One exact Git stage. Commit and push are separate by default.

### REVIEW_ONLY

Inspect exact evidence/diff/receipt only. No mutation.

## 8. PLAN to ACT contract

```text
PLAN_ONLY
→ Cline returns plan
→ ChatGPT reviews
→ PASS / CHANGES_REQUIRED / BLOCKED
→ Human Owner authorizes implementation
→ ACT_BOUNDED
→ "execute the approved plan here"
→ Cline edits/saves
→ stop for review
```

`execute the approved plan here` must never authorize execution during PLAN_ONLY.

## 9. Mandatory task schema

```yaml
GALAX_CLINE_TASK_V4:
  assignment_id:
  repository: ariessocia04-rgb/galax-Ai-project
  workspace:
  branch:
  expected_head_sha:
  contributor: Cline
  mode: PLAN_ONLY | ACT_BOUNDED | VALIDATION_ONLY | GIT_ONLY | REVIEW_ONLY
  authority_source:
  human_authorized: true | false
  primary_skill:
  Skill_10_gate_when_CrewAI_blueprint_task:
  objective:
  verified_context: []
  completed_work_to_preserve: []
  LOCKED_ACCEPTED_to_preserve: []
  do_not_repeat: []
  allowed_reads: []
  allowed_searches: []
  allowed_edits: []
  allowed_commands: []
  prohibited_paths: []
  prohibited_actions: []
  validation_authority:
  commit_authority:
  push_authority:
  stop_condition:
  required_receipt:
```

Material fields must not be vague.

## 10. Approval package

When recommending approval, Prompt Engineer must render:

```text
CLINE SESSION: <NEW|STAY>
CLINE MODE: <mode>
CANONICAL MODE: <canonical mode>
OWNER ACTION: APPROVE — <exact bounded action>
DO NOT APPROVE: <outside scope>
EXPECTED CLINE STOP: <exact stop>
CLINE PROMPT REQUIRED: YES | NO
```

## 11. Rejection package

Bare rejection is prohibited when the correction is knowable.

Required correction data:

```yaml
GALAX_CLINE_REJECTION_WITH_CORRECTION_V3:
  decision: REJECT
  factual_reason:
  retain_unchanged: []
  existing_LOCKED_ACCEPTED_to_preserve: []
  verified_completed_work_to_preserve: []
  verified_ChatGPT_fallback_work_to_preserve: []
  correction_scope_frozen: []
  rejected_part:
  exact_replacement_instruction:
  allowed_reads: []
  allowed_edits: []
  allowed_commands: []
  prohibited_paths: []
  prohibited_actions: []
  stop_condition:
  requires_new_Human_Owner_authorization: true | false
```

A rejection never resets correct work.

## 12. CrewAI Skill 10 gate

For active CrewAI remediation-blueprint implementation only:

```text
load Skill 10
→ require PASS_CLINE_BLUEPRINT_ONLY
→ then emit the bounded Cline task
```

Governance, router, skills, continuity, Prompt Engineer, Context Engineer, and documentation edits are not blocked merely because they are not blueprint implementation.

## 13. Commit and push

```text
local PASS
→ STOP
→ Human Owner authorizes COMMIT
→ GIT_ONLY commit task
→ Cline commit
→ STOP
→ Human Owner separately authorizes PUSH
→ GIT_ONLY push task
→ Cline push
→ STOP
→ ChatGPT remote review
→ Human Owner final acceptance
```

No automatic commit or push.

## 14. Fallback handoff

If Cline factually cannot perform the exact action or the repeated-mismatch gate qualifies, Skill 2 stops and Router may select Skill 12. Skill 2 never silently turns ChatGPT into the executor.
