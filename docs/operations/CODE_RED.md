# CODE RED — Canonical Galax Continuity, Action, Status, and Recovery Record

**Status:** `ACTIVE_CANONICAL_CODE_RED_PROTOCOL`  
**Canonical path:** `docs/operations/CODE_RED.md`  
**Activated:** `2026-07-22`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Applies to:** ChatGPT, Cline, Codex, OpenHands Core, mini-SWE-agent, Aider, PR-Agent, Claude Code, GitHub Copilot, Jules, and every repository-aware AI or human participant  
**Current authorized scope:** Governance Foundation and Agent 01 only  
**Merge/deployment:** prohibited unless separately and explicitly authorized by the human owner

## 1. Meaning of `CODE RED`

`CODE RED` is the mandatory repository-first recovery command for the Galax project.

When the owner says any of the following:

```text
CODE RED
code red
length chat problem
chat length problem
conversation length problem
continue exact Galax flow
operation length problem solve
operatiion length problem solve
backread the repo because the chat is full
```

all participating AI systems must stop relying on remembered conversation fragments and reconstruct the exact project state from the repository before answering or acting.

The old filename:

```text
docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md
```

is now a compatibility redirect only. It is not the canonical continuity record.

## 2. Purpose

CODE RED exists so that every new chat, model, coding assistant, reviewer, or human participant can determine:

```yaml
owner_decisions: what_was_decided
completed_actions: what_was_actually_done
remote_repository_state: what_GitHub_proves
reported_local_state: what_the_owner_or_Cline_reported_but_GitHub_does_not_yet_prove
accepted_work: what_passed_ChatGPT_review_and_human_acceptance
blocked_work: what_must_not_continue
current_stage: where_the_project_is_now
next_allowed_action: exactly_one_safe_next_step
prohibited_actions: what_must_not_happen
active_assignments: who_may_do_what
CrewAI_compatibility: what_is_verified_for_the_pinned_environment
cleanup_state: what_is_canonical_historical_or_safe_to_remove
```

CODE RED is not a verbatim conversation transcript and must never store private chain-of-thought. It stores only concise observable decisions, actions, commands, outputs, hashes, evidence, blockers, reviews, and next steps.

## 3. Source-of-truth hierarchy

```text
README.md current readiness
→ AGENTS.md
→ CODE RED
→ canonical conflict audit and alias target
→ Foundation and Agent 01 Flow execution contract
→ CrewAI 1.15.4 remediation blueprint
→ active rules and plans
→ source index and exact source cards
→ exact current assignment
→ current GitHub branch, PR, issue, commit, test, and evidence state
→ historical records
→ old chat memory or summaries
```

Rules:

- Chat memory never overrides repository evidence.
- A local claim must be labeled `REPORTED_LOCAL_NOT_REMOTE_PROOF` until a commit or exact artifact is available.
- An issue or PR description does not prove a command, test, or file change occurred.
- A lower-priority document cannot reactivate a superseded architecture.
- Conflicts that cannot be resolved by priority return `BLOCKED_SUPERSESSION_CONFLICT`.
- Missing repository access returns `BLOCKED_REPOSITORY_ACCESS_REQUIRED`.

## 4. Mandatory CODE RED reconstruction procedure

Every AI must execute this sequence:

```text
DETECT CODE RED
→ verify repository identity
→ verify main, research, implementation, and PR head SHAs
→ read README.md
→ read AGENTS.md
→ read CODE_RED.md completely
→ read the active Flow contract and applicable plans/rules
→ inspect the active draft PR
→ inspect active assignment issues and latest continuity comments
→ separate remote-proven facts from reported local facts
→ reconstruct completed, rejected, blocked, and pending work
→ detect stale or conflicting records
→ determine the exact current stage
→ produce CODE_RED_RECEIPT
→ act only when safe_to_continue=true
```

Do not ask the owner what the previous chat was doing when repository access exists.

