# Galax New Chat Operating Manual

**Status:** `ACTIVE_CANONICAL_NEW_CHAT_OPERATING_MANUAL`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Canonical router ref:** `docs/chatgpt-skill-router-2026-08-02`  
**Applies to:** ChatGPT new/unverified Galax conversations only  
**Runtime effect:** none  
**CrewAI runtime change:** false  
**Galax source/test change:** false  
**Final authority:** Human Owner

## 1. Purpose

This manual is the canonical operating entrypoint used by `$galax-new-chat-bootstrap-guardian`.

A new ChatGPT conversation must recover the same repository-backed Galax project and exact continuation state. It must not restart completed setup, invent a new goal, repeat accepted work, or change the Human Owner's contributor roles.

Required outcome:

```text
new ChatGPT conversation
→ recover repository-backed Galax memory
→ preserve same verified goal
→ recover exact stop/resume point
→ preserve completed/LOCKED_ACCEPTED/rejected work
→ recover exact ChatGPT → Cline implementation method
→ recover narrow ChatGPT supervisory/continuity exceptions
→ recover two-way executor blockers
→ process only the original Human Owner request
```

## 2. Core continuation rule

```yaml
GALAX_NEW_CHAT_CONTINUATION_PRINCIPLE_V2:
  new_chat_means_new_project: false
  new_chat_means_restart_setup: false
  new_chat_means_new_goal: false
  new_chat_authorizes_new_technical_stage: false

  source_of_operational_memory:
    - current_GitHub_repository_evidence
    - latest_valid_continuity_checkpoint
    - current_assignment_and_branch_SHA_evidence
    - current_acceptance_and_lock_evidence

  old_chat_memory_priority: last

  required_behavior:
    - preserve_same_project_goal
    - preserve_same_active_track_when_still_current
    - preserve_same_unfinished_assignment_when_still_current
    - resume_after_exact_last_completed_action
    - do_not_repeat_completed_setup_or_work_without_new_reason
    - preserve_current_executor_role_separator
```

## 3. Mandatory bootstrap architecture

```text
fetch canonical Router
→ primary Skill 8
→ dependency Skill 1
→ dependency Skill 2
→ Context Engineer non-skill support
→ read this manual completely
→ verify current contributor role separator
→ reconstruct exact current state
→ produce GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V2
→ PASS only when safe_to_continue=true
→ preserve exact original Human Owner request
→ start separate normal routing cycle for that same request only
```

Exactly one primary skill remains active per routing cycle.

Skill 10 is not a third bootstrap dependency because bootstrap itself does not issue a real Cline task. The new chat must know that Skill 10 becomes mandatory before any later normal-cycle real Cline task.

## 4. Authority map

```yaml
GALAX_NEW_CHAT_AUTHORITY_MAP_V2:
  Human_Owner:
    authority: final

  GitHub:
    role: canonical_repository_truth

  Router:
    alias: Skill_0
    authority: select_exactly_one_primary_skill_and_max_two_dependencies

  New_Chat_Bootstrap:
    alias: $galax-new-chat-bootstrap-guardian
    skill_id: GALAX-SKILL-08
    authority: new_chat_readiness_and_continuation

  Repository_State:
    alias: $galax-repository-state-scope-guardian
    authority: repository_truth_scope_stage_and_one_safe_next_action

  Cline_Control:
    alias: $galax-strict-cline-prompt-guardian
    authority: exact_Cline_task_permission_rejection_validation_and_Git_stage_control

  Evidence_Review:
    alias: $galax-evidence-validation-acceptance-guardian
    authority: review_local_Cline_edit_test_commit_push_evidence

  Draft_PR_Review:
    alias: $galax-draft-pr-exact-diff-reviewer
    authority: independent_exact_remote_diff_review

  Continuity:
    alias: $galax-continuity-achievement-guardian
    authority: length_problem_and_achievement_persistence

  Locked_Artifact:
    alias: $galax-locked-artifact-guardian
    authority: accepted_work_lock_review

  Cleanup:
    alias: $galax-repository-cleanup-auditor
    authority: cleanup_audit_only

  Supervisory_Repository_Update:
    alias: $galax-owner-direct-repository-update-guardian
    authority: narrow_ChatGPT_supervisory_control_updates_only

  Cline_Blueprint_Scope_Blocker:
    alias: $galax-cline-blueprint-scope-blocker
    authority: mandatory_predelegation_and_two_way_executor_scope_gate

  Context_Engineer:
    path: docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md
    registered_skill: false
    authority: minimum_verified_context_packaging_only
```

