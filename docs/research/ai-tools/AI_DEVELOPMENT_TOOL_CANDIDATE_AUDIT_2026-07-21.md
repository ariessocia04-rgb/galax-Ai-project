# AI Development Tool Candidate Audit

**Date:** 2026-07-21  
**Branch:** `research/ai-qualification-framework`  
**Status:** `RESEARCH_COMPLETE_CONDITIONAL_SHORTLIST_NOT_ACTIVATED`  
**Authority:** `docs/rules/AI_DEVELOPMENT_CONTRIBUTOR_QUALIFICATION_GATE.md`  
**Sources:** `docs/sources/ai-tools/AI_DEVELOPMENT_TOOL_SOURCE_INDEX_2026-07-21.md`

## Executive decision

The proposal contains four different product classes. They must not be treated as interchangeable AI team members.

```yaml
coding_writers:
  - OpenHands
  - SWE-agent
  - Aider
  - GitHub Copilot
  - Cursor
  - Devin
  - Jules
  - Codex

PR_reviewers:
  - PR-Agent

local_operators:
  - Antigravity

orchestration_frameworks:
  - LangGraph

data_infrastructure:
  - PostgreSQL
  - pgvector

maintenance_or_product_transition_risk:
  - SWE-agent
  - Continue
```

The five strongest complementary candidates for a controlled future trial are:

1. **Jules** — primary GitHub task implementer while the exact free quota is available.
2. **Codex** — high-complexity implementation and independent code-review candidate when authorized usage is available.
3. **Aider** — supervised local surgical editor/test runner on a dedicated worktree.
4. **OpenHands Core** — self-hosted/open-source fallback implementer, not the broad-permission Cloud GitHub App.
5. **PR-Agent** — pinned, self-hosted PR reviewer; read/comment-only and never a merge authority.

This is not permission to run all five together. At most one coding writer may modify a task branch at a time. PR-Agent may review a completed diff without source-write access.

## Why no universal accuracy percentage is reported

An honest percentage requires the same task set, repository state, model/provider, prompt, tool permissions, sandbox, attempt budget, and test harness. Public results do not meet those conditions across this candidate list.

Independent evidence also shows that task category materially changes acceptance rates and that no single agent is best across all task categories [E03]. Benchmark creators have documented defects and contamination risks even in popular coding evaluations [E05, E06]. Therefore:

```yaml
public_accuracy_claim: NOT_ACCEPTED_AS_GALAX_PROOF
Galax_accuracy_source: exact_repeated_fixture_suite_only
```

## Weighted suitability results

These scores measure fit for the proposed bounded role after source review. They are not accuracy scores and do not override hard gates.

| Candidate | Category | Score / 100 | Current decision | Exact proposed role |
|---|---:|---:|---|---|
| Aider | Coding writer | 88 | `STRONG_CONDITIONAL_CANDIDATE` | Supervised local surgical fixes and test repair |
| Jules | Coding writer | 86 | `STRONG_CONDITIONAL_CANDIDATE` | Primary GitHub cloud implementer on one branch/task |
| Codex | Coding writer/reviewer | 86 | `STRONG_CONDITIONAL_CANDIDATE_USAGE_BLOCKED` | Complex implementation or independent review after quota/credit approval |
| PR-Agent | PR reviewer | 83 | `STRONG_CONDITIONAL_CANDIDATE` | Pinned self-hosted review/comment gate only |
| OpenHands Core | Coding writer | 81 | `STRONG_CONDITIONAL_CANDIDATE_SELF_HOSTED_ONLY` | Open-source fallback implementer inside restricted sandbox |
| Antigravity | Local operator | 79 | `LIMITED_ROLE_ONLY` | Local branch recovery, repository inspection, supervised bounded edits |
| GitHub Copilot | Coding writer/reviewer | 77 | `QUALIFIED_BACKUP_NOT_SELECTED` | Backup IDE/cloud contributor; overlaps selected writers |
| Cursor | Coding writer | 72 | `QUALIFIED_BACKUP_NOT_SELECTED` | Paid isolated background writer only after permission review |
| Devin | Coding writer/reviewer | 71 | `QUALIFIED_BACKUP_NOT_SELECTED` | Paid fallback; no auto-merge; cost-controlled task only |
| PostgreSQL + pgvector | Data infrastructure | N/A | `FUTURE_INFRASTRUCTURE_SELECTED_FOR_SEPARATE_VALIDATION` | Memory/storage layer, not an AI teammate |
| LangGraph | Orchestration framework | N/A | `REJECTED_FOR_CURRENT_ARCHITECTURE` | Duplicate orchestration runtime while CrewAI is selected |
| SWE-agent | Coding writer | blocked | `BLOCKED_SUPERSEDED_MAINTENANCE_ONLY` | Re-evaluate mini-SWE-agent separately if nominated |
| Continue | Coding agent/checks | blocked | `BLOCKED_REPOSITORY_READ_ONLY` | Do not newly depend on an unmaintained product |

