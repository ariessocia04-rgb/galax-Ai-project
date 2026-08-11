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

It must make a new chat continue the same repository-backed Galax goal instead of behaving like a fresh project, repeating completed setup, or changing contributor roles.

Before `PASS`, it must reconstruct and preserve:

- current repository-backed project goal;
- active track and exact current assignment/stage;
- exact stop point and resume action;
- completed work and `LOCKED_ACCEPTED` state;
- rejected/superseded work;
- actions not to repeat;
- current Cline prompting/permission/rejection/save/validation/Git rules;
- the Human Owner's exact ChatGPT → Cline implementation separation;
- ChatGPT supervisory/continuity direct-write exceptions and their hard limits;
- the two-way executor blockers.

It produces one `GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V2` and returns `PASS` only when the original Human Owner request can continue safely without guessing or role drift.

## 2. New-chat principle

```yaml
new_chat_means_new_project: false
new_chat_means_restart_setup: false
new_chat_means_new_goal: false
new_chat_authorizes_new_technical_stage: false
required_behavior: resume_same_repository_backed_Galax_goal
```

Repository evidence overrides stale chat memory.

A new conversation must not reinterpret tool availability as new executor authority.

## 3. Activation / invalidation gate

Treat the conversation as `NEW_OR_UNVERIFIED_CHAT` when no valid current bootstrap receipt exists.

Also require a fresh bootstrap after a material invalidation such as:

```yaml
bootstrap_invalidation:
  - explicit_context_loss
  - conversation_length_recovery
  - CODE_RED_recovery_that_requires_reconstruction
  - repository_identity_change
  - canonical_router_change_material_to_current_routing
  - contributor_role_separator_change
  - active_assignment_identity_change_not_already_processed_in_current_chat
  - unresolved_authority_conflict
```

## 4. Mandatory dependencies and support

Bootstrap must load exactly these two dependency skills:

```yaml
required_dependency_skills:
  - $galax-repository-state-scope-guardian
  - $galax-strict-cline-prompt-guardian
```

Also load the Context Engineer as non-skill support.

Purpose separation:

```text
Skill 8 = new-chat readiness and exact continuation
Skill 1 = current repository truth and bounded scope
Skill 2 = exact ChatGPT → Cline prompting/action control
Context Engineer = minimum verified context packaging
```

Skill 10 is not added as a third bootstrap dependency because bootstrap itself does not issue a real Cline task. The new chat must nevertheless know that Skill 10 becomes mandatory before the later normal cycle can issue real Cline work.

## 5. Mandatory first reads

After Skill 8 is selected, fetch and follow completely:

```text
docs/operations/GALAX_NEW_CHAT_OPERATING_MANUAL.md
```

Also verify the current contributor-role separator when role ownership is material:

```text
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
```

If the operating manual is unavailable:

```text
BLOCKED_NEW_CHAT_OPERATING_MANUAL_UNAVAILABLE
```

If the contributor-role separator is required but unavailable:

```text
BLOCKED_NEW_CHAT_ROLE_SEPARATOR_UNAVAILABLE
```

Do not substitute a dated continuity guide as the current bootstrap controller.

## 6. Exact continuation state

Reconstruct at minimum:

```yaml
GALAX_NEW_CHAT_CONTINUATION_STATE_V2:
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

If a material identity is unknown, do not invent it.

## 7. Human Owner's canonical implementation chain

Before bootstrap `PASS`, the new chat must understand exactly:

```text
Human Owner
   ↓
ChatGPT
→ decides WHAT should be done
→ gives one exact bounded command / Cline task
   ↓
Cline
→ executes locally
→ edits/saves only authorized CrewAI implementation
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

Bootstrap must not pass if the new chat believes ChatGPT may take over Cline's CrewAI implementation/edit/validation/commit/push stage.

## 8. Two-way role separator readiness

Required role map:

