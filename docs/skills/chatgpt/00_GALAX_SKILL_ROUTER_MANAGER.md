# Galax ChatGPT Skill Router Manager

**Status:** `ACTIVE_CHATGPT_ROUTING_CONTROL`  
**Repository:** `ariessocia04-rgb/galax-Ai-project`  
**Scope:** ChatGPT skill selection and selective repository reading only  
**Runtime effect:** none  
**CrewAI Flow routing changed:** false  
**Galax source or tests changed:** false  
**Final authority:** Human Owner  

## 1. Purpose

This document defines the ChatGPT routing layer for Galax AI.

Its job is to prevent ChatGPT from reading every Galax skill and scanning the entire repository for every request. It classifies the Human Owner's current request, selects exactly one primary installed Galax skill, loads no more than two genuinely required dependency skills, ignores unrelated skills, and then hands the task to the selected skill.

This router is a routing registry and selection policy only. It does not copy or replace the full instructions of Skills 1–7.

It does not implement or modify:

- the CrewAI `@router` architecture;
- `GalaxFoundationFlow`;
- Agent 01 or Agents 02–15;
- source code or tests;
- Cline software;
- GitHub workflows, secrets, permissions, merge, or deployment;
- the authority of the Human Owner.

## 2. Installed Galax skill references

The router may select only these installed skills:

```text
$galax-repository-state-scope-guardian
$galax-strict-cline-prompt-guardian
$galax-evidence-validation-acceptance-guardian
$galax-draft-pr-exact-diff-reviewer
$galax-continuity-achievement-guardian
$galax-locked-artifact-guardian
$galax-repository-cleanup-auditor
```

The router must not invent another Galax skill, silently substitute a general skill, or load all seven skills by default.

## 3. Router-first policy

For every Galax request:

```text
classify the current request
→ select exactly one primary installed skill
→ select zero to two required dependency skills
→ ignore all unrelated skills
→ let the selected skill determine the minimum repository evidence required
→ complete only the current bounded task
→ stop
```

Rules:

```yaml
primary_skill_limit: 1
dependency_skill_limit: 2
read_all_skills: false
copy_skill_contents_into_router: false
automatic_next_skill: false
Human_Owner_final_authority: true
```

The router itself is not required to be the only skill loaded in the conversation. Its requirement is router-first selection: before unrelated Galax skills influence the task, the router identifies the one primary skill and any necessary dependencies, and unrelated skills are disregarded.

## 4. Routing categories

Classify the Human Owner's request as one of:

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
  purpose: handle_three_hour_continuity_or_separate_achievement_check

LOCKED_ARTIFACT:
  purpose: protect_or_review_a_change_to_LOCKED_ACCEPTED_work

CLEANUP_AUDIT:
  purpose: classify_duplicates_conflicts_references_and_cleanup_candidates

UNKNOWN_OR_MULTI_TASK:
  purpose: stop_when_no_single_safe_primary_skill_can_be_selected
```

## 5. Primary skill routing table

| Human Owner request | Primary installed skill |
|---|---|
| Where did Galax stop, what is current, or what is next? | `$galax-repository-state-scope-guardian` |
| Make the next Cline prompt or review a Cline permission request | `$galax-strict-cline-prompt-guardian` |
| Review a proposed edit, saved receipt, focused test, commit, or push evidence | `$galax-evidence-validation-acceptance-guardian` |
| Review a current remote Draft PR or exact pushed diff | `$galax-draft-pr-exact-diff-reviewer` |
| Handle length problem, three-hour checkpoint, or separate achievement check | `$galax-continuity-achievement-guardian` |
| Determine whether accepted work is locked or review an unlock request | `$galax-locked-artifact-guardian` |
| Audit duplicates, stale conflicts, references, or deletion candidates | `$galax-repository-cleanup-auditor` |

## 6. Conditional dependency rules

A dependency is loaded only when its condition is true.

### Repository-state dependency

Load `$galax-repository-state-scope-guardian` as a dependency only when:

- the conversation is new or resumed after context loss;
- the active branch, exact HEAD SHA, assignment, stop point, or evidence is unclear;
- the primary skill requires live reconstruction;
- repository evidence conflicts with chat memory;
- the Human Owner invokes `CODE RED`, `length problem`, or equivalent continuation language.

Do not load it merely because repository work is mentioned when the exact current state is already verified for the present task.

### Locked-artifact dependency

Load `$galax-locked-artifact-guardian` only when:

- a proposed task, PR, cleanup candidate, test, or command may touch accepted work;
- an unlock request is being reviewed;
- the exact lock status is materially relevant to the current decision.

### Maximum dependency rule

```yaml
maximum_dependencies: 2
third_dependency_needed: BLOCKED_SCOPE_TOO_BROAD
required_action: split_into_separate_bounded_task
```

## 7. Selective repository reading policy

The router does not authorize a full-repository read.

After routing, the selected skill must use the smallest evidence path sufficient for the current task.

Default reading strategy:

```text
read the current authoritative entry point required by the selected skill
→ read the exact active plan, assignment, checkpoint, test, file, issue, or PR needed
→ follow only mandatory references from a higher-authority record
→ stop reading when the current task can be decided safely
```

Do not:

- read every file under `docs/`;
- read all plans, rules, checkpoints, skills, or history by default;
- scan all source and tests when one exact file or test is named;
- search the entire repository when an exact path is already known;
- reread completed evidence without a new factual reason;
- rely on filename similarity when exact content or authority is required.

Expand repository reading only when:

- an exact file cannot be located;
- a higher-authority file explicitly requires another record;
- required evidence is missing or contradictory;
- the current assignment cannot be verified safely;
- a reference or dependency must be proven.

Missing evidence returns a factual blocker. It never authorizes guessing or a broad repository scan.

## 8. Search, save, and edit determination

The router does not directly search, save, edit, test, commit, push, merge, or deploy.

It decides which installed skill owns the decision.

```yaml
where_to_search:
  owner: selected_primary_skill
  rule: exact_file_or_narrow_scope_only

