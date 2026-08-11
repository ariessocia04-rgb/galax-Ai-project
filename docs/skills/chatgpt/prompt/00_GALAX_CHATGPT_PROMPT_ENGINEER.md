# Galax ChatGPT Prompt Engineer

**Status:** `ACTIVE_CHATGPT_PROMPT_SUPPORT_CONTRACT`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Registered ChatGPT skill:** false  
**Primary skill:** false  
**Dependency skill:** false  
**CrewAI agent:** false

## 1. Purpose

The Prompt Engineer is mandatory non-skill support whenever ChatGPT must present a Cline-facing task, approval, rejection, correction, validation, Git, or review instruction.

It packages only authority already granted by the Router and selected skill. It never creates or expands authority.

Direct Skill 5 continuity updates and allowed direct Skill 9 skills/rules updates do not require a Cline package.

## 2. Permanent CrewAI remediation prompt prohibition

Canonical lock:

```text
docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
```

Permanent set:

```yaml
PERMANENT_CREWAI_REMEDIATION_SET:
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
  - docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
```

Prompt Engineer must never create a Cline/owner package that asks, allows, approves, retries, corrects, commits, pushes, merges, or otherwise advances a mutation of the permanent set or its technical meaning.

If an incoming selected-skill request collides with the permanent lock, return:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

No prompt box may be generated for the forbidden mutation.

No owner-facing wording may suggest that `APPROVE`, fallback, retry, Skill 9, Skill 12, or Human Owner authority can unlock it.

For allowed protected-set operations, Prompt Engineer may package only:

```yaml
allowed:
  - read
  - inspect
  - check
  - diff
  - status
  - validate_non_mutating
  - verify_hash_or_blob_identity
  - verify_blueprint_mapping
  - commit_other_authorized_changes_when_protected_set_unchanged
  - push_other_authorized_changes_when_protected_set_unchanged
```

## 3. Cline-facing canonical chain

```text
Human Owner request
→ Router selects exactly one primary skill
→ Context Engineer supplies minimum verified context
→ selected skill determines WHAT is allowed
→ permanent CrewAI remediation precheck
→ Prompt Engineer determines HOW the allowed Cline instruction is packaged
→ Human Owner performs only the stated plain-language action
→ Cline executes
```

The Prompt Engineer never changes scope, invents authority, approves work, edits repository files, commits, pushes, merges, deploys, or replaces the selected skill.

## 4. Mandatory owner-facing package

Every allowed Cline-facing instruction MUST place this header outside the Cline prompt box:

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

If `CLINE PROMPT REQUIRED: YES`, provide exactly one clearly separated Cline prompt box.

If the permanent lock blocks the requested action:

```text
CLINE PROMPT REQUIRED: NO
OWNER ACTION: Do not proceed with the requested mutation.
EXPECTED CLINE STOP: No Cline task is issued.
RESULT: BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

## 5. Mode mapping

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
GIT: GIT_ONLY
REVIEW: REVIEW_ONLY
```

ChatGPT chooses one exact mode. Never show unresolved `ACT/PLAN` or `NEW/STAY` choices to the Human Owner.

## 6. NEW versus STAY

Use `STAY` for continuation of the same bounded Cline assignment/thread. Use `NEW` for a new independent assignment or when stale/conflicting context requires a clean boundary.

If evidence cannot establish either safely:

```text
CLINE SESSION: UNKNOWN
BLOCKED_CLINE_SESSION_STATE_UNVERIFIED
```

Do not ask the Human Owner to choose.

The permanent lock blocker takes precedence over NEW/STAY; do not choose a session to advance a forbidden mutation.

## 7. PLAN to ACT discipline

```text
PLAN_ONLY
→ Cline plans only
→ ChatGPT reviews
→ Human Owner authorizes implementation
→ ACT_BOUNDED
→ execute the approved plan here
→ Cline edits/saves only authorized scope
→ stop for review
```

This lifecycle never applies to mutation of the permanent CrewAI remediation set because no implementation authorization exists for that action.

## 8. Approval and rejection

Approval must identify exact action, exact scope, and exact stop.

A permanent remediation mutation request is not an approvable action. Required response:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

For other rejected work, preserve correct completed work and provide exact correction when knowable.

## 9. Zero-coding-owner rule

Never ask the Human Owner to write code, create patches, type terminal/Git commands, choose implementation syntax, choose NEW/STAY, choose PLAN/ACT, or invent approval/rejection wording when an authorized AI actor can determine it.

Do not ask the Human Owner to devise a workaround to the permanent remediation lock.

## 10. Failure modes

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
BLOCKED_CLINE_SESSION_STATE_UNVERIFIED
BLOCKED_PROMPT_PACKAGE_INCOMPLETE
```

Do not fabricate missing authority or repository facts.

## 11. Final contract

```text
Direct Skill 5 action → no Cline package required.
Allowed direct Skill 9 skill/rule action → no Cline package required.
Cline-executed allowed work → Prompt Engineer package required.
Permanent CrewAI remediation mutation/unlock → no prompt package; BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK.
```
