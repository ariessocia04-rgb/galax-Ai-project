# AI Development Tool Strict Re-screen V2

**Date:** 2026-07-21  
**Branch:** `research/ai-qualification-framework`  
**Status:** `STRICT_RESCREEN_COMPLETE_NO_RUNTIME_ACTIVATION`  
**Qualification authority:** `docs/rules/AI_DEVELOPMENT_CONTRIBUTOR_QUALIFICATION_GATE.md`  
**Source addendum:** `docs/sources/ai-tools/AI_DEVELOPMENT_TOOL_SOURCE_ADDENDUM_V2_2026-07-21.md`

## 1. Correction to the earlier shortlist

The earlier shortlist mixed proprietary hosted services with open-source tools and omitted two strong open-source candidates. This record corrects that without deleting the earlier audit.

```yaml
earlier_conditional_shortlist:
  - Jules
  - Codex
  - Aider
  - OpenHands_Core
  - PR_Agent

strict_open_source_shortlist_v2:
  - Cline
  - OpenHands_Core
  - Aider
  - mini_SWE_agent
  - OpenCode_anomalyco

hosted_tools_not_counted_as_open_source:
  - Jules
  - Codex

specialized_backup_not_in_top_five:
  - PR_Agent
  - goose_custom_distribution

runtime_activated: []
live_tested_in_Galax: []
```

The strict open-source shortlist is not a command to run five writers. It is a candidate pool with non-overlapping proposed roles. Only one source-writing tool may own a task branch at a time.

## 2. Hard screening rules

A candidate is rejected or downgraded when any of these apply:

```text
- repository is archived, read-only, or maintenance-only;
- license or canonical repository cannot be pinned;
- permissions cannot be reduced to the exact role;
- it requires direct writes to main;
- it requires force push, workflow write, secret write, or automatic merge;
- it cannot operate in a dedicated branch/worktree or isolated sandbox;
- it has no deterministic stop, timeout, cost, or iteration bound;
- it duplicates an already-owned role without measurable additional value;
- it cannot read and obey repository rules;
- it cannot produce a reviewable diff and test evidence;
- it depends on account switching to evade quota;
- it claims success without exact test evidence;
- its public score is presented as universal accuracy.
```

## 3. Evidence grades

```yaml
Grade_A:
  meaning: official capability + active maintenance + reproducible benchmark or exact public harness
Grade_B:
  meaning: official capability + active maintenance, but no current comparable benchmark
Grade_C:
  meaning: useful specialized or backup tool with maintenance, permission, or evidence limitations
Blocked:
  meaning: fails a hard qualification gate
```

No grade is runtime approval. Galax controlled trials remain mandatory.

## 4. Final strict open-source top five

### 4.1 Cline — proposed supervised primary local implementer

```yaml
classification: CODING_WRITER
open_source: true
license: Apache-2.0
evidence_grade: B
proposed_role: SUPERVISED_PRIMARY_LOCAL_IMPLEMENTER
Galax_status: STRONG_CONDITIONAL_CANDIDATE_NOT_ACTIVATED
```

**Why it qualifies**

- Officially supports IDE, CLI, SDK, and headless workflows.
- Can read/write files, search code, apply patches, and run commands.
- Normal workflow requires explicit approval.
- Checkpoints use a shadow Git repository, allowing rollback without modifying the project’s normal Git history.
- Can be configured without hosted Cline inference by using a separately approved provider.
- Repository is active and releases are current on the record date.

**Why it was missing from V1**

The first audit evaluated only the user’s initial list. Cline was not in that list even though it has a stronger safety fit than several selected general writers.

**Why it ranks above OpenCode for writing**

Cline provides explicit human approval and checkpoint recovery. OpenCode has granular permissions but officially states that it does not sandbox the agent and begins with relatively permissive defaults.

**Mandatory Galax restrictions**

```yaml
YOLO_mode: prohibited
auto_approve_edits: prohibited
auto_approve_commands: prohibited
auto_approve_browser: prohibited
auto_approve_MCP: prohibited
workspace: dedicated_worktree
branch: dedicated_task_branch
internet: deny_unless_task_explicitly_requires_allowlisted_source
commit: human_approved_only
push: prohibited_until_diff_and_tests_approved
merge: prohibited
```

**Weaknesses**

