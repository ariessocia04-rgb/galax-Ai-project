# Galax ChatGPT Skill Router Manager

**Status:** `ACTIVE_CHATGPT_ROUTING_CONTROL`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Canonical router ref:** `docs/chatgpt-skill-router-2026-08-02`  
**Canonical router path:** `docs/skills/chatgpt/00_GALAX_SKILL_ROUTER_MANAGER.md`  
**Scope:** ChatGPT skill selection, context-engineering support, and selective repository reading only  
**Runtime effect:** none  
**CrewAI Flow routing changed:** false  
**Galax source or tests changed:** false  
**Final authority:** Human Owner

## 1. Purpose

This document defines the ChatGPT routing layer for Galax AI.

For every Galax request, it classifies the current task, selects exactly one primary repository-backed Galax skill document, loads no more than two genuinely required dependency skill documents, uses the canonical non-skill ChatGPT Context Engineer support contract to prepare the minimum verified context required by the already-selected skill, ignores unrelated skills and context, and completes only the current bounded task.

This router does not implement or modify:

- the CrewAI `@router` architecture;
- `GalaxFoundationFlow`;
- Agent 01 or Agents 02–15;
- Galax source code or tests;
- Cline software;
- GitHub workflows, secrets, permissions, merge, or deployment;
- the authority of the Human Owner.

## 2. Critical terminology and loading contract

The `$galax-*` names in this router are **routing aliases**. They are not required to be native ChatGPT plugins, native tool names, MCP tools, or separately installed runtime skills.

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

In this contract, **load a skill** means:

```text
resolve the selected $galax-* alias using the exact registry below
→ fetch the mapped Markdown file from the same repository and ref as this router
→ use that file as the selected skill instruction
```

Do not search for a native registered skill by alias when an exact repository mapping exists.

Do not return `BLOCKED_ROUTER_OR_SKILL_UNAVAILABLE` merely because the `$galax-*` alias is not registered as a native plugin or tool.

Return `BLOCKED_ROUTER_OR_SKILL_UNAVAILABLE` only when:

- this router cannot be fetched from the canonical repository/ref/path; or
- the exact mapped primary skill file cannot be fetched; or
- an exact mapped required dependency file cannot be fetched.

The Context Engineer is **not a skill alias**. It is one fixed ChatGPT supervisory support contract:

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

The Context Engineer may prepare context only after the router has selected the skill. It cannot select, replace, or activate a skill.

## 3. Canonical repository-backed skill registry

```yaml
GALAX_REPOSITORY_SKILL_REGISTRY_V1:
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
```

The exact registry above is authoritative for ChatGPT routing on this branch.

The router must not:

- invent another Galax skill;
- silently substitute a general skill;
- infer a different filename;
- search the repository by alias before using the mapped path;
- require native plugin installation when the mapped repository file is accessible;
- load all seven skill documents by default;
- register the Context Engineer as Skill 8 or any other skill;
- count the Context Engineer against the primary or dependency skill limits.

## 4. Router-first policy

For every Galax request:

```text
fetch this router from the canonical repository/ref/path
→ classify the current request
→ select exactly one primary skill alias
→ resolve the alias to its exact registry path
→ fetch the exact primary skill document
→ select zero to two genuinely required dependency aliases
→ resolve and fetch only those exact dependency documents
→ fetch the canonical Context Engineer support contract
→ use the Context Engineer to prepare only the minimum verified context required by the already-selected skill
→ ignore all unrelated skill documents and unrelated context
→ let the selected skill perform its own bounded job and any mandatory reads it still requires
→ complete only the current bounded task
→ when the bounded result is a new qualifying terminal PASS, perform the mandatory separate Skill 5 achievement-persistence routing cycle defined in Section 12A
→ stop
```

```yaml
primary_skill_limit: 1
dependency_skill_limit: 2
read_all_skills: false
copy_skill_contents_into_router: false
automatic_next_skill: false
mandatory_post_PASS_achievement_persistence_cycle: true
mandatory_post_PASS_cycle_is_separate_routing_cycle: true
mandatory_post_PASS_primary_skill: $galax-continuity-achievement-guardian
post_PASS_technical_continuation_before_persistence: prohibited
context_engineer_required_support_contract: true
context_engineer_registered_skill: false
context_engineer_counts_as_dependency: false
context_engineer_runtime_effect: none
Human_Owner_final_authority: true
```

