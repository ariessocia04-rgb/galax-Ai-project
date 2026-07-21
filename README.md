# Galax AI Project

Galax AI is being designed as a fact-checked, strictly sequential CrewAI multi-agent software-development assistant system.

## Current phase

The repository is in planning, research, conflict-reconciliation, and minimum-runtime validation mode. Agent roles, tools, LLMs, prompts, knowledge, memory, Docker infrastructure, contributor workflows, and execution behavior are not operational until individually implemented, tested, audited, and approved.

## Current readiness decision

```yaml
full_build_prompt_status: BLOCKED_NOT_READY_TO_PROMPT_CREWAI
current_master_prompt_status: DO_NOT_USE_STALE_CONFLICTS
Foundation_Agent01_Flow_contract: ACTIVE_CANONICAL
chat_continuity_protocol: ACTIVE_CANONICAL
Foundation_repository_implementation: NOT_PERFORMED
full_free_runtime_proven: false
agents_enabled: 0
external_contributors_fully_qualified: 0
production_ready: false
```

Do not execute the complete 15-agent build prompt. The architecture is technically possible, but the exact CrewAI, LLM, GitHub/Drive/memory gateways, permission evidence, Docker/sandbox, and sequential runtime chain has not passed the required integration and live tests.

## Canonical current records

- `docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md`
- `docs/research/readiness/FINAL_PRE_PROMPT_CONFLICT_AUDIT_2026-07-20.md`
- the canonical audit target named by that alias
- `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`
- `docs/research/crewai/CREWAI_1_15_4_FULL_AGENT_REMEDIATION_BLUEPRINT_2026-07-20.md`
- `docs/plan/LLM_ASSIGNMENT_PLAN_DRAFT.md`
- `docs/sources/SOURCE_INDEX.md`
- `docs/plan/EXTERNAL_AI_CONTRIBUTOR_EXECUTION_PLAN_DRAFT.md`
- `docs/prompts/EXTERNAL_AI_CONTRIBUTOR_COMMAND_PACK.md`

## Conversation-length continuity trigger

When the owner says `length chat problem`, `conversation length problem`, `continue exact Galax flow`, `operation length problem solve`, or a close spelling variation:

```text
read AGENTS.md
→ read docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md
→ verify repository, branch heads, PR, and assignment issues
→ reconstruct the exact current stage
→ produce OPERATION_LENGTH_CONTINUITY_RECEIPT
→ answer or act only when safe_to_continue=true
```

Do not ask the owner what the previous work was when repository access exists. Do not rely on old chat memory or summaries as repository truth.

## Canonical decision priority

```text
README current readiness
→ canonical chat-continuity protocol
→ canonical conflict audit and alias target
→ Foundation and Agent 01 Flow execution contract
→ full CrewAI 1.15.4 remediation blueprint
→ active rules and plans
→ validated LLM routing and assignment
→ source index and exact source cards
→ exact authorized assignment
→ historical research
→ old chat memory or summaries
```

The active Flow execution contract supersedes only older instructions that attach `RepositoryPreflightTool` directly to Agent 01, require an Agent 01 direct tool call, or use `result_as_answer` for that path.

Historical files remain evidence. They cannot reactivate Cerebras, Notion-primary runtime memory, generic MCP exposure, CrewAI planning/reasoning/native memory, hierarchical delegation, direct-main writes, automatic merge, privileged Docker-in-Docker, or the superseded direct Agent 01 preflight-tool architecture.

## Required reading order

Before changing or implementing any agent, LLM, tool, prompt, knowledge source, memory behavior, infrastructure, contributor workflow, or runtime:

1. Read `README.md`.
2. Read `AGENTS.md`.
3. Read `docs/operations/OPERATIION_LENGTH_PROBLEM_SOLVE.md`.
4. Read the canonical conflict audit and alias target.
5. Read `docs/plan/FOUNDATION_AGENT01_FLOW_EXECUTION_CONTRACT_2026-07-21.md`.
6. Read the full CrewAI 1.15.4 remediation blueprint.
7. Read all applicable files under `docs/rules/` and `docs/plan/`.
8. Read `docs/sources/SOURCE_INDEX.md` and exact source cards.
9. Read the applicable agent research and exact authorized assignment.
10. Verify current external facts using authoritative sources and pinned source/adapters.
11. Inspect current official issues and security notices when documentation is insufficient.
12. Define and pass tests in the exact pinned environment.
13. Only then execute a human-authorized bounded change.