## 5. Mandatory receipt

```yaml
CODE_RED_RECEIPT_V1:
  trigger_detected: true
  reconstructed_at_utc:
  repository: ariessocia04-rgb/galax-Ai-project
  repository_access_verified:

  remote_state:
    main_head_sha:
    research_branch: agent/agent-01-tool-inspection
    research_head_sha:
    implementation_branch: implementation/foundation-agent-01
    implementation_head_sha:
    branch_comparison:
    active_pr_number:
    active_pr_state:
    active_pr_draft:
    active_pr_head_sha:

  reported_local_state:
    local_branch:
    local_head_sha:
    working_tree_status:
    commits_ahead:
    evidence_source:
    remote_proof_available: false

  files_read: []
  active_assignments: []
  owner_decisions_confirmed: []
  completed_actions_confirmed: []
  rejected_or_superseded_actions: []
  accepted_locked_artifacts: []
  unresolved_blockers: []
  stale_records_detected: []
  cleanup_candidates: []
  current_stage:
  next_allowed_action:
  prohibited_next_actions: []
  assumptions: []
  safe_to_continue: false
```

`safe_to_continue` must remain false when repository access is missing, a required record was not read, a branch or SHA is inconsistent, local state is needed but unverified, a canonical conflict exists, or the requested work is absent from the active plan.

## 6. Current remote-proven state

Verified on `2026-07-22`:

```yaml
repository: ariessocia04-rgb/galax-Ai-project
main_head_sha_from_active_PR_base: 41e870d9e57c87f9db317205e9b26dfe555625fb
research_branch: agent/agent-01-tool-inspection
research_head_before_CODE_RED_commit: 3f7dad528a13a0a81069771c52cb4c65f0b0cf20
implementation_branch: implementation/foundation-agent-01
remote_implementation_head: bafb230a995744743af5c0bdd612ad1e7c7568ae
research_ahead_of_remote_implementation_before_CODE_RED: 2
active_PR: 1
active_PR_state: open
active_PR_draft: true
active_PR_merged: false
active_PR_head_branch: agent/agent-01-tool-inspection
active_PR_head_before_CODE_RED_commit: 3f7dad528a13a0a81069771c52cb4c65f0b0cf20
latest_CODE_RED_research_head_before_final_controls: b6ce572107d197cfbb47e7e8fbe101517f58e8d2
```

The exact current SHAs must be re-read dynamically on every CODE RED trigger.

## 7. Current reported local state boundary

The following facts were reported by the owner or Cline during the current work but are not present on the remote implementation branch:

```yaml
classification: REPORTED_LOCAL_NOT_REMOTE_PROOF
local_repository: C:\Users\socia\Desktop\repo clone GALAX\galax-Ai-project
local_branch: implementation/foundation-agent-01
last_reported_local_head: 867f82ab0252b27c3f876d29901274140ef1b18c
last_reported_commits_ahead: 4
last_reported_worktree_clean_after_Stage_0E: true
push_performed: false
sync_performed: false
merge_performed: false
deployment_performed: false
```

The owner later reported that keyboard problems may have deleted current Cline-created files. Therefore:

```yaml
current_local_file_state: UNVERIFIED_AFTER_KEYBOARD_DELETION
safe_to_assume_two_init_files_exist: false
safe_to_assume_models_file_exists: false
safe_to_continue_implementation_without_git_status: false
```

Required recovery evidence:

```powershell
git branch --show-current
git rev-parse HEAD
git status --short
```

Cline checkpoint comparison may be used for recovery, but no restore action is authorized until the exact checkpoint diff is inspected.

### Verified local recovery state - 2026-07-22

The earlier keyboard-incident state above is retained as historical evidence. The following local state was subsequently verified:

