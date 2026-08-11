# Galax AI Project

Galax AI is being designed as a fact-checked, strictly sequential CrewAI multi-agent software-development assistant system.

## Current phase

The repository is in planning, research, conflict-reconciliation, minimum-runtime validation, local Foundation setup, and controlled external-contributor coordination mode.

Agent roles, tools, LLMs, prompts, knowledge, memory, Docker infrastructure, contributor workflows, and execution behavior are not operational until individually implemented, tested, audited, and approved.

## Current readiness decision

```yaml
full_build_prompt_status: BLOCKED_NOT_READY_TO_PROMPT_CREWAI
current_master_prompt_status: DO_NOT_USE_STALE_CONFLICTS
Foundation_Agent01_Flow_contract: ACTIVE_CANONICAL
CODE_RED_protocol: ACTIVE_CANONICAL
ChatGPT_Cline_Draft_PR_control_plan: ACTIVE_CANONICAL
ChatGPT_Cline_execution_role_separator: ACTIVE_CANONICAL
production_ready: false
```

Do not execute the complete 15-agent build prompt.

The architecture is technically possible, but the exact CrewAI, LLM, GitHub/Drive/memory gateways, permission evidence, Docker/sandbox, sequential runtime chain, external contributor workflow, and live tests must pass their exact gates before production readiness can be claimed.

## Canonical current records

Read these first as applicable:

1. `AGENTS.md`
2. `docs/operations/CODE_RED.md`
3. `docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md`
4. `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`
5. `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`
6. `docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md`
7. `docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md`
8. `docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md`
9. `docs/sources/SOURCE_INDEX.md`

The legacy file:

```text
docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md
```

is a compatibility redirect to CODE RED.

## CODE RED trigger

When the owner says `CODE RED`, `code red`, `length chat problem`, `conversation length problem`, `continue exact Galax flow`, `operation length problem solve`, or a close spelling variation:

```text
read AGENTS.md
→ read docs/operations/CODE_RED.md completely
→ verify repository, relevant branch heads, draft PR, and assignment evidence
→ separate remote-proven facts from reported local-only facts
→ reconstruct decisions, completed actions, accepted work, rejected outputs, blockers, cleanup state, current stage, and one exact next allowed action
→ produce the required recovery receipt
→ answer or act only when safe_to_continue=true
```

Do not ask what the previous work was when repository access exists. Do not rely on old chat memory or summaries as repository truth.

## Canonical decision priority

```text
README current readiness
→ AGENTS.md
→ CODE RED
→ canonical conflict audit and alias target
→ Foundation and Agent 01 Flow execution contract
→ CrewAI 1.15.4 remediation blueprint
→ active rules and plans
→ source index and exact source cards
→ exact authorized assignment
→ current GitHub evidence
→ historical research
→ old chat memory or summaries
```

A lower-priority record cannot reactivate a superseded architecture or contributor boundary.

## Human Owner's canonical implementation workflow

For active CrewAI remediation-blueprint implementation, the repository uses this separation of duties:

```text
Human Owner
   ↓
ChatGPT
→ decides WHAT should be done
→ gives one exact bounded command / Cline task
   ↓
Cline
→ executes locally
→ edits/saves only the authorized implementation
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
→ commit
→ separately authorized push
   ↓
GitHub
   ↓
ChatGPT
→ independently reviews the exact remote diff/evidence
   ↓
Human Owner
→ final acceptance
```

This is the canonical meaning of the ChatGPT + Cline development-control architecture.

A ChatGPT PASS does not itself authorize commit or push.

## Contributor responsibility boundary

```yaml
Human_Owner:
  final_authority: true

ChatGPT:
  role: repository_aware_architect_supervisor_and_remote_reviewer
  CrewAI_implementation_writer: false
  CrewAI_implementation_commit_executor: false
  CrewAI_implementation_push_executor: false

Cline:
  role: primary_local_executor_for_active_CrewAI_remediation_blueprint
  implementation_writer: true_when_exactly_authorized
  validation_executor: true_when_separately_authorized
  implementation_commit_executor: true_when_separately_authorized
  implementation_push_executor: true_when_separately_authorized

GitHub:
  canonical_source_of_truth: true
```