A repository-aware contributor must produce `REPOSITORY_READ_RECEIPT` before editing. A conversation-length trigger additionally requires `OPERATION_LENGTH_CONTINUITY_RECEIPT`.

## Meaning of 100% fact-checked

Galax does not promise perfect AI behavior. The permitted statement is:

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
+ exact zero-or-one direct role interface according to the active contract
+ trusted Flow/application dependencies when external actions are not agent-owned
+ permissions and data classification
+ deterministic routers and stage ordering
+ knowledge and memory context when required
+ Docker/sandbox boundary when required
+ hooks or governed executors, guardrails, invocation evidence, and checkpoint
+ deterministic and applicable live tests
+ human approval when required
```

Agent 01 is the current explicit zero-direct-tool evaluator exception:

```yaml
RepositoryPreflightTool_owner: GalaxFoundationFlow
RepositoryPreflightTool_calls: 1
engineering_manager_tools: []
Agent_01_direct_tools: 0
Agent_01_LLM_calls: 1
result_as_answer_for_this_path: prohibited
HumanReviewRequest: pure_Python_Pydantic
```

If any layer is missing, incompatible, or unverified:

```text
STATUS: BLOCKED_UNSUPPORTED_CAPABILITY
```

The system must not simulate success, fabricate tool output, invent missing evidence, or claim content was studied when it was not retrieved.

## Exact-duplicate rule

Exact normalized duplicates are reduced to one canonical record only after every reference is updated and removal is safely verified. Similar records with materially different roles, permissions, inputs, outputs, workflow stages, decisions, or historical evidence remain.

No historical file was deleted merely because a newer record superseded part of it.

## Current CrewAI direction

```yaml
framework_candidate: CrewAI_1.15.4
python_candidate: '>=3.10,<3.14'
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

### Why planning and reasoning are disabled

- CrewAI `planning=True` adds another planning model call and may introduce an unapproved provider and wider prompt exposure.
- CrewAI `reasoning=True` adds a separate refinement loop and is not the selected fail-closed planning boundary.
- CrewAI native memory is not the selected source of truth.
- Galax uses explicit typed tasks, provider-native reasoning settings only after profile testing, and deterministic Flow validation.

## Foundation and Agent 01 final sequence

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

```yaml
repository_preflight_tool_calls: 1
Agent_01_LLM_calls: 1
Agent_01_direct_tools: 0
hidden_second_agent_call: prohibited
unconditional_listen_chain: prohibited
merge: prohibited
deployment: prohibited
Agents_02_to_15: disabled
```

Every blocked, failed, unavailable, pending, rejected, or evidence-missing route must stop or pause. It cannot trigger the next successful stage.

## Governance and evidence direction

Trusted application code must enforce model/profile readiness, governed external invocation, strict typed results, evidence validation, routing, persistence, and human-review state.

An LLM cannot claim an external action ran without trusted invocation evidence. Narrative `Action`, `Observation`, `test passed`, `file written`, or `commit created` is not proof.

`RepositoryPreflightTool` is offline and read-only. It verifies `REPO_PERMISSION_PROFILE_DECLARED` only. Live GitHub identity and permissions require separate trusted `GITHUB_PERMISSIONS_LIVE_VALIDATED` evidence from `GitHubRepositoryGateway`.

Both Agent 01 LLM profiles remain disabled until the exact profile tests and human approval pass. Missing profile readiness returns `BLOCKED_LLM_PROFILE_NOT_APPROVED` before token use.

## GitHub repository direction

The official GitHub MCP Server and GitHub APIs provide repository operations, but Galax does not expose a broad tool catalog directly to an agent.

A future bounded write transaction requires:

```text
trusted Flow/application gateway
→ exact repository and branch
→ expected-head and path/hash verification
→ force=false update
→ post-write commit/diff verification
→ invocation evidence
→ QA/security/audit
→ human-controlled draft PR and later merge decision
```

Direct writes to `main`, force push, automatic merge, broad deletion, workflow/secret changes, unrestricted tokens, and ambiguous automatic write retries are prohibited.

