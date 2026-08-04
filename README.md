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
remote_Foundation_repository_implementation: NOT_PUBLISHED
reported_local_Foundation_setup: PARTIALLY_COMPLETED_UNPUSHED
local_file_state_after_keyboard_incident: UNVERIFIED
full_free_runtime_proven: false
agents_enabled: 0
external_contributors_fully_qualified: 0
production_ready: false
```

Do not execute the complete 15-agent build prompt.

The architecture is technically possible, but the exact CrewAI, LLM, GitHub/Drive/memory gateways, permission evidence, Docker/sandbox, sequential runtime chain, external contributor workflow, and live tests have not passed all required gates.

## Canonical current records

Read these first:

1. `AGENTS.md`
2. `docs/operations/CODE_RED.md`
3. `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`
4. `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`
5. `docs/plan/CHATGPT_CLINE_DRAFT_PR_EXECUTION_CONTROL_PLAN_2026-07-22.md`
6. `docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md`
7. `docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md`
8. `docs/sources/SOURCE_INDEX.md`

The legacy file:

```text
docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md
```

is a temporary compatibility redirect to CODE RED.

## CODE RED trigger

When the owner says `CODE RED`, `code red`, `length chat problem`, `conversation length problem`, `continue exact Galax flow`, `operation length problem solve`, or a close spelling variation:

```text
read AGENTS.md
→ read docs/operations/CODE_RED.md completely
→ verify repository, branch heads, draft PR, and assignment issues
→ separate remote-proven facts from reported local-only facts
→ reconstruct all decisions, completed actions, accepted work, rejected outputs, blockers, cleanup state, current stage, and next allowed action
→ produce CODE_RED_RECEIPT_V1
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

The active Flow execution contract supersedes only older instructions that attach `RepositoryPreflightTool` directly to Agent 01, require an Agent 01 direct tool call, or use `result_as_answer` for that path.

Historical files remain evidence unless a cleanup audit proves they are exact duplicates or safely removable unreferenced junk.

## Required reading and action behavior

Before changing or implementing any agent, LLM, tool, prompt, knowledge source, memory behavior, infrastructure, contributor workflow, or runtime:

```text
verify repository and branch
→ verify exact HEAD SHA
→ inspect Git status
→ read README, AGENTS, and CODE RED
→ follow the full canonical reading order
→ inspect the active draft PR and assignments
→ verify current external facts from authoritative sources when required
→ produce REPOSITORY_READ_RECEIPT
→ define one bounded assignment
→ execute only after human authorization
→ run exact tests
→ publish only after separate commit and push authorization
→ ChatGPT reviews the exact draft-PR diff
→ human accepts or authorizes one exact correction
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

A task requires verified support from:

```text
CrewAI framework and exact version
+ exact role, prompt, task, and output contract
+ exact LLM/provider profile when an LLM is used
+ exact role interface according to the active contract
+ trusted Flow/application dependencies when external actions are not agent-owned
+ permissions and data classification
+ deterministic routers and stage ordering
+ knowledge and memory context when required
+ Docker/sandbox boundary when required
+ hooks or governed executors, guardrails, invocation evidence, and checkpoint
+ deterministic and applicable live tests
+ human approval when required
```

If any layer is missing, incompatible, or unverified:

```text
STATUS: BLOCKED_UNSUPPORTED_CAPABILITY
```

The system must not simulate success, fabricate tool output, invent missing evidence, or claim content was studied when it was not retrieved.

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

Offline `REPO_PERMISSION_PROFILE_DECLARED` is separate from live `GITHUB_PERMISSIONS_LIVE_VALIDATED` evidence owned by `GitHubRepositoryGateway`.

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

CrewAI is the agent/Flow framework. It is not the GitHub API, Google Drive API, database, Docker orchestrator, secure code sandbox, permission proof, or correctness guarantee.

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
primary_local_writer: Cline
exact_failure_fixer: Aider_when_assigned
isolated_patch_comparator: mini-SWE-agent_when_assigned
Docker_fallback_reproducer: OpenHands_Core_when_assigned
read_only_PR_reviewer: PR-Agent_when_assigned
remote_architect_and_exact_diff_reviewer: ChatGPT
final_authority: Human_Owner
simultaneous_writers: prohibited
```

These contributors are not Galax Agents 01–15.

## GitHub and accepted-work direction

The selected development-control workflow is:

```text
ChatGPT issues one exact bounded assignment
→ Cline works locally with manual approvals and checkpoints
→ exact tests
→ separately authorized commit
→ separately authorized push
→ Draft PR exposes the exact diff
→ optional external review layer according to the Stage 1 policy
→ when both reviewers are selected: PR-Agent then Codex sequentially
  against the same unchanged current PR head
→ ChatGPT canonical exact-diff review and receipt reconciliation
→ ChatGPT returns PASS, CHANGES_REQUIRED, or BLOCKED
→ Human Owner accepts, authorizes one exact correction, or rejects
→ accepted work is recorded as LOCKED_ACCEPTED in CODE RED
```

A file or stage accepted through ChatGPT exact-diff review and human decision becomes `LOCKED_ACCEPTED`.

Direct `main` writes, force push, automatic merge, broad deletion, workflow/secret changes, unrestricted tokens, and ambiguous automatic retries are prohibited.

## Repository cleanup rule

Repository cleanup must follow CODE RED.

```text
inventory
→ classify every file by purpose and authority
→ prove exact duplicate or unreferenced generated junk
→ migrate references
→ preserve unique historical evidence
→ run checks
→ obtain human deletion authorization
→ delete
→ verify no broken references
→ record deletion in CODE RED
```

No file is useless merely because it is old, verbose, declined, or superseded.

## Current exact stage

```yaml
current_stage: LOCAL_STATE_RECOVERY_AND_CODE_RED_SYNCHRONIZATION_REQUIRED
safe_to_continue_implementation: false
remote_research_head_at_CODE_RED_activation: b6ce572107d197cfbb47e7e8fbe101517f58e8d2
remote_implementation_head: bafb230a995744743af5c0bdd612ad1e7c7568ae
last_reported_local_head: 867f82ab0252b27c3f876d29901274140ef1b18c
local_state_after_keyboard_incident: UNVERIFIED
```

Exact next evidence required:

```powershell
git branch --show-current
git rev-parse HEAD
git status --short
```

Do not run pull, sync, merge, rebase, reset, clean, push, or resume Phase 2A implementation until local state is verified and the exact safe synchronization plan is approved.

## Minimum gate before full build

```text
1. Recover and verify local state.
2. Synchronize canonical governance updates safely.
3. Implement and validate strict Foundation models, statuses, ledger, hashes, persistence, and blockers.
4. Implement explicit Flow routers and stop routes.
5. Implement Flow-owned RepositoryPreflightTool invocation and deterministic executor.
6. Implement Agent 01 as a zero-tool, one-LLM-call evaluator.
7. Keep LLM profiles disabled until exact readiness tests and human approval pass.
8. Keep offline permission declaration separate from live GitHub evidence.
9. Implement deterministic HumanReviewRequest and authenticated pause/resume contract.
10. Pass unit, contract, security, integration, and applicable live tests.
11. Complete controlled external contributor trials.
12. Only then research and implement Agents 02–15 one at a time.
```

## Current authorization boundary

```yaml
main_write: prohibited
force_push: prohibited
merge: prohibited
deployment: prohibited
workflow_or_secret_change: prohibited
custom_Cline_bridge: deferred
custom_MCP_bridge: prohibited_now
Agents_02_to_15: prohibited
production_ready_claim: prohibited
```
