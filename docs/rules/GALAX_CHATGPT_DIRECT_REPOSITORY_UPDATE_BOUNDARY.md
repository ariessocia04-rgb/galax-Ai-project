# Galax ChatGPT / Cline Execution Role Separator

**Status:** `ACTIVE_CANONICAL_HUMAN_OWNER_CONTRIBUTOR_BOUNDARY`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Final authority:** Human Owner

## 1. Canonical rule

Galax uses Cline-default execution for general repository work, with exactly two standing non-fallback direct ChatGPT repository scopes that implement three Human Owner jobs.

## 2. Exact standing ChatGPT repository jobs

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

  job_3:
    name: update_achievement_in_repo
    authority: Skill_5
    executor: ChatGPT
```

These are standing direct ChatGPT responsibilities. Cline is not required for these exact scopes.

## 3. Skill 5 continuity exception

Skill 5 directly authorizes ChatGPT to create/update exact length-problem and achievement continuity records within Skill 5's continuity boundaries.

```text
Router selects Skill 5
→ Context Engineer supplies verified evidence
→ Skill 5 determines exact content/target/dedupe/numbering/timestamp/evidence class
→ ChatGPT directly persists the exact continuity record
→ ChatGPT verifies resulting remote evidence
→ Human Owner final acceptance
→ stop
```

When the connected GitHub contents API is used, the write creates a remote commit directly. Do not invent a separate local commit or push.

## 4. Skill 9 skill/rule exception

Skill 9 directly authorizes ChatGPT to edit/update rule content only under:

```text
docs/skills/chatgpt/**
docs/rules/**
```

This includes the canonical ChatGPT Router because it lives under `docs/skills/chatgpt/`.

Required path:

```text
Router selects Skill 9
→ Context Engineer supplies verified repository evidence
→ Skill 9 verifies target path is allowed
→ ChatGPT directly edits/updates the exact skill/rule file
→ ChatGPT verifies resulting remote evidence
→ Human Owner final acceptance
→ stop
```

Skill 9 does not authorize direct ChatGPT writes to README, AGENTS, operations docs, plans, research, prompts, source, tests, dependencies, workflows, secrets, runtime data, merge, or deployment.

## 5. General repository execution

Outside exact Skill 5 continuity and exact Skill 9 skill/rule scopes:

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

If Cline is capable outside the standing Skill 5/Skill 9 scopes:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

## 6. Skill 12 fallback for other direct ChatGPT execution

Outside the standing Skill 5 and Skill 9 scopes, ChatGPT may directly execute repository work only through a separately passing Skill 12 fallback gate with explicit Human Owner authorization.

A single Cline mistake is not enough.

## 7. Human Owner zero-coding rule

Never require the Human Owner to write code, patch files, type terminal/Git commands, resolve syntax, choose NEW/STAY, choose PLAN/ACT, or invent technical approval/rejection wording when an authorized AI actor can perform the task.

## 8. Prompt and Context Engineer support

Context Engineer supplies verified minimum context for all routes.

Prompt Engineer is mandatory only for Cline-facing instructions. It is not required for direct Skill 5 or Skill 9 repository actions because Cline is not the executor for those exact scopes.

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
ChatGPT standing jobs:
1. Update length problem in repo → Skill 5.
2. Edit/update ChatGPT skills and rules only → Skill 9.
3. Update achievement in repo → Skill 5.

Everything else and Cline capable
→ Cline executes.

Other direct ChatGPT execution
→ Skill 12 only after verified gate + explicit Human Owner authorization.
```