## Score rationale for selected five

### 1. Jules — primary GitHub cloud implementer

```yaml
category: CODING_WRITER
open_source: false
current_role: PRIMARY_GITHUB_IMPLEMENTER
score: 86
official_free_limit_as_of_record_date:
  tasks_per_rolling_24_hours: 15
  concurrent_tasks: 3
source: S01
```

**Capabilities supported by official sources**

- GitHub-connected tasks run in separate virtual machines with their own logs, environment, and code changes [S02].
- It can plan, edit, test, publish a branch, and create a PR through its GitHub workflow [S03].

**Why selected**

- Directly matches the user's present GitHub-first workflow.
- No local Codex token is needed for the current task.
- Separate task VM and plan approval support bounded implementation.

**Weaknesses and restrictions**

- Proprietary service; internal implementation is not auditable as open source.
- Free quota is task-based and may prevent completion of a long sequence.
- Concurrent tasks are available, but Galax prohibits concurrent writers on overlapping paths.
- Jules must start from the exact required branch and report the full starting SHA.

**Approved future trial**

```text
one Jules task
→ one exact branch
→ one bounded prompt
→ no parallel writer
→ tests and evidence
→ human diff review
→ no merge
```

### 2. Codex — complex implementation and independent review

```yaml
category: CODING_WRITER_OR_REVIEWER
open_source: false
current_role: COMPLEX_TASK_OR_INDEPENDENT_REVIEW
score: 86
current_user_availability: USER_REPORTED_QUOTA_BLOCKED
user_reported_reset_date: 2026-07-26
independent_verification_of_reset_date: NOT_AVAILABLE
```

**Capabilities and limits**

- Codex is an agent for writing, reviewing, and shipping code [S04].
- Usage depends on model, task complexity, context size, and execution type; fixed “messages until empty” cannot be promised [S04].
- Current flexible pricing is token/credit based and must be read from the account Usage panel [S05, S06].

**Why selected**

- Independent PR research reports consistently strong acceptance across multiple task classes, while still warning that no tool is universally best [E03].
- Useful as a second-stage reviewer because it need not edit the same branch as Jules.

**Weaknesses and restrictions**

- Usage is variable and currently unavailable to the user until the account-provided reset or approved credits.
- The July 26 date is a user/account observation, not a general OpenAI product promise.
- Codex must not be used simultaneously as a writer on files currently owned by Jules, Aider, or OpenHands.

### 3. Aider — supervised local surgical editor

```yaml
category: CODING_WRITER
open_source: true
license: Apache-2.0
current_role: LOCAL_SURGICAL_FIXER
score: 88
quota_model: selected_LLM_provider_determines_cost_and_limits
```

**Capabilities**

- Maps a repository and directly edits local files [S13].
- Integrates with Git and can create commits [S13, S14].
- Can run configured lint and test commands automatically [S15].

**Why selected**

- Strong local fallback for small exact fixes when a hosted task is blocked.
- Model can be cloud or local, allowing cost and privacy choices.
- Native Git/test workflow is well suited to a dedicated worktree.

**Weaknesses and restrictions**

- Automatic commit behavior must be explicitly configured; it may otherwise create commits earlier than Galax expects.
- Provider quality, token limit, and cost vary with the selected model [S16].
- Pre-commit/test verification must be enabled and recorded.
- Aider is not an autonomous merge authority and may never work directly on `main`.

### 4. OpenHands Core — open-source self-hosted fallback

```yaml
category: CODING_WRITER
open_source: true
license: MIT_core_enterprise_directory_separate
current_role: SELF_HOSTED_SANDBOXED_FALLBACK
score: 81
cloud_GitHub_app_status: REJECTED_FOR_GALAX_CURRENT_PERMISSION_MODEL
```