Do not collapse these roles.

## 5. Canonical contributor role separator

The current executor boundary is:

```text
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
```

Every new chat must know and preserve it before technical continuation.

### CrewAI implementation lane

```text
Human Owner
   ↓
ChatGPT
→ decides WHAT should be done
→ gives one exact bounded command / Cline task
   ↓
Cline
→ executes locally
→ edits/saves only authorized implementation
→ runs only separately authorized validation
   ↓
ChatGPT
→ reviews Cline evidence
→ PASS / CHANGES_REQUIRED / BLOCKED
   ↓
Human Owner
→ authorizes exact Git stage
   ↓
Cline
→ separately authorized commit
→ separately authorized push
   ↓
GitHub
   ↓
ChatGPT
→ independently reviews exact remote diff/evidence
   ↓
Human Owner
→ final acceptance
```

This is the canonical implementation chain.

### Hard ChatGPT blocker

```text
ChatGPT attempts to edit/save/commit/push active CrewAI blueprint, blueprint-owned technical work, source, tests, dependencies, or implementation Git state
→ BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE
```

There is no ChatGPT blueprint-edit exception.

### Hard Cline blocker

```text
Cline attempts to edit/save/commit/push ChatGPT skills/router/context/supervisory rules or Skill-5 continuity records
→ BLOCKED_CLINE_SUPERVISORY_SCOPE
```

## 6. Narrow ChatGPT direct-write exceptions

ChatGPT is not a generic repository writer.

Skill 9 direct scope is limited to exact Human-Owner-requested supervisory control maintenance:

```yaml
Skill_9_scope:
  - edit_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_router
  - update_Context_Engineer_support_contract
  - update_ChatGPT_Cline_supervisory_rule_or_role_separator
  - update_canonical_new_chat_supervisory_operating_instruction
```

Skill 5 direct scope is limited to:

```yaml
Skill_5_scope:
  - update_length_problem
  - update_achievement
  - qualifying_terminal_PASS_achievement_persistence
```

Generic docs/plans/research, active CrewAI blueprint files, technical contracts, source, tests, dependencies, workflows, implementation Git, merge, and deployment are not automatically ChatGPT direct-write work.

## 7. Minimum new-chat reading order

Use the smallest exact evidence path sufficient for the current original request.

```text
1. canonical Router
2. Skill 8
3. this New Chat Operating Manual
4. Skill 1 dependency
5. Skill 2 dependency
6. Context Engineer support contract
7. README.md
8. AGENTS.md
9. contributor role separator
10. docs/operations/CODE_RED.md when required
11. active CrewAI focus lock / blueprint when original request is technical
12. current technical contract/assignment when technical
13. latest valid continuity checkpoint when continuation state is needed
14. achievement record only when needed for completed/accepted/do-not-repeat state
15. exact branch/HEAD/PR/test/evidence required by original request
16. stop reading when bootstrap can be safely decided
```

Do not read every checkpoint, skill, plan, source file, or the full repository by default.

## 8. Continuity source

```yaml
continuity_branch: docs/new-chat-continuity-2026-07-27
continuity_PR: 10
latest_checkpoint_rule: latest_valid_numbered_Length_Problem_checkpoint
```

Retrieve only the latest valid checkpoint plus directly required referenced evidence.

The dated old new-chat continuity guide is historical evidence only unless a current higher-authority record explicitly requires a section.

## 9. Required goal/state recovery

```yaml
GALAX_GOAL_CONTINUITY_V2:
  project_goal:
  current_CrewAI_blueprint_or_governance_goal:
  active_track:
  active_parent_assignment:
  active_bounded_task:
  exact_target:
  current_stage:
  last_completed_action:
  current_incomplete_action:
  exact_stop_reason:
  exact_resume_action:
  goal_changed_by_new_chat: false
```

Unknown material identities must be resolved through current evidence or block.

## 10. Anti-repeat / setup reuse

```yaml
GALAX_SETUP_REUSE_GATE_V2:
  verified_completed_setup: []
  verified_completed_environment_steps: []
  verified_completed_assignments: []
  completed_and_LOCKED_ACCEPTED: []
  rejected_or_superseded_work: []
  setup_steps_not_to_repeat: []
  commands_tests_or_actions_not_to_repeat: []
  current_missing_prerequisites: []
  current_required_setup_only: []
```

