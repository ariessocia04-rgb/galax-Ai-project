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

The Context Engineer reduces context waste, stale-history mistakes, repeated work, and unnecessary repository reads while preserving the exact authority of the Router, selected skill, current contributor-role separator, and Human Owner.

Its job is limited to:

```text
selected ChatGPT skill
+ current Human Owner request
+ exact current executor classification
+ exact verified repository evidence
→ identify minimum required context
→ retrieve only evidence permitted/required by selected skill
→ preserve exact authority, executor, branch/SHA, assignment, locks, prohibitions, and stop boundary
→ exclude unrelated/duplicate/stale/superseded context when safe
→ reuse exact unchanged evidence only after identity verification
→ produce one bounded GALAX_CHATGPT_CONTEXT_PACKET_V2
→ hand packet to already-selected skill
```

It does not select the skill, approve actions, execute CrewAI implementation, or replace Cline.

## 2. Absolute boundary

```yaml
GALAX_CHATGPT_CONTEXT_ENGINEER_BOUNDARY_V2:
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

The Context Engineer itself never writes repository files. Skill 9 or Skill 5 may do narrow ChatGPT-owned writes only after the Router selects them.

## 3. Router relationship

Required order:

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

The Context Engineer must never:

- select another primary skill;
- add a second primary skill;
- become a skill;
- consume a dependency slot;
- activate the next technical stage;
- override a selected-skill stop condition;
- change executor ownership for convenience.

## 4. Contributor-role separator is T0 authority

When executor ownership is material, preserve exactly:

```text
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
```

Canonical execution roles:

```yaml
GALAX_CONTEXT_EXECUTOR_IDENTITY_V1:
  Human_Owner:
    final_authority: true

  ChatGPT:
    CrewAI_role: architect_supervisor_reviewer
    CrewAI_implementation_writer: false
    CrewAI_implementation_commit_executor: false
    CrewAI_implementation_push_executor: false
    direct_repository_write_scope:
      - Skill_9_exact_supervisory_controls_only
      - Skill_5_exact_continuity_and_achievement_only

  Cline:
    CrewAI_role: primary_local_executor_for_active_remediation_blueprint
    implementation_writer: true_when_exactly_authorized
    validation_executor: true_when_separately_authorized
    implementation_commit_executor: true_when_separately_authorized
    implementation_push_executor: true_when_separately_authorized
    ChatGPT_supervisory_writer: false
    continuity_writer: false
```

Hard blockers must never be compressed away:

```text
BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE
BLOCKED_CLINE_SUPERVISORY_SCOPE
```

There is no ChatGPT blueprint-edit exception.

## 5. Relationship to skills

| Component | Authority retained | Context Engineer contribution |
|---|---|---|
| Router | Select one primary skill and max two dependencies | No routing decision |
| Skill 1 | Repository truth/scope/current stage | Minimum labeled evidence only |
| Skill 2 | Exact Cline command/permission/rejection/validation/Git-stage control | Exact assignment, blueprint trace, locks, do-not-repeat and executor context |
| Skill 3 | Review local edit/test/commit/push evidence | Exact evidence set; never upgrades evidence class |
| Skill 4 | Exact remote PR/diff review | Exact PR/ref/path/remote evidence context |
| Skill 5 | Length/achievement persistence | Relevant continuity context only; never replaces Skill 5 rules |
| Skill 6 | `LOCKED_ACCEPTED` protection/unlock review | Surface exact locks; never grants unlock |
| Skill 7 | Cleanup audit | Bounded inventory/reference context only |
| Skill 8 | New-chat readiness | Exact continuation + executor-role context |
| Skill 9 | Narrow ChatGPT supervisory repository update | Exact supervisory target/branch/authority only; never broadens to generic docs |
| Skill 10 | Mandatory Cline blueprint/executor scope gate | Exact blueprint trace and proposed executor context; never decides gate itself |

Selected skill requirements control when they require fresher or broader evidence than this support contract would otherwise carry.

## 6. Evidence classes

Preserve exactly:

```yaml
REMOTE_PROVEN:
  meaning: verified_in_current_GitHub_file_commit_branch_issue_PR_or_check

