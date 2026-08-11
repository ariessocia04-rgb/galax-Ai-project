```yaml
skill_reference: $galax-cline-blueprint-scope-blocker
skill_id: GALAX-SKILL-10
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 10: Galax Cline Blueprint Scope and Execution Separator

```yaml
skill_name: Galax Cline Blueprint Scope and Execution Separator
skill_type: ChatGPT_Cline_predelegation_and_executor_hard_scope_gate
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

Skill 10 enforces the Human Owner's normal Cline-first execution separation before a real Cline task is created and whenever a proposed normal-lane executor may be crossing roles.

Canonical normal rule:

```text
CrewAI remediation-blueprint execution
→ ChatGPT decides, commands, supervises, and reviews
→ Cline executes locally
→ Cline edits/saves only authorized implementation
→ Cline runs only authorized validation
→ after ChatGPT evidence review and separate Human Owner Git authorization, Cline commits/pushes
→ ChatGPT reviews exact remote GitHub evidence
→ Human Owner final acceptance

ChatGPT supervisory controls
→ Cline is blocked
→ Skill 9 may let ChatGPT update only the exact supervisory allowlist

Length problem / achievement
→ Cline is blocked
→ Skill 5 owns the bounded direct ChatGPT continuity write
```

Skill 10 never writes repository files itself.

The separate Skill 12 technical fallback exception may supersede the normal ChatGPT implementation blocker only when the Router selects Skill 12 and `PASS_CHATGPT_TECHNICAL_FALLBACK` is produced from proven Cline failure/mismatch, proven ChatGPT capability, and explicit Human Owner authorization.

## 2. Canonical authorities

```yaml
role_separator:
  path: docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md

active_CrewAI_remediation_blueprint:
  path: docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md

active_Foundation_execution_contract:
  path: docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md

canonical_ChatGPT_Cline_control_plan:
  path: docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md

Cline_prompt_control:
  path: docs/skills/chatgpt/02_GALAX_STRICT_CLINE_PROMPT_GUARDIAN.md

ChatGPT_supervisory_direct_updates:
  path: docs/skills/chatgpt/09_GALAX_OWNER_DIRECT_REPOSITORY_UPDATE_GUARDIAN.md

continuity_and_achievement:
  path: docs/skills/chatgpt/05_GALAX_CONTINUITY_ACHIEVEMENT_GUARDIAN.md

owner_requirements_and_feasibility:
  path: docs/skills/chatgpt/11_GALAX_OWNER_RULE_SKILL_REQUIREMENTS_FEASIBILITY_GUARDIAN.md

ChatGPT_technical_fallback:
  path: docs/skills/chatgpt/12_GALAX_CHATGPT_TECHNICAL_FALLBACK_EXECUTOR_GUARDIAN.md
```

The current technical contract/assignment may narrow the blueprint. It may never expand the executor beyond this separator without the exact Skill 12 fallback gate.

## 3. Mandatory activation

Skill 10 is a mandatory dependency whenever Skill 2 is selected as primary for a real normal Cline task.

Before any `GALAX_CLINE_TASK_V2` is emitted, Skill 10 must classify the exact objective and return a current gate result.

Skill 10 also provides the canonical normal-lane blocker when routing would make ChatGPT write CrewAI implementation or make Cline write ChatGPT supervisory/continuity records.

Skill 10 is not the fallback executor. When the verified fallback conditions are present, the Router must stop the Skill 2/Skill 10 normal lane and start a separate Skill 12 routing cycle.

## 4. Exact blueprint trace requirement for Cline

Cline may receive a normal task only when the proposed objective has an evidence-backed trace:

```text
active CrewAI remediation blueprint
→ current canonical technical contract/plan that implements or narrows it
→ exact current Human-Owner-authorized technical assignment/stage
→ exact proposed Cline objective
```

All links must be current and compatible.

Insufficient reasons to use Cline include:

```yaml
insufficient_reasons_to_use_Cline:
  - file_is_in_repository
  - change_sounds_technical_without_blueprint_trace
  - Cline_can_edit_files
  - Cline_was_used_before
  - repository_governance_needs_change
  - ChatGPT_rule_skill_or_router_needs_change
  - length_problem_or_achievement_needs_change
```

## 5. Two-way normal-lane classification gate

