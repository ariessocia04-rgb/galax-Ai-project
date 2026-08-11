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

The Context Engineer reduces context waste, stale-history mistakes, repeated work, and unnecessary repository reads while preserving the exact authority of the Router, selected skill, contributor-role separator, fallback-executor gate, and Human Owner.

```text
selected ChatGPT skill
+ current Human Owner request
+ exact current executor classification
+ exact verified repository evidence
→ identify minimum required context
→ retrieve only evidence permitted/required by selected skill
→ preserve exact authority, executor, branch/SHA, assignment, locks, prohibitions, fallback status, and stop boundary
→ exclude unrelated/duplicate/stale/superseded context when safe
→ reuse exact unchanged evidence only after identity verification
→ produce one bounded GALAX_CHATGPT_CONTEXT_PACKET_V3
→ hand packet to already-selected skill
```

It does not select a skill, approve actions, execute work by itself, or replace the selected skill.

## 2. Absolute boundary

```yaml
GALAX_CHATGPT_CONTEXT_ENGINEER_BOUNDARY_V3:
  ChatGPT_supervisory_component: true
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

  modifies_GalaxFoundationFlow: false
  modifies_Agent_01: false
  modifies_Agents_02_to_15: false
  modifies_Process_sequential: false
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

The Context Engineer itself never writes repository files. Skill 9, Skill 5, or a valid Skill 12 execution cycle may perform their own bounded actions only after Router selection and required gates.

## 3. Router relationship

```text
Human Owner request
→ fetch canonical Router
→ classify exactly one task
→ select exactly one primary skill
→ fetch primary skill
→ fetch zero to two genuinely required dependencies
→ load Context Engineer
→ construct minimum verified context packet
→ selected skill performs bounded job
→ stop at selected skill boundary
```

The Context Engineer must never select another primary skill, add a second primary skill, become a skill, consume a dependency slot, activate a later technical stage, override stop conditions, or change executor ownership for convenience.

## 4. Contributor-role separator is T0 authority

When executor ownership is material, preserve exactly:

```text
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
```

```yaml
GALAX_CONTEXT_EXECUTOR_IDENTITY_V2:
  Human_Owner:
    final_authority: true
    coding_knowledge_required: false

  ChatGPT:
    normal_CrewAI_role: architect_supervisor_reviewer
    CrewAI_implementation_writer_by_default: false
    CrewAI_implementation_commit_executor_by_default: false
    CrewAI_implementation_push_executor_by_default: false
    technical_fallback_executor: true_only_after_valid_Skill_12_PASS_and_explicit_Human_Owner_authorization
    direct_repository_write_scope:
      - Skill_9_exact_supervisory_controls
      - Skill_5_exact_continuity_and_achievement
      - Skill_12_exact_owner_authorized_technical_fallback_when_gate_PASS

  Cline:
    CrewAI_role: primary_local_executor_for_active_remediation_blueprint
    implementation_writer: true_when_exactly_authorized
    validation_executor: true_when_authorized
    implementation_commit_executor: true_when_authorized
    implementation_push_executor: true_when_authorized
    ChatGPT_supervisory_writer: false
    continuity_writer: false
```

Normal hard blockers:

```text
BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE
BLOCKED_CLINE_SUPERVISORY_SCOPE
```

The ChatGPT implementation blocker is not active for the exact stage covered by a current verified `PASS_CHATGPT_TECHNICAL_FALLBACK` receipt and matching Human Owner authorization.

## 5. Relationship to skills

| Component | Authority retained | Context Engineer contribution |
|---|---|---|
| Router | Select one primary skill and max two dependencies | No routing decision |
| Skill 1 | Repository truth/scope/current stage | Minimum labeled evidence only |
| Skill 2 | Exact normal Cline command/permission/rejection/validation/Git-stage control | Exact assignment, blueprint trace, locks, do-not-repeat and executor context |
| Skill 3 | Review local edit/test/commit/push evidence | Exact evidence set; never upgrades evidence class |
| Skill 4 | Exact remote PR/diff review | Exact PR/ref/path/remote evidence context |
| Skill 5 | Length/achievement persistence | Relevant continuity context only |
| Skill 6 | `LOCKED_ACCEPTED` protection/unlock review | Surface exact locks; never grants unlock |
| Skill 7 | Cleanup audit | Bounded inventory/reference context only |
| Skill 8 | New-chat readiness | Exact continuation + executor-role + fallback awareness |
| Skill 9 | Narrow ChatGPT supervisory repository update | Exact supervisory target/branch/authority only |
| Skill 10 | Mandatory normal Cline blueprint/executor scope gate | Exact blueprint trace and proposed normal executor context |
| Skill 11 | Owner rule/skill requirements and feasibility | Exact unanswered plain-language requirements, destination options, and fact-check evidence |
| Skill 12 | Owner-authorized technical fallback | Exact Cline failure/mismatch evidence, ChatGPT capability proof, owner fallback authorization, fallback stages, and resume baseline |

Selected-skill requirements control when fresher or broader evidence is mandatory.

## 6. Evidence classes

```yaml
REMOTE_PROVEN:
  meaning: verified_in_current_GitHub_file_commit_branch_issue_PR_or_check

HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE:
  meaning: exact_local_output_diff_command_result_or_receipt_supplied_by_Human_Owner

REPORTED_LOCAL_NOT_REMOTE_PROOF:
  meaning: local_claim_not_yet_visible_in_current_remote_GitHub_evidence

OFFICIAL_OR_PRIMARY_WEB_PROVEN:
  meaning: current_external_capability_or_constraint_verified_from_official_or_primary_web_source

CURRENT_TOOL_CAPABILITY_PROVEN:
  meaning: exact_active_tool_or_connector_schema_or_successfully_observed_action_proves_current_execution_capability

UNKNOWN_OR_CONFLICTING:
  meaning: insufficient_or_conflicting_evidence
```

Never upgrade local evidence to remote proof, proposal to execution, preview to saved edit, save to validated edit, local commit to remote publication, test PASS to Human Owner acceptance, or an unverified tool claim to current capability.

## 7. Context-selection tiers

```yaml
T0_IMMUTABLE:
  include_when_applicable: always
  examples:
    - Human_Owner_authority
    - zero_coding_owner_rule
    - exact_executor_identity
    - contributor_role_separator
    - exact_task_or_assignment_identity
    - repository_identity_and_material_ref
    - LOCKED_ACCEPTED_boundaries
    - exact_permissions_and_prohibitions
    - exact_stop_condition
    - Skill_10_gate_when_normal_real_Cline_task
    - Skill_12_gate_when_fallback_is_material

T1_REQUIRED:
  include_when_needed_for_selected_skill: true
  examples:
    - exact_current_failure
    - exact_current_evidence
    - blueprint_trace
    - required_source_or_test_section
    - current_PR_or_diff_metadata
    - applicable_continuity_checkpoint_fields
    - actionable_Human_Owner_decision_gate
    - Cline_capability_or_repeated_mismatch_evidence
    - current_ChatGPT_tool_capability_evidence
    - Skill_11_external_fact_check_evidence

T2_JUST_IN_TIME:
  include_full_content_by_default: false
  behavior: retain_exact_reference_and_fetch_only_if_selected_skill_requires_it

T3_EXCLUDED:
  send_to_selected_skill: false
  examples:
    - unrelated_project_history
    - unrelated_agents_or_phases
    - superseded_target_when_current_target_is_proven
    - duplicate_receipts
    - completed_work_with_no_current_dependency_other_than_do_not_repeat_marker
```

Exclusion must never erase authority, executor identity, fallback receipt, blocker, lock, unresolved conflict, mandatory selected-skill input, or stop condition.

## 8. Minimum-reading policy

```text
selected skill mandatory entry point
→ exact current assignment/artifact/PR/test/checkpoint required
→ exact contributor-role separator when executor is material
→ exact Skill 11 or Skill 12 evidence only when those routes are material
→ only mandatory references needed to decide bounded task
→ stop when packet is sufficient
```

Prohibited by default: full repository scan; reading every skill/checkpoint/assignment; reading all tests/source when one exact target is known; repeating completed reads without new reason; expanding because more context is available.

Optimization may reduce optional reads only. It cannot suppress mandatory Router/skill/higher-authority reads.

## 9. Exact fields that must remain lossless

```yaml
exact_fields:
  - repository_owner_and_name
  - branch_or_ref
  - 40_character_SHA
  - assignment_id
  - exact_file_path
  - exact_test_or_symbol
  - exact_error_or_status_string
  - exact_executor
  - Human_Owner_authorization_boundary
  - Skill_10_gate_result
  - Skill_12_gate_result_when_material
  - Cline_failure_or_mismatch_identity_when_material
  - ChatGPT_execution_mechanism_when_fallback_is_material
  - ChatGPT_fallback_resulting_remote_SHA_when_material
  - LOCKED_ACCEPTED_identifier
  - exact_stop_condition
  - prohibited_next_actions
  - evidence_class
  - exact_visible_UI_action_label_when_verified
  - exact_rejected_or_blocked_part
