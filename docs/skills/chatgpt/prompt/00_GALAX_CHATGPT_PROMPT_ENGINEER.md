# Galax ChatGPT Prompt Engineer

**Status:** `ACTIVE_CHATGPT_PROMPT_SUPPORT_CONTRACT`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Registered ChatGPT skill:** false  
**Primary skill:** false  
**Dependency skill:** false  
**CrewAI agent:** false  
**Final authority:** Human Owner

## 1. Purpose

The Prompt Engineer is mandatory non-skill support whenever ChatGPT must present a **Cline-facing** task, approval, rejection, correction, validation instruction, Git instruction, or review instruction.

It is not required for direct ChatGPT repository actions under:

```yaml
Skill_5:
  - update_length_problem_in_repo
  - update_achievement_in_repo
  - qualifying_achievement_persistence

Skill_9:
  - edit_or_update_ChatGPT_skills_and_rules_only
  allowed_path_prefixes:
    - docs/skills/chatgpt/
    - docs/rules/
```

For those exact scopes, Cline is not the executor.

## 2. Cline-facing canonical chain

```text
Human Owner request
→ Router selects exactly one primary skill
→ Context Engineer supplies minimum verified context
→ selected skill determines WHAT is allowed
→ Prompt Engineer determines HOW the Cline instruction is packaged
→ Human Owner performs only the stated plain-language action
→ Cline executes
```

The Prompt Engineer never changes scope, invents authority, approves work, edits repository files, commits, pushes, merges, deploys, or replaces the selected skill.

## 3. Mandatory owner-facing package

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

If `CLINE PROMPT REQUIRED: YES`, provide exactly one clearly separated Cline prompt box.

## 4. Mode mapping

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
GIT: GIT_ONLY
REVIEW: REVIEW_ONLY
```

ChatGPT chooses one exact mode. Never show unresolved `ACT/PLAN` or `NEW/STAY` choices to the Human Owner.

## 5. NEW versus STAY

Use `STAY` for continuation of the same bounded Cline assignment/thread. Use `NEW` for a new independent assignment or when stale/conflicting context requires a clean boundary.

If evidence cannot establish either safely:

```text
CLINE SESSION: UNKNOWN
BLOCKED_CLINE_SESSION_STATE_UNVERIFIED
```

Do not ask the Human Owner to choose.

## 6. PLAN to ACT discipline

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

The phrase `execute the approved plan here` must not authorize execution while canonical mode is `PLAN_ONLY`.

## 7. Approval and rejection

Approval must identify exact action, exact scope, and exact stop. Rejection must preserve correct work and provide the exact correction when knowable. Bare rejection is prohibited when a safe exact correction can be stated.

## 8. Zero-coding-owner rule

Never ask the Human Owner to write code, create patches, type terminal/Git commands, choose implementation syntax, choose NEW/STAY, choose PLAN/ACT, or invent approval/rejection wording when an authorized AI actor can determine it.

## 9. Final contract

```text
Direct Skill 5 action → no Cline package required.
Direct Skill 9 skill/rule action → no Cline package required.
Cline-executed work → Prompt Engineer package required.
```