```yaml
GALAX_EXECUTOR_SCOPE_GATE_V3:
  Human_Owner_request:
  proposed_action:
  proposed_executor: ChatGPT | Cline | Skill_5 | Skill_12 | NONE

  active_blueprint_path: docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  active_blueprint_verified: true | false
  active_technical_contract_or_assignment:
  exact_blueprint_trace_evidence: []

  action_is_exact_active_blueprint_execution: true | false
  action_is_ChatGPT_supervisory_control: true | false
  action_is_continuity_or_achievement: true | false
  action_is_other_or_ambiguous: true | false

  ChatGPT_would_edit_blueprint_or_blueprint_owned_technical_record: true | false
  ChatGPT_would_edit_source_or_tests: true | false
  ChatGPT_would_change_dependency_or_workflow: true | false
  ChatGPT_would_commit_or_push_implementation: true | false

  Cline_would_edit_ChatGPT_skill_router_or_context_rule: true | false
  Cline_would_edit_supervisory_role_separator: true | false
  Cline_would_edit_length_problem_or_achievement: true | false

  verified_Skill_12_fallback_cycle_selected: true | false

  executor:
    Cline |
    ChatGPT_Skill_9 |
    ChatGPT_Skill_5 |
    ChatGPT_Skill_12 |
    NONE_BLOCKED

  gate_result:
    PASS_CLINE_BLUEPRINT_ONLY |
    PASS_CHATGPT_SUPERVISORY_ONLY |
    PASS_SKILL_5_CONTINUITY_ONLY |
    HANDOFF_TO_SKILL_12_FALLBACK |
    BLOCK_CHATGPT_CREWAI_IMPLEMENTATION_WRITE |
    BLOCK_CLINE_SUPERVISORY_SCOPE |
    BLOCK_UNRELATED_OR_AMBIGUOUS_SCOPE |
    BLOCK_MISSING_BLUEPRINT_TRACE

  factual_reason:
```

No real normal Cline task may be emitted unless:

```text
gate_result == PASS_CLINE_BLUEPRINT_ONLY
```

No Skill 9 direct write may proceed when this classification proves CrewAI implementation or a non-supervisory target.

## 6. Cline PASS rule

Return `PASS_CLINE_BLUEPRINT_ONLY` only when all are true:

```yaml
cline_pass_requirements:
  active_blueprint_verified: true
  exact_current_technical_assignment_or_stage_verified: true
  proposed_objective_directly_executes_or_validates_blueprint: true
  proposed_objective_within_current_narrow_contract: true
  proposed_objective_within_Human_Owner_authorization: true
  proposed_objective_not_ChatGPT_supervisory_or_continuity_work: true
  proposed_objective_does_not_expand_to_adjacent_work: true
```

Then Skill 2 may create one exact bounded Cline task.

Cline remains responsible for the normal local execution stage, including implementation edits/saves and, only when separately authorized, exact validation, commit, and push stages.

## 7. Cline Git stage rule

For normal active CrewAI implementation, Cline is the executor for implementation Git commands.

```text
local edit/save complete
→ ChatGPT reviews evidence
→ PASS / CHANGES_REQUIRED
→ STOP

Human Owner separately authorizes commit
→ Cline receives one GIT_ONLY commit task
→ Cline commits
→ STOP

Human Owner separately authorizes push
→ Cline receives one GIT_ONLY push task
→ Cline pushes
→ STOP

GitHub remote evidence available
→ ChatGPT independently reviews exact remote diff/evidence
→ Human Owner final acceptance
```

A ChatGPT PASS does not automatically grant commit or push authority.

## 8. Normal hard block: ChatGPT may not execute CrewAI implementation

When the current cycle is the normal Skill 2/Skill 10 Cline lane and no Skill 12 fallback cycle has been selected, if ChatGPT would edit, save, validate, commit, push, or otherwise publish active CrewAI implementation or blueprint-owned technical work, return:

```text
BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE
```

This includes:

```yaml
blocked_ChatGPT_targets_or_actions_normal_lane:
  - active_CrewAI_remediation_blueprint_file
  - blueprint_owned_technical_contract_or_execution_plan
  - src_or_runtime_code
  - executable_tests
  - dependency_or_lockfile
  - implementation_branch_source_or_test_change
  - implementation_commit
  - implementation_push
  - workflow_or_secret
  - merge
  - deployment
```

If the Human Owner authorizes an exact normal CrewAI technical stage, preserve that request and route execution to Cline under Skill 2.

Do not reinterpret normal Human Owner technical authorization as permission for ChatGPT to become implementation writer.

## 9. Skill 12 exception handoff

The normal blocker in Section 8 does not prevent a separate Skill 12 cycle when all fallback prerequisites are proven.

Qualifying reasons are limited to:

```yaml
Skill_12_handoff_reasons:
  - Cline_current_capability_limit_factually_proven
  - Cline_materially_mismatched_same_bounded_goal_again_after_one_exact_corrected_retry
```