**Capabilities**

- Core OpenHands and agent-server are MIT licensed [S07].
- Local CLI/self-hosting is available [S09].
- OpenHands can work on issues and create PRs through its GitHub integration [S08].

**Why selected**

- Open-source fallback can be inspected, pinned, and run behind Galax's own sandbox/gateway.
- Useful when proprietary hosted writers are quota-blocked.

**Weaknesses and restrictions**

- The Cloud GitHub App requests broad read/write permissions including contents, Actions, webhooks, and workflows [S08]. That is incompatible with Galax least privilege for the current phase.
- Requires a model/provider or local model; “open-source agent” does not mean zero inference cost.
- Must use a restricted local token/gateway, no workflow access, no main writes, and no unrestricted internet with sensitive code.

### 5. PR-Agent — dedicated PR reviewer

```yaml
category: PR_REVIEWER
open_source: true
license: Apache-2.0
current_role: READ_COMMENT_ONLY_REVIEW_GATE
score: 83
source_write: prohibited
merge: prohibited
```

**Capabilities**

- Supports PR describe, review, improve suggestions, and questions [S24].
- Can run through CLI, webhook, or GitHub Actions [S24].
- Fixed releases and Docker digests can be pinned [S25].

**Why selected**

- It fills a different role from writers and can review after a writer completes.
- Source-write permission is unnecessary for the initial role.
- A pinned self-hosted reviewer gives repeatable configuration and avoids floating builds.

**Weaknesses and restrictions**

- Requires an LLM provider and therefore has provider cost, privacy, and quota constraints.
- AI review is advisory and cannot replace tests, security scans, or human approval.
- Do not use `@main`, nightly Docker images, auto-fix commits, or merge permissions.

## Full candidate background checks

### OpenHands

**Decision:** selected only as self-hosted fallback.  
**Good at:** autonomous repository exploration, implementation, command execution, issue-to-PR flow.  
**Risk:** Cloud integration permissions are broader than the current Galax need [S08].  
**Alternative when blocked:** Jules for hosted GitHub work; Aider for local bounded edits.

### SWE-agent

**Decision:** blocked.  
**Reason:** official documentation says it has been superseded by mini-SWE-agent and is maintenance-only [S10, S11].  
**Good at historically:** issue-solving research in containerized environments [S10, S12].  
**Remedy:** create a separate mini-SWE-agent nomination if future evidence shows a non-duplicated role. Do not silently substitute it under the old candidate name.

### Aider

**Decision:** selected conditional local writer.  
**Good at:** targeted file edits, repository map, lint/test loops, local Git history [S13-S16].  
**Risk:** automatic commits and provider-dependent quality/cost.  
**Required control:** dedicated worktree, branch check, allowed paths, explicit commit policy, tests.

### LangGraph

**Decision:** rejected for current architecture, not because it is weak.  
**Classification:** orchestration framework, not coding worker.  
**Capability:** durable execution, persistence, and human-in-the-loop [S17, S18].  
**Reason rejected now:** Galax has selected CrewAI 1.15.4 for its current foundation. Adding LangGraph as a second runtime duplicates state, routing, persistence, and approval ownership.  
**Future possibility:** separate architecture experiment after Agent 01 foundation validation; never an unreviewed dependency inside the current Flow.

### PostgreSQL and pgvector

**Decision:** future infrastructure, not top-five AI worker.  
**Capability:** PostgreSQL data storage plus exact or approximate vector similarity search [S19].  
**Known weakness:** HNSW/IVFFlat trade recall, memory, build time, and speed; approximate results are not perfect recall [S19].  
**Security requirement:** pin pgvector 0.8.2 or later because 0.8.2 fixed CVE-2026-3172 [S20].  
**Role:** later Supabase/Postgres memory implementation after the foundation, not current Agent 01 implementation.

### Continue

**Decision:** blocked for a new dependency.  
**Reason:** official docs state the repository is read-only and no longer actively maintained, with final release 2.0.0 [S22].  
**Useful concept:** repository-owned AI checks can inform Galax test design [S23].  
**Rule:** ideas may be studied, but the unmaintained product must not become a new critical dependency.

### PR-Agent / Qodo

