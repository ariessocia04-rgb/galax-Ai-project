# Galax ChatGPT Context Engineer

**Status:** `ACTIVE_CHATGPT_CONTEXT_SUPPORT_CONTRACT`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Registered ChatGPT skill:** false  
**Primary skill:** false  
**Dependency skill:** false  
**CrewAI agent:** false  
**Final authority:** Human Owner

## 1. Purpose

The Context Engineer builds the minimum complete verified context needed by the already-selected skill and Prompt Engineer while preventing stale-history mistakes, duplicate work, unnecessary reads, and authority loss.

```text
Human Owner request
+ Router-selected skill
+ required dependencies
+ exact repository evidence
→ select minimum required context
→ preserve authority and executor identity
→ preserve branch/SHA/assignment/locks/do-not-repeat/stop boundary
→ exclude unrelated/stale/duplicate context when safe
→ produce one bounded context packet
→ hand it to selected skill and Prompt Engineer when Prompt Engineer is required
```

## 2. Absolute boundary

The Context Engineer does not route, approve, reject, execute, edit files, validate, commit, push, merge, deploy, create authority, replace Skill 2, replace Skill 5, or replace Prompt Engineer.

It consumes zero primary/dependency skill slots.

## 3. Executor context

When executor ownership is material, preserve this exact distinction:

```yaml
Human_Owner:
  final_authority: true
  coding_knowledge_required: false

ChatGPT:
  default_role: architect_specification_supervisor_reviewer
  normal_repository_executor_when_Cline_capable: false
  Skill_5_direct_continuity_executor: true
  Skill_5_direct_continuity_publisher: true_when_connected_GitHub_capability_available
  fallback_executor_for_other_work: true_only_after_valid_Skill_12_PASS_and_owner_authorization

Cline:
  default_repository_executor_when_capable: true_except_exact_Skill_5_continuity_scope
  edit_save: only_when_authorized
  validation: only_when_separately_authorized
  commit: only_when_separately_authorized
  push: only_when_separately_authorized
  Skill_5_length_or_achievement_executor: false_by_default
```

For non-Skill-5 work, if Cline is capable, preserve blocker:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

For exact Skill 5 `update_length_problem`, `update_achievement`, or qualifying achievement persistence, preserve that ChatGPT is the direct executor/publisher and Cline is not required.

## 4. Minimum context packet

```yaml
GALAX_CHATGPT_CONTEXT_PACKET_V5:
  repository:
  ref_or_branch:
  verified_HEAD_SHA:
  primary_skill:
  dependency_skills: []
  Human_Owner_request:
  Human_Owner_authorization_boundary:
  executor_identity:
  current_assignment:
  current_stage:
  exact_target:
  completed_work: []
  LOCKED_ACCEPTED: []
  rejected_or_superseded_work: []
  do_not_repeat: []
  current_blockers: []
  allowed_scope: []
  prohibited_scope: []
  evidence_classes: []
  Skill_5_direct_persistence_status_when_material:
  Skill_10_status_when_material:
  Skill_12_status_when_material:
  exact_stop_condition:

  prompt_context:
    current_Cline_assignment:
    current_Cline_session_continuity:
    same_bounded_task_as_previous_prompt: true | false | UNKNOWN
    previous_prompt_completed: true | false | UNKNOWN
    previous_prompt_result:
    correction_of_same_task_required: true | false
    new_independent_task_required: true | false
    owner_action_required:
    exact_execution_stage:
    exact_mode_candidate:
    exact_stop_condition:
```

Do not guess material fields. Mark unknown evidence explicitly.

## 5. Evidence classes

```yaml
REMOTE_PROVEN:
  meaning: verified current GitHub evidence
HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE:
  meaning: exact local Cline output/diff/receipt supplied by owner
REPORTED_LOCAL_NOT_REMOTE_PROOF:
  meaning: local claim not yet remotely verified
CURRENT_TOOL_CAPABILITY_PROVEN:
  meaning: active tool/schema/success proves current capability
OFFICIAL_OR_PRIMARY_WEB_PROVEN:
  meaning: current external fact verified from primary/official source
UNKNOWN_OR_CONFLICTING:
  meaning: insufficient or conflicting evidence
```

Never upgrade local evidence to remote proof, proposal to saved edit, save to validation, commit to push, or prompt to execution.

## 6. Fast-path reuse

The Context Engineer may reuse exact unchanged evidence only when repository, branch/ref, relevant HEAD/identity, assignment, authority, and target remain demonstrably unchanged.

It may never use the fast path to skip a mandatory selected-skill read or hide a material state change.

## 7. Prompt Engineer handoff

When a Cline-facing or owner-action package is required:

```text
Context Engineer verified packet
→ selected skill determines exact authority/scope/mode
→ Prompt Engineer chooses exact NEW/STAY presentation and mode label from verified facts
→ final owner-facing + Cline-facing package
```

For direct Skill 5 continuity persistence, Prompt Engineer is not required because no Cline prompt is needed.

If NEW/STAY cannot be safely established for a Cline task, Prompt Engineer must return `BLOCKED_CLINE_SESSION_STATE_UNVERIFIED`; Context Engineer must not invent it.

## 8. Final rule

Context Engineer optimizes context without weakening Router, selected skill, the standing Skill 5 ChatGPT continuity exception, Skill 10, Skill 12, Human Owner authority, stage separation, LOCKED_ACCEPTED, or the general Cline-default execution model.
