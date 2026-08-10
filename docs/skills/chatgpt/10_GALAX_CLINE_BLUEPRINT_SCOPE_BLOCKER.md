```yaml
skill_reference: $galax-cline-blueprint-scope-blocker
skill_id: GALAX-SKILL-10
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 10: Galax Cline Blueprint Scope Blocker

```yaml
skill_name: Galax Cline Blueprint Scope Blocker
skill_type: ChatGPT_Cline_predelegation_hard_scope_gate
active_project: Galax_AI_only
repository: ariessocia04-rgb/galax-Ai-project
runtime_agent: false
CrewAI_agent: false
Galax_Agent_01_to_15: false
writer: false
approval_authority: false
blocking_authority: repository_policy_gate_only
final_authority: Human_Owner
```

## 1. One job only

This skill has one narrow responsibility:

```text
before ChatGPT gives Cline any Galax task
→ read and classify the exact Human Owner request
→ prove whether the exact proposed Cline objective belongs to the active CrewAI remediation blueprint execution chain
→ PASS only that exact blueprint work to Cline
→ BLOCK every non-blueprint delegation to Cline
→ when the same Human Owner request is an authorized Class B non-blueprint repository update, automatically hand the exact same request back to the Router for Skill 9 and immediate ChatGPT connected-GitHub execution without creating a Cline prompt or asking the Human Owner to repeat the request
```

This skill does not write repository files, create implementation, review evidence, persist continuity, or replace Skill 2 or Skill 9.

It exists to enforce the Human Owner rule:

```text
Cline executes the CrewAI remediation blueprint — NO MORE, NO LESS.

If the Human Owner asks ChatGPT for a repository update and Skill 10 proves it is not CrewAI-blueprint work but is an authorized Class B update, ChatGPT performs that exact request directly through GitHub. Do not give it to Cline and do not ask the Human Owner for the same instruction again.
```

## 2. Canonical boundaries to reference, not duplicate

Use these current authorities instead of copying their full rules into this skill:

```yaml
contributor_boundary:
  path: docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md

active_CrewAI_remediation_blueprint:
  path: docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md

active_Foundation_execution_contract:
  path: docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md

Cline_prompt_control:
  path: docs/skills/chatgpt/02_GALAX_STRICT_CLINE_PROMPT_GUARDIAN.md

owner_direct_non_blueprint_updates:
  path: docs/skills/chatgpt/09_GALAX_OWNER_DIRECT_REPOSITORY_UPDATE_GUARDIAN.md
```

The execution contract or exact current technical assignment may narrow the blueprint. It may not expand Cline beyond the blueprint.

## 3. Mandatory activation

This skill is a mandatory dependency gate whenever the router selects Skill 2 as the primary skill to create, continue, correct, approve, reject, or otherwise authorize a real Cline task.

It is not an additional bootstrap dependency when Skill 2 is loaded only as a dependency of Skill 8 for new-chat readiness, because bootstrap does not itself issue a Cline task.

Before any `GALAX_CLINE_TASK_V2` is emitted, Skill 10 must return a current gate result.

The gate must classify the Human Owner's exact request before any Cline prompt is produced. A request must not be converted into a Cline prompt first and classified afterward.

## 4. Exact blueprint-trace requirement

Cline may receive a task only when the proposed objective has an evidence-backed trace:

```text
active CrewAI remediation blueprint
→ current canonical technical contract or plan that implements/narrows that blueprint
→ exact current Human-Owner-authorized technical assignment
→ exact proposed Cline objective
```

All links in that chain must be current and compatible.

The following are insufficient by themselves:

```yaml
insufficient_reasons_to_use_Cline:
  - the_file_is_in_the_repository
  - the_change_is_technical_sounding
  - Cline_can_edit_files
  - Cline_was_used_previously
  - it_would_be_convenient
  - the_owner_said_update_without_a_blueprint_trace
  - repository_governance_needs_a_change
  - ChatGPT_rules_or_skills_need_a_change
