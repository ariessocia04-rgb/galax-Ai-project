```yaml
skill_reference: $galax-repository-cleanup-auditor
skill_id: GALAX-SKILL-07
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 7: Galax Repository Cleanup Auditor

## 1. Purpose

Skill 7 audits repository organization, duplicates, stale conflicts, redirects, generated junk, and cleanup candidates without deleting or moving anything.

The permanent CrewAI remediation immutable set is categorically outside cleanup/deletion/migration scope.

## 2. Permanent CrewAI remediation cleanup exclusion

Canonical lock:

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

These files and their technical meaning must always be classified:

```text
PERMANENT_IMMUTABLE_CREWAI_REMEDIATION
```

They are never:

- duplicate candidates;
- stale-conflict deletion candidates;
- archive candidates;
- move/rename candidates;
- formatting/normalization candidates;
- reference-migration replacement targets;
- cleanup-generated rewrite targets.

No Human Owner deletion/cleanup authorization can convert them into candidates.

If a cleanup request would mutate, delete, move, rename, supersede, reinterpret, or weaken any protected artifact or its technical meaning, return exactly:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

and stop that cleanup unit.

Allowed interaction is limited to read, inspect, hash/diff/reference checks, and non-mutating validation.

## 3. Other preservation requirements

Preserve:

- active canonical authorities;
- active operational records;
- ordinary `LOCKED_ACCEPTED` artifacts;
- unique historical evidence;
- compatibility redirects still referenced by the repository;
- evidence required for current assignments, checkpoints, issues, and PRs.

Cleanup is never inferred from “make it clean” or similar broad wording.

## 4. Activation triggers

```text
audit the repo cleanup
find duplicate files
which files can be deleted
organize the repository
check stale documentation
remove old files
find broken references
classify repository files
```

## 5. Mandatory authority reconstruction

```text
Router
→ permanent CrewAI remediation lock
→ current active authority needed for requested cleanup scope
→ ordinary locked-artifact registry
→ current assignments/PRs/branches when material
```

Do not audit from filenames alone.

## 6. File classifications

Every reviewed file must be classified as exactly one of:

```yaml
PERMANENT_IMMUTABLE_CREWAI_REMEDIATION:
  meaning: no mutation_cleanup_move_delete_rename_or_unlock_path

ACTIVE_CANONICAL:
  meaning: current_authority_for_a_responsibility

ACTIVE_OPERATIONAL:
  meaning: current_assignment_status_evidence_or_working_record

HISTORICAL_EVIDENCE:
  meaning: unique_record_proving_decisions_actions_failures_or_supersession

COMPATIBILITY_REDIRECT:
  meaning: temporary_pointer_required_until_all_references_are_migrated

EXACT_DUPLICATE_CANDIDATE:
  meaning: content_equivalent_and_removable_only_after_hash_and_reference_proof

STALE_CONFLICT_CANDIDATE:
  meaning: conflicting_record_requiring_reconciliation_before_archive_or_removal

UNREFERENCED_GENERATED_JUNK:
  meaning: generated_artifact_with_no_unique_evidence_or_live_reference

LOCKED_ACCEPTED:
  meaning: ordinary_accepted_artifact_not_eligible_for_cleanup_without_valid_unlock

BLOCKED_UNCLASSIFIED:
  meaning: insufficient_evidence_to_classify_safely
```

Old, verbose, declined, or superseded does not mean useless.

## 7. Required cleanup sequence

```text
inventory exact scope
→ apply permanent remediation exclusion
→ identify purpose/owner/authority/status
→ compare normalized content and hashes
→ locate references
→ identify canonical owner
→ detect ordinary locks and active dependencies
→ preserve unique historical evidence
→ produce cleanup/deletion candidate report excluding permanent set
→ obtain exact Human Owner authorization for eligible non-permanent candidates
→ create separate bounded deletion task
→ verify no broken references
→ stop
```

Skill 7 performs only audit/recommendation.

## 8. Inventory receipt

```yaml
GALAX_CLEANUP_INVENTORY_V2:
  repository:
  branch:
  head_sha:
  scope:
  files_reviewed: []
  permanent_CrewAI_remediation_files_seen: []
  permanent_CrewAI_remediation_integrity_preserved: true | false
  active_assignments_checked: []
  active_PRs_checked: []
  ordinary_locked_artifacts_checked: []
  incomplete_coverage: []
  status: COMPLETE_FOR_SCOPE | PARTIAL | BLOCKED
```

## 9. Per-file classification

```yaml
GALAX_FILE_CLASSIFICATION_V2:
  path:
  classification:
  responsibility:
  authority_source:
  current_references: []
  active_assignment_dependency:
  ordinary_locked_artifact_dependency:
  permanent_CrewAI_remediation_artifact: true | false
  unique_historical_evidence:
  normalized_hash_when_applicable:
  duplicate_of:
  conflict_with:
  safe_action: KEEP | RECONCILE | MIGRATE_REFERENCES | CANDIDATE_FOR_DELETION | BLOCKED
  factual_reason:
```

For `PERMANENT_IMMUTABLE_CREWAI_REMEDIATION`, `safe_action` must be `KEEP` or `BLOCKED`; never deletion/migration.

## 10. Duplicate and conflict proof

No byte/hash/semantic duplication proof can make a permanent remediation artifact deletable or replaceable.

For ordinary files, normal duplicate/conflict analysis may proceed only after permanent-set exclusion.

## 11. Deletion candidate report

```yaml
GALAX_DELETION_CANDIDATE_REPORT_V2:
  audit_scope:
  repository_head_sha:
  permanent_CrewAI_remediation_excluded: true
  candidates: []
  keep_files: []
  reconcile_first: []
  blocked_candidates: []
  Human_Owner_authorization_required: true
```

If a protected remediation file appears in `candidates`, the report is invalid and must return `BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK`.

## 12. Separate deletion task

Only non-permanent eligible candidates may be handed to Skill 2/Cline after Human Owner authorization.

Deletion, validation, commit, and push remain separate tasks.

## 13. Prohibited behavior

```yaml
direct_delete: prohibited
direct_move_or_rename: prohibited
automatic_cleanup: prohibited
delete_because_old: prohibited
delete_because_verbose: prohibited
delete_superseded_unique_evidence: prohibited
delete_compatibility_redirect_before_reference_migration: prohibited
include_ordinary_locked_artifact_as_candidate_without_unlock: prohibited
include_permanent_CrewAI_remediation_artifact_as_candidate: prohibited
move_or_rename_permanent_CrewAI_remediation_artifact: prohibited
rewrite_or_normalize_permanent_CrewAI_remediation_artifact: prohibited
Human_Owner_override_of_permanent_remediation_lock: prohibited
broad_repository_rewrite: prohibited
```

## 14. Final contract

```text
Permanent CrewAI remediation set
→ KEEP permanently.
→ no cleanup/deletion/move/rename/rewrite/unlock.
→ BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK on mutation attempt.

Other repository files
→ normal read-only cleanup audit rules apply.
```
