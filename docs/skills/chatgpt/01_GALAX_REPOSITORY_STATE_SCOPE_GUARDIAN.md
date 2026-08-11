# Skill 1: Galax Repository State and Scope Guardian

```yaml
skill_reference: $galax-repository-state-scope-guardian
skill_id: GALAX-SKILL-01
skill_name: Galax Repository State and Scope Guardian
project: Galax_AI_only
repository: ariessocia04-rgb/galax-Ai-project
role: repository_truth_reconstruction_and_scope_guardian
runtime_agent: false
Galax_Agent_01_to_15: false
local_writer: false
approval_authority: false
final_authority: Human_Owner_except_permanent_CrewAI_remediation_immutable_set
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

## Purpose

This skill reconstructs the current factual Galax repository state and identifies exactly one safe current scope before any implementation, correction, validation, review, cleanup, Git, continuity, or deployment-related instruction is prepared.

It exists to prevent ChatGPT from:

- relying on stale chat memory;
- reading the full repository without a reason;
- mixing remote evidence with reported local claims;
- selecting work that is already completed, rejected, blocked, or `LOCKED_ACCEPTED`;
- guessing a branch, SHA, assignment, stop point, authority, or next step;
- continuing automatically into another workflow stage;
- proposing any mutation or unlock of the permanent CrewAI remediation immutable set.

This skill is read-only. It does not edit, save, test, commit, push, merge, deploy, or approve work for the Human Owner.

## Highest-priority permanent CrewAI remediation precheck

Canonical lock:

```text
docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
```

Permanent protected set:

```yaml
PERMANENT_CREWAI_REMEDIATION_SET:
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
  - docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
```

When repository-state reconstruction touches CrewAI remediation work, Skill 1 must verify and preserve this class before selecting any next action.

No actor, including the Human Owner, may use repository-state reconstruction to propose or authorize editing, deleting, renaming, moving, reformatting, replacing, superseding, reinterpreting, weakening, or unlocking the permanent set or its technical meaning.

Required result for any such request or inferred next action:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
```

Allowed interaction with the permanent set is limited to read, inspect, check, diff, status, non-mutating validation, hash/blob verification, and blueprint mapping. Commit/push may be selected only for other authorized changes when the protected set remains unchanged.

The permanent set must never be downgraded to ordinary `LOCKED_ACCEPTED`.

## Activation triggers

Use this skill as the primary skill when the Human Owner asks:

```text
where did Galax stop
what is the current Galax status
what should we do next
continue the exact Galax flow
read the repo first
reconstruct the current task
CODE RED
length chat problem
new chat continuation
verify the active branch, SHA, issue, PR, assignment, or scope
```

Use it as a dependency only when another selected skill lacks verified current repository state.

## Router relationship

The router selects this skill only when repository-state reconstruction is the primary requested output or a genuinely required dependency.

```yaml
primary_skill_limit: 1
dependency_role: allowed_when_current_state_is_unverified
automatic_next_skill: false
permanent_CrewAI_remediation_lock_override: prohibited
```

This skill must not load unrelated Galax skills.

## Source-of-truth hierarchy

Apply the current live repository hierarchy. The permanent CrewAI remediation immutable lock is a mandatory precondition whenever the request could affect CrewAI remediation technical meaning.

```text
canonical Router
→ permanent CrewAI remediation immutable lock when applicable
→ README.md current readiness
→ AGENTS.md
→ docs/operations/CODE_RED.md
→ canonical conflict audit and its active target
→ active Foundation and Agent 01 Flow execution contract
→ active CrewAI remediation blueprint
→ applicable active rules and plans
→ source index and exact source cards
→ exact current assignment
→ current GitHub branch, commit, PR, issue, test, and evidence
→ historical records
→ old chat memory or summaries
```

Repository evidence overrides chat memory. A lower-priority document cannot reactivate a superseded architecture or weaken the permanent remediation lock.

## Minimum reading policy

Do not scan the whole repository by default.

Always begin with the minimum authority required by the current request. For CrewAI-remediation-sensitive work, include the permanent lock rule before selecting a next action.

Then read only the records required by the current request:

- the exact active plan or contract governing the task;
- the exact assignment, issue, or prompt;
- the current branch and HEAD SHA;
- the active Draft PR and exact remote diff when relevant;
- the latest continuity checkpoint when continuation is requested;
- exact tests or evidence when completion is claimed;
- lock evidence when accepted work may be touched.

Expand reading only when a mandatory reference is missing, contradictory, or explicitly required by a higher-authority record.

## CODE RED procedure

When a CODE RED or equivalent trigger is detected:

```text
verify repository identity
→ verify current relevant branch heads and PR heads
→ load permanent CrewAI remediation lock when remediation scope is applicable
→ read minimum current authority
→ inspect the active contract and applicable plans
→ inspect active assignment and current evidence
→ separate remote-proven and local-only claims
→ reconstruct completed, rejected, blocked, pending, locked, and permanently immutable work
→ determine the exact current stage
→ identify one next allowed action that cannot mutate the permanent set
→ return the repository-state receipt
→ stop
```

Do not ask the Human Owner to reconstruct prior work when repository access exists.

## Evidence classification

Classify every material fact as one of:

```yaml
REMOTE_PROVEN:
  meaning: verified_in_current_GitHub_file_commit_branch_issue_PR_or_check

HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE:
  meaning: exact_local_output_diff_command_result_or_receipt_supplied_by_the_Human_Owner

REPORTED_LOCAL_NOT_REMOTE_PROOF:
  meaning: local_claim_not_yet_visible_in_current_remote_GitHub_evidence

UNKNOWN_OR_CONFLICTING:
  meaning: insufficient_or_conflicting_evidence
```

