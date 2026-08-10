# Galax AI Repository Instructions for External Coding Assistants

**Status:** `ACTIVE_CONTROLLED_TRIAL_INSTRUCTIONS`  
**Applies to:** Cline, OpenHands Core, mini-SWE-agent, Aider, PR-Agent, GitHub Copilot, Codex, Claude Code, Jules, ChatGPT, and every other repository-aware coding assistant  
**Does not approve:** any Galax CrewAI production agent, external contributor, model, tool, merge, or deployment

## 1. Repository identity

```yaml
repository: ariessocia04-rgb/galax-Ai-project
protected_branch: main
research_branch: agent/agent-01-tool-inspection
foundation_implementation_branch: implementation/foundation-agent-01
framework_target: CrewAI_1.15.4
python_target: ">=3.10,<3.14"
current_scope: governance_foundation_and_Agent_01_only
Agents_02_to_15: prohibited
production_ready: false
```

Stop immediately with `BLOCKED_REPOSITORY_STATE_MISMATCH` when the repository, branch, or expected starting SHA does not match the assigned task.

## 2. Mandatory reading order before any answer or edit

Read every applicable item completely in this order:

1. `README.md`
2. `docs/operations/CODE_RED.md`
3. `docs/research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md`
4. The canonical audit target identified by that alias
5. `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`
6. `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`
7. `docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md`
8. Every other applicable file under `docs/rules/`
9. Every applicable file under `docs/plan/`
10. `docs/sources/SOURCE_INDEX.md`
11. Exact source cards for every framework, model, tool, gateway, contributor, and agent involved
12. `docs/research/agents/AGENT-01-engineering-manager/03_TOOL_INSPECTION.md`
13. `docs/prompts/GALAX_FOUNDATION_AGENT01_IMPLEMENTATION_VALIDATION_PROMPT.md`
14. `docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md`
15. `docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md`
16. The exact platform assignment in `docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md` or a newer repository-linked exact assignment
17. Current branch heads, draft PR, assignment issues, tests, and evidence required by the active task

`docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md` is a compatibility redirect only. CODE RED is canonical.

Do not edit before producing a concise `REPOSITORY_READ_RECEIPT` that lists the files actually read, their branch/ref, the current HEAD SHA, detected conflicts, and exact permitted scope.

## 3. CODE RED trigger

Treat these phrases and close spelling variations as the same command:

```text
CODE RED
code red
length chat problem
chat length problem
conversation length problem
continue exact Galax flow
operation length problem solve
operatiion length problem solve
```

On detection:

```text
read docs/operations/CODE_RED.md completely
→ verify repository access and current main, research, implementation, and PR heads
→ inspect active assignment issues and latest continuity comments
→ separate remote-proven facts from reported local-only facts
→ reconstruct decisions, actions done, accepted work, rejected outputs, blockers, cleanup state, current stage, and exact next action
→ return CODE_RED_RECEIPT_V1
→ answer or act only when safe_to_continue=true
```

Do not ask the owner what the previous work was when repository access exists. Do not use remembered conversation fragments as authority.

### 3A. Human Owner standing authorization for bounded one-hour continuity uploads

The Human Owner authorizes a narrow automatic continuity-upload exception. This exception applies only to the Galax continuity records identified below and does not authorize implementation, validation, merge, deployment, or changes to accepted runtime artifacts.

```yaml
standing_authorization_id: GALAX_ONE_HOUR_CONTINUITY_AUTO_UPLOAD_V1
human_authorized: true
timezone_name: Asia/Manila
timezone_offset: "+08:00"
check_interval: 1_hour
maximum_delay_after_new_material_event: 1_hour
actual_GitHub_write_commit_and_branch_publication: required
draft_only_or_notification_only_behavior: prohibited
upload_when_no_new_verified_event: false

repository: ariessocia04-rgb/galax-Ai-project
target_branch: docs/new-chat-continuity-2026-07-27
target_pull_request: 10
direct_main_write: prohibited
merge_authorized: false

length_checkpoint:
  automatic_create_or_update: authorized
  automatic_upload_required: true
  upload_deadline: within_1_hour_after_new_verified_material_event
  directory: docs/operations/checkpoints
  naming_rule: GALAX_LENGTH_PROBLEM_*_VOLUME_<NEXT_NUMBER>_<YYYY-MM-DD>.md
  append_only_after_previous_stop_boundary: true
  exact_Asia_Manila_timestamp_required: true

achievement_record:
  path: docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
  automatic_update: authorized_only_when_new_verified_achievement_exists
  automatic_upload_required_when_triggered: true
  upload_deadline: within_1_hour_after_new_verified_achievement
  update_when_no_new_verified_achievement: prohibited

maximum_repository_writes_per_cycle: 2
```