```yaml
classification: VERIFIED_LOCAL_NOT_REMOTE_PROOF
local_repository: 'C:\Users\socia\Desktop\repo clone GALAX\galax-Ai-project'
local_branch: implementation/foundation-agent-01
pre_sync_local_head: 867f82ab0252b27c3f876d29901274140ef1b18c
local_head_before_this_record_update: b5c837ae4ddeb11d532b1e0079cf13a5be376982
remote_implementation_head: bafb230a995744743af5c0bdd612ad1e7c7568ae
local_commits_preserved: 4
CODE_RED_governance_commits_cherry_picked: 10
local_commits_ahead_after_cherry_pick: 14
cherry_pick_conflicts: 0
safety_branch: safety/pre-code-red-sync-20260722
safety_branch_head: 867f82ab0252b27c3f876d29901274140ef1b18c
backup_path: 'C:\Users\socia\Desktop\GALAX_STAGE1_BACKUP_20260722_163127'
CODE_RED_backup_path: 'C:\Users\socia\Desktop\CODE_RED_before_Stage5G.md'
CODE_RED_backup_SHA256_match: true
tracked_worktree_changes_before_this_record_edit: none
untracked_files:
  - src/galax/__init__.py
  - src/galax/foundation/__init__.py
  - src/galax/foundation/models.py
src_galax_init_state: accepted_content_preserved
foundation_init_state: accepted_content_preserved
models_state: empty_0_bytes
rejected_models_code_restored: false
backup_hash_match_all_three_Phase_2A_files: true
push_performed: false
remote_implementation_updated: false
main_write: false
merge_performed: false
deployment_performed: false
```

## 8. Material action ledger

### `CR-001` — Active Foundation architecture selected

```yaml
RepositoryPreflightTool_owner: GalaxFoundationFlow
repository_preflight_tool_calls: 1
engineering_manager_tools: []
Agent_01_direct_tools: 0
Agent_01_LLM_calls: 1
Agent_01_output: AgentTaskResult
result_as_answer_for_this_path: prohibited
hidden_second_agent_call: prohibited
HumanReviewRequest_builder: pure_Python_Pydantic
explicit_routers_for_every_branch: required
check_llm_profile_readiness_before_Agent_01: required
LLM_profiles_enabled: false
```

### `CR-002` — External contributor sequence selected

```text
Cline primary supervised implementation
→ Aider one exact reproducible repair when assigned
→ mini-SWE-agent isolated comparison when assigned
→ OpenHands Docker-isolated blocker reproduction when assigned
→ PR-Agent read-only review
→ ChatGPT exact draft-PR diff review
→ human decision
```

Simultaneous overlapping writers are prohibited.

### `CR-003` — Foundation Stage 0A completed locally

```yaml
status: PASS_REPORTED_LOCAL
commit_sha: e214e665651d6a9694e161c65f22762a251043df
commit_message: docs(foundation): reconcile Agent 01 scope evidence
```

### `CR-004` — Foundation dependency evidence and metadata

```yaml
Stage_0B: COMPLETED_WITH_OWNER_PROVIDED_OFFICIAL_EVIDENCE
python: ">=3.10,<3.14"
crewai: "1.15.4"
pydantic: "2.12.5"
pytest: "9.0.3"
ruff: "0.15.1"
uv: "0.11.29"
Stage_0C: PASS_REPORTED_LOCAL
known_head_after_Stage_0C: e382246d0b6b80636b1c4307e5c0e4ee66a76425
```

### `CR-005` — Lockfile, local environment exclusion, and Stage 0E

```yaml
Stage_0D_uv_lock: PASS_REPORTED_LOCAL
uv_resolved_packages: 152
local_environment_gitignore: PASS_REPORTED_LOCAL
Stage_0E_environment_validation: PASS_REPORTED_LOCAL
python_runtime: 3.13.14
crewai_import: 1.15.4
pydantic_import: 2.12.5
pytest_import: 9.0.3
ruff_version: 0.15.1
actual_import_evidence: IMPORTS_OK
```

These local commits remain unpushed and must not be represented as remote GitHub files.

