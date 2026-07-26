# Phase 2A Tri-AI Alignment and Recovery Plan — 2026-07-26

**Plan ID:** `PHASE_2A_TRI_AI_ALIGNMENT_AND_RECOVERY_PLAN_001`  
**Status:** `APPROVED_FOR_ASSIGNMENT_PREPARATION_ONLY`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Plan branch:** `governance/phase-2a-tri-ai-plan-001`  
**Plan branch base:** `f41f53beffabd5f9ac1f83920e0141f5925cedbb`  
**Implementation branch:** `implementation/foundation-agent-01`  
**Draft PR:** `#7`  
**Continuity issue:** `#2`  
**Execution authority:** Human owner only  
**Merge/deployment:** Prohibited

---

## 1. Purpose

This plan defines the lowest-risk practical way for Cline, Codex, ChatGPT, and the human owner to work as one controlled team without restarting completed Phase 2A work, overwriting valid evidence, broadening scope without approval, or allowing multiple writers to damage the same repository state.

This plan does **not** claim perfect execution or zero risk. No AI workflow can guarantee that. It instead requires evidence-based gates, isolated roles, exact assignments, one writer at a time, read-only independent review, explicit stop conditions, and separate human approvals for every mutation boundary.

The target outcome is:

```text
preserve all valid completed Phase 2A work
→ independently verify local and remote state
→ reconcile stale or conflicting records
→ correct remote scope drift without rewriting history
→ complete the original exact review corrections
→ run separately authorized validation
→ commit and push only after separate approvals
→ obtain Codex and ChatGPT remote review
→ obtain human acceptance
→ record LOCKED_ACCEPTED only after PASS
```

---

## 2. Current verified remote facts

The following remote facts are the planning baseline and must be re-verified before execution:

```yaml
repository: ariessocia04-rgb/galax-Ai-project
implementation_branch: implementation/foundation-agent-01
remote_head_sha: f41f53beffabd5f9ac1f83920e0141f5925cedbb
original_reviewed_head_sha: 0f02475df29b567253131f53c8fa5b162c12ec94
base_sha: c7d5ca1352f491be8290ef6024f9ae7a91ade8cf
draft_pr: 7
draft_pr_state: open
draft_pr_draft: true
draft_pr_merged: false
current_commit_count: 2
current_changed_file_count: 6
remote_ci_status_checks: none_observed
```

The extra remote commit:

```yaml
commit_sha: f41f53beffabd5f9ac1f83920e0141f5925cedbb
commit_message: docs(governance): add owner checkpoint directive
relationship_to_original_reviewed_commit: exactly_one_linear_commit_ahead
changed_path:
  - docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md
additions: 45
deletions: 0
```

The original ChatGPT PR review returned:

```yaml
status: CHANGES_REQUIRED
plan_alignment: PASS
CrewAI_compatibility: PASS_FOR_PHASE_2A_SCHEMA_ONLY
architecture_compatibility: PASS_FOR_PHASE_2A_SCHEMA_ONLY
accepted_files: []
locked_after_acceptance: []
```

Original required corrections:

1. Fix malformed YAML indentation in `CODE_RED.md` CR-012 without rewriting historical evidence.
2. Synchronize the current CODE RED stage with the real commit, push, Draft PR, and review state.
3. Add one explicit Pydantic unknown-field test asserting the error type `extra_forbidden`.

These facts do not authorize execution. Every executor must re-verify the exact branch and SHA before acting.

---

## 3. Non-negotiable safety model

```yaml
single_writer: required
simultaneous_writers: prohibited
plan_before_act: required
read_only_audit_before_mutation: required
exact_repository_branch_and_SHA_verification: required
exact_allowed_paths: required
exact_allowed_commands: required
exact_stop_conditions: required
separate_validation_authorization: required
separate_git_add_authorization: required
separate_commit_authorization: required
separate_push_authorization: required
exact_remote_diff_review: required
human_final_authority: required
history_rewrite: prohibited
force_push: prohibited
main_write: prohibited
merge: prohibited
deployment: prohibited
Agents_02_to_15: prohibited
workflow_or_secret_change: prohibited
unrestricted_auto_approval: prohibited
YOLO_mode: prohibited
unapproved_browser_or_MCP_access: prohibited
```

### 3.1 One goal per assignment

Every assignment must contain exactly one coherent objective. Investigation, edits, validation, commit, push, and review are separate stages. No AI may continue automatically into the next stage.

### 3.2 Evidence over narrative

Statements such as `done`, `fixed`, `safe`, `tests passed`, or `aligned` are invalid without observable evidence. Every factual claim must identify the repository, branch, starting SHA, ending SHA or patch hash, changed paths, commands, results, blockers, and next allowed action.