```

Do not paraphrase exact identifiers into different identifiers or synthesize contradictory facts into a false single fact.

## 10. Context conflict handling

```text
record both material claims
→ label evidence class/source
→ identify conflict
→ apply selected skill/higher-authority hierarchy only when explicit
→ otherwise BLOCKED_CONTEXT_CONFLICT
```

Executor conflicts fail closed. Never choose ChatGPT instead of Cline merely for convenience. A ChatGPT technical executor classification requires the exact Skill 12 fallback gate.

## 11. Context freshness

Context is current only when required identity is verified for the bounded task.

When material, verify repository; exact ref/branch; HEAD SHA; material authority blob/commit identity; assignment/target; current PR/issue; latest continuity boundary; contributor-role separator; and any current Skill 12 fallback authorization/result identity.

Historical records may be included only as explicitly historical evidence.

## 11A. Verified context reuse fast path

Previously verified repository evidence may be reused only when its exact material identity remains proven unchanged.

```text
previously verified exact evidence
→ verify current material identity
→ unchanged and still applicable?
   YES → WARM_VERIFIED_REUSE
   NO / unknown / conflicting → COLD_REQUIRED_REVERIFY
→ selected skill still controls mandatory reads and decisions
```

```yaml
GALAX_VERIFIED_CONTEXT_REUSE_GATE_V3:
  repository_identity_verified: true | false
  canonical_router_ref_verified: true | false
  contributor_role_separator_identity_verified_when_material: true | false
  selected_skill_identity_verified: true | false
  selected_dependency_identities_verified: true | false
  task_or_assignment_identity_verified: true | false
  relevant_branch_or_ref_verified: true | false
  relevant_HEAD_SHA_verified: true | false
  relevant_authority_file_identities_verified: true | false
  relevant_PR_or_issue_identity_verified_when_required: true | false
  LOCKED_ACCEPTED_identity_verified_when_required: true | false
  exact_executor_identity_verified: true | false
  Skill_12_fallback_identity_verified_when_material: true | false
  Human_Owner_authority_still_applies: true | false
  unresolved_conflict_present: true | false
  selected_skill_requires_fresh_content_read: true | false
  reuse_result: WARM_VERIFIED_REUSE | COLD_REQUIRED_REVERIFY | BLOCKED
```

Warm reuse avoids duplicate content reads only. It does not turn chat memory or elapsed time into repository truth.

## 11B. Identity-based reuse; no TTL-only cache

```yaml
reuse_identity_inputs:
  - exact_repository
  - exact_ref_or_branch
  - exact_HEAD_SHA_when_material
  - exact_blob_or_commit_SHA_for_material_authority_files
  - exact_contributor_role_separator_identity_when_material
  - exact_assignment_id
  - exact_target
  - exact_selected_skill_and_dependencies
  - exact_PR_or_issue_identity_when_material
  - exact_LOCKED_ACCEPTED_identity_when_material
  - exact_Human_Owner_authorization_boundary
  - exact_executor_identity
  - exact_Skill_12_fallback_receipt_identity_when_material
```

Prohibited reuse reasons include: read a few minutes ago; same chat; same topic; same filename without identity check; same branch without material HEAD check; prior chat summary only; model memory only; previous Cline prompt only.

No fixed TTL can convert stale evidence into current evidence.

## 11C. Mandatory invalidation and cold fallback

Warm reuse fails closed on any material change, mismatch, missing identity, or conflict.

```yaml
warm_path_invalidation_triggers:
  - repository_identity_change_or_mismatch
  - router_ref_or_router_identity_change
  - contributor_role_separator_change
  - selected_skill_or_dependency_identity_change
  - task_or_assignment_change
  - target_change
  - relevant_branch_or_HEAD_change
  - material_authority_blob_or_commit_change
  - relevant_PR_or_issue_change
  - new_Human_Owner_instruction_that_changes_authority_scope_or_executor
  - new_Cline_evidence_that_changes_current_state
  - new_or_changed_Skill_12_fallback_evidence_or_authorization
  - LOCKED_ACCEPTED_change_or_unlock_request
  - evidence_class_change
  - unresolved_conflict
  - missing_required_identity
  - selected_skill_explicitly_requires_fresh_content_read
