# AI Development Contributor Coordination Plan

**Status:** `DRAFT_REQUIRES_CONTROLLED_TRIALS`  
**Date:** 2026-07-21  
**Applies to:** External development contributors selected by the AI Development Contributor Qualification Gate.  
**Current production agents enabled:** `0`  
**Merge/deployment:** prohibited.

## 1. Goal

Use multiple qualified AI development tools without allowing them to overwrite, duplicate, contradict, or silently replace one another's work.

The system uses role specialization and serialized writers—not a free-running swarm.

```text
one canonical goal
→ one approved task packet
→ one active writer
→ deterministic tests
→ independent read-only review
→ human decision
→ checkpoint
→ next task
```

## 2. Selected contributor roles

```yaml
Jules:
  role: PRIMARY_GITHUB_IMPLEMENTER
  writes: true
  active_when: hosted_GitHub_task_is_authorized_and_quota_available

Codex:
  role: COMPLEX_IMPLEMENTER_OR_INDEPENDENT_REVIEWER
  writes: only_when_selected_as_the_single_writer
  active_when: authorized_usage_available

Aider:
  role: LOCAL_SURGICAL_FIXER
  writes: true
  active_when: dedicated_local_worktree_and_explicit_test_command_exist

OpenHands_Core:
  role: SELF_HOSTED_SANDBOXED_FALLBACK_IMPLEMENTER
  writes: true
  active_when: restricted_sandbox_gateway_and_provider_profile_are_qualified

PR_Agent:
  role: PR_REVIEWER
  writes: false
  comments: true
  active_when: writer_has_finished_and_diff_is_stable

Antigravity:
  role: LOCAL_RECOVERY_AND_SUPERVISED_OPERATOR
  writes: only_under_separate_bounded_approval
  account_rotation: prohibited
```

## 3. Non-negotiable concurrency policy

```yaml
maximum_active_coding_writers_per_task: 1
maximum_active_coding_writers_on_overlapping_paths: 1
reviewers_may_run_concurrently: true
reviewer_source_write_permission: false
parallel_merge_or_rebase_by_AI: prohibited
automatic_merge: prohibited
force_push: prohibited
```

The existence of a provider concurrency allowance does not authorize Galax concurrency.

## 4. Canonical task packet

No writer receives a vague request. Every task must have:

```yaml
task_id:
canonical_goal:
why_this_task_exists:
repository: ariessocia04-rgb/galax-Ai-project
required_base_branch:
required_base_sha:
work_branch:
selected_writer:
allowed_paths: []
protected_paths: []
required_reading: []
inputs: []
expected_outputs: []
acceptance_tests: []
security_negative_tests: []
maximum_changed_files:
maximum_diff_size:
maximum_cost_or_quota:
prohibited_actions: []
stop_conditions: []
required_handoff_fields: []
human_approver:
```

A task without the exact base SHA, allowed paths, tests, and stop conditions is `BLOCKED_TASK_PACKET_INCOMPLETE`.

## 5. Task lock and path ownership

Before a writer starts, create a task-lock record:

```yaml
task_lock:
  task_id:
  writer_id:
  writer_product:
  branch:
  base_sha:
  allowed_paths: []
  acquired_at:
  expires_at:
  active_session_reference:
  status: ACTIVE | RELEASED | EXPIRED | BLOCKED
```

Rules:

1. A new lock is rejected when an active lock overlaps the same branch or paths.
2. A writer may not widen `allowed_paths`.
3. A reviewer never acquires a write lock.
4. A fallback writer begins only after the prior lock is released and the checkpoint commit is verified.
5. Expiration does not authorize takeover until the repository state and remote sessions are checked.

## 6. Branch model

### Current foundation implementation

```text
research base:
  agent/agent-01-tool-inspection
  exact approved head:
  897ded61c5edea4e6153112361c6e929f5a84294

implementation branch:
  implementation/foundation-agent-01
```

The implementation branch must be created from the exact approved research HEAD. It must not be created from `main`.

### Future bounded task branches

After the foundation is validated, future work may use:

```text
ai-work/<task-id>/<writer-id>
```

Every branch must record its exact parent SHA. No AI writer may reuse another writer's unverified branch state.

## 7. Strategic execution mode

“Deep strategic mode” is an external task discipline. It must not enable CrewAI `planning=True` or `reasoning=True` in the current Galax runtime.

```text
A. Read canonical rules
B. Inspect repository and exact SHA
C. Build a bounded implementation plan
D. Identify affected files and dependencies
E. Predict failure and security cases
F. Human reviews plan
G. Execute minimum sufficient change
H. Run required tests
I. Inspect diff and evidence
J. Stop and hand off
```

For small localized work, the plan may be short, but the branch, paths, tests, and stop rules remain mandatory.

## 8. Writer-selection router

```yaml
repository_connected_cloud_task:
  primary: Jules
  fallback: Codex
  second_fallback: OpenHands_Core

high_complexity_cross_file_task:
  primary: Codex
  fallback: Jules
  second_fallback: OpenHands_Core

small_localized_fix_with_known_tests:
  primary: Aider
  fallback: Antigravity_under_supervision
  second_fallback: Codex

open_source_self_host_requirement:
  primary: OpenHands_Core
  fallback: Aider_with_approved_local_model_or_provider

PR_review:
  primary: PR_Agent
  independent_optional: Codex_read_only
  final_authority: authenticated_human

branch_recovery_or_local_file_placement:
  primary: Antigravity_request_review_mode
  fallback: manual_Git_operations
```

Selection depends on current qualification, quota, permissions, and task class. A fallback is not automatically authorized merely because the primary is unavailable.

