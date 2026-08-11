# Galax ChatGPT / Cline Execution Role Separator

**Status:** `ACTIVE_CANONICAL_HUMAN_OWNER_CONTRIBUTOR_BOUNDARY`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Canonical governance ref:** `docs/chatgpt-skill-router-2026-08-02`  
**Applies to:** ChatGPT, Cline, and every Galax repository-supervision workflow  
**Runtime effect:** none  
**CrewAI architecture change:** false  
**Final authority:** Human Owner

## 1. Purpose

This rule restores the Human Owner's original separation of duties.

The normal CrewAI implementation chain is exactly:

```text
Human Owner
   ↓
ChatGPT
→ decides WHAT should be done
→ gives one exact bounded command / Cline task
   ↓
Cline
→ executes the command locally
→ edits/saves only the authorized implementation scope
→ runs only separately authorized validation
   ↓
ChatGPT
→ reviews Cline's evidence
→ PASS / CHANGES_REQUIRED / BLOCKED
   ↓
Human Owner
→ authorizes the exact Git stage
   ↓
Cline
→ performs the separately authorized commit
→ performs the separately authorized push
   ↓
GitHub
   ↓
ChatGPT
→ independently reviews the exact remote diff / evidence
   ↓
Human Owner
→ final acceptance
```

This chain is the default for active CrewAI remediation-blueprint implementation. ChatGPT is the supervisor/reviewer, not the CrewAI implementation writer or implementation Git executor.

## 2. Exact responsibility split

```yaml
GALAX_CONTRIBUTOR_RESPONSIBILITY_BOUNDARY_V2:
  Human_Owner:
    final_authority: true
    approves_scope: true
    approves_save_when_required: true
    approves_validation: true
    approves_commit: true
    approves_push: true
    approves_merge: true
    approves_deployment: true

  ChatGPT:
    role: repository_aware_architect_supervisor_reviewer
    CrewAI_implementation_writer: false
    CrewAI_implementation_commit_executor: false
    CrewAI_implementation_push_executor: false
    final_acceptance_authority: false

    direct_repository_writer_only_for_supervisory_controls_and_continuity: true

  Cline:
    role: primary_local_executor_for_active_CrewAI_remediation_blueprint
    executes_ChatGPT_bounded_commands: true
    edits_and_saves_authorized_CrewAI_implementation: true
    runs_only_authorized_validation: true
    commit_executor_for_authorized_CrewAI_implementation: true
    push_executor_for_authorized_CrewAI_implementation: true
    ChatGPT_governance_writer: false
    continuity_writer: false
    self_authorization: prohibited

  GitHub:
    canonical_source_of_truth: true

  CrewAI:
    application_runtime_only: true
```

## 3. ChatGPT direct-write allowlist

ChatGPT may perform a repository write without Cline only when the exact Human Owner request belongs to the ChatGPT supervisory/continuity layer.

Allowed classes are limited to:

```yaml
CHATGPT_DIRECT_WRITE_ALLOWLIST_V1:
  - edit_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_skill_router
  - edit_or_update_ChatGPT_Context_Engineer_support_contract
  - edit_or_update_ChatGPT_Cline_supervisory_rule_or_role_separator
  - edit_or_update_new_chat_supervisory_operating_instruction
  - create_or_update_length_problem_checkpoint_under_Skill_5
  - create_or_update_achievement_record_under_Skill_5
```

Typical repository targets include:

```text
docs/skills/chatgpt/**
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
other exact ChatGPT/Cline supervisory rule files explicitly identified by the Human Owner
docs/operations/GALAX_NEW_CHAT_OPERATING_MANUAL.md
docs/operations/checkpoints/GALAX_LENGTH_PROBLEM_*.md
docs/operations/checkpoints/GALAX_ACHIEVEMENTS_FROM_START_TO_CURRENT_2026-07-28.md
```

The allowlist is purpose-based. A file is not ChatGPT-owned merely because it is Markdown or stored under `docs/`.

Generic plans, research, technical contracts, source, tests, dependencies, workflows, implementation evidence, and CrewAI architecture records are **not** automatically included.