### `CR-006` — Phase 2A planning accepted

```yaml
plan_status: PHASE_2A_ACT_READY
scope: typed_Foundation_contracts_only
exact_files:
  - src/galax/__init__.py
  - src/galax/foundation/__init__.py
  - src/galax/foundation/models.py
  - src/galax/foundation/validation.py
  - tests/test_foundation_contracts.py
Flow_runtime: prohibited_in_Phase_2A
Agent_runtime: prohibited_in_Phase_2A
terminal_commands_before_file_creation: prohibited
commit_push_merge_deploy: prohibited_without_separate_authorization
```

### `CR-007` — Cline file proposals and rejection history

```yaml
src_galax_init_proposal: accepted_before_keyboard_incident
foundation_init_proposal: accepted_before_keyboard_incident
first_models_proposal: REJECTED_SCHEMA_DRIFT
second_models_proposal: REJECTED_INVALID_PYDANTIC_VALIDATOR_USAGE_AND_CONTRACT_DRIFT
current_local_files_after_keyboard_incident: UNVERIFIED
```

Rejected code must not be restored as accepted implementation.

### `CR-008` — ChatGPT + Cline + Draft PR control plan

```yaml
control_plan_file: docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md
control_plan_commit: 1df8fb4c8712d57549ed0c93ddd223b2db3d96d3
initial_Cline_rule_commit: 3f7dad528a13a0a81069771c52cb4c65f0b0cf20
method: Cline_local_writer_plus_GitHub_Draft_PR_plus_ChatGPT_review
custom_bridge: deferred
custom_MCP_bridge: prohibited_now
custom_hook_system: deferred
```

### `CR-009` — CODE RED canonicalization

```yaml
old_protocol_name: Operation_Length_Problem_Solve
new_protocol_name: CODE_RED
canonical_file: docs/operations/CODE_RED.md
CODE_RED_create_commit: d7ffb577987e707b3fe799edc50f8d1524debc38
legacy_redirect_commit: 228ad374101ca082211345261fd41951d22cfe40
Cline_CODE_RED_rule_commit: b6ce572107d197cfbb47e7e8fbe101517f58e8d2
CODE_RED_ledger_update_commit: 8a43992b6201eb529d124e18cd7201d8a307c0aa
README_CODE_RED_commit: 1bbab91c0ef189e20adab0aa3aba5f84606e5f91
AGENTS_CODE_RED_commit: aeff5b772cc39d5f353a7307c3146c10372a350e
control_plan_CODE_RED_commit: d591e5fc67d26f809e3158fdca2b7065194a41f2
old_file_behavior: compatibility_redirect
reason: one_clear_discoverable_state_and_recovery_entry_point
```

### `CR-010` - Local recovery and governance synchronization

```yaml
date: 2026-07-22
operation: local_state_recovery_and_governance_synchronization
branch: implementation/foundation-agent-01
pre_sync_local_head: 867f82ab0252b27c3f876d29901274140ef1b18c
local_head_before_this_record_update: b5c837ae4ddeb11d532b1e0079cf13a5be376982
remote_implementation_head: bafb230a995744743af5c0bdd612ad1e7c7568ae
local_commits_preserved: 4
governance_commits_cherry_picked: 10
local_commits_ahead_after_cherry_pick: 14
cherry_pick_conflicts: 0
backup_created: true
safety_branch_created: true
untracked_Phase_2A_files_preserved: 3
two_accepted_init_files_preserved: true
models_file_state: empty_0_bytes
rejected_models_code_restored: false
backup_hash_comparison_passed: true
push_performed: false
remote_implementation_updated: false
main_write: false
merge_performed: false
deployment_performed: false
```

### `CR-011` - Phase 2A resume precheck passed

