# Galax External Development Contributor Operating Standard

**Status:** `MANDATORY_DESIGNATION_STANDARD_NOT_ACTIVATION`  
**Applies to:** Every external AI development contributor used on the Galax repository.

## 1. Professional instruction structure

Every contributor receives instructions in this exact order:

```text
IDENTITY
→ BACKGROUND
→ ROLE
→ GOAL
→ AUTHORITY
→ REQUIRED READING
→ REPOSITORY STATE
→ INPUTS
→ ALLOWED PATHS AND TOOLS
→ PROHIBITED ACTIONS
→ WORKFLOW
→ ACCEPTANCE CRITERIA
→ SECURITY NEGATIVE TESTS
→ LIMITS
→ STOP CONDITIONS
→ OUTPUT CONTRACT
→ HUMAN APPROVAL BOUNDARY
```

This structure is mandatory because vague prompts force the tool to infer scope, permissions, tests, and completion. Galax does not permit those decisions to be inferred.

## 2. Identity

Identify the exact product and selected role. Do not use generic titles such as “developer agent.”

Example:

```yaml
contributor: Cline
role: SUPERVISED_PRIMARY_IMPLEMENTER
task_class: bounded_cross_file_implementation
inside_CrewAI_runtime: false
```

## 3. Background

Background describes only verified capabilities relevant to the selected role. It must not contain marketing claims or unsupported accuracy percentages.

Required background fields:

```yaml
product_class:
license_or_terms:
verified_interfaces:
verified_repository_capabilities:
verified_test_capabilities:
checkpoint_or_trajectory_support:
known_security_boundary:
known_limitations:
why_selected_for_this_role:
```

## 4. Role

A role is a contract, not a persona. It must define:

```yaml
owns:
does_not_own:
may_write:
may_review:
may_run_commands:
may_use_network:
may_use_MCP:
may_commit:
may_push:
may_merge:
```

## 5. Goal

One task has one canonical goal. The goal must be testable and must not combine unrelated feature, refactor, documentation, infrastructure, and security work.

Good goal:

```text
Implement the strict Pydantic RunManifest contract and its unit tests within the declared paths without changing Flow behavior, provider configuration, or repository permissions.
```

Invalid goal:

```text
Finish Galax, improve the architecture, fix everything, and prepare deployment.
```

## 6. Authority

Authority must be explicit and least-privileged.

```yaml
repository:
required_base_branch:
required_base_sha:
work_branch:
allowed_paths: []
protected_paths: []
allowed_commands: []
prohibited_commands: []
network_policy:
credential_policy:
maximum_changed_files:
maximum_diff_size:
```

No contributor may widen its own authority.

## 7. Required reading

The contributor must read `README.md` and `AGENTS.md` first, followed by the current governance, qualification, coordination, role, task, and implementation records.

The contributor must return a reading receipt:

```yaml
reading_receipt:
  - path:
    retrieved: true_or_false
    relevant_rules: []
    conflicts_found: []
```

The receipt is not proof by itself; repository and diff checks remain mandatory.

## 8. Repository-state preflight

Before any edit:

```text
verify repository identity
verify current branch
verify complete starting SHA
inspect working-tree state
inspect existing changes
confirm allowed paths
confirm required tests exist or define the exact blocker
confirm no other writer owns overlapping paths
```

Mismatch result:

```yaml
status: BLOCKED_REPOSITORY_STATE_MISMATCH
expected:
actual:
safe_remedy:
files_changed: []
```

## 9. Plan-before-act

The selected writer must return a bounded implementation plan before editing when the task changes more than one file or crosses a system boundary.

Required plan fields:

```yaml
understood_goal:
files_to_read: []
files_expected_to_change: []
contracts_affected: []
tests_to_add_or_run: []
security_cases: []
risks: []
minimum_change_strategy:
stop_conditions: []
```

A plan is advisory. It cannot expand scope or authorize new paths.

## 10. Execution discipline

```text
inspect
→ change the smallest sufficient unit
→ run the nearest deterministic test
→ inspect result
→ continue only when still inside scope
→ run the full authorized suite
→ inspect complete diff
→ create handoff
→ stop
```

Do not perform opportunistic refactors, dependency upgrades, formatting sweeps, or documentation rewrites unless the task explicitly authorizes them.

## 11. Acceptance criteria

Every criterion must be observable.

Examples:

```yaml
acceptance_criteria:
  - strict model rejects extra fields
  - full SHA validation rejects short hashes
  - unit tests cover valid and invalid records
  - no files outside allowed paths changed
  - all required test commands were executed
  - no secret values appear in output or diff
```

Avoid criteria such as “make it professional,” “make it perfect,” or “improve quality” without measurable definitions.

## 12. Security-negative tests

Every writing task includes relevant rejection tests:

```text
wrong branch
stale SHA
path traversal
absolute path
symlink escape
secret file
workflow modification
main write
force push
merge request
unsupported architecture expansion
missing evidence
```

The contributor must record whether each applicable negative test passed.

## 13. Limits

```yaml
maximum_steps:
maximum_wall_clock:
maximum_cost_or_quota:
maximum_changed_files:
maximum_diff_size:
maximum_retries:
network_limit:
package_install_limit:
```

A limit reached produces a checkpoint and stop. It does not authorize account rotation, model substitution, wider permissions, or an unverified fallback takeover.

## 14. Stop conditions

Stop immediately on:

- wrong repository, branch, or SHA;
- incomplete task packet;
- unexpected dirty state;
- unauthorized path or command requirement;
- missing credential or tool needed for a live test;
- test failure requiring architecture or schema change outside scope;
- security boundary failure;
- quota, cost, time, or step limit;
- request to merge or deploy;
- uncertainty that could cause destructive or broad changes.

## 15. Output contract

Do not return only prose. Use the canonical handoff schema and include:

- repository and task identity;
- role and branch;
- starting and current SHA;
- exact files changed;
- exact commands and test results;
- completed and remaining requirements;
- known failures and security observations;
- resource usage;
- prohibited actions attempted;
- next safe action;
- lock release status.

## 16. Reasoning disclosure

Do not request or publish private chain-of-thought. Require:

```yaml
decision_summary:
key_evidence: []
actions_taken: []
tradeoffs: []
uncertainties: []
```

This gives an auditable rationale without relying on hidden reasoning text.

## 17. Human authority

Only the authenticated human approver may:

- approve a plan;
- allow edits after orientation;
- approve a fallback writer;
- approve publication of a branch or draft PR;
- accept or reject review findings;
- authorize a separate merge or deployment process.

No contributor may approve itself, another contributor, the system, or a merge.

## 18. Completion definition

```yaml
complete_only_when:
  - every authorized acceptance criterion has evidence
  - every required test was executed
  - no unauthorized path changed
  - no unresolved high-severity issue remains
  - handoff is complete
  - contributor stopped

not_complete_when:
  - documentation merely describes expected behavior
  - tests were skipped without an explicit blocker
  - output depends on an unverified assumption
  - another writer must silently continue from prose
```
