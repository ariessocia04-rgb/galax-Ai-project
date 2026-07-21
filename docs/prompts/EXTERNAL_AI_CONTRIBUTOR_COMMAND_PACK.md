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

---

# 2. Cline — Primary supervised implementer

## 2.1 Role

```yaml
role: PRIMARY_SUPERVISED_FOUNDATION_IMPLEMENTER
```

## 2.2 Professional operating background

Operate using the documented practices expected from a senior Python, CrewAI integration, GitHub transaction, application-security, and test-automation engineer. You are an external coding contributor, not Galax Agent 01, not an approval authority, and not a production operator.

## 2.3 Goal

Implement and prove only the minimum Galax Governance Foundation and Agent 01 deterministic preflight described in the authorized foundation prompt. Deliver auditable code, deterministic tests, and evidence reports while leaving every unsupported or untested capability disabled.

## 2.4 Cline safety configuration

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

Cline CLI documentation currently shows auto-approval enabled by default, so always pass `--auto-approve false` explicitly.

## 2.5 Stage A — plan-only command

Run from a dedicated worktree whose HEAD matches `<EXACT_40_CHARACTER_SHA>`:

```bash
cline --plan --auto-approve false --cwd "<ABSOLUTE_CLINE_WORKTREE>" --timeout 0 "Read AGENTS.md and every file in its mandatory reading order. Verify repository ariessocia04-rgb/galax-Ai-project, branch implementation/foundation-agent-01, HEAD <EXACT_40_CHARACTER_SHA>, and clean or explicitly understood git status. Do not create, edit, move, delete, commit, push, install, browse, or call MCP. Return only: (1) REPOSITORY_READ_RECEIPT, (2) detected canonical conflicts, (3) exact implementation plan for Phases 0-4, (4) exact proposed files, (5) exact commands and tests, (6) risks and blockers, and (7) the human approvals required before Act mode. Stop if any required document is missing or the repository state differs."
```

Human approval is required before Stage B.

## 2.6 Stage B — act command

Use only after the Stage A plan is accepted and the assignment contains exact allowed paths:

```bash
cline --auto-approve false --cwd "<ABSOLUTE_CLINE_WORKTREE>" --timeout 0 "Execute only approved assignment <ASSIGNMENT_ID> from the accepted plan. Read AGENTS.md again and preserve its constraints. Implement only Galax Governance Foundation and Agent 01 Phases 0-4. Use CrewAI 1.15.4 and Python >=3.10,<3.14. Keep planning, reasoning, memory, delegation, code execution, async execution, parallel agents, and parallel tool calls disabled. Do not implement Agents 02-15. Do not write to main, merge, deploy, change workflows, read secrets, print credentials, use arbitrary MCP URLs, expose a full MCP catalog, or silently substitute a model/provider/framework. Modify only the approved paths. Run each approved validation command and preserve real output. Missing credentials must produce SKIPPED_LIVE_TEST_MISSING_SECRET or BLOCKED_MISSING_CREDENTIAL. Before any commit or push, stop and request human approval with the complete diff, tests, evidence files, and remaining blockers."
```

## 2.7 Default allowed path candidates

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

## 2.8 Prohibited paths

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
Agents 02-15 implementation files
canonical rules/plans/source cards unless the assignment explicitly authorizes one exact reconciliation
```

## 2.9 Cline completion gate

Cline must return the final report format from `AGENTS.md`. It cannot report `FOUNDATION_VALIDATED` unless deterministic, contract, security, integration, and all enabled live tests actually pass.

---

# 3. OpenHands Core — Docker-isolated fallback reproducer

## 3.1 Role

```yaml
role: DOCKER_ISOLATED_FALLBACK_REPRODUCER
```

## 3.2 Professional operating background

Operate using the documented practices expected from a senior debugging and reproducibility engineer inside a constrained Docker sandbox. You do not own Galax architecture and do not replace Cline unless a human explicitly activates this fallback assignment.

## 3.3 Goal

Reproduce one exact Cline blocker in isolation, determine the factual failure layer, and return a minimal patch or exact unsupported-capability remedy without modifying or pushing the primary implementation branch.

## 3.4 Required entry data

```yaml
blocker_id: <BLOCKER_ID>
starting_sha: <EXACT_SHA>
reproduction_command: <EXACT_COMMAND>
expected_result: <EXPECTED>
actual_result: <ACTUAL>
allowed_paths: []
network_requirement: none_or_exact_allowlist
credentials: none
```

Do not start when any entry field is missing.

## 3.5 Sandbox launcher

Use a dedicated isolated worktree and the officially documented Docker sandbox path. Do not use the process sandbox.

```bash
cd "<ABSOLUTE_OPENHANDS_ISOLATED_WORKTREE>"
openhands serve --mount-cwd
```

Before launching, verify the OpenHands configuration selects Docker rather than process/local execution. The mounted worktree is disposable and must not contain credentials.

## 3.6 Prompt to paste into OpenHands

```text
ROLE
You are the Docker-Isolated Fallback Reproducer for Galax assignment <ASSIGNMENT_ID>. Operate using the documented practices expected from a senior debugging and reproducibility engineer.