```yaml
date: 2026-07-22
operation: Phase_2A_resume_precheck
branch: implementation/foundation-agent-01
verified_HEAD: 9a66670ec2dcb6a63b4cca58167278282a31247e
remote_implementation_head: bafb230a995744743af5c0bdd612ad1e7c7568ae
local_commits_ahead: 15
tracked_worktree_changes: none
untracked_Phase_2A_files: 3
src_galax_init_length: 59
src_galax_init_backup_hash_match: true
foundation_init_length: 26
foundation_init_backup_hash_match: true
models_file_length: 0
models_file_SHA256: E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855
models_file_backup_hash_match: true
rejected_models_code_present: false
Phase_2A_resume_precheck: PASS
push_performed: false
remote_implementation_updated: false
main_write: false
merge_performed: false
deployment_performed: false
```

### `CR-012` - Phase 2A models structural and static validation passed

```yaml
date: 2026-07-23
classification: REPORTED_LOCAL_NOT_REMOTE_PROOF
operation: Phase_2A_models_structural_and_static_validation
branch: implementation/foundation-agent-01
last_verified_local_HEAD: c7d5ca1352f491be8290ef6024f9ae7a91ade8cf
remote_implementation_head: bafb230a995744743af5c0bdd612ad1e7c7568ae
remote_proof_available: false
local_commits_ahead: 16
working_tree_status:
  tracked_changes: none
  untracked_files:
    - src/galax/__init__.py
    - src/galax/foundation/__init__.py
    - src/galax/foundation/models.py
models_py_complete_schema_proposal_saved: true
models_py_structural_review: PASS
models_py_import_check: PASS
models_py_import_check_evidence:
  command: uv run python -c "import sys; sys.path.insert(0, 'src'); import galax.foundation.models; print('MODELS_IMPORT_OK')"
  stdout: MODELS_IMPORT_OK
  exit_code: 0
models_py_ruff_check: PASS
models_py_ruff_evidence:
  command: uv run ruff check src/galax/foundation/models.py
  stdout: All checks passed!
confirmed_models_py_corrections:
  - allowed_paths uses tuple[str, ...], list[str], set[str], and result.append(strict)
  - protected_paths uses tuple[str, ...], list[str], set[str], and result.append(strict)
  - approved_agent_ids accepts exactly ('engineering_manager',)
  - RunManifest contains validate_live_github_evidence
  - RunManifest does not contain validate_resolved_at
  - BlockerRecord contains exactly one validate_resolved_at
  - AgentTaskResult.direct_tool_calls remains Literal[0]
  - RepositoryPreflightTool ownership remains GalaxFoundationFlow
  - result_as_answer remains prohibited
  - hidden second Agent 01 call remains prohibited
  - Agents 02 to 15 remain prohibited
rejected_or_superseded_outputs:
  - stale PHASE_2A_MODELS_CONTRACT_INVENTORY_V1 is not an implementation authority
  - rejected models code must not be restored
  - removal-only misplaced-validator patch was rejected
  - identical SEARCH/REPLACE no-op patch was rejected
  - redirected import command creating .models_import_test.log was rejected
  - duplicate import reruns after PASS were rejected
  - Ruff command chaining that caused E902 parsing errors was rejected
  - no Ruff --fix was authorized
push_performed: false
sync_performed: false
merge_performed: false
deployment_performed: false
  main_write_performed: false
  ```

### `CR-013` - Phase 2A focused validator tests validation completed

```yaml
classification: VERIFIED_LOCAL_NOT_REMOTE_PROOF
date: 2026-07-24
operation: Phase_2A_focused_validator_tests_validation
branch: implementation/foundation-agent-01
local_head_sha: c7d5ca1352f491be8290ef6024f9ae7a91ade8cf
validation_status: PASS
test_file: tests/test_foundation_contracts.py
test_result: 70 passed in 0.50s
test_exit_code: 0
tests_failed: []
tracked_deletions_detected: false
test_file_read_only_setting_applied: true
previous_stage: PHASE_2A_MODELS_FOCUSED_VALIDATOR_TESTS_AUTHORIZATION_REQUIRED
previous_stage_completed: true
implementation_authorized: false
commit_authorized: false
push_authorized: false
merge_authorized: false
deployment_authorized: false
commit_scope_review_required: true
```

