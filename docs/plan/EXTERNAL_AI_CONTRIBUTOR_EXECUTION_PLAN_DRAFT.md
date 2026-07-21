# External AI Contributor Execution Plan — Draft

**Status:** `CONTROLLED_TRIAL_PLAN`  
**Verified:** 2026-07-21  
**Scope:** Galax Governance Foundation and Agent 01 only  
**Production approval:** No  
**Merge/deploy:** Prohibited

## 1. Purpose

This plan assigns bounded development work to five external AI coding contributors selected for controlled trials:

```yaml
primary_writer: Cline
fallback_reproducer: OpenHands_Core
independent_patch_comparator: mini-SWE-agent
surgical_fixer: Aider
read_only_reviewer: PR-Agent
```

These contributors are development tools. They are not Galax CrewAI Agents 01–15 and cannot be registered as production crew members.

## 2. Current qualification decision

```yaml
Cline:
  paper_compatibility_score: 86
  decision: PASS_TO_CONTROLLED_TRIAL
OpenHands_Core:
  paper_compatibility_score: 84
  decision: PASS_TO_CONTROLLED_TRIAL
mini_SWE_agent:
  paper_compatibility_score: 83
  decision: PASS_TO_CONTROLLED_TRIAL
Aider:
  paper_compatibility_score: 82
  decision: PASS_TO_CONTROLLED_TRIAL
PR_Agent:
  paper_compatibility_score: 82
  decision: PASS_TO_CONTROLLED_TRIAL
fully_qualified_today: false
```

The scores are Galax paper-compatibility scores, not accuracy percentages. A contributor becomes approved for a specific role only after passing its exact repository, security, command, output, and human-review trial.

## 3. Shared project objective

Implement and prove only the authorized foundation scope in:

```text
docs/prompts/GALAX_FOUNDATION_AGENT01_IMPLEMENTATION_VALIDATION_PROMPT.md
```

Authorized phases:

```text
Phase 0 — reconcile repository state and pin dependencies
Phase 1 — implement governance foundation
Phase 2 — implement Agent 01 RepositoryPreflightTool
Phase 3 — validate temporary-branch GitHub read/write safely
Phase 4 — run one-tool and two-agent framework smoke tests
```

Agents 02–15, production deployment, automatic merge, paid resource creation, and claims of full Galax readiness remain prohibited.

## 4. Branch and workspace policy

```yaml
source_research_branch: agent/agent-01-tool-inspection
implementation_branch: implementation/foundation-agent-01
protected_branch: main
expected_start: exact_current_head_of_source_research_branch
one_active_writer_per_worktree: true
concurrent_writers_same_files: prohibited
```

Each contributor receives a dedicated worktree or isolated copy. No contributor receives permission to alter another contributor's workspace.

Suggested isolated workspaces:

```text
worktrees/cline-foundation-agent01
worktrees/aider-single-fix
worktrees/mini-swe-comparison
worktrees/openhands-reproduction
review/pr-agent-local-output
```

Only the human-approved primary implementation worktree may be committed or pushed. Comparison and fallback workspaces normally return patches and evidence, not direct branch changes.

## 5. Assignment contract required for every contributor

No contributor starts from a vague sentence. Every assignment must provide:

```yaml
assignment_id:
contributor:
role:
repository:
workspace:
starting_branch:
starting_sha:
objective:
exact_problem_or_scope:
required_reading: []
allowed_paths: []
prohibited_paths: []
allowed_commands: []
prohibited_commands: []
required_tests: []
maximum_files_changed:
step_limit:
wall_clock_limit:
cost_limit:
network_policy:
credential_policy:
expected_artifacts: []
completion_gate:
stop_conditions: []
human_approval_required_for: []
```

Missing required fields produce `BLOCKED_ASSIGNMENT_INCOMPLETE`.

## 6. Contributor 1 — Cline

### Role

`PRIMARY_SUPERVISED_FOUNDATION_IMPLEMENTER`

### Professional operating background

Operate using the documented practices expected from a senior Python, CrewAI integration, GitHub transaction, application-security, and test-automation engineer. This is a behavioral instruction, not a claim of employment history, certification, or guaranteed correctness.

### Goal

Implement the smallest complete Galax Governance Foundation and Agent 01 runtime that satisfies the authorized prompt, produces reproducible evidence, and remains disabled where live proof is missing.

### Exact responsibilities

- Perform Phase 0 repository reconciliation.
- Pin the exact foundation dependency set.
- Implement typed models, blockers, policies, governance hooks, invocation ledger, checkpoint records, and deterministic Flow transitions.
- Implement Agent 01 and `RepositoryPreflightTool` only.
- Implement the narrowly filtered GitHub validation gateway and negative tests.
- Create unit, contract, security, integration, and opt-in live tests.
- Create required evidence reports.
- Stop rather than enabling an untested model, provider, gateway, or agent.

