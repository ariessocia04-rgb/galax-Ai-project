# Galax ChatGPT Skill Router Manager

**Status:** `ACTIVE_CHATGPT_ROUTING_CONTROL`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Canonical router ref:** `docs/chatgpt-skill-router-2026-08-02`  
**Canonical router path:** `docs/skills/chatgpt/00_GALAX_SKILL_ROUTER_MANAGER.md`  
**Runtime effect:** none  
**CrewAI Flow routing changed:** false  
**Galax source or tests changed:** false  
**Final authority:** Human Owner

## 1. Purpose

This router selects exactly one repository-backed Galax ChatGPT skill for the current bounded request, plus no more than two genuinely required dependency skills.

It also enforces the Human Owner's execution separation:

```text
CrewAI remediation-blueprint implementation
→ ChatGPT decides / commands / supervises / reviews
→ Cline executes locally
→ Cline edits/saves only authorized implementation
→ Cline runs only authorized validation
→ after separate Human Owner Git authorization, Cline commits and pushes
→ ChatGPT reviews exact remote GitHub evidence
→ Human Owner final acceptance

ChatGPT supervisory controls
→ ChatGPT may directly maintain only its exact supervisory allowlist through Skill 9

Length problem / achievement
→ ChatGPT may directly maintain only the exact Skill 5 continuity records
```

ChatGPT must never silently become the CrewAI implementation writer or implementation Git executor.
Cline must never silently become the ChatGPT supervisory/continuity writer.

## 2. Repository-backed skill loading contract

The `$galax-*` names are routing aliases backed by exact Markdown files in this repository/ref.

```yaml
skill_representation: repository_backed_markdown_document
native_plugin_registration_required: false
native_tool_registration_required: false
repository_mapping_required: true
load_method: fetch_exact_mapped_file_from_GitHub
registry_repository: ariessocia04-rgb/galax-Ai-project
registry_ref: docs/chatgpt-skill-router-2026-08-02
same_ref_as_router_required: true
```

To load a skill:

```text
resolve the exact alias below
→ fetch the mapped file from this same repository/ref
→ follow that file as the selected skill instruction
```

Return `BLOCKED_ROUTER_OR_SKILL_UNAVAILABLE` only when this router or an exact mapped required skill cannot be fetched.

## 3. Canonical skill registry

```yaml
GALAX_REPOSITORY_SKILL_REGISTRY_V2:
  repository: ariessocia04-rgb/galax-Ai-project
  ref: docs/chatgpt-skill-router-2026-08-02

  skills:
    $galax-repository-state-scope-guardian:
      skill_id: GALAX-SKILL-01
      path: docs/skills/chatgpt/01_GALAX_REPOSITORY_STATE_SCOPE_GUARDIAN.md

    $galax-strict-cline-prompt-guardian:
      skill_id: GALAX-SKILL-02
      path: docs/skills/chatgpt/02_GALAX_STRICT_CLINE_PROMPT_GUARDIAN.md

    $galax-evidence-validation-acceptance-guardian:
      skill_id: GALAX-SKILL-03
      path: docs/skills/chatgpt/03_GALAX_EVIDENCE_VALIDATION_ACCEPTANCE_GUARDIAN.md

    $galax-draft-pr-exact-diff-reviewer:
      skill_id: GALAX-SKILL-04
      path: docs/skills/chatgpt/04_GALAX_DRAFT_PR_EXACT_DIFF_REVIEWER.md

    $galax-continuity-achievement-guardian:
      skill_id: GALAX-SKILL-05
      path: docs/skills/chatgpt/05_GALAX_CONTINUITY_ACHIEVEMENT_GUARDIAN.md

    $galax-locked-artifact-guardian:
      skill_id: GALAX-SKILL-06
      path: docs/skills/chatgpt/06_GALAX_LOCKED_ARTIFACT_GUARDIAN.md

    $galax-repository-cleanup-auditor:
      skill_id: GALAX-SKILL-07
      path: docs/skills/chatgpt/07_GALAX_REPOSITORY_CLEANUP_AUDITOR.md

    $galax-new-chat-bootstrap-guardian:
      skill_id: GALAX-SKILL-08
      path: docs/skills/chatgpt/08_GALAX_NEW_CHAT_BOOTSTRAP_GUARDIAN.md

    $galax-owner-direct-repository-update-guardian:
      skill_id: GALAX-SKILL-09
      path: docs/skills/chatgpt/09_GALAX_OWNER_DIRECT_REPOSITORY_UPDATE_GUARDIAN.md

    $galax-cline-blueprint-scope-blocker:
      skill_id: GALAX-SKILL-10
      path: docs/skills/chatgpt/10_GALAX_CLINE_BLUEPRINT_SCOPE_BLOCKER.md
```

The router must not invent another skill, silently substitute a general skill, infer a different path, or load all skills by default.

## 4. Context Engineer support contract

The Context Engineer remains non-skill support:

```yaml
context_engineer_support_contract:
  path: docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md
  ref: docs/chatgpt-skill-router-2026-08-02
  registered_skill: false
  primary_skill: false
  dependency_skill: false
  counts_toward_primary_skill_limit: false
  counts_toward_dependency_skill_limit: false
  CrewAI_agent: false
  runtime_effect: none
```

