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

It exists so that a new ChatGPT conversation does not behave like a new Galax project, repeat completed setup, forget accepted work, guess the current target, or relearn the Human Owner's Cline-control method from scratch.

The required outcome is:

```text
new ChatGPT conversation
→ recover repository-backed Galax memory
→ continue the same verified goal
→ continue from the exact verified stop point
→ preserve completed/locked/rejected work
→ know the mandatory prompting, permission, reject/correction, button/no-button, save, validation, and Git rules
→ process the original Human Owner request safely
```

## 2. Core continuation rule

```yaml
GALAX_NEW_CHAT_CONTINUATION_PRINCIPLE_V1:
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
```

Repository evidence overrides stale chat memory or a dated snapshot.

## 3. Mandatory bootstrap architecture

For the first Galax request in a new/unverified conversation:

```text
fetch canonical Router
→ Router selects $galax-new-chat-bootstrap-guardian as primary Skill 8
→ load Skill 1 as dependency
→ load Skill 2 as dependency
→ load Context Engineer as non-skill support
→ Skill 8 reads this manual
→ reconstruct and compact current verified state
→ produce GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V1
→ if PASS, begin a separate routing cycle for the same original Human Owner request
→ do not invent a next task or stage
```

Exactly one primary skill remains active per routing cycle. Skill 1 and Skill 2 are dependencies only during bootstrap. Context Engineer is not a skill and does not consume a dependency slot.

## 4. Authority map a new chat must know

```yaml
GALAX_NEW_CHAT_AUTHORITY_MAP_V1:
  Human_Owner:
    authority: final

  GitHub:
    role: canonical_repository_truth

  Router:
    alias: Skill_0
    authority: select_one_primary_skill_and_max_two_dependencies

  New_Chat_Bootstrap:
    alias: $galax-new-chat-bootstrap-guardian
    skill_id: GALAX-SKILL-08
    authority: new_chat_readiness_and_continuation_bootstrap

  Repository_State:
    alias: $galax-repository-state-scope-guardian
    authority: repository_truth_scope_stage_and_one_safe_next_action

  Cline_Prompting:
    alias: $galax-strict-cline-prompt-guardian
    authority: Cline_prompt_permission_rejection_correction_and_stop_rules

  Evidence_Review:
    alias: $galax-evidence-validation-acceptance-guardian
    authority: review_edit_test_commit_push_evidence

  Draft_PR_Review:
    alias: $galax-draft-pr-exact-diff-reviewer
    authority: exact_remote_diff_review

  Continuity:
    alias: $galax-continuity-achievement-guardian
    authority: length_checkpoint_and_achievement_persistence

  Locked_Artifact:
    alias: $galax-locked-artifact-guardian
    authority: accepted_work_lock_review

  Cleanup:
    alias: $galax-repository-cleanup-auditor
    authority: cleanup_candidate_audit_only

  Context_Engineer:
    path: docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md
    registered_skill: false
    authority: minimum_verified_context_packaging_only
```

Do not collapse these roles into one component.

## 5. Minimum new-chat reading order

Use the smallest exact evidence path that proves the current continuation state.

Mandatory startup order:

```text
1. canonical Router
2. Skill 8
3. this New Chat Operating Manual
4. Skill 1 dependency
5. Skill 2 dependency
6. Context Engineer support contract
7. README.md
8. AGENTS.md
9. docs/operations/CODE_RED.md when required by current continuation/recovery state
10. active CrewAI focus lock when the original request is technical
11. latest valid continuity checkpoint from the canonical continuity branch when continuation state is needed
12. achievement record only when required to identify completed/accepted/do-not-repeat state
13. exact active assignment, branch, HEAD, target, PR, test, or evidence required for the original request
14. stop reading when the bootstrap receipt can be decided safely
```

Do not read every checkpoint, every skill, every plan, every source file, or the full repository by default.

## 6. Canonical continuity source

For cross-chat operational continuation, use the live continuity controls and latest valid checkpoint rather than a dated old new-chat guide.

