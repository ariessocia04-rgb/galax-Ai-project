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

| Contributor | Paper score | Exact role | Decision |
|---|---:|---|---|
| Cline | 86 | Primary supervised implementer | `PASS_TO_CONTROLLED_TRIAL` |
| OpenHands Core | 84 | Docker-isolated fallback reproducer | `PASS_TO_CONTROLLED_TRIAL` |
| mini-SWE-agent | 83 | Independent issue solver and patch comparator | `PASS_TO_CONTROLLED_TRIAL` |
| Aider | 82 | Small surgical fix and test repair | `PASS_TO_CONTROLLED_TRIAL` |
| PR-Agent | 82 | Read-only stable PR reviewer | `PASS_TO_CONTROLLED_TRIAL` |
| OpenCode | 74 | Proposed reviewer or backup writer | `DECLINED_SECURITY_BOUNDARY_NOT_PROVEN` |
| goose | 77 | Proposed MCP integration or general agent | `DECLINED_NOW_RESEARCH_LATER` |

The scores are Galax paper-compatibility scores, not AI accuracy percentages. A score of 80 or higher makes the selected candidate eligible for its exact controlled trial only. It does not activate repository permissions.

```yaml
fully_qualified_today: false
next_gate: controlled_Galax_trial
```

OpenCode and goose are not added to the active sequence. Their source cards preserve the declined/deferred research decisions without creating roles, assignments, or permissions.

## 3. Canonical Foundation objective

All contributors must follow, in priority order:

```text
AGENTS.md
→ docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
→ docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
→ applicable active rules and plans
→ docs/prompts/GALAX_FOUNDATION_AGENT01_IMPLEMENTATION_VALIDATION_PROMPT.md
→ exact platform assignment
```

The active Flow execution contract supersedes only older conflicting instructions that attach `RepositoryPreflightTool` directly to Agent 01, require an Agent 01 tool call, or use `result_as_answer` for that path.

Authorized implementation scope:

```text
Phase 0 — reconcile repository state and stale active instructions
Phase 1 — pin the minimum Foundation dependency set
Phase 2 — implement typed models, blockers, ledger, policies, and deterministic state
Phase 3 — implement Flow routers, readiness gates, Flow-owned RepositoryPreflightTool invocation, and one Agent 01 evaluation
Phase 4 — implement deterministic HumanReviewRequest construction and required unit/contract/security/integration fixtures
```

Active Foundation invariants:

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
check_llm_profile_readiness_before_agent: required
LLM_profiles_enabled: false
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

```yaml
role: PRIMARY_SUPERVISED_FOUNDATION_IMPLEMENTER
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

### Professional operating background

Operate using the documented practices expected from a senior Python, CrewAI integration, GitHub transaction, application-security, and test-automation engineer. This is a behavioral instruction, not a claim of employment history, certification, or guaranteed correctness.

### Goal and responsibilities

Implement the smallest complete Governance Foundation and Agent 01 evaluator architecture that satisfies the active Flow execution contract and leaves every unsupported or untested capability disabled.

Cline must:

- perform Phase 0 repository reconciliation;
- pin the exact Foundation dependency set;
- implement strict typed models, blockers, policies, invocation ledger, checkpoint records, and deterministic routers;
- implement `RepositoryPreflightTool` as a Flow-owned read-only external tool;
- keep `engineering_manager.tools` empty;
- run exactly one Agent 01 LLM evaluation that produces `AgentTaskResult`;
- build `HumanReviewRequest` deterministically without another LLM call;
- split offline permission declaration from live GitHub gateway evidence;
- implement applicable unit, contract, security, integration, and opt-in live tests;
- create the required evidence reports;
- stop rather than enabling an untested profile, gateway, or agent.

### Entry gate

- Repository, branch, and exact starting SHA verified.
- `AGENTS.md` and the complete mandatory reading order read.
- `REPOSITORY_READ_RECEIPT` accepted by the human.
- Plan names exact files, commands, and tests.
- No unresolved canonical conflict blocks the task.
- Cline begins in plan-only mode.

### Exit gate

Cline may report completion only with actual files, commands, test outputs, hashes, blockers, and evidence reports. Missing credentials are skipped or blocked, never passed. Commit and push require a separate human decision.

## 7. Contributor 2 — OpenHands Core

```yaml
role: DOCKER_ISOLATED_FALLBACK_REPRODUCER
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

### Goal

Reproduce one exact Cline blocker in an isolated Docker sandbox, determine whether the cause is code, dependency, environment, test fixture, permission, credential absence, or unsupported capability, and return a minimal patch or factual remedy without modifying the primary branch.

### Entry gate

A blocker ID, reproduction command, expected result, actual result, starting SHA, bounded file scope, network policy, and credential policy must exist.

### Exit gate

Return exactly one:

```text
REPRODUCED_WITH_PATCH
REPRODUCED_UNSUPPORTED_CAPABILITY
NOT_REPRODUCED_WITH_ENVIRONMENT_DIFFERENCE
FAILED_REPRODUCTION_WITH_EVIDENCE
```

Include environment fingerprint, commands, raw-error summary, patch/hash, tests, blockers, and exact remedy.

## 8. Contributor 3 — mini-SWE-agent

