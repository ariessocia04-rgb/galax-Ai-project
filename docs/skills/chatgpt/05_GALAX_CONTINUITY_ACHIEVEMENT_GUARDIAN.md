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

It verifies content, evidence, dedupe, numbering, timestamp, exact stop point, completed work, do-not-repeat state, next safe action, and preservation of the permanent CrewAI remediation immutable state.

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
→ apply permanent CrewAI remediation continuity-integrity check when relevant
→ ChatGPT directly creates/updates the exact authorized continuity file through the connected GitHub app when available
→ ChatGPT verifies the resulting remote commit/file
→ Human Owner remains final acceptance authority for the continuity record
→ stop
```

Do **not** route exact Skill 5 length-problem or achievement persistence to Cline merely because Cline is capable of editing Markdown.

Do **not** require a Prompt Engineer Cline package for a direct Skill 5 persistence action because Cline is not the executor for this exact scope.

If ChatGPT lacks the current tool/capability required to persist the exact Skill 5 update, report the factual blocker. Do not silently transfer the task to Cline unless the Human Owner explicitly changes this Skill 5 executor rule.

## 3. Permanent CrewAI remediation continuity-integrity rule

Canonical immutable lock:

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

Skill 5 continuity records must never poison future context by recording any of the following as valid current truth:

- that the permanent set was unlocked;
- that the Human Owner overrode the permanent lock;
- that Skill 9 or Skill 12 bypassed the permanent lock;
- that a protected artifact was validly edited, superseded, weakened, replaced, renamed, moved, or reinterpreted;
- that a mutation of the permanent set became accepted merely because it was committed, pushed, tested, or reported by Cline/ChatGPT;
- that a lower-authority checkpoint, achievement, chat summary, or local report changed the protected technical meaning.

If evidence shows an attempted or actual permanent-set mutation, Skill 5 must record it only as a violation/blocker requiring restoration to verified immutable content, using:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

It must not record the mutation as completed/accepted/current architecture.

When CrewAI remediation integrity is material, the continuity record should preserve verified immutable evidence such as current protected paths and available blob/hash identity, and explicitly state that no unlock path exists.

A continuity record itself cannot create, weaken, supersede, or reinterpret the permanent lock.

## 4. Exact direct-write allowlist

ChatGPT direct repository mutation under Skill 5 is limited to the exact continuity targets needed for:

```yaml
allowed_actions:
  - create_next_length_problem_checkpoint
  - update_exact_length_problem_checkpoint_when_correction_is_authorized
  - append_or_create_achievement_persistence_record
  - create_or_update_an_authorized_sharded_achievement_record_when_required_by_current_continuity_rules
```

This Skill 5 exception does not authorize unrelated governance, source, tests, dependencies, router changes, workflows, merge, deployment, general documentation edits, or mutation of the permanent CrewAI remediation set.

## 5. Continuity targets

```yaml
continuity_branch: docs/new-chat-continuity-2026-07-27
allowed_length_directory: docs/operations/checkpoints
allowed_length_naming_rule: GALAX_LENGTH_PROBLEM_*_VOLUME_<NEXT_NUMBER>_<YYYY-MM-DD>.md
allowed_achievement_file: docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
main_write: prohibited
merge_authorized: false
```

When repository history requires a different currently canonical continuity target, verify it before acting rather than assuming from chat memory.

## 6. Length-problem update requirements

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
- evidence class;
- permanent CrewAI remediation integrity state when relevant.

If a reported next action would mutate the permanent set, it cannot be saved as the next safe action; save the permanent-lock blocker instead.

Do not repeat already persisted checkpoints or invent local work as remote proof.

## 7. Achievement requirements

A new achievement must be based on a new material verified result and must not duplicate an existing achievement.

Qualifying evidence can include current remote GitHub proof or exact Human Owner-provided Cline evidence, but evidence class must remain explicit.

A routing decision, prompt, approval alone, pending work, `BLOCKED`, `FAIL`, duplicate PASS, or permanent-remediation mutation is not a new achievement.

A restoration that re-establishes the exact verified immutable protected content may qualify only if it is a new material verified repair result and the record clearly says the permanent lock was preserved/restored, not changed.

## 8. Connected GitHub publication semantics

When ChatGPT uses the connected GitHub contents API for a Skill 5 update:

```yaml
creates_remote_commit_directly: true
separate_local_commit_step: false
separate_push_step: false
```

ChatGPT must report the actual resulting remote commit SHA and must not claim that Cline committed or pushed the continuity update.

## 9. Hard boundaries

Skill 5 does not authorize unrelated source, tests, dependencies, workflows, merge, deployment, CrewAI architecture changes, router changes, supervisory-rule changes, unrelated documentation changes, or any mutation/unlock of the permanent CrewAI remediation set.

```yaml
permanent_CrewAI_remediation_mutation: prohibited
record_false_unlock_as_current_truth: prohibited
record_protected_mutation_as_accepted: prohibited
lower_authority_continuity_override_of_permanent_lock: prohibited
```

## 10. Final contract

```text
General repository work:
→ Cline is default executor when capable, subject to the Router and selected skill.

Exact Skill 5 length-problem / achievement persistence:
→ ChatGPT is the direct updater and publisher.
→ Cline is not required.
→ Prompt Engineer Cline packaging is not required.
→ ChatGPT verifies the exact remote result.
→ Human Owner remains final authority for continuity acceptance.

Permanent CrewAI remediation state:
→ continuity may record/verify it but can never unlock, supersede, or mutate it.
→ any mutation is recorded only as BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK, never as valid current truth.
```
