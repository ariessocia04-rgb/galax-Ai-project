# Galax ChatGPT / Cline Execution Role Separator

**Status:** `ACTIVE_CANONICAL_HUMAN_OWNER_CONTRIBUTOR_BOUNDARY`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`

## 1. Highest-priority permanent CrewAI remediation boundary

The Human Owner has established a permanent immutable CrewAI remediation set with no unlock path.

Canonical lock:

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

No actor may edit, rewrite, delete, rename, reformat, replace, supersede, reinterpret, weaken, unlock, or indirectly change the technical meaning of this set.

This includes the Human Owner, ChatGPT, Cline, Skill 9, Skill 12, other assistants, contributors, and automated workflows.

Required result for any mutation/unlock attempt:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

No later Human Owner instruction constitutes an unlock.

## 2. Allowed operations on permanent set

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

Commit/push may proceed only when the protected set and its technical meaning remain unchanged.

Validation must not format, fix, regenerate, normalize, or rewrite protected files.

## 3. Exact standing ChatGPT repository jobs outside permanent lock

```yaml
CHATGPT_STANDING_REPOSITORY_JOBS:
  job_1:
    name: update_length_problem_in_repo
    authority: Skill_5
    executor: ChatGPT

  job_2:
    name: edit_or_update_ChatGPT_skills_and_rules_only
    authority: Skill_9
    executor: ChatGPT
    allowed_path_prefixes:
      - docs/skills/chatgpt/
      - docs/rules/
    permanent_CrewAI_remediation_lock_override: prohibited

  job_3:
    name: update_achievement_in_repo
    authority: Skill_5
    executor: ChatGPT
```

These are standing direct ChatGPT responsibilities only when they do not violate the permanent remediation lock.

## 4. Skill 5 continuity exception

Skill 5 directly authorizes ChatGPT to create/update exact length-problem and achievement continuity records within Skill 5 boundaries.

```text
Router selects Skill 5
→ Context Engineer supplies verified evidence
→ Skill 5 determines exact content/target/dedupe/numbering/timestamp/evidence class
→ ChatGPT directly persists exact continuity record
→ ChatGPT verifies resulting remote evidence
→ stop
```

## 5. Skill 9 skill/rule exception

Skill 9 directly authorizes ChatGPT to edit/update allowed rule content under:

```text
docs/skills/chatgpt/**
docs/rules/**
```

But Skill 9 must first apply the permanent remediation lock.

It may not edit the permanent focus lock or create/edit another rule that changes the protected remediation technical meaning.

Required blocker on collision:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

## 6. General repository execution

Outside exact Skill 5 continuity, allowed Skill 9 skill/rule scope, and permanent-lock blocked work:

```text
Human Owner
→ ChatGPT decides/specifies
→ Router selects one primary skill
→ Context Engineer supplies minimum verified context
→ selected skill determines exact authority/scope/mode
→ Prompt Engineer packages Cline instruction when needed
→ Cline executes whenever capable
→ ChatGPT reviews evidence
→ Human Owner separately authorizes COMMIT
→ Cline commit → STOP
→ Human Owner separately authorizes PUSH
→ Cline push → STOP
→ ChatGPT exact remote review
→ Human Owner final acceptance
```

If Cline is capable outside standing Skill 5/Skill 9 scopes:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

## 7. Skill 12 fallback

Outside standing Skill 5/Skill 9 scopes, ChatGPT may directly execute other repository work only through a separately passing Skill 12 fallback gate with explicit Human Owner authorization.

Skill 12 cannot override the permanent remediation lock.

## 8. Human Owner zero-coding rule

Never require the Human Owner to write code, patch files, type terminal/Git commands, resolve syntax, choose NEW/STAY, choose PLAN/ACT, or invent technical approval/rejection wording when an authorized AI actor can perform the task.

For permanent remediation mutation/unlock requests, the system blocks the request instead of asking the owner to perform it manually.

## 9. Consequential-stage separation for Cline work

```text
PLAN ≠ ACT
ACT ≠ VALIDATE
VALIDATE ≠ FIX
FIX ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE REVIEW
REMOTE REVIEW ≠ HUMAN ACCEPTANCE
MERGE ≠ DEPLOY
```

## 10. Final strict rule

```text
Permanent CrewAI remediation blueprint / focus-lock rule / Foundation narrow supersession
→ READ / CHECK / NON-MUTATING VALIDATION ONLY.
→ NO EDIT.
→ NO UNLOCK.
→ NO EXCEPTION, INCLUDING HUMAN OWNER.
→ COMMIT/PUSH only when protected set remains unchanged.
→ mutation attempt = BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK.

ChatGPT standing jobs outside that permanent lock:
1. Update length problem in repo → Skill 5.
2. Edit/update allowed ChatGPT skills and rules only → Skill 9.
3. Update achievement in repo → Skill 5.

Everything else and Cline capable
→ Cline executes.

Other direct ChatGPT execution
→ Skill 12 only after verified gate + explicit Human Owner authorization, never to override permanent remediation lock.
```
