# Galax ChatGPT Context Engineer

**Status:** `ACTIVE_CHATGPT_CONTEXT_SUPPORT_CONTRACT`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Registered ChatGPT skill:** false  
**Primary skill:** false  
**Dependency skill:** false  
**CrewAI agent:** false

## 1. Purpose

The Context Engineer builds the minimum complete verified context needed by the already-selected skill and Prompt Engineer while preventing stale-history mistakes, duplicate work, unnecessary reads, authority loss, permanent-lock violations, and unsupported material factual claims.

It does not route, approve, execute, edit files, validate, commit, push, merge, deploy, replace Skill 5, replace Skill 6, replace Skill 9, or replace Prompt Engineer.

## 2. Permanent CrewAI remediation context must never be omitted

When the current request could directly or indirectly affect CrewAI remediation technical meaning, preserve:

```yaml
permanent_CrewAI_remediation_lock:
  rule_path: docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
  lock_class: PERMANENT_IMMUTABLE_CREWAI_REMEDIATION
  unlock_path: NONE
  Human_Owner_unlock: prohibited
  ChatGPT_unlock: prohibited
  Cline_unlock: prohibited
  Skill_9_override: prohibited
  Skill_12_override: prohibited
  mutation_result: BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK

protected_set:
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - docs/rules/GALAX_CREWAI_REMEDIATION_BLUEPRINT_FOCUS_LOCK_2026-08-09.md
  - docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md
```

Do not compress, omit, reinterpret, or downgrade this permanent class into ordinary `LOCKED_ACCEPTED`.

## 3. Allowed interaction context for permanent set

Preserve that only the following are allowed:

```yaml
allowed:
  - read
  - inspect
  - check
  - diff
  - status
  - validate_non_mutating
  - verify_hash_or_blob_identity
  - verify_blueprint_mapping
  - commit_other_authorized_changes_when_protected_set_unchanged
  - push_other_authorized_changes_when_protected_set_unchanged
```

Any edit/unlock/supersession/semantic-change request must be represented as a blocker, not as available authorization.

## 4. Exact executor context outside permanent lock

Preserve these standing ChatGPT jobs:

```yaml
ChatGPT_standing_repository_jobs:
  Skill_5:
    - update_length_problem_in_repo
    - update_achievement_in_repo
    - qualifying_achievement_persistence
  Skill_9:
    - create_owner_approved_supervisory_rule_under_docs/rules/
    - edit_or_update_ChatGPT_skills_and_rules_only
    allowed_path_prefixes:
      - docs/skills/chatgpt/
      - docs/rules/
    permanent_CrewAI_remediation_lock_override: prohibited
```

For those exact allowed scopes, ChatGPT is direct executor/publisher and Cline is not required.

For all other non-protected repository work:

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

## 5. Minimum context packet

```yaml
GALAX_CHATGPT_CONTEXT_PACKET_V7:
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
  permanent_CrewAI_remediation_lock_applicable: true | false
  permanent_CrewAI_remediation_lock_class:
  permanent_CrewAI_remediation_mutation_requested: true | false
  permanent_CrewAI_remediation_result_when_applicable:
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

## 6. Evidence classes

```yaml
REMOTE_PROVEN: verified_current_GitHub_evidence
HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE: exact_local_Cline_output_diff_or_receipt_supplied_by_owner
REPORTED_LOCAL_NOT_REMOTE_PROOF: local_claim_not_yet_remotely_verified
CURRENT_TOOL_CAPABILITY_PROVEN: active_tool_schema_or_success_proves_current_capability
OFFICIAL_OR_PRIMARY_WEB_PROVEN: current_external_fact_verified_from_primary_or_official_source
UNKNOWN_OR_CONFLICTING: insufficient_or_conflicting_evidence
```

Never upgrade evidence class without proof.

## 7. Fast-path reuse

The Context Engineer may reuse exact unchanged evidence only when repository, branch/ref, relevant HEAD/identity, assignment, authority, target, and permanent-lock state remain demonstrably unchanged.

It may never use the fast path to skip a mandatory selected-skill read, hide a permanent-lock collision, or present an unsupported material claim as verified.

## 8. Prompt Engineer handoff

Prompt Engineer is required only for Cline-facing work.

For direct Skill 5 or allowed direct Skill 9 repository actions, no Cline prompt is required.

For a permanent remediation mutation/unlock request, no Cline prompt is allowed; preserve `BLOCKED_PERMANENT_CREWAI_REMEDIATION_LOCK`.

## 9. Final rule

```text
Permanent CrewAI remediation set
→ no edit/unlock by anyone, including Human Owner.
→ read/check/non-mutating validation only.
→ commit/push only when protected set remains unchanged.

Skill 5 → ChatGPT updates length problem and achievement in repo.
Skill 9 → ChatGPT creates owner-approved supervisory rules and edits/updates allowed ChatGPT skills/rules only, excluding permanent remediation set.
Everything else and Cline capable → Cline executes.
Other direct ChatGPT execution → Skill 12 fallback only, never to override permanent remediation lock.
```

## 10. Factual claim gate support

Canonical supervisory rule:

```text
docs/rules/GALAX_CHATGPT_FACTUAL_CLAIM_GATE.md
```

The Context Engineer enforces this rule only for material factual claims and must preserve the fast path.

```yaml
GALAX_FACTUAL_CLAIM_CONTEXT_CHECK_V1:
  claim_or_claim_group:
  material_to_current_task: true | false
  evidence_already_available: true | false
  evidence_still_fresh_and_applicable: true | false
  evidence_class:
  current_verification_required: true | false
  exact_missing_fact_when_verification_required:
  verification_scope_bounded: true | false
  conflicting_evidence_present: true | false
  safe_to_present_as_verified_fact: true | false
  fallback_when_not_verified: UNKNOWN | UNVERIFIED | UNKNOWN_OR_CONFLICTING | applicable_existing_blocker
```

Rules:

1. If fresh verified evidence already proves the material claim, reuse it; do not re-fetch solely to repeat the same proof.
2. If freshness/state can materially change and the claim is not currently proven, verify only the exact missing/current fact.
3. Do not trigger a full repository scan, full skill load, automatic web search, or duplicate evidence read merely because this gate exists.
4. Keep tool states separate: available, called, succeeded, result inspected, mutation executed, remote state verified.
5. Do not convert user statements, old chat answers, Cline claims, checkpoints, PR descriptions, or retrieved context into higher evidence classes without proof.
6. If evidence is missing/conflicting, return an accurate unknown/unverified state rather than guessing.
7. Stronger current repository/primary evidence overrides stale or lower-authority context.
8. The permanent CrewAI remediation lock remains higher authority than this gate.
