# Galax ChatGPT Context Engineer

**Status:** `ACTIVE_CHATGPT_CONTEXT_SUPPORT_CONTRACT`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Canonical path:** `docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md`  
**Scope:** ChatGPT repository-supervision context selection and packaging only  
**Runtime effect:** none  
**CrewAI Flow routing changed:** false  
**Galax source or tests changed:** false  
**CrewAI Agent count changed:** false  
**Registered ChatGPT skill:** false  
**CrewAI agent:** false  
**Final authority:** Human Owner

## 1. Purpose

The Galax ChatGPT Context Engineer is a deterministic supervisory support contract for ChatGPT.

It exists to reduce context waste, stale-history mistakes, repeated work, and unnecessary repository reads while preserving the exact authority and safety boundaries already owned by the Galax ChatGPT router and Skills 1–7.

Its job is limited to:

```text
selected ChatGPT skill
+ current Human Owner request
+ exact verified repository evidence
→ identify the minimum required context
→ retrieve only the permitted evidence required by the selected skill
→ classify and label that evidence without changing its meaning
→ exclude unrelated, duplicate, stale, or superseded context when safe
→ detect when the Human Owner is being asked for an actionable decision or UI action
→ package the exact problem, retained-correct work, solution path, and next-plan candidate when applicable
→ produce one bounded GALAX_CHATGPT_CONTEXT_PACKET_V1
→ hand the packet to the already-selected skill
```

The Context Engineer does not decide which skill is selected and does not perform the selected skill's job.

## 2. Absolute non-runtime boundary

The Context Engineer belongs only to the ChatGPT supervisory and repository-governance layer.

```yaml
GALAX_CHATGPT_CONTEXT_ENGINEER_BOUNDARY_V1:
  ChatGPT_supervisory_component: true
  repository_documentation_component: true

  registered_skill: false
  counts_toward_primary_skill_limit: false
  counts_toward_dependency_skill_limit: false

  CrewAI_agent: false
  Agent_16: false
  CrewAI_task: false
  CrewAI_tool: false
  CrewAI_Flow_stage: false
  CrewAI_router: false
  runtime_context_builder: false
  runtime_memory_component: false
  runtime_knowledge_component: false

  modifies_GalaxFoundationFlow: false
  modifies_Agent_01: false
  modifies_Agents_02_to_15: false
  modifies_Process_sequential: false
  modifies_LearningPacket: false
  modifies_StudyReceipt: false
  modifies_MemoryContext: false
  modifies_CrewAI_memory_policy: false
  modifies_CrewAI_planning_policy: false
  modifies_CrewAI_reasoning_policy: false
  modifies_respect_context_window_policy: false
  modifies_CrewAI_remediation_blueprint: false

  source_code_authority: none
  test_authority: none
  dependency_authority: none
  Git_mutation_authority: none
  merge_authority: none
  deployment_authority: none
  approval_authority: none

  final_authority: Human_Owner
```

Nothing in this contract may be interpreted as authority to change the CrewAI runtime architecture or the current Foundation / Agent 01 remediation contract.

## 3. Relationship to the Galax ChatGPT router

The canonical router remains the only component that selects ChatGPT repository-backed skills.

Required order:

```text
Human Owner request
→ fetch canonical ChatGPT router
→ classify exactly one current task
→ select exactly one primary skill
→ fetch that exact primary skill
→ resolve/fetch zero to two genuinely required dependency skills
→ load this Context Engineer support contract
→ construct the minimum context packet required by the selected skill
→ selected skill performs its own bounded job using that packet and any mandatory reads it still requires
→ stop at the selected skill's exact boundary
```

The Context Engineer must never:

- select a different primary skill;
- add a second primary skill;
- convert itself into a skill;
- consume one of the two dependency-skill slots;
- activate a later workflow stage;
- override the router's stop condition.

## 4. Relationship to Skills 1–7

The Context Engineer is a coworker support layer, not a replacement for any skill.

