# Shared Execution Protocol for External AI Development Contributors

**Status:** `MANDATORY_ROLE_PROTOCOL_RESEARCH_ONLY`  
**Scope:** External development contributors only. They are not Galax CrewAI runtime agents.

## 1. Command design standard

Every task command must contain these sections in this order:

```text
IDENTITY
BACKGROUND
GOAL
REPOSITORY AND STARTING STATE
MANDATORY READING
AUTHORIZED SCOPE
ALLOWED FILES
PROHIBITED ACTIONS
EXECUTION STEPS
REQUIRED TESTS
STOP CONDITIONS
OUTPUT AND HANDOFF CONTRACT
```

This structure is mandatory because official platform guidance consistently favors persistent repository rules, clear bounded tasks, focused context, explicit tests, and reviewable task history.

## 2. Repository-first rule

Before planning or editing, the selected contributor must:

```bash
git status --short --branch
git rev-parse --show-toplevel
git branch --show-current
git rev-parse HEAD
git diff --stat
git diff --cached --stat
```

Then it must read, in order:

1. `README.md`
2. all applicable `docs/rules/`
3. current readiness and supersession documents named by `README.md`
4. the authorized implementation prompt for the current scope
5. the exact task packet
6. relevant source files and tests

It must report the repository, actual branch, exact 40-character SHA, dirty state, and documents read before any edit.

If the repository, branch, SHA, or authorization differs from the task packet:

```yaml
status: BLOCKED_REPOSITORY_STATE_MISMATCH
files_changed: []
safe_remedy: stop_and_request_correct_starting_state
```

## 3. One-writer rule

```yaml
one_task: one_active_source_writer
parallel_overlapping_writers: prohibited
reviewer_source_write: prohibited
fallback_start: only_after_primary_writer_stops
```

A contributor owns only its assigned task branch or isolated copy. It must not inspect or modify another contributor's live workspace except through a stable handoff artifact.

## 4. Mandatory task packet

```yaml
task_id:
selected_contributor:
role:
repository: ariessocia04-rgb/galax-Ai-project
starting_branch:
starting_sha:
target_branch_or_isolated_copy:
objective:
non_goals: []
allowed_paths: []
protected_paths: []
required_documents: []
required_tests: []
maximum_files_changed:
maximum_iterations:
timeout_minutes:
maximum_approved_cost:
network_policy:
credential_policy:
commit_policy:
push_policy:
stop_conditions: []
required_output_schema:
```

No contributor may infer missing authorization. Missing fields produce `BLOCKED_INCOMPLETE_TASK_PACKET`.

## 5. Planning rule

Before edits, the contributor must return a bounded plan containing:

```yaml
understood_goal:
files_expected_to_read:
files_expected_to_change:
contracts_or_interfaces_affected:
tests_to_run:
risks:
assumptions:
questions_or_blockers:
```

The plan must not redesign the architecture, add another framework, enable prohibited CrewAI features, or expand the scope.

## 6. Work standard

Every change must be:

- minimal for the stated goal;
- consistent with existing package structure and naming;
- typed at machine-controlled boundaries;
- covered by relevant deterministic tests;
- fail-closed for permission, evidence, and security decisions;
- free of fabricated test, tool, API, or repository claims;
- documented when behavior or a contract changes;
- reversible through branch, worktree, patch, or checkpoint evidence.

## 7. Prohibited actions for every contributor

```text
write to main/master
force push
merge or approve merge
automatic merge
change workflow files or repository secrets
print or store credentials
activate Agents 02–15
activate unapproved LLM profiles
replace CrewAI 1.15.4 foundation
turn on CrewAI planning, reasoning, delegation, native memory, or parallel execution
install an unapproved dependency
open arbitrary MCP servers or URLs
claim tests passed without logs
continue after a hard blocker
```

## 8. Testing and evidence

The contributor must run only approved commands and record:

```yaml
commands_run:
  - command:
    exit_code:
    result_summary:
tests:
  collected:
  passed:
  failed:
  skipped:
lint:
type_check:
security_negative_tests:
```

A skipped test cannot be reported as passed. A missing credential must produce `SKIPPED_LIVE_TEST_MISSING_SECRET`.

## 9. Stop conditions

Stop immediately when:

- starting state is wrong;
- required evidence or authorization is missing;
- work would exceed allowed paths or file count;
- a protected file must change;
- dependency or architecture change is required but not authorized;
- a secret is detected;
- tests reveal an unrelated pre-existing failure that prevents proof;
- cost, iteration, or time limit is reached;
- another writer is active on overlapping paths.

## 10. Handoff contract

Every contributor must finish with:

```yaml
status: COMPLETE | PARTIAL | BLOCKED | FAILED
contributor:
role:
repository:
starting_branch:
starting_sha:
ending_branch_or_workspace:
ending_sha_if_any:
files_read: []
files_changed: []
files_created: []
files_deleted: []
commands_run: []
tests_run: []
tests_passed: []
tests_failed: []
security_checks: []
assumptions: []
blockers: []
remaining_work: []
unauthorized_operations_attempted: 0
fabricated_evidence_count: 0
recommended_next_owner:
human_decision_required: true
```

## 11. MCP boundary

The contributors must not call one another directly through MCP. Future integration may use a role-scoped application gateway with only:

```text
submit_task
get_status
cancel_task
read_artifact
```

The gateway must use separate workspaces and must not expose raw GitHub tokens, arbitrary shell/filesystem, main writes, force push, merge, workflows, secrets, or generic MCP catalogs.
