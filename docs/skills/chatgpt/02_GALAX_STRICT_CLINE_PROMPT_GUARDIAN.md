```yaml
skill_reference: $galax-strict-cline-prompt-guardian
skill_id: GALAX-SKILL-02
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 2: Galax Strict Cline Prompt Guardian

## 1. Purpose

Skill 2 controls bounded work given to Cline **only when Cline is the authorized executor**.

It does not apply to direct Skill 5 continuity updates or allowed direct Skill 9 skill/rule updates because those exact standing scopes use ChatGPT as executor.

It can never authorize Cline to mutate the permanent CrewAI remediation immutable set.

## 2. Highest-priority permanent remediation precheck

Before any Cline task is planned, approved, corrected, validated, committed, or pushed, check:

```text
docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
```

Protected set:

```yaml
PERMANENT_CREWAI_REMEDIATION_SET:
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
  - docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
```

If the proposed Cline task would directly or indirectly edit, rewrite, delete, rename, reformat, replace, supersede, reinterpret, weaken, unlock, or alter the technical meaning of this set:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

and do not emit a Cline task.

This blocker applies even when the Human Owner asks for the mutation.

## 3. Allowed Cline interaction with permanent set

Only:

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

Validation must not auto-fix, format, regenerate, normalize, or rewrite protected artifacts.

Commit/push tasks must prove the protected set remains unchanged before proceeding.

## 4. Executor rule outside permanent lock

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
    permanent_CrewAI_remediation_lock_override: prohibited

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

If Cline is capable for non-protected work outside Skill 5/Skill 9 standing scopes and ChatGPT attempts takeover:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

## 5. Mandatory Cline package chain

When Cline is executor and the permanent-lock precheck passes:

```text
Human Owner request
→ Context Engineer supplies verified context
→ Skill 2 fixes exact scope/mode/permissions/stop
→ Prompt Engineer packages Human Owner + Cline instruction
→ Cline executes
→ ChatGPT reviews evidence
→ Human Owner controls next consequential stage
```

Skill 10 remains mandatory for active CrewAI remediation-blueprint implementation tasks.

## 6. Mandatory owner-facing format

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

## 7. NEW/STAY and PLAN/ACT

Use `STAY` for the same bounded Cline assignment/thread. Use `NEW` for a new independent assignment or when stale/conflicting context requires a clean boundary.

If not safely verifiable:

```text
CLINE SESSION: UNKNOWN
BLOCKED_CLINE_SESSION_STATE_UNVERIFIED
```

Planning sequence:

```text
PLAN_ONLY
→ Cline returns plan
→ ChatGPT reviews
→ Human Owner authorizes implementation
→ ACT_BOUNDED
→ execute the approved plan here
→ Cline edits/saves exact non-protected scope
→ stop for review
```

Never use `execute the approved plan here` during PLAN_ONLY.

## 8. Consequential stages

```text
PLAN ≠ ACT
ACT ≠ VALIDATION
VALIDATION ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE REVIEW
```

No automatic next stage.

## 9. Zero-coding-owner rule

Never ask the Human Owner to write code, manually edit files, type terminal/Git commands, choose NEW/STAY, choose PLAN/ACT, or invent technical approval/rejection wording.

For the permanent remediation set, a Human Owner edit/unlock request is blocked rather than converted into a Cline task.

## 10. Final contract

```text
Permanent CrewAI remediation mutation/unlock request
→ BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
→ no Cline prompt.

Permanent set read/check/non-mutating validation
→ allowed when narrowly required.

Commit/push
→ allowed only when protected set remains unchanged.

Skill 5 direct scope → ChatGPT executes.
Allowed non-protected Skill 9 direct scope → ChatGPT executes.
Other non-protected work and Cline capable → Skill 2 packages Cline execution.
Other direct ChatGPT execution → Skill 12 only after verified gate and owner authorization, never to override permanent lock.
```