## 4. Hard ChatGPT blocker for CrewAI implementation

ChatGPT must not directly edit, save, commit, push, or otherwise publish active CrewAI remediation-blueprint implementation or technical execution work.

Hard-blocked classes include:

```yaml
CHATGPT_CREWAI_WRITE_BLOCKLIST_V1:
  - active_CrewAI_remediation_blueprint
  - blueprint_owned_technical_contract_or_execution_plan
  - src_or_runtime_code
  - executable_tests
  - dependency_or_lockfile_change
  - implementation_branch_change
  - implementation_commit
  - implementation_push
  - workflow_or_secret_change
  - production_data_change
  - merge
  - deployment
  - Agents_02_to_15_activation_or_implementation_without_separate_live_authority
```

The active blueprint itself is specifically protected:

```text
docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
```

If ChatGPT is about to write or commit any CrewAI implementation or blueprint-owned technical target, return:

```text
BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE
```

Required correction:

```text
preserve the exact Human Owner request
→ route through the current Galax router
→ for active blueprint execution, use Skill 2 with mandatory Skill 10 gate
→ ChatGPT prepares the exact bounded command
→ Cline executes it
→ preserve the normal save / validation / commit / push / remote-review gates
```

Even explicit Human Owner authorization for a CrewAI implementation stage authorizes **Cline** to execute that bounded stage; it does not convert ChatGPT into the implementation writer or Git executor.

If the Human Owner explicitly wants to change this role boundary itself, that is a supervisory-rule change and may be handled by ChatGPT under this file. It is not implicit permission to edit CrewAI implementation.

## 5. Hard Cline blocker for ChatGPT supervisory work

Cline must not edit, save, commit, or push ChatGPT-owned supervisory/continuity work.

Hard-blocked Cline classes include:

```yaml
CLINE_SUPERVISORY_BLOCKLIST_V1:
  - ChatGPT_skill_create_edit_or_update
  - ChatGPT_router_create_edit_or_update
  - ChatGPT_Context_Engineer_contract_update
  - ChatGPT_Cline_supervisory_rule_update
  - new_chat_supervisory_operating_rule_update
  - length_problem_checkpoint_update
  - achievement_record_update
```

If a Cline task or permission request attempts one of these, return:

```text
BLOCKED_CLINE_SUPERVISORY_SCOPE
```

Required correction:

```text
retain all correct CrewAI implementation work unchanged
→ remove the supervisory/continuity target from the Cline task
→ route the exact supervisory request to Skill 9 or Skill 5 as applicable
→ do not make Cline reread or redo already-correct implementation work
```

## 6. CrewAI implementation action gates

For active CrewAI remediation-blueprint work, authorization remains stage-specific:

```text
PLAN ≠ ACT
ACT ≠ SAVE
SAVE ≠ VALIDATE
VALIDATE ≠ FIX
FIX ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE_ACCEPTANCE
REMOTE_ACCEPTANCE ≠ MERGE
MERGE ≠ DEPLOY
```

A PASS from ChatGPT after reviewing local evidence does not itself authorize commit or push.

Required sequence for Git publication:

```text
ChatGPT reviews local Cline evidence
→ PASS or CHANGES_REQUIRED
→ Human Owner separately authorizes commit
→ Cline commits
→ Human Owner separately authorizes push
→ Cline pushes
→ GitHub exposes exact remote evidence/diff
→ ChatGPT independently reviews the remote diff
→ Human Owner makes final acceptance decision
```

## 7. Request classification

Before any repository write, classify the exact work:

### Class A — Active CrewAI remediation-blueprint execution

Examples:

- Foundation or Agent 01 source implementation required by the active blueprint;
- blueprint-required executable tests;
- an exact technical correction under the current implementation assignment;
- exact blueprint-required validation;
- implementation `git status`, commit, push, or PR publication stage when separately authorized.

Required executor:

```yaml
executor: Cline
ChatGPT_role: command_and_review_only
Skill_2_required_for_real_Cline_task: true
Skill_10_gate_required: true
ChatGPT_direct_write: prohibited
```