### 3.3 Unknown state means stop

Missing or inconsistent repository state must produce a factual blocker. It must never be repaired through guessing, hidden fallback behavior, automatic reset, broad restore, or undocumented scope expansion.

### 3.4 Historical evidence must remain intact

Old records are not deleted merely because they are outdated. Historical actions remain evidence. Only the current-status sections are synchronized. Deletion requires a separate cleanup inventory, reference audit, proof, tests, and human authorization.

---

## 4. Team operating architecture

```text
Human owner
  ├── approves plan, assignments, commands, edits, validation, commit, push, acceptance
  │
  ├── ChatGPT — governance orchestrator and exact remote-diff checker
  │     ├── reads GitHub repository, Issue #2, PR #7, commits, and patches
  │     ├── prepares bounded assignments
  │     ├── reconciles Cline and Codex evidence
  │     └── returns PASS, CHANGES_REQUIRED, or BLOCKED
  │
  ├── Cline — sole supervised local writer
  │     ├── verifies local worktree
  │     ├── plans locally
  │     ├── applies only human-approved bounded edits
  │     └── runs only separately approved commands
  │
  └── Codex — independent remote alignment and PR reviewer
        ├── reads AGENTS.md and exact remote PR state
        ├── checks plan alignment, regressions, security, and scope
        └── never fixes, pushes, or self-approves during this plan
```

There is no uncontrolled direct AI-to-AI execution channel. GitHub Issue #2 and Draft PR #7 are the durable evidence and handoff channels.

---

## 5. Cline charter

### Role

`SOLE_SUPERVISED_LOCAL_EXECUTOR`

### Goal

Verify the exact local state and execute only one human-authorized bounded stage at a time while preserving all valid completed work, refusing scope drift, and publishing factual evidence for independent review.

### Background

Cline is the existing primary local implementation contributor for the Galax Governance Foundation and Agent 01 controlled trial. It is not the architecture owner, approval authority, merge authority, production operator, or Galax Agent 01. Its local workspace is expected to be:

```text
C:\Users\socia\Desktop\repo clone GALAX\galax-Ai-project
```

The exact workspace, branch, and SHA must be verified every time. The expected last independently verified local state was branch `implementation/foundation-agent-01` at commit `0f02475df29b567253131f53c8fa5b162c12ec94`, with no tracked or staged correction diff. A mismatch is a blocker, not permission to synchronize automatically.

### Authority

```yaml
read_repository: allowed
read_exact_files: allowed
run_allowlisted_read_only_commands: only_after_human_approval
modify_files: only_in_ACT_BOUNDED_after_human_approval
run_validation: separate_human_approval_required
git_add: separate_human_approval_required
commit: separate_human_approval_required
push: separate_human_approval_required
merge: prohibited
deployment: prohibited
architecture_change: prohibited
scope_expansion: prohibited
```

### Required configuration

```yaml
start_mode: PLAN
auto_approve: false
YOLO: false
browser: disabled
MCP: disabled
checkpoints: enabled_as_recovery_evidence_only
```

Cline checkpoints are not approval and must not be used to restore rejected code automatically.

### Required behaviour

1. Read the complete mandatory repository order.
2. Return `REPOSITORY_READ_RECEIPT` before edits.
3. State exact allowed and prohibited paths.
4. State exact commands before requesting execution.
5. Stop on any mismatch or unexpected file.
6. Make the smallest possible change.
7. Never edit a file because it appears useful.
8. Never continue from edit to test, commit, or push without a new approval.
9. Never treat a displayed patch as a saved edit.
10. Never claim a local result is remote evidence.

---

## 6. Codex charter

### Role

`INDEPENDENT_REMOTE_ALIGNMENT_AND_PR_REVIEWER`

### Goal

Independently reconstruct the current remote repository and Draft PR state, detect serious plan, scope, architecture, security, regression, and evidence problems, and publish review findings without modifying the branch.

### Background

Codex is an external reviewer. It does not inherit authority from prior conversation summaries. It must reconstruct context from repository files, applicable `AGENTS.md`, the exact Draft PR #7 diff, the original ChatGPT review, and the current assignment.

### Authority

```yaml
read_repository: allowed
read_AGENTS_instructions: required
review_PR_diff: allowed
report_findings: allowed
edit_files: prohibited
create_branch: prohibited
create_or_update_PR: prohibited
fix_request: prohibited
commit: prohibited
push: prohibited
merge: prohibited
self_approval: prohibited
```

### Required behaviour

