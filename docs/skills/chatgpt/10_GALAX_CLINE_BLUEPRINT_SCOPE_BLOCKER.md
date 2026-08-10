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
→ prove that the exact proposed Cline objective belongs to the active CrewAI remediation blueprint execution chain
→ PASS only that exact blueprint work
→ BLOCK every non-blueprint delegation to Cline
```

This skill does not write repository files, create implementation, review evidence, persist continuity, or replace Skill 2 or Skill 9.

It exists to enforce the Human Owner rule:

```text
Cline executes the CrewAI remediation blueprint — NO MORE, NO LESS.
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
    BLOCK_CLINE_ROUTE_TO_CHATGPT |
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

## 7. Non-blueprint hard block

When the proposed Cline objective is repository governance, ChatGPT rules, ChatGPT skills, router maintenance, supervisory documentation, owner-directed repository documentation, or another authorized Class B update outside the active blueprint:

```yaml
result: BLOCK_CLINE_ROUTE_TO_CHATGPT
executor: ChatGPT_Skill_9
Cline_task_created: false
```

Skill 10 must preserve the Human Owner's exact request and return it to the router for a separate Skill 9 routing cycle.

It must not itself perform the Skill 9 update.

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
  proposed_Cline_objective:
  blueprint_trace_verified: true | false
  trace_sources: []
  classification:
  executor:
  gate_result:
  Cline_task_allowed: true | false
  ChatGPT_direct_update_allowed_under_existing_owner_request: true | false
  ChatGPT_blueprint_edit_requires_new_owner_authorization: true | false
  exact_blocker_if_any:
  next_router_action:
  assumptions: []
```

## 12. Final strict contract

```text
about to use Cline
→ Skill 10 proves exact blueprint trace

PASS_CLINE_BLUEPRINT_ONLY
→ Skill 2 may create/continue exactly one bounded Cline blueprint task
→ NO MORE, NO LESS

non-blueprint governance/rules/skills/router/docs
→ BLOCK Cline
→ separate Router cycle to Skill 9 / ChatGPT connected GitHub

continuity/achievement
→ BLOCK Cline
→ Skill 5

technical work outside active blueprint
→ BLOCK Cline
→ wait for exact separate authority

ChatGPT needs to edit blueprint documentation/contract for consistency
→ STOP
→ exact Human Owner authorization required first
→ only exact authorized blueprint document edit may be made by ChatGPT
→ Cline remains blueprint implementation executor
```
