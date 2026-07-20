# AI Development Contributor Final Qualification Review V3

**Date:** 2026-07-21  
**Branch:** `research/ai-qualification-framework`  
**Status:** `PAPER_QUALIFICATION_COMPLETE_LIVE_TRIAL_REQUIRED`  
**Authority:** `docs/rules/AI_DEVELOPMENT_CONTRIBUTOR_QUALIFICATION_GATE.md`

## 1. Meaning of the score

The percentages in this record are **Galax compatibility and qualification scores**, not universal AI accuracy percentages.

```yaml
score_80_to_100:
  meaning: eligible to continue to an exact controlled Galax trial
  does_not_mean: runtime approved or guaranteed correct
score_79_or_lower:
  meaning: declined from the current five
hard_gate_failure:
  meaning: blocked regardless of numeric score
```

A candidate is finally approved only after deterministic fixtures, security-negative tests, cost/quota observation, a live trial, and human review. At the time of this record, none of the candidates has completed those stages.

## 2. Current factual constraints

```yaml
Galax_runtime_framework: CrewAI_1.15.4_selected_for_validation
external_contributors_run_inside_CrewAI: false
one_active_source_writer_per_task: required
parallel_overlapping_writers: prohibited
direct_main_write: prohibited
force_push: prohibited
automatic_merge: prohibited
MCP_generic_remote_catalog: prohibited_current_phase
MCP_role_scoped_gateway: required_before_any_future_connection
```

The five tools are development contributors, not Galax production agents. They must not control the CrewAI Flow or activate Agents 02–15.

## 3. Scoring method

```yaml
weights:
  exact_task_fit: 20
  repository_workflow_and_branch_control: 15
  security_and_least_privilege: 15
  deterministic_testing_and_evidence: 15
  maintenance_license_and_supply_chain: 10
  cost_and_quota_predictability: 10
  Galax_and_CrewAI_boundary_compatibility: 10
  continuity_and_handoff_quality: 5
  total: 100
```

Scores are based on documented capability and controllability for the exact proposed role. Missing live evidence is recorded separately as a blocking activation condition.

## 4. Final scoring table

| Candidate | Proposed exact role | Paper score | Score decision | Activation decision |
|---|---|---:|---|---|
| Cline | Supervised primary local implementer | 86 | `PASS_TO_CONTROLLED_TRIAL` | `BLOCKED_LIVE_TEST_NOT_PERFORMED` |
| OpenHands Core | Autonomous Docker-isolated fallback implementer | 84 | `PASS_TO_CONTROLLED_TRIAL` | `BLOCKED_LIVE_TEST_NOT_PERFORMED` |
| Aider | Surgical fix and test-repair specialist | 82 | `PASS_TO_CONTROLLED_TRIAL` | `BLOCKED_LIVE_TEST_NOT_PERFORMED` |
| mini-SWE-agent | Isolated issue-resolution and patch-comparison worker | 83 | `PASS_TO_CONTROLLED_TRIAL` | `BLOCKED_LIVE_TEST_NOT_PERFORMED` |
| PR-Agent | Pinned self-hosted read-only PR reviewer | 82 | `PASS_TO_CONTROLLED_TRIAL` | `BLOCKED_LIVE_TEST_NOT_PERFORMED` |
| OpenCode | Read-only reviewer / backup writer | 74 | `DECLINED_BELOW_80` | `BLOCKED_SECURITY_BOUNDARY_NOT_PROVEN` |
| goose | MCP integration reserve | 77 | `DECLINED_BELOW_80_CURRENT_PHASE` | `BLOCKED_DUPLICATE_AND_MCP_SURFACE` |

## 5. Candidate reviews

### 5.1 Cline — 86/100

```yaml
role: SUPERVISED_PRIMARY_LOCAL_IMPLEMENTER
open_source: true
license: Apache-2.0
native_MCP_client: true
inside_CrewAI_runtime: false
```

**Qualification strengths**

- Active open-source IDE, CLI, and SDK implementation.
- Reads and edits project files, runs commands, and supports headless structured output.
- Native MCP client support.
- Checkpoints provide recoverable file/task snapshots through a shadow Git repository.
- Per-tool approval categories permit a human-supervised workflow.

**Score deductions**

