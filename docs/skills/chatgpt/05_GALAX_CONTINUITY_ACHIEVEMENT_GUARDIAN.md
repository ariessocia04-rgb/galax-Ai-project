```yaml
skill_reference: $galax-continuity-achievement-guardian
skill_id: GALAX-SKILL-05
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 5: Galax Continuity and Achievement Guardian

## 1. Purpose

Skill 5 owns continuity/achievement correctness **and direct ChatGPT persistence** for its exact continuity scope.

It governs:

```yaml
Skill_5_scope:
  - update_length_problem
  - update_achievement
  - qualifying_terminal_PASS_achievement_persistence
```

It verifies content, evidence, dedupe, numbering, timestamp, exact stop point, completed work, do-not-repeat state, and next safe action.

## 2. Mandatory ChatGPT executor rule

Skill 5 is a specific exception to the general Cline-default repository execution rule.

For exact Skill 5 continuity work:

```yaml
continuity_content_authority: ChatGPT_through_Skill_5
continuity_update_executor: ChatGPT
continuity_repository_publisher: ChatGPT_connected_GitHub_app_when_available
Cline_required: false
Cline_default_executor_rule_overridden_for_exact_Skill_5_scope: true
```

Required chain:

```text
Human Owner requests or an authorized workflow requires a Skill 5 continuity update
→ Router selects Skill 5
→ Context Engineer supplies minimum verified continuity evidence
→ Skill 5 determines exact content, target, numbering, timestamp, dedupe, and evidence class
→ ChatGPT directly creates/updates the exact authorized continuity file through the connected GitHub app when available
→ ChatGPT verifies the resulting remote commit/file
→ Human Owner remains final acceptance authority
→ stop
```

Do **not** route exact Skill 5 length-problem or achievement persistence to Cline merely because Cline is capable of editing Markdown.

Do **not** require a Prompt Engineer Cline package for a direct Skill 5 persistence action because Cline is not the executor for this exact scope.

If ChatGPT lacks the current tool/capability required to persist the exact Skill 5 update, report the factual blocker. Do not silently transfer the task to Cline unless the Human Owner explicitly changes this Skill 5 executor rule.

## 3. Exact direct-write allowlist

ChatGPT direct repository mutation under Skill 5 is limited to the exact continuity targets needed for:

```yaml
allowed_actions:
  - create_next_length_problem_checkpoint
  - update_exact_length_problem_checkpoint_when_correction_is_authorized
  - append_or_create_achievement_persistence_record
  - create_or_update_an_authorized_sharded_achievement_record_when_required_by_current_continuity_rules
```

This Skill 5 exception does not authorize unrelated governance, source, tests, dependencies, router changes, workflows, merge, deployment, or general documentation edits.

## 4. Continuity targets

```yaml
continuity_branch: docs/new-chat-continuity-2026-07-27
allowed_length_directory: docs/operations/checkpoints
allowed_length_naming_rule: GALAX_LENGTH_PROBLEM_*_VOLUME_<NEXT_NUMBER>_<YYYY-MM-DD>.md
allowed_achievement_file: docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
main_write: prohibited
merge_authorized: false
```

When repository history requires a different currently canonical continuity target, verify it before acting rather than assuming from chat memory.

## 5. Length-problem update requirements

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

## 6. Achievement requirements

A new achievement must be based on a new material verified result and must not duplicate an existing achievement.

Qualifying evidence can include current remote GitHub proof or exact Human Owner-provided Cline evidence, but evidence class must remain explicit.

A routing decision, prompt, approval alone, pending work, `BLOCKED`, `FAIL`, or duplicate PASS is not a new achievement.

## 7. Connected GitHub publication semantics

When ChatGPT uses the connected GitHub contents API for a Skill 5 update:

```yaml
creates_remote_commit_directly: true
separate_local_commit_step: false
separate_push_step: false
```

ChatGPT must report the actual resulting remote commit SHA and must not claim that Cline committed or pushed the continuity update.

## 8. Hard boundaries

Skill 5 does not authorize unrelated source, tests, dependencies, workflows, merge, deployment, CrewAI architecture changes, router changes, supervisory-rule changes, or unrelated documentation changes.

## 9. Final contract

```text
General repository work:
→ Cline is default executor when capable, subject to the Router and selected skill.

Exact Skill 5 length-problem / achievement persistence:
→ ChatGPT is the direct updater and publisher.
→ Cline is not required.
→ Prompt Engineer Cline packaging is not required.
→ ChatGPT verifies the exact remote result.
→ Human Owner remains final authority.
```
