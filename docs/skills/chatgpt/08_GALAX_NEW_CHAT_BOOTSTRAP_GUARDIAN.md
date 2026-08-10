```yaml
skill_reference: $galax-new-chat-bootstrap-guardian
skill_id: GALAX-SKILL-08
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 8: Galax New Chat Bootstrap Guardian

```yaml
skill_name: Galax New Chat Bootstrap Guardian
skill_type: ChatGPT_new_chat_continuation_bootstrap_skill
active_project: Galax_AI_only
repository: ariessocia04-rgb/galax-Ai-project
runtime_agent: false
CrewAI_agent: false
Galax_Agent_01_to_15: false
local_writer: false
approval_authority: false
source_code_authority: none
test_authority: none
dependency_authority: none
CrewAI_runtime_authority: none
merge_authority: none
deployment_authority: none
final_authority: Human_Owner
```

## 1. Purpose

This skill is the mandatory bootstrap guardian for a new or unverified Galax ChatGPT conversation.

Its job is to make a new chat continue the same repository-backed Galax goal instead of behaving like a fresh project or repeating setup that the repository already proves is complete.

It must:

- load the canonical New Chat Operating Manual;
- reconstruct the current repository-backed continuation state;
- preserve the same project goal, current track, current assignment, exact stop point, completed work, `LOCKED_ACCEPTED`, rejected/superseded work, and actions that must not be repeated;
- learn the mandatory Cline prompting, permission, rejection, correction, mode, UI-button, no-button, save, validation, and Git boundaries before the new chat is declared ready;
- produce one `GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V1`;
- return `PASS` only when the new chat can safely process the original Human Owner request without guessing or restarting completed setup.

This skill does not implement Galax source or tests and is not part of the CrewAI runtime.

## 2. Activation gate

Treat the current Galax conversation as `NEW_OR_UNVERIFIED_CHAT` when a Galax request is present and no valid `GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V1` for the current conversation is available.

Also require a fresh bootstrap when a prior receipt is materially invalidated by:

```yaml
bootstrap_invalidation:
  - explicit_context_loss
  - conversation_length_recovery
  - CODE_RED_recovery_that_requires_reconstruction
  - repository_identity_change
  - canonical_router_change_material_to_current_routing
  - active_assignment_identity_change_not_already_processed_in_current_chat
  - unresolved_authority_conflict
```

Do not infer that a new technical goal exists merely because the ChatGPT conversation is new.

```yaml
new_chat_means_new_project: false
new_chat_means_restart_setup: false
new_chat_means_new_goal: false
required_behavior: resume_same_repository_backed_Galax_goal
```

## 3. Mandatory bootstrap dependencies

For the Skill 8 bootstrap routing cycle, the router must load exactly these two dependency skills unless an exact higher-authority blocker prevents it:

```yaml
required_dependency_skills:
  - $galax-repository-state-scope-guardian
  - $galax-strict-cline-prompt-guardian
```

The canonical Context Engineer must also be loaded as the normal non-skill support contract and does not consume a dependency slot.

Purpose separation:

```text
Skill 8 = HOW a new chat boots and proves readiness
Skill 1 = WHAT repository state is true now
Context Engineer = WHAT minimum verified context is carried forward
Skill 2 = HOW Cline is prompted, approved/rejected, corrected, and stopped
```

Skill 8 must not perform Skill 1 or Skill 2 authority in their place.

## 4. Mandatory first read

After Skill 8 is selected, fetch and follow completely:

```text
docs/operations/GALAX_NEW_CHAT_OPERATING_MANUAL.md
```

If the manual cannot be fetched from the canonical router ref, return:

```text
BLOCKED_NEW_CHAT_OPERATING_MANUAL_UNAVAILABLE
```

Do not substitute the dated `GALAX_NEW_CHAT_CONTINUITY_GUIDE_2026-07-27.md` as the current bootstrap controller. Dated continuity records may be historical evidence only unless a higher-authority current record explicitly says otherwise.

## 5. Exact continuation principle

A new chat must recover operational memory from repository evidence, not from guesses or raw old-chat recollection.

It must determine, at minimum:

```yaml
continuation_state:
  project_goal:
  current_blueprint_or_governance_goal:
  active_track:
  active_parent_assignment:
  active_bounded_task:
  exact_target:
  current_stage:
  latest_completed_action:
  current_incomplete_action:
  exact_stop_reason:
  exact_resume_action:
  completed_setup: []
  missing_required_setup: []
  completed_and_LOCKED_ACCEPTED: []
  rejected_or_superseded: []
  actions_not_to_repeat: []
  prohibited_next_actions: []