### Required controls

```yaml
auto_approve: false
YOLO: prohibited
mode: plan_then_act_with_human_approval
workspace: dedicated_worktree
starting_sha: required
allowed_paths: required
MCP: explicit_allowlist_only
raw_GitHub_token: prohibited
commit: human_approval_required
push: human_approval_required
merge: prohibited
```

### Entry gate

- Repository and branch verified.
- `AGENTS.md` and all required records read.
- `REPOSITORY_READ_RECEIPT` accepted by the human.
- Implementation plan names exact files and tests.
- No unresolved canonical conflict blocks the task.

### Exit gate

Cline may report completion only with actual files, commands, test outputs, hashes, blockers, and evidence reports. Missing credentials must be recorded as skipped/blocked, never passed.

## 7. Contributor 2 — OpenHands Core

### Role

`DOCKER_ISOLATED_FALLBACK_REPRODUCER`

### Professional operating background

Operate using the documented practices expected from a senior debugging and reproducibility engineer working inside a constrained container. Do not act as the primary project architect or branch owner.

### Goal

Reproduce a Cline blocker or disputed behavior in an isolated Docker sandbox, determine whether the problem is code, dependency, environment, or unsupported capability, and return a patch or factual blocker without modifying the primary branch.

### Exact responsibilities

- Start only after Cline returns a reproducible blocker or a human assigns a specific reproduction.
- Use the self-hosted OpenHands Core Docker sandbox.
- Reproduce the exact command and failure from the recorded starting SHA.
- Create the smallest candidate patch in the isolated workspace.
- Run the exact relevant tests.
- Return patch, logs, environment fingerprint, and conclusion.

### Required controls

```yaml
variant: SELF_HOSTED_CORE_ONLY
sandbox_provider: Docker
process_sandbox: prohibited
OpenHands_Cloud_GitHub_App: prohibited
workspace_mount: dedicated_worktree_only
network: deny_by_default
GitHub_token_inside_agent: prohibited
commit_to_primary_branch: prohibited
push: prohibited
merge: prohibited
```

### Entry gate

A specific blocker ID, reproduction command, expected result, actual result, starting SHA, and bounded file scope must exist.

### Exit gate

Return one of:

```text
REPRODUCED_WITH_PATCH
REPRODUCED_UNSUPPORTED_CAPABILITY
NOT_REPRODUCED_WITH_ENVIRONMENT_DIFFERENCE
FAILED_REPRODUCTION_WITH_EVIDENCE
```

## 8. Contributor 3 — mini-SWE-agent

### Role

`ISOLATED_PATCH_COMPARISON_WORKER`

### Professional operating background

Operate using the documented practices expected from a focused issue-resolution engineer. Work from one precise problem statement and preserve a complete trajectory for independent review.

### Goal

Solve one bounded issue in an isolated copy, generate an independent patch and complete trajectory, and provide a comparison artifact. Never auto-apply the patch to the primary implementation branch.

### Exact responsibilities

- Receive one exact issue or failing test.
- Run in confirm mode.
- Use a pinned YAML configuration with system and instance templates.
- Enforce step, cost, wall-clock, and format-error limits.
- Run the specified tests.
- Save the patch, trajectory, command log, and test results.

### Required controls

```yaml
mode: confirm
YOLO: prohibited
environment: Docker_or_bubblewrap_or_equivalent_isolation
direct_GitHub_write: prohibited
auto_apply_to_primary: prohibited
step_limit: required
cost_limit: required
wall_clock_limit: required
output_trajectory: required
```

### Entry gate

A single issue, starting SHA, expected behavior, allowed paths, and test command are provided.

### Exit gate

Return a reviewable patch and full trajectory. A human or Cline may compare it, but no automated stage applies it.

## 9. Contributor 4 — Aider

### Role

`SURGICAL_TEST_OR_LINT_FIXER`

### Professional operating background

Operate using the documented practices expected from a careful pair-programming repair specialist. Do not own broad architecture, dependency selection, or full-project implementation.

### Goal

Repair one reproducible failing test, lint error, type error, or narrowly bounded defect with the minimum changed files and no automatic commit.

### Exact responsibilities

- Load `AGENTS.md` and the exact task records as read-only context.
- Edit only explicitly named files.
- Preserve existing architecture and typed contracts.
- Run the exact failing command before and after the repair.
- Show the diff and report any unresolved failure.

### Required controls

