# AI Development Contributor Coordination Plan V2

**Date:** 2026-07-21  
**Status:** `CURRENT_DESIGNATION_PLAN_CONTROLLED_TRIALS_REQUIRED`  
**Supersedes:** `AI_DEVELOPMENT_CONTRIBUTOR_COORDINATION_PLAN_DRAFT.md` where role selection conflicts.  
**Merge/deployment:** prohibited.  
**Current production agents enabled:** `0`.

## 1. Objective

Use specialized external AI development contributors to improve implementation and review quality without creating a multi-writer swarm or allowing any tool to control the Galax CrewAI runtime.

```text
one canonical task
→ one active source writer
→ deterministic tests
→ optional isolated comparison
→ read-only review
→ human decision
→ checkpoint
→ next task
```

## 2. Current designated five

```yaml
Cline:
  role: SUPERVISED_PRIMARY_IMPLEMENTER
  score: 86
  write_lock: required

OpenHands_Core:
  role: DOCKER_ISOLATED_FALLBACK_IMPLEMENTER
  score: 84
  write_lock: required_after_prior_writer_stops

mini_SWE_agent:
  role: ISOLATED_PATCH_COMPARATOR
  score: 83
  authoritative_branch_write: false

Aider:
  role: SURGICAL_FIX_AND_TEST_REPAIR_SPECIALIST
  score: 82
  write_lock: required_after_primary_writer_stops

PR_Agent:
  role: READ_ONLY_PR_REVIEWER
  score: 82
  source_write: false
```

All five are paper-qualified for controlled trials only. None is activated.

## 3. Hosted tools outside the open-source five

```yaml
Jules:
  role: CURRENT_HOSTED_REPOSITORY_OPERATOR
  immediate_authorized_action: repository_and_branch_verification_only_until_human_approval

Codex:
  role: HOSTED_COMPLEX_IMPLEMENTER_OR_REVIEWER
  availability: separately_authorized_when_usage_is_available
```

Jules and Codex are not counted as open-source contributors. They remain subject to the same task-packet, branch, scope, evidence, and handoff rules.

## 4. Project compatibility boundary

```yaml
Galax_framework: CrewAI_1.15.4_selected_for_validation
external_tools_inside_CrewAI_runtime: false
external_tools_may_control_Flow: false
external_tools_may_enable_planning_reasoning_memory_or_delegation: false
external_tools_may_enable_Agents_02_to_15: false
external_tools_may_merge_or_deploy: false
```

The selected tools build and review the repository. They are not CrewAI agents in the Galax application.

## 5. Task routing

```yaml
bounded_multi_file_implementation:
  primary: Cline
  fallback_after_stop: OpenHands_Core

one_exact_reproducible_test_or_lint_failure:
  primary: Aider
  prerequisite: primary_writer_stopped_and_lock_released

independent_issue_patch_comparison:
  primary: mini_SWE_agent
  authoritative_branch_write: false

stable_draft_PR_review:
  primary: PR_Agent
  source_write: false

current_GitHub_cloud_orientation_or_authorized_task:
  operator: Jules
  open_source_five_state: inactive_until_trials
```

A fallback is not automatically authorized when the primary is unavailable. A new task packet and human approval are required.

## 6. Work ownership sequence

### Stage A — orientation

Owner: selected contributor in read-only mode.

Required output:

- repository, branch, and full SHA;
- reading receipt;
- applicable rules;
- proposed bounded plan;
- zero changed files.

### Stage B — primary implementation

Owner: Cline after controlled qualification and task approval, or current separately authorized hosted operator.

Rules:

- one dedicated task branch/worktree;
- exact allowed paths;
- plan approval before edits;
- minimum sufficient changes;
- deterministic tests;
- structured handoff;
- stop and release lock.

### Stage C — surgical correction

Owner: Aider only when a stable implementation has one exact reproducible failure.

Rules:

- primary writer stopped;
- one failure and minimal patch;
- no automatic or dirty commits;
- exact lint/test commands;
- no scope expansion.

### Stage D — independent comparison

Owner: mini-SWE-agent on an isolated disposable copy.

Rules:

- same issue and base SHA;
- fixed system/instance templates;
- bounded steps, cost, and wall-clock;
- patch and trajectory only;
- no direct GitHub writes;
- no automatic application.

This stage may run after stable fixtures exist. It must not use another contributor's live worktree.

### Stage E — fallback reproduction or implementation

Owner: OpenHands Core only when the prior writer has stopped and a Docker-isolated fallback is approved.

Rules:

- self-hosted core only;
- Docker sandbox;
- no process mode;
- no GitHub Cloud App;
- no credentials;
- deny-by-default network;
- patch, tests, trajectory, and cleanup evidence.

### Stage F — review

Owner: PR-Agent after the diff is stable and writers have stopped.

Rules:

- exact pinned release and digest;
- local unpublished output initially;
- no source writes, labels, merge, or automatic feedback;
- findings tied to exact rule, location, evidence, and correction;
- suggestions become a new task for one writer.

### Stage G — human decision

Only the human approver decides:

```text
ACCEPT_FOR_NEXT_GATE
RETURN_TO_ONE_WRITER
BLOCK_MISSING_EVIDENCE
STOP_PROJECT_SCOPE
```

## 7. Task lock

```yaml
task_lock:
  task_id:
  contributor:
  role:
  branch:
  base_sha:
  allowed_paths: []
  acquired_at:
  expires_at:
  active_session_reference:
  status: ACTIVE | RELEASED | EXPIRED | BLOCKED
```

Rules:

1. Maximum one active source-writer lock per task.
2. Overlapping branch or path locks are rejected.
3. mini-SWE-agent uses an isolated comparison record, not the authoritative writer lock.
4. PR-Agent never receives a source-write lock.
5. Lock expiration does not authorize takeover until session and repository state are verified.

## 8. Canonical task packet

Use:

```text
docs/ai-contributors/templates/CANONICAL_TASK_PACKET.yaml
```

No work starts until it contains:

- task and role identity;
- exact base branch and SHA;
- work branch;
- allowed and protected paths;
- required reading;
- expected output;
- acceptance and security tests;
- permissions and resource limits;
- stop conditions;
- human approval.

## 9. Contributor-specific instructions

```text
AGENTS.md
+ GALAX_EXTERNAL_CONTRIBUTOR_OPERATING_STANDARD.md
+ selected role card
+ approved task packet
+ task-specific implementation or review prompt
```

Do not give every contributor all tool documentation. Load only the rules and context needed for its exact task.

## 10. Handoff

Use:

```text
docs/ai-contributors/templates/CONTRIBUTOR_HANDOFF.yaml
```

A valid handoff includes exact SHAs, paths, commands, tests, artifacts, blockers, resource usage, prohibited attempts, and lock release. A prose summary alone is invalid.

## 11. MCP decision

```yaml
direct_agent_to_agent_MCP_mesh: prohibited
all_five_native_MCP_clients: false
current_MCP_connection: disabled
future_control_plane: GalaxDevelopmentContributorGateway
future_status: research_only_not_implemented
```

Cline and OpenHands have native MCP support. Aider, mini-SWE-agent, and PR-Agent are addressed through controlled CLI/container adapters. MCP is not used to let contributors call each other or share live workspaces.

Future narrow gateway operations:

```text
submit_task
get_status
cancel_task
read_artifact
```

The gateway must never expose raw GitHub credentials, main write, merge, force push, workflows, secrets, arbitrary shell, arbitrary filesystem, or arbitrary MCP URLs.

## 12. Agent 01 foundation timing

The current controlled five-contributor workflow is estimated as:

```yaml
best_case_working_days: 10
realistic_working_days: 14_to_20
blocked_or_high_rework_case: 21_to_35
```

This estimate covers Foundation and Agent 01 Phases 0–4 only. The five contributors do not provide five-way implementation concurrency; they reduce rework through specialization, comparison, fallback, and review.

## 13. Controlled trial order

```text
1. Cline read-only orientation
2. Cline documentation-only disposable-branch task
3. Cline small test-backed code task
4. Aider exact failure repair
5. mini-SWE-agent isolated patch comparison
6. OpenHands Core Docker reproduction
7. PR-Agent local unpublished review
8. direct-main, secret, scope, quota, and stale-SHA rejection trials
9. human decision records
```

Do not activate all contributors at once.

## 14. Current Agent 01 immediate flow

```text
Jules read-only branch verification
→ human checks exact branch/SHA/prompt
→ prepare implementation/foundation-agent-01 from approved research HEAD
→ place CrewAI Studio ZIP as reference only
→ select one authorized writer
→ implement Phases 0–4
→ tests and handoff
→ optional qualified comparison/fallback/review stages
→ human decision
```

No open-source contributor may interrupt or overlap the current Jules verification session.

## 15. Success thresholds

```yaml
concurrent_writer_violations: 0
unauthorized_path_changes: 0
direct_main_attempts: 0
force_push_attempts: 0
automatic_merge_attempts: 0
secret_exposure_events: 0
fabricated_evidence: 0
required_tests_executed: 100_percent
security_negative_tests_passed: 100_percent
handoffs_complete: true
human_decisions_recorded: true
```

## 16. Current status

```yaml
role_cards_added: true
universal_AGENTS_instructions_added: true
operating_standard_added: true
task_and_handoff_templates_added: true
execution_command_pack_added: true
contributors_installed: false
credentials_added: false
MCP_enabled: false
controlled_trials_completed: false
contributors_activated: false
merge: prohibited
deployment: prohibited
Agents_02_to_15: disabled
```
