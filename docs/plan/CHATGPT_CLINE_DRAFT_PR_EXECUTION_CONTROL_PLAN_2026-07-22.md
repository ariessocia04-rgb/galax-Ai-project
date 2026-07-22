# ChatGPT + Cline + GitHub Draft PR Execution Control Plan

**Status:** `ACTIVE_CANONICAL_CONTROL_PLAN`  
**Verified:** `2026-07-22`  
**Scope:** Galax Governance Foundation and Agent 01 only  
**Framework target:** CrewAI `1.15.4`  
**Production approval:** No  
**Merge/deploy:** Prohibited

## 1. Purpose

This plan defines the fastest safe working method for all repository-aware AI contributors participating in the Galax project.

The operating combination is:

```yaml
architect_and_remote_reviewer: ChatGPT
primary_local_writer: Cline
canonical_source_of_truth: GitHub
review_surface: Draft_Pull_Request
final_authority: Human_Owner
CrewAI_runtime_role: application_runtime_only
simultaneous_writers: prohibited
```

No contributor may invent a different workflow, bypass this plan, or act only from conversation memory.

## 2. Mandatory authority order

```text
README.md
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ canonical conflict audit and alias target
→ docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
→ docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
→ applicable active rules and plans
→ this control plan
→ exact authorized assignment
→ current GitHub branch, PR, issue, test, and evidence state
```

`docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md` is a compatibility redirect only.

An AI must stop with a factual blocker when any higher-priority instruction conflicts with a lower-priority instruction.

Old chat memory, an old summary, or an AI-generated guess cannot override repository evidence.

## 3. Universal strict rule for every AI participant

```yaml
repo_first: required
CODE_RED_reconstruction: required_when_triggered
vague_assignment: prohibited
self_authorization: prohibited
out_of_plan_work: prohibited
architecture_substitution: prohibited
provider_or_model_substitution: prohibited
unsupported_CrewAI_capability_claim: prohibited
fabricated_test_or_tool_result: prohibited
simultaneous_writer: prohibited
direct_main_write: prohibited
force_push: prohibited
merge: prohibited
deployment: prohibited
Agents_02_to_15: prohibited
```

Every AI must execute only an assignment that exists in the repository or in an exact human-authorized GitHub assignment linked to the repository plan.

No AI may treat `helpful improvement`, `cleanup`, `best practice`, `refactor`, or `future-proofing` as authorization to change files outside the exact plan.

## 4. Role boundaries

### 4.1 ChatGPT

ChatGPT is the repository-aware architect, task author, fact checker, compatibility reviewer, and remote exact-diff reviewer.

ChatGPT must:

1. Open and inspect the repository before giving any implementation, correction, cleanup, deletion, or review instruction.
2. Read README, AGENTS, CODE RED, the current plan, rules, branch state, active draft PR, assignment issue, and relevant evidence.
3. Verify version-sensitive facts against authoritative current sources before changing a CrewAI-dependent contract.
4. Write instructions in specific machine-oriented language when ordinary prose could be ambiguous.
5. Give Cline only one bounded assignment or coherent stage at a time.
6. Name exact allowed files, prohibited files, allowed commands, prohibited commands, required tests, stop conditions, and expected output.
7. Inspect every completed coherent job through the exact GitHub draft PR diff before marking that job accepted.
8. Deeply analyze the result for compatibility with the pinned CrewAI version and active Galax Flow contract.
9. Reject any implementation or cleanup absent from the repository plan.
10. Return an explicit review receipt: `PASS`, `CHANGES_REQUIRED`, or `BLOCKED`.
11. Update CODE RED when a material stage, decision, blocker, accepted artifact, rejection, or cleanup state changes.

ChatGPT must not claim to have inspected local Cline work that has not been published to the authorized remote branch or otherwise supplied as exact evidence.

### 4.2 Cline

Cline is the sole primary local writer for the active implementation worktree.

Cline must:

1. Read `README.md`, `AGENTS.md`, `.clinerules/00-galax-governance.md`, `docs/operations/CODE_RED.md`, this plan, and the exact assignment before proposing an edit.
2. Start in Plan mode unless the exact current assignment already contains a separately accepted Act authorization.
3. Return `REPOSITORY_READ_RECEIPT` before any edit.
4. Use only exact allowed paths and commands.
5. Stop after the assigned file, repair, or coherent stage is complete.
6. Never continue into validation, commit, push, another file, another phase, or cleanup unless separately authorized.
7. Keep auto-approval and YOLO disabled.
8. Keep browser and MCP disabled unless an exact named capability is separately authorized.
9. Preserve completed accepted work and never delete, rename, overwrite, restore, or refactor it without an explicit change authorization.
10. Return actual files changed, files deleted, commands run, tests, blockers, evidence, and CrewAI compatibility. Narrative claims are not proof.

### 4.3 Human owner

The human owner retains final authority for:

```yaml
scope: human_only
Act_mode: human_only
local_restore: human_only
accepted_artifact_unlock: human_only
commit: human_only
push: human_only
architecture_acceptance: human_only
cleanup_acceptance: human_only
deletion: human_only
risk_acceptance: human_only
PR_approval: human_only
merge: human_only
deployment: human_only
credentials: human_only
```

### 4.4 Other external contributors

OpenHands Core, mini-SWE-agent, Aider, PR-Agent, Codex, Copilot, Claude Code, Jules, or another coding assistant may act only when an exact repository assignment grants one narrow role.

They are external development contributors. They are not Galax CrewAI Agents 01–15.

Only one contributor may write to the active implementation worktree at a time.

## 5. Machine-oriented assignment language

ChatGPT must use this schema whenever implementation, repair, cleanup, deletion, or review is authorized:

```yaml
GALAX_AI_ASSIGNMENT_V1:
  assignment_id: <UNIQUE_ID>
  repository: ariessocia04-rgb/galax-Ai-project
  branch: <EXACT_BRANCH>
  expected_head_sha: <EXACT_40_CHARACTER_SHA>
  contributor: <EXACT_CONTRIBUTOR>
  role: <EXACT_ROLE>
  mode: PLAN_ONLY | ACT_BOUNDED | REVIEW_ONLY

  authority:
    source: <REPOSITORY_FILE_OR_GITHUB_ASSIGNMENT>
    human_authorized: true_or_false

  objective: <ONE_EXACT_OBJECTIVE>

  required_reading:
    - README.md
    - AGENTS.md
    - docs/operations/CODE_RED.md
    - <OTHER_EXACT_PATH>

  allowed_paths:
    - <EXACT_PATH_OR_NARROW_GLOB>

  prohibited_paths:
    - <EXACT_PATH_OR_GLOB>

  allowed_commands:
    - <EXACT_COMMAND>

  prohibited_actions:
    - create_unlisted_file
    - modify_unlisted_file
    - delete_file
    - rename_file
    - architecture_change
    - dependency_change
    - commit
    - push
    - merge
    - deploy

  implementation_contract:
    - <EXACT_REQUIREMENT>

  required_tests:
    - <EXACT_TEST_COMMAND>

  stop_conditions:
    - repository_mismatch
    - branch_mismatch
    - head_mismatch
    - missing_required_file
    - unresolved_plan_conflict
    - command_not_allowlisted
    - path_not_allowlisted
    - failed_required_test
    - missing_evidence
    - accepted_artifact_without_unlock
    - cleanup_candidate_not_proven

  required_output:
    - CODE_RED_receipt_when_triggered
    - repository_read_receipt
    - exact_files_changed
    - exact_files_deleted
    - exact_diff_summary
    - commands_run
    - tests_passed
    - tests_failed
    - tests_skipped
    - blockers
    - CrewAI_compatibility_assessment
    - next_allowed_action
    - final_status
```

Missing fields produce `BLOCKED_ASSIGNMENT_INCOMPLETE`.

Cline must not infer omitted permissions.

## 6. Exact movement of work