- No universal comparable benchmark was found for current Cline releases.
- Provider quality, privacy, token limit, and cost remain separate qualification layers.
- Checkpoints reduce recovery cost but do not prove code correctness.

### 4.2 OpenHands Core — proposed autonomous sandboxed issue implementer

```yaml
classification: CODING_WRITER
open_source: core_and_agent_server_MIT_enterprise_separate
evidence_grade: A_minus_vendor_benchmark
proposed_role: AUTONOMOUS_SANDBOXED_ISSUE_IMPLEMENTER
Galax_status: STRONG_CONDITIONAL_CANDIDATE_SELF_HOSTED_ONLY_NOT_ACTIVATED
```

**Why it qualifies**

- Open-source core can be pinned and inspected.
- Official Docker sandbox is the recommended local isolation mode.
- Supports repository exploration, command execution, edits, issue work, and PR workflows.
- Official benchmark infrastructure supports SWE-bench and other coding evaluations.
- Vendor report documents 60.6% on SWE-bench Verified for the stated OpenHands setup before inference-time scaling.

**Benchmark interpretation**

The 60.6% is not an OpenHands universal accuracy score. It belongs to the exact model, harness, prompt, attempts, and benchmark environment used in that report.

**Mandatory Galax restrictions**

```yaml
allowed_variant: self_hosted_core
sandbox: Docker_only
process_sandbox: prohibited
OpenHands_Cloud_GitHub_App: prohibited_current_phase
workflow_permission: prohibited
actions_write: prohibited
webhook_write: prohibited
direct_GitHub_token_to_agent: prohibited
repository_mount: dedicated_worktree_only
network: deny_by_default
```

**Weaknesses**

- Cloud GitHub integration asks for permissions broader than Galax currently allows.
- Mounted read-write files may be changed or deleted by the agent.
- Requires provider inference or substantial local hardware.
- Official FAQ says local OpenHands is designed primarily for a single user and is not a built-in secure multi-tenant service.

### 4.3 Aider — proposed surgical fixer and test-repair specialist

```yaml
classification: CODING_WRITER
open_source: true
license: Apache-2.0
evidence_grade: B_plus_historical_benchmark
proposed_role: SURGICAL_FIX_AND_TEST_REPAIR
Galax_status: STRONG_CONDITIONAL_CANDIDATE_NOT_ACTIVATED
```

**Why it qualifies**

- Active open-source repository.
- Direct local editing, repository mapping, Git integration, lint, and test loops.
- Smaller operational surface than a broad autonomous cloud agent.
- Strong fit for exact low-risk corrections after a primary writer produces a failing test or lint result.

**Benchmark interpretation**

Aider’s public 26.3% result is from an older SWE-bench Lite setup. It is historical evidence only and cannot be compared directly with current SWE-bench Verified scores.

**Mandatory Galax restrictions**

```yaml
role: exact_small_fix_only
workspace: dedicated_worktree
auto_commit: disabled_or_explicitly_controlled
allowed_paths: required
lint_command: required
test_command: required
push: prohibited_until_human_review
merge: prohibited
```

**Weaknesses**

- Model/provider determines most capability, cost, context size, and privacy behavior.
- Automatic Git behavior can create commits earlier than Galax expects unless configured.
- No process sandbox is supplied merely by using Aider; external isolation is still required for untrusted execution.

### 4.4 mini-SWE-agent — proposed isolated issue-resolution benchmark worker

```yaml
classification: CODING_WRITER_AND_EVALUATION_HARNESS
open_source: true
license: MIT
evidence_grade: A
proposed_role: ISOLATED_ISSUE_RESOLUTION_AND_EVALUATION_WORKER
Galax_status: STRONG_CONDITIONAL_CANDIDATE_NOT_ACTIVATED
```

**Why it qualifies**

- Current official successor candidate to the original SWE-agent.
- Minimal, inspectable agent loop.
- Official repository reports scores above 74% on SWE-bench Verified for specific model/version configurations.
- Official SWE-bench leaderboard identifies exact mini-SWE-agent versions and models.
- Current releases add cost and wall-clock controls.

**Important correction**

The score belongs to the model plus mini-SWE-agent harness and exact configuration. Official leaderboard results using the same mini-SWE-agent version range widely by model, proving that “mini-SWE-agent accuracy” cannot be reduced to one number.

**Why it does not replace Cline as the daily primary writer**