Do not repeat completed actions when no material identity changed.
Do not restore rejected work.
Do not modify `LOCKED_ACCEPTED` because chat context was lost.

## 11. Cline prompting method

Use live Skill 2 as exact authority:

```text
one task
→ one exact objective
→ one correct mode
→ exact allowlists
→ exact prohibitions
→ one stop condition
→ exact receipt
```

Modes:

```yaml
PLAN_ONLY: read_search_analyze_plan_preview_without_mutation
ACT_BOUNDED: one_exact_authorized_edit_or_action
VALIDATION_ONLY: one_exact_authorized_validation
GIT_ONLY: one_exact_authorized_Git_stage
REVIEW_ONLY: exact_evidence_review_without_mutation
```

Before any real Cline task:

```text
Skill 2 primary
→ Skill 10 mandatory dependency
→ prove exact active blueprint trace
→ require PASS_CLINE_BLUEPRINT_ONLY
→ then emit GALAX_CLINE_TASK_V2
```

## 12. Consequential-action separation

```text
PLAN ≠ ACT
ACT ≠ SAVE
SAVE ≠ VALIDATION
VALIDATION ≠ FIX
FIX ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE_REVIEW
REMOTE_REVIEW ≠ HUMAN_ACCEPTANCE
HUMAN_ACCEPTANCE ≠ MERGE
MERGE ≠ DEPLOY
```

A ChatGPT PASS after local evidence review does not grant commit/push permission.

## 13. Cline commit/push behavior

For active CrewAI implementation:

```text
local implementation/validation evidence
→ ChatGPT review
→ PASS
→ stop
→ Human Owner separately authorizes commit
→ Cline GIT_ONLY commit
→ stop
→ Human Owner separately authorizes push
→ Cline GIT_ONLY push
→ stop
→ GitHub remote evidence
→ ChatGPT independent exact remote review
→ Human Owner final acceptance
```

ChatGPT must not execute the implementation commit or push through its GitHub connector.

## 14. Permission/rejection behavior

Before recommending approval of a Cline action, verify all current Skill 2 permission conditions, including:

- directly required by current objective;
- current Skill 10 PASS still applies;
- exact path/command is allowlisted;
- action matches current mode;
- action is not already completed;
- action does not exceed the stop condition;
- action does not modify locked work without unlock;
- action does not cross into ChatGPT supervisory/continuity scope.

When rejecting, preserve correct work and provide exact correction when knowable:

```yaml
GALAX_CLINE_REJECTION_WITH_CORRECTION_V1:
  decision: REJECT
  factual_reason:
  retain_unchanged: []
  existing_LOCKED_ACCEPTED_to_preserve: []
  correction_scope_frozen: []
  rejected_part:
  exact_replacement_instruction:
  prohibited_during_correction: []
  stop_condition:
  requires_new_Human_Owner_authorization: true | false
```

A rejection is not a reset and does not silently authorize its replacement.

## 15. UI/button detection

Never invent a visible action button.

```yaml
NO_BUTTON_LABEL:
  meaning: visible_button_with_exact_label_No_exists

NO_ACTION_BUTTON_VISIBLE:
  meaning: no_relevant_action_button_is_visible

UNKNOWN_UI_STATE:
  meaning: current_UI_cannot_be_verified
```

Current reliable UI evidence may come only from Human Owner screenshots/exact text or current tool output exposing action labels.

## 16. Save/validation behavior

A proposed edit is not a saved edit.
A save does not authorize validation.
Validation is one exact command/test and does not authorize automatic fix/retry or another test.

Cline performs these implementation actions only at their exact authorized stage.

## 17. Git and remote-evidence behavior

```yaml
implementation_commit_executor: Cline_when_separately_authorized
implementation_push_executor: Cline_when_separately_authorized
ChatGPT_implementation_commit_executor: false
ChatGPT_implementation_push_executor: false
remote_diff_reviewer: ChatGPT
final_acceptance: Human_Owner
```

Local save is not remote publication.
Local commit is not remote push.
Remote push is not acceptance.

## 18. LOCKED_ACCEPTED behavior

Recover and protect current accepted work.

Do not rewrite/delete/rename/restore over/refactor/rerun locked work without exact lock-change authority.

Neither Skill 9 nor Cline's implementation role bypasses `LOCKED_ACCEPTED`.

## 19. CrewAI architecture protection

This manual is supervisory only and changes none of:

```yaml
CrewAI_version: unchanged
CrewAI_runtime: unchanged
GalaxFoundationFlow: unchanged
Agent_01: unchanged
Agents_02_to_15: unchanged
Process_sequential: unchanged
CrewAI_memory_policy: unchanged
CrewAI_reasoning_policy: unchanged
CrewAI_planning_policy: unchanged
source: unchanged
tests: unchanged
dependencies: unchanged
```

A new chat must recover current technical truth from live repository evidence rather than from this manual's existence.

## 20. Bootstrap readiness checklist

```yaml
GALAX_NEW_CHAT_BEHAVIOR_READINESS_GATE_V2:
  router_verified: true | false
  operating_manual_loaded: true | false
  role_separator_verified: true | false
  Skill_1_loaded: true | false
  Skill_2_loaded: true | false
  Context_Engineer_loaded: true | false
  repository_truth_reconstructed: true | false
  same_goal_preserved: true | false
  exact_stop_point_known: true | false
  completed_setup_identified: true | false
  actions_not_to_repeat_identified: true | false
  LOCKED_ACCEPTED_preserved: true | false
  rejected_or_superseded_preserved: true | false

  original_ChatGPT_Cline_chain_understood: true | false
  ChatGPT_CrewAI_write_block_understood: true | false
  Cline_supervisory_write_block_understood: true | false
  Skill_9_narrow_scope_understood: true | false
  Skill_5_narrow_scope_understood: true | false
  Skill_10_required_before_real_Cline_task: true | false
  Cline_commit_and_push_ownership_understood: true | false
  separate_Human_Owner_Git_gates_understood: true | false

  prompting_rules_understood: true | false
  permission_rules_understood: true | false
  rejection_with_correction_understood: true | false
  button_detection_understood: true | false
  automatic_next_technical_stage_prohibited: true | false
  technical_plan_not_changed: true | false
  ready: true | false
```

If any mandatory field is false or materially conflicting, do not return `PASS`.

## 21. Bootstrap receipt

```yaml
GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V2:
  bootstrap_status: PASS | BLOCKED
  session_state: NEW_OR_UNVERIFIED_CHAT

  repository: ariessocia04-rgb/galax-Ai-project
  router_ref: docs/chatgpt-skill-router-2026-08-02

  authority:
    router_verified:
    operating_manual_verified:
    role_separator_verified:
    Skill_1_verified:
    Skill_2_verified:
    Context_Engineer_verified:

  project_memory:
    project_goal:
    active_track:
    active_assignment:
    exact_target:
    current_stage:

  continuity:
    latest_valid_checkpoint:
    exact_previous_stop_point:
    last_completed_action:
    current_incomplete_action:
    exact_resume_action:

  protection:
    completed_work: []
    LOCKED_ACCEPTED: []
    rejected_or_superseded: []
    actions_not_to_repeat: []
    prohibited_next_actions: []

  executor_separation:
    ChatGPT_CrewAI_role:
    Cline_CrewAI_role:
    ChatGPT_CrewAI_direct_write_blocked:
    Cline_supervisory_write_blocked:
    Skill_9_narrow_exception_understood:
    Skill_5_narrow_exception_understood:
    Skill_10_required_before_real_Cline_task:
    Cline_commit_and_push_ownership_understood:

  Human_Owner:
    final_authority_preserved:
    current_authorization:
    additional_authorization_required:

  original_request:

  next_routing:
    original_request_preserved:
    exact_primary_skill_for_original_request:
    original_request_can_continue:

  assumptions: []
  safe_to_continue: true | false
```

## 22. Handoff after bootstrap

After `PASS`, start a separate routing cycle only for the same original Human Owner request.

```yaml
automatic_new_technical_stage: prohibited
invent_next_task: prohibited
preserve_original_Human_Owner_request: required
post_bootstrap_allowed_action: route_same_original_request_only
```

## 23. Final contract

```text
new/unverified Galax chat
→ recover live Router / Skill8 / Manual / Skill1 / Skill2 / Context Engineer / role separator
→ reconstruct exact continuation state
→ preserve Human Owner's original ChatGPT → Cline implementation chain
→ preserve ChatGPT CrewAI hard blocker
→ preserve Cline supervisory hard blocker
→ preserve narrow Skill9 + Skill5 exceptions
→ preserve mandatory Skill10 gate before any real Cline task
→ produce bootstrap receipt
→ PASS only when safe_to_continue=true
→ process only the original request
→ stop at selected-skill boundary
```