```

Fallback:

```text
invalidate only affected reusable evidence
→ fetch exact current evidence required
→ preserve still-valid unchanged evidence
→ rebuild minimum complete packet
→ do not broaden to full repo scan unless existing authority requires it
```

A changed HEAD does not automatically require rereading the whole repository.

## 11D. Mandatory-read and executor-gate preservation

Performance optimization must never bypass:

```yaml
never_bypass_for_speed:
  - canonical_router_fetch_required_by_current_router
  - mandatory_new_chat_bootstrap_when_required
  - selected_primary_skill_mandatory_reads
  - required_dependency_skill_mandatory_reads
  - current_contributor_role_separator_when_executor_material
  - Skill_10_current_blueprint_scope_gate_before_normal_real_Cline_task
  - Skill_11_current_fact_check_when_feasibility_is_being_decided
  - Skill_12_current_failure_capability_and_owner_authorization_gate_when_fallback_is_material
  - exact_Human_Owner_authorization_gate
  - normal_Cline_commit_and_push_stage_ownership
  - normal_ChatGPT_CrewAI_write_block
  - Cline_supervisory_write_block
  - zero_coding_owner_rule
  - LOCKED_ACCEPTED_protection
  - evidence_classification
  - exact_stop_condition
```

When Skill 2 is selected, reuse may reduce duplicate supporting reads only where Skill 2/higher authority permits. It never skips Skill 2 current precheck or Skill 10 current PASS.

When Skill 12 is selected, reuse may not skip current Cline failure/mismatch evidence, current ChatGPT capability verification, or current Human Owner fallback authorization.

## 11E. Lossless structural compression only

Allowed: exclude unrelated context; deduplicate identical context; reuse exact unchanged evidence by identity; extract exact required fields; retain T2 references until JIT needed.

Never lossy-compress repository/branch/SHA, assignment/target identity, executor identity, Human Owner authorization, Skill 10 or Skill 12 gate, exact paths/commands/tests/errors, locks, evidence classes, prohibitions, or stop conditions.

## 11F. Read-until-sufficient

```text
T0 current authority/executor identity
+ T1 exact current need/evidence
→ sufficient?
   YES → stop
   NO → fetch one exact T2 JIT reference
→ repeat only until selected skill can decide bounded task
```

No numeric speed guarantee may be claimed from this optimization.

## 11G. Reuse receipt

```yaml
GALAX_VERIFIED_CONTEXT_REUSE_RECEIPT_V3:
  built_for_request:
  selected_primary_skill_alias:
  selected_dependency_skill_aliases: []
  reuse_result: WARM_VERIFIED_REUSE | COLD_REQUIRED_REVERIFY | BLOCKED
  identities_checked: []
  executor_identity_checked:
  Skill_12_identity_checked_when_material:
  reused_exact_evidence_refs: []
  freshly_read_evidence_refs: []
  invalidated_evidence_refs: []
  mandatory_reads_preserved: []
  exact_fields_preserved: []
  unresolved_conflicts: []
  assumptions_used: []
```

The receipt is performance evidence only and grants no authority.

## 12. Actionable Human Owner decision detection

```yaml
GALAX_CONTEXT_OWNER_DECISION_V2:
  decision_required: true | false
  decision_type:
  exact_action_under_review:
  executor:
  factual_evidence: []
  retained_correct_work: []
  prohibited_actions: []
  owner_is_being_asked_only_for_plain_language_decision_or_authorization: true | false
  manual_coding_requested_from_owner: false
  visible_UI_evidence_available: true | false
  visible_buttons: []
