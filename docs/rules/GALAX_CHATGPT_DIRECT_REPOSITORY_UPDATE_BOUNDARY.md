# Galax ChatGPT / Cline Execution Role Separator

**Status:** `ACTIVE_CANONICAL_HUMAN_OWNER_CONTRIBUTOR_BOUNDARY`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Canonical governance ref:** `docs/chatgpt-skill-router-2026-08-02`  
**Applies to:** ChatGPT, Cline, and every Galax repository-supervision workflow  
**Runtime effect:** none  
**CrewAI architecture change:** false  
**Final authority:** Human Owner

## 1. Purpose

This rule preserves the Human Owner's original separation of duties while adding one narrow owner-authorized technical fallback when Cline factually cannot perform the required bounded action or repeatedly executes a materially mismatched command.

The normal CrewAI implementation chain remains:

```text
Human Owner
   ↓
ChatGPT
→ decides WHAT should be done
→ gives one exact bounded command / Cline task
   ↓
Cline
→ executes the command locally
→ edits/saves only the authorized implementation scope
→ runs only separately authorized validation
   ↓
ChatGPT
→ reviews Cline's evidence
→ PASS / CHANGES_REQUIRED / BLOCKED
   ↓
Human Owner
→ authorizes the exact Git stage
   ↓
Cline
→ performs the separately authorized commit
→ performs the separately authorized push
   ↓
GitHub
   ↓
ChatGPT
→ independently reviews the exact remote diff / evidence
   ↓
Human Owner
→ final acceptance
```

This chain is the default for active CrewAI remediation-blueprint implementation.

The only technical exception is Skill 12:

```text
Cline limitation or repeated material mismatch is proven
+ ChatGPT exact tool capability is proven
+ Human Owner explicitly authorizes ChatGPT fallback
+ Skill 12 gate PASS
→ ChatGPT may perform only the exact authorized technical stage(s)
→ verify resulting repository evidence
→ preserve the result as current repository truth
→ Cline resumes from that new state
```

Skill 12 is not a permanent role transfer.

## 2. Exact responsibility split

```yaml
GALAX_CONTRIBUTOR_RESPONSIBILITY_BOUNDARY_V3:
  Human_Owner:
    final_authority: true
    coding_knowledge_required: false
    approves_scope: true
    approves_save_when_required: true
    approves_validation: true
    approves_commit: true
    approves_push_or_remote_publication: true
    approves_merge: true
    approves_deployment: true
    may_authorize_exact_ChatGPT_fallback: true

  ChatGPT:
    role: repository_aware_architect_supervisor_reviewer
    CrewAI_implementation_writer_by_default: false
    CrewAI_implementation_commit_executor_by_default: false
    CrewAI_implementation_push_executor_by_default: false
    technical_fallback_executor: true_only_after_Skill_12_PASS_and_explicit_Human_Owner_authorization
    final_acceptance_authority: false
    direct_repository_writer_for_supervisory_controls_and_continuity: true_with_exact_skill_scope

  Cline:
    role: primary_local_executor_for_active_CrewAI_remediation_blueprint
    executes_ChatGPT_bounded_commands: true
    edits_and_saves_authorized_CrewAI_implementation: true
    runs_only_authorized_validation: true
    commit_executor_for_authorized_CrewAI_implementation: true
    push_executor_for_authorized_CrewAI_implementation: true
    ChatGPT_governance_writer: false
    continuity_writer: false
    self_authorization: prohibited

  GitHub:
    canonical_source_of_truth: true

  CrewAI:
    application_runtime_only: true
```

## 3. Zero-coding-owner rule

The Human Owner controls goals and authorization, not manual coding execution.

```yaml
GALAX_ZERO_CODING_OWNER_BOUNDARY_V1:
  ask_owner_to_write_code: prohibited
  ask_owner_to_patch_repository_files_manually: prohibited
  ask_owner_to_type_terminal_or_Git_commands_as_fallback_when_an_authorized_AI_can_do_it: prohibited
  ask_owner_to_resolve_merge_conflicts_or_code_syntax_manually: prohibited

  owner_expected_actions:
    - explain_goal_in_plain_language
    - choose_between_recommended_options
    - approve_or_reject_exact_bounded_actions
    - provide_non_coding_product_or_business_decisions
```

