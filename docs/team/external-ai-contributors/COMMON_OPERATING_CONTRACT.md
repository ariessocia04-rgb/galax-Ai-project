# Galax External AI Contributor Common Operating Contract

**Status:** `DESIGNATED_NOT_ACTIVATED`  
**Applies to:** Cline, OpenHands Core, Aider, mini-SWE-agent, and PR-Agent  
**Runtime relationship:** external development contributors only; not Galax CrewAI production agents

## 1. Governing objective

The contributor must help implement or verify only the authorized Galax Governance Foundation and Agent 01 scope while preserving the repository's canonical architecture, evidence rules, and safety boundaries.

The contributor is not authorized to decide the Galax roadmap, change the selected CrewAI foundation, activate Agents 02–15, merge, deploy, or claim production readiness.

## 2. Mandatory repository orientation

Before proposing or making any change, the contributor must:

1. Verify the repository is `ariessocia04-rgb/galax-Ai-project`.
2. Report the actual checked-out branch.
3. Report the complete 40-character HEAD SHA.
4. Run or inspect repository status and disclose dirty or untracked files.
5. Read `README.md` completely.
6. Read the final pre-prompt conflict audit.
7. Read the CrewAI 1.15.4 remediation blueprint.
8. Read every applicable file under `docs/rules/`.
9. Read the exact authorized implementation prompt.
10. Read the applicable research, source, task, and role records.
11. Inspect existing dependency, test, Docker, and project structure before proposing additions.

No edit is allowed before this orientation is reported.

## 3. Canonical reading order

```text
README.md
→ docs/research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md
→ docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
→ applicable docs/rules/**
→ docs/prompts/GALAX_FOUNDATION_AGENT01_IMPLEMENTATION_VALIDATION_PROMPT.md
→ docs/research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md
→ docs/sources/SOURCE_INDEX.md and applicable source cards
→ current external contributor role card and task packet
```

When records conflict, the newest applicable canonical decision wins. Historical documents remain evidence but cannot reactivate superseded behavior.

## 4. Current project truth

```yaml
framework_target: CrewAI_1.15.4
python_target: '>=3.10,<3.14'
process: sequential
planning: false
reasoning: false
memory: false
allow_delegation: false
allow_code_execution_for_CrewAI_agent: false
parallel_agents: false
parallel_tool_calls: false
production_agents_enabled: 0_until_tests_pass
external_contributors_inside_CrewAI_runtime: false
Agents_02_to_15: disabled
merge: prohibited
deployment: prohibited
```

External development tools may edit an authorized development branch. This does not make them CrewAI agents and does not grant them control over Flow transitions.

## 5. One-writer ownership rule

```text
one task
→ one active source writer
→ one dedicated branch or worktree
→ one declared path set
→ one verified handoff
```

No two source writers may edit overlapping files concurrently. A fallback writer starts only after the previous writer is stopped and the branch/worktree state is verified.

A read-only reviewer may inspect a stable diff but may not modify source files, create commits, push, or merge.

## 6. Required task packet

A contributor may begin only when its task packet states:

```yaml
task_id:
contributor_id:
role:
repository:
required_base_branch:
required_starting_SHA:
task_branch_or_worktree:
single_goal:
problem_statement:
in_scope_paths: []
out_of_scope_paths: []
required_reading: []
acceptance_criteria: []
required_tests: []
security_negative_tests: []
maximum_time:
maximum_steps_or_iterations:
maximum_authorized_cost:
network_policy:
secret_policy:
commit_policy:
push_policy:
stop_conditions: []
required_handoff:
```

Missing branch, SHA, allowed paths, tests, or stop conditions produces `BLOCKED_INCOMPLETE_TASK_PACKET`.

## 7. Professional execution cycle

### Phase A — Orient

- Verify repository, branch, SHA, status, and required files.
- Summarize current architecture and restrictions.
- Identify contradictions or missing evidence.
- Make no changes.

### Phase B — Plan

- State the smallest valid implementation approach.
- List files expected to change.
- Map each acceptance criterion to a code change or test.
- Identify security, compatibility, and rollback risks.
- Stop for human approval when the task is architectural, multi-file, or security-sensitive.

### Phase C — Execute

- Modify only allowed files.
- Preserve existing architecture unless a current fact proves change is required.
- Keep diffs bounded and reviewable.
- Never install or enable an unapproved provider, MCP server, model, memory system, or hosted integration.

### Phase D — Validate

- Run every required test.
- Run lint and type checks when configured.
- Run required security-negative tests.
- Record exact commands and results.
- Do not represent a skipped test as passed.

### Phase E — Handoff

- Stop editing.
- Report final SHA or patch hash.
- List all changed files.
- Include diff summary, commands, tests, blockers, remaining work, and risks.
- State explicitly whether any credential, network, write, merge, or deployment action occurred.

## 8. Universal prohibited actions

```text
direct write to main or master
force push
rebase of shared branches without explicit approval
automatic merge
deployment
workflow modification
secret creation or modification
printing or storing credentials
unrestricted GitHub token exposure
arbitrary remote MCP connection
broad filesystem access outside the authorized worktree
parallel edit of overlapping files
activation of Agents 02–15
activation of unapproved LLM profiles
replacement of CrewAI with another orchestration framework
claiming tests or tool calls that did not occur
claiming production readiness
```

## 9. Mandatory stop conditions

The contributor must stop immediately and return a blocker when:

- repository, branch, or SHA does not match;
- required canonical documentation is missing or contradictory;
- requested work exceeds authorized scope;
- an allowed-path boundary would be crossed;
- the current task requires a prohibited permission;
- a secret appears in input, output, logs, or diff;
- tests cannot be run or required infrastructure is unavailable;
- the working tree contains unexplained changes from another writer;
- implementation requires an unapproved architecture change;
- quota, time, cost, or step limit is reached;
- evidence is insufficient to make a factual claim.

Required blocker format:

```yaml
status: BLOCKED
contributor_id:
task_id:
failed_gate:
observed_state:
evidence:
files_changed_before_stop: []
commands_run: []
safe_remedy:
```

## 10. Required handoff schema

```yaml
status: COMPLETED | PARTIAL | BLOCKED | FAILED
contributor_id:
role:
task_id:
repository:
starting_branch:
starting_SHA:
ending_branch_or_worktree:
ending_SHA_or_patch_hash:
files_read: []
files_changed: []
files_created: []
files_deleted: []
commands_run: []
tests:
  passed: []
  failed: []
  skipped: []
security_negative_tests:
  passed: []
  failed: []
claims_and_evidence: []
unauthorized_operations_attempted: 0
secrets_exposed: 0
network_access_used: []
commits_created: []
push_performed: false
PR_created_or_modified: false
merge_performed: false
deployment_performed: false
blockers: []
remaining_work: []
recommended_next_owner:
human_decision_required: true
```

## 11. Acceptance rule

A contribution is not accepted because code was produced. It is eligible for human review only when:

```yaml
repository_orientation_complete: true
scope_compliance: true
unauthorized_operations: 0
fabricated_evidence: 0
required_tests_executed: 100_percent
security_negative_tests_passed: 100_percent
bounded_diff: true
handoff_complete: true
human_review: pending
```

## 12. Activation state

```yaml
role_contract_defined: true
candidate_tools_installed_by_this_record: false
credentials_configured: false
repository_write_permission_granted: false
MCP_gateway_implemented: false
live_trials_completed: false
runtime_activation_authorized: false
```
