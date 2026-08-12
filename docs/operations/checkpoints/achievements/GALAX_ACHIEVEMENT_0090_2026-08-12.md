# Galax Achievement 90 — Failure #2 models.py worktree-vs-index delta isolation PASS

```yaml
GALAX_ACHIEVEMENT_SHARD_V1:
  achievement_number: 90
  recorded_local_datetime: 2026-08-12T16:23+08:00
  timezone_name: Asia/Manila
  source_primary_skill_alias: $galax-evidence-validation-acceptance-guardian
  source_task_or_assignment_id: GALAX_FAILURE_2_TEST_AND_IMPLEMENTATION_ACT_V1
  source_terminal_status: PASS
  bounded_objective_completed: true
  new_material_result: true
  persistence_class: LATE_PERSISTENCE_OF_PREVIOUSLY_VERIFIED_UNSHARDED_PASS
  evidence_class: HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE
  exact_completed_result: FAILURE_2_MODELS_WORKTREE_VS_INDEX_DELTA_ISOLATION_PASS
  exact_evidence_reference: GALAX_LENGTH_PROBLEM_1248_FAILURE_2_VALIDATION_PASS_COMMIT_BLOCKED_BASELINE_RECONCILIATION_MODELS_ISOLATED_VOLUME_76_2026_08_12
  prior_sharded_achievement_number: 89
  DO_NOT_REPEAT:
    - repeat src/galax/foundation/models.py worktree-vs-index delta isolation solely to reproduce this already-reviewed PASS
    - recreate Achievement 90 from the same models.py delta-isolation evidence
    - infer complete baseline final acceptance or commit readiness from this file-level isolation PASS
    - infer full-suite pytest PASS from this file-level isolation PASS
    - modify LOCKED_ACCEPTED
    - absorb or modify Failure #3
    - mutate or unlock the permanent CrewAI remediation set
  does_not_authorize_next_technical_stage: true
```

## Verified completed result

The previously reviewed Failure #2 `src/galax/foundation/models.py` worktree-vs-index isolation result is persisted here as a separate achievement because it is a material technical PASS that was present in Volume 76 but had not received its own numbered achievement shard.

The Human Owner-provided Cline terminal diff was reviewed as showing only the already-approved Failure #2 source delta on top of the pre-existing staged baseline.

```yaml
path: src/galax/foundation/models.py
present_in_HEAD: false
index_blob_sha: d600cecd681963cbfd4c03cfef63d335ce62a74b
staged_baseline_exists: true
worktree_delta_exists: true
worktree_delta_matches_only_Failure_2: true
unrelated_worktree_changes_detected: false
models_delta_isolation_status: PASS
evidence_class: HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE
```

The reviewed Failure #2 source delta included the already-approved evidence-trust implementation areas:

```yaml
EvidenceRecord_delta:
  - run_id
  - task_id
  - agent_id
  - expires_at
  - validate_expiry_window

supported_claim_classifier_delta:
  - classify_supported_claim_evidence
  - ABSENT
  - UNTRUSTED
  - MISMATCHED
  - EXPIRED
  - valid_at

FoundationFlowState_delta:
  - exact linked LLM invocation lookup
  - run_id match
  - task_id match
  - agent_id match
  - status == SUCCEEDED
  - finished_at required
  - validity anchored to finished_at
  - invalid or unprovable evidence may remain only BLOCKED on human_review_required
```

## Why this is Achievement 90

Achievements 87–89 already persist:

```yaml
Achievement_87: Failure_2_saved_ACT_PASS
Achievement_88: Failure_2_focused_validation_PASS_14_of_14
Achievement_89: Failure_2_test_file_worktree_vs_index_delta_isolation_PASS
```

The `models.py` worktree-vs-index isolation PASS is materially distinct from those three results and had not been separately sharded. This record is therefore a deduplicated late persistence of an already-verified material PASS, not a rerun and not a new implementation action.

This does not convert any blocked result into PASS. In particular:

```yaml
full_suite_validation_status: BLOCKED_VALIDATION_OUTPUT_STILL_UNOBSERVABLE
baseline_final_acceptance: NOT_PROVEN
baseline_final_commit_eligibility: NOT_PROVEN
commit_blocker: BLOCKED_COMMIT_SCOPE_NOT_PROVEN
commit_created: false
push_performed: false
```

## Protected state

```text
LOCKED_ACCEPTED:
tests/test_foundation_contracts.py::TestFoundationFlowState::test_completion_requires_pass_preflight
```

```yaml
Failure_3_rule: preflight_result.run_id == run_manifest.run_id
Failure_3_modified: false
LOCKED_ACCEPTED_modified: false
```

Permanent immutable protected set remains unchanged:

```text
docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
```

No source/test edit, validation rerun, index mutation, implementation commit, push, merge, or deployment is authorized by this achievement persistence record.
