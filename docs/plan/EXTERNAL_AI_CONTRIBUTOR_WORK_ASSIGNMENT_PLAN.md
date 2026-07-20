# External AI Contributor Work Assignment Plan

**Status:** `WORK_DESIGNATED_NOT_ACTIVATED`  
**Scope:** Galax Governance Foundation and Agent 01 only  
**Branch:** `research/ai-qualification-framework`

## 1. Objective

Assign exact, non-overlapping responsibilities to the five paper-qualified external development contributors while preserving one active source writer per task.

The five tools do not divide the repository into five simultaneous coding zones. The primary implementation remains coherent under one writer. Other contributors enter only at controlled checkpoints.

## 2. Contributor roster

| ID | Tool | Designated role | Repository write |
|---|---|---|---|
| `CLINE-01` | Cline | Supervised primary implementation engineer | Allowed only after controlled-trial approval and exact task packet |
| `AIDER-01` | Aider | Surgical test/lint repair specialist | Allowed only after primary writer stops and one failure is assigned |
| `MSWE-01` | mini-SWE-agent | Independent isolated patch/trajectory analyst | No direct repository write |
| `OPENHANDS-01` | OpenHands Core | Docker-isolated fallback/reproduction engineer | Allowed only after primary writer stops and fallback is explicitly activated |
| `PRAGENT-01` | PR-Agent | Read-only stable PR reviewer | No source write, approval, or merge |

## 3. Agent 01 implementation work packages

### WP-00 — Repository orientation and implementation baseline

```yaml
owner: CLINE-01
estimated_working_days: 1_to_2
source_write: no_during_orientation
outputs:
  - verified repository, branch, and starting SHA
  - canonical reading receipt
  - existing project structure inventory
  - dependency and environment inventory
  - file-by-file implementation plan
  - acceptance-criterion-to-test matrix
unlock_condition:
  - human approves plan
```

No other source writer may begin during WP-00.

### WP-01 — Strict domain models and deterministic blockers

```yaml
owner: CLINE-01
estimated_working_days: 1_to_3
expected_paths:
  - src/galax_ai/models/**
  - src/galax_ai/governance/blockers.py
  - tests/unit/models/**
  - tests/contract/**
required_outputs:
  - strict Pydantic boundary models
  - forbidden extra fields
  - typed status enums
  - canonical validation errors
  - deterministic blocker tests
```

Exact paths must be adapted to the repository's existing package tree. Creating a duplicate package tree is prohibited.

### WP-02 — Governance policies, invocation evidence, and gates

```yaml
owner: CLINE-01
estimated_working_days: 2_to_4
expected_paths:
  - src/galax_ai/governance/policies.py
  - src/galax_ai/governance/invocation_ledger.py
  - src/galax_ai/governance/model_hooks.py
  - src/galax_ai/governance/tool_hooks.py
  - tests/unit/governance/**
  - tests/security/**
required_outputs:
  - fail-closed model and tool policy checks
  - append-only invocation evidence behavior
  - one-call and one-tool enforcement
  - secret/path/permission negative tests
```

No live provider profile is enabled in this work package.

### WP-03 — Repository preflight executor and Agent 01 boundary

```yaml
owner: CLINE-01
estimated_working_days: 2_to_4
expected_paths:
  - src/galax_ai/tools/repository_preflight_tool.py
  - src/galax_ai/agents/engineering_manager.py
  - src/galax_ai/gateways/github_repository_gateway.py
  - tests/unit/tools/**
  - tests/integration/preflight/**
  - tests/security/repository_boundary/**
required_outputs:
  - read-only RepositoryPreflightTool
  - Flow-owned governed tool execution
  - typed RepositoryPreflightResult
  - Agent 01 with no direct repository writes
  - branch/path/symlink/traversal/security tests
```

Agent 01 must not receive broad GitHub, shell, filesystem, Drive, Supabase, Notion, or MCP tool access.

### WP-04 — Foundation Flow, transitions, continuation, and human review request

```yaml
owner: CLINE-01
estimated_working_days: 2_to_4
expected_paths:
  - src/galax_ai/flow/foundation_flow.py
  - src/galax_ai/flow/transitions.py
  - src/galax_ai/models/checkpoints.py
  - related deterministic tests
required_outputs:
  - deterministic state transitions
  - stop on BLOCKED or FAIL
  - typed human-review request
  - continuation boundary without claiming unverified native resume
  - canonical checkpoint evidence
```

### WP-05 — Complete deterministic test suite and evidence report

