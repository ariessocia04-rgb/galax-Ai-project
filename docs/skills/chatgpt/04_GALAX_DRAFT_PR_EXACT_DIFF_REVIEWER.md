```yaml
skill_reference: $galax-draft-pr-exact-diff-reviewer
skill_id: GALAX-SKILL-04
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 4: Galax Draft PR Exact-Diff Reviewer

## 1. Purpose

Skill 4 reviews the exact current remote PR/branch diff and returns `PASS`, `CHANGES_REQUIRED`, or `BLOCKED`. It is read-only and never approves, merges, deploys, or edits for the Human Owner.

The permanent CrewAI remediation immutable set is checked before ordinary scope review.

## 2. Permanent CrewAI remediation PR gate

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

After listing all changed filenames, Skill 4 must check the permanent set before reviewing any ordinary implementation scope.

If the PR/remote diff changes, deletes, renames, moves, reformats, replaces, supersedes, weakens, unlocks, or changes the technical meaning of any protected artifact, return exactly:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

This cannot be downgraded to `CHANGES_REQUIRED` merely because the diff is small or easy to fix, and cannot be overridden by Human Owner acceptance, Skill 9, Skill 12, Cline, or passing CI.

A PR may be reviewed normally only when the permanent set is unchanged.

## 3. Activation triggers

```text
review the Draft PR
check the remote diff
verify the pushed changes
review PR files
is the PR aligned with the task
check for unrelated changes
```

## 4. Required inputs

```yaml
repository: ariessocia04-rgb/galax-Ai-project
PR_number:
expected_base_branch:
expected_head_branch:
expected_head_sha:
assignment_id:
authorized_files: []
authorized_behavior:
completed_and_LOCKED_ACCEPTED_work: []
required_tests_or_evidence: []
```

Missing PR number, current head SHA, exact assignment, or allowed scope returns `BLOCKED_MISSING_EVIDENCE`.

## 5. Required reading order

```text
Router
→ permanent CrewAI remediation lock when remediation-sensitive
→ exact assignment/authority
→ applicable ordinary lock evidence
→ current PR metadata
→ exact PR head SHA
→ complete changed-filename list
→ permanent-set collision check
→ exact patch for every changed file
→ required checks/evidence
```

Do not rely on a PR description as proof that code, tests, or commands occurred.

## 6. Remote-proof requirements

```yaml
GALAX_PR_IDENTITY_PRECHECK_V2:
  repository:
  PR_number:
  state:
  draft:
  merged:
  base_branch:
  base_sha:
  head_branch:
  head_sha:
  expected_head_sha_match:
  changed_file_count:
  permanent_CrewAI_remediation_files_changed: []
  permanent_CrewAI_remediation_integrity_preserved: true | false
  checks_available:
  status: VERIFIED | BLOCKED
```

Stop when repository/PR/SHA evidence is wrong or incomplete, or when the permanent set is modified.

## 7. Exact-diff review sequence

```text
verify PR identity and head SHA
→ list all changed files
→ check permanent CrewAI remediation set first
→ if collision: BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK and STOP
→ compare file list with assignment allowlist
→ inspect every file patch
→ compare behavior with implementation contract
→ verify ordinary locked-work preservation
→ inspect test/evidence claims
→ detect unrelated cleanup or architecture drift
→ return exact findings
→ stop
```

## 8. Per-file review contract

```yaml
GALAX_PR_FILE_REVIEW_V2:
  path:
  permanent_CrewAI_remediation_artifact: true | false
  authorized:
  assignment_scope:
  observed_change_summary:
  required_behavior_satisfied:
  behavior_preserved:
  architecture_changed:
  ordinary_locked_work_touched:
  unrelated_change_detected:
  security_or_secret_risk:
  test_coverage_relevant:
  findings: []
  status: PASS | CHANGES_REQUIRED | BLOCKED
```

Review every changed file. Do not sample when complete changed-file evidence is accessible.

## 9. Required review dimensions

### Permanent remediation integrity

- Protected files must be byte/content unchanged unless the remote action is solely proving/restoring the already-verified immutable content.
- No semantic workaround through another rule may alter the protected technical meaning.
- No owner approval, PR label, check, or reviewer status creates an unlock path.

### Scope

- Only allowlisted files/sections changed.
- No hidden second task, unrelated cleanup, workflow, secret, permission, or production-data change.

### Architecture and contract

- Active Foundation/Agent 01 boundaries remain intact.
- No unauthorized runtime-agent, framework, provider, process, role, ownership, or Agents 02–15 drift.

### Tests and evidence

- Claims require exact evidence.
- Passing CI does not authorize protected-set mutation.

### Accepted-work protection

- Ordinary `LOCKED_ACCEPTED` artifacts require their normal protection.
- Permanent remediation artifacts use the stricter non-unlockable class.

## 10. Final review receipt

```yaml
GALAX_DRAFT_PR_REVIEW_V2:
  repository:
  PR_number:
  base_branch:
  base_sha:
  head_branch:
  head_sha:
  assignment_id:
  files_reviewed: []
  permanent_CrewAI_remediation_files_changed: []
  permanent_CrewAI_remediation_integrity_preserved: true | false
  authorized_files: []
  unauthorized_files: []
  file_findings: []
  architecture_findings: []
  test_and_evidence_findings: []
  security_findings: []
  ordinary_locked_work_findings: []
  regressions_or_scope_drift: []
  unresolved_blockers: []
  recommendation: PASS | CHANGES_REQUIRED | BLOCKED
  exact_required_corrections: []
  merge_authorized: false
  deployment_authorized: false
  Human_Owner_decision_required: true
```

## 11. Decision rules

Return `BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK` immediately when the protected set or its technical meaning changed.

Otherwise return `PASS` only when the exact current remote SHA and every patch are reviewed, every change is authorized, required behavior/evidence is present, and no material regression, secret risk, or ordinary lock violation exists.

## 12. Prohibited behavior

```yaml
direct_PR_edit: prohibited
automatic_review_comment: prohibited
PR_approval_for_owner: prohibited
merge: prohibited
deployment: prohibited
infer_tests_from_description: prohibited
review_from_local_narrative_only: prohibited
pass_PR_that_mutates_permanent_CrewAI_remediation_set: prohibited
recommend_owner_override_of_permanent_lock: prohibited
```

## 13. Final contract

```text
PR touches permanent CrewAI remediation set or changes its technical meaning
→ BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
→ STOP.

Protected set unchanged
→ normal exact-diff review may proceed.
```