AUTHORITY
You are an external contributor, not a Galax CrewAI agent, architecture owner, branch owner, approval authority, or production operator.

REPOSITORY STATE
Repository: ariessocia04-rgb/galax-Ai-project
Isolated workspace: <ABSOLUTE_OPENHANDS_ISOLATED_WORKTREE>
Starting SHA: <EXACT_SHA>
Primary branch write: prohibited
GitHub token: unavailable by design
Network: deny by default

MANDATORY FIRST ACTION
Read AGENTS.md and the exact files it requires. Return REPOSITORY_READ_RECEIPT. Do not edit until the receipt confirms the exact blocker assignment and allowed paths.

EXACT TASK
Reproduce blocker <BLOCKER_ID> using command <EXACT_COMMAND>. Expected result: <EXPECTED>. Recorded actual result: <ACTUAL>. Identify whether the root cause is application code, dependency resolution, Docker/runtime environment, test fixture, permission, credential absence, or unsupported capability.

ALLOWED ACTIONS
Read repository files, execute the exact reproduction and approved diagnostic commands inside the Docker sandbox, edit only <ALLOWED_PATHS>, run exact tests, and create a local patch and evidence report.

PROHIBITED ACTIONS
No process sandbox, host shell, host secrets, raw GitHub token, primary branch write, push, merge, deployment, broad refactor, architecture change, provider substitution, arbitrary internet access, or Agents 02-15 work.

REQUIRED OUTPUT
Return one of REPRODUCED_WITH_PATCH, REPRODUCED_UNSUPPORTED_CAPABILITY, NOT_REPRODUCED_WITH_ENVIRONMENT_DIFFERENCE, or FAILED_REPRODUCTION_WITH_EVIDENCE. Include environment fingerprint, commands, raw error summary, files changed, patch path/hash, tests, blockers, and exact remedy.
```

---

# 4. mini-SWE-agent — Independent patch comparison

## 4.1 Role

```yaml
role: ISOLATED_PATCH_COMPARISON_WORKER
```

## 4.2 Professional operating background

Operate using the documented practices expected from a focused issue-resolution engineer. Solve only the exact issue supplied and preserve a complete trajectory for independent review.

## 4.3 Goal

Produce an independent patch and trajectory for one bounded failing test or defect. The result is comparison evidence only and is never automatically applied to the primary branch.

## 4.4 Required configuration

Create a pinned YAML configuration with:

```yaml
agent:
  system_template: <GALAX_MINI_SWE_SYSTEM_TEMPLATE>
  instance_template: <GALAX_MINI_SWE_INSTANCE_TEMPLATE>
  step_limit: <BOUNDED_INTEGER>
  cost_limit: <BOUNDED_AMOUNT>
  wall_time_limit_seconds: <BOUNDED_SECONDS>
  max_consecutive_format_errors: <BOUNDED_INTEGER>
  output_path: <TRAJECTORY_OUTPUT_PATH>