### Class B-S — ChatGPT supervisory repository controls

Examples:

- edit/update/add a ChatGPT skill;
- edit/update/add the ChatGPT router;
- edit/update the Context Engineer support contract;
- edit/update the ChatGPT/Cline supervisory rules or role separator;
- edit/update the canonical new-chat supervisory operating instruction.

Required executor:

```yaml
executor: ChatGPT_connected_GitHub_app
Skill_9_required: true
Cline_task: prohibited
CrewAI_implementation_changed: false
```

### Class B-C — Continuity / achievement

Examples:

- `update length problem`;
- `update achievement`;
- mandatory qualifying terminal-PASS achievement persistence.

Required executor:

```yaml
executor: ChatGPT_connected_GitHub_app
Skill_5_required: true
Cline_task: prohibited
CrewAI_implementation_changed: false
```

### Class C — Other consequential or ambiguous work

Anything outside the above exact classes is blocked until an existing repository authority and the Human Owner identify the executor and bounded stage.

Do not broaden Class B-S into "all documentation" or "anything outside the blueprint."

## 8. Examples

```text
ChatGPT tries to edit or commit the CrewAI remediation blueprint
→ BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE

ChatGPT tries to edit src/galax/** or tests/**
→ BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE

Human Owner says "update this ChatGPT skill"
→ Skill 9
→ ChatGPT may update the exact skill on the non-main governance branch

Human Owner says "update length problem"
→ Skill 5
→ ChatGPT may create/publish the exact continuity record

Cline wants to edit ChatGPT rules or skills
→ BLOCKED_CLINE_SUPERVISORY_SCOPE

Cline wants to execute an exact current CrewAI implementation edit after Skill 10 PASS and Human Owner authorization
→ PROCEED under Skill 2

Cline wants to run the exact authorized validation
→ PROCEED only in the separately authorized validation stage

Cline wants to commit the exact passed CrewAI implementation after Human Owner commit authorization
→ PROCEED as Cline GIT_ONLY commit task

Cline wants to push the exact authorized implementation commit after separate Human Owner push authorization
→ PROCEED as Cline GIT_ONLY push task
```

## 9. Protection boundaries

```yaml
direct_main_write: prohibited
force_push: prohibited
history_rewrite: prohibited
LOCKED_ACCEPTED_change_without_exact_unlock: prohibited
workflow_or_secret_change_by_inference: prohibited
merge_without_separate_Human_Owner_authorization: prohibited
deployment_without_separate_Human_Owner_authorization: prohibited
simultaneous_overlapping_implementation_writers: prohibited
ChatGPT_and_Cline_same_implementation_change_as_writers: prohibited
```

ChatGPT direct supervisory writes must use the correct non-main governance or continuity branch and remain limited to the exact Human Owner request.

Cline implementation Git operations must use the exact active implementation branch/worktree and remain separately authorized.

## 10. Supersession

This rule supersedes the August 10 interpretation that broadly treated all non-blueprint governance/documentation/repository work as direct ChatGPT execution.

The restored interpretation is:

```text
ChatGPT = architect / supervisor / reviewer for CrewAI implementation.
Cline = local executor / implementation writer / authorized validator / authorized implementation commit-and-push executor.

ChatGPT direct GitHub writing exists only for the explicit supervisory-controls and continuity allowlists in Sections 3 and 7.
Cline is blocked from those ChatGPT-owned supervisory and continuity targets.
```

Older wording such as:

```text
ChatGPT = direct updater for every non-blueprint repository change
```

is superseded where it conflicts with this exact boundary.

The canonical ChatGPT → Cline control plan remains authoritative for the implementation workflow:

```text
docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md
```

## 11. Final strict rule

```text
Is this exact action a ChatGPT supervisory-control or Skill-5 continuity/achievement update?
YES
→ ChatGPT may execute only that exact allowlisted repository update.

NO
→ Is it exact active CrewAI remediation-blueprint execution?
YES
→ ChatGPT commands/reviews; Cline executes; Cline validates/commits/pushes only at separately authorized stages.

NO / ambiguous
→ BLOCK until exact authority and executor are proven.
```
