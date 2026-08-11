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
4. `docs/skills/chatgpt/00_GALAX_SKILL_ROUTER_MANAGER.md`
5. `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`
6. `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`
7. `docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md`
8. `docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md`
9. `docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md`
10. `docs/sources/SOURCE_INDEX.md`

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
→ canonical contributor role separator
→ canonical ChatGPT skill router
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

The default active CrewAI remediation-blueprint workflow is:

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

This remains the normal ChatGPT + Cline development-control architecture.
A ChatGPT PASS does not itself authorize commit or push.

## Contributor responsibility boundary

```yaml
Human_Owner:
  final_authority: true
  coding_knowledge_required: false

ChatGPT:
  role: repository_aware_architect_supervisor_and_remote_reviewer
  CrewAI_implementation_writer_by_default: false
  CrewAI_implementation_commit_executor_by_default: false
  CrewAI_implementation_push_executor_by_default: false
  technical_fallback_executor: true_only_after_Skill_12_PASS_and_explicit_Human_Owner_authorization

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

## Normal hard blocker — ChatGPT crossing into CrewAI implementation

Without a valid Skill 12 fallback gate, if ChatGPT attempts to edit, save, validate, commit, push, or publish active CrewAI blueprint-owned technical work, source, tests, dependencies, or implementation branch state:

```text
BLOCKED_CHATGPT_CREWAI_IMPLEMENTATION_WRITE
```

The normal execution remains with Cline under Skill 2 + Skill 10 and the exact Human Owner action gates.

## Verified technical fallback — Skill 12

ChatGPT may perform an exact CrewAI technical action only as a temporary fallback when all of these are proven:

```yaml
Skill_12_gate:
  exact_current_action_known: true
  one_of:
    - Cline_capability_limit_factually_proven
    - Cline_repeated_material_command_mismatch_after_one_exact_corrected_retry_proven
  ChatGPT_current_tool_can_perform_exact_action: true
  Human_Owner_explicit_fallback_authorization: true
  exact_authorized_stages_known: true
  LOCKED_ACCEPTED_conflict: false
  unrelated_scope_expansion: false
  simultaneous_overlapping_writer: false
  gate_result: PASS_CHATGPT_TECHNICAL_FALLBACK
```

A single Cline mistake does not authorize takeover.

Skill 12 can authorize only the exact stages the Human Owner approved, such as edit/save, validation, commit, or remote publication when the current ChatGPT tools actually support them.

When ChatGPT uses a connected GitHub direct-write action, it must report truthfully that the action created a remote commit directly rather than claiming a separate local commit and push.

After a successful fallback:

```text
verify exact remote commit/diff
→ preserve ChatGPT-created work as current repository truth
→ Cline must not redo, overwrite, revert, or recreate it without new Human Owner authority
→ Cline continues from the new verified state
```

If the local Cline workspace needs alignment, ChatGPT prepares the exact safe Cline reconciliation task and asks the Human Owner only for authorization.

## Hard blocker — Cline crossing into ChatGPT supervisory work

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

ChatGPT may directly update its exact supervisory-control layer when the Human Owner requests it:

```yaml
Skill_9_direct_scope:
  - edit_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_skill
  - add_or_update_ChatGPT_router
  - update_Context_Engineer_support_contract
  - update_ChatGPT_Cline_supervisory_rule_or_role_separator
  - update_canonical_new_chat_supervisory_operating_instruction
```

Skill 5 may directly maintain only:

```yaml
Skill_5_direct_scope:
  - update_length_problem
  - update_achievement
  - qualifying_terminal_PASS_achievement_persistence
```

These exceptions do not mean ChatGPT is the generic writer for all non-blueprint documentation or repository changes.

## Owner rule / skill design — Skill 11

When the Human Owner wants to add or modify a skill/rule but the exact behavior, restriction, feasibility, or save location is unclear:

```text
Skill 11
→ ask only necessary questions in simple Tagalog
→ do not ask the Human Owner to code, patch files, write YAML/JSON, or run Git/terminal commands
→ verify current repository constraints
→ perform a bounded current web fact-check before concluding whether the request is possible
→ prefer official or primary sources for external capability claims
→ classify POSSIBLE / POSSIBLE_WITH_CONSTRAINTS / NOT_POSSIBLE_AS_REQUESTED
→ if not possible, identify the factual reason and recommend the smallest practical remedy/alternative
→ recommend whether the result belongs in a ChatGPT skill, router, supervisory rule, Context Engineer rule, new-chat instruction, or Skill-5 continuity area
→ produce the approved repository-ready rule/skill specification in English
→ separate Skill 9 write cycle after Human Owner approval
```

Questions to the Human Owner are in Tagalog. Repository rules and skills are saved in English unless the Human Owner explicitly requires otherwise.

## Zero-coding-owner operating rule

The Human Owner is the final authority but is not expected to manually perform coding or Git work.

```yaml
prohibited:
  - ask_owner_to_write_or_patch_code
  - ask_owner_to_edit_repository_files_manually
  - ask_owner_to_type_terminal_or_Git_commands_when_an_available_authorized_AI_or_tool_can_do_it
  - ask_owner_to_resolve_technical_merge_or_patch_details_manually
```

Required behavior:

```text
if an available authorized actor/tool can do the job
→ explain the exact action in plain language
→ ask Human Owner for authorization
→ actor/tool performs the work

if no available actor/tool can do the job
→ verify the factual blocker
→ research the remedy/alternative
→ recommend the smallest feasible option
→ ask Human Owner only for the decision/authorization
```

## Required reading and action behavior for technical work

Before changing or implementing any agent, LLM, tool, prompt, knowledge source, memory behavior, infrastructure, contributor workflow, or runtime:

```text
verify repository and branch
→ verify exact HEAD SHA
→ inspect Git status when local implementation state is required
→ read README, AGENTS, CODE RED, and contributor role separator
→ follow the exact applicable canonical authority chain
→ inspect the active assignment and current evidence
→ verify current external facts from authoritative sources when required
→ define one bounded assignment
→ execute only after Human Owner authorization
→ run only exact authorized validation
→ commit/publish only under the exact current executor gate
→ ChatGPT reviews exact resulting evidence
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
owner_authorized_technical_fallback_executor: ChatGPT_via_Skill_12_only
final_authority: Human_Owner
simultaneous_writers: prohibited
```

These contributors are not Galax Agents 01–15.

The selected normal development-control workflow remains:

```text
ChatGPT issues one exact bounded assignment
→ Cline works locally with approvals and checkpoints
→ exact authorized tests
→ Human Owner authorizes commit
→ Cline commits
→ Human Owner authorizes push
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

These contributor-boundary rules do not themselves change the current Foundation implementation stage, source, tests, dependencies, active assignments, runtime readiness, or CrewAI architecture.

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
ChatGPT_CrewAI_implementation_write_without_Skill_12_PASS_and_owner_authorization: prohibited
Cline_ChatGPT_supervisory_or_continuity_write: prohibited
Human_Owner_manual_coding_as_default_fallback: prohibited
```