```

## 5. Hard classification gate

Before Cline is tasked, establish:

```yaml
GALAX_CLINE_BLUEPRINT_SCOPE_GATE_V1:
  Human_Owner_request:
  proposed_Cline_objective:

  active_blueprint_path: docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  active_blueprint_verified: true | false
  active_technical_contract_or_assignment:
  exact_blueprint_trace_evidence: []

  objective_is_exact_blueprint_execution: true | false
  objective_is_non_blueprint_governance_or_docs: true | false
  objective_is_continuity_or_achievement: true | false
  objective_is_ChatGPT_router_skill_or_rule_update: true | false
  objective_is_adjacent_cleanup_or_housekeeping: true | false
  objective_is_unrelated_technical_work: true | false

  current_Human_Owner_request_already_authorizes_exact_Class_B_update: true | false
  same_request_can_continue_without_reasking_owner: true | false

  ChatGPT_blueprint_file_edit_required_for_consistency: true | false
  exact_blueprint_file_or_section_if_required:
  explicit_Human_Owner_authorization_for_ChatGPT_blueprint_edit: true | false

  executor:
    Cline |
    ChatGPT_Skill_9 |
    ChatGPT_Skill_5 |
    NONE_BLOCKED

  gate_result:
    PASS_CLINE_BLUEPRINT_ONLY |
    BLOCK_CLINE_AUTO_EXECUTE_BY_CHATGPT |
    BLOCK_CLINE_ROUTE_TO_SKILL_5 |
    BLOCK_UNRELATED_TECHNICAL_SCOPE |
    BLOCK_CHATGPT_BLUEPRINT_EDIT_REQUIRES_HUMAN_AUTHORIZATION |
    BLOCK_MISSING_BLUEPRINT_TRACE

  factual_reason:
```

No `GALAX_CLINE_TASK_V2` may be created unless:

```text
gate_result == PASS_CLINE_BLUEPRINT_ONLY
```

## 6. Cline PASS rule — NO MORE, NO LESS

Return `PASS_CLINE_BLUEPRINT_ONLY` only when all are true:

```yaml
cline_pass_requirements:
  active_blueprint_verified: true
  exact_current_technical_assignment_verified: true
  proposed_objective_directly_implements_or_validates_blueprint: true
  proposed_objective_within_current_narrow_contract: true
  proposed_objective_within_Human_Owner_authorization: true
  proposed_objective_not_governance_housekeeping_or_ChatGPT_maintenance: true
  proposed_objective_does_not_expand_to_adjacent_work: true
```

Cline then executes only the exact blueprint objective through Skill 2 controls.

Cline must not receive nearby work just because it touches the same file, branch, package, feature, or repository area.

## 7. Non-blueprint hard block and automatic ChatGPT execution

When the exact Human Owner request is repository governance, ChatGPT rules, ChatGPT skills, router maintenance, supervisory documentation, owner-directed repository documentation, or another authorized Class B update outside the active blueprint:

```yaml
result: BLOCK_CLINE_AUTO_EXECUTE_BY_CHATGPT
executor: ChatGPT_Skill_9
Cline_task_created: false
Cline_prompt_created: false
preserve_exact_Human_Owner_request: true
ask_Human_Owner_to_repeat_same_request: false
additional_authorization_for_same_clear_Class_B_request: false
automatic_same_request_router_handoff: required
ChatGPT_connected_GitHub_execution_after_Skill_9_precheck: required
```

Required behavior:

```text
Skill 10 detects exact requested work is not active CrewAI blueprint execution
→ BLOCK Cline immediately
→ do not draft, display, or prepare a Cline prompt for that work
→ preserve the exact Human Owner request unchanged
→ Router immediately starts the separate same-request Skill 9 cycle required by the one-primary-skill rule
→ Skill 9 performs its normal live repository and Class B precheck
→ when Skill 9 precheck passes, ChatGPT executes the exact requested update directly through the connected GitHub app
→ verify the remote commit
→ stop at the normal Skill 9 boundary
```

This automatic handoff is not invented work and is not automatic technical continuation. It is execution of the same explicit Human Owner request by the correct repository owner after Cline has been ruled out.

Do not ask the Human Owner whether ChatGPT should do the same Class B update after Skill 10 has already classified it. The existing Human Owner request is the authority, subject to Skill 9's normal precheck and protection boundaries.

Skill 10 itself remains read-only and does not perform the GitHub write; Skill 9 owns execution.

Continuity or achievement work remains owned by Skill 5:

```yaml
result: BLOCK_CLINE_ROUTE_TO_SKILL_5
executor: ChatGPT_Skill_5
Cline_task_created: false
```

## 8. Unrelated technical work is not automatically Cline work

A technical task outside the active CrewAI remediation blueprint is not reassigned to Cline merely because Cline is the blueprint executor.

```yaml
non_blueprint_consequential_technical_scope:
  default_result: BLOCK_UNRELATED_TECHNICAL_SCOPE
  executor: NONE_BLOCKED
  required_next_step: exact_separate_Human_Owner_and_repository_authority