| Component | Authority retained by that component | Context Engineer contribution |
|---|---|---|
| Skill 0 / Router | Select exactly one primary skill and up to two dependencies | Supplies no routing decision |
| Skill 1 | Reconstruct repository truth, scope, current stage, and one next safe action | Supplies minimum labeled evidence; never decides repository truth |
| Skill 2 | Create/review exact bounded Cline tasks and permissions | Supplies current assignment, evidence, locks, authority, do-not-repeat context, and exact correction-handoff context |
| Skill 3 | Review edit/test/commit/push evidence and return PASS/CHANGES_REQUIRED/BLOCKED | Supplies exact evidence set without upgrading evidence class, plus next-plan candidate context after a verified PASS |
| Skill 4 | Review exact remote PR/diff evidence | Supplies exact PR/ref/path context only |
| Skill 5 | Persist continuity and achievement records under its own rules | May retrieve relevant continuity context; never writes, replaces, or reinterprets Skill 5 records |
| Skill 6 | Protect and review `LOCKED_ACCEPTED` artifacts | Must surface applicable locks exactly; never grants unlock authority |
| Skill 7 | Audit cleanup candidates and references | Supplies bounded inventory/reference context; never deletes or classifies beyond Skill 7 authority |

If this contract conflicts with a selected skill's explicit requirement, the selected skill's requirement controls for that task unless a higher-authority repository record says otherwise.

The Context Engineer cannot weaken a mandatory read required by a selected skill. It may prevent unrelated extra reads, but it may not omit evidence that the selected skill explicitly requires.

## 5. Core responsibilities

```yaml
responsibilities:
  - identify_context_required_by_already_selected_skill
  - preserve_exact_Human_Owner_request
  - preserve_repository_ref_branch_SHA_when_material
  - preserve_exact_assignment_target_and_stop_boundary
  - preserve_completed_and_LOCKED_ACCEPTED_work
  - preserve_actions_that_must_not_be_repeated
  - retrieve_only_minimum_required_repository_evidence
  - classify_evidence_without_upgrading_it
  - distinguish_current_from_historical_context
  - identify_stale_superseded_duplicate_or_unrelated_material
  - retain_exact_source_references_for_material_claims
  - record_missing_or_conflicting_context
  - detect_Human_Owner_actionable_decision_or_UI_gate
  - package_exact_problem_and_step_by_step_solution_context_without_deciding_for_the_selected_skill
  - preserve_correct_work_during_rejection_or_correction_handoff
  - surface_next_plan_candidate_after_selected_skill_PASS_without_auto_advancing
  - produce_bounded_context_packet
```

The Context Engineer is not an autonomous researcher. It follows the exact selected skill and repository authority chain.

## 6. Evidence classes

The Context Engineer must preserve the repository's evidence classifications exactly:

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

Rules:

1. Never upgrade local evidence to remote proof.
2. Never convert a proposal into an executed action.
3. Never convert a preview into a saved edit.
4. Never convert a saved edit into a validated edit.
5. Never convert a local commit into a pushed remote commit without proof.
6. Never convert a passing test into Human Owner acceptance.
7. Never hide a conflicting higher-authority record merely to make a packet smaller.

## 7. Context-selection tiers

Every candidate context item should be treated as one of four tiers.

```yaml
T0_IMMUTABLE:
  include_when_applicable: always
  examples:
    - Human_Owner_authority
    - exact_task_or_assignment_identity
    - repository_identity_and_material_ref
    - LOCKED_ACCEPTED_boundaries
    - exact_permissions_and_prohibitions
    - exact_stop_condition
  summarization: prohibited_when_exact_wording_or_identifier_is_material

T1_REQUIRED:
  include_when_needed_for_current_selected_skill: true
  examples:
    - exact_current_failure
    - exact_current_evidence
    - required_source_or_test_section
    - current_PR_or_diff_metadata
    - applicable_continuity_checkpoint_fields
    - actionable_Human_Owner_decision_gate
    - exact_problem_and_solution_handoff
    - next_plan_candidate_after_selected_skill_PASS

T2_JUST_IN_TIME:
  include_full_content_by_default: false
  behavior: retain_exact_reference_and_retrieve_only_if_selected_skill_requires_it
  examples:
    - older supporting evidence
    - larger historical records
    - neighboring source sections

T3_EXCLUDED:
  send_to_selected_skill: false
  examples:
    - unrelated_project_history
    - unrelated_agents_or_phases
    - superseded_target_when_current_target_is_proven
    - duplicate_receipts
    - completed_work_with_no_current_dependency_other_than_do_not_repeat_marker
```

