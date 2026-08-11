```yaml
skill_reference: $galax-locked-artifact-guardian
skill_id: GALAX-SKILL-06
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 6: Galax Locked Artifact Guardian

**Project:** Galax AI  
**Final authority:** Human Owner except the owner-established permanent CrewAI remediation immutable set, which has no unlock path.

## 1. Purpose

Skill 6 protects accepted artifacts and enforces one stronger permanent immutable class for the CrewAI remediation technical center.

Two lock classes exist:

```yaml
lock_classes:
  LOCKED_ACCEPTED:
    normal_owner_unlock_workflow_available: true

  PERMANENT_IMMUTABLE_CREWAI_REMEDIATION:
    normal_owner_unlock_workflow_available: false
    any_actor_unlock_available: false
```

## 2. Permanent CrewAI remediation immutable set

Canonical lock rule:

```text
docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
```

Protected artifacts include:

```yaml
PERMANENT_CREWAI_REMEDIATION_SET:
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
  - docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
```

This set is not ordinary `LOCKED_ACCEPTED` work.

## 3. Absolute permanent-lock behavior

No actor may edit, rewrite, delete, rename, move, reformat, replace, supersede, reinterpret, weaken, unlock, or indirectly change the technical meaning of the permanent set.

This includes:

```yaml
actors_blocked_from_mutation:
  - Human_Owner
  - ChatGPT
  - Cline
  - Skill_9
  - Skill_12
  - Codex
  - other_AI_or_repository_contributor
```

Any mutation/unlock request returns:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

and stops.

## 4. No Human Owner unlock for this class

The normal owner unlock workflow applies only to ordinary `LOCKED_ACCEPTED` artifacts.

For `PERMANENT_IMMUTABLE_CREWAI_REMEDIATION`:

```yaml
Human_Owner_unlock: prohibited
Human_Owner_exception_authorization: prohibited
ChatGPT_unlock: prohibited
Cline_unlock: prohibited
Skill_12_fallback_override: prohibited
```

A later request from the Human Owner to unlock/edit this set is evidence of a blocked request, not unlock authority.

## 5. Allowed operations on the permanent set

Only non-mutating inspection/validation and Git publication that preserves the immutable set are allowed:

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

## 6. Commit / push gate

Before commit or push when the remediation worktree is material, require:

```yaml
GALAX_PERMANENT_CREWAI_LOCK_GIT_CHECK_V1:
  protected_paths_changed: false
  protected_content_changed: false
  protected_path_or_mode_changed: false
  indirect_rule_or_plan_supersession_detected: false
  technical_meaning_changed: false
  status: PASS | BLOCKED
```

If any protected state is changed or unknown:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

Commit/push may proceed only when the protected set remains unchanged.

## 7. Indirect mutation protection

A new file or change outside the protected paths is also blocked when it attempts to:

- supersede the remediation blueprint;
- replace or weaken its technical rules;
- add a competing remediation plan;
- modify the Foundation narrow supersession meaning;
- create an exception that permits later mutation;
- reinterpret the frozen requirements into different technical scope.

Result:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

## 8. Ordinary LOCKED_ACCEPTED behavior

For artifacts that are ordinary `LOCKED_ACCEPTED` and are not part of the permanent remediation set, the existing evidence-backed owner unlock process remains available.

An ordinary unlock request must still prove exact artifact identity, factual need, smallest change, exact scope, validation, and Human Owner authorization.

The permanent CrewAI remediation set must never enter that ordinary unlock workflow.

## 9. Pre-task collision check

Before any task that could touch or semantically affect protected remediation work, return:

```yaml
GALAX_LOCK_COLLISION_CHECK_V2:
  assignment_id:
  proposed_reads: []
  proposed_edits: []
  proposed_commands: []
  permanent_remediation_artifacts_applicable: []
  ordinary_LOCKED_ACCEPTED_applicable: []
  direct_permanent_lock_collision: []
  indirect_permanent_lock_collision: []
  protected_set_unchanged_after_allowed_action: true | false | UNKNOWN
  status: PASS | CHANGES_REQUIRED | BLOCKED
```

Any direct or indirect permanent-lock collision requires `BLOCKED`.

## 10. Final contract

```text
Ordinary LOCKED_ACCEPTED
→ protected
→ exact owner unlock may be possible under normal lock process.

Permanent CrewAI remediation set
→ READ / CHECK / NON-MUTATING VALIDATION only.
→ COMMIT / PUSH only if protected set remains unchanged.
→ NO EDIT.
→ NO UNLOCK.
→ NO EXCEPTION.
→ Human Owner cannot override this permanent class.
→ BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK on any mutation attempt.
```