`automatic_next_skill: false` continues to prohibit automatic movement into the next technical workflow stage. The mandatory post-PASS achievement-persistence cycle is a documentation-preservation exception backed by the live continuity standing authorization. It begins a new routing cycle with exactly one primary skill and does not authorize implementation, validation, Git mutation on an implementation branch, merge, or deployment.

### 4A. Context Engineer support rule

The Context Engineer is allowed to retrieve, filter, label, and package context only within the authority and reading boundaries of the selected skill and higher-authority repository records.

It must not weaken a selected skill's mandatory reading rule. It may prevent unrelated extra reads, duplicate history, stale context, or already-completed work from being loaded without a current factual reason.

Required relationship:

```text
router chooses WHO owns the current ChatGPT workflow
→ Context Engineer prepares WHAT verified context that owner needs
→ selected Skill decides HOW to perform its own authorized workflow
```

The Context Engineer cannot:

- determine repository truth instead of Skill 1;
- create Cline policy instead of Skill 2;
- accept evidence instead of Skill 3;
- review remote diffs instead of Skill 4;
- persist continuity instead of Skill 5;
- unlock accepted work instead of Skill 6;
- classify/delete cleanup targets instead of Skill 7.

If the Context Engineer support contract cannot be fetched from its exact canonical path and ref, stop with `BLOCKED_CONTEXT_ENGINEER_UNAVAILABLE`. Do not silently bypass it after this integration is active.

## 5. Routing categories

```yaml
REPOSITORY_STATE:
  purpose: reconstruct_current_Galax_state_and_next_safe_action

CLINE_PROMPT:
  purpose: create_or_review_one_exact_bounded_Cline_task

EVIDENCE_REVIEW:
  purpose: review_Cline_edit_validation_commit_or_push_evidence

DRAFT_PR_REVIEW:
  purpose: inspect_current_remote_PR_SHA_changed_files_and_patches

CONTINUITY_OR_ACHIEVEMENT:
  purpose: handle_three_hour_continuity_or_separate_achievement_check_or_mandatory_new_terminal_PASS_persistence

LOCKED_ARTIFACT:
  purpose: protect_or_review_a_change_to_LOCKED_ACCEPTED_work

CLEANUP_AUDIT:
  purpose: classify_duplicates_conflicts_references_and_cleanup_candidates

UNKNOWN_OR_MULTI_TASK:
  purpose: stop_when_no_single_safe_primary_skill_can_be_selected
```

## 6. Primary routing table

| Human Owner request | Primary skill alias | Exact repository path |
|---|---|---|
| Where did Galax stop, what is current, what is unfinished, or what is next? | `$galax-repository-state-scope-guardian` | `docs/skills/chatgpt/01_GALAX_REPOSITORY_STATE_SCOPE_GUARDIAN.md` |
| Make the next Cline prompt or review a Cline permission request | `$galax-strict-cline-prompt-guardian` | `docs/skills/chatgpt/02_GALAX_STRICT_CLINE_PROMPT_GUARDIAN.md` |
| Review a proposed edit, saved receipt, focused test, commit, or push evidence | `$galax-evidence-validation-acceptance-guardian` | `docs/skills/chatgpt/03_GALAX_EVIDENCE_VALIDATION_ACCEPTANCE_GUARDIAN.md` |
| Review a current remote Draft PR or exact pushed diff | `$galax-draft-pr-exact-diff-reviewer` | `docs/skills/chatgpt/04_GALAX_DRAFT_PR_EXACT_DIFF_REVIEWER.md` |
| Handle length problem, three-hour checkpoint, separate achievement check, or mandatory persistence of a new terminal PASS | `$galax-continuity-achievement-guardian` | `docs/skills/chatgpt/05_GALAX_CONTINUITY_ACHIEVEMENT_GUARDIAN.md` |
| Determine whether accepted work is locked or review an unlock request | `$galax-locked-artifact-guardian` | `docs/skills/chatgpt/06_GALAX_LOCKED_ARTIFACT_GUARDIAN.md` |
| Audit duplicates, stale conflicts, references, or deletion candidates | `$galax-repository-cleanup-auditor` | `docs/skills/chatgpt/07_GALAX_REPOSITORY_CLEANUP_AUDITOR.md` |

