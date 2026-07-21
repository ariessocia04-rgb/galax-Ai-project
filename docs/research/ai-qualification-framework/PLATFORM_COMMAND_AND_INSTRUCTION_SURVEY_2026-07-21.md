# External AI Platform Command and Qualification Survey — 2026-07-21

**Status:** `OFFICIAL_SOURCE_RESEARCH_COMPLETE_CONTROLLED_TRIAL_PENDING`  
**Purpose:** Define clear repository-aware assignments and record the final paper qualification decision for external Galax development contributors.  
**Approval effect:** None. Documentation and paper scoring do not prove Galax compatibility until exact controlled trials pass.

## 1. Final paper qualification result

| Contributor | Galax paper score | Exact proposed role | Decision |
|---|---:|---|---|
| Cline | 86 | Primary supervised implementer | `PASS_TO_CONTROLLED_TRIAL` |
| OpenHands Core | 84 | Docker-isolated fallback implementer/reproducer | `PASS_TO_CONTROLLED_TRIAL` |
| mini-SWE-agent | 83 | Independent issue solver and patch comparator | `PASS_TO_CONTROLLED_TRIAL` |
| Aider | 82 | Small surgical fixes and test repair | `PASS_TO_CONTROLLED_TRIAL` |
| PR-Agent | 82 | Read-only PR reviewer | `PASS_TO_CONTROLLED_TRIAL` |
| OpenCode | 74 | Proposed reviewer or backup writer | `DECLINED` |
| goose | 77 | Proposed MCP integration/general agent | `DECLINED_NOW_RESEARCH_LATER` |

```yaml
score_meaning: Galax_paper_compatibility_not_accuracy_percentage
controlled_trial_threshold: 80
fully_qualified_today: false
next_gate: controlled_Galax_trial
```

A score of 80 or higher makes a contributor eligible only for its named controlled trial. It does not authorize installation, credentials, repository writes, commit, push, review publication, merge, deployment, MCP connection, or production use.

## 2. Professional command pattern adopted by Galax

The consistent pattern across current coding-agent platforms is:

```text
persistent repository instructions
+ one bounded task assignment
+ exact repository/branch/SHA/workspace
+ role, goal, and authority boundary
+ required reading before edits
+ exact allowed and prohibited paths
+ exact commands and tests
+ safe execution and approval mode
+ observable artifacts and evidence
+ stop conditions
+ human review
```

Vague commands such as `fix the project`, `continue`, `finish everything`, or `make it production ready` are not sufficient for a new assignment.

Every assignment must provide:

```yaml
assignment_id:
repository:
branch_or_isolated_copy:
starting_sha:
workspace:
role:
goal:
exact_scope:
required_reading: []
allowed_paths: []
prohibited_paths: []
allowed_commands: []
prohibited_commands: []
required_tests: []
network_policy:
credential_policy:
limits:
expected_artifacts: []
stop_conditions: []
human_approval_points: []
```

Professional background language must describe expected operating practices, not invent employment history, certification, or guaranteed correctness.

## 3. Repository instruction design

Galax uses:

```yaml
root_AGENTS_md: required
active_Foundation_Agent01_Flow_contract: required
platform_specific_configuration: required
one_exact_task_prompt: required
REPOSITORY_READ_RECEIPT_before_edit: required
```

`AGENTS.md` is persistent repository context. It does not replace the exact assignment.

The active Foundation authority is:

- `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`

It resolves the remaining direct-tool conflict:

```yaml
RepositoryPreflightTool_owner: GalaxFoundationFlow
RepositoryPreflightTool_calls: 1
engineering_manager_tools: []
Agent_01_direct_tools: 0
Agent_01_LLM_calls: 1
result_as_answer_for_this_path: prohibited
HumanReviewRequest: pure_Python_Pydantic
explicit_routers: required
LLM_profile_readiness_before_Agent_01: required
```

## 4. Cline — 86

### Decision

```yaml
role: PRIMARY_SUPERVISED_FOUNDATION_IMPLEMENTER
decision: PASS_TO_CONTROLLED_TRIAL
```

### Documented mechanisms considered

- Workspace rules in `.clinerules/`.
- Cross-tool `AGENTS.md` support.
- Plan and Act modes.
- File editing, terminal execution, checkpoints, CLI/headless operation, and MCP configuration.
- Explicit auto-approval controls.

### Required Galax profile

```yaml
auto_approve: false
YOLO: prohibited
first_stage: plan_only
act_stage: human_approved
workspace: dedicated_worktree
starting_sha: required
allowed_paths: required
MCP: disabled_unless_exact_allowlist
commit: human_approval_required
push: human_approval_required
```

Cline is not qualified until it proves repository-reading compliance, exact architecture adherence, protected-path refusal, evidence accuracy, and repeatable test behavior.

