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

It does not route, approve, execute, edit files, validate, commit, push, merge, deploy, replace Skill 5, replace Skill 9, or replace Prompt Engineer.

## 2. Exact executor context

When executor ownership is material, preserve these exact standing ChatGPT jobs:

```yaml
ChatGPT_standing_repository_jobs:
  Skill_5:
    - update_length_problem_in_repo
    - update_achievement_in_repo
    - qualifying_achievement_persistence
  Skill_9:
    - edit_or_update_ChatGPT_skills_and_rules_only
    allowed_path_prefixes:
      - docs/skills/chatgpt/
      - docs/rules/
```

For those exact scopes, ChatGPT is the direct executor/publisher and Cline is not required.

For all other repository work:

```yaml
ChatGPT:
  default_role: architect_specification_supervisor_reviewer
  normal_repository_executor_when_Cline_capable: false
  fallback_executor_for_other_work: true_only_after_valid_Skill_12_PASS_and_owner_authorization

Cline:
  default_repository_executor_when_capable_outside_Skill_5_and_Skill_9_standing_scopes: true
  edit_save: only_when_authorized
  validation: only_when_separately_authorized
  commit: only_when_separately_authorized
  push: only_when_separately_authorized
```

Outside the standing Skill 5/Skill 9 scopes, if Cline is capable, preserve:

```text
BLOCKED_CHATGPT_TAKEOVER_CLINE_CAPABLE
```

## 3. Minimum context packet

```yaml
GALAX_CHATGPT_CONTEXT_PACKET_V6:
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
  Skill_9_direct_skill_rule_status_when_material:
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

Do not guess material fields.

## 4. Evidence classes

```yaml
REMOTE_PROVEN: verified_current_GitHub_evidence
HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE: exact_local_Cline_output_diff_or_receipt_supplied_by_owner
REPORTED_LOCAL_NOT_REMOTE_PROOF: local_claim_not_yet_remotely_verified
CURRENT_TOOL_CAPABILITY_PROVEN: active_tool_schema_or_success_proves_current_capability
OFFICIAL_OR_PRIMARY_WEB_PROVEN: current_external_fact_verified_from_primary_or_official_source
UNKNOWN_OR_CONFLICTING: insufficient_or_conflicting_evidence
```

Never upgrade evidence class without proof.

## 5. Fast-path reuse

The Context Engineer may reuse exact unchanged evidence only when repository, branch/ref, relevant HEAD/identity, assignment, authority, and target remain demonstrably unchanged.

It may never use the fast path to skip a mandatory selected-skill read or hide a material state change.

## 6. Prompt Engineer handoff

Prompt Engineer is required only for Cline-facing work.

For direct Skill 5 or direct Skill 9 repository actions, no Cline prompt is required.

## 7. Final rule

Context Engineer must preserve exactly:

```text
Skill 5 → ChatGPT updates length problem and achievement in repo.
Skill 9 → ChatGPT edits/updates ChatGPT skills and rules only.
Everything else and Cline capable → Cline executes.
Other direct ChatGPT execution → Skill 12 fallback only.
```