where_to_save:
  owner: $galax-strict-cline-prompt-guardian
  rule: exact_allowlisted_path_and_separate_save_authorization

what_to_edit:
  owner: $galax-strict-cline-prompt-guardian
  rule: one_exact_file_or_section_and_one_stop_condition

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

No routing decision grants permission for the later action itself.

## 9. Routing receipt

Before handing off to a selected skill, determine:

```yaml
GALAX_CHATGPT_SKILL_ROUTE_V1:
  request_summary:
  repository: ariessocia04-rgb/galax-Ai-project
  task_category:
  primary_skill:
  dependency_skills: []
  dependency_reasons: []
  unrelated_skills_ignored: []
  exact_current_output_required:
  repository_state_already_verified:
  route_status: SELECTED | BLOCKED_AMBIGUOUS | BLOCKED_MISSING_INSTALLED_SKILL | BLOCKED_SCOPE_TOO_BROAD
```

When the route is selected, load only the named primary skill and the listed dependencies.

## 10. Multi-stage request handling

When one request includes several stages, route only the first repository-authorized stage.

Examples:

```text
"Review the edit, test it, commit, and push"
→ primary skill: $galax-evidence-validation-acceptance-guardian
→ review current edit evidence only
→ test, commit, and push remain separate later tasks

"Make the prompt, let Cline edit, run tests, and publish"
→ primary skill: $galax-strict-cline-prompt-guardian
→ create one exact current Cline task only
→ no automatic Act, validation, commit, or push

"Audit duplicates and delete them"
→ primary skill: $galax-repository-cleanup-auditor
→ produce cleanup evidence and candidates only
→ deletion requires a separate bounded task and Human Owner authorization
```

Do not activate several primary skills to satisfy a broad request in one pass.

## 11. Stop and handoff behavior

After the selected skill returns the current result, stop.

```text
Skill 3 returns PASS
→ do not automatically prepare a commit task

Skill 4 returns PASS
→ do not automatically approve or merge the PR

Skill 5 prepares a checkpoint
→ do not automatically save, commit, or push

Skill 7 identifies deletion candidates
→ do not automatically delete or create cleanup commits
```

A new Human Owner instruction is required before routing the next stage.

## 12. Relationship to Galax runtime routing

This ChatGPT skill router is separate from the canonical CrewAI Flow routing.

```text
ChatGPT skill routing
≠ CrewAI Flow @router execution
≠ Cline tool permission flow
≠ GitHub branch or pull-request routing
```

This document must not change the active runtime invariant that every conditional Foundation stage uses explicit named CrewAI routes and that blocked, failed, unavailable, pending, rejected, or evidence-missing outcomes do not enter a success path.

## 13. Strict prohibitions

```yaml
copy_or_embed_Skills_1_to_7: prohibited
read_all_skills_by_default: prohibited
load_unrelated_skills: prohibited
multiple_primary_skills_for_one_task: prohibited
more_than_two_dependencies: prohibited
automatic_next_skill: prohibited
full_repository_scan_by_default: prohibited
infer_missing_path_or_authority: prohibited
invent_installed_skill: prohibited
modify_CrewAI_router: prohibited
modify_Galax_source_or_tests: prohibited
direct_repository_edit_by_router: prohibited
direct_test_execution_by_router: prohibited
direct_commit_or_push_by_router: prohibited
merge_or_deployment_by_router: prohibited
approve_for_Human_Owner: prohibited
self_authorization: prohibited
```

## 14. Failure behavior

Return a blocker when:

- no installed skill matches the current request;
- more than one independent primary task is present;
- more than two dependencies are genuinely required;
- the selected installed skill is unavailable;
- required repository evidence is missing;
- a route would conflict with a higher-authority Galax record;
- the Human Owner has not authorized the current action.

The safe response is to name the exact blocker and the smallest required remedy. Do not compensate by reading all skills, scanning the entire repository, or broadening scope.

## 15. Final routing contract

```text
Human Owner request
→ classify one current task
→ select one primary installed Galax skill
→ add no more than two required dependencies
→ ignore unrelated skills
→ selected skill reads only the minimum authoritative repository evidence
→ selected skill returns the exact current output
→ Human Owner decides any consequential action
→ stop
```