```yaml
GALAX_NEW_CHAT_EXECUTOR_ROLE_MAP_V2:
  Human_Owner:
    final_authority: true

  ChatGPT:
    CrewAI_role: architect_supervisor_reviewer
    CrewAI_implementation_writer: false
    CrewAI_implementation_commit_executor: false
    CrewAI_implementation_push_executor: false
    direct_supervisory_writer: narrow_Skill_9_allowlist_only
    direct_continuity_writer: narrow_Skill_5_allowlist_only

  Cline:
    CrewAI_role: primary_local_executor_for_active_remediation_blueprint
    implementation_writer: true_when_exactly_authorized
    validation_executor: true_when_separately_authorized
    implementation_commit_executor: true_when_separately_authorized
    implementation_push_executor: true_when_separately_authorized
    ChatGPT_supervisory_writer: false
    continuity_writer: false
```

Hard blockers:

```text
ChatGPT tries to edit/save/commit/push active CrewAI blueprint/source/tests/implementation
→ BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE

Cline tries to edit/save/commit/push ChatGPT skill/router/context/supervisory rule/length/achievement
→ BLOCKED_CLINE_SUPERVISORY_SCOPE
```

There is no ChatGPT blueprint-edit exception.

## 9. Narrow ChatGPT direct-write exceptions

A new chat must know that ChatGPT direct GitHub writing is not a generic repository-writer role.

Skill 9 may be used only for exact Human-Owner-requested supervisory-control maintenance:

```yaml
Skill_9_exact_scope:
  - edit_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_router
  - update_Context_Engineer_support_contract
  - update_ChatGPT_Cline_supervisory_rule_or_role_separator
  - update_canonical_new_chat_supervisory_operating_instruction
```

Skill 5 may directly handle only its exact continuity/achievement duties:

```yaml
Skill_5_exact_scope:
  - update_length_problem
  - update_achievement
  - qualifying_terminal_PASS_achievement_persistence
```

Generic documentation, plans, research, blueprint files, source, tests, dependencies, workflows, implementation Git, merge, and deployment are not automatically ChatGPT direct-write work.

## 10. Cline prompting and stage separation readiness

Bootstrap must understand the current live Skill 2 method:

```text
one task
→ one objective
→ one mode
→ exact allowlists
→ exact prohibitions
→ one stop condition
→ one receipt
```

Modes:

```yaml
PLAN_ONLY: read_search_analyze_plan_preview_without_mutation
ACT_BOUNDED: one_exact_authorized_edit_or_action
VALIDATION_ONLY: one_exact_authorized_validation
GIT_ONLY: one_exact_authorized_Git_stage
REVIEW_ONLY: exact_evidence_review_without_mutation
```

Consequential stages remain separate:

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

A ChatGPT PASS does not automatically authorize commit or push.

## 11. Mandatory Skill 10 awareness

Before the post-bootstrap normal cycle issues any real Cline task:

```text
Router selects Skill 2
→ load Skill 10 as mandatory dependency
→ prove exact active blueprint trace
→ require PASS_CLINE_BLUEPRINT_ONLY
→ only then issue GALAX_CLINE_TASK_V2
```

Bootstrap itself does not call Skill 10 as a third dependency, but must preserve this rule exactly.

## 12. Permission and rejection readiness

A new chat must preserve the live Skill 2 permission gate and reject-with-correction behavior.

Every rejection must preserve correct work and, when knowable, provide exact replacement instructions:

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

A rejection is not a reset and never silently authorizes its replacement action.

## 13. UI/button readiness

Never invent a visible action button.

Distinguish exactly:

```yaml
NO_BUTTON_LABEL:
  meaning: visible_button_with_exact_label_No_exists

NO_ACTION_BUTTON_VISIBLE:
  meaning: no_relevant_action_button_is_visible

UNKNOWN_UI_STATE:
  meaning: current_UI_cannot_be_verified
```

Button evidence may come only from current reliable Human Owner screenshot/text or a current tool/connector output exposing the action label.

