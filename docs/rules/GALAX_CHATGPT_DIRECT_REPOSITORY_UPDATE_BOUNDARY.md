# Galax ChatGPT Direct Repository Update Boundary

**Status:** `ACTIVE_CANONICAL_HUMAN_OWNER_CONTRIBUTOR_BOUNDARY`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Canonical governance ref:** `docs/chatgpt-skill-router-2026-08-02`  
**Applies to:** ChatGPT, Cline, and every Galax repository-supervision workflow  
**Runtime effect:** none  
**CrewAI architecture change:** false  
**Final authority:** Human Owner

## 1. Purpose

This rule separates Cline's real job from repository-governance work that belongs to ChatGPT.

The Human Owner's standing contributor boundary is:

```text
active CrewAI remediation blueprint implementation work
→ Cline is the primary local implementation writer

Human-Owner-requested repository update that is outside the active CrewAI remediation blueprint
→ ChatGPT performs the exact bounded repository update directly through the connected GitHub app
→ do not create a Cline task merely to perform that update
```

This rule exists to prevent Cline from being assigned governance, continuity, documentation, routing, repository-memory, or other owner-requested repository updates that are not part of Cline's active CrewAI blueprint implementation assignment.

## 2. Canonical responsibility split

```yaml
GALAX_CONTRIBUTOR_RESPONSIBILITY_BOUNDARY_V1:
  Human_Owner:
    final_authority: true

  ChatGPT:
    role: repository_aware_architect_reviewer_and_owner_direct_repo_updater
    direct_GitHub_writer_for_owner_authorized_non_blueprint_repo_updates: true
    must_use_connected_GitHub_for_direct_updates: true
    must_verify_live_repo_before_write: true

  Cline:
    role: primary_local_writer_for_active_CrewAI_blueprint_implementation_only
    generic_repository_governance_writer: false
    continuity_writer: false
    ChatGPT_skill_or_router_writer_by_default: false
    owner_direct_non_blueprint_repo_update_writer: false

  GitHub:
    canonical_source_of_truth: true

  CrewAI:
    application_runtime_only: true
```

The phrase `Cline is the primary local writer` is henceforth scoped to the active CrewAI remediation blueprint implementation worktree and its exact authorized technical assignments. It must not be interpreted as a requirement to delegate every repository write to Cline.

## 3. Request classification gate

Before deciding who performs an update, classify the exact requested change.

### Class A — Active CrewAI blueprint implementation

Examples:

- Foundation or Agent 01 source implementation required by the active remediation blueprint;
- blueprint-required contract test implementation;
- an exact technical correction explicitly authorized by the current CrewAI implementation assignment;
- blueprint-required local validation or implementation Git task when separately authorized.

Required executor:

```yaml
executor: Cline
control: GALAX_CLINE_TASK_V2
one_task_one_goal_one_stop: required
Human_Owner_action_gates: preserved
```

ChatGPT remains architect/reviewer and does not silently replace Cline as the implementation worktree writer for Class A.

### Class B — Human-Owner-authorized repository update outside the active CrewAI blueprint

Examples include exact bounded updates to:

- ChatGPT router or ChatGPT supervisory skills;
- Galax repository governance rules;
- operating manuals;
- repository documentation;
- plans or records that do not implement CrewAI runtime/source/tests;
- continuity and achievement records under their separate live authority;
- repository-management metadata or owner-directed governance records;
- corrections to ChatGPT/Cline supervisory policy.

Required executor:

```yaml
executor: ChatGPT_connected_GitHub_app
Cline_task_required: false
Cline_prompt_for_the_update: prohibited
Human_Owner_exact_request_is_execution_authority_when_target_is_clear: true
```

For Class B, ChatGPT must not tell the Human Owner to send the work to Cline merely because the target is stored in the repository.

### Class C — Non-blueprint consequential technical change

This includes a requested change outside the active CrewAI blueprint that would modify:

- Galax runtime/source;
- tests as executable technical contracts;
- dependencies or lockfiles;
- workflows;
- secrets or credentials;
- repository security settings;
- production data;
- merge or deployment state;
- Agents 02–15.

Default result:

```yaml
executor: NONE_UNTIL_SEPARATELY_AUTHORIZED
send_to_Cline_just_because_it_is_technical: prohibited
ChatGPT_direct_write_by_inference: prohibited
required_result: factual_blocker_or_separate_exact_Human_Owner_and_repository_authority
```

A Class C request must not be converted into a Cline assignment merely to avoid the direct-update boundary.

## 4. Direct ChatGPT update procedure for Class B

When the Human Owner requests a clear Class B repository update:

