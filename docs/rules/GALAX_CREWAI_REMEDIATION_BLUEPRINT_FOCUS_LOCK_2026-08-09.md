# Galax CrewAI Remediation Blueprint Permanent Immutable Lock

**Status:** `ACTIVE_PERMANENT_IMMUTABLE_LOCK`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Established by:** Human Owner  
**Unlock path:** `NONE`  
**Runtime effect:** none  
**Source/test mutation authorized by this rule:** false

## 1. Permanent owner-established boundary

The Human Owner establishes this as a one-way permanent governance lock.

After this rule is published, no actor inside the Galax governance system may edit, rewrite, delete, rename, move, reformat, supersede, reinterpret, unlock, or otherwise change the protected CrewAI remediation technical meaning.

This prohibition applies to:

- Human Owner;
- ChatGPT;
- Cline;
- Codex;
- other AI assistants;
- repository contributors;
- automated tools or workflows.

A later instruction from any actor, including the Human Owner, does not unlock this permanent set.

Required blocker:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

## 2. Permanent immutable set

The following canonical artifacts are permanently protected:

```yaml
GALAX_CREWAI_REMEDIATION_IMMUTABLE_SET_V1:
  technical_blueprint:
    path: docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
    locked_blob_sha: c8c4f69e2aeff332cfebc0943ba1d59d045d035e

  permanent_focus_lock:
    path: docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
    lock_effective_after_this_commit: true

  canonical_foundation_narrow_supersession:
    path: docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
    locked_blob_sha: 6a1fc969e422eb10063158356e328222ae9e1217
```

The Foundation/Agent 01 contract is included because it is the only existing canonical narrow supersession that changes how one part of the remediation blueprint is interpreted. Leaving it mutable would create an indirect way to alter the frozen remediation meaning.

## 3. No direct or indirect mutation

The protected remediation technical meaning must not be changed directly or indirectly.

Prohibited actions include:

```yaml
prohibited:
  - edit_content
  - append_content
  - delete_content
  - rename_file
  - move_file
  - delete_file
  - reformat_file
  - normalize_line_endings_as_a_write
  - change_file_mode_when_tracked
  - replace_file
  - restore_over_file
  - resolve_merge_conflict_by_modifying_protected_content
  - create_a_new_rule_that_supersedes_protected_technical_meaning
  - create_a_new_plan_that_competes_with_or_changes_protected_technical_meaning
  - reinterpret_protected_requirements_to_create_new_scope
  - narrow_or_broaden_protected_requirements
  - change_CrewAI_version_or_process_through_documentation
  - add_new_technical_exception_or_supersession
  - remove_existing_Foundation_narrow_supersession
  - unlock_or_weaken_this_lock
```

Any request that would produce one of those effects must return:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

and stop.

## 4. Allowed actions only

Only non-mutating inspection and publication mechanics that preserve the immutable set are allowed.

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
  - commit_other_authorized_repository_changes_when_immutable_set_is_unchanged
  - push_other_authorized_repository_changes_when_immutable_set_is_unchanged
```

Validation must not rewrite files, auto-fix, format, regenerate, normalize, or otherwise mutate the immutable set.

## 5. Commit and push gate

Commit and push are permitted only when the protected set remains unchanged.

Before any commit or push that could include or affect the remediation worktree, verify:

```yaml
GALAX_CREWAI_IMMUTABLE_GIT_GATE_V1:
  blueprint_path_unchanged: true
  blueprint_blob_or_content_identity_preserved: true
  focus_lock_path_unchanged: true
  focus_lock_content_unchanged_after_lock_commit: true
  Foundation_contract_path_unchanged: true
  Foundation_contract_blob_or_content_identity_preserved: true
  no_new_rule_supersedes_remediation_meaning: true
  no_new_plan_competes_with_remediation_meaning: true
  no_indirect_semantic_mutation: true
  status: PASS | BLOCKED
```

If any field is false or unknown, commit/push must not proceed.

Required result:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

## 6. Human Owner cannot unlock this set

For this exact permanent immutable set only, the normal Human Owner unlock authority does not apply.

```yaml
Human_Owner_may_edit_protected_set: false
Human_Owner_may_unlock_protected_set: false
Human_Owner_may_authorize_exception: false
ChatGPT_may_edit_protected_set: false
ChatGPT_Skill_9_may_edit_protected_set: false
ChatGPT_Skill_12_may_edit_protected_set: false
Cline_may_edit_protected_set: false
other_actor_may_edit_protected_set: false
```

The Human Owner remains final authority for all other Galax decisions that do not mutate, weaken, supersede, or unlock this permanent remediation set.

## 7. Relationship to ChatGPT Skill 9

Skill 9 may normally edit/update `docs/skills/chatgpt/**` and `docs/rules/**`, but this file and any protected remediation rule/artifact are explicit exclusions.

Path prefix permission never overrides this immutable lock.

## 8. Relationship to Skill 6

Skill 6 must treat this protected set as `PERMANENT_IMMUTABLE`, not ordinary `LOCKED_ACCEPTED`.

Ordinary unlock workflows do not apply.

Any unlock/edit request must be rejected with:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

## 9. Relationship to Skill 12 fallback

Skill 12 fallback cannot override this permanent lock.

Cline incapability, repeated mismatch, tool availability, urgency, convenience, or explicit owner fallback authorization do not authorize mutation of the immutable remediation set.

## 10. Development focus remains unchanged

Galax technical development remains centered on:

```text
docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
```

with the already-canonical narrow Foundation/Agent 01 supersession preserved exactly as currently locked.

Technical implementation may implement, prove, validate, or unblock exact requirements from this frozen remediation center, but must not rewrite the center itself.

## 11. Final strict rule

```text
CrewAI remediation blueprint / protected remediation rule or canonical technical supersession
→ READ / CHECK / VALIDATE NON-MUTATING ONLY.
→ NO EDIT.
→ NO DELETE.
→ NO RENAME.
→ NO REFORMAT.
→ NO SUPERSESSION.
→ NO UNLOCK.
→ NO EXCEPTION, INCLUDING HUMAN OWNER.

Commit or push
→ allowed only when the immutable set and its technical meaning remain unchanged.

Any mutation request
→ BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
→ STOP.
```