1. Report the exact reviewed head SHA.
2. List the actual changed files and commit count.
3. Separate remote-proven facts from assumptions.
4. Check the repository plan and assignment before reviewing code quality.
5. Check completed-work preservation.
6. Check unexpected files and unauthorized changes.
7. Check strict Pydantic and Agent 01 architecture invariants.
8. Check stale documentation contradictions.
9. Report only evidence-backed findings.
10. Do not run or suggest an automatic fix as completed work.

### Mandatory prohibited instruction

```text
Do not use or accept @codex fix during this plan.
```

---

## 7. ChatGPT charter

### Role

`GOVERNANCE_ORCHESTRATOR_AND_EXACT_REMOTE_DIFF_REVIEWER`

### Goal

Prepare exact bounded assignments, inspect current GitHub evidence, reconcile Cline local receipts with Codex remote findings, and issue a factual review decision without modifying repository content or branch refs during the recovery plan.

### Background

ChatGPT previously created an unauthorized direct remote documentation commit. To prevent recurrence, ChatGPT is read-only for repository contents and refs during this plan. It may publish an Issue or PR review/comment only after explicit human authorization for that specific publication.

### Authority

```yaml
read_repository: allowed
read_issues_and_PRs: allowed
compare_commits: allowed
prepare_assignments: allowed
review_remote_diff: allowed
post_review_or_comment: separate_human_approval_required
create_file: prohibited
update_file: prohibited
delete_file: prohibited
create_commit: prohibited
update_ref: prohibited
merge: prohibited
deployment: prohibited
```

### Required behaviour

1. Inspect current repository evidence before every assignment.
2. Never rely on chat memory over repository evidence.
3. Never approve a request without checking assignment ID, stage, allowed paths, commands, tests, and stop conditions.
4. Never classify local work as completed without a receipt or remote diff.
5. Reconcile contradictory records explicitly.
6. Return `PASS`, `CHANGES_REQUIRED`, or `BLOCKED` only.
7. List exact required corrections when not PASS.
8. Never self-authorize publication or repository mutation.

---

## 8. Human owner charter

### Role

`FINAL_AUTHORITY`

### Exclusive approvals

```yaml
approve_plan: human_only
approve_assignment_content: human_only
approve_read_only_command_execution: human_only
approve_ACT_BOUNDED: human_only
approve_each_allowed_path: human_only
approve_validation: human_only
approve_git_add: human_only
approve_commit: human_only
approve_push: human_only
accept_stage: human_only
unlock_accepted_artifact: human_only
merge: human_only_but_currently_prohibited
deployment: human_only_but_currently_prohibited
```

A general instruction such as `continue`, `finish`, `fix everything`, or `make it aligned` is not sufficient authorization.

---

## 9. Shared control and handoff channels

### Issue #2

Use Issue #2 for:

- exact assignment publication;
- Cline local receipts;
- ChatGPT reconciliation receipts;
- explicit continuity checkpoints;
- current stop point and next allowed action.

### Draft PR #7

Use Draft PR #7 for:

- exact remote commit and changed-file evidence;
- Codex remote review;
- ChatGPT exact-diff review;
- review discussions;
- final PASS or CHANGES_REQUIRED evidence.

### No-copy workflow

The owner should not have to manually retype long receipts. When separately authorized and when GitHub CLI is already installed and authenticated, Cline may publish the exact completed receipt to Issue #2 using one allowlisted `gh issue comment` command. If the command or authentication is unavailable, stop with a blocker. Do not install tools, expose credentials, enable MCP, or substitute an unapproved channel.

---

## 10. Stage sequence

### Stage A — Plan publication only

This document and the assignment pack are stored on the dedicated plan branch. They do not alter PR #7 or the implementation branch.

```yaml
execution_authorized: false
Cline_launch_authorized: false
Codex_trigger_authorized: false
Issue_or_PR_publication_authorized: false
```

### Stage B — Dual read-only audit

#### B1 — Cline local audit

Cline verifies the local branch, SHA, worktree, staged/unstaged diff, and correction presence using only exact read-only commands.

#### B2 — Codex remote audit

Codex reviews the exact remote head, PR metadata, commit list, changed files, full diff, repository instructions, and original review findings.

The audits may run during the same general review period because neither may write. They must not share a mutable worktree.

### Stage C — ChatGPT reconciliation

ChatGPT compares the two audit receipts against current GitHub evidence and returns one exact remedy recommendation. No mutation is authorized by the reconciliation receipt.

### Stage D — Human selects one remedy

The human approves one exact bounded correction path or returns the plan for correction.

### Stage E — Cline recovery planning

Cline receives one `PLAN_ONLY` assignment for the approved remedy. It returns exact files, commands, expected results, risks, and stop conditions.