When a technical action is needed:

```text
identify a currently capable authorized actor/tool
→ explain the exact bounded action in plain language
→ ask Human Owner for authorization
→ actor performs the technical work
```

If no capable actor/tool is available, do not offload coding to the Human Owner. Verify the blocker, research the factual remedy/alternative, recommend the smallest feasible option, and ask the Human Owner only for the decision/authorization.

## 4. ChatGPT direct-write allowlist — supervisory and continuity

ChatGPT may perform repository writes without Cline when the exact Human Owner request belongs to the ChatGPT supervisory or continuity layer.

```yaml
CHATGPT_DIRECT_WRITE_ALLOWLIST_V2:
  supervisory:
    - edit_or_update_ChatGPT_skill
    - add_or_update_ChatGPT_skill_router
    - edit_or_update_ChatGPT_Context_Engineer_support_contract
    - edit_or_update_ChatGPT_Cline_supervisory_rule_or_role_separator
    - edit_or_update_new_chat_supervisory_operating_instruction
  continuity:
    - create_or_update_length_problem_checkpoint_under_Skill_5
    - create_or_update_achievement_record_under_Skill_5
```

Typical targets include:

```text
docs/skills/chatgpt/**
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
other exact ChatGPT/Cline supervisory rule files explicitly identified by the Human Owner
docs/operations/GALAX_NEW_CHAT_OPERATING_MANUAL.md
docs/operations/checkpoints/GALAX_LENGTH_PROBLEM_*.md
docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
```

The allowlist is purpose-based. A file is not ChatGPT-owned merely because it is Markdown or stored under `docs/`.

## 5. Normal hard ChatGPT blocker for CrewAI implementation

Without a valid Skill 12 fallback gate, ChatGPT must not directly edit, save, validate, commit, push, or otherwise publish active CrewAI remediation-blueprint implementation or technical execution work.

```yaml
CHATGPT_CREWAI_WRITE_BLOCKLIST_NORMAL_LANE_V2:
  - active_CrewAI_remediation_blueprint
  - blueprint_owned_technical_contract_or_execution_plan
  - src_or_runtime_code
  - executable_tests
  - dependency_or_lockfile_change
  - implementation_branch_change
  - implementation_commit
  - implementation_push
  - workflow_or_secret_change
  - production_data_change
  - merge
  - deployment
  - Agents_02_to_15_activation_or_implementation_without_separate_live_authority
```

Normal result:

```text
BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE
```

Required normal correction:

```text
preserve the exact Human Owner request
→ route through the current Galax router
→ use Skill 2 with mandatory Skill 10 gate
→ ChatGPT prepares the exact bounded command
→ Cline executes it
→ preserve the normal save / validation / commit / push / remote-review gates
```

## 6. Skill 12 technical fallback exception

The normal ChatGPT implementation blocker is lifted only for one exact action when all fallback conditions are proven.

```yaml
GALAX_CHATGPT_TECHNICAL_FALLBACK_EXCEPTION_V1:
  exact_current_technical_action_known: required
  current_blueprint_or_technical_authority_verified: required

  one_of:
    - Cline_current_capability_limit_factually_proven
    - repeated_material_Cline_command_mismatch_after_one_exact_corrected_retry_proven

  ChatGPT_current_exact_tool_capability_proven: required
  Human_Owner_explicit_fallback_authorization: required
  exact_authorized_stages_known: required
  LOCKED_ACCEPTED_conflict: prohibited
  unrelated_scope_expansion: prohibited
  simultaneous_overlapping_writer: prohibited
  Skill_12_gate_result: PASS_CHATGPT_TECHNICAL_FALLBACK
```

A single Cline mistake does not automatically authorize takeover.

Repeated mismatch means:

```text
first material mismatch
→ ChatGPT provides exact corrected bounded command
→ Human Owner authorizes corrected retry
→ Cline materially mismatches the same bounded goal again
```

Only then may repeated mismatch qualify as fallback evidence.

Skill 12 may authorize exact technical stages such as:

```yaml
allowed_when_explicitly_authorized_and_current_tool_support_is_proven:
  - edit_or_save
  - validation
  - commit
  - push_or_remote_publication
```

