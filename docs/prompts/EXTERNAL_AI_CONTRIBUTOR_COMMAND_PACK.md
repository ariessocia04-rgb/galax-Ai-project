# Galax External AI Contributor Command Pack

**Status:** `READY_FOR_CONTROLLED_TRIAL_SETUP`  
**Scope:** Governance Foundation and Agent 01 only  
**Production approval:** No  
**Required before use:** Replace every `<PLACEHOLDER>` with an exact value and verify it against the repository.

## 1. Universal assignment header

Attach this header to every platform-specific task:

```yaml
assignment_id: <ASSIGNMENT_ID>
repository: ariessocia04-rgb/galax-Ai-project
repository_url: https://github.com/ariessocia04-rgb/galax-Ai-project
source_research_branch: agent/agent-01-tool-inspection
implementation_branch: implementation/foundation-agent-01
starting_sha: <EXACT_40_CHARACTER_SHA>
workspace: <ABSOLUTE_DEDICATED_WORKTREE_OR_ISOLATED_COPY>
current_scope: Galax Governance Foundation and Agent 01 only
Agents_02_to_15: prohibited
main_write: prohibited
force_push: prohibited
merge: prohibited
deployment: prohibited
secrets_access: prohibited
human_owner: required_for_scope_commit_push_merge_and_deployment
```

Mandatory authority order:

```text
AGENTS.md
→ docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
→ canonical conflict audit and target
→ CrewAI remediation blueprint
→ applicable active rules and plans
→ non-conflicting Foundation prompt requirements
→ exact contributor assignment
```

Where an older record attaches `RepositoryPreflightTool` directly to Agent 01 or requires `result_as_answer`, the active Flow execution contract controls.

Every contributor must first return:

```yaml
REPOSITORY_READ_RECEIPT:
  repository:
  branch:
  head_sha:
  git_status:
  files_read: []
  canonical_decision_understood:
  assigned_role_understood:
  allowed_paths: []
  prohibited_paths: []
  detected_conflicts: []
  blockers: []
  safe_to_begin: false
```

`safe_to_begin` remains false until the exact platform entry gate is satisfied.

## 2. Active Foundation architecture all contributors must preserve

```yaml
RepositoryPreflightTool:
  owner: GalaxFoundationFlow
  invoked_by_agent: false
  calls_per_run: 1

engineering_manager:
  tools: []
  direct_tool_calls: 0
  receives: trusted_RepositoryPreflightResult
  produces: AgentTaskResult

Agent_01_LLM_calls: 1
result_as_answer_for_this_path: prohibited
hidden_second_agent_call: prohibited
HumanReviewRequest_builder: pure_Python_Pydantic
explicit_router_per_branching_stage: required
check_llm_profile_readiness_before_Agent_01: required
LLM_profiles_enabled: false
```

Required sequence:

```text
validate_run_manifest()
→ router
→ check_external_preflight_tool_availability()
→ router
→ invoke_repository_preflight_tool()
→ router
→ check_llm_profile_readiness()
→ router
→ run_agent_01_evaluation()
→ validate supported claims
→ router
→ build_human_review_request()
→ authenticated human decision pause/router
→ complete_foundation_plan()
```

No blocked route may trigger a successful stage. Offline `REPO_PERMISSION_PROFILE_DECLARED` is not live GitHub proof; live evidence must be produced separately by `GitHubRepositoryGateway` as `GITHUB_PERMISSIONS_LIVE_VALIDATED`.

# 3. Cline — Primary supervised implementer

## 3.1 Role and goal

```yaml
role: PRIMARY_SUPERVISED_FOUNDATION_IMPLEMENTER
```

Operate using the documented practices expected from a senior Python, CrewAI integration, GitHub transaction, application-security, and test-automation engineer. You are an external coding contributor, not Galax Agent 01, not an approval authority, and not a production operator.

