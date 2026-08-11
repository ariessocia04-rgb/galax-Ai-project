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

- current project goal, active track, assignment/stage, stop point, and resume action;
- completed work, `LOCKED_ACCEPTED`, rejected/superseded work, and actions not to repeat;
- the normal Human Owner → ChatGPT → Cline implementation chain;
- ChatGPT Skill 9 supervisory and Skill 5 continuity direct-write scopes;
- the normal ChatGPT CrewAI write blocker and Cline supervisory blocker;
- Skill 11 Tagalog requirements / fact-check / English specification behavior;
- Skill 12 owner-authorized technical fallback behavior;
- any completed ChatGPT fallback commit/work that Cline must preserve and continue from;
- the zero-coding-owner rule.

It produces one `GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V3` and returns `PASS` only when the original Human Owner request can continue safely without guessing or role drift.

## 2. New-chat principle

```yaml
new_chat_means_new_project: false
new_chat_means_restart_setup: false
new_chat_means_new_goal: false
new_chat_authorizes_new_technical_stage: false
required_behavior: resume_same_repository_backed_Galax_goal
```

Repository evidence overrides stale chat memory.
A new conversation must not reinterpret tool availability as executor authority without the current Router and role-separator rules.

## 3. Activation / invalidation gate

Treat the conversation as `NEW_OR_UNVERIFIED_CHAT` when no valid current bootstrap receipt exists.

Also require a fresh bootstrap after:

```yaml
bootstrap_invalidation:
  - explicit_context_loss
  - conversation_length_recovery
  - CODE_RED_recovery_that_requires_reconstruction
  - repository_identity_change
  - canonical_router_change_material_to_current_routing
  - contributor_role_separator_change
  - Skill_11_or_Skill_12_material_rule_change
  - active_assignment_identity_change_not_already_processed_in_current_chat
  - unresolved_authority_conflict
```

## 4. Mandatory dependencies and support

Bootstrap loads exactly:

```yaml
required_dependency_skills:
  - $galax-repository-state-scope-guardian
  - $galax-strict-cline-prompt-guardian
```

Also load the Context Engineer as non-skill support.

```text
Skill 8 = new-chat readiness and continuation
Skill 1 = repository truth and bounded scope
Skill 2 = normal ChatGPT → Cline prompting/action control
Context Engineer = minimum verified context packaging
```

Skill 10 is not a third bootstrap dependency because bootstrap itself does not issue a real Cline task. It becomes mandatory before a later normal Cline task.
Skill 11 or Skill 12 is selected only in a separate later routing cycle when its exact trigger applies.

## 5. Mandatory first reads

After Skill 8 is selected, fetch and follow completely:

```text
docs/operations/GALAX_NEW_CHAT_OPERATING_MANUAL.md
```

Verify:

```text
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
```

If unavailable, return the exact blocker:

```text
BLOCKED_NEW_CHAT_OPERATING_MANUAL_UNAVAILABLE
BLOCKED_NEW_CHAT_ROLE_SEPARATOR_UNAVAILABLE
```

Do not substitute a dated continuity guide as current bootstrap controller.

## 6. Exact continuation state

```yaml
GALAX_NEW_CHAT_CONTINUATION_STATE_V3:
  project_goal:
  current_blueprint_or_governance_goal:
  active_track:
  active_parent_assignment:
  active_bounded_task:
  exact_target:
  current_stage:
  current_executor:
  latest_completed_action:
  current_incomplete_action:
  exact_stop_reason:
  exact_resume_action:
  completed_setup: []
  missing_required_setup: []
  completed_and_LOCKED_ACCEPTED: []
  completed_ChatGPT_fallback_work_to_preserve: []
  current_Skill_12_fallback_baseline_if_any:
  rejected_or_superseded: []
  actions_not_to_repeat: []
  prohibited_next_actions: []
```

If a material identity is unknown, do not invent it.

## 7. Normal implementation chain readiness

Before bootstrap `PASS`, the new chat must understand the default chain:

```text
Human Owner
→ ChatGPT decides WHAT should be done and gives one exact bounded Cline task
→ Cline executes/edits/saves only authorized implementation
→ Cline runs only authorized validation
→ ChatGPT reviews evidence
→ Human Owner authorizes exact Git stage
→ Cline commits and later pushes only when authorized
→ GitHub exposes exact remote evidence
→ ChatGPT independently reviews exact remote diff
→ Human Owner final acceptance
```

A ChatGPT `PASS` does not itself authorize commit or push.

## 8. Executor role map