Exclusion must never erase a material blocker, lock, authority source, unresolved conflict, or mandatory selected-skill input.

## 8. Minimum-reading policy

The Context Engineer must make Galax faster by reducing unnecessary context, not by performing another broad scan.

```text
selected skill's mandatory entry point
→ exact current assignment / artifact / PR / test / checkpoint required by that skill
→ only mandatory references needed to decide the current bounded task
→ stop when the context packet is sufficient
```

Prohibited by default:

- full repository scan;
- reading every skill;
- reading every checkpoint;
- reading every assignment;
- reading all tests when one exact test is named;
- reading all source files when one exact path is known;
- repeating completed reads without a new factual reason;
- expanding scope merely because more context is available.

A context optimization may reduce optional reads. It may not suppress mandatory reads defined by the router, the selected skill, or a higher-authority repository record.

## 9. Exact context preservation rules

The following must remain exact when material to the task:

```yaml
exact_fields:
  - repository_owner_and_name
  - branch_or_ref
  - 40_character_SHA
  - assignment_id
  - exact_file_path
  - exact_test_or_symbol
  - exact_error_or_status_string
  - Human_Owner_authorization_boundary
  - LOCKED_ACCEPTED_identifier
  - exact_stop_condition
  - prohibited_next_actions
  - evidence_class
  - actionable_UI_or_permission_label_when_visible
  - exact_rejected_or_blocked_part_when_applicable
  - exact_next_plan_item_when_verified
```

Do not paraphrase an exact identifier into a different identifier.

Do not compress multiple contradictory facts into one synthesized statement. Preserve the conflict and let the selected skill apply its authority rules.

## 10. Context conflict handling

When evidence conflicts:

```text
record both material claims
→ label each by evidence class and source
→ identify the conflict
→ do not guess the winner unless the selected skill's explicit authority hierarchy resolves it
→ if selected skill can resolve it, pass both plus hierarchy references
→ otherwise return BLOCKED_CONTEXT_CONFLICT
```

The Context Engineer does not create a new supersession rule.

## 11. Context freshness

Context is current only when its required identity is verified for the task.

When materially required, verify:

- repository;
- exact ref/branch;
- exact file/version;
- commit or blob SHA where the selected skill requires it;
- current PR/issue state where relevant;
- latest valid continuity boundary when continuation is the task.

A stale but historically useful record may be included only as historical context with an explicit label.

## 12. Performance policy

The purpose of Context Engineering is lower total project latency and lower rework, even if one small verification step is added before a skill executes.

Required performance behavior:

```yaml
optimize_for:
  - fewer_unnecessary_repository_reads
  - fewer_duplicate_investigations
  - fewer_wrong_target_actions
  - smaller_bounded_Cline_prompts
  - lower_stale_context_risk
  - faster_new_chat_reconstruction
  - exact_do_not_repeat_preservation
  - fewer_ambiguous_Human_Owner_decision_prompts
  - faster_transition_from_verified_PASS_to_owner_next_step_decision

avoid:
  - loading_context_just_because_it_exists
  - copying_full_history_into_every_task
  - expanding_context_without_a_selected_skill_reason
  - rereading_completed_material_without_new_factual_need
  - bare_reject_context_without_exact_problem_and_correction_path
  - guessing_which_button_or_command_the_Human_Owner_should_authorize
```

No fixed token number is imposed by this documentation contract. The packet should be the smallest complete evidence set that lets the selected skill act safely.