## 7. Exact skill-resolution algorithm

```text
selected alias
→ look up exact path in GALAX_REPOSITORY_SKILL_REGISTRY_V1
→ fetch that exact path from ariessocia04-rgb/galax-Ai-project
→ use ref docs/chatgpt-skill-router-2026-08-02
→ verify returned file exists and its declared skill_reference matches the selected alias
→ mark skill_load_status: LOADED_FROM_REPOSITORY
```

Required behavior:

```yaml
alias_found_and_file_fetched: continue
alias_found_but_file_fetch_failed: BLOCKED_ROUTER_OR_SKILL_UNAVAILABLE
alias_not_in_registry: BLOCKED_MISSING_REGISTERED_SKILL_MAPPING
native_plugin_missing_but_repository_file_fetched: continue
search_repository_by_alias_only: prohibited
```

A successful exact file fetch is sufficient to load the selected skill for this ChatGPT workflow.

### 7A. Exact Context Engineer resolution

After the primary and any required dependency skills are selected and fetched:

```text
fetch docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md
from ariessocia04-rgb/galax-Ai-project
using ref docs/chatgpt-skill-router-2026-08-02
→ verify Status is ACTIVE_CHATGPT_CONTEXT_SUPPORT_CONTRACT
→ verify Registered ChatGPT skill is false
→ verify CrewAI agent is false
→ use it only to prepare minimum verified context for the selected skill
```

Required behavior:

```yaml
context_contract_fetched_and_identity_valid: continue
context_contract_fetch_failed: BLOCKED_CONTEXT_ENGINEER_UNAVAILABLE
context_contract_claims_registered_skill_or_runtime_agent: BLOCKED_CONTEXT_ENGINEER_IDENTITY_MISMATCH
context_engineer_added_to_skill_registry: prohibited
context_engineer_added_to_dependency_list: prohibited
```

## 8. Conditional dependency rules

### Repository-state dependency

Load `$galax-repository-state-scope-guardian` only when:

- the conversation is new or resumed after context loss;
- the active branch, exact HEAD SHA, assignment, stop point, or evidence is unclear;
- the primary skill requires live state reconstruction;
- repository evidence conflicts with chat memory;
- the Human Owner invokes `CODE RED`, `length problem`, or equivalent continuation language.

Do not load it when the exact current state was already verified for the present bounded task.

### Locked-artifact dependency

Load `$galax-locked-artifact-guardian` only when:

- a proposed task, PR, cleanup candidate, test, or command may touch accepted work;
- an unlock request is being reviewed;
- exact lock status is materially relevant.

```yaml
maximum_dependencies: 2
third_dependency_needed: BLOCKED_SCOPE_TOO_BROAD
required_action: split_into_separate_bounded_task
```

The Context Engineer is not a dependency skill and must not consume a dependency slot.

## 9. Selective repository reading policy

The router does not authorize a full-repository read.

After routing, the selected skill and Context Engineer must use the smallest evidence path sufficient for the current task:

```text
read the current authoritative entry point required by the selected skill
→ read the exact active plan, assignment, checkpoint, test, file, issue, or PR required
→ follow only mandatory references from a higher-authority record
→ package only the minimum complete verified context
→ stop when the current task can be decided safely
```

Do not:

- read every file under `docs/`;
- read all plans, rules, checkpoints, skills, or history by default;
- scan all source and tests when one exact file or test is named;
- search the entire repository when an exact path is known;
- reread completed evidence without a new factual reason;
- rely on filename similarity when exact content or authority is required;
- load historical context merely because it exists;
- copy full conversation or repository history into every selected skill.

Expand reading only when:

- an exact required file cannot be located;
- a higher-authority file explicitly requires another record;
- required evidence is missing or contradictory;
- the current assignment cannot be verified safely;
- a reference or dependency must be proven;
- the selected skill explicitly requires the additional evidence.

