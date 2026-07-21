# Galax AI Repository Instructions for External Development Contributors

**Status:** `RESEARCH_BRANCH_INSTRUCTIONS_NOT_RUNTIME_AUTHORIZATION`  
**Applies to:** Cline, OpenHands Core, Aider, mini-SWE-agent, PR-Agent, Jules, Codex, and any other repository-aware development assistant.  
**Current authorized build scope:** Governance Foundation and Agent 01, Phases 0–4 only.  
**Agents 02–15:** disabled.  
**Merge and deployment:** prohibited.

## 1. Read before doing anything

Read these files in order and resolve conflicts using the newest applicable decision:

1. `README.md`
2. `AGENTS.md`
3. `docs/research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md`
4. `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`
5. all applicable files under `docs/rules/`
6. `docs/research/ai-tools/AI_DEVELOPMENT_CONTRIBUTOR_FINAL_QUALIFICATION_REVIEW_V3_2026-07-21.md`
7. `docs/plan/AI_DEVELOPMENT_CONTRIBUTOR_COORDINATION_PLAN_V2.md`
8. the selected contributor role card under `docs/ai-contributors/roles/`
9. the approved task packet
10. the authorized implementation prompt when the task concerns Foundation and Agent 01

Do not claim these files were read unless they were actually retrieved.

## 2. Repository truth

```yaml
repository: ariessocia04-rgb/galax-Ai-project
framework_target: CrewAI_1.15.4
current_runtime_agents_enabled: 0
current_implementation_scope: Foundation_and_Agent_01_only
research_base_branch: agent/agent-01-tool-inspection
approved_research_head: 897ded61c5edea4e6153112361c6e929f5a84294
implementation_branch: implementation/foundation-agent-01
```

Never use `main` as a fallback when another base branch or SHA is required.

## 3. External contributor boundary

External development tools are not Galax production agents.

```yaml
inside_CrewAI_runtime: false
may_control_Galax_Flow: false
may_enable_Agents_02_to_15: false
may_change_architecture_without_authorization: false
may_merge: false
may_deploy: false
```

## 4. One task, one writer

Only one source-writing contributor may own a task at a time.

```yaml
parallel_writers_on_same_task: prohibited
parallel_writers_on_overlapping_paths: prohibited
reviewer_source_write: prohibited
force_push: prohibited
automatic_merge: prohibited
direct_main_write: prohibited
account_rotation_to_evade_quota: prohibited
```

A fallback writer may begin only after the prior writer has stopped, produced a complete handoff, released the task lock, and the current branch SHA has been verified.

## 5. Task packet required

Do not edit files unless the task includes all of the following:

```yaml
task_id:
canonical_goal:
selected_contributor:
required_base_branch:
required_base_sha:
work_branch:
allowed_paths: []
protected_paths: []
required_reading: []
expected_outputs: []
acceptance_tests: []
security_negative_tests: []
maximum_changed_files:
maximum_diff_size:
maximum_cost_or_quota:
stop_conditions: []
required_handoff_fields: []
human_approver:
```

An incomplete packet produces:

```text
STATUS: BLOCKED_TASK_PACKET_INCOMPLETE
```

## 6. Assigned development roles

```yaml
Cline:
  role: SUPERVISED_PRIMARY_IMPLEMENTER
  writes: only_when_selected_as_single_writer

OpenHands_Core:
  role: DOCKER_ISOLATED_FALLBACK_IMPLEMENTER
  writes: only_after_prior_writer_stops

Aider:
  role: SURGICAL_FIX_AND_TEST_REPAIR_SPECIALIST
  writes: one_small_reproducible_fix_only

mini_SWE_agent:
  role: ISOLATED_PATCH_COMPARATOR
  writes_to_authoritative_branch: false

PR_Agent:
  role: READ_ONLY_PR_REVIEWER
  source_write: false
  merge_authority: false

Jules:
  role: CURRENT_HOSTED_REPOSITORY_OPERATOR
  status: outside_open_source_five

Codex:
  role: HOSTED_COMPLEX_IMPLEMENTER_OR_REVIEWER
  status: separately_selected_when_authorized_usage_exists
```

The exact rules for each selected open-source contributor are in `docs/ai-contributors/roles/`.

## 7. Required work method

```text
read rules
→ verify repository, branch, and SHA
→ inspect only relevant files
→ return a bounded plan
→ wait for approval when required
→ make the minimum sufficient change
→ run every required test
→ inspect the complete diff
→ produce evidence and handoff
→ stop
```

Do not activate CrewAI `planning=True`, `reasoning=True`, native memory, delegation, parallel agents, or any LLM profile as a substitute for this external work discipline.

## 8. Truth and evidence

Never fabricate:

- file contents;
- commands;
- tool calls;
- test results;
- commits;
- API responses;
- permissions;
- usage or cost;
- evidence IDs;
- completion status.

Do not provide hidden chain-of-thought. Provide a concise decision rationale, actions taken, evidence, commands, test results, blockers, and next safe action.

## 9. Immediate stop conditions

Stop without additional edits when any of these occurs:

```text
wrong repository
wrong branch
wrong starting SHA
missing required document
missing allowed-path declaration
request to write main/master
request to force push or merge
request to edit workflows or secrets without explicit authorization
unexpected files already modified
scope requires Agents 02–15
architecture or schema decision outside the approved task
security boundary cannot be enforced
quota or cost limit reached
required test cannot be run
```

Return an explicit blocker and safe remedy.

## 10. Required final handoff

Every completion, failure, interruption, or quota stop must return:

```yaml
repository:
task_id:
contributor:
role:
branch:
starting_sha:
current_sha:
working_tree_clean:
files_changed: []
files_untracked: []
commands_run: []
tests_run: []
requirements_completed: []
requirements_remaining: []
known_failures: []
security_observations: []
quota_or_cost_observed:
prohibited_actions_attempted: []
next_safe_action:
lock_release_status:
status:
```

A prose-only handoff is invalid.