Required handoff:

```text
normal Cline task cannot be completed reliably
→ preserve correct completed Cline work
→ stop/freeze overlapping Cline action
→ verify current ChatGPT tool can perform the exact action
→ explain limitation/mismatch to Human Owner in plain Tagalog
→ obtain explicit Human Owner fallback authorization
→ Router selects Skill 12 in a separate cycle
→ Skill 12 independently produces PASS_CHATGPT_TECHNICAL_FALLBACK or blocks
```

Skill 10 must not itself convert `BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE` into fallback authority.

## 10. Hard block: Cline may not maintain ChatGPT supervisory controls

If Cline would edit, save, commit, or push any ChatGPT-owned supervisory target, return:

```text
BLOCKED_CLINE_SUPERVISORY_SCOPE
```

Examples:

```yaml
blocked_Cline_targets:
  - ChatGPT_skill
  - ChatGPT_router
  - ChatGPT_Context_Engineer_support_contract
  - ChatGPT_Cline_supervisory_rule_or_role_separator
  - canonical_new_chat_supervisory_operating_instruction
  - length_problem_checkpoint
  - achievement_record
```

Required handoff:

```text
ChatGPT skill/router/rule supervisory maintenance
→ Skill 9

length problem / achievement
→ Skill 5
```

Do not restart, rewrite, or invalidate correct Cline implementation work when removing a supervisory target from an overbroad request.

## 11. Skill 9 PASS rule

Return `PASS_CHATGPT_SUPERVISORY_ONLY` only when the requested repository change is exactly within Skill 9's supervisory allowlist and changes no CrewAI blueprint/runtime/source/tests/dependencies/workflows/implementation Git state.

## 12. Skill 5 PASS rule

Length-problem and achievement work is classified separately:

```yaml
result: PASS_SKILL_5_CONTINUITY_ONLY
executor: ChatGPT_Skill_5
Cline_task_created: false
Skill_9_write: false
```

## 13. Other or ambiguous work

A technical task outside the current blueprint is not automatically Cline work, and a non-blueprint repository task is not automatically ChatGPT direct-write work.

```yaml
other_or_ambiguous_scope:
  default_result: BLOCK_UNRELATED_OR_AMBIGUOUS_SCOPE
  executor: NONE_BLOCKED
  required_next_step: prove_existing_repository_authority_and_exact_executor_or_obtain_exact_Human_Owner_instruction
```

Do not broaden Skill 9 into generic documentation maintenance.
Do not broaden Cline into generic repository maintenance.
Do not broaden Skill 12 into a permanent ChatGPT implementation role.

## 14. Required receipt

```yaml
GALAX_EXECUTOR_SCOPE_BLOCKER_RECEIPT_V3:
  Human_Owner_request:
  proposed_action:
  proposed_executor:
  blueprint_trace_verified: true | false
  trace_sources: []
  classification:
  executor:
  gate_result:

  Cline_task_allowed: true | false
  ChatGPT_supervisory_direct_update_allowed: true | false
  Skill_5_continuity_direct_update_allowed: true | false
  Skill_12_fallback_handoff_allowed: true | false

  ChatGPT_CrewAI_write_blocked_in_normal_lane: true | false
  Cline_supervisory_write_blocked: true | false

  exact_blocker_if_any:
  next_router_action:
  assumptions: []
```

## 15. Final strict contract

```text
exact active CrewAI remediation-blueprint execution in normal lane
→ PASS_CLINE_BLUEPRINT_ONLY
→ ChatGPT prepares one exact bounded command
→ Cline executes
→ Cline validation / commit / push only at authorized stages
→ ChatGPT reviews evidence and remote diff
→ Human Owner final acceptance

Cline cannot perform exact action OR materially mismatches it again after one corrected retry
→ stop normal lane
→ verify ChatGPT exact capability
→ obtain Human Owner explicit fallback authorization
→ separate Skill 12 cycle

ChatGPT skill/router/context/supervisory rule maintenance
→ BLOCK Cline
→ PASS_CHATGPT_SUPERVISORY_ONLY
→ Skill 9

length problem / achievement
→ BLOCK Cline
→ PASS_SKILL_5_CONTINUITY_ONLY
→ Skill 5

ChatGPT tries CrewAI implementation write in normal lane without Skill 12
→ BLOCK_CHATGPT_CREWAI_IMPLEMENTATION_WRITE

Cline tries ChatGPT rules/skills/router/continuity
→ BLOCK_CLINE_SUPERVISORY_SCOPE

anything else or ambiguous
→ BLOCK_UNRELATED_OR_AMBIGUOUS_SCOPE
```