- CLI documentation shows global auto-approval can be enabled and may default to enabled in CLI automation; Galax must explicitly set it to false.
- Cline checkpoints improve recovery but do not prove test correctness.
- Model/provider quality, privacy, token limits, and cost remain separate qualification layers.
- No current directly comparable official benchmark is accepted as a Galax accuracy score.

**Required trial configuration**

```yaml
mode: plan_then_supervised_act
auto_approve: false
YOLO: prohibited
MCP: disabled_except_explicit_allowlist
workspace: dedicated_worktree
starting_SHA: required
allowed_paths: required
timeout: required
human_approval_before_edit_or_command: required
commit_and_push: prohibited_until_review
```

### 5.2 OpenHands Core — 84/100

```yaml
role: AUTONOMOUS_DOCKER_FALLBACK_IMPLEMENTER
open_source: core_MIT_enterprise_separate
native_MCP_client: true
inside_CrewAI_runtime: false
```

**Qualification strengths**

- Open-source agent SDK, CLI, and local GUI.
- Official Docker sandbox is the recommended local isolation provider.
- Supports MCP over stdio, SSE, and Streamable HTTP.
- Supports repository exploration, commands, edits, issue workflows, and PR creation.
- Provides benchmark/evaluation infrastructure and public SWE-bench evidence for exact configurations.

**Score deductions**

- Process sandbox is explicitly unsafe and prohibited.
- Read-write mounts can be modified or deleted by the agent.
- Containers may have internet access and can use any credentials provided to them.
- Hosted GitHub integration requests broad write permission including Actions, workflows, webhooks, contents, and pull requests; that hosted integration is rejected for Galax.
- Requires paid/provider inference or qualified local hardware.

**Required trial configuration**

```yaml
variant: self_hosted_core_only
sandbox: Docker
process_mode: prohibited
GitHub_Cloud_App: prohibited
repository: dedicated_worktree_mount
network: deny_by_default
credentials_inside_agent: none
MCP: local_allowlisted_servers_only
output: patch_test_log_and_trajectory
```

### 5.3 Aider — 82/100

```yaml
role: SURGICAL_FIX_AND_TEST_REPAIR
open_source: true
license: Apache-2.0
native_MCP_client: not_documented_in_official_sources
inside_CrewAI_runtime: false
```

**Qualification strengths**

- Active open-source terminal pair programmer.
- Strong local Git integration and immediate diff/undo workflow.
- Supports automatic linting and configured test execution after edits.
- Provider-agnostic and supports local models.
- Small, exact fixes are a distinct role from a primary implementer.

**Score deductions**

- By default, Aider creates Git commits after edits and may commit pre-existing dirty work; Galax must disable or tightly control this behavior.
- Automatic testing is not enabled by default and must be configured.
- Aider itself is not a security sandbox.
- No native MCP integration was found in the official Aider documentation reviewed for this decision.
- Model/provider largely determines capability, context, cost, and privacy.

**Required trial configuration**

```yaml
scope: one_reproducible_failure_one_small_patch
workspace: dedicated_worktree
no_auto_commits: true
no_dirty_commits: true
git_commit_verify: true
auto_test: true
test_command: required
lint_command: required
MCP: not_required
push: prohibited
```

### 5.4 mini-SWE-agent — 83/100

```yaml
role: ISOLATED_ISSUE_RESOLUTION_AND_PATCH_COMPARISON
open_source: true
license: MIT
native_MCP_client: false_or_not_documented
inside_CrewAI_runtime: false
```

**Qualification strengths**

- Current minimal successor candidate to the original SWE-agent.
- Very small, inspectable control loop.
- Supports local, Docker/Podman, Singularity/Apptainer, bubblewrap, and other environments.
- Starts in confirmation mode in its interactive CLI; YOLO is optional and prohibited for Galax.
- Saves full trajectory JSON including configuration, API calls, and cost statistics.
- Official SWE-bench evidence reports above 74% for exact model/harness configurations.

**Score deductions**

- It exposes essentially only bash to the model and does not provide a rich role-scoped tool interface.
- Benchmark scores vary significantly by model and release; they are not a universal accuracy score.
- No native MCP client capability was found in the official documentation reviewed.
- It is better suited to isolated patch generation/evaluation than direct GitHub branch ownership.

**Required trial configuration**