Required relationship:

```text
Router chooses WHO owns the current ChatGPT workflow
→ Context Engineer prepares the minimum verified context
→ selected skill performs the bounded job
```

The Context Engineer may reduce duplicate/stale reads through its verified identity-based reuse rules, but may not skip a selected skill's mandatory read or authorization gate.

If the Context Engineer cannot be fetched, return `BLOCKED_CONTEXT_ENGINEER_UNAVAILABLE`.

## 5. Mandatory new-chat bootstrap

A Galax conversation is `NEW_OR_UNVERIFIED_CHAT` when no valid current `GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V1` exists or a material bootstrap invalidation occurred.

Required bootstrap cycle:

```text
fetch Router
→ primary Skill 8
→ dependency Skill 1
→ dependency Skill 2
→ Context Engineer support
→ Skill 8 reads docs/operations/GALAX_NEW_CHAT_OPERATING_MANUAL.md
→ reconstruct repository-backed goal, exact stop point, completed work, locks, rejected/superseded work, do-not-repeat state, Cline control method, and current contributor boundary
→ produce GALAX_NEW_CHAT_BOOTSTRAP_RECEIPT_V1
→ PASS only when safe_to_continue=true
→ preserve the exact original Human Owner request
→ start a separate normal routing cycle for that same request only
```

Skill 10 is not a third bootstrap dependency because bootstrap does not itself issue a real Cline task. Skill 10 becomes mandatory when the normal cycle actually selects Skill 2 for Cline execution.

## 6. Canonical execution separator

Always fetch/follow when executor ownership is material:

```text
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
```

### 6A. CrewAI lane — Cline execution

For exact active CrewAI remediation-blueprint implementation:

```yaml
ChatGPT:
  decide_and_command: true
  supervise_and_review: true
  direct_implementation_write: prohibited
  direct_implementation_commit: prohibited
  direct_implementation_push: prohibited

Cline:
  primary_local_executor: true
  implementation_edit_save: only_when_authorized
  validation: only_when_separately_authorized
  commit: only_when_separately_authorized
  push: only_when_separately_authorized

Human_Owner:
  final_authority: true
```

Required chain:

```text
Human Owner
→ ChatGPT exact bounded command
→ Cline execution/edit/save
→ ChatGPT evidence review
→ PASS / CHANGES_REQUIRED
→ Human Owner exact Git authorization
→ Cline commit
→ separate Human Owner push authorization
→ Cline push
→ GitHub remote evidence
→ ChatGPT exact remote diff review
→ Human Owner final acceptance
```

ChatGPT attempting to write, commit, or push CrewAI implementation must return:

```text
BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE
```

### 6B. ChatGPT supervisory lane — Skill 9

Skill 9 is **not** a generic non-blueprint writer.

It applies only to exact Human-Owner-requested ChatGPT supervisory control maintenance:

```yaml
Skill_9_scope:
  - edit_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_router
  - update_Context_Engineer_support_contract
  - update_ChatGPT_Cline_supervisory_rule_or_role_separator
  - update_canonical_new_chat_supervisory_operating_instruction
```

Cline must be blocked from those targets:

```text
BLOCKED_CLINE_SUPERVISORY_SCOPE
```

Generic docs, plans, research, technical contracts, blueprint files, source, tests, dependencies, workflows, and implementation Git actions are not automatically Skill 9 work.

### 6C. Continuity lane — Skill 5

Skill 5 owns the Human Owner's narrow direct ChatGPT continuity exceptions:

```yaml
Skill_5_scope:
  - update_length_problem
  - update_achievement
  - qualifying_terminal_PASS_achievement_persistence
```

Cline must not be used for those exact continuity writes.

## 7. Router-first normal cycle

After any required bootstrap:

```text
classify the exact Human Owner request
→ select exactly one primary skill
→ fetch that exact skill
→ select zero to two genuinely required dependencies
→ fetch only those dependencies
→ fetch Context Engineer support
→ prepare only minimum verified context
→ selected skill performs only its bounded job
→ do not automatically continue to another technical stage
→ if a new qualifying terminal PASS occurs, run the mandatory separate Skill 5 achievement-persistence cycle
→ stop
```

```yaml
primary_skill_limit: 1
dependency_skill_limit: 2
read_all_skills: false
automatic_next_skill: false
Human_Owner_final_authority: true
```

## 8. Routing categories

```yaml
NEW_CHAT_BOOTSTRAP:
  primary: $galax-new-chat-bootstrap-guardian

REPOSITORY_STATE:
  primary: $galax-repository-state-scope-guardian

CLINE_BLUEPRINT_EXECUTION_COMMAND_OR_PERMISSION:
  primary: $galax-strict-cline-prompt-guardian
  mandatory_dependency: $galax-cline-blueprint-scope-blocker

EVIDENCE_REVIEW:
  primary: $galax-evidence-validation-acceptance-guardian

DRAFT_PR_REVIEW:
  primary: $galax-draft-pr-exact-diff-reviewer

CONTINUITY_OR_ACHIEVEMENT:
  primary: $galax-continuity-achievement-guardian

LOCKED_ARTIFACT:
  primary: $galax-locked-artifact-guardian

CLEANUP_AUDIT:
  primary: $galax-repository-cleanup-auditor

CHATGPT_SUPERVISORY_CONTROL_UPDATE:
  primary: $galax-owner-direct-repository-update-guardian

UNKNOWN_OR_MULTI_TASK:
  result: BLOCKED_UNTIL_ONE_SAFE_PRIMARY_SCOPE_IS_PROVEN
```