```

If repository evidence proves a setup step is already complete, do not recommend or execute that setup again without a new factual reason.

## 6. Mandatory UI, button, no-button, approve, and reject readiness

Before bootstrap `PASS`, the new chat must understand and preserve the current Skill 2 and Context Engineer rules for actionable Human Owner decisions.

It must distinguish these UI states exactly:

```yaml
GALAX_NEW_CHAT_UI_STATE_V1:
  NO_BUTTON_LABEL:
    meaning: a_visible_button_labeled_No_exists

  NO_ACTION_BUTTON_VISIBLE:
    meaning: no_relevant_action_button_is_visible

  UNKNOWN_UI_STATE:
    meaning: no_reliable_current_UI_evidence_is_available
```

Never invent a visible button.

Button evidence may come only from current reliable evidence such as:

```yaml
button_evidence_sources:
  - Human_Owner_provided_screenshot
  - Human_Owner_provided_exact_UI_text
  - current_tool_or_connector_output_that_exposes_the_action_label
```

Required behavior:

```yaml
GALAX_UI_ACTION_DETECTION_V1:
  evidence_source:
  visible_buttons: []
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

If a visible `No`, `Reject`, `Deny`, `Cancel`, or equivalent button is the correct action, name the exact visible label and explain the factual reason and exact correction that follows.

If no relevant action button is visible, do not tell the Human Owner to click a nonexistent button. State `NO_ACTION_BUTTON_VISIBLE` and provide the exact next bounded instruction instead.

If UI state is unknown, do not guess a label. State that the button cannot be verified and provide the policy decision plus exact replacement instruction.

## 7. Mandatory rejection quality

A new chat must never reduce a knowable correction to a bare rejection.

When rejecting a Cline request, use Skill 2's canonical rejection contract and preserve correct work:

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

Mandatory principles:

- reject only the exact noncompliant part;
- retain correct evidence-supported work;
- freeze correct scope so it is not redone or invalidated;
- never upgrade preserved work to `LOCKED_ACCEPTED` without acceptance evidence;
- provide the exact replacement action when knowable;
- do not silently authorize the correction;
- stop at the current bounded decision gate.

## 8. Mandatory prompting and permission readiness

Before bootstrap `PASS`, the new chat must know and preserve:

```yaml
prompting_readiness:
  one_task_one_goal_one_stop: true
  PLAN_ONLY_behavior: understood
  ACT_BOUNDED_behavior: understood
  VALIDATION_ONLY_behavior: understood
  GIT_ONLY_behavior: understood
  REVIEW_ONLY_behavior: understood
  exact_allowlists_required: true
  repeat_completed_work: prohibited
  automatic_scope_expansion: prohibited
  automatic_test_after_edit: prohibited
  automatic_retry: prohibited
  automatic_Ruff_or_formatting: prohibited
  dependency_change_without_separate_authorization: prohibited
  commit_without_separate_authorization: prohibited
  push_without_separate_authorization: prohibited
  merge_without_separate_authorization: prohibited
  deployment_without_separate_authorization: prohibited
  Human_Owner_final_authority: true
  ChatGPT_recommends_but_does_not_self_approve: true
```

The new chat must use the live Skill 2 contract as authority for the exact Cline task schema and exact permission/rejection behavior. Skill 8 must not fork or silently replace Skill 2 policy.

## 9. CrewAI and technical-plan boundary