Official sources:

- https://docs.cline.bot/customization/cline-rules
- https://docs.cline.bot/features/auto-approve
- https://docs.cline.bot/usage/cli-overview
- https://docs.cline.bot/cli/cli-reference

## 5. OpenHands Core — 84

### Decision

```yaml
role: DOCKER_ISOLATED_FALLBACK_REPRODUCER
decision: PASS_TO_CONTROLLED_TRIAL
```

### Documented mechanisms considered

- Repository customization under `.openhands`.
- Docker sandbox support.
- CLI, SDK, local GUI, and MCP support.
- Read-write workspace mounts.
- Process mode that runs on the host without container isolation.

### Required Galax profile

```yaml
variant: SELF_HOSTED_CORE_ONLY
sandbox: Docker
process_mode: prohibited
OpenHands_Cloud_GitHub_App: prohibited
repository_mount: dedicated_isolated_worktree
network: deny_by_default
GitHub_token_inside_agent: prohibited
role: fallback_reproduction_only
```

OpenHands starts only for one exact blocker after Cline stops or a human explicitly assigns reproduction. It cannot run concurrently against overlapping primary files.

Official sources:

- https://docs.openhands.dev/openhands/usage/customization/repository
- https://docs.openhands.dev/openhands/usage/sandboxes/docker
- https://docs.openhands.dev/openhands/usage/sandboxes/overview

## 6. mini-SWE-agent — 83

### Decision

```yaml
role: ISOLATED_PATCH_COMPARISON_WORKER
decision: PASS_TO_CONTROLLED_TRIAL
```

### Documented mechanisms considered

- Task, model, and YAML configuration inputs.
- Confirmation mode and optional YOLO behavior.
- Separate system/instance templates.
- Step, cost, wall-time, and format-error limits.
- Complete trajectory output with model-call and cost metadata.
- Published benchmark results for exact model/configuration combinations.

Published benchmark results are not universal accuracy claims and are not directly transferable across model, release, configuration, or environment changes.

### Required Galax profile

```yaml
mode: confirm
YOLO: prohibited
environment: Docker_or_bubblewrap_or_equivalent
one_exact_issue: required
direct_GitHub_write: prohibited
auto_apply_patch: prohibited
step_limit: required
cost_limit: required
wall_clock_limit: required
patch_and_full_trajectory: required
```

Official sources:

- https://mini-swe-agent.com/latest/usage/mini/
- https://mini-swe-agent.com/latest/usage/config/
- https://mini-swe-agent.com/latest/reference/agents/default/
- https://mini-swe-agent.com/latest/usage/output_files/

## 7. Aider — 82

### Decision

```yaml
role: SURGICAL_TEST_OR_LINT_FIXER
decision: PASS_TO_CONTROLLED_TRIAL
```

### Documented mechanisms considered

- Repository editing and Git integration.
- Diff and undo support.
- Lint and test loops.
- Configured conventions/read-only context.
- Automatic commit behavior and controls.

### Required Galax profile

```yaml
maximum_scope: one_reproducible_failure
--no-auto-commits: required
--no-dirty-commits: required
--git-commit-verify: required
--auto-lint: required
--auto-test: task_specific
push: prohibited
```

No official native MCP client was established in the reviewed Aider documentation. Any future integration uses a bounded CLI adapter rather than assuming direct MCP support.

Official sources:

- https://aider.chat/docs/config/aider_conf.html
- https://aider.chat/docs/config/options.html
- https://aider.chat/docs/usage/conventions.html
- https://aider.chat/docs/git.html
- https://aider.chat/docs/scripting.html

## 8. PR-Agent — 82

### Decision

```yaml
role: READ_ONLY_STABLE_PR_REVIEWER
decision: PASS_TO_CONTROLLED_TRIAL
```

### Documented mechanisms considered

- Review, describe, suggestions, and questions.
- CLI, Docker, self-hosted, and GitHub integrations.
- `.pr_agent.toml` configuration.
- Repository-specific review instructions.
- Local output with `publish_output=false`.
- Config-branch trust-boundary warning.

### Required Galax profile

```yaml
source_write: prohibited
automatic_feedback: disabled
publish_output: false_initially
label_write: prohibited_initially
approval: prohibited
merge_permission: prohibited
config_branch: fixed_maintainer_controlled_value
exact_release_and_digest: required
```

The current canonical community repository and exact release/image must be pinned before trial.

Official sources:

- https://docs.pr-agent.ai/usage-guide/configuration_options/
- https://docs.pr-agent.ai/usage-guide/additional_configurations/
- https://docs.pr-agent.ai/usage-guide/automations_and_usage/
- https://github.com/The-PR-Agent/pr-agent

## 9. OpenCode — 74, declined