- It is optimized for issue-resolution and reproducible evaluation rather than a rich human approval workflow.
- It does not provide Cline-style checkpoints or a full IDE review surface.
- It should produce a patch in an isolated environment, not receive direct repository write authority.

**Mandatory Galax restrictions**

```yaml
execution: isolated_container_or_bubblewrap
direct_GitHub_write: prohibited
output: patch_and_trajectory_only
cost_limit: required
wall_clock_limit: required
step_limit: required
network: deny_by_default
human_review_before_apply: required
```

### 4.5 OpenCode (`anomalyco/opencode`) — proposed deny-first read-only reviewer and backup writer

```yaml
classification: CODING_AGENT
open_source: true
license: MIT
evidence_grade: B
proposed_role: READ_ONLY_REVIEWER_THEN_SUPERVISED_BACKUP_WRITER
Galax_status: CONDITIONAL_CANDIDATE_NOT_ACTIVATED
canonical_repository: anomalyco/opencode
```

**Why it qualifies**

- Active current repository with frequent releases.
- Provider-agnostic and open source.
- Reads `AGENTS.md`, matching Galax repository-governance practice.
- Granular per-agent permission model can deny edits, web access, external directories, subagents, commits, and pushes.
- Can define dedicated plan, review, security, and build agents.

**Why it is not the primary writer**

- Official security documentation says there is no sandbox.
- Default permissions are relatively permissive; a deny-first Galax configuration is mandatory.
- No current directly comparable official benchmark was found for the exact OpenCode harness.

**Initial Galax role**

```yaml
mode: read_only_review
permissions:
  edit: deny
  external_directory: deny
  webfetch: deny
  websearch: deny
  task: deny
  bash:
    default: ask
    allow:
      - git status
      - git diff
      - git log
      - pytest --collect-only
    deny:
      - git commit
      - git push
      - git reset
      - git clean
      - rm
```

Only after read-only trial success may a separate supervised writer profile be evaluated.

## 5. Strong alternatives that did not enter the top five

### goose — qualified reserve, not current team member

```yaml
open_source: true
license: Apache-2.0
decision: QUALIFIED_RESERVE_CUSTOM_DISTRIBUTION_ONLY
```

**Strengths**

- Desktop, CLI, and API.
- Provider-agnostic.
- Documents sandbox mode, prompt-injection detection, tool permissions, adversary review, recipes, and subagents.

**Why not top five**

- Broad general-purpose scope duplicates CrewAI orchestration and several coding-agent roles.
- More than 70 MCP extensions substantially expand the attack surface.
- Galax currently prohibits generic remote MCP catalogs and arbitrary tool exposure.
- No current comparable coding benchmark was found for the exact goose harness.

**Reconsideration condition**

A custom distribution with zero default external extensions, an allowlisted tool set, sandbox mode, no parallel writers, and exact Galax tests.

### PR-Agent — specialized backup reviewer

```yaml
decision: SPECIALIZED_BACKUP_NOT_TOP_FIVE
role: PR_COMMENT_REVIEW_ONLY
```

**Why downgraded**

- Narrow PR-review value remains useful.
- Open-source project is community-maintained/transitioning rather than the vendor’s primary product.
- Historical repository paths and license metadata are inconsistent across indexed copies.
- Cline and OpenCode can provide controlled review while also supporting broader local workflows.

**Still potentially qualified when**

The exact `The-PR-Agent/pr-agent` commit, license, Docker digest, provider, prompts, and read/comment-only GitHub permissions are pinned and tested.

### Jules — current hosted operator, not open source

```yaml
decision: CURRENT_HOSTED_OPERATOR_OUTSIDE_OPEN_SOURCE_TOP_FIVE
```

Jules remains useful for the current GitHub-connected workflow and current available quota. It is not open source and cannot replace the open-source auditability requirement. It must remain one writer on one branch with human plan and diff review.

### Codex — hosted high-complexity standby, not open source

```yaml
decision: HOSTED_STANDBY_USAGE_BLOCKED
```

Codex remains a strong complex implementation/review candidate when the user’s authorized usage becomes available. It is not counted in the open-source five and may not bypass quota through account rotation.

## 6. Rejected or blocked candidates