```yaml
continuity_branch: docs/new-chat-continuity-2026-07-27
continuity_PR: 10
latest_checkpoint_rule: latest_valid_numbered_Length_Problem_checkpoint
```

Retrieve only the latest valid checkpoint plus directly required referenced evidence. Do not replay all historical volumes unless a conflict or missing fact requires it.

The dated file:

```text
docs/operations/GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md
```

is not the canonical bootstrap controller. Treat its fixed historical state as historical evidence unless a current higher-authority record explicitly requires a specific section.

## 7. Required goal and state recovery

A new chat must establish:

```yaml
GALAX_GOAL_CONTINUITY_V1:
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

If any material identity is unknown, do not invent it. Use Skill 1 to resolve it or block.

## 8. Setup reuse and anti-repeat gate

A new chat must classify setup/work before recommending anything:

```yaml
GALAX_SETUP_REUSE_GATE_V1:
  verified_completed_setup: []
  verified_completed_environment_steps: []
  verified_completed_assignments: []
  completed_and_LOCKED_ACCEPTED: []
  rejected_or_superseded_work: []
  setup_steps_not_to_repeat: []
  commands_tests_or_actions_not_to_repeat: []
  current_missing_prerequisites: []
  current_required_setup_only: []
  setup_restart_required: false
```

Rules:

- If repository evidence proves a setup step complete, do not repeat it.
- If repository evidence proves a command/test/action already completed and no material state changed, do not rerun it.
- Never restore rejected code or rejected workflow as accepted work.
- Never modify `LOCKED_ACCEPTED` merely because the new conversation lacks prior chat context.
- Only recommend new setup when exact current evidence proves a required prerequisite is missing.

## 9. Cline prompting method every new chat must know

The new chat must use live Skill 2 as the exact authority.

Core rule:

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
PLAN_ONLY:
  use_for: read_search_analyze_plan_preview_without_mutation

ACT_BOUNDED:
  use_for: one_exact_Human_Owner_authorized_edit_or_action

VALIDATION_ONLY:
  use_for: one_exact_test_or_command

GIT_ONLY:
  use_for: one_exact_Git_action

REVIEW_ONLY:
  use_for: exact_evidence_or_diff_review_without_mutation
```

Do not combine stages merely for convenience.

## 10. Consequential-action separation

Every new chat must preserve:

```text
PLAN ≠ ACT
ACT ≠ SAVE
SAVE ≠ TEST
TEST ≠ FIX
FIX ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ MERGE
MERGE ≠ DEPLOY
```

Authorization for one stage never silently authorizes a later stage.

## 11. Permission decision gate

Before recommending approval of a Cline action, verify all six:

```yaml
GALAX_CLINE_PERMISSION_GATE_V1:
  directly_required_by_current_objective:
  exact_path_or_command_allowlisted:
  matches_current_mode:
  not_already_completed:
  does_not_exceed_stop_condition:
  does_not_modify_LOCKED_ACCEPTED_without_exact_unlock:
```

All true:

```text
APPROVE — <brief factual reason>
```

Any false:

```text
REJECT — <brief factual reason>
```

and apply the exact rejection-with-correction contract below.

ChatGPT recommends. The Human Owner decides.

## 12. Mandatory reject-with-correction behavior

A rejection is not a reset.

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

Rules:

1. Preserve every correct evidence-supported part.
2. Reject only the exact noncompliant part.
3. Freeze correct scope so Cline does not redo, rewrite, delete, broaden, revert, or invalidate it.
4. Do not upgrade merely preserved work to `LOCKED_ACCEPTED`.
5. Give the exact replacement action when knowable.
6. Do not say only `try again`, `fix it`, `redo it`, or `use the correct command` when the exact correction is known.
7. A rejection never silently grants permission to execute the replacement.
8. Stop after the bounded reject/correction decision.

## 13. Mandatory UI/button detection

A new chat must reason from actual visible UI evidence, not imagined controls.