```yaml
role: ISOLATED_PATCH_COMPARISON_WORKER
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

### Goal

Solve one bounded issue in an isolated copy, generate an independent patch and complete trajectory, and provide comparison evidence. Never auto-apply the patch to the primary implementation branch.

### Entry and exit gates

A single issue, starting SHA, expected behavior, current reproducible behavior, allowed paths, and exact test command are required. Return a reviewable patch, full trajectory, commands, tests, blockers, and exact remedy.

## 9. Contributor 4 — Aider

```yaml
role: SURGICAL_TEST_OR_LINT_FIXER
maximum_scope: one_reproducible_failure
auto_commits: false
dirty_commits: false
git_commit_verify: true
auto_lint: true
auto_test: task_specific
push: prohibited
merge: prohibited
```

### Goal

Repair one reproducible failing test, lint error, type error, or narrowly bounded defect with the smallest defensible diff.

Aider starts only when the exact command currently fails, failure output is attached, starting SHA is known, and editable files plus the required success command are named. It must not broaden the task, change architecture, add unrelated dependencies, or perform a commit or push.

## 10. Contributor 5 — PR-Agent

```yaml
role: READ_ONLY_STABLE_PR_REVIEWER
source_write: prohibited
publish_output: false_initially
automatic_feedback: disabled
label_write: prohibited_initially
approval: prohibited
merge_permission: prohibited
config_branch: fixed_maintainer_controlled_branch_only
exact_release_and_digest: required_before_trial
```

### Goal

Review a stable draft PR for scope compliance, architecture drift, missing tests, fabricated evidence, security violations, and unresolved blockers. It must compare the implementation against `AGENTS.md`, the active Flow execution contract, the authorized Foundation prompt's non-conflicting requirements, and actual evidence artifacts.

Return:

```yaml
review_status: PASS_FOR_HUMAN_REVIEW | CHANGES_REQUIRED | BLOCKED_EVIDENCE_MISSING
critical_findings: []
high_findings: []
medium_findings: []
missing_tests: []
unsupported_claims: []
recommended_next_action:
approval_given: false
merge_performed: false
```

## 11. Deterministic work sequence

```text
STAGE 0 Human creates assignment and verifies source branch
STAGE 1 Cline plan-only repository reading and preflight
STAGE 2 Human accepts or rejects Cline plan
STAGE 3 Cline implements bounded Foundation work
STAGE 4 Deterministic tests run
STAGE 5 Aider may repair one exact reproducible failure
STAGE 6 mini-SWE-agent may produce one isolated comparison patch
STAGE 7 OpenHands may reproduce one unresolved environment or blocker issue
STAGE 8 Human selects or rejects external patches
STAGE 9 PR-Agent performs local read-only review
STAGE 10 Human decides revise, publish/update draft PR, stop, or later merge
```

Stages 5–7 are conditional and sequential. They are not parallel writers and may be skipped when their entry conditions are absent.

## 12. Handoff package

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

MCP may later expose narrow operations such as `submit_task`, `get_status`, `cancel_task`, and `read_artifact` through trusted adapters. It must not provide raw tokens, main writes, merge, force push, workflow/secret writes, arbitrary shell, arbitrary filesystem, or arbitrary MCP URLs.

## 14. Controlled trial pass criteria

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

## 15. Time and quality planning boundary

The five contributors do not make the work five times faster because simultaneous overlapping writers are prohibited. Their benefit is reduced rework, independent comparison, fallback reproduction, and earlier defect detection.

| Work | Planning estimate |
|---|---|
| Repository setup, dependency pinning, fixtures | 1–2 working days |
| Typed models, ledger, policies, gates | 2–4 working days |
| Flow, Agent 01 evaluator, preflight tool, executor | 3–5 working days |
| Unit, contract, security, integration tests | 3–5 working days |
| mini-SWE independent comparison when needed | 1–2 working days |
| OpenHands sandbox reproduction when needed | 1–2 working days |
| PR-Agent and human review | 1–3 working days |
| Live provider/GitHub tests when credentials are authorized | 2–4 working days |

```yaml
best_case: 10_working_days
realistic: 14_to_20_working_days
high_rework_or_blocked: 21_to_35_working_days
scope: Governance_Foundation_and_Agent_01_only
```

These are planning estimates, not delivery guarantees.

Before controlled trials, no honest quality percentage may be claimed. After every exact gate passes, an internal engineering-process quality target of `85–92/100` may be used only as a review target, not as a probability of being bug-free.

Required quality conditions:

```yaml
unauthorized_operations: 0
fabricated_evidence: 0
required_tests_executed: 100_percent
security_negative_tests_passed: 100_percent
repeated_results: stable
high_severity_findings: 0_unresolved
human_review: accepted
```

## 16. Current status

```yaml
plan_documented: true
Foundation_Agent01_Flow_contract_documented: true
platform_prompts_documented: true
selected_source_cards_documented: true
declined_source_cards_documented: true
implementation_branch_created: true
implementation_branch_synchronized: true
Cline_assignment_SHA_updated: true
contributors_installed_or_connected: false
exact_versions_pinned: false
controlled_trials_run: false
fully_qualified_contributors: 0
Agent_01_runtime_approved: false
production_ready: false
next_action: Cline_plan_only_ready_for_human_launch
```