**Decision:** selected reviewer only.  
**Clarification:** the current community PR-Agent repository is not the hosted Qodo free tier [S24].  
**Required:** pin a release and digest, read/comment-only permissions, no source writes, no merge.

### GitHub Copilot / Copilot Workspace

**Decision:** qualified backup, not selected.  
**Clarification:** current official product documentation should control; do not build a plan around an older “Copilot Workspace” name when the current offering is Copilot cloud agent/agent mode [S26].  
**Strength:** direct GitHub/IDE integration and multiple coding/review modes.  
**Weakness:** overlaps Jules/Codex/Aider; current plans use limited allowances/AI credits and paid tiers [S26, S27].  
**Reason not selected:** adds another writer without a unique current role.

### Cursor

**Decision:** qualified backup, not selected.  
**Strength:** isolated background VMs, automatic commands, repository editing [S29].  
**Risks:** read/write GitHub App, internet access, automatic terminal execution, code retention for the run, prompt-injection/exfiltration risk [S29].  
**Cost:** agent use is model-API-priced and heavy users may exceed entry-plan allowance [S28].  
**Reason not selected:** permission/cost burden and responsibility overlap.

### Devin

**Decision:** qualified paid backup, not selected.  
**Strength:** broad autonomous development and review workflow.  
**Cost:** usage depends on actions, complexity, VM time, and networking; plans and on-demand credits vary [S30-S32].  
**Risk:** role overlap and variable cost; any auto-merge capability must be disabled.  
**Alternative:** Jules/Codex for hosted tasks and PR-Agent for review.

### Jules

**Decision:** selected primary hosted writer.  
**Current fit:** already connected to the exact Galax research branch.  
**Quota rule:** one large task at a time despite three possible concurrent free tasks. Concurrency availability is not permission to run concurrent writers.

### Codex

**Decision:** selected conditional complex writer/reviewer.  
**Current state:** usage-blocked according to the user's account until its displayed reset; do not attempt model-switching as a quota bypass.  
**Fallback:** wait, use approved credits, or hand off a clean checkpoint to Jules/Aider/OpenHands.

### Antigravity

**Decision:** limited local operator, not top-five writer.  
**Strength:** local project/worktree operation, planning artifacts, command and file tools [S33-S35].  
**Required mode:** strict/request-review, outside-workspace access denied, sandbox enabled where supported [S34].  
**Rejected proposal:** switching accounts when quota is exhausted. Account rotation must not be used to evade provider limits or terms.  
**Approved role:** branch recovery, repository inspection, ZIP placement, supervised small edits after a separate task approval.

## Three evidence-backed conclusions

### Proof class 1 — Coding agents are doing real repository work at scale

AIDev reports 932,791 agent-authored PRs across 116,211 repositories for five major agents [E01]. This supports the claim that coding agents can contribute real GitHub changes. It does not prove their correctness for Galax.

### Proof class 2 — Specialization is stronger than “one best AI”

The task-stratified study of 7,156 PRs found large task-category differences and no universal winner [E03]. This supports assigning exact roles—writer, surgical fixer, and reviewer—rather than allowing every tool to do everything.

### Proof class 3 — Uncoordinated multi-writer operation creates measurable conflict

A 2026 study reports textual conflicts in 41.7% of sampled concurrent cross-agent PR pairs versus 19.8% for same-agent pairs, with most conflicted files being source code [E02]. This directly supports serialized writers, dedicated branches, path ownership, and a review gate.

## What the evidence cannot prove

No source proves that the selected five will have zero conflicts or finish every Galax task. The approved claim is:

```text
They cover complementary roles and have documented controls designed to avoid overlapping writes. Actual Galax approval requires deterministic fixtures and controlled live trials.
```

## Current activation state

```yaml
selected_candidates: 5
candidates_live_tested_in_Galax: 0
candidates_approved_for_repository_write: 0
primary_next_trial_candidate: Jules
current_Jules_task_allowed: repository_verification_only_until_plan_review
Codex_current_state: USER_REPORTED_QUOTA_BLOCKED
Aider_current_state: NOT_CONFIGURED
OpenHands_current_state: NOT_CONFIGURED
PR_Agent_current_state: NOT_CONFIGURED
merge: PROHIBITED
deployment: PROHIBITED
Agents_02_to_15: DISABLED
```