```yaml
mode: confirm
YOLO: prohibited
environment: Docker_or_bubblewrap
network: deny_by_default
direct_GitHub_write: prohibited
output: patch_and_full_trajectory
step_limit: required
wall_clock_limit: required
cost_limit: required
human_review_before_apply: required
```

### 5.5 PR-Agent — 82/100

```yaml
role: READ_ONLY_PR_REVIEWER
open_source: true
license_for_current_canonical_repository: Apache-2.0_to_be_pinned_and_reverified
native_MCP_client: false_or_not_documented
inside_CrewAI_runtime: false
```

**Qualification strengths**

- Exact role is specialized and non-duplicative: review a stable PR diff after the writer stops.
- Supports review, describe, improve suggestions, questions, CLI, GitHub Actions, Docker, and self-hosting.
- Current canonical community repository has active 2026 releases.
- Self-hosted mode sends code directly to the selected LLM provider rather than Qodo servers.
- Can print review output locally without publishing by setting `publish_output=false`.
- Fixed releases and Docker digests can be pinned.

**Score deductions**

- It is a community-maintained legacy project donated away from Qodo's primary product.
- Historical repository paths and old indexed license metadata are inconsistent; exact canonical repository, tag, license file, and image digest must be verified before installation.
- Requires an LLM provider and consumes provider quota/cost.
- AI review remains advisory and does not replace tests, security scans, or human review.
- It has no documented native MCP role in the official sources reviewed.

**Required trial configuration**

```yaml
canonical_repository: The-PR-Agent/pr-agent
exact_release: required
Docker_digest: required
publish_output: false_initially
automatic_feedback: disabled
source_write: prohibited
label_write: prohibited_initially
merge_permission: prohibited
GitHub_token_scope: read_PR_contents_only_where_possible
```

## 6. Declined candidates

### 6.1 OpenCode — 74/100, declined

OpenCode has useful deny/ask/allow permissions, project instructions, specialized agents, and native MCP support. It is declined from the current five because its own security policy states that it does not sandbox the agent and that its permission system is a UX feature rather than security isolation. The repository also has published high/critical security advisories involving local command execution surfaces. It may be reconsidered only inside an independently audited container/VM after the current five are tested.

```yaml
status: DECLINED_BELOW_80
hard_gate: BLOCKED_SECURITY_BOUNDARY_NOT_PROVEN
```

### 6.2 goose — 77/100, declined for current phase

goose is active, Apache-2.0, MCP-native, provider-agnostic, and documents sandbox and prompt-injection controls. It is declined from the current five because its broad general-purpose scope and large MCP extension ecosystem duplicate orchestration/integration responsibilities while Galax currently prohibits generic MCP catalogs. A custom zero-extension distribution may be reconsidered after Agent 01 and the role-scoped gateway are validated.

```yaml
status: DECLINED_BELOW_80_CURRENT_PHASE
reconsider_after:
  - Agent_01_foundation_passes
  - MCP_security_blocker_resolved
  - custom_zero_default_extension_distribution_exists
```

## 7. Final five

```yaml
final_paper_qualified_five:
  - Cline
  - OpenHands_Core
  - Aider
  - mini_SWE_agent
  - PR_Agent

all_scores_at_least_80: true
finally_runtime_qualified: false
reason_not_final:
  - deterministic_Galax_fixtures_not_run
  - security_negative_tests_not_run
  - cost_and_quota_not_observed
  - live_trials_not_run
  - human_decision_records_not_created
```

## 8. Can the five be connected through MCP?

### Native MCP support matrix

| Candidate | Native MCP client documented | Safe current Galax use |
|---|---|---|
| Cline | Yes | Only explicit local allowlisted servers; MCP auto-approval off |
| OpenHands Core | Yes | Only self-hosted Docker and filtered local servers |
| Aider | No official native support found | Invoke through supervised CLI, not direct MCP |
| mini-SWE-agent | No official native support found; bash-only design | Invoke as isolated CLI/batch worker |
| PR-Agent | No official native support found | Invoke through pinned CLI/container after a PR exists |

### Decision

```yaml
direct_agent_to_agent_MCP_mesh: prohibited
all_five_as_MCP_clients: false
future_connection_pattern: GALAX_DEVELOPMENT_CONTRIBUTOR_GATEWAY
current_status: NOT_IMPLEMENTED_NOT_AUTHORIZED
```