Missing evidence produces a factual blocker. It never authorizes guessing or a broad repository scan.

## 10. Action ownership and authorization

The router and Context Engineer do not search broadly, save, edit, test, commit, push, merge, or deploy. The router identifies the skill that owns the current decision; the Context Engineer only prepares that skill's verified context.

```yaml
where_to_search:
  owner: selected_primary_skill
  context_engineer_role: package_only_within_selected_skill_boundaries
  rule: exact_file_or_narrow_scope_only

where_to_save_or_edit:
  owner: $galax-strict-cline-prompt-guardian
  rule: exact_allowlisted_path_and_separate_Human_Owner_authorization

how_to_review_edit_or_test:
  owner: $galax-evidence-validation-acceptance-guardian

how_to_review_remote_diff:
  owner: $galax-draft-pr-exact-diff-reviewer

how_to_handle_continuity:
  owner: $galax-continuity-achievement-guardian

how_to_protect_accepted_work:
  owner: $galax-locked-artifact-guardian

how_to_plan_cleanup:
  owner: $galax-repository-cleanup-auditor
```

A routing decision or context packet does not grant permission for a later consequential action.

## 11. Routing and load receipt

Before handing off, return or internally establish:

```yaml
GALAX_CHATGPT_SKILL_ROUTE_V2:
  request_summary:
  repository: ariessocia04-rgb/galax-Ai-project
  router_ref: docs/chatgpt-skill-router-2026-08-02
  router_path: docs/skills/chatgpt/00_GALAX_SKILL_ROUTER_MANAGER.md
  task_category:

  primary_skill_alias:
  primary_skill_path:
  primary_skill_load_status: LOADED_FROM_REPOSITORY | BLOCKED

  dependency_skill_aliases: []
  dependency_skill_paths: []
  dependency_load_statuses: []
  dependency_reasons: []

  context_engineer_path: docs/skills/chatgpt/context/00_GALAX_CHATGPT_CONTEXT_ENGINEER.md
  context_engineer_load_status: LOADED_SUPPORT_CONTRACT | BLOCKED
  context_engineer_registered_skill: false
  context_engineer_runtime_effect: none

  unrelated_skills_ignored: []
  exact_current_output_required:
  repository_state_already_verified:
  route_status:
    SELECTED |
    BLOCKED_AMBIGUOUS |
    BLOCKED_ROUTER_OR_SKILL_UNAVAILABLE |
    BLOCKED_CONTEXT_ENGINEER_UNAVAILABLE |
    BLOCKED_CONTEXT_ENGINEER_IDENTITY_MISMATCH |
    BLOCKED_SCOPE_TOO_BROAD
```

When the route is selected, load only the exact mapped primary/dependency skill files plus the one canonical Context Engineer support contract.

The selected skill may use `GALAX_CHATGPT_CONTEXT_PACKET_V1` from the Context Engineer when useful. Producing the full packet verbatim is not mandatory for trivial tasks if all required context and evidence boundaries are already explicit, but the Context Engineer's selection/protection rules still apply.

## 12. Multi-stage request handling

When one request includes several stages, route only the first repository-authorized stage.

Examples:

```text
"Review the edit, test it, commit, and push"
→ review current edit evidence only
→ test, commit, and push remain separate tasks

"Make the prompt, let Cline edit, run tests, and publish"
→ create one exact current Cline task only
→ no automatic Act, validation, commit, or push

"Audit duplicates and delete them"
→ produce cleanup evidence and candidates only
→ deletion requires a separate bounded task and Human Owner authorization
```

Do not activate multiple primary skills to satisfy one broad request.

The Context Engineer must not combine multiple workflow stages merely because their context is related.

## 12A. Mandatory terminal-PASS achievement persistence

Every new terminal `PASS` from a completed bounded Galax repository-supervision task is a mandatory achievement-persistence trigger before another technical task may begin.

This rule exists specifically to prevent completed PASS work from being forgotten, re-investigated, or restarted after conversation/context loss.

A qualifying event must satisfy all of:

