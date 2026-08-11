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

A new ChatGPT conversation must recover the same repository-backed Galax project and exact continuation state. It must not restart completed setup, invent a new goal, repeat accepted work, or silently change contributor roles.

Required outcome:

```text
new ChatGPT conversation
→ recover repository-backed Galax memory
→ preserve same verified goal
→ recover exact stop/resume point
→ preserve completed/LOCKED_ACCEPTED/rejected work
→ recover normal ChatGPT → Cline implementation method
→ recover Skill 9 / Skill 5 direct-write scopes
→ recover Skill 11 owner-requirements behavior
→ recover Skill 12 technical fallback rule
→ recover zero-coding-owner rule
→ process only the original Human Owner request
```

## 2. Core continuation rule

```yaml
GALAX_NEW_CHAT_CONTINUATION_PRINCIPLE_V3:
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
    - preserve_any_current_verified_Skill_12_fallback_baseline
```

## 3. Mandatory bootstrap architecture

```text
fetch canonical Router
→ primary Skill 8
→ dependency Skill 1
→ dependency Skill 2
→ Context Engineer non-skill support
→ read this manual completely
→ verify contributor role separator
→ reconstruct exact current state
→ produce GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V3
→ PASS only when safe_to_continue=true
→ preserve exact original Human Owner request
→ start separate normal routing cycle for that same request only
```

Exactly one primary skill remains active per routing cycle.
Skill 10 becomes mandatory before a later normal real Cline task. Skill 11 and Skill 12 are selected only when their own later request/conditions apply.

## 4. Authority map

```yaml
GALAX_NEW_CHAT_AUTHORITY_MAP_V3:
  Human_Owner:
    authority: final
    coding_knowledge_required: false

  GitHub:
    role: canonical_repository_truth

  Router:
    alias: Skill_0
    authority: select_exactly_one_primary_skill_and_max_two_dependencies

  New_Chat_Bootstrap:
    alias: $galax-new-chat-bootstrap-guardian
    skill_id: GALAX-SKILL-08

  Repository_State:
    alias: $galax-repository-state-scope-guardian

  Cline_Control:
    alias: $galax-strict-cline-prompt-guardian

  Evidence_Review:
    alias: $galax-evidence-validation-acceptance-guardian

  Draft_PR_Review:
    alias: $galax-draft-pr-exact-diff-reviewer

  Continuity:
    alias: $galax-continuity-achievement-guardian

  Locked_Artifact:
    alias: $galax-locked-artifact-guardian

  Cleanup:
    alias: $galax-repository-cleanup-auditor

  Supervisory_Repository_Update:
    alias: $galax-owner-direct-repository-update-guardian

  Cline_Blueprint_Scope_Blocker:
    alias: $galax-cline-blueprint-scope-blocker

  Owner_Rule_Skill_Requirements_Feasibility:
    alias: $galax-owner-rule-skill-requirements-feasibility-guardian

  ChatGPT_Technical_Fallback:
    alias: $galax-chatgpt-technical-fallback-executor-guardian

  Context_Engineer:
    path: docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md
    registered_skill: false
```

Do not collapse these roles.

## 5. Canonical contributor role separator

Read and preserve:

```text
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
```

### Normal CrewAI implementation lane

```text
Human Owner
→ ChatGPT decides and gives one exact bounded Cline task
→ Cline executes/edits/saves only authorized implementation
→ Cline runs only authorized validation
→ ChatGPT reviews evidence
→ Human Owner authorizes exact Git stage
→ Cline commits and later pushes only when authorized
→ GitHub exposes exact remote evidence
→ ChatGPT independently reviews exact remote diff
→ Human Owner final acceptance
```

Without a valid Skill 12 fallback gate:

```text
ChatGPT direct CrewAI technical write
→ BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE
```

### Cline supervisory blocker

```text
Cline edits/saves/commits/pushes ChatGPT skills/router/context/supervisory rules or Skill-5 continuity
→ BLOCKED_CLINE_SUPERVISORY_SCOPE
```

## 6. Skill 12 technical fallback rule

A new chat must know that ChatGPT may temporarily execute an exact technical action only when:

```yaml
Skill_12_requirements:
  exact_current_action_known: true
  one_of:
    - Cline_capability_limit_factually_proven
    - Cline_materially_mismatched_same_bounded_goal_again_after_one_exact_corrected_retry
  ChatGPT_current_exact_tool_capability_proven: true
  Human_Owner_explicit_fallback_authorization: true
  authorized_stages_known: true
  no_LOCKED_ACCEPTED_conflict: true
  no_unrelated_scope_expansion: true
  no_simultaneous_overlapping_writer: true
  gate_result: PASS_CHATGPT_TECHNICAL_FALLBACK
```

A single Cline mistake is insufficient.
Skill 12 is selected in a separate routing cycle. It is not an automatic continuation from Skill 2.

After a successful fallback:

```text
verify exact result / remote commit / diff
→ preserve ChatGPT-created work as current repository truth
→ Cline must not redo/overwrite/revert it
→ Cline resumes from new verified state
```

If Cline local state needs synchronization, ChatGPT prepares the exact safe Cline action and the Human Owner only approves/rejects it.

## 7. Skill 11 owner requirements / feasibility rule

When the Human Owner wants a skill/rule change but the exact requirement or location is unclear:

```text
Skill 11
→ ask only needed questions in simple Tagalog
→ never ask owner to write code, edit files, write YAML/JSON, or run Git/terminal commands
→ preserve answers already given
→ verify live repository constraints
→ perform bounded current web fact-check before final feasibility conclusion
→ prefer official/primary sources
→ classify POSSIBLE / POSSIBLE_WITH_CONSTRAINTS / NOT_POSSIBLE_AS_REQUESTED
→ when not possible, explain factual reason and recommend smallest practical remedy/alternative
→ recommend correct repository destination
→ prepare repository-ready specification in English
→ Human Owner approves/rejects
→ separate Skill 9 cycle writes it
```

If the exact supervisory requirement is already complete, do not force Skill 11 questions; route to Skill 9.

## 8. Zero-coding-owner rule

The Human Owner is final authority, not a manual implementation fallback.

```yaml
prohibited:
  - ask_owner_to_write_or_patch_code
  - ask_owner_to_edit_repository_files_manually
  - ask_owner_to_type_terminal_or_Git_commands_when_an_available_authorized_actor_can_do_it
  - ask_owner_to_resolve_technical_merge_or_patch_details
```

Required behavior:

```text
if ChatGPT, Cline, or another currently authorized tool can do the job
→ explain bounded action in plain language
→ ask owner authorization
→ capable actor performs it

if no capable actor exists
→ verify blocker
→ research remedy/alternative
→ recommend feasible next option
→ ask owner only for decision/authorization
```

## 9. Narrow ChatGPT direct-write scopes

Skill 9:

```yaml
- edit_or_update_ChatGPT_skill
- add_or_update_ChatGPT_skill
- add_or_update_ChatGPT_router
- update_Context_Engineer_support_contract
- update_ChatGPT_Cline_supervisory_rule_or_role_separator
- update_canonical_new_chat_supervisory_operating_instruction
```

Skill 5:

```yaml
- update_length_problem
- update_achievement
- qualifying_terminal_PASS_achievement_persistence
```

These are not generic all-documentation authority.

## 10. Minimum new-chat reading order

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
10. CODE_RED.md when required
11. active CrewAI blueprint/focus lock when technical
12. current technical contract/assignment when technical
13. latest valid continuity checkpoint when continuation state is needed
14. achievement record only when needed
15. exact branch/HEAD/PR/test/evidence needed by original request
16. exact Skill 12 fallback receipt/baseline when current continuation depends on it
17. stop reading when bootstrap can be safely decided
```

Do not read every checkpoint, skill, plan, source file, or the full repository by default.

## 11. Continuity source

```yaml
continuity_branch: docs/new-chat-continuity-2026-07-27
continuity_PR: 10
latest_checkpoint_rule: latest_valid_numbered_Length_Problem_checkpoint
```

Use only the latest valid checkpoint plus directly required referenced evidence.

## 12. Required goal/state recovery

```yaml
GALAX_GOAL_CONTINUITY_V3:
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
  current_executor:
  current_Skill_12_fallback_baseline_if_any:
  goal_changed_by_new_chat: false
```

Unknown material identities must be resolved or block.

## 13. Anti-repeat and setup reuse

```yaml
GALAX_SETUP_REUSE_GATE_V3:
  verified_completed_setup: []
  verified_completed_environment_steps: []
  verified_completed_assignments: []
  completed_and_LOCKED_ACCEPTED: []
  completed_ChatGPT_fallback_actions_not_to_repeat: []
  rejected_or_superseded_work: []
  commands_tests_or_actions_not_to_repeat: []
  current_missing_prerequisites: []