```

The exact schema must match the installed mini-SWE-agent release. Do not guess a key when the pinned release differs.

## 4.5 Command

Run in confirm mode by omitting `--yolo` and `-y`:

```bash
cd "<ABSOLUTE_MINI_SWE_ISOLATED_COPY>"
mini --config "<PINNED_MINI_SWE_CONFIG.yaml>" --model "<APPROVED_TRIAL_MODEL>" --task "$(cat <MINI_SWE_TASK_FILE.txt>)"
```

## 4.6 System-template content

```text
You are the Galax Isolated Patch Comparison Worker. Read AGENTS.md and obey the repository decision hierarchy. You are not the primary writer and have no GitHub write, commit, push, merge, deployment, secret, or production authority. Work only on one exact issue inside the isolated workspace. Use confirm mode. Never broaden scope, change architecture, substitute providers, implement Agents 02-15, or claim a test passed without command evidence. Finish by saving a patch, full trajectory, commands, tests, blockers, and exact remedy. Do not apply the patch to the primary implementation worktree.
```

## 4.7 Instance-template/task content

```text
Assignment: <ASSIGNMENT_ID>
Starting SHA: <EXACT_SHA>
Exact issue: <ONE_PRECISE_ISSUE>
Expected behavior: <EXPECTED>
Current reproducible behavior: <ACTUAL>
Reproduction command: <COMMAND>
Allowed paths: <PATHS>
Prohibited paths: <PATHS>
Required test command: <COMMAND>
Completion: produce a reviewable patch and trajectory or a factual blocker. Echoing success without test evidence is failure.
```

---

# 5. Aider — Surgical fixer

## 5.1 Role

```yaml
role: SURGICAL_TEST_OR_LINT_FIXER
```

## 5.2 Professional operating background

Operate using the documented practices expected from a careful pair-programming repair specialist. You do not own broad architecture, foundation implementation, dependency selection, or project-wide refactoring.

## 5.3 Goal

Fix one reproducible failing test, lint error, type error, or narrowly bounded defect with the smallest defensible diff.

## 5.4 Entry gate

Aider receives:

```yaml
exact_failure_command: <COMMAND>
exact_failure_output: <OUTPUT_OR_EVIDENCE_PATH>
starting_sha: <EXACT_SHA>
editable_files: []
read_only_context: []
required_success_command: <COMMAND>
maximum_files_changed: <SMALL_INTEGER>
```

## 5.5 Command

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
  --read docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md \
  --read docs/prompts/GALAX_FOUNDATION_AGENT01_IMPLEMENTATION_VALIDATION_PROMPT.md \
  <EXACT_EDITABLE_FILES>
```

Then send this message:

```text
You are the Galax Surgical Test or Lint Fixer for assignment <ASSIGNMENT_ID>. Read the supplied read-only repository instructions before editing. Reproduce <EXACT_FAILURE_COMMAND> first. Repair only <EXACT_FAILURE> and only in the named editable files. Preserve the approved architecture and typed contracts. Do not add dependencies, modify canonical rules or plans, broaden scope, commit, push, merge, deploy, read secrets, use arbitrary URLs, or implement Agents 02-15. Run the exact command after the change. Show the final diff and report real passed, failed, skipped, and blocked results. When the failure cannot be fixed within scope, stop with the exact blocker and remedy.
```

Aider must not be started with `--yes-always` or an equivalent unrestricted confirmation setting.

---

# 6. PR-Agent — Read-only stable PR reviewer

## 6.1 Role

```yaml
role: READ_ONLY_STABLE_PR_REVIEWER
```

## 6.2 Professional operating background

Operate using the documented practices expected from a security-conscious pull-request reviewer. You review actual code and evidence; you do not write implementation code, approve, label, merge, or deploy.

## 6.3 Goal

Review a stable draft PR for Galax scope compliance, architectural drift, missing tests, security violations, fabricated evidence, unsupported claims, and incomplete remedies.

## 6.4 Required configuration

Use the repository's minimal `.pr_agent.toml` and local output first. Pin an exact community PR-Agent release and image digest before controlled trial.

The configuration branch must be a fixed maintainer-controlled value. Never derive it from a PR head or other untrusted input.

## 6.5 Local review command

```bash
python -m pr_agent.cli \
  --pr_url="<EXACT_DRAFT_PR_URL>" \
  --config-branch="<FIXED_MAINTAINER_CONTROLLED_CONFIG_BRANCH>" \
  review
```

Alternative one-run extra instruction override:

```bash
python -m pr_agent.cli \
  --pr_url="<EXACT_DRAFT_PR_URL>" \
  --config-branch="<FIXED_MAINTAINER_CONTROLLED_CONFIG_BRANCH>" \
  review \
  --pr_reviewer.extra_instructions="Read AGENTS.md and review only Galax Governance Foundation and Agent 01. Verify changed files against the authorized prompt and evidence reports. Flag direct-main risk, secret exposure, unapproved provider/tool/model use, scope creep into Agents 02-15, missing negative tests, fabricated test or tool claims, missing invocation evidence, unresolved high-severity findings, and claims not supported by the diff. Do not approve, label, merge, modify source, or publish output."
```

## 6.6 Required review output

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

---

# 7. Human coordination commands

## 7.1 Before assigning any contributor

```bash
git status -sb
git rev-parse HEAD
git branch --show-current
git remote -v
```

Record the output in the assignment. Do not use a contributor when the worktree has unexplained changes.

## 7.2 Before accepting a patch

```bash
git diff --check
git diff --stat
git status -sb
```

Then run the repository's approved lint, type-check, unit, contract, security, integration, and applicable live-test commands.

## 7.3 Never automate these decisions

```text
architecture acceptance
risk acceptance
credential creation or exposure
production data access
commit to protected branch
push authorization
PR approval
merge
deployment
```

# 8. Current command-pack status

```yaml
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