Canonical separator:

```text
docs/rules/GALAX_CHATGPT_DIRECT_REPOSITORY_UPDATE_BOUNDARY.md
```

### Hard blocker — ChatGPT crossing into CrewAI implementation

If ChatGPT attempts to edit, save, commit, push, or publish:

- the active CrewAI remediation blueprint;
- a blueprint-owned technical contract/execution plan;
- `src/**` or runtime implementation;
- executable tests;
- dependencies or lockfiles;
- implementation branch Git state;
- implementation commit or push;

return:

```text
BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE
```

The execution must remain with Cline under the normal Skill 2 + Skill 10 controls and separate Human Owner action gates.

There is no ChatGPT blueprint-edit exception.

### Hard blocker — Cline crossing into ChatGPT supervisory work

Cline must not edit/save/commit/push:

- ChatGPT skills;
- ChatGPT router;
- Context Engineer supervisory contract;
- ChatGPT/Cline role-separator or other exact ChatGPT supervisory rules;
- length-problem checkpoints;
- achievement record.

Return:

```text
BLOCKED_CLINE_SUPERVISORY_SCOPE
```

## Narrow ChatGPT direct repository exceptions

ChatGPT may directly update only its exact supervisory-control layer when the Human Owner requests it:

```yaml
Skill_9_direct_scope:
  - edit_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_router
  - update_Context_Engineer_support_contract
  - update_ChatGPT_Cline_supervisory_rule_or_role_separator
  - update_canonical_new_chat_supervisory_operating_instruction
```

And Skill 5 may directly maintain only:

```yaml
Skill_5_direct_scope:
  - update_length_problem
  - update_achievement
  - qualifying_terminal_PASS_achievement_persistence
```

These exceptions do **not** mean ChatGPT is the generic writer for all non-blueprint documentation or repository changes.

## Required reading and action behavior for technical work

Before changing or implementing any agent, LLM, tool, prompt, knowledge source, memory behavior, infrastructure, contributor workflow, or runtime:

```text
verify repository and branch
→ verify exact HEAD SHA
→ inspect Git status when local implementation state is required
→ read README, AGENTS, and CODE RED
→ follow the exact applicable canonical authority chain
→ inspect the active assignment and current evidence
→ verify current external facts from authoritative sources when required
→ define one bounded assignment
→ execute only after Human Owner authorization
→ run only exact separately authorized validation
→ commit only after separate Human Owner commit authorization
→ push only after separate Human Owner push authorization
→ ChatGPT reviews the exact remote diff/evidence
→ Human Owner accepts or authorizes one exact correction
```

No contributor may infer missing permission.

## Meaning of 100% fact-checked

Galax does not promise perfect AI behavior.

The permitted statement is:

```text
100% of the defined documentation, source-code or adapter, compatibility,
security, and live execution tests passed for the exact pinned environment
and recorded date.
```

Any material fingerprint change returns affected capabilities to `REVALIDATION_REQUIRED`.

## Non-negotiable capability gate

```text
Never assign an agent or external contributor work that the complete verified runtime cannot perform.
```

A task requires verified support from the exact framework/version, role/task/output contract, LLM/provider when used, role interface, trusted dependencies/gateways, permissions/data classification, deterministic routing, required knowledge/memory, sandbox boundary when needed, governed executors/guardrails, applicable tests, and required human approval.

If a required layer is missing, incompatible, or unverified:

```text
STATUS: BLOCKED_UNSUPPORTED_CAPABILITY
```

The system must not simulate success, fabricate output, invent evidence, or claim content was studied when it was not retrieved.

## Active Foundation architecture

```yaml
RepositoryPreflightTool_owner: GalaxFoundationFlow
RepositoryPreflightTool_calls: 1
engineering_manager_tools: []
Agent_01_direct_tools: 0
Agent_01_LLM_calls: 1
Agent_01_output: AgentTaskResult
result_as_answer_for_this_path: prohibited
hidden_second_agent_call: prohibited
HumanReviewRequest: pure_Python_Pydantic
explicit_routers_for_every_branch: required
check_llm_profile_readiness_before_Agent_01: required
LLM_profiles_enabled: false
```