```text
fetch live Galax router
→ verify the request is outside the active CrewAI blueprint implementation scope
→ read only the minimum authority and exact target files
→ verify target repository, branch/ref, and current HEAD
→ identify completed and LOCKED_ACCEPTED work that must be preserved
→ determine the smallest exact file set required for a consistent rule/update
→ perform the exact bounded write through the connected GitHub app
→ commit to the correct non-main branch
→ verify the resulting commit and branch head remotely
→ report the exact files and commit
→ stop
```

No Cline prompt, local Cline edit, Cline validation, or Cline Git task is part of this procedure.

## 5. Direct-command interpretation

When the Human Owner says an equivalent of:

```text
update this rule in my repo
update my repo with this governance change
change this ChatGPT rule
fix the repository instructions
save this non-blueprint repository update
```

and the exact current target is unambiguous from the live conversation plus repository evidence, the instruction is execution authority for the exact bounded Class B update.

ChatGPT must execute it directly through GitHub rather than drafting a Cline prompt.

When the target is materially ambiguous, ChatGPT must reconstruct the smallest repository context needed. It must not guess, broaden scope, or delegate the ambiguity to Cline.

## 6. Cline strict non-job rule

Cline must not be assigned work solely because a file is in the Galax repository.

The following are explicitly outside Cline's default job unless they are themselves an exact required deliverable of the active CrewAI remediation blueprint:

```yaml
Cline_prohibited_default_non_blueprint_jobs:
  - update_ChatGPT_router
  - update_ChatGPT_supervisory_skills
  - update_new_chat_operating_rules
  - update_length_problem_or_achievement_records
  - maintain_repository_memory_or_continuity
  - rewrite_repository_governance_for_ChatGPT
  - perform_owner_direct_documentation_updates
  - perform_generic_repository_housekeeping_updates
  - act_as_the_default_writer_for_every_repo_change
```

If ChatGPT is about to create a Cline task for any item above, it must stop and reclassify the request under this boundary first.

## 7. Existing Cline wording supersession

This rule intentionally narrows older wording such as:

```text
sole_primary_local_writer: Cline
Cline: sole primary local writer
all implementation and non-continuity work uses Cline
```

The corrected interpretation is:

```text
Cline = primary local writer for the active CrewAI remediation blueprint implementation work only.

ChatGPT = direct connected-GitHub writer for exact Human-Owner-authorized repository governance/documentation/supervisory updates outside that blueprint.
```

For non-blueprint repository updates, this rule supersedes conflicting broader Cline-writer wording in lower-priority plans, Skill 2 role descriptions, historical records, or old summaries.

It does not erase those records; it changes their current interpretation only where they conflict with this exact contributor boundary.

## 8. Protection boundaries remain active

Direct ChatGPT execution under this rule does not authorize broad or unsafe changes.

```yaml
direct_main_write: prohibited
force_push: prohibited
history_rewrite: prohibited
LOCKED_ACCEPTED_change_without_exact_unlock: prohibited
source_or_runtime_change_outside_blueprint_by_inference: prohibited
test_change_outside_blueprint_by_inference: prohibited
dependency_change_by_inference: prohibited
workflow_or_secret_change: prohibited
merge: prohibited_without_separate_Human_Owner_authorization
deployment: prohibited_without_separate_Human_Owner_authorization
Agents_02_to_15: prohibited_without_exact_live_authority
```

Every direct update must remain bounded to the Human Owner's exact request and the minimum files required to keep the governing rule internally consistent.

## 9. Current prompt-box governance task transition

The existing prompt-box-separation governance track is not CrewAI blueprint implementation.

Therefore:

```yaml
parent_assignment: GALAX_CHATGPT_CLINE_PROMPT_BOX_SEPARATION_PLAN_20260810_01
prior_Cline_contributor_assignment_for_governance_edit: superseded_by_this_boundary
prompt_box_rule_content_completed_by_this_rule: false
prompt_box_rule_still_incomplete: true
future_executor_if_Human_Owner_authorizes_that_governance_update: ChatGPT_connected_GitHub_app
future_Cline_task_for_that_governance_update: prohibited
```

This transition does not pretend the three-file prompt-box patch was previewed, saved, validated, committed, or completed. It only corrects who owns that non-blueprint governance work going forward.

## 10. Final strict rule

```text
Is the requested repository work an exact active CrewAI remediation-blueprint implementation task?
YES
→ use Cline under the normal bounded implementation controls.

NO
→ is it an exact Human-Owner-authorized governance/documentation/supervisory repository update?
YES
→ ChatGPT performs it directly through connected GitHub.

NO / consequential technical scope outside blueprint
→ block until exact separate authority exists.
```

Do not use Cline as a generic repository updater.
Do not make Cline maintain ChatGPT's governance system.
Do not delegate ChatGPT-owned repository rules back to Cline.