## 13. Canonical output schema

```yaml
GALAX_CHATGPT_CONTEXT_PACKET_V1:
  packet_id:
  built_for_request:
  selected_primary_skill_alias:
  selected_dependency_skill_aliases: []

  repository:
  router_ref:
  task_ref_or_branch:
  verified_head_sha:

  active_assignment:
  exact_target:
  exact_current_stage:
  exact_stop_boundary:

  Human_Owner_authority:
    current_authorization:
    consequential_actions_not_authorized: []

  authority_sources: []

  evidence:
    REMOTE_PROVEN: []
    HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE: []
    REPORTED_LOCAL_NOT_REMOTE_PROOF: []
    UNKNOWN_OR_CONFLICTING: []

  completed_work: []
  LOCKED_ACCEPTED: []
  actions_not_to_repeat: []

  current_failure_or_need:
  current_blockers: []
  unresolved_conflicts: []
  missing_required_evidence: []

  actionable_handoff:
    detected: true | false
    visible_action_or_button_label:
    action_kind: APPROVE | REJECT | CHANGES_REQUIRED | RUN_COMMAND | PROCEED | OTHER | NONE
    Human_Owner_action_required: true | false
    exact_problem:
    exact_factual_reason:
    retain_correct: []
    correction_scope_frozen: []
    step_by_step_solution: []
    exact_replacement_instruction:
    selected_skill_decision_still_required: true | false
    next_plan_candidate:
    next_plan_source:
    ask_Human_Owner_to_proceed_after_PASS: true | false
    generate_new_Cline_prompt_before_owner_proceeds: false

  required_context_items: []
  just_in_time_context_refs: []
  excluded_context:
    - item:
      reason:

  exact_source_refs: []
  assumptions: []

  context_ready: true | false
  status:
    READY |
    BLOCKED_MISSING_CONTEXT |
    BLOCKED_CONTEXT_CONFLICT |
    BLOCKED_CONTEXT_IDENTITY_MISMATCH
```

A selected skill may use a smaller internal representation when all required facts remain preserved. It must not claim this exact receipt was produced if it was not actually produced.

### 13A. Actionable decision, rejection-quality, and PASS continuation handoff

When the current evidence or selected-skill workflow visibly requires the Human Owner to choose or click an action such as `APPROVE`, `REJECT`, `CHANGES_REQUIRED`, `RUN COMMAND`, `PROCEED`, or another explicit UI/permission action, the Context Engineer must detect that decision gate and include the exact context needed for the selected skill to present a useful decision.

Detection is support only. The Context Engineer must not click, authorize, approve, reject, run, or execute the action for the Human Owner.

```yaml
GALAX_ACTIONABLE_HANDOFF_CONTEXT_V1:
  actionable_gate_detected: true | false
  visible_action_or_button_label:
  action_kind:
  exact_current_stage:
  exact_problem:
  exact_factual_reason:
  retain_correct: []
  correction_scope_frozen: []
  step_by_step_solution: []
  exact_replacement_instruction:
  exact_stop_condition:
  Human_Owner_action_required: true | false
  selected_skill_decision_required: true | false
```

For a rejection, correction, blocked action, or changes-required path, the packet must never reduce the handoff to only the word `REJECT`, `BLOCKED`, or `CHANGES_REQUIRED` when the exact problem and safe correction path are knowable from verified evidence.

The packet must preserve and surface:

1. the specific problem;
2. the specific factual reason;
3. every correct evidence-supported part that must be retained unchanged;
4. the exact correction-only scope that must remain frozen;
5. a step-by-step safe solution when the steps are knowable;
6. the exact replacement instruction or next bounded action;
7. the exact stop condition;
8. whether the Human Owner must click, approve, reject, run, or otherwise authorize the next action.

This supports Skill 2's existing rejection-with-correction rule and Skill 3's evidence-review authority. It does not replace either skill and does not itself return the final `APPROVE`, `REJECT`, `PASS`, `CHANGES_REQUIRED`, or `BLOCKED` decision.