Offline `REPO_PERMISSION_PROFILE_DECLARED` remains separate from live `GITHUB_PERMISSIONS_LIVE_VALIDATED` evidence owned by `GitHubRepositoryGateway`.

## Current CrewAI direction

```yaml
framework_candidate: CrewAI_1.15.4
python_candidate: ">=3.10,<3.14"
process: Process.sequential
active_agent_count: 1
concurrent_LLM_calls: 1
planning: false
reasoning: false
memory: false
allow_delegation: false
allow_code_execution: false
async_tasks: false
parallel_tool_calls: false
respect_context_window: false
framework_status: SELECTED_FOR_PINNED_VALIDATION_NOT_APPROVED
```

CrewAI is the application agent/Flow framework. It is not the GitHub API, Google Drive API, database, Docker orchestrator, secure code sandbox, permission proof, or correctness guarantee.

## Foundation and Agent 01 sequence

```text
validate_run_manifest()
→ router
→ check_external_preflight_tool_availability()
→ router
→ invoke_repository_preflight_tool()
→ router
→ check_llm_profile_readiness()
→ router
→ run_agent_01_evaluation()
→ validate supported claims
→ router
→ build_human_review_request() with pure Python/Pydantic
→ authenticated human decision pause/router
→ complete_foundation_plan()
```

Every blocked, failed, unavailable, pending, rejected, or evidence-missing route must stop or pause.

## External development contributors

```yaml
primary_local_writer_and_executor: Cline
exact_failure_fixer: Aider_when_assigned
isolated_patch_comparator: mini-SWE-agent_when_assigned
Docker_fallback_reproducer: OpenHands_Core_when_assigned
read_only_PR_reviewer: PR-Agent_when_assigned
remote_architect_and_exact_diff_reviewer: ChatGPT
final_authority: Human_Owner
simultaneous_writers: prohibited
```

These contributors are not Galax Agents 01–15.

The selected development-control workflow is:

```text
ChatGPT issues one exact bounded assignment
→ Cline works locally with manual approvals and checkpoints
→ exact separately authorized tests
→ Human Owner separately authorizes commit
→ Cline commits
→ Human Owner separately authorizes push
→ Cline pushes to the implementation branch
→ Draft PR exposes the exact diff
→ ChatGPT reviews plan alignment, CrewAI compatibility, architecture, tests, security, regressions, and accepted-work preservation
→ Human Owner accepts or authorizes one exact correction
```

A file or stage accepted through exact remote review and Human Owner decision becomes `LOCKED_ACCEPTED`.

## Repository cleanup rule

Repository cleanup must follow CODE RED and the selected cleanup skill/rules.

```text
inventory
→ classify every file by purpose and authority
→ prove exact duplicate or unreferenced generated junk
→ migrate references
→ preserve unique historical evidence
→ run applicable checks
→ obtain Human Owner deletion authorization
→ delete
→ verify no broken references
→ record the result
```

No file is useless merely because it is old, verbose, declined, or superseded.

## Current technical status preservation

This contributor-boundary restoration does not itself change the current Foundation implementation stage, source, tests, dependencies, active assignments, runtime readiness, or CrewAI architecture.

Those facts must be reconstructed from current GitHub evidence, CODE RED, the latest valid continuity checkpoint, current assignments, and active branch/PR evidence rather than inferred from this README.

## Current authorization boundary

```yaml
main_write: prohibited
force_push: prohibited
history_rewrite: prohibited
merge: prohibited_without_separate_Human_Owner_authorization
deployment: prohibited_without_separate_Human_Owner_authorization
workflow_or_secret_change: prohibited
Agents_02_to_15: prohibited_without_exact_live_authority
production_ready_claim: prohibited
ChatGPT_CrewAI_implementation_write: prohibited
Cline_ChatGPT_supervisory_or_continuity_write: prohibited
```