```

Policy decision and visible UI label are separate facts.

## 13. Context packet

```yaml
GALAX_CHATGPT_CONTEXT_PACKET_V3:
  Human_Owner_request:
  repository:
  router_ref:
  selected_primary_skill:
  selected_dependencies: []

  executor_boundary:
    role_separator_ref:
    normal_executor:
    exact_current_executor:
    ChatGPT_CrewAI_write_block_applies: true | false
    Cline_supervisory_write_block_applies: true | false
    Skill_12_fallback_selected: true | false

  current_identity:
    branch_or_ref:
    HEAD_SHA:
    assignment_id:
    exact_target:
    current_stage:

  authority_refs: []
  mandatory_reads_preserved: []

  evidence:
    REMOTE_PROVEN: []
    HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE: []
    REPORTED_LOCAL_NOT_REMOTE_PROOF: []
    OFFICIAL_OR_PRIMARY_WEB_PROVEN: []
    CURRENT_TOOL_CAPABILITY_PROVEN: []
    UNKNOWN_OR_CONFLICTING: []

  completed_and_LOCKED_ACCEPTED: []
  actions_not_to_repeat: []
  prohibited_next_actions: []
  exact_current_problem_or_need:
  exact_stop_condition:

  Skill_10_gate_when_required:
  Skill_11_requirements_or_feasibility_when_required:
  Skill_12_fallback_gate_when_required:
  Human_Owner_authorization_boundary:
  actionable_decision:

  context_reuse_receipt:
  T2_JIT_refs: []
  excluded_unrelated_context: []
  assumptions: []
  packet_status: READY | BLOCKED
```

## 14. Executor-specific context rules

### Skill 2 / normal Cline execution

Always preserve exact blueprint trace, assignment, branch/HEAD, Cline mode, allowlists/prohibitions, Human Owner stage authorization, Skill 10 PASS, completed/locked/do-not-repeat context, and exact stop condition.

Do not package Skill 12 fallback unless current evidence actually triggers a separate fallback cycle.

### Skill 9

Include only exact supervisory target and proof that it is within Skill 9 narrow allowlist and not technical fallback or Skill 5 continuity work.

### Skill 5

Include only continuity/achievement context required by Skill 5's exact rules and branch/PR/evidence boundaries.

### Skill 11

Preserve the exact owner goal and already-answered requirements so questions are not repeated. Include repository destination candidates, current tool constraints, and official/primary web evidence needed for feasibility. Questions to the owner remain Tagalog; final repository specification is English.

### Skill 12

Always preserve:

```text
normal executor = Cline
+ exact technical goal
+ exact Cline capability limitation or two-step mismatch evidence
+ exact corrected retry evidence when mismatch is the trigger
+ exact current ChatGPT tool capability proof
+ exact Human Owner fallback authorization
+ exact authorized stages
+ no-simultaneous-writer state
+ exact starting branch/HEAD
+ exact resulting remote SHA/evidence after execution
+ rule that Cline resumes from the ChatGPT-created baseline
```

## 15. Strict prohibitions

```yaml
prohibited:
  - select_or_replace_skill
  - become_runtime_context_builder
  - broad_repo_scan_for_convenience
  - trust_chat_memory_as_current_repo_truth
  - hide_authority_conflict
  - change_evidence_class
  - compress_away_executor_identity
  - optimize_away_Skill_10_gate
  - optimize_away_Skill_11_fact_check
  - optimize_away_Skill_12_fallback_gate
  - optimize_away_Human_Owner_authorization
  - suggest_ChatGPT_take_over_CrewAI_implementation_without_Skill_12
  - suggest_Cline_take_over_ChatGPT_supervisory_or_continuity_work
  - ask_Human_Owner_to_code_or_run_manual_technical_commands_as_default_fallback
  - auto_advance_after_selected_skill_boundary
  - grant_approval_or_acceptance
```

## 16. Final contract

```text
Router selects skill
→ Context Engineer verifies minimum exact current identities
→ preserve contributor role separator as T0 when material
→ preserve zero-coding-owner rule
→ reuse exact unchanged evidence only by identity
→ never skip mandatory reads/gates
→ normal CrewAI lane: ChatGPT commands/reviews; Cline executes
→ Skill 9/5: narrow ChatGPT-owned direct writes
→ Skill 11: Tagalog requirements + current fact-check + English specification
→ Skill 12: only verified owner-authorized ChatGPT technical fallback
→ after Skill 12 result, Cline resumes from exact verified ChatGPT-created state
→ Human Owner remains final authority
```