| Candidate | Decision | Strict reason |
|---|---|---|
| Roo Code | `BLOCKED_ARCHIVED` | Official repository archived and read-only on 2026-05-15. |
| Original SWE-agent | `SUPERSEDED_FOR_NEW_ADOPTION` | Evaluate mini-SWE-agent as a separate current candidate. |
| `opencode-ai/opencode` | `BLOCKED_ARCHIVED_NAME_COLLISION` | Archived predecessor; current candidate is `anomalyco/opencode`. |
| Continue | `BLOCKED_MAINTENANCE_STATUS` | Do not add a new critical dependency until maintenance status materially changes and is revalidated. |
| LangGraph | `NOT_A_TEAM_WORKER_REJECTED_DUPLICATE_RUNTIME` | Orchestration framework duplicates CrewAI Flow ownership. |
| PostgreSQL + pgvector | `INFRASTRUCTURE_NOT_AI_WORKER` | Future storage/retrieval infrastructure, not coding agent. |
| Antigravity account switching | `PROHIBITED_QUOTA_EVASION` | Account rotation is not a valid reliability or capacity design. |

## 7. Strict role map without conflicts

```text
Repository rules and canonical task packet
                    ↓
          Human selects ONE writer
                    ↓
     ┌──────────────┼────────────────┐
     │              │                │
   Cline        OpenHands Core      Aider
 supervised     autonomous Docker   surgical fix
 primary        bounded issue       after exact failure
     │              │                │
     └──────────────┴────────────────┘
                    ↓
          tests + trajectory + diff
                    ↓
          OpenCode read-only review
                    ↓
      optional mini-SWE-agent isolated
      comparison on the same issue fixture
                    ↓
            human approval decision
                    ↓
          branch publication or STOP
```

Rules:

```yaml
one_active_source_writer: required
Cline_and_OpenHands_same_task: prohibited
Aider_during_primary_write: prohibited
mini_SWE_agent_direct_patch_apply: prohibited
OpenCode_initial_source_write: prohibited
reviewer_merge_authority: prohibited
automatic_merge: prohibited
force_push: prohibited
direct_main_write: prohibited
```

## 8. Three-proof qualification requirement

Every selected candidate must produce all three proof classes:

### Proof 1 — official capability and security proof

```text
license
maintenance
exact version
supported tools
permission model
sandbox/isolation
provider and data path
cost/limit controls
```

### Proof 2 — reproducible external proof

At least one:

```text
public benchmark with exact model and harness
reproducible official test harness
public issue-to-patch trajectories
independent empirical study
```

This proof is contextual only.

### Proof 3 — exact Galax controlled trial

Required for activation:

```text
read README and all rules
correct starting branch and SHA
allowed-path compliance
no unauthorized operation
exact requested change
lint/test result
repeat run consistency
bounded cost/time/steps
reviewable patch and trajectory
human acceptance
```

Current result:

```yaml
Cline_Galax_trial: NOT_PERFORMED
OpenHands_Core_Galax_trial: NOT_PERFORMED
Aider_Galax_trial: NOT_PERFORMED
mini_SWE_agent_Galax_trial: NOT_PERFORMED
OpenCode_Galax_trial: NOT_PERFORMED
activation_authorized: false
```

## 9. Qualification order

```text
1. Cline read-only repository and rule-compliance trial
2. OpenCode read-only independent review trial
3. Aider tiny deterministic fixture in isolated worktree
4. mini-SWE-agent issue fixture with patch-only output
5. OpenHands Core Docker fixture with restricted mount and no GitHub token
6. compare results, unauthorized operations, process quality, cost, and repeatability
7. human decision record
```

Do not begin the trials while the Agent 01 foundation implementation branch has an active writer on overlapping files.

## 10. Final decision

```yaml
strict_open_source_top_five:
  - Cline
  - OpenHands_Core
  - Aider
  - mini_SWE_agent
  - OpenCode_anomalyco

strong_reserve:
  - goose_custom_distribution
  - PR_Agent_read_only

current_hosted_operator:
  - Jules

hosted_standby:
  - Codex

removed_from_top_five:
  - PR_Agent

newly_added_after_strict_rescreen:
  - Cline
  - mini_SWE_agent
  - OpenCode_anomalyco

universal_accuracy_claim: prohibited
all_five_working_in_Galax: false
all_five_qualified_for_runtime: false
repository_write_access_granted: false
merge: prohibited
deployment: prohibited
```
