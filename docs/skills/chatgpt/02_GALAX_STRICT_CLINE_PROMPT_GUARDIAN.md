```yaml
skill_reference: $galax-strict-cline-prompt-guardian
skill_id: GALAX-SKILL-02
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 2: Galax Strict Cline Prompt Guardian

## 1. Purpose

Skill 2 controls bounded work given to Cline **only when Cline is the authorized executor**.

It does not apply to direct Skill 5 continuity updates or direct Skill 9 skill/rule updates because those exact standing scopes use ChatGPT as executor.

## 2. Executor rule

```yaml
standing_ChatGPT_direct_scopes:
  Skill_5:
    - update_length_problem
    - update_achievement
    - qualifying_achievement_persistence
  Skill_9:
    allowed_path_prefixes:
      - docs/skills/chatgpt/
      - docs/rules/
    actions:
      - edit_rule_content
      - update_rule_content

Cline:
  default_repository_executor_when_capable_outside_standing_ChatGPT_scopes: true
  edit_save: only_when_authorized
  validation: only_when_separately_authorized
  commit: only_when_separately_authorized
  push: only_when_separately_authorized
  self_authorization: prohibited
  automatic_scope_expansion: prohibited
  automatic_next_stage: prohibited
```

If Cline is capable for work outside Skill 5/Skill 9 standing scopes and ChatGPT attempts takeover:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

Skill 12 is the fallback for other direct ChatGPT execution.

## 3. Mandatory Cline package chain

When Cline is executor:

```text
Human Owner request
→ Context Engineer supplies verified context
→ Skill 2 fixes exact scope/mode/permissions/stop
→ Prompt Engineer packages the Human Owner + Cline instruction
→ Cline executes
→ ChatGPT reviews evidence
→ Human Owner controls next consequential stage
```

Skill 10 remains mandatory only for active CrewAI remediation-blueprint implementation tasks.

## 4. Mandatory owner-facing format

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

ChatGPT chooses exactly one session and one mode.

```yaml
PLAN: PLAN_ONLY
ACT: ACT_BOUNDED
VALIDATE: VALIDATION_ONLY
GIT: GIT_ONLY
REVIEW: REVIEW_ONLY
```

## 5. NEW/STAY rule

Use `STAY` for the same bounded Cline assignment/thread. Use `NEW` for a new independent assignment or when stale/conflicting context requires a clean boundary.

If not safely verifiable:

```text
CLINE SESSION: UNKNOWN
BLOCKED_CLINE_SESSION_STATE_UNVERIFIED
```

Do not ask the Human Owner to decide.

## 6. PLAN to ACT rule

```text
PLAN_ONLY
→ Cline returns plan
→ ChatGPT reviews
→ Human Owner authorizes implementation
→ ACT_BOUNDED
→ execute the approved plan here
→ Cline edits/saves exact scope
→ stop for review
```

Never use `execute the approved plan here` during PLAN_ONLY.

## 7. Consequential stages

```text
PLAN ≠ ACT
ACT ≠ VALIDATION
VALIDATION ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE REVIEW
```

No automatic next stage.

## 8. Zero-coding-owner rule

Never ask the Human Owner to write code, manually edit files, type terminal/Git commands, choose NEW/STAY, choose PLAN/ACT, or invent technical approval/rejection wording.

## 9. Final contract

```text
Skill 5 direct scope → ChatGPT executes.
Skill 9 direct skill/rule scope → ChatGPT executes.
Other work and Cline capable → Skill 2 packages Cline execution.
Other ChatGPT execution → Skill 12 only after verified gate and owner authorization.
```
