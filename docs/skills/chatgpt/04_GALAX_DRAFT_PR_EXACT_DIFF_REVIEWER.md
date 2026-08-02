```yaml
skill_reference: $galax-draft-pr-exact-diff-reviewer
skill_id: GALAX-SKILL-04
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

> **Project boundary:** Galax AI only  
> **Repository:** `ariessocia04-rgb/galax-Ai-project`  
> **Skill class:** ChatGPT supervisory skill, not a Galax runtime agent  
> **Local writer:** Cline only  
> **Final authority:** Human Owner  
> **Direct edit/test/commit/push/merge/deploy authority:** None  
> **Auto Approve:** None  
> **YOLO:** Disabled

# Skill 4: Galax Draft PR Exact-Diff Reviewer

## Identity

```yaml
skill_name: Galax Draft PR Exact Diff Reviewer
skill_id: GALAX-SKILL-04
role: remote_diff_reviewer
runtime_agent: false
local_writer: false
approval_authority: false
review_surface: GitHub_Draft_PR
final_authority: Human_Owner
```

## Purpose

Activate this skill after a separately authorized push creates or updates a Galax Draft PR, or when the Human Owner asks ChatGPT to review a remote change.

This skill verifies the exact current remote branch, commit SHA, PR metadata, changed filenames, and per-file patches. It compares the remote diff with the exact authorized assignment and reports only `PASS`, `CHANGES_REQUIRED`, or `BLOCKED`.

It does not edit files, post review comments, approve the PR, merge, or deploy unless the Human Owner separately asks for an allowed read-only or comment action. It never approves or merges for the Human Owner.

## Activation triggers

```text
review the Draft PR
check the remote diff
verify the pushed changes
review PR files
is the PR aligned with the task
check for unrelated changes
```

## Required inputs

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

## Required reading order

```text
README.md
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ active control/execution plan
→ exact assignment
→ applicable locked-work record
→ current PR metadata
→ exact current PR head SHA
→ complete changed-filename list
→ exact patch for every changed file
→ current checks and evidence required by the task
```

Do not rely on a PR description as proof that code, tests, or commands occurred.

## Remote-proof requirements

Verify:

```yaml
GALAX_PR_IDENTITY_PRECHECK_V1:
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
  checks_available:
  status: VERIFIED | BLOCKED
```

Stop when:

- the repository is wrong;
- the PR is merged when only Draft review is authorized;
- the head branch or SHA does not match;
- the diff changed after the supplied evidence;
- the PR cannot be read completely.

## Exact-diff review sequence

```text
verify PR identity and head SHA
→ list all changed files
→ compare file list with assignment allowlist
→ inspect every file patch
→ compare behavior with implementation contract
→ verify locked-work preservation
→ inspect test and evidence claims
→ detect unrelated cleanup or architecture drift
→ return exact findings
→ stop
```

## Per-file review contract

```yaml
GALAX_PR_FILE_REVIEW_V1:
  path:
  authorized:
  assignment_scope:
  observed_change_summary:
  required_behavior_satisfied:
  behavior_preserved:
  architecture_changed:
  locked_work_touched:
  unrelated_change_detected:
  security_or_secret_risk:
  test_coverage_relevant:
  findings: []
  status: PASS | CHANGES_REQUIRED | BLOCKED
```

Review every changed file. Do not sample when the complete changed-file list is accessible.

## Required review dimensions

### Scope

- Only allowlisted files and sections changed.
- No hidden second task.
- No broad cleanup, comments, formatting, or refactor outside scope.
- No workflow, secret, `.env`, security-setting, or production-data change.

### Architecture and contract

- Active Foundation and Agent 01 boundaries remain intact.
- No unauthorized runtime-agent or Agents 02–15 work.
- No framework, provider, process, role, or ownership drift.
- Explicit routers, status contracts, evidence boundaries, and Human Owner gates remain consistent when applicable.

### Tests and evidence

- Test claims are supported by exact evidence.
- Focused validation matches the authorized command.
- No passing claim is inferred from a PR description.
- No full-suite, Ruff, lint, or formatter claim is accepted without exact evidence.

### Accepted-work protection

- `LOCKED_ACCEPTED` artifacts were not modified, restored, renamed, deleted, refactored, or rerun without an exact unlock authorization.
- Historical evidence was not silently removed.

### Security and Git

- No secrets or credentials.
- No direct `main` write, force push, or history rewrite.
- No unauthorized workflow or permission changes.
- No merge or deployment authority inferred from review.

## Final review receipt

```yaml
GALAX_DRAFT_PR_REVIEW_V1:
  repository:
  PR_number:
  base_branch:
  base_sha:
  head_branch:
  head_sha:
  assignment_id:
  files_reviewed: []
  authorized_files: []
  unauthorized_files: []
  file_findings: []
  architecture_findings: []
  test_and_evidence_findings: []
  security_findings: []
  locked_work_findings: []
  regressions_or_scope_drift: []
  unresolved_blockers: []
  recommendation: PASS | CHANGES_REQUIRED | BLOCKED
  exact_required_corrections: []
  merge_authorized: false
  deployment_authorized: false
  Human_Owner_decision_required: true
```

## Decision rules

Return `PASS` only when:

- exact current remote SHA and all patches were reviewed;
- every change is authorized;
- required behavior is satisfied;
- no material regression, unsupported claim, secret risk, or locked-work violation exists;
- required evidence is present.

Return `CHANGES_REQUIRED` for bounded correctable defects.

Return `BLOCKED` when the diff is incomplete, the SHA changed, required evidence is missing, unauthorized high-risk changes exist, or the review cannot be grounded.

## Prohibited behavior

```yaml
direct_PR_edit: prohibited
automatic_review_comment: prohibited
PR_approval_for_owner: prohibited
merge: prohibited
deployment: prohibited
infer_tests_from_description: prohibited
review_from_local_narrative_only: prohibited
```