For this section, `automatic upload` means the actual authorized GitHub file write, commit, and publication to `docs/new-chat-continuity-2026-07-27`. Preparing a draft, displaying a preview, or sending a reminder without performing the repository upload does not satisfy this rule when all verification requirements pass.

Required decision sequence for every automatic cycle:

```text
verify live repository, continuity branch, PR #10, and latest checkpoint
→ collect only new verified events after the previous exact stop boundary
→ classify evidence as REMOTE_PROVEN, HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE, or REPORTED_LOCAL_NOT_REMOTE_PROOF
→ determine whether a new verified achievement exists
→ when no new verified achievement exists, create only the next numbered length checkpoint
→ when a new verified achievement exists, update the achievement record first in its own commit
→ verify the achievement commit SHA
→ create the next numbered length checkpoint in a separate commit referencing the verified achievement commit SHA
→ verify final branch head and PR #10 remain open and draft
→ stop
```

Automatic continuity uploads are pre-authorized only when every condition below is satisfied:

- At least one new verified material event exists after the previous checkpoint boundary.
- The previous checkpoint and exact stop timestamp were read and verified.
- Every recorded claim has an explicit evidence classification.
- The upload changes only the authorized continuity file or files.
- Achievement entries describe completed, verified achievements rather than plans, previews, permission requests, or unsupported completion claims.
- The length checkpoint includes the exact Philippine date, time, minute, previous checkpoint, coverage start, coverage end, exact stop point, next resume boundary, latest completed action, exact safe resume action, and actions that must not be repeated.
- When both files change, they use two sequential commits: achievement record first, length checkpoint second.
- The length checkpoint references the exact achievement-update commit SHA.
- PR #10 remains open and draft, and no merge is performed.

The automatic cycle must stop without writing and report `BLOCKED_CONTINUITY_AUTO_UPLOAD` when any of the following occurs:

- repository, branch, PR, file, or expected boundary mismatch;
- exact timestamp is unavailable or would need to be guessed;
- evidence classification is uncertain;
- the proposed entry would modify or reinterpret `LOCKED_ACCEPTED` work;
- a source, runtime, test, dependency, workflow, secret, implementation, or non-continuity file would change;
- a duplicate or already-covered event would be recorded;
- the achievement record would be updated without a new verified achievement;
- GitHub access or write verification fails.

This standing authorization permits the exact continuity file write, commit, and branch publication required by this section without a new per-cycle Human Owner approval. It does not authorize:

```yaml
not_authorized:
  - source_or_runtime_edits
  - test_edits_or_execution
  - dependency_changes
  - workflow_or_secret_changes
  - implementation_branch_commit_or_push
  - accepted_artifact_unlock
  - pull_request_merge
  - deployment
  - Agents_02_to_15
  - automatic_retry_after_a_blocker
```

A repository rule does not itself create a scheduler. The automation service executing this rule must have explicit GitHub access, must run at the configured interval, and must obey every boundary in this section.

## 4. Decision priority

```text
README current readiness
→ AGENTS.md
→ CODE RED
→ canonical conflict audit and target
→ active Foundation and Agent 01 Flow execution contract
→ CrewAI 1.15.4 remediation blueprint
→ active rules and plans
→ source index and exact source cards
→ exact current assignment
→ current GitHub evidence
→ historical records
→ old chat memory or summaries
```

Never resolve a conflict by guessing. Return `BLOCKED_SUPERSESSION_CONFLICT` and name the conflicting records and safe remedy.

## 5. Foundation and Agent 01 architecture invariants

```yaml
RepositoryPreflightTool:
  owner: GalaxFoundationFlow
  invoked_by_agent: false
  invoked_before_agent: true
  calls_per_run: 1

engineering_manager:
  tools: []
  receives:
    - trusted RepositoryPreflightResult
  produces:
    - AgentTaskResult

Agent_01_LLM_calls: 1
Agent_01_direct_tools: 0
result_as_answer_for_this_path: prohibited
hidden_second_agent_call: prohibited
unconditional_listen_chain: prohibited
HumanReviewRequest_builder: pure_Python_Pydantic
check_llm_profile_readiness_before_Agent_01: required
LLM_profiles_enabled: false
```