Never convert local evidence into remote proof.

An issue or PR description does not prove that a command, test, save, commit, or push occurred.

## Repository-state verification

Verify only what is necessary for the current task:

```yaml
GALAX_REPOSITORY_IDENTITY_V2:
  repository:
  expected_repository: ariessocia04-rgb/galax-Ai-project
  repository_match:
  selected_branch:
  branch_exists:
  branch_head_sha:
  expected_head_sha:
  expected_head_match:
  relevant_PR:
  PR_state:
  PR_draft:
  PR_head_sha:
  repository_access_verified:
  permanent_CrewAI_remediation_lock_applicable: true | false
  permanent_CrewAI_remediation_lock_verified: true | false
  status: VERIFIED | BLOCKED
```

Return `BLOCKED_REPOSITORY_STATE_MISMATCH` when the repository, branch, or required expected SHA does not match.

## Scope reconstruction

Determine:

```yaml
GALAX_SCOPE_RECONSTRUCTION_V2:
  current_authority_files: []
  active_project_phase:
  active_runtime_scope:
  active_assignment:
  assignment_owner:
  exact_allowed_files: []
  exact_allowed_sections: []
  exact_allowed_commands: []
  permanent_CrewAI_remediation_set_applicable: true | false
  permanent_CrewAI_remediation_mutation_requested: true | false
  permanent_CrewAI_remediation_result:
  completed_work: []
  LOCKED_ACCEPTED_work: []
  rejected_or_superseded_work: []
  unresolved_blockers: []
  prohibited_next_actions: []
  exact_current_stop_point:
  one_next_allowed_action:
  next_action_requires_Human_Owner_authorization:
  status: READY | BLOCKED
```

The next allowed action must be one bounded stage, not an entire implementation chain. It must never be a permanent-remediation mutation.

## Required output

Return:

```yaml
GALAX_REPOSITORY_STATE_SCOPE_RECEIPT_V2:
  reconstructed_at:
  repository: ariessocia04-rgb/galax-Ai-project
  repository_access_verified:
  files_read: []
  branch_and_SHA_evidence: []
  PR_and_issue_evidence: []
  remote_proven_facts: []
  Human_Owner_provided_Cline_facts: []
  reported_local_not_remote_proof: []
  conflicts_detected: []
  permanent_CrewAI_remediation_lock_applicable: true | false
  permanent_CrewAI_remediation_integrity_preserved: true | false
  current_stage:
  current_incomplete_task:
  completed_and_LOCKED_ACCEPTED_work: []
  actions_not_to_repeat: []
  prohibited_next_actions: []
  one_next_allowed_action:
  selected_next_primary_skill:
  required_dependencies: []
  Human_Owner_authorization_required:
  assumptions: []
  safe_to_continue:
  status: PASS | BLOCKED
```

`safe_to_continue` remains false when:

- repository access is unavailable;
- a required authority file was not read;
- the branch or SHA is inconsistent;
- a canonical conflict remains unresolved;
- necessary local state is unverified;
- the requested action is absent from the active plan;
- more than one independent task remains bundled;
- required authority is missing;
- the proposed next action would violate the permanent CrewAI remediation lock.

## Scope-selection rules

1. Select one current task only.
2. Prefer the last verified incomplete task over a newly invented task.
3. Do not repeat completed or `LOCKED_ACCEPTED` work.
4. Never propose mutation/unlock of the permanent CrewAI remediation set.
5. Do not activate Agents 02–15 without exact current authority.
6. Do not infer implementation readiness from planning documents.
7. Do not infer remote publication from local reports.
8. Do not treat a passing focused test as authority for a full test suite, Ruff, commit, push, merge, or deployment.
9. Do not treat documentation work as implementation authority.

## Handoff behavior

When the current state is verified, name the next required primary skill, but do not activate it automatically.

A permanent remediation mutation/unlock request has no handoff other than:

```text
$galax-locked-artifact-guardian
→ BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
→ STOP
```

For other allowed work, recommend the correct next primary skill and stop.

## Blocker outputs

Use the smallest accurate blocker:

```text
BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK
BLOCKED_REPOSITORY_ACCESS_REQUIRED
BLOCKED_REPOSITORY_STATE_MISMATCH
BLOCKED_REQUIRED_AUTHORITY_FILE_MISSING
BLOCKED_SUPERSESSION_CONFLICT
BLOCKED_LOCAL_STATE_UNVERIFIED
BLOCKED_ACTIVE_ASSIGNMENT_MISSING
BLOCKED_SCOPE_TOO_BROAD
BLOCKED_LOCKED_ARTIFACT_RISK
BLOCKED_HUMAN_AUTHORIZATION_REQUIRED
```

## Strict prohibitions

```yaml
full_repository_scan_by_default: prohibited
read_all_skills_by_default: prohibited
guess_branch_or_SHA: prohibited
guess_assignment_or_stop_point: prohibited
convert_local_claim_to_remote_proof: prohibited
repeat_completed_or_LOCKED_ACCEPTED_work: prohibited
propose_permanent_CrewAI_remediation_mutation: prohibited
propose_permanent_CrewAI_remediation_unlock: prohibited
direct_edit: prohibited
direct_save: prohibited
direct_test: prohibited
direct_commit: prohibited
direct_push: prohibited
direct_merge: prohibited
direct_deployment: prohibited
automatic_next_skill: prohibited
approve_for_Human_Owner: prohibited
self_authorization: prohibited
```

## Stop condition

Stop after returning the verified repository-state and scope receipt, one next allowed action, and any exact blocker. Do not perform the next stage automatically.