```yaml
GALAX_NEW_CHAT_EXECUTOR_ROLE_MAP_V3:
  Human_Owner:
    final_authority: true
    coding_knowledge_required: false

  ChatGPT:
    normal_CrewAI_role: architect_supervisor_reviewer
    CrewAI_implementation_writer_by_default: false
    CrewAI_implementation_commit_executor_by_default: false
    CrewAI_implementation_push_executor_by_default: false
    technical_fallback_executor: true_only_after_Skill_12_PASS_and_explicit_Human_Owner_authorization
    direct_supervisory_writer: Skill_9_only
    direct_continuity_writer: Skill_5_only

  Cline:
    CrewAI_role: primary_local_executor_for_active_remediation_blueprint
    implementation_writer: true_when_exactly_authorized
    validation_executor: true_when_authorized
    implementation_commit_executor: true_when_authorized
    implementation_push_executor: true_when_authorized
    ChatGPT_supervisory_writer: false
    continuity_writer: false
```

Normal blockers:

```text
ChatGPT technical write without valid Skill 12
→ BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE

Cline supervisory/continuity write
→ BLOCKED_CLINE_SUPERVISORY_SCOPE
```

## 9. Skill 12 readiness

Bootstrap must know the exception but must not activate it automatically.

```yaml
Skill_12_minimum_gate:
  exact_current_action_known: true
  one_of:
    - Cline_capability_limit_factually_proven
    - Cline_materially_mismatched_same_bounded_goal_again_after_one_exact_corrected_retry
  ChatGPT_current_exact_tool_capability_proven: true
  Human_Owner_explicit_fallback_authorization: true
  exact_authorized_stages_known: true
  no_LOCKED_ACCEPTED_conflict: true
  no_unrelated_scope_expansion: true
  no_simultaneous_overlapping_writer: true
  result: PASS_CHATGPT_TECHNICAL_FALLBACK
```

A single Cline mistake is insufficient.

After successful fallback:

```text
verify exact result / remote commit / diff
→ preserve ChatGPT-created work as current repository truth
→ Cline must not redo/overwrite/revert it
→ Cline resumes from new verified state
```

If Cline local state is behind/conflicting, ChatGPT prepares the exact safe Cline reconciliation task; the Human Owner only approves/rejects it.

## 10. Skill 11 readiness

Bootstrap must know that unclear new rule/skill requests route to Skill 11.

```text
Skill 11
→ ask only necessary questions in simple Tagalog
→ never ask Human Owner to code, edit files, write YAML/JSON, or run Git/terminal commands
→ preserve already-answered details
→ verify live repository constraints
→ bounded current web fact-check using official/primary sources before feasibility conclusion
→ POSSIBLE / POSSIBLE_WITH_CONSTRAINTS / NOT_POSSIBLE_AS_REQUESTED
→ factual remedy/alternative when needed
→ recommend repository destination
→ final repository-ready specification in English
→ Human Owner approves/rejects
→ separate Skill 9 write cycle
```

If requirements are already exact, do not ask redundant questions; route directly to Skill 9.

## 11. Zero-coding-owner rule

Bootstrap must preserve:

```yaml
owner_manual_coding: prohibited_as_default_or_fallback
owner_manual_repository_editing: prohibited_when_authorized_AI_or_tool_can_do_it
owner_manual_Git_or_terminal_commands: prohibited_when_authorized_AI_or_tool_can_do_it
owner_role: plain_language_goal_and_authorization
```

If no available actor/tool can perform a required action, verify the blocker, research a factual remedy/alternative, and ask the Human Owner only for the decision/authorization.

## 12. Narrow ChatGPT direct-write exceptions

Skill 9 exact scope:

```yaml
- edit_or_update_ChatGPT_skill
- add_or_update_ChatGPT_skill
- add_or_update_ChatGPT_router
- update_Context_Engineer_support_contract
- update_ChatGPT_Cline_supervisory_rule_or_role_separator
- update_canonical_new_chat_supervisory_operating_instruction
```

Skill 5 exact scope:

```yaml
- update_length_problem
- update_achievement
- qualifying_terminal_PASS_achievement_persistence
```

These are not generic repository-writing authority.

## 13. Cline prompting and stage separation readiness

Bootstrap must understand Skill 2 normal method:

```text
one task
→ one objective
→ one mode
→ exact allowlists
→ exact prohibitions
→ one stop condition
→ one receipt
```

Normal stages:

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

Skill 12 fallback also separates stages by default, but the Human Owner may explicitly combine multiple fully bounded fallback stages in one authorization.

## 14. Mandatory Skill 10 awareness

Before the post-bootstrap normal cycle issues any real Cline task:

```text
Router selects Skill 2
→ load Skill 10
→ prove exact active blueprint trace
→ require PASS_CLINE_BLUEPRINT_ONLY
→ only then issue GALAX_CLINE_TASK_V2
```