```text
STAGE 0 — ChatGPT reconstructs repository truth through CODE RED
STAGE 1 — ChatGPT issues one exact bounded assignment
STAGE 2 — Cline returns REPOSITORY_READ_RECEIPT and plan
STAGE 3 — Human accepts or rejects the plan
STAGE 4 — Cline performs only the bounded Act work
STAGE 5 — Human reviews the proposed local action
STAGE 6 — Cline runs only separately authorized validation commands
STAGE 7 — Human authorizes a coherent local commit
STAGE 8 — Human separately authorizes push to the implementation branch
STAGE 9 — Draft PR updates with the exact remote diff
STAGE 10 — ChatGPT inspects the exact PR diff, repository rules, tests, cleanup effects, accepted-work preservation, and CrewAI compatibility
STAGE 11 — ChatGPT returns PASS, CHANGES_REQUIRED, or BLOCKED
STAGE 12 — Human accepts the stage or authorizes one exact correction
STAGE 13 — Accepted files and stage are recorded as LOCKED_ACCEPTED in CODE RED
```

A job is not `DONE` merely because Cline created a file locally.

A coherent job becomes accepted only after:

```yaml
local_change_complete: true
required_local_tests: passed_or_factually_blocked
commit_authorized_by_human: true
push_authorized_by_human: true
draft_PR_diff_available: true
ChatGPT_exact_diff_review: PASS
human_stage_acceptance: true
CODE_RED_updated: true
```

## 7. Draft PR review contract

The draft PR is the exact code-review channel between Cline execution and ChatGPT inspection.

ChatGPT must inspect:

```yaml
repository_and_branch_identity: required
starting_and_ending_SHA: required
changed_files: required
additions_and_deletions: required
full_relevant_diff: required
scope_alignment: required
CrewAI_1_15_4_compatibility: required
Flow_contract_compatibility: required
architecture_invariants: required
required_tests_and_real_results: required
security_and_secret_risk: required
unsupported_claims: required
completed_work_preservation: required
cleanup_and_reference_integrity: required_when_applicable
```

ChatGPT review output:

```yaml
GALAX_CHATGPT_REVIEW_RECEIPT_V1:
  assignment_id:
  repository:
  branch:
  reviewed_head_sha:
  files_reviewed: []
  plan_alignment: PASS | FAIL | BLOCKED
  CrewAI_compatibility: PASS | FAIL | BLOCKED
  architecture_compatibility: PASS | FAIL | BLOCKED
  cleanup_integrity: PASS | FAIL | NOT_APPLICABLE | BLOCKED
  tests_verified: []
  tests_missing: []
  unauthorized_changes: []
  regressions: []
  broken_references: []
  blockers: []
  exact_required_corrections: []
  accepted_files: []
  locked_after_acceptance: []
  status: PASS | CHANGES_REQUIRED | BLOCKED
  next_allowed_action:
```

ChatGPT must not mark `PASS` when the exact diff, required test evidence, pinned compatibility evidence, or required cleanup proof is unavailable.

## 8. Completed-work protection

A completed accepted file or stage must not be casually changed or deleted.

Each accepted item must be recorded in CODE RED with:

```yaml
GALAX_ACCEPTED_ARTIFACT_V1:
  assignment_id:
  stage:
  path:
  accepted_commit_sha:
  accepted_blob_or_content_hash:
  ChatGPT_review_status: PASS
  human_acceptance: true
  lock_status: LOCKED_ACCEPTED
  accepted_at:
```

The accepted state is protected by:

1. Cline checkpoints for immediate local rollback.
2. Git commits for exact local and remote history.
3. The draft PR diff for independent inspection.
4. Prohibition on force push and history rewrite.
5. A mandatory explicit unlock/change contract before modification.

Required change authorization:

```yaml
GALAX_ACCEPTED_ARTIFACT_CHANGE_V1:
  change_id:
  path:
  current_accepted_commit_sha:
  current_accepted_hash:
  factual_reason:
  exact_required_change:
  allowed_files:
  required_tests:
  maximum_writes:
  human_authorized: true
```

Without this contract, an accepted file must be treated as read-only.

## 9. Repository cleanup contract

Cleanup is a separate bounded task. It is never implied by implementation work.

Every file must be classified as:

```text
ACTIVE_CANONICAL
ACTIVE_OPERATIONAL
HISTORICAL_EVIDENCE
COMPATIBILITY_REDIRECT
EXACT_DUPLICATE_CANDIDATE
STALE_CONFLICT_CANDIDATE
UNREFERENCED_GENERATED_JUNK
```

Required cleanup procedure:

```text
inventory all files
→ identify purpose, authority, owner, and references
→ prove normalized exact duplicate or genuinely unreferenced generated junk
→ select one canonical record
→ migrate all references
→ preserve unique evidence
→ run checks
→ produce exact deletion candidate report
→ obtain human deletion authorization
→ delete only authorized files
→ verify no broken references
→ record the deletion in CODE RED
```

No file is useless merely because it is old, verbose, declined, historical, or superseded.

## 10. Cline instruction quality rules

To make Cline follow instructions more reliably:

1. Keep durable rules in `.clinerules/`, `AGENTS.md`, and CODE RED.
2. Use exact file paths.
3. Give one bounded objective at a time.
4. Separate Plan, Act, validation, commit, push, cleanup, and deletion authorization.
5. State prohibitions as explicit actions and paths.
6. Require a fixed output contract.
7. Require Cline to stop after the assigned objective.
8. Never combine file creation, broad refactoring, cleanup, testing, commit, and push in one vague instruction.
9. Require exact SHA and branch verification before mutation.
10. Repeat critical architecture invariants inside the exact assignment.
11. Require CODE RED reconstruction whenever state is uncertain or the owner triggers it.

This structured AI-to-AI language reduces ambiguity. It is not a hidden language and grants no additional authority.

## 11. CrewAI compatibility gate

The development-control workflow is external to CrewAI and does not modify CrewAI runtime semantics by itself.

CrewAI remains the application runtime framework for:

```yaml
Flow_orchestration: true
explicit_routers: required
typed_state: required
persistence_and_resume: required_when_implemented
Agent_01_evaluation: one_LLM_call
Agent_01_direct_tools: zero
Flow_owned_repository_preflight: one_call
HumanReviewRequest: deterministic_Python_Pydantic
Agents_02_to_15: disabled
```

Every result must be checked against:

```yaml
python: ">=3.10,<3.14"
crewai: "1.15.4"
pydantic: "2.12.5"
pytest: "9.0.3"
ruff: "0.15.1"
```

Current online CrewAI documentation may describe features newer than `1.15.4`. A feature is not authorized merely because it exists in current documentation. It must be verified in the pinned environment and aligned with the active Flow contract.

CrewAI must not control Cline while the Galax Foundation itself is incomplete. That would create a circular trust dependency.

## 12. Current simplification decision

```yaml
Cline_bridge: deferred
custom_MCP_bridge: prohibited_now
custom_PowerShell_hook_system: deferred
GitHub_Actions_autonomous_writer: prohibited_now
selected_method: Cline_plus_GitHub_Draft_PR_plus_ChatGPT_review
reason:
  - minimum_new_tools
  - exact_remote_diff_visibility
  - Git_history_recovery
  - lower_setup_complexity
  - human_control_preserved
```

Cline built-in rules, manual approvals, checkpoints, Git commits, implementation branch, draft PR, ChatGPT review, and CODE RED are sufficient for the current controlled stage.

## 13. Non-negotiable stop conditions

Stop with a factual blocker when any of these are true:

```text
repository or branch mismatch
unexpected HEAD SHA
working tree contains unexplained changes
required repository record is missing
CODE RED reconstruction is incomplete
assignment is vague or incomplete
requested file is outside the plan
accepted artifact would be altered without unlock authorization
cleanup candidate is not proven safe
CrewAI feature compatibility is unverified
required command or test is not allowlisted
required test fails
required evidence is missing
another writer is active on the same worktree
commit or push lacks separate human authorization
```

No blocked stage may continue to the next successful stage.

## 14. Current authorization boundary

This document controls contributor coordination and review only.

It does not authorize:

```yaml
implementation_file_change: false
implementation_branch_publication: false
commit_of_local_unpushed_work: false
push_of_local_unpushed_work: false
cleanup_deletion: false
merge: false
deployment: false
LLM_profile_activation: false
Agents_02_to_15: false
production_ready_claim: false
```