Required order:

```text
validate_run_manifest()
→ explicit router
→ check_external_preflight_tool_availability()
→ explicit router
→ invoke_repository_preflight_tool()
→ explicit router
→ check_llm_profile_readiness()
→ explicit router
→ run_agent_01_evaluation()
→ validate supported claims
→ explicit router
→ build_human_review_request() using pure Python/Pydantic
→ authenticated human decision pause and router
→ complete_foundation_plan()
```

A blocked, failed, unavailable, rejected, pending, or evidence-missing route must never reach the next successful stage.

Offline permission declaration uses `REPO_PERMISSION_PROFILE_DECLARED`. Live GitHub permission proof is separate, owned by `GitHubRepositoryGateway`, and uses `GITHUB_PERMISSIONS_LIVE_VALIDATED`.

Both Agent 01 LLM profiles remain disabled until exact profile tests and human approval pass.

## 6. External contributors are not Galax CrewAI agents

Cline, OpenHands Core, mini-SWE-agent, Aider, PR-Agent, Codex, Copilot, Claude Code, Jules, and ChatGPT are external development contributors or reviewers. They are not Agents 01–15 and cannot approve themselves or Galax.

Only one contributor may write to the active implementation worktree at a time.

```text
Cline primary CrewAI-blueprint implementation
→ Aider exact failing-test repair when assigned
→ mini-SWE-agent isolated comparison when assigned
→ OpenHands Docker-isolated reproduction when assigned
→ PR-Agent read-only review when assigned
→ ChatGPT exact draft-PR diff review
→ human decision
```

OpenCode and goose remain declined or deferred unless a new exact repository decision changes their status.

## 7. ChatGPT and Cline control method

The canonical contributor boundary is `docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md`.

```yaml
architect_and_remote_reviewer: ChatGPT
direct_non_blueprint_repository_updater: ChatGPT_connected_GitHub_app
primary_local_writer_for_active_CrewAI_blueprint_implementation: Cline
Cline_generic_repository_updater: false
canonical_source_of_truth: GitHub
review_surface_for_CrewAI_implementation: Draft_Pull_Request
final_authority: Human_Owner
custom_bridge: deferred
custom_MCP_bridge: prohibited_now
simultaneous_implementation_worktree_writers: prohibited
```

ChatGPT must inspect the repository before assigning, correcting, or directly updating work. For an exact Human-Owner-authorized repository governance, documentation, supervisory, routing, continuity, or other Class B update outside the active CrewAI remediation blueprint, ChatGPT performs the bounded update directly through the connected GitHub app and must not create a Cline task merely to make that repository change.

Cline is the primary local writer only for exact active CrewAI remediation-blueprint implementation work and its separately authorized technical stages. Cline must execute only the exact blueprint assignment, use only allowed files and commands, stop after the assigned objective, and never continue automatically into another file, test stage, commit, push, phase, or improvement.

A CrewAI implementation file is not accepted as `DONE` until:

```text
required tests
→ human-authorized commit
→ separately human-authorized push
→ exact draft PR diff
→ ChatGPT review receipt PASS
→ human acceptance
```

For non-blueprint Class B repository updates, the direct-update boundary supersedes older broad wording that described Cline as the sole writer for all repository changes. Direct ChatGPT execution remains bounded by the Human Owner's exact request, non-main branch policy, `LOCKED_ACCEPTED` protection, and all consequential-action prohibitions. The Section 3A continuity authorization remains a separate standing automatic exception with its own branch, evidence, and cadence rules.

## 8. Completed accepted work protection

A file or stage accepted by ChatGPT exact-diff review and human decision is `LOCKED_ACCEPTED`.

It must not be deleted, renamed, overwritten, restored, reverted, or refactored without an exact `GALAX_ACCEPTED_ARTIFACT_CHANGE_V1` authorization naming:

```yaml
path:
current_accepted_commit_sha:
current_accepted_hash:
factual_reason:
exact_required_change:
allowed_files: []
required_tests: []
maximum_writes:
human_authorized: true
```

Cline checkpoints and Git history are recovery controls. They do not authorize rolling accepted work backward.