```yaml
owner: CLINE-01
repair_owner_when_exact_failure_exists: AIDER-01
estimated_working_days: 3_to_5
expected_paths:
  - tests/unit/**
  - tests/contract/**
  - tests/integration/**
  - tests/security/**
  - docs/evidence/**
required_outputs:
  - unit tests
  - contract tests
  - integration tests
  - security-negative tests
  - deterministic fixture results
  - implementation evidence report
```

AIDER-01 may enter only after CLINE-01 stops and identifies one exact reproducible failure. AIDER-01 receives only the files and commands required for that failure.

### WP-06 — Independent patch and trajectory comparison

```yaml
owner: MSWE-01
estimated_working_days: 1_to_2
repository_write: prohibited
input:
  - stable repository snapshot
  - one exact issue fixture
  - starting SHA
  - acceptance criteria
  - test commands
outputs:
  - candidate patch
  - full trajectory
  - tests and command logs
  - elapsed time, steps, and cost
  - process-quality concerns
```

The patch is comparison evidence and is never auto-applied.

### WP-07 — Docker fallback or reproduction validation

```yaml
owner: OPENHANDS-01
estimated_working_days: 1_to_2
activation:
  - CLINE-01 is stopped or blocked
  - or isolated environment reproduction is specifically required
outputs:
  - Docker reproduction result
  - optional bounded fallback patch
  - trajectory and test logs
  - environment-difference analysis
```

OpenHands does not use the Cloud GitHub App, host process mode, host Docker socket, repository credentials, or shared worktree.

### WP-08 — Stable draft PR quality review

```yaml
owner: PRAGENT-01
estimated_working_days: 1_to_2
repository_write: prohibited
preconditions:
  - implementation writer stopped
  - head SHA stable
  - required tests and evidence attached
outputs:
  - prioritized confirmed findings
  - missing tests
  - unsupported claims
  - questions
  - optional improvements
```

PR-Agent begins with `publish_output=false`. Human review decides whether any comment may later be published.

### WP-09 — Human decision and controlled live-test authorization

```yaml
owner: human_coordinator
estimated_working_days: 1_to_2
allowed_decisions:
  - ACCEPT_FOR_NEXT_TEST_GATE
  - RETURN_TO_CLINE
  - ASSIGN_EXACT_AIDER_REPAIR
  - REQUEST_OPENHANDS_REPRODUCTION
  - REJECT_AND_STOP
merge: prohibited
deployment: prohibited
```

## 4. Ownership locks

```yaml
CLINE_01_active:
  AIDER_01_source_write: blocked
  OPENHANDS_01_source_write: blocked

AIDER_01_active:
  CLINE_01_source_write: blocked
  OPENHANDS_01_source_write: blocked

OPENHANDS_01_active:
  CLINE_01_source_write: blocked
  AIDER_01_source_write: blocked

MSWE_01_active:
  repository_write: false
  primary_writer_may_continue: only_when_fixture_snapshot_is_frozen_and_no_shared_workspace_exists

PRAGENT_01_active:
  source_write: false
  reviewed_head_SHA_must_remain_stable: true
```

If the PR head changes during review, the review is stale and must restart against the new SHA.

## 5. Handoff transitions

```text
CLINE-01 → AIDER-01
Required: stopped writer, exact failure, clean worktree, current SHA, editable file list, reproduction command.

CLINE-01 → OPENHANDS-01
Required: stopped writer, complete handoff, clean isolated snapshot, exact blocker or remaining goal.

CLINE-01 → MSWE-01
Required: frozen snapshot, issue fixture, no direct write, bounded environment.

CLINE-01/AIDER-01 → PRAGENT-01
Required: stable draft PR, final head SHA, test evidence, source writers stopped.

Any contributor → Human
Required: common handoff schema, claims with evidence, blockers and remaining work.
```

## 6. Estimated schedule

```yaml
best_case_working_days: 10
realistic_working_days: 14_to_20
high_rework_or_blocked_case: 21_to_35
```

This is not five-way parallel implementation. The improvement comes from specialization, fallback capacity, independent comparison, and stronger defect detection.

## 7. Completion quality target

After all controlled role trials and required task gates pass:

```yaml
internal_engineering_process_target: 85_to_92_out_of_100
not_a_bug_free_probability: true
required_conditions:
  unauthorized_operations: 0
  fabricated_evidence: 0
  required_tests_executed: 100_percent
  security_negative_tests_passed: 100_percent
  unresolved_high_severity_findings: 0
  stable_repeated_results: true
  human_acceptance: true
```

No contributor or coordinator may promise 100% defect-free output.

## 8. Current state

```yaml
work_packages_defined: true
contributors_installed: false
contributors_connected_to_repository: false
controlled_trials_completed: false
repository_write_authorized: false
MCP_gateway_implemented: false
merge_authorized: false
deployment_authorized: false
```