## 9. Current stage and exact next action

```yaml
current_stage: "Read-only coherent local commit-scope review required before STAGE 7 — Human authorizes a coherent local commit"
safe_to_continue_implementation: false
last_completed_action:
  - Phase 2A Models Validation Step 1 import check passed
  - Phase 2A Models Validation Step 2 Ruff check passed
  - Phase 2A Models Validation Step 3 focused validator tests passed: 70 passed in 0.50s, exit code 0
next_allowed_action:
  - human authorizes a read-only coherent local commit-scope review
action_sequence_after_authorization:
  - read-only inventory of every modified and untracked path
  - classify each path as include, exclude, local-only, or unresolved
  - produce the exact proposed coherent commit scope
  - human reviews the inclusion/exclusion matrix
  - separate human authorization is required before any git add or commit
```

Prohibited now:

```text
modification of src/galax/__init__.py
modification of src/galax/foundation/__init__.py
validation.py creation
test creation
Flow runtime implementation
Agent runtime implementation
RepositoryPreflightTool implementation
terminal commands
Ruff execution
pytest execution
git add
git commit
git pull
git sync
git merge
git rebase
git reset
git clean
git push
main write
workflow change
deployment
Agents 02-15
MCP integration
```

## 10. Required record after every coherent job

Every repository-aware AI that completes or reviews one coherent job must add or update a CODE RED checkpoint through the active issue/PR continuity channel.

Required schema:

```yaml
CODE_RED_ACTION_RECORD_V1:
  record_id:
  recorded_at_utc:
  assignment_id:
  contributor:
  repository:
  branch:
  starting_sha:
  ending_sha_or_patch_hash:
  authority_source:
  objective:
  files_read: []
  files_created: []
  files_modified: []
  files_deleted: []
  commands_run: []
  tests_passed: []
  tests_failed: []
  tests_skipped: []
  review_status:
  CrewAI_compatibility:
  accepted_locked_artifacts: []
  rejected_outputs: []
  blockers: []
  unsupported_capabilities: []
  exact_remedies: []
  next_allowed_action:
  prohibited_next_actions: []
  commit_authorized: false
  push_authorized: false
  merge_performed: false
  deployment_performed: false
```

A narrative such as `done`, `fixed`, or `tests passed` is insufficient without this evidence.

## 11. Repository cleanup and organization policy

The repository must remain clean, folderized, and non-duplicative, but cleanup must never destroy unique evidence or accepted work.

Every file must be classified as one of:

```yaml
ACTIVE_CANONICAL: current_authority
ACTIVE_OPERATIONAL: current_assignment_status_or_evidence
HISTORICAL_EVIDENCE: retained_because_it_proves_decision_history
COMPATIBILITY_REDIRECT: temporary_pointer_during_reference_migration
EXACT_DUPLICATE_CANDIDATE: removable_only_after_hash_and_reference_verification
STALE_CONFLICT_CANDIDATE: requires_reconciliation_before_archive_or_removal
UNREFERENCED_GENERATED_JUNK: removable_after_proof_and_human_authorization
```

### Cleanup sequence

```text
inventory all files
→ identify owner, purpose, authority, and status
→ calculate or verify exact normalized duplicates
→ locate every inbound reference
→ select one canonical owner
→ update references
→ run documentation, link, and applicable tests
→ preserve unique historical evidence
→ produce deletion candidate report
→ obtain human authorization
→ delete only proven-safe candidates
→ verify no broken references
→ record the deletion in CODE RED
```

### Current cleanup decisions