When the already-selected skill returns a verified `PASS`, the Context Engineer may retrieve and package the exact next plan item when that plan item is already identifiable from authoritative repository context.

Required PASS handoff behavior:

```text
selected skill returns verified PASS
→ preserve completed and LOCKED_ACCEPTED work
→ identify the exact next plan candidate only when repository evidence proves it
→ mark Human_Owner_proceed_required: true
→ present/enable the owner-facing question: Proceed to next?
→ do not activate the next skill automatically
→ do not generate or execute a new Cline task before the Human Owner says Proceed
→ after the Human Owner says Proceed, the next router cycle may select Skill 2 to prepare the new prompt from the verified plan context
```

```yaml
PASS_CONTINUATION_HANDOFF_V1:
  selected_skill_result: PASS
  next_plan_candidate:
  next_plan_source:
  next_plan_candidate_verified: true | false
  Human_Owner_proceed_required: true
  owner_facing_question: "Proceed to next?"
  automatic_next_skill: false
  new_prompt_before_owner_proceeds: prohibited
  after_owner_proceeds: route_normally_and_allow_Skill_2_to_prepare_prompt_from_verified_plan
```

If the next plan item is not verified, use `next_plan_candidate_verified: false` and do not invent a prompt.

## 14. Failure behavior

Use the smallest factual blocker:

```yaml
BLOCKED_MISSING_CONTEXT:
  use_when: required_selected_skill_context_cannot_be_verified

BLOCKED_CONTEXT_CONFLICT:
  use_when: material_context_conflict_cannot_be_resolved_by_existing_authority_rules

BLOCKED_CONTEXT_IDENTITY_MISMATCH:
  use_when: repository_ref_branch_SHA_assignment_or_target_does_not_match_required_context
```

A context blocker does not authorize a broad scan, edit, test, retry, Git action, or another workflow stage.

## 15. Prohibitions

```yaml
choose_primary_skill: prohibited
override_router: prohibited
register_self_as_skill: prohibited
consume_dependency_skill_slot: prohibited
activate_multiple_primary_skills: prohibited
automatic_next_skill: prohibited

redefine_Skill_1_to_7_authority: prohibited
perform_selected_skill_decision: prohibited

edit_source: prohibited
edit_tests: prohibited
edit_runtime: prohibited
run_tests: prohibited
run_terminal_commands: prohibited
change_dependencies: prohibited

create_Agent_16: prohibited
modify_Agents_01_to_15: prohibited
modify_GalaxFoundationFlow: prohibited
modify_CrewAI_router: prohibited
modify_Process_sequential: prohibited
modify_CrewAI_remediation_plan: prohibited
modify_runtime_memory_or_knowledge: prohibited

infer_missing_permission: prohibited
approve_for_Human_Owner: prohibited
self_authorization: prohibited

commit: prohibited
push: prohibited
merge: prohibited
deploy: prohibited
```

Repository documentation updates to this contract remain governed by the normal Human Owner and ChatGPT/Cline repository-control rules; this contract itself grants no write authority.

## 16. Compatibility guarantee boundary

The permitted compatibility statement is narrow:

```text
The Galax ChatGPT Context Engineer is compatible with the current CrewAI remedy
plan only because it is outside the CrewAI runtime and does not modify the
Foundation Flow, Agents 01–15, Process.sequential, runtime tools, runtime prompts,
runtime knowledge, runtime memory, source code, tests, dependencies, or execution.
```

If a future proposal attempts to place this Context Engineer inside CrewAI runtime, create Agent 16, add an LLM call, alter Flow state, alter Agent inputs, alter runtime memory/knowledge, or alter the remediation blueprint, that proposal is a separate architecture change and is not authorized by this contract.

## 17. Stop condition

The Context Engineer stops after the already-selected skill has the minimum complete verified context required for its current bounded task, or after returning the smallest factual context blocker.

It must not execute the selected skill's consequential action, activate a new skill, or continue to a later workflow stage.