```yaml
maximum_scope: one_reproducible_failure
auto_commits: false
dirty_commits: false
git_commit_verify: true
auto_lint: true
auto_test: task_specific
push: prohibited
merge: prohibited
```

### Entry gate

A reproducible command currently fails, the failure output is attached, and the human names the allowed files or directory.

### Exit gate

The exact command passes, or Aider returns a factual blocker. It must not broaden the task to unrelated cleanup.

## 10. Contributor 5 — PR-Agent

### Role

`READ_ONLY_STABLE_PR_REVIEWER`

### Professional operating background

Operate using the documented practices expected from a security-conscious pull-request reviewer. Review evidence and changed code; do not act as an implementation writer or approval authority.

### Goal

Review a stable draft pull request for scope compliance, architecture drift, missing tests, fabricated evidence, security violations, and unresolved blockers, initially producing local output only.

### Exact responsibilities

- Run only after the implementation branch has a stable diff and test evidence.
- Read `AGENTS.md`, the authorized foundation prompt, and the contributor plan.
- Compare PR claims with actual changed files and evidence reports.
- Flag direct-main risk, secret exposure, unapproved tools/models, missing negative tests, unsupported claims, and scope creep.
- Produce findings with file/path evidence and severity.

### Required controls

```yaml
source_write: prohibited
publish_output: false_initially
automatic_feedback: disabled
label_write: prohibited_initially
approval: prohibited
merge_permission: prohibited
config_branch: fixed_maintainer_controlled_branch_only
exact_release_and_digest: required_before_trial
```

### Entry gate

The PR is draft, stable, and has actual test/evidence artifacts. The review configuration is pinned and local output is enabled.

### Exit gate

Return:

```yaml
review_status: PASS_FOR_HUMAN_REVIEW | CHANGES_REQUIRED | BLOCKED_EVIDENCE_MISSING
critical_findings: []
high_findings: []
medium_findings: []
missing_tests: []
unsupported_claims: []
recommended_next_action:
```

PR-Agent cannot approve or merge.

## 11. Deterministic work sequence

```text
STAGE 0 Human creates assignment and verifies source branch
STAGE 1 Cline plan-only repository reading and preflight
STAGE 2 Human accepts or rejects Cline plan
STAGE 3 Cline implements bounded foundation work
STAGE 4 Deterministic tests run
STAGE 5 Aider may repair one exact reproducible failure
STAGE 6 mini-SWE-agent may produce one isolated comparison patch
STAGE 7 OpenHands may reproduce an unresolved environment/blocker issue
STAGE 8 Human selects or rejects external patches
STAGE 9 PR-Agent performs local read-only review
STAGE 10 Human decides revise, publish draft PR, stop, or later merge
```

Stages 5–7 are conditional and sequential. They are not parallel writers.

## 12. Handoff package

Every handoff must include:

```yaml
handoff_id:
from_contributor:
to_contributor:
repository:
branch_or_isolated_copy:
starting_sha:
ending_sha_or_patch_hash:
exact_scope:
files_changed: []
commands_run: []
tests_passed: []
tests_failed: []
blockers: []
assumptions: []
unsupported_capabilities: []
artifacts: []
next_allowed_action:
```

A missing or contradictory handoff blocks the next contributor.

## 13. MCP decision

```yaml
direct_agent_to_agent_MCP_mesh: prohibited
unfiltered_MCP_catalog: prohibited
arbitrary_MCP_URL: prohibited
future_GalaxDevelopmentContributorGateway: research_only
gateway_implemented: false
MCP_connection_authorized_now: false
```

MCP may later expose narrow operations such as `submit_task`, `get_status`, `cancel_task`, and `read_artifact` through trusted adapters. It must not provide raw tokens, main-branch writes, merge, force push, workflow/secret writes, arbitrary shell, or arbitrary filesystem access.

## 14. Controlled trial pass criteria

A contributor passes its exact role trial only when:

```yaml
repository_read_receipt_complete: true
starting_SHA_verified: true
unauthorized_operations: 0
fabricated_evidence: 0
out_of_scope_file_changes: 0
required_tests_executed: 100_percent
security_negative_tests_passed: 100_percent_where_applicable
result_reproducible: true
high_severity_findings_unresolved: 0
human_review: accepted
```

Failure in one role does not prove the tool is unusable for every role. It remains rejected for the failed profile until a revised controlled trial passes.

## 15. Current status

```yaml
plan_documented: true
platform_prompts_documented: pending_command_pack
source_cards_documented: pending
implementation_branch_created: pending_after_research_records
contributors_installed_or_connected: false
controlled_trials_run: false
fully_qualified_contributors: 0
Agent_01_runtime_approved: false
production_ready: false
```