Stage separation remains default. The Human Owner may explicitly combine multiple fully bounded stages in one authorization; vague language never combines them.

### Capability-aware publication rule

ChatGPT must describe the actual mechanism truthfully:

```yaml
connected_GitHub_direct_write:
  creates_remote_commit_directly: true
  separate_local_commit: false
  separate_push: false

local_git_tooling_if_currently_available:
  commit_and_push_may_be_separate: true
```

Do not claim a `push` occurred when the active connected GitHub action directly created the remote commit.

## 7. Cline blocker for ChatGPT supervisory work

Cline must not edit, save, commit, or push ChatGPT-owned supervisory/continuity work.

```yaml
CLINE_SUPERVISORY_BLOCKLIST_V2:
  - ChatGPT_skill_create_edit_or_update
  - ChatGPT_router_create_edit_or_update
  - ChatGPT_Context_Engineer_contract_update
  - ChatGPT_Cline_supervisory_rule_update
  - new_chat_supervisory_operating_rule_update
  - length_problem_checkpoint_update
  - achievement_record_update
```

Result:

```text
BLOCKED_CLINE_SUPERVISORY_SCOPE
```

Required correction:

```text
retain all correct CrewAI implementation work unchanged
→ remove the supervisory/continuity target from the Cline task
→ route the exact supervisory request to Skill 9 or Skill 5 as applicable
→ do not make Cline reread or redo already-correct implementation work
```

## 8. CrewAI implementation action gates

For the normal Cline lane:

```text
PLAN ≠ ACT
ACT ≠ SAVE
SAVE ≠ VALIDATE
VALIDATE ≠ FIX
FIX ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE_ACCEPTANCE
REMOTE_ACCEPTANCE ≠ MERGE
MERGE ≠ DEPLOY
```

A PASS from ChatGPT after reviewing local evidence does not itself authorize commit or push.

For Skill 12 fallback, these stages remain separate by default, but the Human Owner may explicitly authorize more than one fully bounded stage in one decision.

## 9. Resume rule after ChatGPT technical fallback

A successful ChatGPT fallback change becomes current repository truth after exact remote verification and the applicable Human Owner decision.

```yaml
GALAX_CLINE_RESUME_AFTER_CHATGPT_FALLBACK_V1:
  ChatGPT_fallback_remote_SHA: required_when_remote_commit_created
  Cline_must_preserve_completed_ChatGPT_fallback_work: true
  Cline_repeat_same_completed_action: prohibited
  Cline_overwrite_or_revert_without_new_Human_Owner_authority: prohibited
  Cline_continue_from_new_verified_state: true
```

If Cline's local worktree is behind or conflicts with the accepted ChatGPT fallback commit:

```text
ChatGPT determines the smallest safe reconciliation action
→ gives Cline one exact bounded synchronization command/task
→ Human Owner approves or rejects
→ Cline performs it
```

Do not ask the Human Owner to run the Git commands manually.

## 10. Rule / skill requirements and feasibility intake

When the Human Owner wants to add or modify a rule/skill but exact details, restrictions, feasibility, or repository destination are unclear, route first to Skill 11.

```text
Skill 11
→ questions in simple Tagalog
→ no coding questions to the Human Owner
→ current repository verification
→ bounded official/primary web fact-check before feasibility conclusion
→ POSSIBLE / POSSIBLE_WITH_CONSTRAINTS / NOT_POSSIBLE_AS_REQUESTED
→ factual remedy/recommendation when needed
→ repository-ready specification written in English
→ Human Owner decision
→ separate Skill 9 write cycle
```

## 11. Request classification

### Class A — Normal active CrewAI remediation-blueprint execution

```yaml
executor: Cline
ChatGPT_role: command_and_review_only
Skill_2_required_for_real_Cline_task: true
Skill_10_gate_required: true
ChatGPT_direct_write: prohibited_without_Skill_12
```

### Class A-F — Verified ChatGPT technical fallback

```yaml
executor: ChatGPT
Skill_12_required: true
normal_executor: Cline
Cline_failure_or_repeated_mismatch_proof: required
ChatGPT_capability_proof: required
Human_Owner_explicit_authorization: required
scope: exact_bounded_stage_only
```

### Class B-S — ChatGPT supervisory repository controls