## 15. Permission, rejection, UI, save and validation readiness

The new chat must preserve live Skill 2 rules for exact permission, reject-with-correction, UI/button evidence, save vs preview, and validation-only stages.

Never invent a visible button.
Never treat rejection as reset or silent replacement authority.
Never automatically fix/retry after a validation failure.

## 16. Anti-repeat and lock preservation

```yaml
GALAX_SETUP_REUSE_GATE_V3:
  verified_completed_setup: []
  verified_completed_assignments: []
  completed_and_LOCKED_ACCEPTED: []
  completed_ChatGPT_fallback_actions_not_to_repeat: []
  rejected_or_superseded_work: []
  setup_steps_not_to_repeat: []
  commands_tests_or_actions_not_to_repeat: []
  current_missing_prerequisites: []
```

Do not repeat completed work or overwrite an accepted ChatGPT fallback result because executor ownership later returned to Cline.

## 17. Technical architecture protection

Bootstrap changes no CrewAI runtime architecture, source, tests, dependencies, Process settings, Agents 01–15 behavior, or technical roadmap.

Recover technical truth from current repository evidence.

## 18. Bootstrap readiness gate

```yaml
GALAX_NEW_CHAT_BEHAVIOR_READINESS_GATE_V3:
  router_verified: true | false
  operating_manual_loaded: true | false
  role_separator_verified: true | false
  Skill_1_loaded: true | false
  Skill_2_loaded: true | false
  Context_Engineer_loaded: true | false
  repository_truth_reconstructed: true | false
  same_goal_preserved: true | false
  exact_stop_point_known: true | false
  LOCKED_ACCEPTED_preserved: true | false
  actions_not_to_repeat_identified: true | false

  normal_ChatGPT_Cline_chain_understood: true | false
  normal_ChatGPT_CrewAI_write_block_understood: true | false
  Cline_supervisory_write_block_understood: true | false
  Skill_9_scope_understood: true | false
  Skill_5_scope_understood: true | false
  Skill_10_predelegation_gate_understood: true | false
  Skill_11_Tagalog_fact_check_workflow_understood: true | false
  Skill_12_fallback_gate_understood: true | false
  Cline_resume_after_fallback_understood: true | false
  zero_coding_owner_rule_understood: true | false

  automatic_next_technical_stage_prohibited: true | false
  technical_plan_not_changed: true | false
  ready: true | false
```

Any material false/conflict blocks bootstrap PASS.

## 19. Bootstrap receipt

```yaml
GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V3:
  bootstrap_status: PASS | BLOCKED
  session_state: NEW_OR_UNVERIFIED_CHAT
  repository: ariessocia04-rgb/galax-Ai-project
  router_ref: docs/chatgpt-skill-router-2026-08-02

  authority_files_verified: []

  project_memory:
    project_goal:
    active_track:
    active_assignment:
    exact_target:
    current_stage:
    current_executor:

  continuity:
    latest_valid_checkpoint:
    exact_previous_stop_point:
    last_completed_action:
    current_incomplete_action:
    exact_resume_action:

  protection:
    completed_work: []
    LOCKED_ACCEPTED: []
    completed_ChatGPT_fallback_work_to_preserve: []
    rejected_or_superseded: []
    actions_not_to_repeat: []
    prohibited_next_actions: []

  executor_rules:
    normal_Cline_first_lane_understood: true | false
    Skill_12_exception_understood: true | false
    zero_coding_owner_rule_understood: true | false

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

## 20. Handoff after bootstrap

A Skill 8 PASS authorizes only a separate routing cycle for the same original Human Owner request.

```yaml
automatic_new_technical_stage: prohibited
invent_next_task: prohibited
preserve_original_Human_Owner_request: required
post_bootstrap_allowed_action: route_same_original_request_only
```

## 21. Final contract

```text
new/unverified Galax chat
→ Router selects Skill 8
→ Skill 8 reads New Chat Operating Manual and role separator
→ load Skill 1 + Skill 2 + Context Engineer
→ reconstruct exact repository-backed continuation state
→ preserve normal Cline-first chain
→ preserve narrow Skill 9 / Skill 5 direct-write scopes
→ preserve Skill 11 Tagalog requirements + web fact-check + English spec workflow
→ preserve Skill 12 owner-authorized technical fallback
→ preserve ChatGPT-created fallback work as current repository truth
→ never ask Human Owner to code manually when an authorized actor/tool can do the job
→ bootstrap PASS only when safe_to_continue=true
→ route only the same original Human Owner request
→ stop at selected skill boundary
```
