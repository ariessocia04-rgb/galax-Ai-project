```yaml
skill_reference: $galax-owner-direct-repository-update-guardian
skill_id: GALAX-SKILL-09
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 9: Galax ChatGPT Supervisory Repository Update Guardian

```yaml
skill_name: Galax ChatGPT Supervisory Repository Update Guardian
skill_type: ChatGPT_owner_authorized_supervisory_repository_update_skill
active_project: Galax_AI_only
repository: ariessocia04-rgb/galax-Ai-project
runtime_agent: false
CrewAI_agent: false
Galax_Agent_01_to_15: false
local_implementation_writer: false
CrewAI_implementation_git_executor_by_default: false
direct_connected_GitHub_writer_for_exact_supervisory_controls: true
technical_fallback_owned_here: false
approval_authority: false
final_authority: Human_Owner
```

## 1. One job only

Skill 9 exists so ChatGPT can maintain its own Galax supervisory control layer without sending that maintenance work to Cline.

```text
Human Owner requests an exact ChatGPT supervisory-control repository update
→ ChatGPT verifies the live router, role separator, exact target, branch and HEAD
→ ChatGPT writes only the exact allowlisted supervisory target through the connected GitHub app
→ ChatGPT verifies the resulting remote commit
→ stop
```

Skill 9 is not a generic non-blueprint repository writer and is not the technical fallback executor.

Canonical boundary:

```text
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
```

## 2. Activation triggers

Use Skill 9 when the Human Owner requests an exact already-defined supervisory update such as:

```text
edit this ChatGPT skill
update this ChatGPT skill
add this exact ChatGPT skill
update the ChatGPT router
add or update the skill router
update the Context Engineer rule
update the ChatGPT/Cline role separator
update this ChatGPT supervisory rule
update the new-chat supervisory operating instruction
```

If the Human Owner wants a new/changed rule or skill but the exact desired behavior, restrictions, feasibility, or destination is unclear:

```text
route to Skill 11 first
```

If the task is CrewAI technical execution after verified Cline failure/mismatch:

```text
route to Skill 12
```

Continuity and achievement remain Skill 5 work.

## 3. Exact direct-write allowlist

```yaml
GALAX_SKILL_9_DIRECT_WRITE_ALLOWLIST_V3:
  allowed_purposes:
    - ChatGPT_skill_create_edit_or_update
    - ChatGPT_router_create_edit_or_update
    - ChatGPT_Context_Engineer_support_contract_update
    - ChatGPT_Cline_supervisory_rule_or_role_separator_update
    - canonical_new_chat_supervisory_operating_instruction_update

  typical_allowed_paths:
    - docs/skills/chatgpt/**
    - docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
    - exact_other_ChatGPT_Cline_supervisory_rule_explicitly_named_by_Human_Owner
    - docs/operations/GALAX_NEW_CHAT_OPERATING_MANUAL.md
```

Path alone never grants authority. The exact purpose must also be supervisory.

A generic document, plan, research file, technical contract, blueprint, source file, test, dependency file, workflow, or implementation record is not Skill 9 work merely because it is outside `src/`.

## 4. Technical implementation is not Skill 9

Skill 9 must fail closed when the target is CrewAI implementation or blueprint-owned technical authority.

```yaml
GALAX_SKILL_9_CHATGPT_BLOCKLIST_V2:
  - docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md
  - blueprint_owned_technical_contract_or_execution_plan
  - src/**
  - tests/**
  - pyproject.toml
  - uv.lock
  - requirements_or_dependency_files
  - .github/workflows/**
  - implementation_branch_source_or_test_change
  - implementation_commit
  - implementation_push
  - merge
  - deployment
  - production_data
```

Required Skill 9 result:

```text
BLOCKED_NOT_SKILL_9_SCOPE
```

Then route based on current evidence:

```text
normal active CrewAI implementation and Cline can execute
→ Skill 2 + Skill 10

verified Cline capability block or repeated material mismatch after one corrected retry
→ prove ChatGPT exact capability
→ obtain Human Owner fallback authorization
→ Skill 12
```

Skill 9 itself must never be used to bypass the Skill 12 fallback gate.

## 5. Cline exclusion from Skill 9 work

```yaml
Cline_prohibited_for_Skill_9_targets:
  - edit_or_add_ChatGPT_skill
  - edit_or_add_ChatGPT_router
  - edit_Context_Engineer_contract
  - edit_ChatGPT_Cline_supervisory_rule
  - edit_new_chat_supervisory_operating_instruction
  - commit_or_push_those_supervisory_changes_as_a_Cline_task
```

Result:

```text
BLOCKED_CLINE_SUPERVISORY_SCOPE
```

Do not make Cline reread or redo correct CrewAI implementation work when removing an out-of-scope supervisory target.

## 6. Mandatory precheck

```yaml
GALAX_CHATGPT_SUPERVISORY_UPDATE_PRECHECK_V3:
  repository_verified: true | false
  router_verified: true | false
  role_separator_verified: true | false
  exact_Human_Owner_request_preserved: true | false
  exact_target_files_known: true | false
  target_branch_known: true | false
  target_branch_is_not_main: true | false
  current_target_branch_head_verified: true | false

  target_is_ChatGPT_supervisory_control: true | false
  target_is_continuity_or_achievement: true | false
  target_is_CrewAI_blueprint_or_implementation: true | false
  target_is_generic_documentation_or_plan: true | false
  target_is_source_or_test: true | false
  target_is_dependency_or_workflow: true | false
  owner_requirements_still_ambiguous: true | false

  LOCKED_ACCEPTED_conflict: true | false
  unrelated_scope_expansion: true | false

  executor:
    ChatGPT_Skill_9 |
    ChatGPT_Skill_5 |
    Skill_11_requirements_first |
    Cline_via_Skill_2_and_Skill_10 |
    ChatGPT_via_Skill_12 |
    NONE_BLOCKED

  safe_to_write: true | false
```

Skill 9 may write only when the exact target is a known ChatGPT supervisory control, owner requirements are sufficiently clear, target branch is not main, and no lock/scope conflict exists.

## 7. Minimum-change rule

For an authorized Skill 9 update:

1. Change only the smallest supervisory file set required by the Human Owner's exact request.
2. Preserve unrelated governance, technical contracts, source, tests, and history.
3. Never edit executable source/tests/dependencies/workflows under Skill 9.
4. Never write to `main`.
5. Never merge or deploy.
6. Never create a Cline task merely to maintain ChatGPT supervisory controls.
7. Verify every resulting GitHub commit remotely.
8. Stop after the exact supervisory update and receipt.

## 8. Direct-command interpretation

When the Human Owner gives an exact command such as:

```text
edit skill
update skill
add this skill
update skill router
update router
update this ChatGPT rule
fix this ChatGPT/Cline supervisory rule
```

and the exact supervisory target and requested behavior are already clear from current conversation plus live repository evidence, that instruction is execution authority for the exact Skill 9 update.

Do not convert it into a Cline task.

If requirements are materially unclear, route to Skill 11 instead of guessing.

## 9. Relationship to Skill 11

Skill 11 owns plain-language requirements gathering and feasibility verification when the Human Owner does not yet have a complete exact rule/skill specification.

```text
unclear new rule/skill request
→ Skill 11 asks minimal questions in Tagalog
→ fact-checks repo + current external capability using official/primary sources
→ recommends destination/remedy
→ produces English specification
→ Human Owner approves
→ separate Skill 9 cycle writes it
```

Skill 9 must not repeat Skill 11 questions when the approved specification already exists.

## 10. Relationship to Skill 12

Skill 12 owns the exceptional technical ChatGPT execution path after verified Cline failure or repeated command mismatch.

Skill 9 does not perform technical fallback edits, validation, implementation commits, or remote publication.

```text
technical fallback request
→ Skill 12
not Skill 9
```

## 11. Relationship to Skill 5

Skill 5 remains the only ChatGPT direct writer for:

```yaml
Skill_5_owned_direct_updates:
  - length_problem_checkpoint
  - achievement_record
  - qualifying_terminal_PASS_achievement_persistence
```

Skill 9 must route those exact requests to Skill 5.

## 12. Zero-coding-owner rule

Do not ask the Human Owner to write code, edit repository files, or type terminal/Git commands to accomplish a Skill 9 update.

If a required supervisory action is within current ChatGPT/GitHub capability, ask only for the needed plain-language decision/authorization and perform the action.

## 13. Required output

```yaml
GALAX_CHATGPT_SUPERVISORY_REPO_UPDATE_V3:
  repository: ariessocia04-rgb/galax-Ai-project
  executor: ChatGPT_connected_GitHub_app
  Human_Owner_request:
  classification: ChatGPT_supervisory_control_update
  authority_files_read: []
  target_branch:
  starting_head_sha:
  files_created: []
  files_modified: []
  files_deleted: []
  commit_shas: []
  final_branch_head_sha:

  Cline_task_created: false
  Skill_11_required_before_write: false
  Skill_12_used: false
  CrewAI_blueprint_changed: false
  CrewAI_runtime_changed: false
  source_changed: false
  tests_changed: false
  dependencies_changed: false
  workflows_or_secrets_changed: false
  LOCKED_ACCEPTED_changed: false
  merge_performed: false
  deployment_performed: false

  blockers: []
  status: PASS | BLOCKED | FAIL
```

## 14. Blockers

```text
BLOCKED_DIRECT_UPDATE_BOUNDARY_UNAVAILABLE
BLOCKED_DIRECT_UPDATE_TARGET_AMBIGUOUS
BLOCKED_DIRECT_UPDATE_BRANCH_UNVERIFIED
BLOCKED_DIRECT_UPDATE_MAIN_PROHIBITED
BLOCKED_NOT_SKILL_9_SCOPE
BLOCKED_CLINE_SUPERVISORY_SCOPE
BLOCKED_DIRECT_UPDATE_LOCK_CONFLICT
BLOCKED_DIRECT_UPDATE_SCOPE_EXPANSION
BLOCKED_DIRECT_UPDATE_GITHUB_WRITE_FAILED
BLOCKED_DIRECT_UPDATE_POST_WRITE_VERIFICATION_FAILED
```

## 15. Terminal PASS behavior

A genuinely new completed Skill 9 supervisory update may return terminal `PASS` only after exact remote commit and branch head are verified.

A qualifying terminal PASS remains subject to the router's separate Skill 5 achievement-persistence cycle.

## 16. Final contract

```text
exact known Human Owner supervisory control update
→ Skill 9
→ ChatGPT direct bounded governance-branch update
→ verify remote commit
→ stop

unclear new skill/rule/restriction/location/feasibility
→ Skill 11 first

length problem / achievement
→ Skill 5

normal CrewAI implementation
→ Skill 2 + Skill 10

verified Cline failure/mismatch + ChatGPT capability + owner fallback authorization
→ Skill 12

anything else
→ BLOCK until exact authority/executor is proven
```