```

Do not repeat completed actions when no material identity changed.
Do not restore rejected work.
Do not overwrite accepted ChatGPT fallback work merely because Cline is the normal executor again.

## 14. Cline prompting method

Use live Skill 2 as authority for the normal Cline lane:

```text
one task
→ one exact objective
→ one correct mode
→ exact allowlists
→ exact prohibitions
→ one stop condition
→ exact receipt
```

Before any real normal Cline task:

```text
Skill 2 primary
→ Skill 10 dependency
→ prove exact active blueprint trace
→ require PASS_CLINE_BLUEPRINT_ONLY
→ emit GALAX_CLINE_TASK_V2
```

## 15. Consequential-action separation

Normal lane:

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

Skill 12 also defaults to separate stages, but the Human Owner may explicitly combine multiple fully bounded fallback stages in one authorization.

## 16. Permission and rejection behavior

A Cline action is approved only when it is required by the current objective, current Skill 10 PASS applies, exact path/command is allowlisted, mode matches, action is not already completed, stop condition is respected, locked work is protected, and supervisory/continuity scope is not crossed.

When rejecting, preserve correct work and give exact correction when knowable. A rejection does not silently authorize its replacement.

## 17. UI/button detection

Never invent a visible action button.

```yaml
NO_BUTTON_LABEL: visible_button_labeled_No_exists
NO_ACTION_BUTTON_VISIBLE: no_relevant_action_button_is_visible
UNKNOWN_UI_STATE: current_UI_cannot_be_verified
```

Reliable UI evidence comes from Human Owner screenshot/exact UI text or current tool output exposing the action label.

## 18. Evidence and Git truth

Local save is not remote publication.
Local commit is not push.
A connected GitHub direct write may create a remote commit without a separate local push; report the actual mechanism truthfully.
Remote publication is not final acceptance.

## 19. LOCKED_ACCEPTED

Do not rewrite/delete/rename/restore over/refactor/rerun locked work without exact lock-change authority.
Skill 9, Skill 12, and Cline do not bypass `LOCKED_ACCEPTED`.

## 20. Bootstrap readiness checklist

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
  completed_and_LOCKED_ACCEPTED_identified: true | false
  rejected_or_superseded_preserved: true | false
  actions_not_to_repeat_identified: true | false

  normal_ChatGPT_Cline_chain_understood: true | false
  normal_ChatGPT_CrewAI_write_block_understood: true | false
  Cline_supervisory_write_block_understood: true | false
  Skill_9_scope_understood: true | false
  Skill_5_scope_understood: true | false
  Skill_10_required_before_normal_Cline_task: true | false
  Skill_11_Tagalog_requirements_and_fact_check_understood: true | false
  Skill_12_fallback_gate_understood: true | false
  Cline_resume_after_ChatGPT_fallback_understood: true | false
  zero_coding_owner_rule_understood: true | false

  automatic_next_technical_stage_prohibited: true | false
  technical_plan_not_changed: true | false
  ready: true | false
```

If any mandatory field is false or materially conflicting, do not return PASS.

## 21. Bootstrap receipt

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
    rejected_or_superseded: []
    actions_not_to_repeat: []
    ChatGPT_fallback_completed_work_to_preserve: []

  executor_rules:
    normal_Cline_first_lane_understood: true | false
    Skill_12_exception_understood: true | false
    zero_coding_owner_rule_understood: true | false

  blockers: []
  assumptions: []
  safe_to_continue: true | false
```

## 22. Final new-chat contract

```text
NEW CHAT
→ Router first
→ Skill 8 + Skill 1 + Skill 2 + Context Engineer
→ this manual
→ exact minimum live evidence
→ preserve normal Cline-first architecture
→ preserve Skill 11 requirements/fact-check behavior
→ preserve Skill 12 owner-authorized fallback behavior
→ preserve ChatGPT-created fallback work as current repository truth
→ never ask Human Owner to code manually when an authorized AI/tool can do the job
→ bootstrap PASS only when safe
→ start separate routing cycle for original Human Owner request
→ never auto-continue to an invented next technical stage
```