```yaml
GALAX_UI_ACTION_DETECTION_V1:
  evidence_source:
    HUMAN_OWNER_SCREENSHOT |
    HUMAN_OWNER_UI_TEXT |
    CURRENT_TOOL_OUTPUT |
    UNKNOWN

  visible_buttons: []

  recognized_action_labels:
    approve_button:
    reject_button:
    no_button:
    cancel_button:
    deny_button:
    allow_button:
    run_button:
    proceed_button:
    confirm_button:
    save_button:
    retry_button:
    other_buttons: []

  actionable_gate_detected: true | false
  exact_button_recommended:
  button_recommendation:
    APPROVE |
    REJECT |
    CLICK_NO |
    CLICK_CANCEL |
    CLICK_DENY |
    CLICK_RUN |
    CLICK_PROCEED |
    DO_NOT_CLICK |
    NO_ACTION_BUTTON_VISIBLE |
    UNKNOWN
  factual_reason:
  Human_Owner_decision_required: true | false
```

## 14. `No` button versus no button

These are different states and must never be confused:

```yaml
NO_BUTTON_LABEL:
  meaning: a_visible_button_with_exact_label_No_exists
  behavior: may_recommend_CLICK_NO_only_when_policy_decision_is_reject_and_button_is_verified_visible

NO_ACTION_BUTTON_VISIBLE:
  meaning: no_relevant_action_button_is_visible
  behavior: do_not_tell_Human_Owner_to_click_a_button; provide_exact_next_instruction

UNKNOWN_UI_STATE:
  meaning: current_UI_cannot_be_verified
  behavior: state_policy_decision_without_inventing_button_label
```

Examples:

```text
Visible [Yes] [No] + action is not allowed
→ REJECT
→ exact visible action: Click No
→ explain reason
→ preserve correct work
→ provide exact replacement instruction
→ stop
```

```text
No action button visible
→ do not say "Click Reject" or "Click No"
→ state NO_ACTION_BUTTON_VISIBLE
→ provide exact next Cline instruction or blocker
```

```text
UI not supplied/visible
→ do not guess a button
→ state UNKNOWN_UI_STATE
→ provide policy decision and exact correction only
```

## 15. Save and edit behavior

A proposed edit is not a saved edit.

Before save, require a complete reviewable change under the live Skill 2 contract.

A save authorization applies only to the exact reviewed change and does not authorize:

- another file;
- nearby cleanup;
- formatting;
- tests;
- Ruff;
- dependency changes;
- Git operations;
- another task.

## 16. Validation behavior

Validation is a separate task.

Required characteristics:

```yaml
validation:
  exact_command_or_test: required
  expected_result: required
  additional_tests: prohibited_unless_listed
  automatic_fix_after_failure: prohibited
  automatic_retry: prohibited
  file_changes_during_validation: prohibited_unless_separately_authorized
  next_action_requires_separate_authorization: true
```

## 17. Git behavior

Each Git operation is independently bounded unless a current higher-authority rule explicitly says otherwise.

Default:

```yaml
git_status: separate_task_when_needed
commit: separate_authorization
push: separate_authorization
merge: separate_authorization
force_push: prohibited
history_rewrite: prohibited
```

Do not interpret local save as remote publication.

## 18. `LOCKED_ACCEPTED` behavior

A new chat must recover and protect current accepted work.

Do not:

- rewrite;
- delete;
- rename;
- restore over;
- refactor;
- repeatedly rerun an accepted test;
- include locked work in unrelated cleanup;

without exact lock evidence review and Human Owner authorization under Skill 6.

## 19. CrewAI technical-plan protection

This manual is ChatGPT governance only.

It must never be interpreted as modifying:

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

For a technical original request, read the active CrewAI remediation focus lock and map the technical action before execution. Preserve the existing narrow Foundation supersession when applicable.

Skill 8 and this manual do not create a new technical roadmap.

## 20. Bootstrap readiness checklist

Skill 8 may return `PASS` only when all current mandatory items are established:

```yaml
GALAX_NEW_CHAT_BEHAVIOR_READINESS_GATE_V1:
  router_verified: true | false
  operating_manual_loaded: true | false
  Skill_1_loaded: true | false
  Skill_2_loaded: true | false
  Context_Engineer_loaded: true | false
  repository_truth_reconstructed: true | false
  same_goal_preserved: true | false
  exact_stop_point_known: true | false
  completed_setup_identified: true | false
  missing_setup_identified: true | false
  actions_not_to_repeat_identified: true | false
  LOCKED_ACCEPTED_preserved: true | false
  rejected_or_superseded_preserved: true | false
  prompting_rules_understood: true | false
  permission_rules_understood: true | false
  rejection_with_correction_understood: true | false
  button_detection_understood: true | false
  No_button_understood: true | false
  no_visible_button_understood: true | false
  unknown_UI_state_understood: true | false
  button_guessing_prohibited: true | false
  automatic_next_technical_stage_prohibited: true | false
  technical_plan_not_changed: true | false
  ready: true | false
```

If required state is missing or conflicting, block instead of guessing.

## 21. Required bootstrap receipt

```yaml
GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V1:
  bootstrap_status: PASS | BLOCKED
  session_state: NEW_OR_UNVERIFIED_CHAT

  repository: ariessocia04-rgb/galax-Ai-project
  router_ref: docs/chatgpt-skill-router-2026-08-02

  authority:
    router_verified:
    operating_manual_verified:
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

  setup_state:
    completed_setup: []
    missing_required_setup: []
    setup_steps_not_to_repeat: []

  protection:
    completed_work: []
    LOCKED_ACCEPTED: []
    rejected_or_superseded: []
    actions_not_to_repeat: []
    prohibited_next_actions: []

  UI_and_permission_readiness:
    button_detection_ready:
    reject_with_correction_ready:
    no_visible_button_behavior_ready:
    unknown_UI_behavior_ready:

  Human_Owner:
    current_authorization:
    additional_authorization_required:

  original_request:

  continuation:
    same_goal_preserved: true | false
    restart_setup: false
    new_goal_invented: false

  next_routing:
    original_request_preserved: true | false
    exact_primary_skill_for_original_request:
    original_request_can_continue: true | false

  assumptions: []
  safe_to_continue: true | false
```

## 22. Post-bootstrap rule

A successful bootstrap is a prerequisite, not a technical milestone.

After bootstrap `PASS`:

```text
preserve exact original Human Owner request
→ start a separate Router cycle
→ select the one primary skill that owns that original request
→ reuse only still-current verified bootstrap evidence
→ perform only that bounded request
→ stop normally
```

Do not invent or auto-start another development stage.

## 23. Failure behavior

Use the smallest accurate blocker:

```text
BLOCKED_NEW_CHAT_OPERATING_MANUAL_UNAVAILABLE
BLOCKED_NEW_CHAT_OPERATING_RULES_INCOMPLETE
BLOCKED_NEW_CHAT_REPOSITORY_STATE_UNVERIFIED
BLOCKED_NEW_CHAT_CONTEXT_CONFLICT
BLOCKED_NEW_CHAT_LOCK_CONFLICT
BLOCKED_ROUTER_OR_SKILL_UNAVAILABLE
BLOCKED_CONTEXT_ENGINEER_UNAVAILABLE
```

Never resolve a material conflict by guessing.

## 24. Final operating contract

```text
NEW / UNVERIFIED GALAX CHAT
→ Router
→ Skill 8
→ this Operating Manual
→ Skill 1 + Skill 2 dependencies
→ Context Engineer
→ current repository truth + latest valid continuity boundary
→ same goal + exact unfinished work + completed setup + locks + do-not-repeat
→ mandatory prompting/permission/rejection/UI-button/no-button readiness
→ GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V1
→ PASS only when safe_to_continue=true
→ separate routing cycle for the same original Human Owner request only
→ no invented next stage
```