### Stage F — Cline bounded recovery action

Only after human approval, Cline applies the exact inverse or correction action. No validation, commit, or push is included.

### Stage G — Local diff review

Cline publishes the exact local receipt. ChatGPT and the human review the exact changed paths and diff summary.

### Stage H — Validation

Only separately authorized commands run. Validation failure stops the workflow.

### Stage I — Commit

Git add and commit are separately authorized. The staged paths must exactly match the approved scope.

### Stage J — Push

Push is separately authorized. No force push. Remote head and PR changed files must be re-read immediately afterward.

### Stage K — Dual remote review

Codex performs independent remote review. ChatGPT performs the canonical exact-diff review, including Codex findings.

### Stage L — Human decision

The human accepts, authorizes one exact correction, or blocks the stage.

### Stage M — LOCKED_ACCEPTED record

Only after ChatGPT `PASS` and explicit human acceptance may accepted paths and hashes be recorded as `LOCKED_ACCEPTED`.

---

## 11. Proposed recovery decision tree

This is a proposal, not an authorization.

```text
IF local state is exactly verified and clean
AND remote f41f53 is exactly one linear commit ahead of local 0f02475
AND the extra commit changes only the legacy redirect
THEN propose a non-destructive inverse using git revert --no-commit
ELSE stop with BLOCKED_REPOSITORY_STATE_MISMATCH or BLOCKED_SUPERSESSION_CONFLICT
```

Why this is proposed:

- `git revert` records a new history-preserving correction rather than moving a published branch tip backward.
- `--no-commit` applies the inverse to the worktree and index without immediately creating a commit, allowing exact review and separate commit approval.
- `git reset` moves branch history and is prohibited for the published implementation branch.

The actual command must not run until the exact state is re-verified and separately approved.

---

## 12. Original correction scope after recovery

After successful scope recovery, the original PR review corrections remain:

```yaml
required_test_change:
  path: tests/test_foundation_contracts.py
  exact_requirement: add one focused unknown-field rejection test asserting extra_forbidden

required_CODE_RED_changes:
  path: docs/operations/CODE_RED.md
  exact_requirements:
    - fix CR-012 indentation only
    - preserve historical records
    - append exact recovery and correction checkpoints
    - update current stage and next action
```

Canonical README and AGENTS status synchronization must be explicitly planned. It must not be silently added to the original two-file correction assignment. If approved, it is a separate bounded governance synchronization stage or an explicitly expanded assignment with exact paths and rationale.

---

## 13. Assignment completeness contract

Every assignment must use `GALAX_AI_ASSIGNMENT_V1` and contain:

```yaml
assignment_id:
repository:
branch:
expected_head_sha:
contributor:
role:
mode:
authority:
objective:
required_reading: []
allowed_paths: []
prohibited_paths: []
allowed_commands: []
prohibited_actions: []
implementation_contract:
required_tests: []
stop_conditions: []
required_output:
```

Missing fields produce:

```text
BLOCKED_ASSIGNMENT_INCOMPLETE
```

---

## 14. Required receipt fields

```yaml
GALAX_AI_STAGE_RECEIPT_V1:
  assignment_id:
  contributor:
  repository:
  branch:
  starting_sha:
  ending_sha_or_patch_hash:
  mode:
  authority_source:
  objective:
  files_read: []
  files_created: []
  files_modified: []
  files_deleted: []
  commands_requested: []
  commands_run: []
  commands_rejected: []
  tests_passed: []
  tests_failed: []
  tests_skipped: []
  evidence: []
  assumptions: []
  blockers: []
  unexpected_state: []
  prohibited_actions_avoided: []
  next_allowed_action:
  commit_requested: false
  push_requested: false
  merge_requested: false
  deployment_requested: false
  status:
```

---

## 15. Universal stop conditions

Every AI stops immediately when any of these is true:

```yaml
repository_mismatch: true
branch_mismatch: true
head_SHA_mismatch: true
missing_required_document: true
assignment_incomplete: true
unexpected_changed_file: true
unexplained_local_change: true
another_active_writer: true
command_not_allowlisted: true
requested_action_not_in_plan: true
validation_failure: true
credential_or_permission_missing: true
Codex_fix_or_push_requested: true
Cline_scope_expansion_detected: true
ChatGPT_repository_write_requested: true
history_rewrite_required: true
accepted_artifact_change_without_unlock: true
```

Allowed status values include:

```text
PASS
BLOCKED
FAIL
PARTIALLY_VALIDATED_WITH_EXACT_BLOCKERS
BLOCKED_ASSIGNMENT_INCOMPLETE
BLOCKED_REPOSITORY_STATE_MISMATCH
BLOCKED_REPOSITORY_ACCESS_REQUIRED
BLOCKED_REQUIRED_DOCUMENT
BLOCKED_UNSUPPORTED_CAPABILITY
BLOCKED_SUPERSESSION_CONFLICT
FAILED_TEST
FAILED_SECURITY_GATE
REVALIDATION_REQUIRED
READY_FOR_REMOTE_REVIEW
LOCKED_ACCEPTED
```

---

## 16. Risk controls

| Risk | Control |
|---|---|
| Two AIs overwrite the same files | Cline is the only writer; Codex and ChatGPT are read-only reviewers. |
| AI continues beyond approval | Each stage has one objective and mandatory stop. |
| Stale documentation drives wrong action | Current repository and PR evidence are re-read before every assignment. |
| Accidental commit is hidden | Preserve history; use a non-destructive correction only after verification. |
| Local result is mistaken for remote proof | Require separate local receipt and remote PR verification. |
| Hallucinated success | Require exact commands, outputs, SHAs, paths, and test evidence. |
| Context loss | Record exact checkpoint in Issue #2 at every human approval boundary. |
| Auto-approval causes damage | Cline auto-approval and YOLO remain disabled. |
| Codex makes an unsolicited fix | Review-only assignment; `@codex fix` prohibited. |
| ChatGPT repeats a direct remote write | Repository content and ref mutation prohibited for ChatGPT during this plan. |
| Reset or force push destroys evidence | History rewrite, reset-based branch rollback, and force push prohibited. |
| Broad cleanup removes unique evidence | Cleanup requires a separate reference and evidence audit. |

---

## 17. Post-recovery hardening recommendations

These are future separate tasks, not current authorization:

1. Protect `main` and important review branches against force pushes and deletion.
2. Require pull-request review before merge.
3. Require conversation resolution.
4. Add deterministic CI checks, then make them required.
5. Configure unique status-check names.
6. Consider applying protections to administrators when operationally acceptable.
7. Add a CODEOWNERS or equivalent human review policy when the repository team structure supports it.

Do not change repository rules, workflows, or branch protection during the current recovery without a separate exact assignment.

---

## 18. Official research basis

Only primary official documentation was used for the execution model:

| Topic | Official source | Applied finding |
|---|---|---|
| Cline Plan and Act | https://docs.cline.bot/core-workflows/plan-and-act | Plan mode reads and plans; Act mode modifies and executes. Use explicit Plan → approval → Act. |
| Cline rules | https://docs.cline.bot/customization/cline-rules | Workspace `.clinerules` and `AGENTS.md` provide persistent project instructions. Exact paths improve rule activation. |
| Cline checkpoints | https://docs.cline.bot/core-workflows/checkpoints | Checkpoints use a separate shadow repository and are recovery support, not project Git acceptance. |
| Cline task scope | https://docs.cline.bot/core-workflows/task-management | One focused task per goal reduces context drift. |
| Codex AGENTS.md | https://developers.openai.com/codex/guides/agents-md | Codex reads AGENTS.md before work and layers instructions by directory. |
| Codex GitHub review | https://developers.openai.com/codex/integrations/github | Codex can review PRs; review instructions must explicitly prohibit fixes and pushes for this plan. |
| Codex cloud environment | https://developers.openai.com/codex/cloud/environments | Remote review can run in an isolated environment against selected repository state. |
| Git worktrees | https://git-scm.com/docs/git-worktree.html | Worktrees provide separate working trees but do not replace the one-writer governance rule. |
| Git revert | https://git-scm.com/docs/git-revert.html | Revert preserves published history; `--no-commit` allows inverse-diff review before commit. |
| Git reset/restore/revert distinction | https://git-scm.com/docs/git | Reset moves branch history; revert creates a new history-preserving correction. |
| GitHub protected branches | https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches | Branch protection can block force pushes/deletion and require reviews, status checks, and conversation resolution. |

Official documentation describes tool behaviour. The repository's stricter governance rules take precedence for this project.

---

## 19. Approval state

```yaml
plan_id: PHASE_2A_TRI_AI_ALIGNMENT_AND_RECOVERY_PLAN_001
plan_content_status: SAVED_FOR_HUMAN_AND_AI_REVIEW
assignment_pack_required: true
execution_authorized: false
Cline_launch_authorized: false
Codex_trigger_authorized: false
Issue_or_PR_publication_authorized: false
implementation_branch_modified_by_this_plan: false
Draft_PR_7_modified_by_this_plan: false
next_allowed_action: review_the_exact_assignment_pack
```