Skill 8 is repository governance only.

```yaml
CrewAI_runtime_changed: false
GalaxFoundationFlow_changed: false
Agent_01_changed: false
Agents_02_to_15_changed: false
CrewAI_process_changed: false
CrewAI_memory_changed: false
CrewAI_reasoning_changed: false
CrewAI_planning_changed: false
source_changed: false
tests_changed: false
dependencies_changed: false
```

When the original Human Owner request is technical, the bootstrap must preserve the active CrewAI remediation blueprint focus lock and any existing narrow Foundation supersession. Skill 8 itself does not create a new technical plan.

## 10. Bootstrap readiness gate

Before returning `PASS`, establish:

```yaml
GALAX_NEW_CHAT_BEHAVIOR_READINESS_GATE_V1:
  operating_manual_loaded: true | false
  Skill_1_loaded: true | false
  Skill_2_loaded: true | false
  Context_Engineer_loaded: true | false
  repository_truth_reconstructed: true | false
  same_goal_preserved: true | false
  exact_stop_point_known: true | false
  completed_setup_identified: true | false
  do_not_repeat_identified: true | false
  LOCKED_ACCEPTED_preserved: true | false
  prompting_rules_understood: true | false
  approval_rules_understood: true | false
  rejection_with_correction_understood: true | false
  button_detection_understood: true | false
  No_button_understood: true | false
  no_visible_button_understood: true | false
  unknown_UI_state_understood: true | false
  button_guessing_prohibited: true | false
  technical_plan_not_changed: true | false
  ready: true | false
```

If any mandatory field is false or required evidence is conflicting, do not return `PASS`.

Use the smallest accurate blocker, including:

```text
BLOCKED_NEW_CHAT_OPERATING_MANUAL_UNAVAILABLE
BLOCKED_NEW_CHAT_OPERATING_RULES_INCOMPLETE
BLOCKED_NEW_CHAT_REPOSITORY_STATE_UNVERIFIED
BLOCKED_NEW_CHAT_CONTEXT_CONFLICT
BLOCKED_NEW_CHAT_LOCK_CONFLICT
```

## 11. Canonical bootstrap receipt

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

## 12. Handoff after bootstrap

A Skill 8 `PASS` does not authorize an invented next technical stage.

After `PASS`, the router may start a separate routing cycle only to process the same original Human Owner request that triggered bootstrap.

```yaml
automatic_new_technical_stage: prohibited
invent_next_task: prohibited
preserve_original_Human_Owner_request: required
post_bootstrap_allowed_action: route_same_original_request_only
```

If the original request itself requires a consequential action not already authorized, the normal Human Owner gate remains required.

## 13. Prohibited behavior

```yaml
prohibited:
  - treat_new_chat_as_new_project
  - restart_completed_setup_without_new_evidence
  - repeat_completed_or_rejected_work_without_new_reason
  - guess_branch_SHA_assignment_or_stop_point
  - guess_visible_UI_button
  - tell_owner_to_click_nonexistent_button
  - use_bare_REJECT_when_exact_correction_is_knowable
  - invalidate_correct_work_during_rejection
  - self_approve_for_Human_Owner
  - create_new_CrewAI_agent
  - become_Agent_16
  - modify_CrewAI_runtime
  - modify_Galax_source_or_tests
  - modify_dependencies
  - auto_continue_to_new_technical_stage
  - merge
  - deploy
```

## 14. Final contract

```text
new or unverified Galax chat
→ Router selects Skill 8
→ Skill 8 reads GALAX_NEW_CHAT_OPERATING_MANUAL.md
→ load Skill 1 + Skill 2 as the two bootstrap dependencies
→ load Context Engineer as non-skill support
→ reconstruct repository-backed continuation state
→ verify same goal, exact stop point, completed setup, locks, do-not-repeat, prompting, rejection, UI-button and no-button behavior
→ produce GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V1
→ PASS only when safe_to_continue=true
→ route only the same original Human Owner request in a separate routing cycle
→ stop at that selected skill's normal boundary
```