## MCP security direction

```yaml
generic_remote_MCP: prohibited
arbitrary_URL_MCP_tools: prohibited
full_MCP_tool_catalog_to_agents: prohibited
direct_agent_to_agent_MCP_mesh: prohibited
local_role_scoped_gateway: required_for_future_use
URL_domain_and_IP_validation: required
private_link_local_metadata_IPs: blocked
write_retry: zero_automatic_retries
```

## Corrected LLM direction

```yaml
bounded_private_primary: groq/openai/gpt-oss-20b
bounded_hosted_fallback: cloudflare/@cf/openai/gpt-oss-20b
high_complexity_private_primary: groq/openai/gpt-oss-120b
high_complexity_hosted_fallback: cloudflare/@cf/openai/gpt-oss-120b
public_redacted_long_context: gemini/gemini-2.5-flash
optional_local_fallback: ollama/gpt-oss:20b
rejected_trial_only: cerebras/gpt-oss-120b
all_profiles: DISABLED_PENDING_EXACT_TESTS
```

Provider switching is deterministic Flow behavior only, after independent approval and a safe checkpoint. It is prohibited during non-idempotent operations.

## External development contributors

Selected for controlled trial only:

| Contributor | Paper score | Exact role |
|---|---:|---|
| Cline | 86 | Primary supervised Foundation implementer |
| OpenHands Core | 84 | Docker-isolated fallback reproducer |
| mini-SWE-agent | 83 | Isolated patch comparator |
| Aider | 82 | Surgical exact-failure fixer |
| PR-Agent | 82 | Read-only stable PR reviewer |

Declined or deferred:

| Contributor | Paper score | Decision |
|---|---:|---|
| OpenCode | 74 | Declined: security boundary not proven |
| goose | 77 | Declined now: scope too broad and role duplication; research later |

The five selected tools are not fully qualified, installed, connected, or authorized for production. They are not Galax Agents 01–15.

```text
Cline plan and bounded implementation
→ optional Aider exact repair
→ optional mini-SWE isolated comparison
→ optional OpenHands blocker reproduction
→ PR-Agent read-only review
→ human decision
```

Stages are conditional and sequential. Simultaneous overlapping writers are prohibited.

## Knowledge, memory, Docker, and sandbox direction

- Approved Google Drive folders are future controlled knowledge sources through a bounded gateway and `LearningPacket`/`StudyReceipt` evidence.
- Supabase/Postgres is the selected primary machine/runtime memory candidate; Notion is an optional curated mirror.
- GitHub/current evidence outranks memory.
- CrewAI native memory remains disabled.
- Application services may use hardened Docker Compose.
- Coding/test execution requires a separate rootless sandbox boundary.
- Privileged Docker-in-Docker and unrestricted Docker socket mounts are prohibited.
- These gateways and sandbox components remain unimplemented or untested unless exact evidence states otherwise.

## Minimum gate before full build

```text
1. Reconcile active conflicts and keep the old full master prompt blocked.
2. Pin the exact Foundation dependency set.
3. Implement strict models, statuses, ledger, hashes, persistence, and blockers.
4. Implement explicit Flow routers and stop routes.
5. Implement Flow-owned RepositoryPreflightTool invocation and its deterministic executor.
6. Implement Agent 01 as a zero-tool, one-LLM-call evaluator.
7. Implement LLM profile readiness and keep profiles disabled until tested.
8. Separate offline permission declaration from live GitHub permission evidence.
9. Implement deterministic HumanReviewRequest and authenticated pause/resume contract.
10. Pass unit, contract, security, integration, and applicable live tests.
11. Complete controlled external contributor trials.
12. Only then research and implement Agents 02–15 one at a time.
```

## Current next action

```yaml
next_scope: Governance_Foundation_and_Agent_01_only
next_environment: repository_aware_coding_agent
next_contributor_stage: Cline_plan_only
implementation_branch: implementation/foundation-agent-01
commit_or_push_authorized: false_until_separate_human_approval
full_master_prompt: still_blocked
```

The Foundation plan is finalized for bounded coding handoff. It is not operational, implemented, live-tested, runtime-approved, merged, deployed, or production-ready.