Goal: implement and prove only the minimum Governance Foundation and Agent 01 evaluator architecture. Deliver auditable code, deterministic tests, and evidence reports while leaving unsupported, untested, or unapproved capabilities disabled.

## 3.2 Safety configuration

```yaml
auto_approve: false
YOLO: false
browser: disabled_unless_separately_approved
MCP: disabled_unless_exact_server_and_tools_are_allowlisted
read_outside_workspace: false
edit_outside_workspace: false
commit: human_approval_required
push: human_approval_required
```

Always pass `--auto-approve false` explicitly.

## 3.3 Stage A — plan-only command

```bash
cline --plan --auto-approve false --cwd "<ABSOLUTE_CLINE_WORKTREE>" --timeout 0 "Execute assignment <ASSIGNMENT_ID> in plan-only mode. Verify repository ariessocia04-rgb/galax-Ai-project, branch implementation/foundation-agent-01, exact HEAD <EXACT_40_CHARACTER_SHA>, and git status. Read AGENTS.md and its full mandatory reading order, including docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md. Do not create, edit, move, delete, install, browse, call MCP, commit, or push. Return only: (1) REPOSITORY_READ_RECEIPT, (2) canonical conflict reconciliation, (3) exact Phases 0-4 implementation plan, (4) proposed files, (5) commands and tests, (6) risks/blockers, and (7) human approval points. The plan must keep RepositoryPreflightTool Flow-owned with one call, engineering_manager.tools empty, Agent 01 direct tools zero, Agent 01 LLM calls exactly one, explicit routers for every branch, check_llm_profile_readiness before Agent 01, deterministic HumanReviewRequest construction, and separate offline/live GitHub permission evidence. Stop on any mismatch or missing record."
```

Human approval is required before Stage B.

## 3.4 Stage B — act command

Use only after the Stage A plan is accepted and the assignment contains exact allowed paths:

```bash
cline --auto-approve false --cwd "<ABSOLUTE_CLINE_WORKTREE>" --timeout 0 "Execute only approved assignment <ASSIGNMENT_ID>. Read AGENTS.md and the active Foundation Agent 01 Flow execution contract again. Implement only Phases 0-4. Use CrewAI 1.15.4 and Python >=3.10,<3.14. Keep planning, reasoning, memory, delegation, code execution, async execution, parallel agents, and parallel tool calls disabled. Implement RepositoryPreflightTool as Flow-owned and invoked exactly once. Keep engineering_manager.tools empty and Agent 01 direct tools at zero. Run Agent 01 exactly once to produce AgentTaskResult. Build HumanReviewRequest in pure Python/Pydantic without a second LLM call. Use explicit routers and prevent blocked routes from continuing. Run check_llm_profile_readiness before Agent 01 and keep both profiles disabled until exact tests and approval exist. Separate REPO_PERMISSION_PROFILE_DECLARED from GITHUB_PERMISSIONS_LIVE_VALIDATED. Do not implement Agents 02-15, write main, merge, deploy, change workflows, read secrets, print credentials, use arbitrary MCP URLs, expose a full MCP catalog, or silently substitute a model/provider/framework. Modify only approved paths. Preserve real command/test evidence. Missing credentials must produce SKIPPED_LIVE_TEST_MISSING_SECRET or BLOCKED_MISSING_CREDENTIAL. Before any commit or push, stop and request human approval with the complete diff, tests, evidence, and blockers."
```

## 3.5 Default allowed path candidates

The human assignment must narrow this list when possible:

```text
pyproject.toml
uv.lock
.python-version
src/galax_ai/**
tests/**
Dockerfile
compose.yaml
compose.yml
docker-compose.yml
.dockerignore
docs/evidence/foundation/**
docs/evidence/live-validation/**
```

Prohibited:

```text
main branch
.github/workflows/**
.env
.env.*
**/*.pem
**/*.key
**/*.p12
**/*.pfx
.ssh/**
.aws/**
.git/credentials
production data
repository secrets and settings
Agents 02-15 implementation
canonical rules/plans/source cards unless one exact reconciliation is explicitly assigned
```