```yaml
GALAX_TERMINAL_PASS_PERSISTENCE_TRIGGER_V1:
  source_primary_skill_is_repository_backed: true
  source_primary_skill_is_Skill_5: false
  terminal_status: PASS
  bounded_objective_completed: true
  new_material_result: true
  exact_evidence_available: true
  already_present_in_achievement_record: false
```

The following do **not** qualify as terminal PASS achievements:

- router `SELECTED` status;
- Cline permission `APPROVE` recommendations;
- pending approvals;
- plans or prompts merely prepared;
- unsaved previews;
- proposed diffs that have not reached their assigned completion boundary;
- `BLOCKED`, `FAIL`, `CHANGES_REQUIRED`, or equivalent non-PASS results;
- an identical PASS already persisted in the achievement record;
- Skill 5's own persistence result, which must never recursively create another achievement event.

Required routing sequence:

```text
current primary skill returns qualifying terminal PASS
→ freeze the exact completed result as DO_NOT_REPEAT evidence
→ stop that primary-skill routing cycle
→ start one new routing cycle with task_category CONTINUITY_OR_ACHIEVEMENT
→ select exactly one primary skill: $galax-continuity-achievement-guardian
→ load the Context Engineer support contract
→ verify the live achievement record, continuity branch, PR, exact PASS evidence, and duplicate status
→ append the new PASS achievement through Skill 5's authorized connected-GitHub path
→ verify the achievement commit remotely
→ stop the persistence cycle
→ only then may a later Human Owner instruction route the next technical stage
```

This mandatory persistence cycle is synchronous repository documentation in the active conversation. It is not background work and does not create a scheduler.

If a qualifying PASS cannot be persisted because repository access, branch/PR identity, evidence, timestamp, or duplicate verification cannot be established, return:

```text
BLOCKED_PASS_ACHIEVEMENT_PERSISTENCE
```

and do not automatically proceed to another technical workflow stage.

The achievement persistence cycle never authorizes:

- implementation edits;
- source or test changes;
- validation;
- Ruff or formatting;
- dependency changes;
- implementation Git actions;
- accepted-artifact unlock;
- merge;
- deployment;
- Agents 02–15.

## 13. Stop and handoff behavior

After the selected skill returns the current bounded result, stop except for the mandatory Section 12A achievement-persistence cycle when that result is a new qualifying terminal PASS.

```text
Skill 3 returns PASS
→ persist that new PASS through the mandatory separate Skill 5 cycle
→ do not automatically prepare a commit task

Skill 4 returns PASS
→ persist that new PASS through the mandatory separate Skill 5 cycle
→ do not automatically approve or merge the PR

Skill 5 prepares or persists continuity/achievement documentation
→ do not recursively create another achievement from Skill 5's own result
→ do not automatically enter a technical stage

Skill 7 identifies deletion candidates
→ do not automatically delete or create cleanup commits
```

A new Human Owner instruction is required before routing the next **technical** stage, except for an exact active standing authorization already present in the live repository. Section 12A is the mandatory documentation-persistence exception and does not count as automatic technical continuation.

A Context Engineer packet never creates technical continuation authority.

## 14. Relationship to Galax runtime routing

```text
ChatGPT repository-backed skill routing
≠ ChatGPT Context Engineer support layer
≠ CrewAI Flow @router execution
≠ Cline tool permission flow
≠ GitHub branch or pull-request routing
```

The Context Engineer exists only in the ChatGPT supervisory layer.

It must not be inserted into:

- `GalaxFoundationFlow`;
- Agent 01;
- Agents 02–15;
- CrewAI tasks;
- CrewAI tools;
- CrewAI runtime context;
- runtime memory;
- runtime knowledge;
- runtime prompts.

This router and Context Engineer must not change the active runtime invariant that every conditional Foundation stage uses explicit named CrewAI routes and that blocked, failed, unavailable, pending, rejected, or evidence-missing outcomes do not enter a success path.

## 15. Strict prohibitions