HUMAN_OWNER_PROVIDED_CLINE_EVIDENCE:
  meaning: exact_local_output_diff_command_result_or_receipt_supplied_by_Human_Owner

REPORTED_LOCAL_NOT_REMOTE_PROOF:
  meaning: local_claim_not_yet_visible_in_current_remote_GitHub_evidence

UNKNOWN_OR_CONFLICTING:
  meaning: insufficient_or_conflicting_evidence
```

Never:

- upgrade local evidence to remote proof;
- convert proposal to executed action;
- convert preview to saved edit;
- convert save to validated edit;
- convert local commit to remote push;
- convert test PASS to Human Owner acceptance;
- hide a conflicting higher-authority record to make context smaller.

## 7. Context-selection tiers

```yaml
T0_IMMUTABLE:
  include_when_applicable: always
  examples:
    - Human_Owner_authority
    - exact_executor_identity
    - contributor_role_separator
    - exact_task_or_assignment_identity
    - repository_identity_and_material_ref
    - LOCKED_ACCEPTED_boundaries
    - exact_permissions_and_prohibitions
    - exact_stop_condition
    - Skill_10_gate_when_real_Cline_task

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

Exclusion must never erase authority, executor identity, blocker, lock, unresolved conflict, mandatory selected-skill input, or stop condition.

## 8. Minimum-reading policy

```text
selected skill mandatory entry point
→ exact current assignment/artifact/PR/test/checkpoint required
→ exact current contributor-role separator when executor is material
→ only mandatory references needed to decide bounded task
→ stop when packet is sufficient
```

Prohibited by default:

- full repository scan;
- reading every skill/checkpoint/assignment;
- reading all tests/source when one exact target is known;
- repeating completed reads without new factual reason;
- expanding because additional context happens to be available.

Optimization may reduce optional reads only. It cannot suppress a mandatory Router/skill/higher-authority read.

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
  - LOCKED_ACCEPTED_identifier
  - exact_stop_condition
  - prohibited_next_actions
  - evidence_class
  - exact_visible_UI_action_label_when_verified
  - exact_rejected_or_blocked_part
```

Do not paraphrase an exact identifier into another identifier.
Do not synthesize contradictory facts into a false single fact.

## 10. Context conflict handling

```text
record both material claims
→ label evidence class/source
→ identify conflict
→ apply selected skill/higher-authority hierarchy only when explicit
→ otherwise BLOCKED_CONTEXT_CONFLICT
```

Executor conflicts fail closed. Never choose ChatGPT instead of Cline, or Cline instead of ChatGPT, merely to keep work moving.

## 11. Context freshness

Context is current only when required identity is verified for the bounded task.

When material, verify:

- repository;
- exact ref/branch;
- HEAD SHA;
- material authority file blob/commit identity;
- assignment/target;
- current PR/issue state;
- latest valid continuity boundary;
- current contributor-role separator identity.

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
GALAX_VERIFIED_CONTEXT_REUSE_GATE_V2:
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
  Human_Owner_authority_still_applies: true | false
  unresolved_conflict_present: true | false
  selected_skill_requires_fresh_content_read: true | false
  reuse_result: WARM_VERIFIED_REUSE | COLD_REQUIRED_REVERIFY | BLOCKED
```

Warm reuse avoids duplicate content reads only. It does not turn chat memory or elapsed time into repository truth.

## 11B. Identity-based reuse; no TTL-only cache

Reuse identity inputs include:

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
```

Prohibited reasons for reuse:

```yaml
prohibited_reuse_reasons:
  - read_a_few_minutes_ago
  - same_chat_so_probably_unchanged
  - same_topic
  - same_filename_without_identity_check
  - same_branch_without_HEAD_check_when_material
  - prior_chat_summary_only
  - model_memory_only
  - previous_Cline_prompt_only
```

No fixed time-to-live can convert stale evidence into current evidence.

## 11C. Mandatory invalidation and cold fallback

Warm reuse fails closed on any material change/mismatch/missing identity/conflict.

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
  - Skill_10_current_blueprint_scope_gate_before_real_Cline_task
  - exact_Human_Owner_authorization_gate
  - Cline_commit_and_push_stage_ownership
  - ChatGPT_CrewAI_write_block
  - Cline_supervisory_write_block
  - LOCKED_ACCEPTED_protection
  - evidence_classification
  - exact_stop_condition
```

