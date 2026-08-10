```yaml
skill_reference: $galax-owner-direct-repository-update-guardian
skill_id: GALAX-SKILL-09
native_plugin_skill: false
custom_GPT_knowledge_file: true
```

# Skill 9: Galax Owner Direct Repository Update Guardian

```yaml
skill_name: Galax Owner Direct Repository Update Guardian
skill_type: ChatGPT_owner_authorized_non_blueprint_repository_update_skill
active_project: Galax_AI_only
repository: ariessocia04-rgb/galax-Ai-project
runtime_agent: false
CrewAI_agent: false
Galax_Agent_01_to_15: false
local_implementation_writer: false
direct_connected_GitHub_writer_for_Class_B_updates: true
approval_authority: false
final_authority: Human_Owner
```

## 1. Purpose

This skill owns exact Human-Owner-authorized Galax repository updates that are outside the active CrewAI remediation blueprint implementation scope and are classified as Class B under:

```text
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
```

Its core rule is:

```text
Human Owner requests an exact non-blueprint repository governance/documentation/supervisory update
→ ChatGPT verifies the live repository and exact scope
→ ChatGPT writes the bounded update directly through the connected GitHub app
→ ChatGPT verifies the resulting commit remotely
→ stop
```

Do not create a Cline task merely because the requested update changes repository files.

## 2. Activation triggers

Use this skill as the primary skill when the Human Owner requests an exact repository update such as:

```text
update this rule in my repo
update my repo with this governance change
change the ChatGPT rule
fix the repository instructions
update the router or supervisory skills
save this documentation/governance update
```

and the requested change is outside the active CrewAI blueprint implementation scope.

Do not use this skill for:

- active CrewAI blueprint source/test implementation assigned to Cline;
- merge or deployment;
- secrets, credentials, security settings, or workflows;
- non-blueprint runtime/source/test/dependency changes that lack separate exact authority;
- continuity/achievement writes that are already owned by Skill 5.

## 3. Mandatory boundary read

Before any write, fetch and follow:

```text
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
```

Also read only the minimum exact authority and target files needed for the current update.

If the boundary file cannot be fetched from the canonical router ref, return:

```text
BLOCKED_DIRECT_UPDATE_BOUNDARY_UNAVAILABLE
```

## 4. Executor classification gate

Before writing, establish:

```yaml
GALAX_DIRECT_UPDATE_CLASSIFICATION_V1:
  requested_change:
  active_CrewAI_blueprint_scope:
  requested_change_is_blueprint_implementation: true | false
  requested_change_is_Class_B_non_blueprint_repo_update: true | false
  requested_change_is_Class_C_consequential_technical_change: true | false
  exact_Human_Owner_authorization_present: true | false
  executor: ChatGPT_connected_GitHub_app | Cline | NONE_BLOCKED
```

Required results:

```yaml
blueprint_implementation:
  executor: Cline
  this_skill_writes: false

Class_B:
  executor: ChatGPT_connected_GitHub_app
  Cline_task: prohibited

Class_C_without_separate_exact_authority:
  executor: NONE_BLOCKED
  Cline_task: prohibited
  ChatGPT_direct_write: prohibited
```

## 5. Direct-write precheck

A Class B write may proceed only when all are true:

```yaml
GALAX_OWNER_DIRECT_REPO_UPDATE_PRECHECK_V1:
  repository_verified: true
  router_verified: true
  boundary_rule_verified: true
  exact_Human_Owner_request_preserved: true
  exact_target_files_known: true
  target_branch_known: true
  target_branch_is_not_main: true
  current_target_branch_head_verified: true
  requested_scope_is_Class_B: true
  CrewAI_runtime_or_source_change: false
  executable_test_change: false
  dependency_change: false
  workflow_or_secret_change: false
  merge_or_deploy: false
  LOCKED_ACCEPTED_conflict: false
  unrelated_scope_expansion: false
  Cline_not_required: true
  safe_to_write: true
```

Any required false field blocks the write.

## 6. Minimum-change rule

For an authorized Class B update:

1. Change only the smallest file set required to make the Human Owner's rule internally consistent.
2. Preserve all unrelated text and repository history.
3. Do not rewrite source/tests/runtime merely because they reference the same topic.
4. Do not modify `LOCKED_ACCEPTED` without a separate exact unlock.
5. Do not write to `main`.
6. Do not merge or deploy.
7. Do not create a Cline task for the update.
8. Do not run tests, Ruff, formatting, or dependency commands unless a separate exact authority requires them.
9. Verify every resulting GitHub commit remotely.

## 7. Direct-command authority

When the Human Owner's current instruction clearly names the repository update and the target can be resolved from live repository evidence, that instruction is execution authority for the exact Class B change.

ChatGPT must not respond with a Cline prompt instead of performing the authorized update.

If the target is ambiguous, reconstruct only the minimum repository context needed. Do not delegate target discovery to Cline by default.

## 8. Cline non-delegation rule

```yaml
Cline_non_delegation:
  update_ChatGPT_router: prohibited_for_Class_B
  update_ChatGPT_skills: prohibited_for_Class_B
  update_ChatGPT_operating_manual: prohibited_for_Class_B
  update_repository_governance: prohibited_for_Class_B
  update_continuity_or_achievement: prohibited_here_and_owned_by_Skill_5
  generic_owner_direct_documentation_update: prohibited_for_Cline
```

Cline remains the primary local writer for the active CrewAI blueprint implementation work only.

## 9. Required output

After execution, return:

```yaml
GALAX_OWNER_DIRECT_REPO_UPDATE_V1:
  repository: ariessocia04-rgb/galax-Ai-project
  executor: ChatGPT_connected_GitHub_app
  Human_Owner_request:
  classification: Class_B_non_blueprint_repository_update
  authority_files_read: []
  target_branch:
  starting_head_sha:
  files_created: []
  files_modified: []
  files_deleted: []
  commit_shas: []
  final_branch_head_sha:
  Cline_task_created: false
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

## 10. Blockers

Use the smallest accurate blocker:

```text
BLOCKED_DIRECT_UPDATE_BOUNDARY_UNAVAILABLE
BLOCKED_DIRECT_UPDATE_TARGET_AMBIGUOUS
BLOCKED_DIRECT_UPDATE_BRANCH_UNVERIFIED
BLOCKED_DIRECT_UPDATE_MAIN_PROHIBITED
BLOCKED_DIRECT_UPDATE_NOT_CLASS_B
BLOCKED_DIRECT_UPDATE_LOCK_CONFLICT
BLOCKED_DIRECT_UPDATE_SCOPE_EXPANSION
BLOCKED_DIRECT_UPDATE_GITHUB_WRITE_FAILED
BLOCKED_DIRECT_UPDATE_POST_WRITE_VERIFICATION_FAILED
```

Do not convert a blocker into a Cline assignment unless the request is independently proven to be an active CrewAI blueprint implementation task.

## 11. Terminal PASS behavior

A genuinely new completed Class B direct repository update may return terminal `PASS` only after the final remote commit and branch head are verified.

A qualifying new terminal PASS is then subject to the router's normal separate Skill 5 achievement-persistence rule. That documentation cycle does not authorize another technical or repository update.

## 12. Final contract

```text
exact Human Owner non-blueprint repo-update request
→ Router selects Skill 9
→ read direct-update boundary
→ verify exact Class B scope and live branch/head
→ no Cline handoff
→ ChatGPT writes only the minimum exact files through connected GitHub
→ verify remote commit and branch head
→ return factual receipt
→ if qualifying new terminal PASS, persist it separately through Skill 5
→ stop
```
