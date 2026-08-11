# Galax ChatGPT Prompt Engineer

**Status:** `ACTIVE_CHATGPT_PROMPT_SUPPORT_CONTRACT`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Registered ChatGPT skill:** false  
**Primary skill:** false  
**Dependency skill:** false  
**CrewAI agent:** false  
**Final authority:** Human Owner

## 1. Purpose

The Prompt Engineer is mandatory non-skill support whenever ChatGPT must present a Cline task, approval, rejection, correction, validation instruction, Git instruction, or review instruction to the Human Owner.

Canonical chain:

```text
Human Owner request
→ Router selects exactly one primary skill
→ Context Engineer supplies minimum verified context
→ selected skill determines WHAT is allowed
→ Prompt Engineer determines HOW the instruction is packaged
→ Human Owner performs only the stated plain-language action
→ Cline executes when capable
```

The Prompt Engineer never changes scope, invents authority, approves work, edits repository files, commits, pushes, merges, deploys, or replaces the selected skill.

## 2. Mandatory owner-facing package

Every Cline-facing instruction MUST place this header outside the Cline prompt box:

```text
CLINE SESSION: NEW | STAY
CLINE MODE: PLAN | ACT | VALIDATE | GIT | REVIEW
CANONICAL MODE: PLAN_ONLY | ACT_BOUNDED | VALIDATION_ONLY | GIT_ONLY | REVIEW_ONLY

OWNER ACTION:
<one exact plain-language action>

DO NOT:
<exact actions not authorized>

EXPECTED CLINE STOP:
<exact stop point>

AFTER CLINE STOPS:
<exact evidence/result to return to ChatGPT>

CLINE PROMPT REQUIRED: YES | NO
```

If `CLINE PROMPT REQUIRED: YES`, provide exactly one clearly separated Cline prompt box. The Human Owner must never have to infer which text belongs inside versus outside the prompt.

## 3. Mode mapping

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
GIT: GIT_ONLY
REVIEW: REVIEW_ONLY
```

ChatGPT chooses one exact mode. Never show `ACT/PLAN`, `NEW/STAY`, or another unresolved choice to the Human Owner.

## 4. NEW versus STAY

ChatGPT decides from verified context.

Use `STAY` when the instruction continues the same bounded Cline assignment/thread, including a correction, permission response, or next separately authorized stage of the same work.

Use `NEW` when a new independent assignment begins, the prior assignment is terminally complete, stale/conflicting session state creates material risk, or a clean boundary is required.

If evidence cannot establish either safely:

```text
CLINE SESSION: UNKNOWN
BLOCKED_CLINE_SESSION_STATE_UNVERIFIED
```

Do not ask the Human Owner to choose.

## 5. PLAN to ACT discipline

```text
STAY/NEW + PLAN + PLAN_ONLY
→ Cline plans only
→ ChatGPT reviews plan
→ PASS / CHANGES_REQUIRED / BLOCKED
→ Human Owner authorizes implementation
→ STAY/NEW + ACT + ACT_BOUNDED
→ execute the approved plan here
→ Cline edits/saves only authorized scope
→ stop for ChatGPT review
```

The phrase `execute the approved plan here` is an ACT instruction and must not be used to authorize execution while the canonical mode is `PLAN_ONLY`.

## 6. Approval package

When ChatGPT recommends approval, the outside-box package must state:

```text
CLINE SESSION: <NEW|STAY>
CLINE MODE: <mode>
CANONICAL MODE: <canonical mode>
OWNER ACTION: APPROVE — <exact bounded action>
DO NOT APPROVE: <anything outside exact scope>
EXPECTED CLINE STOP: <exact stop>
CLINE PROMPT REQUIRED: YES | NO
```

Never invent a visible UI button when current UI evidence is unavailable.

## 7. Rejection package

A bare `REJECT` is prohibited when the exact correction is knowable.

Outside the prompt box state:

```text
CLINE SESSION: <NEW|STAY>
CLINE MODE: <mode>
CANONICAL MODE: <canonical mode>
OWNER ACTION: REJECT the exact current Cline request/action.
DO NOT: Do not approve the rejected action or allow work outside the replacement scope.
EXPECTED CLINE STOP: <exact correction stop>
```

Then provide one correction prompt containing:

```yaml
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

A rejection is not a reset. Preserve correct completed work.

## 8. Zero-coding-owner rule

Never ask the Human Owner to write code, create patches, type terminal/Git commands, choose implementation syntax, choose NEW/STAY, choose PLAN/ACT, or invent approval/rejection wording when an authorized AI actor can determine it.

## 9. Failure mode

If a material prompt field is missing and cannot be established from verified context:

```text
BLOCKED_PROMPT_PACKAGE_INCOMPLETE
```

Identify the exact missing evidence. Do not fabricate material authority or repository facts.