```

This prevents `Cline only does blueprint` from being misread as `every technical task goes to Cline`.

The automatic ChatGPT execution rule in Section 7 applies to authorized Class B repository governance/documentation/supervisory work. It does not silently authorize runtime/source/test/dependency/workflow/security/merge/deployment changes outside the active blueprint.

## 9. ChatGPT blueprint-edit exception requires explicit Human Owner authorization

ChatGPT owns non-blueprint rules, skills, router, governance, and documentation through the connected GitHub app.

ChatGPT must not edit the active CrewAI remediation blueprint or a blueprint-owned canonical technical contract merely to keep a non-blueprint rule change convenient.

If a non-blueprint ChatGPT update reveals that an exact blueprint document or blueprint-owned technical contract also needs a consistency correction:

```text
identify the exact blueprint file
→ identify the exact section
→ state the exact minimal required change
→ STOP before editing that blueprint file
→ require explicit Human Owner authorization for ChatGPT to edit that exact blueprint target
```

Required blocker:

```yaml
GALAX_CHATGPT_BLUEPRINT_EDIT_AUTHORIZATION_GATE_V1:
  result: BLOCK_CHATGPT_BLUEPRINT_EDIT_REQUIRES_HUMAN_AUTHORIZATION
  exact_file:
  exact_section:
  exact_reason:
  exact_proposed_change_boundary:
  source_or_test_implementation_authorized: false
  Cline_blueprint_execution_role_changed: false
  Human_Owner_authorization_required: true
```

After the Human Owner explicitly authorizes that exact ChatGPT blueprint-document edit, ChatGPT may perform only that exact bounded GitHub documentation/contract edit.

That exception does not authorize ChatGPT to take over CrewAI blueprint implementation, source edits, test implementation, validation, implementation Git actions, merge, or deployment. Cline remains the blueprint execution writer.

## 10. No duplication rule

This skill must not become a second copy of Skill 2 or Skill 9.

```yaml
Skill_10_owns:
  - predelegation_blueprint_scope_classification
  - hard_block_of_non_blueprint_Cline_work
  - same_request_automatic_handoff_to_correct_ChatGPT_owner
  - blueprint_trace_evidence_gate
  - ChatGPT_blueprint_edit_authorization_blocker

Skill_10_does_not_own:
  - detailed_Cline_prompt_schema
  - Cline_permission_UI_logic
  - repository_write_execution
  - evidence_acceptance
  - continuity_persistence
  - remote_PR_review
  - cleanup_execution
```

Detailed Cline task construction remains Skill 2.
Direct Class B updates remain Skill 9.
Continuity remains Skill 5.

## 11. Required handoff receipt

Return exactly one current scope-gate receipt before Cline work:

```yaml
GALAX_CLINE_BLUEPRINT_SCOPE_BLOCKER_RECEIPT_V1:
  Human_Owner_request:
  proposed_Cline_objective:
  blueprint_trace_verified: true | false
  trace_sources: []
  classification:
  executor:
  gate_result:
  Cline_task_allowed: true | false
  Cline_prompt_created: true | false
  ChatGPT_direct_update_allowed_under_existing_owner_request: true | false
  same_request_automatic_router_handoff_required: true | false
  ask_owner_to_repeat_same_request: false
  ChatGPT_blueprint_edit_requires_new_owner_authorization: true | false
  exact_blocker_if_any:
  next_router_action:
  assumptions: []
```

For an authorized Class B result, the required receipt fields are:

```yaml
Cline_task_allowed: false
Cline_prompt_created: false
ChatGPT_direct_update_allowed_under_existing_owner_request: true
same_request_automatic_router_handoff_required: true
ask_owner_to_repeat_same_request: false
next_router_action: START_SAME_REQUEST_SKILL_9_CYCLE_AND_EXECUTE_AFTER_PRECHECK
```

## 12. Final strict contract

```text
Human Owner asks ChatGPT to do Galax repository work
→ before any Cline task, Skill 10 reads and classifies the exact request

exact active CrewAI blueprint execution
→ PASS_CLINE_BLUEPRINT_ONLY
→ Skill 2 may create/continue exactly one bounded Cline blueprint task
→ NO MORE, NO LESS

non-blueprint governance/rules/skills/router/docs and other authorized Class B repository updates
→ BLOCK Cline
→ NO Cline prompt
→ preserve the same Human Owner request
→ automatically start the separate same-request Skill 9 routing cycle
→ ChatGPT executes the requested update through connected GitHub after Skill 9 precheck
→ do not ask the Human Owner to repeat or reconfirm the same clear Class B request

continuity/achievement
→ BLOCK Cline
→ Skill 5

technical work outside active blueprint that is not an authorized Class B update
→ BLOCK Cline
→ wait for exact separate authority

ChatGPT needs to edit blueprint documentation/contract for consistency
→ STOP
→ exact Human Owner authorization required first
→ only exact authorized blueprint document edit may be made by ChatGPT
→ Cline remains blueprint implementation executor
```