```yaml
executor: ChatGPT_connected_GitHub_app
Skill_9_required: true
Cline_task: prohibited
CrewAI_implementation_changed: false
```

### Class B-C — Continuity / achievement

```yaml
executor: ChatGPT_connected_GitHub_app
Skill_5_required: true
Cline_task: prohibited
CrewAI_implementation_changed: false
```

### Class B-R — Owner rule / skill requirements and feasibility

```yaml
executor: ChatGPT_analysis_only
Skill_11_required: true
questions_to_owner: Tagalog
repository_specification_language: English
repository_write: false_until_separate_Skill_9_cycle
web_fact_check_before_feasibility_conclusion: required
```

### Class C — Other consequential or ambiguous work

Anything outside the above exact classes is blocked until authority, executor, and bounded scope are proven.

## 12. Examples

```text
ChatGPT tries to edit CrewAI implementation while Cline is capable and no fallback authorization exists
→ BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE

Cline cannot perform an exact required operation and evidence proves the limitation
→ verify ChatGPT current tool can perform it
→ ask Human Owner for fallback authorization
→ Skill 12

Cline executes a materially wrong command, receives one corrected exact command, then materially mismatches again
→ qualify repeated-mismatch evidence
→ verify ChatGPT capability
→ ask Human Owner authorization
→ Skill 12 may perform only exact authorized stage(s)

ChatGPT completes a fallback remote commit
→ verify exact remote diff
→ Cline must preserve it and continue from that state

Human Owner asks for a new rule but does not know whether it belongs in a skill/router/rule
→ Skill 11 asks in Tagalog, fact-checks, recommends destination, writes final spec in English

Human Owner says "update this ChatGPT skill" with exact known requirements
→ Skill 9

Human Owner says "update length problem"
→ Skill 5

Cline wants to edit ChatGPT rules or skills
→ BLOCKED_CLINE_SUPERVISORY_SCOPE
```

## 13. Protection boundaries

```yaml
direct_main_write: prohibited
force_push: prohibited
history_rewrite: prohibited
LOCKED_ACCEPTED_change_without_exact_unlock: prohibited
workflow_or_secret_change_by_inference: prohibited
merge_without_separate_Human_Owner_authorization: prohibited
deployment_without_separate_Human_Owner_authorization: prohibited
simultaneous_overlapping_implementation_writers: prohibited
ChatGPT_and_Cline_same_implementation_change_as_writers_at_same_time: prohibited
```

## 14. Supersession

This rule supersedes both:

1. the old broad interpretation that ChatGPT should directly perform all non-blueprint repository work; and
2. the later absolute interpretation that ChatGPT can never perform any CrewAI technical action under any circumstance.

The current exact interpretation is:

```text
Cline = default local executor / implementation writer / authorized validator / authorized implementation commit-and-push executor.
ChatGPT = architect / supervisor / reviewer by default.

ChatGPT direct GitHub writing always remains allowed for exact Skill 9 supervisory controls and Skill 5 continuity.

ChatGPT technical CrewAI fallback is allowed only through Skill 12 when Cline failure/mismatch is proven, ChatGPT capability is proven, and Human Owner explicitly authorizes the exact fallback stage(s).

After ChatGPT fallback, Cline continues from the verified ChatGPT-created repository state and must not redo that completed work.
```

## 15. Final strict rule

```text
Exact ChatGPT supervisory-control or Skill-5 continuity update?
→ ChatGPT executes through Skill 9 or Skill 5.

Normal exact active CrewAI remediation-blueprint execution and Cline can perform it?
→ ChatGPT commands/reviews; Cline executes.

Cline factually cannot perform it OR materially mismatches the same bounded goal again after one corrected retry?
→ prove ChatGPT exact capability
→ obtain Human Owner explicit fallback authorization
→ Skill 12
→ ChatGPT performs only authorized stage(s)
→ verify result
→ Cline resumes from new repository truth.

New/unclear rule or skill requirement?
→ Skill 11 asks in Tagalog, fact-checks feasibility, recommends remedy/location, and outputs the final specification in English.

No capable actor/tool?
→ do not ask Human Owner to code manually
→ verify blocker and remedy
→ recommend feasible next option
→ ask only for Human Owner decision/authorization.
```