MCP is a tool/resource protocol, not a safe multi-writer coordinator. An MCP client trusts the servers it connects to, and stdio servers run as local processes with the privileges of the client. Therefore Galax must not expose a generic GitHub/filesystem/shell catalog to all contributors.

### Future narrow gateway

```text
Human or external development coordinator
              ↓
GalaxDevelopmentContributorGateway
              ↓
submit_task | get_status | cancel_task | read_artifact
              ↓
Cline adapter | OpenHands adapter | Aider CLI adapter
mini-SWE batch adapter | PR-Agent review adapter
```

The gateway must not expose:

```text
raw GitHub token
main write
force push
merge
workflow or secret write
arbitrary shell
arbitrary filesystem
arbitrary MCP URL
one contributor's live workspace to another contributor
```

Each worker receives a separate branch/worktree and returns artifacts. The gateway is an application control plane; it is not permission for the five tools to call one another.

## 9. Conflict-free work sequence

```text
1. Cline owns the bounded implementation task branch.
2. Cline stops and produces SHA, diff, commands, tests, and blockers.
3. Aider may repair one reproducible test/lint failure after Cline is stopped.
4. mini-SWE-agent may generate an independent patch on an isolated copy for comparison; its patch is never auto-applied.
5. OpenHands Core is a fallback implementer only if Cline is stopped or blocked; it never writes concurrently to the same task.
6. PR-Agent reviews the stable draft PR with no source-write or merge authority.
7. Human decides accept, revise, or stop.
```

## 10. Estimated duration for the Agent 01 foundation

These are planning estimates, not guarantees. They assume the repository state is correct, one primary writer at a time, normal model/provider availability, and no major architecture redesign.

### Five-contributor controlled workflow

| Stage | Main owner | Estimated working days |
|---|---|---:|
| Repository orientation, environment pinning, fixture definition | Cline + human | 1–2 |
| Typed models, ledger, policies, readiness gates | Cline | 2–4 |
| Flow, Agent 01, preflight tool, governed executor | Cline | 3–5 |
| Unit, contract, security, and integration tests | Cline; Aider only for exact failures | 3–5 |
| Independent patch comparison and trajectory audit | mini-SWE-agent | 1–2, partly parallel after fixtures stabilize |
| Sandboxed fallback/reproduction check | OpenHands Core | 1–2, only on isolated copy |
| Stable PR review and human corrections | PR-Agent + human | 1–3 |
| Live provider/GitHub tests when credentials are available | human-controlled environment | 2–4 |

```yaml
best_case_working_days: 10
realistic_working_days: 14_to_20
blocked_or_high_rework_case: 21_to_35
```

The five tools do not make the work five times faster because source writers are serialized. Their primary benefit is specialization, independent verification, recovery, and better defect detection. The realistic speed improvement over one unsupervised general writer is expected to come from reduced rework, not simultaneous edits.

## 11. Expected output quality

No honest percentage can be guaranteed before trials. The expected engineering quality depends on passing the gates below.

```yaml
before_Galax_trials:
  expected_quality_claim: NOT_ESTABLISHED
  allowed_claim: strong_candidate_pool_with_documented_controls

after_all_five_role_trials_pass:
  expected_process_quality_band: 85_to_92_out_of_100
  interpretation: internal engineering process score, not defect-free probability
  conditions:
    - zero_unauthorized_operations
    - zero_fabricated_evidence
    - all_required_tests_executed
    - all_security_negative_tests_passed
    - stable_repeated_results
    - human_review_acceptance
    - no_unresolved_high_severity_findings
```

A 100/100 output guarantee is prohibited. The target is auditable, tested, bounded, and reviewable output—not perfect autonomous coding.

## 12. Final decision

```yaml
paper_qualification_complete: true
threshold: 80
passed_to_controlled_trial:
  - Cline_86
  - OpenHands_Core_84
  - Aider_82
  - mini_SWE_agent_83
  - PR_Agent_82
declined:
  - OpenCode_74
  - goose_77
runtime_activated: []
MCP_mesh_approved: false
future_narrow_gateway_approved_for_research_only: true
estimated_Agent01_foundation_duration: 14_to_20_working_days
merge: prohibited
deployment: prohibited
Agents_02_to_15: disabled
```