```yaml
OPERATIION_LENGTH_PROBLEM_SOLVE.md:
  classification: COMPATIBILITY_REDIRECT
  deletion_now: prohibited
  future_removal_gate: all_references_migrated_and_verified

FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md:
  classification: COMPATIBILITY_REDIRECT_OR_ALIAS
  deletion_now: prohibited
  reason: existing_references_depend_on_it

historical_research_and_source_cards:
  classification: HISTORICAL_EVIDENCE
  deletion_merely_because_superseded: prohibited

rejected_or_stale_master_prompt:
  classification: STALE_CONFLICT_CANDIDATE
  execution: prohibited
  deletion_now: prohibited_until_reference_and_evidence_audit

exact_duplicate_files:
  deletion_now: only_after_normalized_hash_equality_and_reference_migration
```

No repository file is declared useless merely because it is old, verbose, declined, or superseded. `Useless` must be proven through purpose, reference, uniqueness, and evidence analysis.

## 12. Accepted-work protection

A file or coherent stage becomes `LOCKED_ACCEPTED` only after:

```text
required work completed
→ required tests passed or factually blocked
→ human-authorized commit
→ separately human-authorized push
→ exact draft PR diff available
→ ChatGPT review receipt PASS
→ human acceptance
```

Changing a locked artifact requires `GALAX_ACCEPTED_ARTIFACT_CHANGE_V1` with the current accepted commit SHA, current hash, factual reason, exact change, allowed paths, required tests, maximum writes, and explicit human authorization.

## 13. CrewAI compatibility boundary

The selected development workflow is external to CrewAI. CrewAI remains the application runtime framework.

Pinned compatibility target:

```yaml
python: ">=3.10,<3.14"
crewai: "1.15.4"
pydantic: "2.12.5"
pytest: "9.0.3"
ruff: "0.15.1"
```

Current online documentation may describe features newer than CrewAI `1.15.4`. A feature must be tested in the exact pinned environment before it is accepted.

CrewAI must not control Cline while the Foundation is incomplete because that would create a circular trust dependency.

## 14. Minimal command for any new AI

```text
CODE RED. Open GitHub repository ariessocia04-rgb/galax-Ai-project. Read README.md, AGENTS.md, and docs/operations/CODE_RED.md completely. Verify the current main, research, implementation, and Draft PR #1 head SHAs. Read the latest Issue #2 continuity checkpoint and Draft PR #1 before returning CODE_RED_RECEIPT_V1. Reconstruct all confirmed decisions, completed actions, reported local-only work, accepted locked artifacts, rejected outputs, blockers, cleanup state, current stage, and exact next allowed action. The exact resume point is a read-only coherent commit-scope review before "STAGE 7 — Human authorizes a coherent local commit." Do not guess, do not duplicate, do not restore rejected code, do not alter accepted work, and continue only when safe_to_continue=true.
```

## 15. Current authorization boundary

Current boundary after Phase 2A Models Validation Steps 1, 2, and focused validator tests:

```yaml
read_only_contract_and_plan_review: true
models_py_complete_schema_proposal_saved: true
models_py_structural_review: true
models_py_import_check: true
models_py_ruff_check: true
focused_validator_tests_completed: true
focused_validator_tests_status: PASS
CODE_RED_documentation_sync_applied: true
commit_scope_review_completed: false
commit_authorized: false
```

It does not authorize:

```yaml
focused_validator_tests_authorized: false
automatic_test_creation: false
models_py_git_add_authorized: false
models_py_commit_authorized: false
models_py_push_authorized: false
validation_py_creation: false
Flow_runtime_implementation: false
Agent_runtime_implementation: false
RepositoryPreflightTool_runtime: false
terminal_command_execution: false
Ruff_execution: false
pytest_execution: false
git_add: false
git_commit: false
git_pull: false
git_sync: false
git_merge: false
git_rebase: false
git_reset: false
git_clean: false
git_push: false
main_write: false
workflow_change: false
deployment: false
Agents_02_to_15: false
production_ready_claim: false
MCP_integration: false
```