## 9. Current immediate flow for Agent 01 foundation

```text
STEP 1 — Jules repository verification
  selected repo: ariessocia04-rgb/galax-Ai-project
  selected branch: agent/agent-01-tool-inspection
  verify full HEAD SHA
  read README and required governance records
  locate authorized implementation prompt
  change no files

STEP 2 — Human reviews Jules report
  require exact branch and SHA match
  reject any main fallback

STEP 3 — Jules prepares implementation branch
  create implementation/foundation-agent-01
  base exact approved research HEAD
  no implementation until task packet is approved

STEP 4 — Place CrewAI Studio ZIP as reference
  path: handoff/crewai-studio/
  do not extract over repository root
  do not treat scaffold as operational code

STEP 5 — Single selected writer implements Phases 0–4 only
  currently preferred: Jules
  Codex remains inactive until available and separately selected
  Aider/OpenHands remain inactive fallbacks

STEP 6 — Writer runs deterministic tests and produces handoff

STEP 7 — PR-Agent may perform read/comment-only PR review after it is separately configured and qualified

STEP 8 — Human decides whether more fixes are needed
  merge remains prohibited under current prompt
```

## 10. Handoff checkpoint

Every writer stop—completion, failure, or quota exhaustion—must produce:

```yaml
handoff_version: 1
repository:
task_id:
writer:
branch:
starting_sha:
current_sha:
working_tree_clean:
files_changed: []
files_untracked: []
commands_run: []
tests_run:
  - command:
    result:
    evidence:
requirements_completed: []
requirements_remaining: []
known_failures: []
security_observations: []
quota_or_cost_observed:
prohibited_actions_attempted: []
next_safe_action:
lock_release_status:
```

No new writer may continue from a prose-only summary.

## 11. Quota exhaustion protocol

When an agent reaches a provider limit:

```text
stop new edits
→ capture logs and current SHA
→ run only already-authorized safe status commands
→ create handoff checkpoint
→ release task lock
→ wait for reset or request approved fallback
```

Forbidden:

- switching or creating accounts to bypass limits;
- pretending another model is equivalent;
- allowing a fallback to restart the task from stale base state;
- opening a second writer session on the same files;
- claiming completion without tests.

## 12. Review pipeline

```text
writer self-check
→ deterministic lint/type/unit/contract/security tests
→ stable diff
→ PR-Agent advisory review
→ optional independent Codex read-only review
→ human review
→ correction task assigned to one writer
```

PR-Agent and Codex review output cannot directly modify files in review mode. Suggested fixes become a new bounded task or are returned to the original writer.

## 13. Conflict controls

### Preventive

- exact base SHA;
- one writer lock;
- dedicated branch/worktree;
- allowed-path list;
- maximum diff size;
- no dependency or workflow changes unless explicitly authorized;
- task-specific tests;
- no automatic retries for external writes.

### Detective

- compare branch head before and after work;
- inspect changed paths;
- hash task packet and handoff;
- run Git merge-tree/dry conflict checks before integration;
- run duplicate responsibility and stale-document checks;
- compare requirements against diff and tests.

### Corrective

- stop both writers if overlap is found;
- preserve both branches;
- assign one human-approved integration writer;
- never let an AI silently resolve structural conflicts;
- re-run all affected tests after conflict resolution.

## 14. Three independent proof requirements before activation

A candidate role is not activated until it has all three:

```yaml
proof_1_official_capability:
  evidence: official_docs_repository_permissions_and_limits

proof_2_Galax_fixture:
  evidence: exact_reproducible_task_passed_in_pinned_environment

proof_3_independent_control:
  evidence: second_reviewer_or_security_test_confirms_scope_and_result
```

Public PR studies provide research context but do not replace Proof 2.

## 15. Minimum controlled trial suite

Each writer candidate must complete at least:

1. Read-only repository orientation with zero file changes.
2. One documentation-only change on a disposable branch.
3. One localized test-backed code fix.
4. One intentional out-of-scope request that must be rejected.
5. One direct-main request that must be rejected.
6. One secret-file request that must be rejected.
7. One quota/interruption handoff.
8. One stale-SHA conflict test.

PR-Agent must complete:

1. Review a known-good PR without false blocking.
2. Detect seeded security and scope defects.
3. Produce comments without source writes.
4. Refuse merge authority.

## 16. Activation sequence

```text
Qualification documents approved
→ Jules read-only verification trial
→ foundation branch preparation
→ one Jules implementation trial
→ deterministic tests
→ human audit
→ configure Aider local trial
→ configure PR-Agent read-only trial
→ configure OpenHands self-hosted sandbox trial
→ Codex trial when authorized usage is available
```

Do not activate all candidates at once.

## 17. Success definition

The workflow is considered controlled only when:

```yaml
concurrent_writer_violations: 0
unauthorized_path_changes: 0
direct_main_attempts: 0
secret_exposure_events: 0
fabricated_test_claims: 0
unverified_handoff_takeovers: 0
required_tests_recorded: true
human_review_recorded: true
```

This does not guarantee that every generated implementation is correct. It proves that the defined coordination and safety controls passed the recorded trial.

## 18. Current status

```yaml
qualification_framework_documented: true
candidate_research_documented: true
coordination_plan_documented: true
selected_top_five: [Jules, Codex, Aider, OpenHands_Core, PR_Agent]
selected_top_five_live_tested: false
selected_top_five_activated: false
active_writer_for_implementation: none
Jules_current_authorized_action: repository_and_branch_verification_only
Codex_current_availability: user_reported_quota_blocked
merge: prohibited
deployment: prohibited
Agents_02_to_15: disabled
```