```yaml
role_proposed: reviewer_or_backup_writer
decision: DECLINED
blocker: SECURITY_BOUNDARY_NOT_PROVEN
```

OpenCode provides granular allow/ask/deny permissions and supports MCP and multiple agent modes. However, its official security policy states that the agent is not sandboxed and that the permission system is a user-experience approval feature rather than security isolation. It recommends Docker or a VM for true isolation.

At verification time, the official security page also listed a critical and a high advisory published on 2026-01-12 for local/server execution surfaces. Exact-release remediation and negative testing would be required before reconsideration.

Official sources:

- https://github.com/anomalyco/opencode
- https://github.com/anomalyco/opencode/security
- https://opencode.ai/docs/permissions/
- https://github.com/anomalyco/opencode/blob/dev/LICENSE

Source record:

- `docs/sources/tools/opencode/SOURCE_CARD.md`

## 10. goose — 77, declined now

```yaml
role_proposed: MCP_integration_or_general_agent
decision: DECLINED_NOW_RESEARCH_LATER
blocker: SCOPE_TOO_BROAD_AND_ROLE_DUPLICATION
```

The canonical project describes goose as a general-purpose local AI agent with desktop, CLI, and API surfaces, support for many providers, and more than 70 extensions through MCP. It is Apache-2.0 and part of the Agentic AI Foundation.

Those are useful capabilities, but the current surface is broader than the bounded Foundation need and overlaps contributor coordination and future gateway responsibilities. A future custom distribution with a minimal extension allowlist may be researched only after Agent 01 and the Governance Foundation are validated.

Official sources:

- https://github.com/aaif-goose/goose
- https://goose-docs.ai/
- https://github.com/aaif-goose/goose/blob/main/LICENSE
- https://github.com/aaif-goose/goose/blob/main/documentation/docs/guides/environment-variables.md
- https://github.com/aaif-goose/goose/blob/main/CUSTOM_DISTROS.md

Source record:

- `docs/sources/tools/goose/SOURCE_CARD.md`

## 11. MCP decision

```yaml
direct_agent_to_agent_MCP_mesh: prohibited
shared_raw_GitHub_credentials: prohibited
simultaneous_repository_writers: prohibited
unfiltered_MCP_catalog: prohibited
arbitrary_MCP_URL: prohibited
future_GalaxDevelopmentContributorGateway: research_only
gateway_implemented: false
MCP_connection_authorized_now: false
```

MCP is a protocol for tools and resources. It is not a safe multi-writer coordination system by itself.

Future concept only:

```text
Human or Development Coordinator
→ GalaxDevelopmentContributorGateway
→ submit_task | get_status | cancel_task | read_artifact
→ bounded contributor adapters
```

The future gateway must not expose raw GitHub tokens, main writes, merge, force push, workflow/secret writes, arbitrary shell, arbitrary filesystem, or arbitrary MCP URLs.

## 12. Sequential collaboration model

```text
1. Cline — primary implementation on dedicated branch
2. Aider — one exact repair after Cline stops and a reproducible failure exists
3. mini-SWE-agent — isolated comparison patch, never auto-applied
4. OpenHands Core — fallback reproduction for one unresolved blocker
5. PR-Agent — read-only review of stable draft PR
6. Human — final approve, revise, or stop decision
```

Stages 2–4 are conditional and may be skipped. They are not simultaneous writers.

## 13. Time and quality planning

For Governance Foundation and Agent 01 only:

```yaml
best_case: 10_working_days
realistic: 14_to_20_working_days
high_rework_or_blocked: 21_to_35_working_days
```

These are estimates, not guarantees.

Before controlled trials, no honest quality percentage is available. After all exact gates pass, `85–92/100` may be used only as an internal engineering-process quality target, not as a probability of bug-free output.

Conditions:

```yaml
unauthorized_operations: 0
fabricated_evidence: 0
required_tests_executed: 100_percent
security_negative_tests_passed: 100_percent
repeated_results: stable
high_severity_findings: 0_unresolved
human_review: accepted
```

## 14. Remaining gates

Every selected contributor still needs:

```text
- exact installed release or commit;
- exact license and security recheck;
- exact model/provider profile;
- environment and sandbox fingerprint;
- credential and network behavior validation;
- repository-read compliance trial;
- protected-path and unauthorized-command negative tests;
- output/evidence-contract validation;
- reproducibility trial;
- human acceptance.
```

## 15. Final factual status

```yaml
paper_research: complete
selected_candidates: 5
declined_or_deferred_candidates: 2
platform_command_pack: specified
source_cards_for_all_seven: complete
controlled_trials: not_run
contributors_installed_or_connected: false
fully_qualified_contributors: 0
production_use: prohibited
realistic_Agent01_completion: 14_to_20_working_days
MCP_mesh: prohibited
next_gate: controlled_Galax_trial
```