```yaml
copy_or_embed_full_Skills_1_to_7_into_router: prohibited
read_all_skills_by_default: prohibited
load_unrelated_skills: prohibited
multiple_primary_skills_for_one_task: prohibited
more_than_two_dependencies: prohibited
automatic_next_skill: prohibited
automatic_next_technical_skill_after_PASS_before_achievement_persistence: prohibited
full_repository_scan_by_default: prohibited
infer_unmapped_path: prohibited
search_by_alias_before_using_registry: prohibited
require_native_plugin_when_repository_file_is_accessible: prohibited
claim_repository_skill_file_is_missing_after_successful_fetch: prohibited
invent_skill_mapping: prohibited
modify_CrewAI_router: prohibited
modify_Galax_source_or_tests: prohibited
direct_test_execution_by_router: prohibited
merge_or_deployment_by_router: prohibited
approve_for_Human_Owner: prohibited
self_authorization: prohibited

register_Context_Engineer_as_skill: prohibited
create_Skill_8_for_Context_Engineer: prohibited
count_Context_Engineer_as_dependency: prohibited
create_Agent_16_for_Context_Engineer: prohibited
insert_Context_Engineer_into_CrewAI_runtime: prohibited
use_Context_Engineer_to_override_selected_skill: prohibited
use_Context_Engineer_to_skip_mandatory_selected_skill_evidence: prohibited
```

`automatic_next_skill: prohibited` refers to automatic continuation into another technical workflow stage. It does not cancel the mandatory Section 12A documentation-only Skill 5 persistence cycle because that cycle is a separate one-primary-skill routing cycle under the live achievement standing authorization.

## 16. Failure behavior

Use the smallest accurate blocker:

```yaml
BLOCKED_ROUTER_OR_SKILL_UNAVAILABLE:
  use_only_when:
    - canonical_router_fetch_failed
    - exact_mapped_primary_skill_fetch_failed
    - exact_mapped_required_dependency_file_fetch_failed
  required_details:
    - repository
    - ref
    - exact_failed_path

BLOCKED_CONTEXT_ENGINEER_UNAVAILABLE:
  use_when:
    - canonical_context_engineer_support_contract_fetch_failed
  required_details:
    - repository
    - ref
    - exact_failed_path

BLOCKED_CONTEXT_ENGINEER_IDENTITY_MISMATCH:
  use_when:
    - context_contract_claims_to_be_registered_skill
    - context_contract_claims_to_be_CrewAI_agent_or_runtime_component

BLOCKED_MISSING_REGISTERED_SKILL_MAPPING:
  use_when: selected_alias_is_not_present_in_the_exact_registry

BLOCKED_SCOPE_TOO_BROAD:
  use_when:
    - more_than_one_independent_primary_task
    - more_than_two_genuine_dependencies

BLOCKED_MISSING_EVIDENCE:
  use_when: selected_skill_loaded_but_required_task_evidence_is_missing

BLOCKED_PASS_ACHIEVEMENT_PERSISTENCE:
  use_when:
    - a_new_qualifying_terminal_PASS_exists
    - mandatory_Skill_5_persistence_cannot_be_verified_or_completed
```

Do not use `BLOCKED_ROUTER_OR_SKILL_UNAVAILABLE` when the exact mapped Markdown skill file was successfully fetched.

Do not bypass a missing Context Engineer contract by registering it as a skill or by inventing another path.

## 17. Final routing contract

```text
Human Owner request
→ fetch this exact router
→ classify one current task
→ select one primary skill alias
→ resolve the alias to its exact repository path
→ fetch the mapped primary skill document
→ resolve and fetch no more than two required dependency documents
→ fetch the one canonical non-skill Context Engineer support contract
→ Context Engineer prepares the minimum verified context required by the already-selected skill
→ ignore unrelated skills and unrelated context
→ selected skill performs only its own bounded job
→ if the result is a new qualifying terminal PASS, complete the separate mandatory Skill 5 achievement-persistence routing cycle
→ Human Owner decides any consequential next technical action
→ stop
```

```yaml
CrewAI_runtime_changed_by_this_router: false
GalaxFoundationFlow_changed_by_this_router: false
Agents_01_to_15_changed_by_this_router: false
CrewAI_remediation_plan_changed_by_this_router: false
Context_Engineer_runtime_effect: none
```