## 9. Primary routing table

| Human Owner request | Primary skill | Important executor rule |
|---|---|---|
| First Galax request in new/unverified chat | Skill 8 | Bootstrap only; no technical execution |
| Where did Galax stop / current status / exact next safe action | Skill 1 | Read-only state reconstruction |
| Give Cline the next CrewAI task / review Cline permission | Skill 2 + mandatory Skill 10 | ChatGPT commands; Cline executes |
| Review local edit/test/commit/push evidence | Skill 3 | Review only; Human Owner decides next gate |
| Review exact remote Draft PR/diff | Skill 4 | ChatGPT independent remote review |
| Length problem / achievement / post-PASS persistence | Skill 5 | ChatGPT bounded continuity write only |
| Review `LOCKED_ACCEPTED` change/unlock | Skill 6 | No implicit unlock |
| Cleanup audit | Skill 7 | Audit only unless separately authorized |
| Edit/update/add ChatGPT skill/router/context/supervisory rule | Skill 9 | ChatGPT may write only exact supervisory allowlist |
| Cline scope classification for a real Cline task | Skill 10 dependency | PASS only exact active blueprint execution |

## 10. Mandatory Skill 10 gate for real Cline work

Before Skill 2 creates, continues, corrects, or authorizes a real Cline task:

```text
load Skill 10
→ prove exact blueprint trace
→ classify executor
→ require PASS_CLINE_BLUEPRINT_ONLY
→ only then allow Skill 2 to emit GALAX_CLINE_TASK_V2
```

Skill 10 must also block:

```text
ChatGPT tries to write/commit/push CrewAI blueprint implementation
→ BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE

Cline tries to write ChatGPT skills/router/supervisory rules/continuity
→ BLOCKED_CLINE_SUPERVISORY_SCOPE
```

There is no ChatGPT blueprint-edit exception.

## 11. Consequential-action separation

For Cline/CrewAI implementation:

```text
PLAN ≠ ACT
ACT ≠ SAVE
SAVE ≠ VALIDATION
VALIDATION ≠ FIX
FIX ≠ COMMIT
COMMIT ≠ PUSH
PUSH ≠ REMOTE_REVIEW
REMOTE_REVIEW ≠ HUMAN_ACCEPTANCE
HUMAN_ACCEPTANCE ≠ MERGE
MERGE ≠ DEPLOY
```

Each consequential stage requires its own current authority unless an exact higher-authority rule explicitly combines it.

A ChatGPT `PASS` after evidence review does not itself authorize Cline commit or push.

## 12. Mandatory post-PASS achievement persistence

When a bounded routing cycle returns a genuinely new qualifying terminal `PASS`, start a **separate routing cycle** with Skill 5 before any later technical stage.

```yaml
mandatory_post_PASS_achievement_persistence_cycle: true
mandatory_post_PASS_primary_skill: $galax-continuity-achievement-guardian
post_PASS_technical_continuation_before_persistence: prohibited
recursive_Skill_5_achievement: prohibited
```

This is a documentation-memory exception only. It does not authorize implementation, validation, implementation Git mutation, merge, or deployment.

## 13. Hard prohibitions

```yaml
prohibited:
  - full_repository_scan_by_default
  - read_all_skills_by_default
  - automatic_next_technical_stage
  - invent_branch_SHA_assignment_or_test_result
  - repeat_completed_or_LOCKED_ACCEPTED_work_without_new_reason
  - ChatGPT_direct_CrewAI_blueprint_or_implementation_write
  - ChatGPT_direct_implementation_commit_or_push
  - Cline_ChatGPT_skill_router_rule_or_continuity_write
  - Cline_self_authorization
  - implicit_commit_after_PASS
  - implicit_push_after_commit
  - direct_main_write
  - force_push
  - history_rewrite
  - merge_without_separate_Human_Owner_authorization
  - deployment_without_separate_Human_Owner_authorization
```

## 14. Final routing contract

```text
fetch live Router
→ bootstrap if required
→ preserve exact Human Owner request
→ classify exactly one current task

CrewAI blueprint execution?
→ Skill 2 + mandatory Skill 10
→ ChatGPT commands/reviews
→ Cline executes/validates/commits/pushes only at separately authorized stages

ChatGPT supervisory skill/router/context/rule maintenance?
→ Skill 9
→ ChatGPT may directly update only the exact supervisory target

length problem / achievement?
→ Skill 5
→ ChatGPT may directly update only the exact continuity target

anything else?
→ route to its exact mapped skill when proven, otherwise BLOCK

→ stop at the selected skill boundary
```