Cline cannot report `FOUNDATION_VALIDATED` without the exact evidence required by the active contract and repository gates.

# 4. OpenHands Core — Docker-isolated fallback reproducer

## 4.1 Role and entry data

```yaml
role: DOCKER_ISOLATED_FALLBACK_REPRODUCER
blocker_id: <BLOCKER_ID>
starting_sha: <EXACT_SHA>
reproduction_command: <EXACT_COMMAND>
expected_result: <EXPECTED>
actual_result: <ACTUAL>
allowed_paths: []
network_requirement: none_or_exact_allowlist
credentials: none
```

Do not start when an entry field is missing. Use self-hosted OpenHands Core with a Docker sandbox, never process mode or the Cloud GitHub App. The mounted worktree must be isolated and credential-free.

## 4.2 Prompt

```text
ROLE
You are the Docker-Isolated Fallback Reproducer for Galax assignment <ASSIGNMENT_ID>. Operate as a bounded debugging and reproducibility contributor.

AUTHORITY
You are not a Galax CrewAI agent, architecture owner, branch owner, approval authority, or production operator.

MANDATORY FIRST ACTION
Read AGENTS.md, the active Foundation Agent 01 Flow execution contract, and the exact required records. Return REPOSITORY_READ_RECEIPT before any edit.

EXACT TASK
Reproduce blocker <BLOCKER_ID> from starting SHA <EXACT_SHA> using <EXACT_COMMAND>. Expected: <EXPECTED>. Recorded actual: <ACTUAL>. Identify the factual failure layer.

ALLOWED
Read scoped repository files, execute approved diagnostics inside Docker, edit only <ALLOWED_PATHS>, run exact tests, and return a local patch and evidence.

PROHIBITED
No process sandbox, host shell, host secrets, raw GitHub token, primary branch write, push, merge, deployment, architecture change, provider substitution, arbitrary internet, direct Agent 01 tool ownership, result_as_answer restoration, or Agents 02-15 work.

OUTPUT
Return REPRODUCED_WITH_PATCH, REPRODUCED_UNSUPPORTED_CAPABILITY, NOT_REPRODUCED_WITH_ENVIRONMENT_DIFFERENCE, or FAILED_REPRODUCTION_WITH_EVIDENCE with environment fingerprint, commands, error summary, patch/hash, tests, blockers, and remedy.
```

# 5. mini-SWE-agent — Independent patch comparison

## 5.1 Required configuration

```yaml
role: ISOLATED_PATCH_COMPARISON_WORKER
mode: confirm
step_limit: <BOUNDED_INTEGER>
cost_limit: <BOUNDED_AMOUNT>
wall_time_limit_seconds: <BOUNDED_SECONDS>
max_consecutive_format_errors: <BOUNDED_INTEGER>
output_path: <TRAJECTORY_OUTPUT_PATH>
```

Use a pinned configuration matching the installed release. Do not guess schema keys. Omit `--yolo` and `-y`.

```bash
cd "<ABSOLUTE_MINI_SWE_ISOLATED_COPY>"
mini --config "<PINNED_MINI_SWE_CONFIG.yaml>" --model "<APPROVED_TRIAL_MODEL>" --task "$(cat <MINI_SWE_TASK_FILE.txt>)"
```

System instruction:

```text
Read AGENTS.md and the active Foundation Agent 01 Flow execution contract. Work on one exact issue inside the isolated workspace. You are not the primary writer and have no GitHub write, commit, push, merge, deployment, secret, or production authority. Preserve Flow-owned preflight invocation, zero Agent 01 direct tools, one Agent 01 LLM call, explicit routers, readiness gates, and deterministic human-review construction. Use confirm mode. Do not broaden scope, change architecture, implement Agents 02-15, or claim tests passed without evidence. Save patch, trajectory, commands, tests, blockers, and remedy. Do not apply the patch to the primary worktree.
```

