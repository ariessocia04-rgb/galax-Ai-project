```yaml
skill_reference: $galax-continuity-achievement-guardian
skill_id: GALAX-SKILL-05
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 5: Galax Continuity and Achievement Guardian

## 1. Purpose

Skill 5 owns continuity/achievement correctness, not normal repository publication.

It governs:

```yaml
Skill_5_scope:
  - update_length_problem
  - update_achievement
  - qualifying_terminal_PASS_achievement_persistence
```

It verifies content, evidence, dedupe, numbering, timestamp, exact stop point, completed work, do-not-repeat state, and next safe action.

## 2. Cline-default execution

When Cline is capable:

```text
ChatGPT/Skill 5 determines exact continuity content
→ Context Engineer supplies verified evidence
→ Prompt Engineer creates exact Cline package
→ Cline edits/saves locally
→ ChatGPT reviews
→ Human Owner authorizes COMMIT
→ Cline commits
→ STOP
→ Human Owner separately authorizes PUSH
→ Cline pushes
→ STOP
→ ChatGPT verifies exact remote diff
→ Human Owner final acceptance
```

Skill 5 does NOT make ChatGPT the normal direct GitHub uploader.

If ChatGPT attempts direct publication while Cline is capable:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

Only a separately selected, fully passing Skill 12 fallback may permit ChatGPT direct repository execution/publication.

## 3. Continuity targets

```yaml
continuity_branch: docs/new-chat-continuity-2026-07-27
allowed_length_directory: docs/operations/checkpoints
allowed_length_naming_rule: GALAX_LENGTH_PROBLEM_*_VOLUME_<NEXT_NUMBER>_<YYYY-MM-DD>.md
allowed_achievement_file: docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
main_write: prohibited
merge_authorized: false
```

When repository history requires a different currently canonical continuity target, verify it before acting rather than assuming from chat memory.

## 4. Length-problem update requirements

A valid length-problem update must preserve:

- exact current repository/task identity;
- last completed action;
- current unfinished task;
- exact stop point;
- exact next safe action;
- completed/accepted work;
- rejected/superseded work;
- do-not-repeat state;
- blockers;
- Asia/Manila timestamp;
- evidence class.

Do not repeat already persisted checkpoints or invent local work as remote proof.

## 5. Achievement requirements

A new achievement must be based on a new material verified result and must not duplicate an existing achievement.

Qualifying evidence can include current remote GitHub proof or exact Human Owner-provided Cline evidence, but evidence class must remain explicit.

A routing decision, prompt, approval alone, pending work, `BLOCKED`, `FAIL`, or duplicate PASS is not a new achievement.

## 6. Prompt packaging

Any Cline-facing continuity instruction must use:

```text
CLINE SESSION: NEW | STAY
CLINE MODE: PLAN | ACT | VALIDATE | GIT | REVIEW
CANONICAL MODE: PLAN_ONLY | ACT_BOUNDED | VALIDATION_ONLY | GIT_ONLY | REVIEW_ONLY
OWNER ACTION: ...
DO NOT: ...
EXPECTED CLINE STOP: ...
AFTER CLINE STOPS: ...
CLINE PROMPT REQUIRED: YES | NO
```

Prompt Engineer chooses the presentation; Human Owner is not asked to choose NEW/STAY or PLAN/ACT.

## 7. Hard boundaries

Skill 5 does not authorize unrelated source, tests, dependencies, workflows, merge, deployment, CrewAI architecture changes, or unrelated documentation changes.

## 8. Final contract

```text
Skill 5 = continuity authority/content/evidence controller.
Cline = default edit/save/commit/push executor when capable.
ChatGPT = author/specification/reviewer by default.
Skill 12 = only verified owner-authorized ChatGPT execution fallback.
```