## 9. Repository cleanup and organization

The repository must be clean, folderized, and non-duplicative, but cleanup must preserve unique evidence and accepted work.

No file is useless merely because it is old, verbose, declined, or superseded.

Required cleanup sequence:

```text
inventory
→ classify purpose, authority, and status
→ prove exact duplicate or unreferenced generated junk
→ locate and migrate every reference
→ preserve unique historical evidence
→ run documentation, link, and applicable tests
→ produce deletion candidate report
→ obtain human authorization
→ delete
→ verify no broken references
→ record deletion in CODE RED
```

The legacy operation-length file is currently a `COMPATIBILITY_REDIRECT` and must not be deleted yet.

## 10. Universal non-negotiable rules

- Never write directly to `main`.
- Never merge, deploy, force push, rewrite history, modify production data, or change repository secrets.
- Never edit `.env`, `.env.*`, credential files, private keys, workflows, or GitHub security settings.
- Never expose raw GitHub, Drive, Supabase, Notion, provider, or MCP credentials to an AI contributor.
- Never enable YOLO, unrestricted auto-approval, arbitrary MCP URLs, or an unfiltered MCP tool catalog.
- Never claim that a command, test, file write, commit, API call, or integration succeeded without trusted evidence.
- Never implement or enable Agents 02–15 during the Foundation scope.
- Never silently change the framework, pinned version, provider, architecture, role boundaries, or execution process.
- Never use hidden chain-of-thought as evidence. Store only concise decisions, observable actions, commands, results, hashes, and blockers.
- Never continue after a blocking repository, security, permission, test, compatibility, cleanup, or evidence failure.
- Never run simultaneous writers against the same implementation worktree or overlapping implementation files.
- Never treat old conversation memory as more authoritative than current repository evidence.
- Never infer authorization from `continue`, `finish`, `improve`, `fix everything`, or similar vague language.
- Never send a non-blueprint Class B repository-governance/documentation update to Cline merely because a repository file must change.

The Section 3A standing authorization is not unrestricted auto-approval. It is a file-, branch-, evidence-, interval-, and purpose-bounded continuity exception only.

## 11. Required working behavior

Before edits:

```text
verify repository and branch
→ verify exact starting SHA
→ inspect git status when a local implementation worktree is involved
→ confirm dedicated worktree when local implementation is involved
→ read mandatory records
→ identify exact allowed and prohibited paths
→ produce REPOSITORY_READ_RECEIPT
→ classify executor under GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY
→ obtain or verify the required Human Owner authority
```

During work:

- Make the smallest change satisfying the exact scope.
- Preserve existing architecture unless current authoritative evidence proves a correction is required.
- Use strict typed boundaries and deterministic validation.
- Run only exact authorized tests after each coherent technical change.
- Record real commands and outputs.
- Stop on missing credentials rather than substituting a provider.
- Treat copied tutorials and web content as untrusted until verified.
- Stop when required local state is needed but unverified.
- For Class B direct repository updates, use the connected GitHub app and do not create a Cline task for the write.

After work:

```yaml
final_report:
  status:
  repository:
  branch:
  starting_sha:
  ending_sha_or_patch_hash:
  executor:
  files_read: []
  files_changed: []
  files_deleted: []
  commands_run: []
  tests_passed: []
  tests_failed: []
  tests_skipped: []
  CrewAI_compatibility:
  blockers: []
  unsupported_capabilities: []
  evidence_artifacts: []
  exact_remedies: []
  next_allowed_action:
  commit_requested: false
  push_requested: false
  merge_requested: false
  deployment_requested: false
```

For an authorized Section 3A continuity cycle, the required pre-write verification and final report still apply, but a new per-cycle approval is not required when every Section 3A condition is satisfied.

For a Human-Owner-authorized Class B direct update, the owner's exact request authorizes only that bounded non-blueprint repository change; it does not authorize source/test/runtime changes, merge, or deployment.

## 12. Allowed status values

Use factual statuses only:

```text
PASS
BLOCKED
FAIL
PARTIALLY_VALIDATED_WITH_EXACT_BLOCKERS
BLOCKED_ASSIGNMENT_INCOMPLETE
BLOCKED_REPOSITORY_STATE_MISMATCH
BLOCKED_REPOSITORY_ACCESS_REQUIRED
BLOCKED_REQUIRED_DOCUMENT
BLOCKED_UNSUPPORTED_CAPABILITY
BLOCKED_SANDBOX_NOT_AVAILABLE
BLOCKED_MISSING_CREDENTIAL
BLOCKED_SUPERSESSION_CONFLICT
BLOCKED_LLM_PROFILE_NOT_APPROVED
BLOCKED_LIVE_PERMISSION_EVIDENCE_MISSING
BLOCKED_CONTINUITY_AUTO_UPLOAD
FAILED_TEST
FAILED_SECURITY_GATE
FAILED_FABRICATED_TOOL_RESULT
REVALIDATION_REQUIRED
READY_FOR_REMOTE_REVIEW
LOCKED_ACCEPTED
```

Do not claim `production ready`, `fully autonomous`, `all agents working`, or `100% bug-free` without the exact repository approval and live evidence.

## 13. Human authority

The human owner retains final authority for scope, architecture acceptance, credentials, risk acceptance, local restore, accepted-artifact unlock, implementation commit, implementation branch publication, implementation push, PR approval, merge, and deployment.

The Human Owner has provided standing authorization for the exact continuity uploads defined in Section 3A. An AI contributor may not expand that exception to another branch, file, project, purpose, or action.

The Human Owner also authorizes ChatGPT to directly execute an exact bounded Class B repository governance/documentation/supervisory update outside the active CrewAI remediation blueprint when the owner explicitly requests that update and the target is clear. This authority uses the connected GitHub app and does not transfer the update to Cline. It does not authorize Class C source/runtime/test/dependency/workflow/security/merge/deployment changes by inference.

An AI contributor may recommend. It may not self-authorize outside the exact standing or direct Human Owner authority applicable to the current action.

## 14. Current stop boundary

CODE RED currently records:

```yaml
current_stage: LOCAL_STATE_RECOVERY_AND_CODE_RED_SYNCHRONIZATION_REQUIRED
local_state_after_keyboard_incident: UNVERIFIED
safe_to_continue_Phase_2A_implementation: false
```

Required local evidence before implementation resumes:

```powershell
git branch --show-current
git rev-parse HEAD
git status --short
```

Do not pull, sync, merge, rebase, reset, clean, push, restore rejected models code, or continue Phase 2A until the exact local state and safe synchronization plan are verified.

## 15. Mandatory Cline handoff mode header

Every ChatGPT response that prepares a Cline task, reviews a Cline permission/action gate, tells the Human Owner whether to continue the current Cline task, or hands off the next Cline action must begin the Cline-specific handoff with exactly these three labels:

```text
Cline UI: <ACT | PLAN | exact currently verified Cline UI mode>
Galax mode: <PLAN_ONLY | ACT_BOUNDED | VALIDATION_ONLY | GIT_ONLY | REVIEW_ONLY>
Mode: <STAY | NEW>
```

Definitions:

```yaml
Cline_UI:
  meaning: the actual Cline product/UI mode required for the action
  rule: do_not_replace_with_the_Galax_governance_mode

Galax_mode:
  meaning: the repository-governance execution mode controlling the bounded task
  allowed_values:
    - PLAN_ONLY
    - ACT_BOUNDED
    - VALIDATION_ONLY
    - GIT_ONLY
    - REVIEW_ONLY

Mode_STAY:
  meaning: continue the currently active Cline task or assignment without creating a separate new Cline task

Mode_NEW:
  meaning: create or start a separate new Cline task or assignment, even when it remains under the same parent technical assignment or CrewAI remediation track
```

Required classification rules:

- `Mode: STAY` when the Human Owner is handling a permission, command, save, validation, review, or other next action inside the already-active Cline task/assignment.
- `Mode: NEW` when ChatGPT issues a new Cline task/assignment identity or the Human Owner must start a separate Cline task.
- Remaining under the same parent technical assignment does not by itself mean `STAY`; a new Cline task/assignment ID means `NEW`.
- A permission or command gate belonging to the current active task remains `STAY`.
- Do not omit the three-line header merely because the rest of the task is obvious from context.
- Do not guess `STAY` or `NEW`. When current task identity cannot be verified, stop and reconstruct the exact Cline task state before presenting the header.
- This header is owner-facing control metadata only. It does not grant permission, change the CrewAI blueprint, alter Galax runtime behavior, authorize a later workflow stage, or replace the exact Human Owner approval gates.