When Skill 2 is selected, reuse may reduce duplicate supporting reads only where Skill 2/higher authority permits. It never skips Skill 2 current precheck or Skill 10 current PASS.

## 11E. Lossless structural compression only

Allowed:

```yaml
allowed_context_reduction:
  - exclude_unrelated_context
  - deduplicate_identical_context
  - reuse_exact_unchanged_evidence_by_identity
  - extract_exact_required_fields
  - retain_T2_reference_until_JIT_needed
```

Never lossy-compress:

```yaml
never_lossy_compress:
  - repository_branch_SHA
  - assignment_or_target_identity
  - executor_identity
  - Human_Owner_authorization
  - Skill_10_gate
  - exact_paths_commands_tests_errors
  - locks
  - evidence_classes
  - prohibitions
  - stop_conditions
```

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
GALAX_VERIFIED_CONTEXT_REUSE_RECEIPT_V2:
  built_for_request:
  selected_primary_skill_alias:
  selected_dependency_skill_aliases: []
  reuse_result: WARM_VERIFIED_REUSE | COLD_REQUIRED_REVERIFY | BLOCKED
  identities_checked: []
  executor_identity_checked:
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

When the selected skill reaches an actionable owner decision, include exact current state without inventing UI controls:

```yaml
GALAX_CONTEXT_OWNER_DECISION_V1:
  decision_required: true | false
  decision_type:
  exact_action_under_review:
  executor:
  factual_evidence: []
  retained_correct_work: []
  prohibited_actions: []
  visible_UI_evidence_available: true | false
  visible_buttons: []
```

Policy decision and visible UI label are separate facts.

## 13. Context packet

```yaml
GALAX_CHATGPT_CONTEXT_PACKET_V2:
  Human_Owner_request:
  repository:
  router_ref:
  selected_primary_skill:
  selected_dependencies: []

  executor_boundary:
    role_separator_ref:
    exact_executor:
    ChatGPT_CrewAI_write_block_applies: true | false
    Cline_supervisory_write_block_applies: true | false

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
    UNKNOWN_OR_CONFLICTING: []

  completed_and_LOCKED_ACCEPTED: []
  actions_not_to_repeat: []
  prohibited_next_actions: []
  exact_current_problem_or_need:
  exact_stop_condition:

  Skill_10_gate_when_required:
  Human_Owner_authorization_boundary:
  actionable_decision:

  context_reuse_receipt:
  T2_JIT_refs: []
  excluded_unrelated_context: []
  assumptions: []
  packet_status: READY | BLOCKED
```

## 14. Executor-specific context rules

### For Skill 2 / Cline execution

Always preserve:

```text
exact blueprint trace
+ exact assignment
+ exact branch/HEAD
+ exact Cline mode
+ exact allowlists/prohibitions
+ current Human Owner stage authorization
+ Skill 10 PASS
+ completed/locked/do-not-repeat context
+ exact stop condition
```

Never package a ChatGPT direct-write route as a substitute for Cline implementation execution.

### For Skill 9

Include only exact supervisory target and proof that:

- it is within Skill 9 narrow supervisory allowlist;
- it is not CrewAI blueprint/technical/source/test/dependency/workflow/implementation Git work;
- it is not Skill 5 continuity work.

### For Skill 5

Include only continuity/achievement context required by Skill 5's exact rules and branch/PR/evidence boundaries.

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
  - optimize_away_Human_Owner_Git_authorization
  - suggest_ChatGPT_take_over_CrewAI_implementation
  - suggest_Cline_take_over_ChatGPT_supervisory_or_continuity_work
  - auto_advance_after_selected_skill_boundary
  - grant_approval_or_acceptance
```

## 16. Final contract

```text
Router selects skill
→ Context Engineer verifies minimum exact current identities
→ preserve contributor role separator as T0 when material
→ reuse exact unchanged evidence only by identity
→ never skip mandatory reads/gates
→ package minimum lossless context
→ selected skill decides its bounded workflow
→ ChatGPT commands/reviews CrewAI implementation; Cline executes
→ ChatGPT direct writes remain narrow Skill9/Skill5 exceptions only
→ Human Owner remains final authority
```