# 6. Aider — Surgical fixer

## 6.1 Entry gate and command

```yaml
role: SURGICAL_TEST_OR_LINT_FIXER
exact_failure_command: <COMMAND>
exact_failure_output: <OUTPUT_OR_EVIDENCE_PATH>
starting_sha: <EXACT_SHA>
editable_files: []
read_only_context: []
required_success_command: <COMMAND>
maximum_files_changed: <SMALL_INTEGER>
```

```bash
cd "<ABSOLUTE_AIDER_ISOLATED_WORKTREE>"
aider \
  --no-auto-commits \
  --no-dirty-commits \
  --git-commit-verify \
  --auto-lint \
  --auto-test \
  --test-cmd "<EXACT_FAILURE_COMMAND>" \
  --read AGENTS.md \
  --read docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md \
  --read docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md \
  <EXACT_EDITABLE_FILES>
```

Message:

```text
Repair only <EXACT_FAILURE> in the named editable files. Reproduce the failure first. Preserve the active Flow contract and typed boundaries. Do not add dependencies, modify canonical records, broaden scope, commit, push, merge, deploy, read secrets, restore direct Agent 01 tool ownership/result_as_answer, or implement Agents 02-15. Run the exact required success command and return the diff plus evidence or a factual blocker.
```

Never start Aider with `--yes-always` or an equivalent unrestricted confirmation setting.

# 7. PR-Agent — Read-only stable PR reviewer

## 7.1 Configuration and command

Use local output first, `publish_output=false`, a fixed maintainer-controlled config branch, and an exact pinned release/image digest.

```bash
python -m pr_agent.cli \
  --pr_url="<EXACT_DRAFT_PR_URL>" \
  --config-branch="<FIXED_MAINTAINER_CONTROLLED_CONFIG_BRANCH>" \
  review \
  --pr_reviewer.extra_instructions="Read AGENTS.md and docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md. Review only Governance Foundation and Agent 01. Verify RepositoryPreflightTool is Flow-owned and invoked once, engineering_manager.tools is empty, Agent 01 direct tools are zero, result_as_answer is absent, Agent 01 has one LLM call, every conditional stage uses explicit routers, check_llm_profile_readiness runs before Agent 01, HumanReviewRequest is pure Python/Pydantic, offline and live GitHub permission evidence are separate, blocked routes stop, profiles remain disabled without proof, and no operational/tested/merge/deployment/Agents 02-15 claim is unsupported. Flag scope creep, secret exposure, fabricated evidence, missing tests, and high-severity findings. Do not approve, label, merge, modify source, or publish output."
```

Required output:

```yaml
review_status: PASS_FOR_HUMAN_REVIEW | CHANGES_REQUIRED | BLOCKED_EVIDENCE_MISSING
scope_compliance:
architecture_compliance:
security_findings: []
missing_tests: []
unsupported_claims: []
fabricated_or_unverifiable_evidence: []
files_requiring_attention: []
recommended_next_action:
approval_given: false
merge_performed: false
```

# 8. Human coordination commands

Before assignment:

```bash
git status -sb
git rev-parse HEAD
git branch --show-current
git remote -v
```

Before accepting a patch:

```bash
git diff --check
git diff --stat
git status -sb
```

Then run the approved lint, type-check, unit, contract, security, integration, and applicable live-test commands.

Never automate architecture acceptance, risk acceptance, credential creation/exposure, production access, protected-branch commit, push authorization, PR approval, merge, or deployment.

# 9. Current command-pack status

```yaml
Foundation_Agent01_Flow_contract: specified
Cline_command: specified
OpenHands_prompt_and_launcher: specified
mini_SWE_command_and_templates: specified
Aider_command: specified
PR_Agent_command: specified
exact_versions_pinned: false
credentials_configured: false
controlled_trials_run: false
contributors_fully_qualified: false
implementation_started: false
```