## 14. Anti-repeat and lock preservation

Before recommending any setup/action:

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

Do not repeat a completed action when no material identity changed.
Do not modify `LOCKED_ACCEPTED` without the applicable unlock/change authority.

## 15. Technical architecture protection

Bootstrap changes no CrewAI runtime architecture:

```yaml
CrewAI_runtime_changed: false
GalaxFoundationFlow_changed: false
Agent_01_changed: false
Agents_02_to_15_changed: false
Process_changed: false
CrewAI_memory_changed: false
CrewAI_reasoning_changed: false
CrewAI_planning_changed: false
source_changed: false
tests_changed: false
dependencies_changed: false
```

For technical continuation, recover the current active blueprint/technical contract/assignment exactly. Skill 8 does not invent a new technical roadmap.

## 16. Bootstrap readiness gate

Before `PASS`, establish:

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
  Skill_10_predelegation_gate_understood: true | false
  commit_and_push_separate_owner_gates_understood: true | false

  prompting_rules_understood: true | false
  approval_rules_understood: true | false
  rejection_with_correction_understood: true | false
  button_detection_understood: true | false
  automatic_next_technical_stage_prohibited: true | false
  technical_plan_not_changed: true | false
  ready: true | false
```

If any mandatory field is false or current evidence conflicts, do not return `PASS`.

## 17. Blockers

Use the smallest accurate blocker:

```text
BLOCKED_NEW_CHAT_OPERATING_MANUAL_UNAVAILABLE
BLOCKED_NEW_CHAT_ROLE_SEPARATOR_UNAVAILABLE
BLOCKED_NEW_CHAT_OPERATING_RULES_INCOMPLETE
BLOCKED_NEW_CHAT_REPOSITORY_STATE_UNVERIFIED
BLOCKED_NEW_CHAT_CONTEXT_CONFLICT
BLOCKED_NEW_CHAT_LOCK_CONFLICT
BLOCKED_NEW_CHAT_EXECUTOR_ROLE_CONFLICT
```

## 18. Bootstrap receipt

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
    ChatGPT_CrewAI_role: architect_supervisor_reviewer
    Cline_CrewAI_role: primary_local_executor
    ChatGPT_CrewAI_direct_write_blocked: true | false
    Cline_supervisory_direct_write_blocked: true | false
    Skill_9_narrow_exception_understood: true | false
    Skill_5_narrow_exception_understood: true | false
    Skill_10_required_before_real_Cline_task: true | false

  Human_Owner:
    final_authority_preserved: true | false
    current_authorization:
    additional_authorization_required:

  original_request:

  next_routing:
    original_request_preserved: true | false
    exact_primary_skill_for_original_request:
    original_request_can_continue: true | false

  assumptions: []
  safe_to_continue: true | false
```

## 19. Handoff after bootstrap

A Skill 8 `PASS` authorizes only a separate routing cycle for the **same original Human Owner request**.

```yaml
automatic_new_technical_stage: prohibited
invent_next_task: prohibited
preserve_original_Human_Owner_request: required
post_bootstrap_allowed_action: route_same_original_request_only
```

If the original request requires a consequential action not yet authorized, the normal Human Owner gate remains required.

## 20. Final contract

```text
new/unverified Galax chat
→ Router selects Skill 8
→ Skill 8 loads New Chat Operating Manual
→ load Skill 1 + Skill 2 dependencies
→ load Context Engineer support
→ verify contributor role separator
→ reconstruct exact repository-backed continuation state
→ verify original ChatGPT → Cline implementation chain
→ verify ChatGPT CrewAI hard block
→ verify Cline supervisory hard block
→ verify narrow Skill 9 / Skill 5 exceptions
→ verify Skill 10 is mandatory before any later real Cline task
→ produce GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V2
→ PASS only when safe_to_continue=true
→ route only the same original Human Owner request
→ stop at the selected skill boundary
```
